#!/usr/bin/env python3
"""Comprueba el cierre cuantitativo de Fase 8 sin reinterpretar métricas.

El combinado es informativo. Cada motor debe tener reportes `general` y
`desafio`. Las métricas no evaluables permanecen ``null`` y nunca se convierten
en 1.0. Un motor puede declarar explícitamente que un estrato sin positivos se
use como control negativo; en ese caso el estrato solo cumple con cero falsos
positivos y con positivos manuales en el estrato complementario.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_THRESHOLDS = ROOT / "analista/calibracion/umbrales-v1.1.0.json"
DEFAULT_REPORT = ROOT / "analista/generado/reporte-calibracion.json"
PILOTO_ID = "AA-SP-V1"
THRESHOLD_VERSION = "1.1.0"
REPORT_VERSION = "1.1.0"
REQUIRED_STRATA = ("general", "desafio")
THRESHOLD_TO_METRIC = {
    "precision_minima": "precision",
    "cobertura_minima": "cobertura",
    "exactitud_clasificacion_minima": "exactitud_clasificacion",
    "exactitud_estatus_minima": "exactitud_estatus",
    "exactitud_identidad_minima": "exactitud_identidad",
}
COUNT_FIELDS = (
    "positivos_esperados",
    "predicciones_emitidas",
    "verdaderos_positivos",
    "falsos_positivos",
    "falsos_negativos",
)


def load_json(path: Path) -> dict:
    if not path.is_file():
        raise SystemExit(f"No existe insumo requerido: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def nonnegative_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value >= 0


def gold_positives(row: dict | None) -> int | None:
    if row is None:
        return None
    value = row.get("positivos_esperados")
    return value if nonnegative_int(value) else None


def common_metric_checks(row: dict) -> tuple[list[dict], bool]:
    metrics: list[dict] = []
    passed = True
    units = row.get("unidades_procesadas")
    units_ok = isinstance(units, int) and not isinstance(units, bool) and units > 0
    metrics.append(
        {
            "metrica": "unidades_procesadas",
            "valor": units,
            "minimo": 1,
            "cumple": units_ok,
            "razon": None if units_ok else "sin_unidades_revisadas",
        }
    )
    passed = passed and units_ok

    counts: dict[str, int] = {}
    for field in COUNT_FIELDS:
        value = row.get(field)
        ok = nonnegative_int(value)
        metrics.append(
            {
                "metrica": field,
                "valor": value,
                "minimo": 0,
                "cumple": ok,
                "razon": None if ok else "conteo_invalido_o_faltante",
            }
        )
        if ok:
            counts[field] = value
        passed = passed and ok

    consistency_ok = False
    if len(counts) == len(COUNT_FIELDS):
        consistency_ok = (
            counts["positivos_esperados"]
            == counts["verdaderos_positivos"] + counts["falsos_negativos"]
            and counts["predicciones_emitidas"]
            == counts["verdaderos_positivos"] + counts["falsos_positivos"]
        )
    metrics.append(
        {
            "metrica": "consistencia_conteos",
            "valor": consistency_ok,
            "cumple": consistency_ok,
            "razon": None if consistency_ok else "denominadores_inconsistentes",
        }
    )
    passed = passed and consistency_ok
    return metrics, passed


def check(thresholds: dict, report: dict) -> dict:
    if thresholds.get("version") != THRESHOLD_VERSION or thresholds.get("obra_id") != PILOTO_ID:
        raise AssertionError(f"Umbrales incompatibles con Fase 8 {THRESHOLD_VERSION}")
    motors = thresholds.get("motores")
    if not isinstance(motors, dict) or not motors:
        raise AssertionError("No hay motores declarados en umbrales")

    rows = report.get("reportes")
    if not isinstance(rows, list):
        raise AssertionError("Reporte de calibración sin lista 'reportes'")
    by_key: dict[tuple[str, str], dict] = {}
    for row in rows:
        if row.get("version") != REPORT_VERSION or row.get("obra_id") != PILOTO_ID:
            raise AssertionError("Fila de calibración incompatible")
        key = (row.get("motor"), row.get("estrato"))
        if key in by_key:
            raise AssertionError(f"Reporte duplicado motor–estrato: {key}")
        by_key[key] = row

    details: list[dict] = []
    all_pass = True
    for motor, rules in motors.items():
        allow_negative_control = rules.get("permitir_control_solo_negativos") is True
        max_false_positives = rules.get("falsos_positivos_maximos_control_negativo", 0)
        if allow_negative_control and not nonnegative_int(max_false_positives):
            raise AssertionError(f"Máximo de falsos positivos inválido para {motor}")

        for stratum in REQUIRED_STRATA:
            row = by_key.get((motor, stratum))
            if row is None:
                details.append(
                    {
                        "motor": motor,
                        "estrato": stratum,
                        "estado": "faltante",
                        "modo": "umbral",
                        "metricas": [],
                        "metricas_no_aplicables": [],
                    }
                )
                all_pass = False
                continue

            metric_results, stratum_pass = common_metric_checks(row)
            positives = gold_positives(row)
            is_negative_control = allow_negative_control and positives == 0

            if is_negative_control:
                complement = "desafio" if stratum == "general" else "general"
                complement_row = by_key.get((motor, complement))
                complement_positives = gold_positives(complement_row)
                fp = row.get("falsos_positivos")
                fp_ok = nonnegative_int(fp) and fp <= max_false_positives
                complement_ok = isinstance(complement_positives, int) and complement_positives > 0
                metric_results.append(
                    {
                        "metrica": "falsos_positivos_control_negativo",
                        "valor": fp,
                        "maximo": max_false_positives,
                        "cumple": fp_ok,
                        "razon": None if fp_ok else "falsos_positivos_en_control_negativo",
                    }
                )
                metric_results.append(
                    {
                        "metrica": "positivos_estrato_complementario",
                        "valor": complement_positives,
                        "minimo": 1,
                        "cumple": complement_ok,
                        "razon": None if complement_ok else "sin_positivos_en_estrato_complementario",
                    }
                )
                stratum_pass = stratum_pass and fp_ok and complement_ok
                non_applicable = [
                    metric_name
                    for threshold_name, metric_name in THRESHOLD_TO_METRIC.items()
                    if threshold_name in rules
                ]
                details.append(
                    {
                        "motor": motor,
                        "estrato": stratum,
                        "estado": "cumple_control_negativo" if stratum_pass else "no_cumple_control_negativo",
                        "modo": "control_solo_negativos",
                        "metricas": metric_results,
                        "metricas_no_aplicables": non_applicable,
                    }
                )
                all_pass = all_pass and stratum_pass
                continue

            for threshold_name, metric_name in THRESHOLD_TO_METRIC.items():
                if threshold_name not in rules:
                    continue
                minimum = rules[threshold_name]
                value = row.get(metric_name)
                numeric = isinstance(value, (int, float)) and not isinstance(value, bool)
                passed = bool(numeric and value >= minimum)
                metric_results.append(
                    {
                        "metrica": metric_name,
                        "valor": value,
                        "minimo": minimum,
                        "cumple": passed,
                        "razon": None if passed else ("no_evaluable" if value is None else "bajo_umbral"),
                    }
                )
                stratum_pass = stratum_pass and passed

            details.append(
                {
                    "motor": motor,
                    "estrato": stratum,
                    "estado": "cumple" if stratum_pass else "no_cumple",
                    "modo": "umbral",
                    "metricas": metric_results,
                    "metricas_no_aplicables": [],
                }
            )
            all_pass = all_pass and stratum_pass

    return {
        "version": THRESHOLD_VERSION,
        "version_reporte": REPORT_VERSION,
        "obra_id": PILOTO_ID,
        "fase": 8,
        "cierre_cuantitativo": all_pass,
        "criterio": (
            "general_y_desafio_separados; control_solo_negativos_explicito_con_fp_cero_y_"
            "positivos_complementarios; combinado_informativo"
        ),
        "detalle": details,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--umbrales", type=Path, default=DEFAULT_THRESHOLDS)
    parser.add_argument("--reporte", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--salida", type=Path, default=None)
    args = parser.parse_args()
    result = check(load_json(args.umbrales), load_json(args.reporte))
    payload = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    if args.salida is not None:
        args.salida.parent.mkdir(parents=True, exist_ok=True)
        args.salida.write_text(payload, encoding="utf-8")
    print(payload, end="")
    return 0 if result["cierre_cuantitativo"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
