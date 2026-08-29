#!/usr/bin/env python3
from __future__ import annotations
import copy, json, re, subprocess, sys
from collections import Counter
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "analista/esquema/contratos-v1.0.0.schema.json"
UNIDADES = ROOT / "analista/generado/unidades.jsonl"
CONCEPTOS = ROOT / "analista/generado/conceptos.jsonl"
DEFINICIONES = ROOT / "analista/generado/definiciones.jsonl"
COBERTURA = ROOT / "analista/generado/cobertura-definiciones.jsonl"
LEGACY = ROOT / "analisis/generado/sobre-la-pasion/definiciones.jsonl"
MOTOR = ROOT / "analista/motores/definiciones.py"
PILOTO_ID = "AA-SP-V1"
MOTOR_VERSION = "1.1.0"
ROMAN_RE = re.compile(r"^[IVXLCDM]+$")


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def validator_for(schema: dict, name: str) -> Draft202012Validator:
    return Draft202012Validator({"$schema": schema["$schema"], "$defs": schema["$defs"], "$ref": f"#/$defs/{name}"})


def clean_literal(text: str) -> str:
    return " ".join(line.strip() for line in text.splitlines() if line.strip() and not ROMAN_RE.fullmatch(line.strip()))


def assert_literal_location(definition: dict, unit: dict) -> None:
    loc = definition["localizacion"]
    assert unit["archivo"] == loc["ruta"]
    assert unit["localizacion"]["linea_inicio"] <= loc["linea_inicio"] <= unit["localizacion"]["linea_fin"]
    lines = (ROOT / loc["ruta"]).read_text(encoding="utf-8").splitlines()
    assert 1 <= loc["linea_inicio"] <= loc["linea_fin"] <= len(lines)
    excerpt = "\n".join(lines[loc["linea_inicio"] - 1:loc["linea_fin"]])
    literal = definition["texto_literal"]
    position = excerpt.find(literal)
    assert position >= 0, f"Texto no literal en rango: {definition['id']}"
    before = excerpt[:position]
    after = excerpt[position + len(literal):]
    assert "\n" not in before, f"Inicio declarado demasiado temprano: {definition['id']}"
    assert "\n" not in after, f"Fin declarado demasiado tarde: {definition['id']}"
    if not loc["ruta"].endswith("99-glosario.md"):
        assert loc["linea_fin"] <= unit["localizacion"]["linea_fin"], f"Definición de prosa excede su unidad: {definition['id']}"
        assert literal in unit["texto_literal"]


def reproducible() -> None:
    before = {p: p.read_bytes() for p in (DEFINICIONES, COBERTURA)}
    subprocess.run([sys.executable, str(MOTOR)], cwd=ROOT, check=True)
    for path, content in before.items():
        assert path.read_bytes() == content, f"Salida no reproducible: {path.name}"


def main() -> int:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    definition_validator = validator_for(schema, "definicion")
    coverage_validator = validator_for(schema, "reporte_cobertura")
    unidades = load_jsonl(UNIDADES)
    conceptos = load_jsonl(CONCEPTOS)
    definiciones = load_jsonl(DEFINICIONES)
    reportes = load_jsonl(COBERTURA)
    legacy = load_jsonl(LEGACY)

    pilot_units = [u for u in unidades if u["fuente_id"] == PILOTO_ID]
    unit_by_id = {u["id"]: u for u in pilot_units}
    concept_ids = {c["id"] for c in conceptos}
    assert len(pilot_units) == 836
    assert len(conceptos) == 21
    assert len(reportes) == 1
    assert len(definiciones) == 60, f"Baseline determinista 4B v1.1 cambió: {len(definiciones)}"
    classes = Counter(d["clasificacion_definicion"] for d in definiciones)
    assert classes == {"definicion_explicita": 25, "definicion_candidata": 35}

    ids = [d["id"] for d in definiciones]
    assert len(ids) == len(set(ids)), "IDs duplicados de definición."
    legacy_by_id = {d["id"]: d for d in legacy}
    assert len(legacy_by_id) == 21
    assert set(legacy_by_id).issubset(ids), "Se perdió algún ID histórico de definición."

    for definition in definiciones:
        errors = list(definition_validator.iter_errors(definition))
        assert not errors, f"Definición inválida {definition.get('id')}: {errors[0].message}"
        assert definition["fuente_id"] == PILOTO_ID
        assert definition["concepto_id"] in concept_ids
        assert definition["unidad_id"] in unit_by_id
        assert definition["estado_verificacion"] == "pendiente"
        assert definition["estado_auditoria"] == "pendiente"
        assert definition["normalizacion_formal"] is None
        assert definition["normalizacion_lexica"] is None
        assert definition["producido_por"] == {"motor": "definiciones", "version": MOTOR_VERSION}
        assert "sin_fusion_conceptual" in definition["criterio_deteccion"] or definition["criterio_deteccion"] == "entrada_de_glosario_bajo_declaracion_explicita_de_definicion_tecnica"

        if definition["clasificacion_definicion"] == "definicion_explicita":
            assert definition["estado_extraccion"] == "extraido"
            assert definition["estatus_enunciativo"] == "definicion"
        else:
            assert definition["estado_extraccion"] == "candidato"
            assert definition["estatus_enunciativo"] in {"formulacion_condicional", "afirmacion_autoral", "no_determinado"}
            assert definition["estatus_enunciativo"] != "definicion"

        unit = unit_by_id[definition["unidad_id"]]
        assert_literal_location(definition, unit)

        if definition["id"] in legacy_by_id:
            old = legacy_by_id[definition["id"]]
            assert definition["clasificacion_definicion"] == "definicion_explicita"
            assert definition["localizacion"]["ruta"].endswith("99-glosario.md")
            assert clean_literal(definition["texto_literal"]) == old["evidencia"]["texto_literal"]
            assert definition["concepto_id"] == old["concepto_id"]

    report = reportes[0]
    errors = list(coverage_validator.iter_errors(report))
    assert not errors, errors[0].message if errors else ""
    assert report["obra_id"] == PILOTO_ID
    assert report["motor"] == "definiciones"
    assert report["version_motor"] == MOTOR_VERSION
    assert report["producido_por"] == {"motor": "definiciones", "version": MOTOR_VERSION}
    assert report["unidades_totales"] == len(pilot_units) == 836
    assert report["unidades_procesadas"] == len(pilot_units)
    assert report["unidades_omitidas"] == [] and report["errores"] == []
    assert report["estado_verificacion"] == "pendiente"

    explicit = next(d for d in definiciones if d["clasificacion_definicion"] == "definicion_explicita")
    bad_status = copy.deepcopy(explicit)
    bad_status["estatus_enunciativo"] = "afirmacion_autoral"
    assert not definition_validator.is_valid(bad_status), "El contrato aceptó una definición explícita con estatus incorrecto."
    bad_field = copy.deepcopy(explicit)
    bad_field["solucion_doctrinal"] = "X"
    assert not definition_validator.is_valid(bad_field), "El contrato aceptó un campo doctrinal prohibido."

    reproducible()
    print(
        "OK Fase 4B v1.1: 60 registros (25 explícitos/35 candidatos), 836 unidades; "
        "21 IDs históricos preservados; literalidad/rangos/fuerza probatoria verificados; verificación pendiente."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
