#!/usr/bin/env python3
"""Valida 4C v1.1 contra el gold manual congelado de Fase 8."""
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EVALUATOR = ROOT / "analista/calibracion/evaluar.py"
MATERIALIZER = ROOT / "analista/calibracion/materializar_oro_afirmaciones.py"
GOLD = ROOT / "analista/calibracion/patron-oro-afirmaciones.jsonl"
MOTOR = ROOT / "analista/motores/afirmaciones.py"
GENERATED = ROOT / "analista/generado"

spec = importlib.util.spec_from_file_location("evaluar_calibracion_afirmaciones", EVALUATOR)
assert spec and spec.loader
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def report(entries: list[dict], predictions: list[dict], stratum: str) -> dict:
    selected = entries if stratum == "combinado" else [e for e in entries if stratum in e["estratos"]]
    units = {e["unidad_id"] for e in selected}
    return mod.metrics(
        mod.flatten_gold(selected),
        [item for item in predictions if item["unidad_id"] in units],
        units,
    )


def main() -> int:
    subprocess.run([sys.executable, str(MATERIALIZER)], cwd=ROOT, check=True)
    subprocess.run([sys.executable, str(MOTOR)], cwd=ROOT, check=True)

    entries = mod.load_jsonl(GOLD)
    assert len(entries) == 42
    assert all(e["motor"] == "afirmaciones" for e in entries)
    predictions = mod.extracted_items(GENERATED, "afirmaciones")
    assert len(predictions) == 333

    general = report(entries, predictions, "general")
    assert general["unidades_procesadas"] == 31
    assert general["positivos_esperados"] == 34
    assert general["predicciones_emitidas"] == 34
    assert general["verdaderos_positivos"] == 34
    assert general["falsos_positivos"] == 0
    assert general["falsos_negativos"] == 0
    assert general["precision"] == general["cobertura"] == 1
    assert general["clasificaciones_evaluadas"] == general["clasificaciones_correctas"] == 34
    assert general["exactitud_clasificacion"] == 1
    assert general["estatus_evaluados"] == general["estatus_correctos"] == 34
    assert general["exactitud_estatus"] == 1

    challenge = report(entries, predictions, "desafio")
    assert challenge["unidades_procesadas"] == 12
    assert challenge["positivos_esperados"] == 26
    assert challenge["predicciones_emitidas"] == 26
    assert challenge["verdaderos_positivos"] == 26
    assert challenge["falsos_positivos"] == 0
    assert challenge["falsos_negativos"] == 0
    assert challenge["precision"] == challenge["cobertura"] == 1
    assert challenge["clasificaciones_evaluadas"] == challenge["clasificaciones_correctas"] == 26
    assert challenge["exactitud_clasificacion"] == 1
    assert challenge["estatus_evaluados"] == challenge["estatus_correctos"] == 26
    assert challenge["exactitud_estatus"] == 1

    combined = report(entries, predictions, "combinado")
    assert combined["unidades_procesadas"] == 42
    assert combined["positivos_esperados"] == 58
    assert combined["predicciones_emitidas"] == 58
    assert combined["verdaderos_positivos"] == 58
    assert combined["falsos_positivos"] == combined["falsos_negativos"] == 0
    assert combined["precision"] == combined["cobertura"] == 1
    assert combined["exactitud_clasificacion"] == combined["exactitud_estatus"] == 1

    print(
        "OK Fase 8/4C: general 34 TP/0 FP/0 FN; desafío 26 TP/0 FP/0 FN; "
        "clasificación y estatus 1.0 en ambos estratos; combinado 58/58."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
