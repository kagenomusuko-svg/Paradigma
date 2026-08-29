#!/usr/bin/env python3
"""Validador mecánico del patrón de oro manual de Fase 8.

No decide qué debería decir el corpus. Comprueba únicamente que cada anotación
manual pertenece a la muestra congelada, usa categorías contractuales y apunta
a evidencia literal existente en la fuente canónica.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
PILOTO_ID = "AA-SP-V1"
DEFAULT_GOLD = ROOT / "analista/calibracion/patron-oro.jsonl"
DEFAULT_SCHEMA = ROOT / "analista/calibracion/patron-oro-v1.0.0.schema.json"
DEFAULT_LOCK = ROOT / "analista/calibracion/muestra-fase8.lock.json"
DEFAULT_UNITS = ROOT / "analista/generado/unidades.jsonl"
DEFAULT_CORPUS = ROOT

MOTOR_TYPES = {
    "conceptos_apariciones": {"aparicion_conceptual", "concepto"},
    "definiciones": {"definicion"},
    "afirmaciones": {"afirmacion"},
    "formulas": {"formula"},
    "relaciones_explicitas": {"relacion_explicita"},
    "limitadores": {"distincion", "negacion", "excepcion", "restriccion_alcance"},
}
CLASS_ALLOWED = {
    "aparicion_conceptual": {"candidato", "extraido"},
    "concepto": {"no_determinada", "establecida_por_evidencia"},
    "definicion": {"definicion_candidata", "definicion_explicita"},
    "afirmacion": {"afirmacion_candidata", "afirmacion_explicita"},
    "formula": {"formula_candidata", "formula_explicita"},
    "relacion_explicita": {"relacion_candidata", "relacion_explicita"},
    "distincion": {"distincion_candidata", "distincion_explicita"},
    "negacion": {"negacion_candidata", "negacion_explicita"},
    "excepcion": {"excepcion_candidata", "excepcion_explicita"},
    "restriccion_alcance": {"restriccion_candidata", "restriccion_explicita"},
}
STATUS_ALLOWED = {
    "afirmacion_autoral",
    "negacion_autoral",
    "cita",
    "discurso_referido",
    "objecion",
    "hipotesis",
    "ejemplo",
    "pregunta",
    "definicion",
    "formulacion_condicional",
    "caso_contrafactico",
    "no_determinado",
}


def load_jsonl(path: Path) -> list[dict]:
    if not path.is_file():
        raise SystemExit(f"No existe insumo requerido: {path}")
    rows: list[dict] = []
    for number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        try:
            rows.append(json.loads(raw))
        except json.JSONDecodeError as exc:
            raise SystemExit(f"JSONL inválido en {path}:{number}: {exc}") from exc
    return rows


def canonical_excerpt(corpus_root: Path, route: str, start: int, end: int) -> str:
    path = corpus_root / route
    if not path.is_file():
        raise AssertionError(f"Fuente canónica inexistente: {route}")
    lines = path.read_text(encoding="utf-8").splitlines()
    if not 1 <= start <= end <= len(lines):
        raise AssertionError(f"Rango fuera de fuente {route}:{start}-{end}")
    return "\n".join(lines[start - 1 : end])


def validate_paths(
    *,
    gold: Path,
    schema: Path,
    lock: Path,
    units: Path,
    corpus_root: Path,
) -> dict:
    schema_doc = json.loads(schema.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema_doc)
    lock_doc = json.loads(lock.read_text(encoding="utf-8"))
    if lock_doc.get("obra_id") != PILOTO_ID:
        raise AssertionError(f"Lock no corresponde a {PILOTO_ID}")

    unit_rows = load_jsonl(units)
    pilot_units = {row["id"]: row for row in unit_rows if row.get("fuente_id") == PILOTO_ID}
    if not pilot_units:
        raise AssertionError(f"No hay unidades para {PILOTO_ID}")

    frozen = set(lock_doc["desafios"]["general"])
    for motor in MOTOR_TYPES:
        frozen.update(lock_doc["desafios"][motor])

    rows = load_jsonl(gold)
    seen_entries: set[tuple[str, str]] = set()
    seen_items: set[tuple] = set()
    total_items = 0

    for number, row in enumerate(rows, start=1):
        errors = sorted(validator.iter_errors(row), key=lambda error: list(error.path))
        if errors:
            raise AssertionError(f"Fila {number} fuera de esquema: {errors[0].message}")

        entry_key = (row["unidad_id"], row["motor"])
        if entry_key in seen_entries:
            raise AssertionError(f"Anotación duplicada unidad–motor: {entry_key}")
        seen_entries.add(entry_key)

        unit_id = row["unidad_id"]
        motor = row["motor"]
        if unit_id not in frozen:
            raise AssertionError(f"Unidad fuera del lock de Fase 8: {unit_id}")
        if unit_id not in pilot_units:
            raise AssertionError(f"Unidad desconocida del piloto: {unit_id}")
        if "general" in row["estratos"] and unit_id not in lock_doc["desafios"]["general"]:
            raise AssertionError(f"{unit_id} marcado general sin pertenecer al estrato general")
        if "desafio" in row["estratos"] and unit_id not in lock_doc["desafios"][motor]:
            raise AssertionError(f"{unit_id} marcado desafío sin pertenecer al desafío de {motor}")

        unit = pilot_units[unit_id]
        unit_start = unit["localizacion"]["linea_inicio"]
        unit_end = unit["localizacion"]["linea_fin"]
        route = unit["archivo"]

        for item in row["items_esperados"]:
            total_items += 1
            kind = item["tipo_registro"]
            if kind not in MOTOR_TYPES[motor]:
                raise AssertionError(f"{kind} no pertenece al motor {motor}")

            classification = item.get("clasificacion")
            if classification is not None and classification not in CLASS_ALLOWED[kind]:
                raise AssertionError(f"Clasificación inválida para {kind}: {classification}")
            status = item.get("estatus_enunciativo")
            if status is not None and status not in STATUS_ALLOWED:
                raise AssertionError(f"Estatus enunciativo inválido: {status}")
            if kind == "definicion" and classification == "definicion_explicita" and status != "definicion":
                raise AssertionError("Una definición explícita manual debe conservar estatus 'definicion'")

            start = item["linea_inicio"]
            end = item["linea_fin"]
            if start > end:
                raise AssertionError(f"Rango invertido {unit_id}:{start}-{end}")
            if not unit_start <= start <= unit_end:
                raise AssertionError(
                    f"Ítem no anclado en su unidad: {unit_id} inicia {start}; unidad={unit_start}-{unit_end}"
                )

            excerpt = canonical_excerpt(corpus_root, route, start, end)
            literal = item["texto_literal"]
            if not literal:
                raise AssertionError(f"Literal vacío en {unit_id}/{motor}")
            position = excerpt.find(literal)
            if position < 0:
                raise AssertionError(f"Literal no coincide con fuente {route}:{start}-{end}")
            before = excerpt[:position]
            after = excerpt[position + len(literal) :]
            if "\n" in before:
                raise AssertionError(f"Inicio declarado demasiado temprano en {unit_id}:{start}-{end}")
            if "\n" in after:
                raise AssertionError(f"Fin declarado demasiado tarde en {unit_id}:{start}-{end}")

            detection_identity = (
                kind,
                unit_id,
                literal,
                start,
                end,
                item.get("concepto_designacion"),
                item.get("sujeto_designacion"),
                item.get("objeto_designacion"),
                item.get("termino_a_literal"),
                item.get("termino_b_literal"),
                item.get("objeto_negado_literal"),
                item.get("fragmento_literal"),
            )
            if detection_identity in seen_items:
                raise AssertionError(f"Ítem manual duplicado: {detection_identity[:5]}")
            seen_items.add(detection_identity)

    return {
        "revisiones": len(rows),
        "items": total_items,
        "motores": sorted({row["motor"] for row in rows}),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--patron", type=Path, default=DEFAULT_GOLD)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--lock", type=Path, default=DEFAULT_LOCK)
    parser.add_argument("--unidades", type=Path, default=DEFAULT_UNITS)
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    args = parser.parse_args()
    result = validate_paths(
        gold=args.patron,
        schema=args.schema,
        lock=args.lock,
        units=args.unidades,
        corpus_root=args.corpus,
    )
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
