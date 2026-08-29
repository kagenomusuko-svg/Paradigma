#!/usr/bin/env python3
"""Fija el baseline real de 4B v1.0.0 contra el gold efectivo de Fase 8."""
from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EVALUATOR = ROOT / "analista/calibracion/evaluar.py"
MANIFEST = ROOT / "analista/calibracion/patron-oro-manifiesto.json"
GENERATED = ROOT / "analista/generado"
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
    entries = [e for e in mod.load_manifest(MANIFEST) if e["motor"] == MOTOR]
    predictions = mod.extracted_items(GENERATED, MOTOR)
    assert len(entries) == 38
    assert len(predictions) == 21, "El baseline 4B v1.0.0 cambió; recalibrar antes de alterar esta prueba."

    general = report(entries, predictions, "general")
    assert general["unidades_procesadas"] == 31
    assert general["positivos_esperados"] == 12
    assert general["predicciones_emitidas"] == 3
    assert general["verdaderos_positivos"] == 3
    assert general["falsos_positivos"] == 0
    assert general["falsos_negativos"] == 9
    assert general["precision"] == 1
    assert general["cobertura"] == 0.25
    assert general["clasificaciones_evaluadas"] == 3
    assert general["clasificaciones_correctas"] == 3
    assert general["exactitud_clasificacion"] == 1
    assert general["estatus_evaluados"] == 3
    assert general["estatus_correctos"] == 3
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
    assert combined["predicciones_emitidas"] == 24
    assert combined["verdaderos_positivos"] == 24
    assert combined["falsos_positivos"] == 0
    assert combined["falsos_negativos"] == 9
    assert combined["precision"] == 1
    assert combined["cobertura"] == 24 / 33

    print(
        "OK baseline Fase 8/4B: v1.0.0 conserva 21 definiciones de glosario; general 3 TP/0 FP/9 FN "
        "(cobertura 0.25); desafío 21 TP/0 FP/0 FN; la cobertura general impide cierre."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
