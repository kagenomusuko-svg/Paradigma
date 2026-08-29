#!/usr/bin/env python3
"""Valida el motor 4C sobre el producto real sin ascenso enunciativo automático."""
from __future__ import annotations

import copy
import json
import subprocess
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "analista/esquema/contratos-v1.0.0.schema.json"
UNIDADES = ROOT / "analista/generado/unidades.jsonl"
AFIRMACIONES = ROOT / "analista/generado/afirmaciones-candidatas.jsonl"
COBERTURA = ROOT / "analista/generado/cobertura-afirmaciones.jsonl"
LEGACY = ROOT / "analisis/generado/sobre-la-pasion/afirmaciones-candidatas.jsonl"
MOTOR = ROOT / "analista/motores/afirmaciones.py"
PILOTO_ID = "AA-SP-V1"


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def validator_for(schema: dict, name: str) -> Draft202012Validator:
    return Draft202012Validator(
        {"$schema": schema["$schema"], "$defs": schema["$defs"], "$ref": f"#/$defs/{name}"}
    )


def assert_reproducible() -> None:
    before = {p: p.read_bytes() for p in (AFIRMACIONES, COBERTURA)}
    subprocess.run([sys.executable, str(MOTOR)], cwd=ROOT, check=True)
    for path, content in before.items():
        assert path.read_bytes() == content, f"Salida no reproducible: {path.name}"


def main() -> int:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    assertion_validator = validator_for(schema, "afirmacion")
    coverage_validator = validator_for(schema, "reporte_cobertura")

    unidades = load_jsonl(UNIDADES)
    afirmaciones = load_jsonl(AFIRMACIONES)
    reportes = load_jsonl(COBERTURA)
    legacy = load_jsonl(LEGACY)
    pilot_units = [u for u in unidades if u["fuente_id"] == PILOTO_ID]
    unit_by_id = {u["id"]: u for u in pilot_units}

    assert len(pilot_units) == 836
    assert len(reportes) == 1
    assert afirmaciones, "No se recuperaron candidatos."
    assert len(afirmaciones) == 73, f"Recall histórico inesperado: {len(afirmaciones)}"
    assert {a["id"] for a in afirmaciones} == {a["id"] for a in legacy}, (
        "El motor 4C debe preservar el conjunto histórico de 73 IDs candidatos."
    )

    ids = set()
    for record in afirmaciones:
        errors = list(assertion_validator.iter_errors(record))
        assert not errors, f"Afirmación inválida {record.get('id')}: {errors[0].message}"
        assert record["id"] not in ids, f"ID duplicado: {record['id']}"
        ids.add(record["id"])
        assert record["fuente_id"] == PILOTO_ID
        assert record["unidad_id"] in unit_by_id
        assert record["clasificacion_afirmacion"] == "afirmacion_candidata"
        assert record["estado_extraccion"] == "candidato"
        assert record["estado_verificacion"] == "pendiente"
        assert record["estado_auditoria"] == "pendiente"
        assert record["estatus_enunciativo"] == "no_determinado", (
            "Un marcador de recuperación no basta para atribuir voz autoral, objeción, cita o hipótesis."
        )
        assert record["concepto_ids"] == [], (
            "4C no debe enlazar conceptos desde apariciones todavía candidatas."
        )
        assert record["sujeto_literal"] is None
        assert record["predicado_literal"] is None
        assert record["objeto_literal"] is None
        assert record["confianza_extraccion"] is None
        assert record["normalizacion_formal"] is None
        assert record["normalizacion_lexica"] is None

        unit = unit_by_id[record["unidad_id"]]
        assert record["texto_literal"] == unit["texto_literal"]
        assert record["localizacion"] == unit["localizacion"]
        lines = (ROOT / record["localizacion"]["ruta"]).read_text(encoding="utf-8").splitlines()
        loc = record["localizacion"]
        source_text = "\n".join(lines[loc["linea_inicio"] - 1 : loc["linea_fin"]])
        assert source_text == record["texto_literal"], f"Texto no literal: {record['id']}"

    report = reportes[0]
    errors = list(coverage_validator.iter_errors(report))
    assert not errors, errors[0].message if errors else ""
    assert report["obra_id"] == PILOTO_ID
    assert report["motor"] == "afirmaciones"
    assert report["unidades_totales"] == len(pilot_units)
    assert report["unidades_procesadas"] == len(pilot_units)
    assert report["unidades_omitidas"] == []
    assert report["errores"] == []
    assert report["estado_verificacion"] == "pendiente"

    forbidden = copy.deepcopy(afirmaciones[0])
    forbidden["solucion_doctrinal"] = "X"
    assert not assertion_validator.is_valid(forbidden), "El contrato aceptó un campo doctrinal prohibido."

    assert_reproducible()
    print(
        "OK Fase 4C: 73 candidatos históricos preservados; 836 unidades procesadas; "
        "estatus no_determinado en todos; 0 tesis autorales fabricadas; verificación pendiente."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
