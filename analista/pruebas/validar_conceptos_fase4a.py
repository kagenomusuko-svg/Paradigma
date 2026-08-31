#!/usr/bin/env python3
"""Validación de cierre del motor 4A v1.1 sobre sus productos reales."""
from __future__ import annotations

import copy
import hashlib
import json
import subprocess
import sys
import unicodedata
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "analista/esquema/contratos-v1.0.0.schema.json"
FUENTES_PATH = ROOT / "analista/generado/fuentes.jsonl"
UNIDADES_PATH = ROOT / "analista/generado/unidades.jsonl"
APARICIONES_PATH = ROOT / "analista/generado/apariciones-conceptuales.jsonl"
CONCEPTOS_PATH = ROOT / "analista/generado/conceptos.jsonl"
COBERTURA_PATH = ROOT / "analista/generado/cobertura-conceptos.jsonl"
MOTOR_PATH = ROOT / "analista/motores/conceptos.py"
PILOTO_ID = "AA-SP-V1"
MOTOR_VERSION = "1.1.0"


def load_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    with path.open("r", encoding="utf-8") as fh:
        for n, raw in enumerate(fh, start=1):
            if not raw.strip():
                continue
            try:
                rows.append(json.loads(raw))
            except json.JSONDecodeError as exc:
                raise AssertionError(f"JSONL inválido {path}:{n}: {exc}") from exc
    return rows


def norm(text: str) -> str:
    return " ".join(unicodedata.normalize("NFKC", text).casefold().split())


def stable_concept_id(designacion: str) -> str:
    digest = hashlib.sha1(norm(designacion).encode("utf-8")).hexdigest()[:12].upper()
    return f"CON-{digest}"


def validator_for(schema: dict, name: str) -> Draft202012Validator:
    return Draft202012Validator({"$schema": schema["$schema"], "$defs": schema["$defs"], "$ref": f"#/$defs/{name}"})


def assert_reproducible() -> None:
    before = {path: path.read_bytes() for path in (APARICIONES_PATH, CONCEPTOS_PATH, COBERTURA_PATH)}
    subprocess.run([sys.executable, str(MOTOR_PATH)], cwd=ROOT, check=True)
    for path, content in before.items():
        assert path.read_bytes() == content, f"Salida no reproducible: {path.name}"


def main() -> int:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    appearance_validator = validator_for(schema, "aparicion_conceptual")
    concept_validator = validator_for(schema, "concepto")
    coverage_validator = validator_for(schema, "reporte_cobertura")

    fuentes = load_jsonl(FUENTES_PATH)
    unidades = load_jsonl(UNIDADES_PATH)
    apariciones = load_jsonl(APARICIONES_PATH)
    conceptos = load_jsonl(CONCEPTOS_PATH)
    reportes = load_jsonl(COBERTURA_PATH)

    fuente = next((row for row in fuentes if row["id"] == PILOTO_ID), None)
    assert fuente is not None
    pilot_units = [row for row in unidades if row["fuente_id"] == PILOTO_ID]
    unit_by_id = {row["id"]: row for row in pilot_units}
    assert len(pilot_units) == len(unit_by_id) == 836

    assert len(reportes) == 1
    report = reportes[0]
    errors = list(coverage_validator.iter_errors(report))
    assert not errors, errors[0].message if errors else ""
    assert report["obra_id"] == PILOTO_ID
    assert report["motor"] == "conceptos_apariciones"
    assert report["version_motor"] == MOTOR_VERSION
    assert report["producido_por"] == {"motor": "conceptos_apariciones", "version": MOTOR_VERSION}
    assert report["unidades_totales"] == report["unidades_procesadas"] == 836
    assert report["unidades_omitidas"] == [] and report["errores"] == []
    assert report["estado_verificacion"] == "pendiente"

    # El sistema vigente no depende del prototipo retirado. Los IDs se validan
    # contra la regla estable del propio contrato 4A y la salida se exige
    # byte-reproducible más abajo.
    assert len(conceptos) == 21
    normalized_designations = [norm(row["designacion_operativa"]) for row in conceptos]
    assert len(normalized_designations) == len(set(normalized_designations)) == 21
    assert all(row["id"] == stable_concept_id(row["designacion_operativa"]) for row in conceptos)

    appearance_by_id = {row["id"]: row for row in apariciones}
    assert len(appearance_by_id) == len(apariciones) == 2575
    linked = [row for row in apariciones if row.get("concepto_id") is not None]
    candidates = [row for row in apariciones if row.get("concepto_id") is None]
    assert len(linked) == 419
    assert len(candidates) == 2156

    concept_by_id = {row["id"]: row for row in conceptos}
    evidence_ids: set[str] = set()
    all_linked_ids: set[str] = set()
    for concept in conceptos:
        errors = list(concept_validator.iter_errors(concept))
        assert not errors, f"Concepto inválido {concept.get('id')}: {errors[0].message}"
        assert concept["producido_por"] == {"motor": "conceptos_apariciones", "version": MOTOR_VERSION}
        assert concept["estado_extraccion"] == "extraido"
        assert concept["estado_verificacion"] == "pendiente"
        assert concept["estado_auditoria"] == "pendiente"
        assert concept["estado_identidad_conceptual"] == "establecida_por_evidencia"
        assert len(concept["evidencia_identidad_ids"]) == 1
        assert set(concept["evidencia_identidad_ids"]).issubset(concept["aparicion_ids"])
        assert concept["formas_literales_observadas"] == [concept["designacion_operativa"]]
        assert concept["texto_literal"] == concept["designacion_operativa"]
        for aid in concept["aparicion_ids"]:
            assert aid in appearance_by_id
            assert appearance_by_id[aid]["concepto_id"] == concept["id"]
            all_linked_ids.add(aid)
        evidence_ids.update(concept["evidencia_identidad_ids"])
    assert all_linked_ids == {row["id"] for row in linked}
    assert len(evidence_ids) == 21

    for appearance in apariciones:
        errors = list(appearance_validator.iter_errors(appearance))
        assert not errors, f"Aparición inválida {appearance.get('id')}: {errors[0].message}"
        assert appearance["producido_por"] == {"motor": "conceptos_apariciones", "version": MOTOR_VERSION}
        assert appearance["fuente_id"] == PILOTO_ID
        assert appearance["unidad_id"] in unit_by_id
        assert appearance["estado_verificacion"] == "pendiente"
        assert appearance["estado_auditoria"] == "pendiente"
        assert appearance["texto_literal"] == appearance["forma_literal"]
        assert appearance["normalizacion_lexica"] is None
        assert appearance["variantes_lexicas_busqueda"] == []

        unit = unit_by_id[appearance["unidad_id"]]
        loc = appearance["localizacion"]
        assert loc["ruta"] == unit["archivo"]
        assert unit["localizacion"]["linea_inicio"] <= loc["linea_inicio"] <= loc["linea_fin"] <= unit["localizacion"]["linea_fin"]
        source_lines = (ROOT / loc["ruta"]).read_text(encoding="utf-8").splitlines()
        fragment = "\n".join(source_lines[loc["linea_inicio"] - 1:loc["linea_fin"]])
        assert norm(appearance["forma_literal"]) in norm(fragment)
        if appearance["variante_formal"] is not None:
            assert norm(appearance["variante_formal"]) == norm(appearance["forma_literal"])

        if appearance["concepto_id"] is None:
            assert appearance["estado_extraccion"] == "candidato"
            assert "identidad_conceptual_no_determinada" in appearance["criterio_deteccion"]
        else:
            concept = concept_by_id[appearance["concepto_id"]]
            assert appearance["estado_extraccion"] == "extraido"
            if appearance["id"] in evidence_ids:
                assert appearance["criterio_deteccion"] == "lema_en_glosario_tecnico_explicito"
                assert loc["ruta"].endswith("99-glosario.md")
            else:
                assert len(concept["designacion_operativa"].split()) > 1
                assert norm(appearance["forma_literal"]) == norm(concept["designacion_operativa"])
                assert appearance["criterio_deteccion"] == "designacion_tecnica_multilexema_exacta; sin_normalizacion_semantica"

    # Ninguna palabra simple fuera de su declaración puede recibir identidad automática.
    for appearance in linked:
        if appearance["id"] in evidence_ids:
            continue
        concept = concept_by_id[appearance["concepto_id"]]
        assert len(concept["designacion_operativa"].split()) > 1

    aego = next(row for row in conceptos if row["designacion_operativa"] == "Aego")
    afasia = next(row for row in conceptos if row["designacion_operativa"] == "Afasia volitiva")
    assert aego["id"] != afasia["id"]
    assert len(aego["aparicion_ids"]) == 1, "Aego simple no debe enlazarse fuera de su declaración por forma sola."

    mutated = copy.deepcopy(conceptos[0])
    mutated["equivalencias_confirmadas"] = [conceptos[1]["id"]]
    assert not concept_validator.is_valid(mutated)

    assert_reproducible()
    print(
        "OK Fase 4A v1.1: 21 conceptos del piloto; 2575 apariciones = 419 vinculadas + "
        "2156 candidatas; 21 evidencias declarativas; palabras simples no se vinculan por forma; "
        "836 unidades; IDs estables; sin sinónimos, abreviaturas ni fusión conceptual."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
