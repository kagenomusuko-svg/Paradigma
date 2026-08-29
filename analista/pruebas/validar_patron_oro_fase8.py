#!/usr/bin/env python3
"""Pruebas de cierre de infraestructura del patrón de oro de Fase 8."""
from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALIDADOR = ROOT / "analista/calibracion/validar_patron_oro.py"
MANIFEST = ROOT / "analista/calibracion/patron-oro-manifiesto.json"
SCHEMA = ROOT / "analista/calibracion/patron-oro-v1.0.0.schema.json"
LOCK = ROOT / "analista/calibracion/muestra-fase8.lock.json"
UNIDADES = ROOT / "analista/generado/unidades.jsonl"

spec = importlib.util.spec_from_file_location("validar_patron_oro", VALIDADOR)
if spec is None or spec.loader is None:
    raise SystemExit("No se pudo cargar el validador de Fase 8")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def load_gold() -> list[dict]:
    rows: list[dict] = []
    for path in mod.manifest_files(MANIFEST):
        rows.extend(mod.load_jsonl(path))
    return rows


def validate(path: Path) -> dict:
    return mod.validate_paths(
        gold=path,
        schema=SCHEMA,
        lock=LOCK,
        units=UNIDADES,
        corpus_root=ROOT,
    )


def expect_failure(rows: list[dict], expected: str) -> None:
    with tempfile.TemporaryDirectory() as td:
        path = Path(td) / "patron.jsonl"
        path.write_text(
            "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows),
            encoding="utf-8",
        )
        try:
            validate(path)
        except AssertionError as exc:
            if expected not in str(exc):
                raise AssertionError(f"Se esperaba {expected!r}; obtenido={exc}") from exc
            return
        raise AssertionError(f"La mutación debía fallar: {expected}")


def main() -> int:
    rows = load_gold()
    result = mod.validate_manifest(
        manifest=MANIFEST,
        schema=SCHEMA,
        lock=LOCK,
        units=UNIDADES,
        corpus_root=ROOT,
    )
    if result != {
        "revisiones": 89,
        "items": 60,
        "motores": ["definiciones", "formulas", "relaciones_explicitas"],
        "archivos_gold": [
            "patron-oro.jsonl",
            "patron-oro-formulas.jsonl",
            "patron-oro-formulas-general.jsonl",
            "patron-oro-relaciones-general.jsonl",
        ],
    }:
        raise AssertionError(f"Producto real inesperado: {result}")

    by_motor_stratum = Counter(
        (row["motor"], stratum)
        for row in rows
        for stratum in row["estratos"]
    )
    assert by_motor_stratum[("formulas", "general")] == 31
    assert by_motor_stratum[("formulas", "desafio")] == 18
    assert by_motor_stratum[("relaciones_explicitas", "general")] == 31
    assert by_motor_stratum[("relaciones_explicitas", "desafio")] == 2

    general_formulas = [
        row for row in rows
        if row["motor"] == "formulas" and "general" in row["estratos"]
    ]
    desafio_formulas = [
        row for row in rows
        if row["motor"] == "formulas" and "desafio" in row["estratos"]
    ]
    assert all(not row["items_esperados"] for row in general_formulas)
    assert sum(len(row["items_esperados"]) for row in desafio_formulas) == 21

    general_relations = [
        row for row in rows
        if row["motor"] == "relaciones_explicitas" and "general" in row["estratos"]
    ]
    desafio_relations = [
        row for row in rows
        if row["motor"] == "relaciones_explicitas" and "desafio" in row["estratos"]
    ]
    assert sum(bool(row["items_esperados"]) for row in general_relations) == 6
    assert sum(len(row["items_esperados"]) for row in general_relations) == 14
    assert sum(len(row["items_esperados"]) for row in desafio_relations) == 4

    mutated = copy.deepcopy(rows)
    mutated.append(copy.deepcopy(rows[0]))
    expect_failure(mutated, "duplicada unidad–motor")

    mutated = copy.deepcopy(rows)
    mutated[0]["items_esperados"][0]["texto_literal"] += " CORRUPCIÓN"
    expect_failure(mutated, "Literal no coincide")

    mutated = copy.deepcopy(rows)
    mutated[0]["items_esperados"][0]["clasificacion"] = "definicion_inferida"
    expect_failure(mutated, "Clasificación inválida")

    mutated = copy.deepcopy(rows)
    mutated[0]["estratos"] = ["general"]
    expect_failure(mutated, "marcado general")

    mutated = copy.deepcopy(rows)
    mutated[0]["items_esperados"][0]["tipo_registro"] = "formula"
    expect_failure(mutated, "no pertenece al motor")

    print(
        "OK Fase 8 infraestructura: patrón manifestado real 89 revisiones/60 ítems; "
        "fórmulas 31 general negativas + 18 desafío/21 ítems; relaciones 31 general/14 ítems "
        "en 6 unidades + 2 desafío/4 ítems; 5 corrupciones manuales rechazadas."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
