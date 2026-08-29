#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MATERIALIZER = ROOT / "analista/calibracion/materializar_oro_formulas_fase10.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"No se pudo cargar {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def detection_key(item: dict) -> tuple:
    return (
        item["tipo_registro"],
        item["unidad_id"],
        item["texto_literal"],
        item["linea_inicio"],
        item["linea_fin"],
    )


def metrics(gold: list[dict], predicted: list[dict], units: set[str]) -> dict:
    gold_counter = Counter(detection_key(item) for item in gold)
    pred_counter = Counter(detection_key(item) for item in predicted)
    intersection = gold_counter & pred_counter
    tp = sum(intersection.values())
    fp = sum((pred_counter - gold_counter).values())
    fn = sum((gold_counter - pred_counter).values())
    precision = None if tp + fp == 0 else tp / (tp + fp)
    recall = None if tp + fn == 0 else tp / (tp + fn)

    gold_by_key: dict[tuple, list[dict]] = defaultdict(list)
    pred_by_key: dict[tuple, list[dict]] = defaultdict(list)
    for item in gold:
        gold_by_key[detection_key(item)].append(item)
    for item in predicted:
        pred_by_key[detection_key(item)].append(item)

    class_total = class_ok = 0
    for key, count in intersection.items():
        for expected, actual in zip(gold_by_key[key][:count], pred_by_key[key][:count]):
            if expected.get("clasificacion") is not None:
                class_total += 1
                class_ok += int(expected["clasificacion"] == actual.get("clasificacion"))

    return {
        "unidades_revisadas": len(units),
        "positivos_esperados": sum(gold_counter.values()),
        "predicciones_emitidas": sum(pred_counter.values()),
        "verdaderos_positivos": tp,
        "falsos_positivos": fp,
        "falsos_negativos": fn,
        "precision": precision,
        "cobertura": recall,
        "clasificaciones_correctas": class_ok,
        "clasificaciones_evaluables": class_total,
        "exactitud_clasificacion": None if class_total == 0 else class_ok / class_total,
    }


def evaluate(*, policy: Path, generated_root: Path, units: Path, schema: Path) -> dict:
    materializer = load_module("fase10_materializer_formulas", MATERIALIZER)
    raw_gold = materializer.materialize(
        policy_path=policy,
        units_path=units,
        schema_path=schema,
    )
    gold_entries = [json.loads(line) for line in raw_gold.decode("utf-8").splitlines() if line]
    obra_id = gold_entries[0]["obra_id"] if gold_entries else None
    if not obra_id:
        raise SystemExit("Patrón manual vacío")

    predicted_records = load_jsonl(generated_root / "formulas-candidatas.jsonl")
    predicted: list[dict] = []
    for record in predicted_records:
        predicted.append(
            {
                "tipo_registro": "formula",
                "unidad_id": record["unidad_id"],
                "texto_literal": record["texto_literal"],
                "linea_inicio": record["localizacion"]["linea_inicio"],
                "linea_fin": record["localizacion"]["linea_fin"],
                "clasificacion": record["clasificacion_formula"],
            }
        )

    result = {
        "version": "1.0.0",
        "obra_id": obra_id,
        "motor": "formulas",
        "patron_manual_sha256": hashlib.sha256(raw_gold).hexdigest(),
        "producto_evaluado_sha256": sha(generated_root / "formulas-candidatas.jsonl"),
        "estratos": {},
    }
    for stratum in ("general", "desafio"):
        unit_ids = {entry["unidad_id"] for entry in gold_entries if stratum in entry["estratos"]}
        gold: list[dict] = []
        for entry in gold_entries:
            if entry["unidad_id"] not in unit_ids:
                continue
            for item in entry["items_esperados"]:
                gold.append({**item, "unidad_id": entry["unidad_id"]})
        pred = [item for item in predicted if item["unidad_id"] in unit_ids]
        result["estratos"][stratum] = metrics(gold, pred, unit_ids)
    return result


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--politica", type=Path, required=True)
    ap.add_argument("--generated-root", type=Path, required=True)
    ap.add_argument("--unidades", type=Path, default=ROOT / "analista/generado/unidades.jsonl")
    ap.add_argument("--schema", type=Path, default=ROOT / "analista/calibracion/patron-oro-obra-v1.1.0.schema.json")
    ap.add_argument("--salida", type=Path)
    args = ap.parse_args()
    result = evaluate(
        policy=args.politica,
        generated_root=args.generated_root,
        units=args.unidades,
        schema=args.schema,
    )
    raw = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    if args.salida:
        args.salida.parent.mkdir(parents=True, exist_ok=True)
        args.salida.write_text(raw, encoding="utf-8")
    print(raw, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
