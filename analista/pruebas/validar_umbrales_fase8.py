#!/usr/bin/env python3
"""Prueba que Fase 8 no pueda cerrarse con evidencia cuantitativa insuficiente."""
from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MOTOR = ROOT / "analista/calibracion/comprobar_umbrales.py"
THRESHOLDS = ROOT / "analista/calibracion/umbrales-v1.1.0.json"

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
                "verdaderos_positivos": 10,
                "falsos_positivos": 0,
                "falsos_negativos": 0,
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


def row_for(payload: dict, motor: str, stratum: str) -> dict:
    return next(
        row
        for row in payload["reportes"]
        if row["motor"] == motor and row["estrato"] == stratum
    )


def detail_for(result: dict, motor: str, stratum: str) -> dict:
    return next(
        row
        for row in result["detalle"]
        if row["motor"] == motor and row["estrato"] == stratum
    )


def make_formula_general_negative(payload: dict) -> None:
    target = row_for(payload, "formulas", "general")
    target.update(
        {
            "unidades_procesadas": 31,
            "verdaderos_positivos": 0,
            "falsos_positivos": 0,
            "falsos_negativos": 0,
            "precision": None,
            "cobertura": None,
            "exactitud_clasificacion": None,
        }
    )


def main() -> int:
    thresholds = json.loads(THRESHOLDS.read_text(encoding="utf-8"))

    perfect = perfect_report(thresholds)
    result = mod.check(thresholds, perfect)
    assert result["version"] == "1.1.0"
    assert result["cierre_cuantitativo"] is True
    assert len(result["detalle"]) == 12
    assert all(row["estado"] == "cumple" for row in result["detalle"])

    # Caso real previsto para fórmulas: general tiene 31 controles y cero positivos.
    negative_control = perfect_report(thresholds)
    make_formula_general_negative(negative_control)
    result = mod.check(thresholds, negative_control)
    assert result["cierre_cuantitativo"] is True
    formula_general = detail_for(result, "formulas", "general")
    assert formula_general["estado"] == "cumple_control_negativo"
    assert formula_general["modo"] == "control_solo_negativos"
    assert set(formula_general["metricas_no_aplicables"]) == {
        "precision", "cobertura", "exactitud_clasificacion"
    }
    assert row_for(negative_control, "formulas", "general")["precision"] is None
    assert row_for(negative_control, "formulas", "general")["cobertura"] is None

    false_positive = copy.deepcopy(negative_control)
    target = row_for(false_positive, "formulas", "general")
    target["falsos_positivos"] = 1
    target["precision"] = 0.0
    result = mod.check(thresholds, false_positive)
    assert result["cierre_cuantitativo"] is False
    assert detail_for(result, "formulas", "general")["estado"] == "no_cumple_control_negativo"

    no_positive_complement = copy.deepcopy(negative_control)
    target = row_for(no_positive_complement, "formulas", "desafio")
    target["verdaderos_positivos"] = 0
    target["falsos_negativos"] = 0
    target["precision"] = None
    target["cobertura"] = None
    target["exactitud_clasificacion"] = None
    result = mod.check(thresholds, no_positive_complement)
    assert result["cierre_cuantitativo"] is False
    assert detail_for(result, "formulas", "general")["estado"] == "no_cumple_control_negativo"

    missing = copy.deepcopy(perfect)
    missing["reportes"] = [
        row
        for row in missing["reportes"]
        if not (row["motor"] == "formulas" and row["estrato"] == "general")
    ]
    result = mod.check(thresholds, missing)
    assert result["cierre_cuantitativo"] is False
    assert detail_for(result, "formulas", "general")["estado"] == "faltante"

    null_metric = copy.deepcopy(perfect)
    target = row_for(null_metric, "relaciones_explicitas", "general")
    target["cobertura"] = None
    result = mod.check(thresholds, null_metric)
    assert result["cierre_cuantitativo"] is False
    detail = detail_for(result, "relaciones_explicitas", "general")
    coverage = next(metric for metric in detail["metricas"] if metric["metrica"] == "cobertura")
    assert coverage["cumple"] is False and coverage["razon"] == "no_evaluable"

    low = copy.deepcopy(perfect)
    target = row_for(low, "afirmaciones", "desafio")
    target["precision"] = thresholds["motores"]["afirmaciones"]["precision_minima"] - 0.01
    result = mod.check(thresholds, low)
    assert result["cierre_cuantitativo"] is False

    zero_units = copy.deepcopy(perfect)
    zero_units["reportes"][0]["unidades_procesadas"] = 0
    result = mod.check(thresholds, zero_units)
    assert result["cierre_cuantitativo"] is False

    missing_counts = copy.deepcopy(perfect)
    row_for(missing_counts, "definiciones", "general").pop("falsos_negativos")
    result = mod.check(thresholds, missing_counts)
    assert result["cierre_cuantitativo"] is False

    print(
        "OK gate Fase 8 v1.1: 12 motor–estrato requeridos; control negativo explícito "
        "conserva métricas null y exige 0 FP + positivos complementarios; estrato faltante, "
        "conteos incompletos, métricas no evaluables fuera del control, umbral bajo o cero "
        "unidades impiden el cierre."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
