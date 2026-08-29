#!/usr/bin/env python3
"""Fija el baseline real de 4E contra el gold efectivo de Fase 8.

Esta prueba NO declara cierre. Documenta mecánicamente por qué relaciones
explícitas sigue bajo umbral antes de calibrar el motor: usa el producto JSONL
versionado, no una reconstrucción sintética.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EVALUATOR = ROOT / "analista/calibracion/evaluar.py"
MANIFEST = ROOT / "analista/calibracion/patron-oro-manifiesto.json"
GENERATED = ROOT / "analista/generado"
MOTOR = "relaciones_explicitas"

spec = importlib.util.spec_from_file_location("evaluar_calibracion_relaciones", EVALUATOR)
assert spec and spec.loader
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def report(entries: list[dict], predictions: list[dict], stratum: str) -> dict:
    selected = (
        entries if stratum == "combinado"
        else [entry for entry in entries if stratum in entry["estratos"]]
    )
    units = {entry["unidad_id"] for entry in selected}
    gold = mod.flatten_gold(selected)
    predicted = [item for item in predictions if item["unidad_id"] in units]
    return mod.metrics(gold, predicted, units)


def main() -> int:
    entries = [entry for entry in mod.load_manifest(MANIFEST) if entry["motor"] == MOTOR]
    predictions = mod.extracted_items(GENERATED, MOTOR)

    assert len(entries) == 33
    assert len(predictions) == 4, "El baseline cambió; recalibrar antes de actualizar esta prueba."

    general = report(entries, predictions, "general")
    assert general["unidades_procesadas"] == 31
    assert general["positivos_esperados"] == 14
    assert general["predicciones_emitidas"] == 0
    assert general["verdaderos_positivos"] == 0
    assert general["falsos_positivos"] == 0
    assert general["falsos_negativos"] == 14
    assert general["precision"] is None
    assert general["cobertura"] == 0
    assert general["clasificaciones_evaluadas"] == 0

    challenge = report(entries, predictions, "desafio")
    assert challenge["unidades_procesadas"] == 2
    assert challenge["positivos_esperados"] == 14
    assert challenge["predicciones_emitidas"] == 4
    assert challenge["verdaderos_positivos"] == 4
    assert challenge["falsos_positivos"] == 0
    assert challenge["falsos_negativos"] == 10
    assert challenge["precision"] == 1
    assert challenge["cobertura"] == 4 / 14
    assert challenge["clasificaciones_evaluadas"] == 4
    assert challenge["clasificaciones_correctas"] == 4
    assert challenge["exactitud_clasificacion"] == 1

    combined = report(entries, predictions, "combinado")
    assert combined["unidades_procesadas"] == 33
    assert combined["positivos_esperados"] == 28
    assert combined["predicciones_emitidas"] == 4
    assert combined["verdaderos_positivos"] == 4
    assert combined["falsos_positivos"] == 0
    assert combined["falsos_negativos"] == 24
    assert combined["precision"] == 1
    assert combined["cobertura"] == 1 / 7

    print(
        "OK baseline Fase 8/4E: producto real v1.0.0 = 4 relaciones; general 0 TP/0 FP/14 FN; "
        "desafío 4 TP/0 FP/10 FN; precisión observada 1 donde evaluable, cobertura bajo umbral."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
