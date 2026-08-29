#!/usr/bin/env python3
"""Reproduce y verifica la muestra congelada de Fase 8."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
UNIDADES = ROOT / "analista/generado/unidades.jsonl"
GENERADO = ROOT / "analista/generado"
LOCK = ROOT / "analista/calibracion/muestra-fase8.lock.json"


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def rank(seed: str, ids: list[str]) -> list[str]:
    return sorted(ids, key=lambda item: hashlib.sha256(f"{seed}|{item}".encode()).hexdigest())


def diverse(seed: str, ids: set[str], n: int, units: dict[str, dict]) -> list[str]:
    ordered = rank(seed, list(ids))
    selected: list[str] = []
    files: set[str] = set()
    for unit_id in ordered:
        filename = units[unit_id]["archivo"]
        if filename not in files:
            selected.append(unit_id)
            files.add(filename)
            if len(selected) >= n:
                return selected
    for unit_id in ordered:
        if unit_id not in selected:
            selected.append(unit_id)
            if len(selected) >= n:
                break
    return selected


def unit_ids(root: Path, filename: str) -> set[str]:
    return {
        row["unidad_id"]
        for row in load_jsonl(root / filename)
        if row.get("unidad_id")
    }


def select(units_path: Path, generated_root: Path) -> dict:
    rows = load_jsonl(units_path)
    units = {row["id"]: row for row in rows if row.get("fuente_id") == "AA-SP-V1"}
    by_file: dict[str, list[dict]] = {}
    for row in units.values():
        by_file.setdefault(row["archivo"], []).append(row)

    general: list[str] = []
    for filename in sorted(by_file):
        candidates = [row["id"] for row in by_file[filename] if row["tipo_estructural"] == "parrafo"]
        if not candidates:
            candidates = [row["id"] for row in by_file[filename]]
        general.append(rank("general-file", candidates)[0])
    general.extend(rank("general-header", [row["id"] for row in units.values() if row["tipo_estructural"] == "encabezado"])[:5])
    general.extend(rank("general-sep", [row["id"] for row in units.values() if row["tipo_estructural"] == "separador"])[:3])
    general = list(dict.fromkeys(general))

    appearances = unit_ids(generated_root, "apariciones-conceptuales.jsonl")
    definitions = unit_ids(generated_root, "definiciones.jsonl")
    assertions = unit_ids(generated_root, "afirmaciones-candidatas.jsonl")
    formulas = unit_ids(generated_root, "formulas-candidatas.jsonl")
    relations = unit_ids(generated_root, "relaciones-explicitas.jsonl")
    distinctions = unit_ids(generated_root, "distinciones.jsonl")
    negations = unit_ids(generated_root, "negaciones.jsonl")
    exceptions = unit_ids(generated_root, "excepciones.jsonl")
    restrictions = unit_ids(generated_root, "restricciones-alcance.jsonl")

    challenges = {
        "conceptos_apariciones": diverse("4a", appearances, 10, units),
        "definiciones": sorted(definitions, key=lambda item: (units[item]["archivo"], units[item]["localizacion"]["linea_inicio"])),
        "afirmaciones": diverse("4c", assertions, 12, units),
        "formulas": sorted(formulas, key=lambda item: (units[item]["archivo"], units[item]["localizacion"]["linea_inicio"])),
        "relaciones_explicitas": sorted(relations),
        "limitadores": list(
            dict.fromkeys(
                sorted(exceptions | restrictions)
                + diverse("4f-dist", distinctions, 12, units)
                + diverse("4f-neg", negations - distinctions - exceptions - restrictions, 12, units)
            )
        ),
    }
    return {
        "version": "1.0.0",
        "obra_id": "AA-SP-V1",
        "selector": "sha256-stratified-v1",
        "general": general,
        "desafios": challenges,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--unidades", type=Path, default=UNIDADES)
    parser.add_argument("--generado", type=Path, default=GENERADO)
    parser.add_argument("--lock", type=Path, default=LOCK)
    args = parser.parse_args()

    generated = select(args.unidades, args.generado)
    locked = json.loads(args.lock.read_text(encoding="utf-8"))
    if generated != locked:
        raise SystemExit("La selección actual difiere de muestra-fase8.lock.json; la muestra no puede moverse durante calibración.")

    unique = set(generated["general"])
    for ids in generated["desafios"].values():
        unique.update(ids)
    print(
        json.dumps(
            {
                "lock_verificado": True,
                "unidades_unicas": len(unique),
                "general": len(generated["general"]),
                "desafios": {key: len(value) for key, value in generated["desafios"].items()},
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
