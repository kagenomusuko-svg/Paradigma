#!/usr/bin/env python3
"""Valida el primer maestro no piloto de Fase 10: Afrodita Areia: Ágape."""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[2]
AGAPE = "FUE-2C28F35DD6CF"
PILOTO = "AA-SP-V1"
OBRA = ROOT / "analista/generado/obras" / AGAPE
MASTER = ROOT / "analista/generado/maestros" / f"{AGAPE}.json"
ASSEMBLER = ROOT / "analista/motores/ensamblador_maestro_obra_fase10.py"
OLD_SCHEMA = ROOT / "analista/esquema/contratos-v1.0.0.schema.json"
MASTER_SCHEMA = ROOT / "analista/esquema/expediente-maestro-fase10-v1.2.0.schema.json"

FILE_BY_FIELD = {
    "apariciones_conceptuales": "apariciones-conceptuales.jsonl",
    "conceptos": "conceptos.jsonl",
    "definiciones": "definiciones.jsonl",
    "afirmaciones": "afirmaciones-candidatas.jsonl",
    "formulas": "formulas-candidatas.jsonl",
    "relaciones_explicitas": "relaciones-explicitas.jsonl",
    "distinciones": "distinciones.jsonl",
    "negaciones": "negaciones.jsonl",
    "excepciones": "excepciones.jsonl",
    "restricciones_alcance": "restricciones-alcance.jsonl",
}
REF_BY_FIELD = {
    "apariciones_conceptuales": "aparicion_conceptual",
    "conceptos": "concepto",
    "definiciones": "definicion",
    "afirmaciones": "afirmacion",
    "formulas": "formula",
    "relaciones_explicitas": "relacion_explicita",
    "distinciones": "distincion",
    "negaciones": "negacion",
    "excepciones": "excepcion",
    "restricciones_alcance": "restriccion_alcance",
}
EXPECTED_COVERAGE = {
    "conceptos_apariciones",
    "definiciones",
    "afirmaciones",
    "formulas",
    "relaciones_explicitas",
    "limitadores",
}


def load_jsonl(path: Path) -> list[dict]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line
    ]


def import_assembler():
    spec = importlib.util.spec_from_file_location("ensamblador_maestro_obra_fase10", ASSEMBLER)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validator(old: dict, name: str) -> Draft202012Validator:
    return Draft202012Validator(
        {"$schema": old["$schema"], "$defs": old["$defs"], "$ref": f"#/$defs/{name}"}
    )


def expect_trace_failure(module, master: dict, text: str) -> None:
    try:
        module.validate_traceability(master)
    except AssertionError as exc:
        assert text in str(exc), (text, exc)
        return
    raise AssertionError(f"La mutación debía fallar: {text}")


def main() -> int:
    subprocess.run(
        [sys.executable, str(ASSEMBLER), "--obra-id", AGAPE],
        cwd=ROOT,
        check=True,
    )
    master = json.loads(MASTER.read_text(encoding="utf-8"))
    module = import_assembler()

    old = json.loads(OLD_SCHEMA.read_text(encoding="utf-8"))
    new = json.loads(MASTER_SCHEMA.read_text(encoding="utf-8"))
    registry = Registry().with_resource(old["$id"], Resource.from_contents(old))
    errors = list(Draft202012Validator(new, registry=registry).iter_errors(master))
    assert not errors, errors[0].message if errors else ""

    assert master["id"] == f"MAE-{AGAPE}"
    assert master["obra_id"] == AGAPE
    assert master["titulo"] == "Afrodita Areia: Ágape"
    assert master["schema_version"] == "1.2.0"
    assert master["producido_por"] == {
        "motor": "ensamblador_maestro_obra_fase10",
        "version": "1.0.0",
    }
    assert master["estado_verificacion"] == "verificado"
    assert master["estado_auditoria"] == "no_aplica"
    assert len(master["fuentes"]) == 1 and master["fuentes"][0]["id"] == AGAPE
    assert len(master["unidades"]) == 643

    source_validator = validator(old, "fuente")
    unit_validator = validator(old, "unidad_textual")
    assert not list(source_validator.iter_errors(master["fuentes"][0]))
    for unit in master["unidades"]:
        assert not list(unit_validator.iter_errors(unit))
        assert unit["fuente_id"] == AGAPE

    total_records = 0
    for field, filename in FILE_BY_FIELD.items():
        rows = master[field]
        original = load_jsonl(OBRA / "auditados" / filename)
        assert rows == original, f"El ensamblador transformó {field}"
        total_records += len(rows)
        row_validator = validator(old, REF_BY_FIELD[field])
        for row in rows:
            errors = list(row_validator.iter_errors(row))
            assert not errors, f"{field}/{row.get('id')}: {errors[0].message}"
            assert row["estado_verificacion"] == "verificado"
            assert row["estado_auditoria"] == "auditado"

    formulas = master["formulas"]
    assert len(formulas) == 33
    assert all(
        row["producido_por"] == {"motor": "formulas", "version": "1.3.0"}
        for row in formulas
    )

    findings = master["hallazgos_auditoria"]
    assert findings == load_jsonl(OBRA / "hallazgos-auditoria.jsonl")
    finding_validator = validator(old, "hallazgo_auditoria")
    for row in findings:
        assert not list(finding_validator.iter_errors(row))
        assert row["resolucion_doctrinal"] == "no_realizada"

    coverage = master["reportes_cobertura"]
    assert len(coverage) == 6
    assert {row["motor"] for row in coverage} == EXPECTED_COVERAGE
    assert all(row["obra_id"] == AGAPE for row in coverage)
    assert all(
        row["unidades_totales"] == row["unidades_procesadas"] == 643
        for row in coverage
    )
    assert all(not row["unidades_omitidas"] and not row["errores"] for row in coverage)

    controls = master["controles_fase10"]
    assert controls == {
        "version": "1.0.0",
        "obra_id": AGAPE,
        "fase": 10,
        "comparacion_interobra": False,
        "maestro_independiente": True,
        "normalizacion_recuperacion": True,
        "verificacion_evidencia": True,
        "auditoria_intraobra": True,
        "calibracion_formulas": {
            "perfil_calibrado": True,
            "version_produccion": "1.3.0",
            "perfil": f"analista/calibracion/fase10/{AGAPE}/perfil-extractores.json",
            "perfil_sha256": controls["calibracion_formulas"]["perfil_sha256"],
        },
    }
    assert controls["calibracion_formulas"]["perfil_sha256"]
    assert len(controls["calibracion_formulas"]["perfil_sha256"]) == 64

    trace = master["trazabilidad_archivos"]
    assert len(trace) == 41
    functions = {row["funcion"] for row in trace}
    assert functions == {
        "fuente",
        "unidades",
        "manifest",
        "producto_normalizado",
        "producto_verificado",
        "producto_auditado",
        "hallazgos",
        "cobertura",
        "calibracion_obra",
    }
    for entry in trace:
        path = ROOT / entry["ruta"]
        assert path.is_file(), entry["ruta"]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == entry["sha256"]

    assert PILOTO not in MASTER.read_text(encoding="utf-8")

    module.validate_traceability(master)

    sidecar = MASTER.with_suffix(MASTER.suffix + ".sha256")
    digest, filename = sidecar.read_text(encoding="utf-8").strip().split("  ", 1)
    assert filename == MASTER.name
    assert digest == hashlib.sha256(MASTER.read_bytes()).hexdigest()

    snapshot = MASTER.read_bytes(), sidecar.read_bytes()
    subprocess.run(
        [sys.executable, str(ASSEMBLER), "--obra-id", AGAPE],
        cwd=ROOT,
        check=True,
    )
    assert (MASTER.read_bytes(), sidecar.read_bytes()) == snapshot

    broken = copy.deepcopy(master)
    broken["fuentes"][0]["id"] = PILOTO
    expect_trace_failure(module, broken, "solo la fuente de su obra")

    broken = copy.deepcopy(master)
    broken["controles_fase10"]["comparacion_interobra"] = True
    expect_trace_failure(module, broken, "no permite comparación interobra")

    if findings:
        broken = copy.deepcopy(master)
        broken["hallazgos_auditoria"][0]["resolucion_doctrinal"] = "armonizada"
        expect_trace_failure(module, broken, "resolución doctrinal")

    print(
        "OK Fase 10 Ágape maestro: "
        f"643 unidades, {total_records} registros auditados, {len(findings)} hallazgos, "
        "6 coberturas y 41 hashes de insumo; maestro independiente, trazable, "
        "byte-reproducible y sin comparación interobra."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
