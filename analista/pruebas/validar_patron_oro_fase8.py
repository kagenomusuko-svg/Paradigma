#!/usr/bin/env python3
"""Pruebas de cierre de infraestructura del patrón de oro de Fase 8."""
from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALIDADOR = ROOT / "analista/calibracion/validar_patron_oro.py"
GOLD = ROOT / "analista/calibracion/patron-oro.jsonl"
SCHEMA = ROOT / "analista/calibracion/patron-oro-v1.0.0.schema.json"
LOCK = ROOT / "analista/calibracion/muestra-fase8.lock.json"
UNIDADES = ROOT / "analista/generado/unidades.jsonl"

spec = importlib.util.spec_from_file_location("validar_patron_oro", VALIDADOR)
if spec is None or spec.loader is None:
    raise SystemExit("No se pudo cargar el validador de Fase 8")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def load_gold() -> list[dict]:
    return [json.loads(line) for line in GOLD.read_text(encoding="utf-8").splitlines() if line]


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
    result = validate(GOLD)
    if result != {
        "revisiones": 9,
        "items": 25,
        "motores": ["definiciones", "relaciones_explicitas"],
    }:
        raise AssertionError(f"Producto real inesperado: {result}")

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
        "OK Fase 8 infraestructura: patrón real 9 revisiones/25 ítems; "
        "5 corrupciones manuales rechazadas."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
