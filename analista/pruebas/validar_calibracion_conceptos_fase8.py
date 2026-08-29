#!/usr/bin/env python3
"""Calibra 4A v1.1 contra el gold manual reproducible de Fase 8."""
from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EVALUATOR = ROOT / "analista/calibracion/evaluar.py"
MATERIALIZER = ROOT / "analista/calibracion/materializar_oro_conceptos.py"
MANIFEST = ROOT / "analista/calibracion/patron-oro-manifiesto.json"
GENERATED = ROOT / "analista/generado"
EXTRACTOR = ROOT / "analista/motores/conceptos.py"
MOTOR = "conceptos_apariciones"

spec = importlib.util.spec_from_file_location("evaluar_calibracion_conceptos", EVALUATOR)
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
    subprocess.run([sys.executable, str(EXTRACTOR)], cwd=ROOT, check=True)
    entries = [e for e in mod.load_manifest(MANIFEST) if e["motor"] == MOTOR]
    predictions = mod.extracted_items(GENERATED, MOTOR)

    assert len(entries) == 41
    assert len(predictions) == 2596  # 2575 apariciones + 21 conceptos

    general = report(entries, predictions, "general")
    assert general["unidades_procesadas"] == 31
    assert general["positivos_esperados"] == 114
    assert general["predicciones_emitidas"] == 114
    assert general["verdaderos_positivos"] == 114
    assert general["falsos_positivos"] == 0
    assert general["falsos_negativos"] == 0
    assert general["precision"] == 1
    assert general["cobertura"] == 1
    assert general["identidades_evaluadas"] == 17
    assert general["identidades_correctas"] == 17
    assert general["exactitud_identidad"] == 1
    assert general["clasificaciones_evaluadas"] == 3
    assert general["clasificaciones_correctas"] == 3

    challenge = report(entries, predictions, "desafio")
    assert challenge["unidades_procesadas"] == 10
    assert challenge["positivos_esperados"] == 70
    assert challenge["predicciones_emitidas"] == 70
    assert challenge["verdaderos_positivos"] == 70
    assert challenge["falsos_positivos"] == 0
    assert challenge["falsos_negativos"] == 0
    assert challenge["precision"] == 1
    assert challenge["cobertura"] == 1
    assert challenge["identidades_evaluadas"] == 8
    assert challenge["identidades_correctas"] == 8
    assert challenge["exactitud_identidad"] == 1

    combined = report(entries, predictions, "combinado")
    assert combined["unidades_procesadas"] == 41
    assert combined["positivos_esperados"] == 184
    assert combined["predicciones_emitidas"] == 184
    assert combined["verdaderos_positivos"] == 184
    assert combined["falsos_positivos"] == 0
    assert combined["falsos_negativos"] == 0
    assert combined["precision"] == 1
    assert combined["cobertura"] == 1
    assert combined["identidades_evaluadas"] == 25
    assert combined["identidades_correctas"] == 25
    assert combined["exactitud_identidad"] == 1

    print(
        "OK calibración Fase 8/4A v1.1: general 114 TP/0 FP/0 FN e identidad 17/17; "
        "desafío 70 TP/0 FP/0 FN e identidad 8/8; sin sinónimos, abreviaturas ni palabras simples enlazadas."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
