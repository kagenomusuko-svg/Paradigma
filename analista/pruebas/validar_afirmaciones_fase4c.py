#!/usr/bin/env python3
"""Valida 4C v1.1 sobre su producto proposicional real."""
from __future__ import annotations

import copy
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "analista/esquema/contratos-v1.0.0.schema.json"
UNIDADES = ROOT / "analista/generado/unidades.jsonl"
AFIRMACIONES = ROOT / "analista/generado/afirmaciones-candidatas.jsonl"
COBERTURA = ROOT / "analista/generado/cobertura-afirmaciones.jsonl"
MOTOR = ROOT / "analista/motores/afirmaciones.py"
PILOTO_ID = "AA-SP-V1"
EXPECTED_STATUS = {
    "afirmacion_autoral": 142,
    "cita": 21,
    "discurso_referido": 87,
    "ejemplo": 7,
    "formulacion_condicional": 32,
    "negacion_autoral": 25,
    "objecion": 3,
    "pregunta": 16,
}


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def validator_for(schema: dict, name: str) -> Draft202012Validator:
    return Draft202012Validator(
        {"$schema": schema["$schema"], "$defs": schema["$defs"], "$ref": f"#/$defs/{name}"}
    )


def occurrences_with_line_span(unit: dict, literal: str) -> list[tuple[int, int]]:
    text = unit["texto_literal"]
    base = unit["localizacion"]["linea_inicio"]
    out: list[tuple[int, int]] = []
    start = 0
    while True:
        pos = text.find(literal, start)
        if pos < 0:
            return out
        line_start = base + text[:pos].count("\n")
        line_end = line_start + literal.count("\n")
        out.append((line_start, line_end))
        start = pos + 1


def run_motor() -> None:
    subprocess.run([sys.executable, str(MOTOR)], cwd=ROOT, check=True)


def main() -> int:
    run_motor()
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    assertion_validator = validator_for(schema, "afirmacion")
    coverage_validator = validator_for(schema, "reporte_cobertura")

    unidades = load_jsonl(UNIDADES)
    afirmaciones = load_jsonl(AFIRMACIONES)
    reportes = load_jsonl(COBERTURA)
    pilot_units = [u for u in unidades if u["fuente_id"] == PILOTO_ID]
    unit_by_id = {u["id"]: u for u in pilot_units}

    assert len(pilot_units) == 836
    assert len(afirmaciones) == 333
    assert len({r["id"] for r in afirmaciones}) == 333
    assert sum(r["clasificacion_afirmacion"] == "afirmacion_explicita" for r in afirmaciones) == 304
    assert sum(r["clasificacion_afirmacion"] == "afirmacion_candidata" for r in afirmaciones) == 29
    assert Counter(r["estatus_enunciativo"] for r in afirmaciones) == Counter(EXPECTED_STATUS)
    assert not any(r["estatus_enunciativo"] == "no_determinado" for r in afirmaciones)

    for record in afirmaciones:
        errors = list(assertion_validator.iter_errors(record))
        assert not errors, f"Afirmación inválida {record.get('id')}: {errors[0].message}"
        assert record["fuente_id"] == PILOTO_ID
        assert record["unidad_id"] in unit_by_id
        assert record["producido_por"] == {"motor": "afirmaciones", "version": "1.1.0"}
        assert record["estado_verificacion"] == "pendiente"
        assert record["estado_auditoria"] == "pendiente"
        assert record["normalizacion_formal"] is None
        assert record["normalizacion_lexica"] is None
        assert record["concepto_ids"] == []
        assert record["sujeto_literal"] is None
        assert record["predicado_literal"] is None
        assert record["objeto_literal"] is None
        assert record["confianza_extraccion"] is None
        assert "sin_atribucion_autoral_por_coaparicion" in record["criterio_deteccion"]

        if record["clasificacion_afirmacion"] == "afirmacion_explicita":
            assert record["estado_extraccion"] == "extraido"
        else:
            assert record["estado_extraccion"] == "candidato"

        unit = unit_by_id[record["unidad_id"]]
        loc = record["localizacion"]
        assert loc["ruta"] == unit["archivo"]
        assert unit["localizacion"]["linea_inicio"] <= loc["linea_inicio"] <= loc["linea_fin"] <= unit["localizacion"]["linea_fin"]
        assert (loc["linea_inicio"], loc["linea_fin"]) in occurrences_with_line_span(
            unit, record["texto_literal"]
        ), f"Literal/rango no reproducible: {record['id']}"

        if record["estatus_enunciativo"] == "cita":
            assert record["texto_literal"].startswith("«") and record["texto_literal"].endswith("»")
        if loc["ruta"].endswith("00-preliminares.md") and loc["linea_inicio"] < 57:
            assert record["estatus_enunciativo"] == "cita", (
                "Portada, índice o mobiliario de preliminares no pueden ascender a afirmación."
            )

    assert sum(r["estatus_enunciativo"] == "cita" for r in afirmaciones) == 21

    assert len(reportes) == 1
    report = reportes[0]
    errors = list(coverage_validator.iter_errors(report))
    assert not errors, errors[0].message if errors else ""
    assert report["obra_id"] == PILOTO_ID
    assert report["motor"] == "afirmaciones"
    assert report["version_motor"] == "1.1.0"
    assert report["producido_por"] == {"motor": "afirmaciones", "version": "1.1.0"}
    assert report["unidades_totales"] == report["unidades_procesadas"] == 836
    assert report["unidades_omitidas"] == [] and report["errores"] == []
    assert report["estado_verificacion"] == "pendiente"

    forbidden = copy.deepcopy(afirmaciones[0])
    forbidden["solucion_doctrinal"] = "X"
    assert not assertion_validator.is_valid(forbidden), "El contrato aceptó un campo doctrinal prohibido."

    before = {AFIRMACIONES: AFIRMACIONES.read_bytes(), COBERTURA: COBERTURA.read_bytes()}
    run_motor()
    for path, payload in before.items():
        assert path.read_bytes() == payload, f"Salida no reproducible: {path.name}"

    print(
        "OK Fase 4C v1.1: 333 proposiciones trazables (304 explícitas/29 candidatas); "
        "836 unidades; 21 citas; 0 no_determinado; 0 enlaces conceptuales inferidos; "
        "salida reproducible."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
