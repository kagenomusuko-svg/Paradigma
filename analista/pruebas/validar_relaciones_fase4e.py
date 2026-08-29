#!/usr/bin/env python3
"""Valida el motor 4E sobre relaciones literalmente documentadas."""
from __future__ import annotations

import copy
import json
import subprocess
import sys
import unicodedata
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "analista/esquema/contratos-v1.0.0.schema.json"
UNIDADES = ROOT / "analista/generado/unidades.jsonl"
CONCEPTOS = ROOT / "analista/generado/conceptos.jsonl"
RELACIONES = ROOT / "analista/generado/relaciones-explicitas.jsonl"
COBERTURA = ROOT / "analista/generado/cobertura-relaciones.jsonl"
MOTOR = ROOT / "analista/motores/relaciones_explicitas.py"
PILOTO_ID = "AA-SP-V1"
EXPECTED_PAIRS = {
    ("Aego", "Afasia volitiva"),
    ("Aego", "Singularidad ontológica"),
    ("Afasia volitiva", "Aego"),
    ("Ego", "Mediación bis"),
}


def norm(text: str) -> str:
    return " ".join(unicodedata.normalize("NFKC", text).casefold().split())


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def validator_for(schema: dict, name: str) -> Draft202012Validator:
    return Draft202012Validator(
        {"$schema": schema["$schema"], "$defs": schema["$defs"], "$ref": f"#/$defs/{name}"}
    )


def assert_reproducible() -> None:
    before = {p: p.read_bytes() for p in (RELACIONES, COBERTURA)}
    subprocess.run([sys.executable, str(MOTOR)], cwd=ROOT, check=True)
    for path, content in before.items():
        assert path.read_bytes() == content, f"Salida no reproducible: {path.name}"


def main() -> int:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    relation_validator = validator_for(schema, "relacion_explicita")
    coverage_validator = validator_for(schema, "reporte_cobertura")

    unidades = load_jsonl(UNIDADES)
    conceptos = load_jsonl(CONCEPTOS)
    relaciones = load_jsonl(RELACIONES)
    reportes = load_jsonl(COBERTURA)

    pilot_units = [u for u in unidades if u["fuente_id"] == PILOTO_ID]
    unit_by_id = {u["id"]: u for u in pilot_units}
    concept_by_id = {c["id"]: c for c in conceptos}
    concept_by_name = {c["designacion_operativa"]: c for c in conceptos}

    assert len(pilot_units) == 836
    assert len(conceptos) == 21
    assert len(reportes) == 1
    assert len(relaciones) == 4, f"Relaciones explícitas inesperadas: {len(relaciones)}"
    assert set(concept_by_name) >= {name for pair in EXPECTED_PAIRS for name in pair}

    observed_pairs: set[tuple[str, str]] = set()
    ids: set[str] = set()
    for record in relaciones:
        errors = list(relation_validator.iter_errors(record))
        assert not errors, f"Relación inválida {record.get('id')}: {errors[0].message}"
        assert record["id"] not in ids, f"ID duplicado: {record['id']}"
        ids.add(record["id"])
        assert record["fuente_id"] == PILOTO_ID
        assert record["unidad_id"] in unit_by_id
        assert record["sujeto_ref"] in concept_by_id
        assert record["objeto_ref"] in concept_by_id
        assert record["sujeto_ref"] != record["objeto_ref"]
        assert record["clasificacion_relacion"] == "relacion_explicita"
        assert record["estado_extraccion"] == "extraido"
        assert record["estado_verificacion"] == "pendiente"
        assert record["estado_auditoria"] == "pendiente"
        assert record["estatus_enunciativo"] is None
        assert record["normalizacion_formal"] is None
        assert record["normalizacion_lexica"] is None

        subject = concept_by_id[record["sujeto_ref"]]["designacion_operativa"]
        target = concept_by_id[record["objeto_ref"]]["designacion_operativa"]
        observed_pairs.add((subject, target))

        loc = record["localizacion"]
        assert loc["linea_inicio"] == loc["linea_fin"], "4E debe citar la línea relacional exacta."
        unit = unit_by_id[record["unidad_id"]]
        assert unit["archivo"] == loc["ruta"]
        assert unit["localizacion"]["linea_inicio"] <= loc["linea_inicio"] <= unit["localizacion"]["linea_fin"]
        lines = (ROOT / loc["ruta"]).read_text(encoding="utf-8").splitlines()
        source_line = lines[loc["linea_inicio"] - 1]
        assert source_line == record["texto_literal"] == record["relacion_literal"]

        source_norm = norm(source_line)
        if "cf." in source_norm:
            suffix = source_norm.split("cf.", 1)[1]
            targets = {part.strip().rstrip(".;") for part in suffix.split(",")}
            assert norm(target) in targets, (
                f"La remisión no nombra literalmente el objeto {target!r}: {source_line!r}"
            )
        else:
            assert source_norm.startswith("nombre técnico del ")
            named = source_norm.removeprefix("nombre técnico del ").strip().rstrip(":.;")
            assert named == norm(target), (
                f"La formulación directa no nombra literalmente el objeto {target!r}: {source_line!r}"
            )

    assert observed_pairs == EXPECTED_PAIRS, (
        f"Conjunto relacional inesperado. esperado={EXPECTED_PAIRS!r}; observado={observed_pairs!r}"
    )
    # La remisión abreviada "Integral" no autoriza identidad con "Integral del ego — I(t)".
    assert ("Ego", "Integral del ego — I(t)") not in observed_pairs
    # Tampoco se materializan cierres transitivos, simetrías ni relaciones por coaparición.
    assert ("Afasia volitiva", "Singularidad ontológica") not in observed_pairs
    assert ("Mediación bis", "Ego") not in observed_pairs

    report = reportes[0]
    errors = list(coverage_validator.iter_errors(report))
    assert not errors, errors[0].message if errors else ""
    assert report["obra_id"] == PILOTO_ID
    assert report["motor"] == "relaciones_explicitas"
    assert report["unidades_totales"] == len(pilot_units)
    assert report["unidades_procesadas"] == len(pilot_units)
    assert report["unidades_omitidas"] == []
    assert report["errores"] == []
    assert report["estado_verificacion"] == "pendiente"

    forbidden = copy.deepcopy(relaciones[0])
    forbidden["armonizacion_propuesta"] = "X"
    assert not relation_validator.is_valid(forbidden), "El contrato aceptó un campo doctrinal prohibido."

    assert_reproducible()
    print(
        "OK Fase 4E: 4 relaciones explícitas literales; 836 unidades procesadas; "
        "0 transitividades/simetrías inferidas; abreviatura Integral no fusionada; verificación pendiente."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
