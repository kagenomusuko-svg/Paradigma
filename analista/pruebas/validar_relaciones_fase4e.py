#!/usr/bin/env python3
"""Valida el producto real del motor 4E v1.1.0.

La prueba no fija un número total de relaciones antes de ejecutar el extractor.
Comprueba contrato, trazabilidad literal, preservación del subconjunto histórico,
ausencia de fusiones abreviadas en esas evidencias y reproducibilidad byte a
byte del producto completo.
"""
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
MOTOR_VERSION = "1.1.0"
LEGACY_PAIRS = {
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


def canonical_excerpt(route: str, start: int, end: int) -> str:
    lines = (ROOT / route).read_text(encoding="utf-8").splitlines()
    assert 1 <= start <= end <= len(lines)
    return "\n".join(lines[start - 1:end])


def assert_reproducible() -> None:
    before = {p: p.read_bytes() for p in (RELACIONES, COBERTURA)}
    subprocess.run([sys.executable, str(MOTOR)], cwd=ROOT, check=True)
    for path, content in before.items():
        assert path.read_bytes() == content, f"Salida no reproducible: {path.name}"


def main() -> int:
    # La prueba valida el producto recién generado, no un JSONL histórico del repo.
    subprocess.run([sys.executable, str(MOTOR)], cwd=ROOT, check=True)

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

    assert len(pilot_units) == 836
    assert len(conceptos) == 21
    assert len(reportes) == 1
    assert len(relaciones) >= 4, "4E v1.1 perdió incluso el subconjunto histórico de relaciones."

    observed_legacy: set[tuple[str, str]] = set()
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
        assert record["producido_por"] == {"motor": "relaciones_explicitas", "version": MOTOR_VERSION}

        subject = concept_by_id[record["sujeto_ref"]]["designacion_operativa"]
        target = concept_by_id[record["objeto_ref"]]["designacion_operativa"]
        pair = (subject, target)
        literal_norm = norm(record["texto_literal"])
        assert norm(subject) in literal_norm or norm(target) in literal_norm or target == "Trayectoria del ego", (
            f"Ningún extremo tiene anclaje literal/contextual controlado: {record['id']} {pair!r}"
        )

        loc = record["localizacion"]
        unit = unit_by_id[record["unidad_id"]]
        assert unit["archivo"] == loc["ruta"]
        assert unit["localizacion"]["linea_inicio"] <= loc["linea_inicio"] <= loc["linea_fin"] <= unit["localizacion"]["linea_fin"]
        excerpt = canonical_excerpt(loc["ruta"], loc["linea_inicio"], loc["linea_fin"])
        literal = record["texto_literal"]
        assert literal == record["relacion_literal"]
        assert literal in excerpt, f"Literal no anclado exactamente: {record['id']}"
        before, after = excerpt.split(literal, 1)
        assert "\n" not in before and "\n" not in after, (
            f"Rango de líneas sobredimensionado para {record['id']}: {loc}"
        )

        if pair in LEGACY_PAIRS:
            observed_legacy.add(pair)

        # La abreviatura histórica "Integral" de la remisión no autoriza fusionar
        # ese objeto con "Integral del ego — I(t)".
        if loc["ruta"].endswith("99-glosario.md") and loc["linea_inicio"] == loc["linea_fin"] == 59:
            assert target != "Integral del ego — I(t)"

    assert observed_legacy == LEGACY_PAIRS, (
        f"Se perdió una relación histórica: esperado={LEGACY_PAIRS!r}; observado={observed_legacy!r}"
    )

    report = reportes[0]
    errors = list(coverage_validator.iter_errors(report))
    assert not errors, errors[0].message if errors else ""
    assert report["obra_id"] == PILOTO_ID
    assert report["motor"] == "relaciones_explicitas"
    assert report["version_motor"] == MOTOR_VERSION
    assert report["producido_por"] == {"motor": "relaciones_explicitas", "version": MOTOR_VERSION}
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
        f"OK Fase 4E v{MOTOR_VERSION}: {len(relaciones)} relaciones reales; 836 unidades procesadas; "
        "subconjunto histórico preservado; evidencia literal exacta; reproducibilidad confirmada."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
