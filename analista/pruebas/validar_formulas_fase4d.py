#!/usr/bin/env python3
"""Valida Fase 4D sobre fórmulas candidatas y su contexto estructural."""
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
    before = {p: p.read_bytes() for p in (FORMULAS, COBERTURA)}
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
        (u for u in unidades if u["fuente_id"] == PILOTO_ID),
        key=lambda u: u["orden_textual"],
    )
    unit_by_id = {u["id"]: u for u in pilot_units}
    index_by_id = {u["id"]: i for i, u in enumerate(pilot_units)}
    seeds, heading_seeds = seed_lines(pilot_units)
    seed_unit_ids = {unit_id for unit_id, _ in seeds}
    legacy_unit_ids = {row["unidad_id"] for row in legacy}
    assert len(pilot_units) == 836
    assert len(seeds) == 20, f"Se esperaban 20 semillas elegibles; obtenidas={len(seeds)}"
    assert len(heading_seeds) == 1, (
        f"Debe existir un único rótulo de encabezado con '=' excluido; obtenidos={len(heading_seeds)}"
    )
    assert len(seed_unit_ids) == 18, f"Las 20 semillas deben distribuirse en 18 unidades; obtenidas={len(seed_unit_ids)}"
    assert seed_unit_ids == legacy_unit_ids, (
        "Las unidades elegibles con fórmula deben coincidir con las 18 unidades contextuales del postproceso histórico."
    )
    assert heading_seeds[0][0] not in legacy_unit_ids, (
        "El encabezado formal no debe ascender a unidad de fórmula por sí solo."
    )
    assert formulas, "No se generaron fórmulas candidatas."

    formulas_by_unit: dict[str, list[dict]] = defaultdict(list)
    ids = set()
    for formula in formulas:
        errors = list(formula_validator.iter_errors(formula))
        assert not errors, f"Fórmula inválida {formula.get('id')}: {errors[0].message}"
        assert formula["id"] not in ids
        ids.add(formula["id"])
        assert formula["fuente_id"] == PILOTO_ID
        assert formula["unidad_id"] in unit_by_id
        assert formula["clasificacion_formula"] == "formula_candidata"
        assert formula["estado_extraccion"] == "candidato"
        assert formula["estado_verificacion"] == "pendiente"
        assert formula["estado_auditoria"] == "pendiente"
        assert formula["estatus_enunciativo"] is None
        assert formula["formula_literal"] == formula["texto_literal"]
        assert "=" in formula["formula_literal"]
        assert formula["normalizacion_formal"] is None
        assert formula["normalizacion_lexica"] is None

        unit = unit_by_id[formula["unidad_id"]]
        assert unit.get("tipo_estructural") != "encabezado", (
            f"Un encabezado ascendió a fórmula candidata: {formula['id']}"
        )
        assert formula["formula_literal"] in unit["texto_literal"], (
            f"Fórmula no literal en {formula['id']}"
        )
        loc = formula["localizacion"]
        assert loc["ruta"] == unit["archivo"]
        assert unit["localizacion"]["linea_inicio"] <= loc["linea_inicio"] <= loc["linea_fin"] <= unit["localizacion"]["linea_fin"]
        idx = index_by_id[unit["id"]]
        assert formula["contexto_unidad_ids"] == context_expected(pilot_units, idx), (
            f"Contexto estructural incompleto en {formula['id']}"
        )
        assert unit["id"] in formula["contexto_unidad_ids"]
        assert balanced(formula["formula_literal"], "(", ")"), (
            f"Paréntesis cortados en {formula['id']}"
        )
        assert balanced(formula["formula_literal"], "[", "]"), (
            f"Corchetes cortados en {formula['id']}"
        )
        formulas_by_unit[formula["unidad_id"]].append(formula)

    uncovered = []
    multiply_covered = []
    for unit_id, line_no in seeds:
        matches = [
            f for f in formulas_by_unit.get(unit_id, [])
            if f["localizacion"]["linea_inicio"] <= line_no <= f["localizacion"]["linea_fin"]
        ]
        if not matches:
            uncovered.append((unit_id, line_no))
        if len(matches) > 1:
            multiply_covered.append((unit_id, line_no, [m["id"] for m in matches]))
    assert not uncovered, f"Semillas sin fórmula completa: {uncovered}"
    assert not multiply_covered, f"Semillas duplicadas entre fórmulas: {multiply_covered}"

    assert len(reports) == 1
    report = reports[0]
    errors = list(coverage_validator.iter_errors(report))
    assert not errors, errors[0].message if errors else ""
    assert report["obra_id"] == PILOTO_ID
    assert report["motor"] == "formulas"
    assert report["version_motor"] == "1.0.1"
    assert report["unidades_totales"] == len(pilot_units)
    assert report["unidades_procesadas"] == len(pilot_units)
    assert report["unidades_omitidas"] == [] and report["errores"] == []
    assert report["estado_verificacion"] == "pendiente"

    forbidden = copy.deepcopy(formulas[0])
    forbidden["interpretacion"] = "X"
    assert not formula_validator.is_valid(forbidden), "El contrato aceptó interpretación ad hoc de fórmula."

    assert_reproducible()
    print(
        f"OK Fase 4D: 20 semillas elegibles en 18 unidades históricas cubiertas exactamente una vez por {len(formulas)} "
        "fórmulas candidatas; 1 encabezado duplicativo excluido; delimitadores completos; "
        "contexto vecino preservado; 836 unidades procesadas; verificación pendiente."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
