#!/usr/bin/env python3
"""Compara 4E v1.1.0 con el baseline real congelado de Fase 8.

El baseline histórico permanece fijado en 4 TP / 24 FN sobre 28 relaciones
manuales. La prueba reconstruye el producto actual y exige mejora real, pero no
sustituye al gate de umbrales: precisión/cobertura de producción se deciden en
`comprobar_umbrales.py` usando el reporte completo.
"""
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EVALUATOR = ROOT / "analista/calibracion/evaluar.py"
MANIFEST = ROOT / "analista/calibracion/patron-oro-manifiesto.json"
GENERATED = ROOT / "analista/generado"
EXTRACTOR = ROOT / "analista/motores/relaciones_explicitas.py"
MOTOR = "relaciones_explicitas"
BASELINE = {
    "general": {"tp": 0, "fp": 0, "fn": 14},
    "desafio": {"tp": 4, "fp": 0, "fn": 10},
    "combinado": {"tp": 4, "fp": 0, "fn": 24},
}

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
    subprocess.run([sys.executable, str(EXTRACTOR)], cwd=ROOT, check=True)

    entries = [entry for entry in mod.load_manifest(MANIFEST) if entry["motor"] == MOTOR]
    predictions = mod.extracted_items(GENERATED, MOTOR)
    assert len(entries) == 33
    assert len(predictions) >= 4, "4E v1.1 perdió el producto histórico completo."

    general = report(entries, predictions, "general")
    challenge = report(entries, predictions, "desafio")
    combined = report(entries, predictions, "combinado")

    assert general["unidades_procesadas"] == 31
    assert challenge["unidades_procesadas"] == 2
    assert combined["unidades_procesadas"] == 33
    assert general["positivos_esperados"] == 14
    assert challenge["positivos_esperados"] == 14
    assert combined["positivos_esperados"] == 28

    # Mejora mínima frente al producto v1.0.0 ya documentado. El gate separado
    # conserva la responsabilidad de exigir los umbrales de producción.
    assert general["verdaderos_positivos"] > BASELINE["general"]["tp"], general
    assert general["falsos_negativos"] < BASELINE["general"]["fn"], general
    assert challenge["verdaderos_positivos"] >= BASELINE["desafio"]["tp"], challenge
    assert challenge["falsos_negativos"] <= BASELINE["desafio"]["fn"], challenge
    assert combined["verdaderos_positivos"] > BASELINE["combinado"]["tp"], combined
    assert combined["falsos_negativos"] < BASELINE["combinado"]["fn"], combined
    assert combined["cobertura"] is not None and combined["cobertura"] > 1 / 7, combined

    # Toda clasificación de una detección correctamente emparejada debe seguir
    # siendo `relacion_explicita`; no se mejora recall degradando la etiqueta.
    assert general["clasificaciones_correctas"] == general["clasificaciones_evaluadas"]
    assert challenge["clasificaciones_correctas"] == challenge["clasificaciones_evaluadas"]

    print(
        json.dumps(
            {
                "baseline": BASELINE,
                "actual": {
                    "general": general,
                    "desafio": challenge,
                    "combinado": combined,
                },
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
