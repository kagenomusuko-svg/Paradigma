#!/usr/bin/env python3
"""Comprueba el cierre cuantitativo de Fase 8 sin reinterpretar métricas.

El combinado es informativo. Cada motor debe tener reportes `general` y
`desafio`, y todas las métricas congeladas para ese motor deben ser numéricas y
alcanzar su mínimo. Una métrica `null` significa "no evaluable con esta muestra"
y por tanto NO satisface el cierre.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_THRESHOLDS = ROOT / "analista/calibracion/umbrales-v1.0.0.json"
DEFAULT_REPORT = ROOT / "analista/generado/reporte-calibracion.json"
PILOTO_ID = "AA-SP-V1"
REQUIRED_STRATA = ("general", "desafio")
THRESHOLD_TO_METRIC = {
    "precision_minima": "precision",
    "cobertura_minima": "cobertura",
    "exactitud_clasificacion_minima": "exactitud_clasificacion",
    "exactitud_estatus_minima": "exactitud_estatus",
    "exactitud_identidad_minima": "exactitud_identidad",
}


def load_json(path: Path) -> dict:
    if not path.is_file():
        raise SystemExit(f"No existe insumo requerido: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def check(thresholds: dict, report: dict) -> dict:
    if thresholds.get("version") != "1.0.0" or thresholds.get("obra_id") != PILOTO_ID:
        raise AssertionError("Umbrales incompatibles con Fase 8 v1.0.0")
    motors = thresholds.get("motores")
    if not isinstance(motors, dict) or not motors:
        raise AssertionError("No hay motores declarados en umbrales")

    rows = report.get("reportes")
    if not isinstance(rows, list):
        raise AssertionError("Reporte de calibración sin lista 'reportes'")
    by_key: dict[tuple[str, str], dict] = {}
    for row in rows:
        if row.get("version") != "1.0.0" or row.get("obra_id") != PILOTO_ID:
            raise AssertionError("Fila de calibración incompatible")
        key = (row.get("motor"), row.get("estrato"))
        if key in by_key:
            raise AssertionError(f"Reporte duplicado motor–estrato: {key}")
        by_key[key] = row

    details: list[dict] = []
    all_pass = True
    for motor, rules in motors.items():
        for stratum in REQUIRED_STRATA:
            row = by_key.get((motor, stratum))
            if row is None:
                details.append(
                    {
                        "motor": motor,
                        "estrato": stratum,
                        "estado": "faltante",
                        "metricas": [],
                    }
                )
                all_pass = False
                continue

            metric_results: list[dict] = []
            stratum_pass = True
            if not isinstance(row.get("unidades_procesadas"), int) or row["unidades_procesadas"] <= 0:
                metric_results.append(
                    {
                        "metrica": "unidades_procesadas",
                        "valor": row.get("unidades_procesadas"),
                        "minimo": 1,
                        "cumple": False,
                        "razon": "sin_unidades_revisadas",
                    }
                )
                stratum_pass = False

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
                    "metricas": metric_results,
                }
            )
            all_pass = all_pass and stratum_pass

    return {
        "version": "1.0.0",
        "obra_id": PILOTO_ID,
        "fase": 8,
        "cierre_cuantitativo": all_pass,
        "criterio": "general_y_desafio_deben_cumplir_por_separado; combinado_informativo",
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
