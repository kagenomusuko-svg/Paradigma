#!/usr/bin/env python3
"""Calibra 4B v1.1.0 contra el gold efectivo congelado de Fase 8."""
from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EVALUATOR = ROOT / "analista/calibracion/evaluar.py"
MANIFEST = ROOT / "analista/calibracion/patron-oro-manifiesto.json"
GENERATED = ROOT / "analista/generado"
EXTRACTOR = ROOT / "analista/motores/definiciones.py"
MOTOR = "definiciones"

spec = importlib.util.spec_from_file_location("evaluar_calibracion_definiciones", EVALUATOR)
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
    subprocess.run([sys.executable, str(EXTRACTOR)], cwd=ROOT, check=True)
    entries = [e for e in mod.load_manifest(MANIFEST) if e["motor"] == MOTOR]
    predictions = mod.extracted_items(GENERATED, MOTOR)
    assert len(entries) == 38
    assert len(predictions) == 60, "El producto 4B v1.1 cambió; revisar calibración antes de alterar esta prueba."

    general = report(entries, predictions, "general")
    assert general["unidades_procesadas"] == 31
    assert general["positivos_esperados"] == 12
    assert general["predicciones_emitidas"] == 12
    assert general["verdaderos_positivos"] == 12
    assert general["falsos_positivos"] == 0
    assert general["falsos_negativos"] == 0
    assert general["precision"] == 1
    assert general["cobertura"] == 1
    assert general["clasificaciones_evaluadas"] == 12
    assert general["clasificaciones_correctas"] == 12
    assert general["exactitud_clasificacion"] == 1
    assert general["estatus_evaluados"] == 12
    assert general["estatus_correctos"] == 12
    assert general["exactitud_estatus"] == 1

    challenge = report(entries, predictions, "desafio")
    assert challenge["unidades_procesadas"] == 7
    assert challenge["positivos_esperados"] == 21
    assert challenge["predicciones_emitidas"] == 21
    assert challenge["verdaderos_positivos"] == 21
    assert challenge["falsos_positivos"] == 0
    assert challenge["falsos_negativos"] == 0
    assert challenge["precision"] == 1
    assert challenge["cobertura"] == 1
    assert challenge["exactitud_clasificacion"] == 1
    assert challenge["exactitud_estatus"] == 1

    combined = report(entries, predictions, "combinado")
    assert combined["unidades_procesadas"] == 38
    assert combined["positivos_esperados"] == 33
    assert combined["predicciones_emitidas"] == 33
    assert combined["verdaderos_positivos"] == 33
    assert combined["falsos_positivos"] == 0
    assert combined["falsos_negativos"] == 0
    assert combined["precision"] == 1
    assert combined["cobertura"] == 1
    assert combined["exactitud_clasificacion"] == 1
    assert combined["exactitud_estatus"] == 1

    print(
        "OK calibración Fase 8/4B v1.1: general 12 TP/0 FP/0 FN; desafío 21 TP/0 FP/0 FN; "
        "precisión, cobertura, clasificación y estatus = 1.0 en ambos estratos."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
