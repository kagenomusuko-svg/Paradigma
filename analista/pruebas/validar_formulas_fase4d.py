#!/usr/bin/env python3
"""Valida Fase 4D calibrada sobre fórmulas literales y contexto estructural."""
from __future__ import annotations

import copy
import json
import subprocess
import sys
from collections import defaultdict
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "analista/esquema/contratos-v1.0.0.schema.json"
UNIDADES = ROOT / "analista/generado/unidades.jsonl"
FORMULAS = ROOT / "analista/generado/formulas-candidatas.jsonl"
COBERTURA = ROOT / "analista/generado/cobertura-formulas.jsonl"
LEGACY = ROOT / "analisis/generado/sobre-la-pasion/formulas-candidatas.jsonl"
MOTOR = ROOT / "analista/motores/formulas.py"
PILOTO_ID = "AA-SP-V1"
MOTOR_VERSION = "1.1.0"


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def validator_for(schema: dict, name: str) -> Draft202012Validator:
    return Draft202012Validator({"$schema": schema["$schema"], "$defs": schema["$defs"], "$ref": f"#/$defs/{name}"})


def seed_lines(units: list[dict]) -> tuple[list[tuple[str, int]], list[tuple[str, int]]]:
    eligible = []
    headings = []
    for unit in units:
        target = headings if unit.get("tipo_estructural") == "encabezado" else eligible
        for offset, line in enumerate(unit["texto_literal"].splitlines()):
            stripped = line.strip()
            if stripped and "=" in stripped and len(stripped) <= 320 and "http" not in stripped:
                target.append((unit["id"], unit["localizacion"]["linea_inicio"] + offset))
    return eligible, headings


def context_expected(units: list[dict], index: int) -> list[str]:
    current = units[index]
    out = []
    if index > 0 and units[index - 1]["archivo"] == current["archivo"]:
        out.append(units[index - 1]["id"])
    out.append(current["id"])
    if index + 1 < len(units) and units[index + 1]["archivo"] == current["archivo"]:
        out.append(units[index + 1]["id"])
    return out


def balanced(text: str, opening: str, closing: str) -> bool:
    level = 0
    for ch in text:
        if ch == opening:
            level += 1
        elif ch == closing:
            level -= 1
            if level < 0:
                return False
    return level == 0


def assert_reproducible() -> None:
    before = {path: path.read_bytes() for path in (FORMULAS, COBERTURA)}
    subprocess.run([sys.executable, str(MOTOR)], cwd=ROOT, check=True)
    for path, content in before.items():
        assert path.read_bytes() == content, f"Salida no reproducible: {path.name}"


def main() -> int:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    formula_validator = validator_for(schema, "formula")
    coverage_validator = validator_for(schema, "reporte_cobertura")
    unidades = load_jsonl(UNIDADES)
    formulas = load_jsonl(FORMULAS)
    reports = load_jsonl(COBERTURA)
    legacy = load_jsonl(LEGACY)

    pilot_units = sorted(
        (unit for unit in unidades if unit["fuente_id"] == PILOTO_ID),
        key=lambda unit: unit["orden_textual"],
    )
    unit_by_id = {unit["id"]: unit for unit in pilot_units}
    index_by_id = {unit["id"]: index for index, unit in enumerate(pilot_units)}
    seeds, heading_seeds = seed_lines(pilot_units)
    legacy_unit_ids = {row["unidad_id"] for row in legacy}

    assert len(pilot_units) == 836
    assert len(seeds) == 20, f"Se esperaban 20 semillas '=' elegibles; obtenidas={len(seeds)}"
    assert len(heading_seeds) == 1, "Debe existir un único encabezado con '=' excluido."
    assert formulas, "No se generaron fórmulas."
    assert len(formulas) == 21, f"La calibración fijó 21 fórmulas literales; obtenidas={len(formulas)}"

    formulas_by_unit: dict[str, list[dict]] = defaultdict(list)
    ids: set[str] = set()
    no_equals: list[dict] = []
    for formula in formulas:
        errors = list(formula_validator.iter_errors(formula))
        assert not errors, f"Fórmula inválida {formula.get('id')}: {errors[0].message}"
        assert formula["id"] not in ids
        ids.add(formula["id"])
        assert formula["fuente_id"] == PILOTO_ID
        assert formula["unidad_id"] in unit_by_id
        assert formula["clasificacion_formula"] == "formula_explicita"
        assert formula["estado_extraccion"] == "extraido"
        assert formula["estado_verificacion"] == "pendiente"
        assert formula["estado_auditoria"] == "pendiente"
        assert formula["estatus_enunciativo"] is None
        assert formula["formula_literal"] == formula["texto_literal"]
        assert formula["normalizacion_formal"] is None
        assert formula["normalizacion_lexica"] is None
        assert formula["producido_por"] == {"motor": "formulas", "version": MOTOR_VERSION}

        unit = unit_by_id[formula["unidad_id"]]
        assert unit.get("tipo_estructural") != "encabezado", f"Encabezado ascendido: {formula['id']}"
        assert formula["formula_literal"] in unit["texto_literal"], f"Fórmula no literal en {formula['id']}"
        location = formula["localizacion"]
        assert location["ruta"] == unit["archivo"]
        assert unit["localizacion"]["linea_inicio"] <= location["linea_inicio"] <= location["linea_fin"] <= unit["localizacion"]["linea_fin"]
        index = index_by_id[unit["id"]]
        assert formula["contexto_unidad_ids"] == context_expected(pilot_units, index), f"Contexto incompleto: {formula['id']}"
        assert unit["id"] in formula["contexto_unidad_ids"]
        assert balanced(formula["formula_literal"], "(", ")"), f"Paréntesis cortados: {formula['id']}"
        assert balanced(formula["formula_literal"], "[", "]"), f"Corchetes cortados: {formula['id']}"
        if "=" not in formula["formula_literal"]:
            no_equals.append(formula)
        formulas_by_unit[formula["unidad_id"]].append(formula)

    formula_unit_ids = set(formulas_by_unit)
    assert formula_unit_ids == legacy_unit_ids, (
        "La calibración añade una fórmula dentro de las mismas 18 unidades históricas, sin ampliar por similitud."
    )
    assert heading_seeds[0][0] not in formula_unit_ids

    uncovered = []
    multiply_covered = []
    for unit_id, line_no in seeds:
        matches = [
            formula
            for formula in formulas_by_unit.get(unit_id, [])
            if formula["localizacion"]["linea_inicio"] <= line_no <= formula["localizacion"]["linea_fin"]
        ]
        if not matches:
            uncovered.append((unit_id, line_no))
        if len(matches) > 1:
            multiply_covered.append((unit_id, line_no, [match["id"] for match in matches]))
    assert not uncovered, f"Semillas '=' sin fórmula literal: {uncovered}"
    assert not multiply_covered, f"Semillas '=' cubiertas por más de una fórmula: {multiply_covered}"

    assert len(no_equals) == 1, f"Debe existir una fórmula explícita sin '='; obtenidas={len(no_equals)}"
    assert no_equals[0]["unidad_id"] == "UT-F71941666B52"
    assert no_equals[0]["localizacion"]["linea_inicio"] == 32
    assert no_equals[0]["formula_literal"] == "(Identidad + Voluntad + φ₁ (v, c) + Acto + φ₂ (Acto, I)) ⁿ"

    assert len(reports) == 1
    report = reports[0]
    errors = list(coverage_validator.iter_errors(report))
    assert not errors, errors[0].message if errors else ""
    assert report["obra_id"] == PILOTO_ID
    assert report["motor"] == "formulas"
    assert report["version_motor"] == MOTOR_VERSION
    assert report["unidades_totales"] == len(pilot_units)
    assert report["unidades_procesadas"] == len(pilot_units)
    assert report["unidades_omitidas"] == [] and report["errores"] == []
    assert report["estado_verificacion"] == "pendiente"

    forbidden = copy.deepcopy(formulas[0])
    forbidden["interpretacion"] = "X"
    assert not formula_validator.is_valid(forbidden), "El contrato aceptó interpretación ad hoc de fórmula."

    assert_reproducible()
    print(
        "OK Fase 4D v1.1.0: 21 fórmulas explícitas literales en 18 unidades; "
        "20 semillas '=' cubiertas exactamente una vez y 1 fórmula explícita sin '=' recuperada; "
        "1 encabezado excluido; contexto vecino y delimitadores preservados; 836 unidades procesadas."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
