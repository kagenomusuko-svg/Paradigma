#!/usr/bin/env python3
"""Evalúa extractores contra anotaciones manuales de Fase 8.

La métrica de detección se separa de clasificación, estatus e identidad. La
muestra general, los desafíos y el combinado se informan por separado; el
combinado deduplica cada par unidad–motor. Por defecto el patrón de oro se carga
solo desde el manifiesto versionado y únicamente se abren salidas de motores que
ya tienen anotaciones manuales.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_GENERATED = ROOT / "analista/generado"
DEFAULT_MANIFEST = ROOT / "analista/calibracion/patron-oro-manifiesto.json"
DEFAULT_OUTPUT = ROOT / "analista/generado/reporte-calibracion.json"
PILOTO_ID = "AA-SP-V1"
REPORT_VERSION = "1.1.0"

MOTOR_FILES = {
    "conceptos_apariciones": ["apariciones-conceptuales.jsonl", "conceptos.jsonl"],
    "definiciones": ["definiciones.jsonl"],
    "afirmaciones": ["afirmaciones-candidatas.jsonl"],
    "formulas": ["formulas-candidatas.jsonl"],
    "relaciones_explicitas": ["relaciones-explicitas.jsonl"],
    "limitadores": ["distinciones.jsonl", "negaciones.jsonl", "excepciones.jsonl", "restricciones-alcance.jsonl"],
}
CLASS_FIELDS = {
    "aparicion_conceptual": None,
    "concepto": "estado_identidad_conceptual",
    "definicion": "clasificacion_definicion",
    "afirmacion": "clasificacion_afirmacion",
    "formula": "clasificacion_formula",
    "relacion_explicita": "clasificacion_relacion",
    "distincion": "clasificacion_distincion",
    "negacion": "clasificacion_negacion",
    "excepcion": "clasificacion_excepcion",
    "restriccion_alcance": "clasificacion_restriccion",
}
LABEL_FIELDS = (
    "clasificacion",
    "estatus_enunciativo",
    "concepto_designacion",
    "sujeto_designacion",
    "objeto_designacion",
    "termino_a_literal",
    "termino_b_literal",
    "objeto_negado_literal",
    "fragmento_literal",
)


def load_jsonl(path: Path) -> list[dict]:
    if not path.is_file():
        raise SystemExit(f"No existe insumo requerido para calibración: {path}")
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def manifest_files(path: Path) -> list[Path]:
    if not path.is_file():
        raise SystemExit(f"No existe manifiesto de patrón de oro: {path}")
    doc = json.loads(path.read_text(encoding="utf-8"))
    if doc.get("version") != "1.0.0" or doc.get("obra_id") != PILOTO_ID:
        raise SystemExit("Manifiesto de patrón de oro incompatible")
    names = doc.get("archivos")
    if not isinstance(names, list) or not names or len(names) != len(set(names)):
        raise SystemExit("El manifiesto debe declarar archivos únicos y no vacíos")
    root = path.parent.resolve()
    files: list[Path] = []
    for name in names:
        if not isinstance(name, str) or not name.endswith(".jsonl"):
            raise SystemExit(f"Entrada inválida en manifiesto: {name!r}")
        candidate = (path.parent / name).resolve()
        try:
            candidate.relative_to(root)
        except ValueError as exc:
            raise SystemExit(f"Ruta fuera del directorio de calibración: {name}") from exc
        if not candidate.is_file():
            raise SystemExit(f"Archivo de patrón declarado pero inexistente: {name}")
        files.append(candidate)
    return files


def load_manifest(path: Path) -> list[dict]:
    rows: list[dict] = []
    for gold_file in manifest_files(path):
        rows.extend(load_jsonl(gold_file))
    return rows


def blank_item() -> dict:
    return {field: None for field in LABEL_FIELDS}


def load_concepts(root: Path) -> dict[str, dict]:
    return {row["id"]: row for row in load_jsonl(root / "conceptos.jsonl")}


def extracted_items(root: Path, motor: str) -> list[dict]:
    if motor not in MOTOR_FILES:
        raise SystemExit(f"Motor de calibración desconocido: {motor}")

    concepts: dict[str, dict] = {}
    appearances: dict[str, dict] = {}
    if motor in {"conceptos_apariciones", "definiciones", "relaciones_explicitas"}:
        concepts = load_concepts(root)
    if motor == "conceptos_apariciones":
        appearances = {
            row["id"]: row for row in load_jsonl(root / "apariciones-conceptuales.jsonl")
        }

    output: list[dict] = []
    for filename in MOTOR_FILES[motor]:
        for record in load_jsonl(root / filename):
            kind = record["tipo_registro"]
            item = blank_item()
            item["tipo_registro"] = kind

            if kind == "concepto":
                evidence = record.get("evidencia_identidad_ids", [])
                if not evidence or evidence[0] not in appearances:
                    continue
                appearance = appearances[evidence[0]]
                item["unidad_id"] = appearance["unidad_id"]
                location = appearance["localizacion"]
                item["texto_literal"] = record.get("texto_literal") or record["designacion_operativa"]
                item["concepto_designacion"] = record["designacion_operativa"]
            else:
                item["unidad_id"] = record.get("unidad_id")
                location = record.get("localizacion")
                item["texto_literal"] = record.get("texto_literal") or ""

            if not item.get("unidad_id") or not location:
                continue
            item["linea_inicio"] = location["linea_inicio"]
            item["linea_fin"] = location["linea_fin"]

            class_field = CLASS_FIELDS[kind]
            item["clasificacion"] = (
                record.get(class_field)
                if class_field
                else record.get("estado_extraccion") if kind == "aparicion_conceptual" else None
            )
            item["estatus_enunciativo"] = record.get("estatus_enunciativo")

            if kind == "aparicion_conceptual" and record.get("concepto_id") in concepts:
                item["concepto_designacion"] = concepts[record["concepto_id"]]["designacion_operativa"]
            elif kind == "definicion" and record.get("concepto_id") in concepts:
                item["concepto_designacion"] = concepts[record["concepto_id"]]["designacion_operativa"]
            elif kind == "relacion_explicita":
                subject = record.get("sujeto_ref")
                obj = record.get("objeto_ref")
                if subject not in concepts or obj not in concepts:
                    raise SystemExit(f"Relación con referente conceptual inexistente: {record.get('id')}")
                item["sujeto_designacion"] = concepts[subject]["designacion_operativa"]
                item["objeto_designacion"] = concepts[obj]["designacion_operativa"]
            elif kind == "distincion":
                item["termino_a_literal"] = record.get("termino_a_literal")
                item["termino_b_literal"] = record.get("termino_b_literal")
            elif kind == "negacion":
                item["objeto_negado_literal"] = record.get("objeto_negado_literal")
            elif kind == "excepcion":
                item["fragmento_literal"] = record.get("fragmento_exceptivo_literal")
            elif kind == "restriccion_alcance":
                item["fragmento_literal"] = record.get("fragmento_restriccion_literal")

            output.append(item)
    return output


def detection_key(item: dict) -> tuple:
    key = [
        item["tipo_registro"],
        item["unidad_id"],
        item["texto_literal"],
        item["linea_inicio"],
        item["linea_fin"],
    ]
    kind = item["tipo_registro"]
    if kind in {"concepto", "definicion"}:
        key.append(item.get("concepto_designacion"))
    elif kind == "relacion_explicita":
        key.extend([item.get("sujeto_designacion"), item.get("objeto_designacion")])
    elif kind == "distincion":
        key.extend([item.get("termino_a_literal"), item.get("termino_b_literal")])
    elif kind == "negacion":
        key.append(item.get("objeto_negado_literal"))
    elif kind in {"excepcion", "restriccion_alcance"}:
        key.append(item.get("fragmento_literal"))
    return tuple(key)


def flatten_gold(entries: list[dict]) -> list[dict]:
    output: list[dict] = []
    for entry in entries:
        for source in entry["items_esperados"]:
            item = dict(source)
            item["unidad_id"] = entry["unidad_id"]
            output.append(item)
    return output


def metrics(gold: list[dict], predicted: list[dict], units: set[str]) -> dict:
    gold_counter = Counter(detection_key(item) for item in gold)
    predicted_counter = Counter(detection_key(item) for item in predicted)
    intersection = gold_counter & predicted_counter
    expected_positives = sum(gold_counter.values())
    emitted_predictions = sum(predicted_counter.values())
    true_positive = sum(intersection.values())
    false_positive = sum((predicted_counter - gold_counter).values())
    false_negative = sum((gold_counter - predicted_counter).values())

    precision = None if true_positive + false_positive == 0 else true_positive / (true_positive + false_positive)
    recall = None if true_positive + false_negative == 0 else true_positive / (true_positive + false_negative)

    gold_by_key: dict[tuple, list[dict]] = defaultdict(list)
    predicted_by_key: dict[tuple, list[dict]] = defaultdict(list)
    for item in gold:
        gold_by_key[detection_key(item)].append(item)
    for item in predicted:
        predicted_by_key[detection_key(item)].append(item)

    class_total = class_ok = status_total = status_ok = identity_total = identity_ok = 0
    for key, count in intersection.items():
        for expected, actual in zip(gold_by_key[key][:count], predicted_by_key[key][:count]):
            if expected.get("clasificacion") is not None:
                class_total += 1
                class_ok += int(expected.get("clasificacion") == actual.get("clasificacion"))
            if expected.get("estatus_enunciativo") is not None:
                status_total += 1
                status_ok += int(expected.get("estatus_enunciativo") == actual.get("estatus_enunciativo"))
            if expected["tipo_registro"] == "aparicion_conceptual" and expected.get("concepto_designacion") is not None:
                identity_total += 1
                identity_ok += int(expected.get("concepto_designacion") == actual.get("concepto_designacion"))

    return {
        "positivos_esperados": expected_positives,
        "predicciones_emitidas": emitted_predictions,
        "precision": precision,
        "cobertura": recall,
        "verdaderos_positivos": true_positive,
        "falsos_positivos": false_positive,
        "falsos_negativos": false_negative,
        "unidades_procesadas": len(units),
        "clasificaciones_evaluadas": class_total,
        "clasificaciones_correctas": class_ok,
        "exactitud_clasificacion": None if class_total == 0 else class_ok / class_total,
        "estatus_evaluados": status_total,
        "estatus_correctos": status_ok,
        "exactitud_estatus": None if status_total == 0 else status_ok / status_total,
        "identidades_evaluadas": identity_total,
        "identidades_correctas": identity_ok,
        "exactitud_identidad": None if identity_total == 0 else identity_ok / identity_total,
    }


def validate_entries(entries: list[dict]) -> list[str]:
    seen: set[tuple[str, str]] = set()
    motors: list[str] = []
    for entry in entries:
        key = (entry["unidad_id"], entry["motor"])
        if key in seen:
            raise SystemExit(f"Anotación duplicada unidad–motor: {key}")
        seen.add(key)
        motor = entry["motor"]
        if motor not in MOTOR_FILES:
            raise SystemExit(f"Motor de patrón desconocido: {motor}")
        if motor not in motors:
            motors.append(motor)
    return motors


def main() -> int:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--patron", type=Path, default=None, help="Evalúa un JSONL aislado")
    group.add_argument("--manifiesto", type=Path, default=None, help="Evalúa un manifiesto alternativo")
    parser.add_argument("--generado", type=Path, default=DEFAULT_GENERATED)
    parser.add_argument("--salida", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    if args.patron is not None:
        entries = load_jsonl(args.patron)
    else:
        entries = load_manifest(args.manifiesto or DEFAULT_MANIFEST)
    motors = validate_entries(entries)

    reports: list[dict] = []
    for motor in MOTOR_FILES:
        if motor not in motors:
            continue
        motor_entries = [entry for entry in entries if entry["motor"] == motor]
        predictions = extracted_items(args.generado, motor)
        for stratum in ("general", "desafio", "combinado"):
            selected = (
                motor_entries
                if stratum == "combinado"
                else [entry for entry in motor_entries if stratum in entry["estratos"]]
            )
            if not selected:
                continue
            unit_ids = {entry["unidad_id"] for entry in selected}
            gold = flatten_gold(selected)
            predicted = [item for item in predictions if item["unidad_id"] in unit_ids]
            reports.append(
                {
                    "version": REPORT_VERSION,
                    "obra_id": PILOTO_ID,
                    "motor": motor,
                    "estrato": stratum,
                    **metrics(gold, predicted, unit_ids),
                }
            )

    args.salida.parent.mkdir(parents=True, exist_ok=True)
    args.salida.write_text(
        json.dumps({"reportes": reports}, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"version": REPORT_VERSION, "reportes": len(reports), "motores": sorted({row["motor"] for row in reports})}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
