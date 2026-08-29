#!/usr/bin/env python3
"""Prueba que Fase 8 no pueda cerrarse con estratos o métricas incompletos."""
from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MOTOR = ROOT / "analista/calibracion/comprobar_umbrales.py"
THRESHOLDS = ROOT / "analista/calibracion/umbrales-v1.0.0.json"

spec = importlib.util.spec_from_file_location("comprobar_umbrales", MOTOR)
assert spec and spec.loader
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

METRIC_FIELDS = {
    "precision_minima": "precision",
    "cobertura_minima": "cobertura",
    "exactitud_clasificacion_minima": "exactitud_clasificacion",
    "exactitud_estatus_minima": "exactitud_estatus",
    "exactitud_identidad_minima": "exactitud_identidad",
}


def perfect_report(thresholds: dict) -> dict:
    rows = []
    for motor, rules in thresholds["motores"].items():
        for stratum in ("general", "desafio"):
            row = {
                "version": "1.0.0",
                "obra_id": "AA-SP-V1",
                "motor": motor,
                "estrato": stratum,
                "unidades_procesadas": 10,
                "precision": 1.0,
                "cobertura": 1.0,
                "exactitud_clasificacion": None,
                "exactitud_estatus": None,
                "exactitud_identidad": None,
            }
            for threshold_name, metric_name in METRIC_FIELDS.items():
                if threshold_name in rules:
                    row[metric_name] = 1.0
            rows.append(row)
        # El combinado puede faltar: nunca sustituye los dos estratos requeridos.
    return {"reportes": rows}


def main() -> int:
    thresholds = json.loads(THRESHOLDS.read_text(encoding="utf-8"))
    perfect = perfect_report(thresholds)
    result = mod.check(thresholds, perfect)
    assert result["cierre_cuantitativo"] is True
    assert len(result["detalle"]) == 12
    assert all(row["estado"] == "cumple" for row in result["detalle"])

    missing = copy.deepcopy(perfect)
    missing["reportes"] = [
        row
        for row in missing["reportes"]
        if not (row["motor"] == "formulas" and row["estrato"] == "general")
    ]
    result = mod.check(thresholds, missing)
    assert result["cierre_cuantitativo"] is False
    assert next(
        row for row in result["detalle"] if row["motor"] == "formulas" and row["estrato"] == "general"
    )["estado"] == "faltante"

    null_metric = copy.deepcopy(perfect)
    target = next(
        row
        for row in null_metric["reportes"]
        if row["motor"] == "relaciones_explicitas" and row["estrato"] == "general"
    )
    target["cobertura"] = None
    result = mod.check(thresholds, null_metric)
    assert result["cierre_cuantitativo"] is False
    detail = next(
        row
        for row in result["detalle"]
        if row["motor"] == "relaciones_explicitas" and row["estrato"] == "general"
    )
    coverage = next(metric for metric in detail["metricas"] if metric["metrica"] == "cobertura")
    assert coverage["cumple"] is False and coverage["razon"] == "no_evaluable"

    low = copy.deepcopy(perfect)
    target = next(
        row for row in low["reportes"] if row["motor"] == "afirmaciones" and row["estrato"] == "desafio"
    )
    target["precision"] = thresholds["motores"]["afirmaciones"]["precision_minima"] - 0.01
    result = mod.check(thresholds, low)
    assert result["cierre_cuantitativo"] is False

    zero_units = copy.deepcopy(perfect)
    zero_units["reportes"][0]["unidades_procesadas"] = 0
    result = mod.check(thresholds, zero_units)
    assert result["cierre_cuantitativo"] is False

    print(
        "OK gate Fase 8: 12 motor–estrato requeridos; faltar un estrato, una métrica, "
        "el umbral o unidades revisadas impide el cierre; combinado no sustituye evidencia."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
