#!/usr/bin/env python3
"""Validación de cierre del motor 4A sobre sus productos reales."""
from __future__ import annotations

import copy
import json
import subprocess
import sys
import unicodedata
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "analista" / "esquema" / "contratos-v1.0.0.schema.json"
FUENTES_PATH = ROOT / "analista" / "generado" / "fuentes.jsonl"
UNIDADES_PATH = ROOT / "analista" / "generado" / "unidades.jsonl"
APARICIONES_PATH = ROOT / "analista" / "generado" / "apariciones-conceptuales.jsonl"
CONCEPTOS_PATH = ROOT / "analista" / "generado" / "conceptos.jsonl"
COBERTURA_PATH = ROOT / "analista" / "generado" / "cobertura-conceptos.jsonl"
LEGACY_CONCEPTOS = ROOT / "analisis" / "generado" / "sobre-la-pasion" / "conceptos.json"
MOTOR_PATH = ROOT / "analista" / "motores" / "conceptos.py"
PILOTO_ID = "AA-SP-V1"


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


def validator_for(schema: dict, name: str) -> Draft202012Validator:
    return Draft202012Validator(
        {
            "$schema": schema["$schema"],
            "$defs": schema["$defs"],
            "$ref": f"#/$defs/{name}",
        }
    )


def assert_reproducible() -> None:
    before = {
        path: path.read_bytes()
        for path in (APARICIONES_PATH, CONCEPTOS_PATH, COBERTURA_PATH)
    }
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
    assert fuente is not None, "Falta la fuente piloto."
    pilot_units = [row for row in unidades if row["fuente_id"] == PILOTO_ID]
    assert pilot_units, "No hay unidades de la obra piloto."
    unit_by_id = {row["id"]: row for row in pilot_units}
    assert len(unit_by_id) == len(pilot_units), "IDs de unidad duplicados."

    assert len(reportes) == 1, "Debe existir un único reporte de cobertura de 4A."
    report = reportes[0]
    errors = list(coverage_validator.iter_errors(report))
    assert not errors, errors[0].message if errors else ""
    assert report["obra_id"] == PILOTO_ID
    assert report["motor"] == "conceptos_apariciones"
    assert report["unidades_totales"] == len(pilot_units)
    assert report["unidades_procesadas"] == len(pilot_units)
    assert report["unidades_omitidas"] == []
    assert report["errores"] == []
    assert report["estado_verificacion"] == "pendiente"

    legacy = json.loads(LEGACY_CONCEPTOS.read_text(encoding="utf-8"))
    legacy_ids = {row["id"]: row["lema"] for row in legacy}
    new_ids = {row["id"]: row["designacion_operativa"] for row in conceptos}
    assert new_ids == legacy_ids, (
        "Los conceptos explícitos del glosario deben preservar los 21 IDs históricos."
    )
    assert len(conceptos) == 21

    appearance_by_id = {row["id"]: row for row in apariciones}
    assert len(appearance_by_id) == len(apariciones), "IDs de aparición duplicados."
    assert apariciones, "No hay apariciones."

    linked_ids: set[str] = set()
    for concept in conceptos:
        errors = list(concept_validator.iter_errors(concept))
        assert not errors, f"Concepto inválido {concept.get('id')}: {errors[0].message}"
        assert concept["estado_extraccion"] == "extraido"
        assert concept["estado_verificacion"] == "pendiente"
        assert concept["estado_auditoria"] == "pendiente"
        assert concept["estado_identidad_conceptual"] == "establecida_por_evidencia"
        assert len(concept["aparicion_ids"]) == 1
        assert concept["aparicion_ids"] == concept["evidencia_identidad_ids"]
        assert concept["formas_literales_observadas"] == [concept["designacion_operativa"]]
        assert concept["texto_literal"] == concept["designacion_operativa"]
        aid = concept["aparicion_ids"][0]
        assert aid in appearance_by_id, f"Evidencia inexistente en {concept['id']}"
        linked_ids.add(aid)

    candidate_count = 0
    for appearance in apariciones:
        errors = list(appearance_validator.iter_errors(appearance))
        assert not errors, (
            f"Aparición inválida {appearance.get('id')}: {errors[0].message}"
        )
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
        assert unit["localizacion"]["linea_inicio"] <= loc["linea_inicio"]
        assert loc["linea_fin"] <= unit["localizacion"]["linea_fin"]
        source_lines = (ROOT / loc["ruta"]).read_text(encoding="utf-8").splitlines()
        fragment = "\n".join(source_lines[loc["linea_inicio"] - 1 : loc["linea_fin"]])
        assert norm(appearance["forma_literal"]) in norm(fragment), (
            f"Forma no trazable en {appearance['id']}"
        )
        if appearance["variante_formal"] is not None:
            assert norm(appearance["variante_formal"]) == norm(appearance["forma_literal"])

        if appearance["id"] in linked_ids:
            assert appearance["concepto_id"] in new_ids
            assert appearance["estado_extraccion"] == "extraido"
            assert appearance["criterio_deteccion"] == "lema_en_glosario_tecnico_explicito"
            assert loc["ruta"].endswith("99-glosario.md")
        else:
            candidate_count += 1
            assert appearance["concepto_id"] is None, (
                "Una coincidencia fuera de la declaración explícita no puede ascender "
                "automáticamente a identidad conceptual."
            )
            assert appearance["estado_extraccion"] == "candidato"
            assert "identidad_conceptual_no_determinada" in appearance["criterio_deteccion"]

    assert candidate_count > 0, "La prueba no ejercitó apariciones candidatas."
    assert len(linked_ids) == len(conceptos) == 21

    aego = next(row for row in conceptos if row["designacion_operativa"] == "Aego")
    afasia = next(
        row for row in conceptos if row["designacion_operativa"] == "Afasia volitiva"
    )
    assert aego["id"] != afasia["id"], (
        "4A no puede fusionar Aego y Afasia volitiva aunque el glosario los relacione; "
        "la relación explícita pertenece a otro motor."
    )

    mutated = copy.deepcopy(conceptos[0])
    mutated["equivalencias_confirmadas"] = [conceptos[1]["id"]]
    assert not concept_validator.is_valid(mutated), (
        "El contrato aceptó una equivalencia ad hoc en concepto."
    )

    assert_reproducible()
    print(
        "OK Fase 4A: "
        f"{len(conceptos)} conceptos explícitos preservados; "
        f"{len(apariciones)} apariciones trazables, {candidate_count} candidatas no vinculadas; "
        f"{len(pilot_units)} unidades procesadas; sin fusión léxica ni verificación anticipada."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
