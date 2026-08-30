#!/usr/bin/env python3
"""Ejecuta y valida de extremo a extremo una obra no piloto de Fase 10.

La validación es intraobra. No compara contenidos entre obras ni interpreta la
ausencia de registros como ausencia semántica. Una obra sin glosario técnico
explícito conserva vacíos los productos que requieren identidad conceptual y
registra esa limitación en su manifest.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[2]
FUENTES = ROOT / "analista/generado/fuentes.jsonl"
UNIDADES = ROOT / "analista/generado/unidades.jsonl"
OLD_SCHEMA = ROOT / "analista/esquema/contratos-v1.0.0.schema.json"
MASTER_SCHEMA = ROOT / "analista/esquema/expediente-maestro-fase10-v1.2.0.schema.json"
EXTRACTOR = ROOT / "analista/motores/ejecutar_extractores_obra_fase10.py"
NORMALIZER = ROOT / "analista/motores/normalizacion.py"
VERIFIER = ROOT / "analista/motores/verificador_evidencia.py"
STRUCTURAL = ROOT / "analista/motores/auditor_estructural.py"
DESCRIPTIVE = ROOT / "analista/motores/auditor_descriptivo.py"
ASSEMBLER = ROOT / "analista/motores/ensamblador_maestro_obra_fase10.py"
PILOT = "AA-SP-V1"

PRODUCT_TYPES = {
    "apariciones-conceptuales.jsonl": "aparicion_conceptual",
    "conceptos.jsonl": "concepto",
    "definiciones.jsonl": "definicion",
    "afirmaciones-candidatas.jsonl": "afirmacion",
    "formulas-candidatas.jsonl": "formula",
    "relaciones-explicitas.jsonl": "relacion_explicita",
    "distinciones.jsonl": "distincion",
    "negaciones.jsonl": "negacion",
    "excepciones.jsonl": "excepcion",
    "restricciones-alcance.jsonl": "restriccion_alcance",
}
MASTER_FIELD = {
    "apariciones-conceptuales.jsonl": "apariciones_conceptuales",
    "conceptos.jsonl": "conceptos",
    "definiciones.jsonl": "definiciones",
    "afirmaciones-candidatas.jsonl": "afirmaciones",
    "formulas-candidatas.jsonl": "formulas",
    "relaciones-explicitas.jsonl": "relaciones_explicitas",
    "distinciones.jsonl": "distinciones",
    "negaciones.jsonl": "negaciones",
    "excepciones.jsonl": "excepciones",
    "restricciones-alcance.jsonl": "restricciones_alcance",
}
COVERAGES = (
    "cobertura-conceptos.jsonl",
    "cobertura-definiciones.jsonl",
    "cobertura-afirmaciones.jsonl",
    "cobertura-formulas.jsonl",
    "cobertura-relaciones.jsonl",
    "cobertura-limitadores.jsonl",
)
EXPECTED_COVERAGE_MOTORS = {
    "conceptos_apariciones",
    "definiciones",
    "afirmaciones",
    "formulas",
    "relaciones_explicitas",
    "limitadores",
}
CONCEPTUAL_FILES = {
    "apariciones-conceptuales.jsonl",
    "conceptos.jsonl",
    "definiciones.jsonl",
    "relaciones-explicitas.jsonl",
}


def load_jsonl(path: Path) -> list[dict]:
    if not path.is_file():
        raise AssertionError(f"Falta archivo JSONL: {path}")
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, cwd=ROOT, check=True)


def atomic_validator(schema: dict, def_name: str) -> Draft202012Validator:
    return Draft202012Validator(
        {
            "$schema": schema["$schema"],
            "$defs": schema["$defs"],
            "$ref": f"#/$defs/{def_name}",
        }
    )


def import_assembler():
    spec = importlib.util.spec_from_file_location("ensamblador_maestro_obra_fase10", ASSEMBLER)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def execute_chain(obra_id: str, work_root: Path, master_path: Path) -> None:
    run(
        [
            sys.executable,
            str(EXTRACTOR),
            "--obra-id",
            obra_id,
            "--fuentes",
            str(FUENTES),
            "--unidades",
            str(UNIDADES),
            "--output-root",
            str(work_root),
        ]
    )
    run(
        [
            sys.executable,
            str(NORMALIZER),
            "--input-root",
            str(work_root),
            "--output-root",
            str(work_root / "normalizados"),
        ]
    )
    manifest = json.loads((work_root / "manifest-extractores.json").read_text(encoding="utf-8"))
    formula_version = manifest.get("calibracion", {}).get("formulas", {}).get("version_produccion")
    if not isinstance(formula_version, str) or not formula_version:
        raise AssertionError(f"{obra_id}: manifest sin versión de producción de fórmulas")
    run(
        [
            sys.executable,
            str(VERIFIER),
            "--repo-root",
            str(ROOT),
            "--fuentes",
            str(work_root / "fuente.jsonl"),
            "--unidades",
            str(work_root / "unidades.jsonl"),
            "--input-root",
            str(work_root / "normalizados"),
            "--output-root",
            str(work_root / "verificados"),
            "--producer-version",
            f"formulas={formula_version}",
        ]
    )
    run(
        [
            sys.executable,
            str(STRUCTURAL),
            "--input-root",
            str(work_root / "verificados"),
            "--output-root",
            str(work_root / "auditados"),
            "--unidades",
            str(work_root / "unidades.jsonl"),
        ]
    )
    run(
        [
            sys.executable,
            str(DESCRIPTIVE),
            "--input-root",
            str(work_root / "auditados"),
            "--output",
            str(work_root / "hallazgos-auditoria.jsonl"),
            "--obra-id",
            obra_id,
        ]
    )
    run(
        [
            sys.executable,
            str(ASSEMBLER),
            "--obra-id",
            obra_id,
            "--obra-root",
            str(work_root),
            "--output",
            str(master_path),
        ]
    )


def expected_output_paths(work_root: Path, master_path: Path) -> list[Path]:
    paths = [
        work_root / "fuente.jsonl",
        work_root / "unidades.jsonl",
        work_root / "manifest-extractores.json",
        work_root / "hallazgos-auditoria.jsonl",
        *[work_root / name for name in PRODUCT_TYPES],
        *[work_root / name for name in COVERAGES],
        *[
            work_root / layer / name
            for layer in ("normalizados", "verificados", "auditados")
            for name in PRODUCT_TYPES
        ],
        master_path,
        master_path.with_suffix(master_path.suffix + ".sha256"),
    ]
    assert len(paths) == len(set(paths))
    return paths


def validate_work(obra_id: str, work_root: Path, master_path: Path) -> dict:
    sources = load_jsonl(FUENTES)
    units = load_jsonl(UNIDADES)
    source_rows = [row for row in sources if row.get("id") == obra_id]
    assert len(source_rows) == 1, (obra_id, len(source_rows))
    source = source_rows[0]
    work_units = [row for row in units if row.get("fuente_id") == obra_id]
    assert work_units, f"{obra_id}: sin unidades"
    assert len({row["id"] for row in work_units}) == len(work_units)

    local_source = load_jsonl(work_root / "fuente.jsonl")
    local_units = load_jsonl(work_root / "unidades.jsonl")
    assert local_source == [source]
    assert local_units == work_units

    manifest = json.loads((work_root / "manifest-extractores.json").read_text(encoding="utf-8"))
    assert manifest["version"] == "1.3.0"
    assert manifest["obra_id"] == obra_id
    assert manifest["titulo"] == source["titulo"]
    assert manifest["unidades"] == len(work_units)
    assert manifest["comparacion_interobra"] is False

    glossaries = [r for r in source.get("rutas_derivadas", []) if str(r).endswith("99-glosario.md")]
    assert len(glossaries) <= 1
    has_glossary = bool(glossaries)
    assert manifest["glosario_tecnico"] == (glossaries[0] if has_glossary else None)
    assert manifest["perfil_conceptual"] == (
        "glosario_tecnico_explicito" if has_glossary else "sin_glosario_tecnico_explicito"
    )
    limitations = manifest["limitaciones_conceptuales"]
    assert limitations == {
        "extraccion_conceptual_habilitada": has_glossary,
        "identidades_conceptuales_inferidas": False,
        "glosario_interobra_reutilizado": False,
        "interpretacion_cero_registros": "no_autoriza_afirmar_ausencia_semantica",
    }
    profile = manifest["calibracion"]["formulas"]
    if profile.get("perfil") is not None:
        assert profile["perfil"] == f"analista/calibracion/fase10/{obra_id}/perfil-extractores.json"
        profile_path = ROOT / profile["perfil"]
        assert profile_path.is_file()
        assert profile["perfil_sha256"] == sha(profile_path)
    else:
        assert profile.get("perfil_sha256") is None
        assert profile.get("perfil_calibrado") is False

    for filename, digest in manifest["productos"].items():
        path = work_root / filename
        assert path.is_file(), filename
        assert sha(path) == digest, filename

    old_schema = json.loads(OLD_SCHEMA.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(old_schema)
    for filename, def_name in PRODUCT_TYPES.items():
        raw = load_jsonl(work_root / filename)
        normalized = load_jsonl(work_root / "normalizados" / filename)
        verified = load_jsonl(work_root / "verificados" / filename)
        audited = load_jsonl(work_root / "auditados" / filename)
        assert [row["id"] for row in raw] == [row["id"] for row in normalized] == [row["id"] for row in verified] == [row["id"] for row in audited]
        v = atomic_validator(old_schema, def_name)
        for layer, rows in (("extraido", raw), ("normalizado", normalized), ("verificado", verified), ("auditado", audited)):
            for row in rows:
                errors = list(v.iter_errors(row))
                assert not errors, f"{obra_id}/{layer}/{filename}/{row.get('id')}: {errors[0].message if errors else ''}"
                if "fuente_id" in row:
                    assert row["fuente_id"] == obra_id
        for before, after in zip(raw, normalized):
            b = dict(before)
            a = dict(after)
            for key in ("normalizacion_formal", "normalizacion_lexica"):
                b.pop(key, None)
                a.pop(key, None)
            assert b == a, f"Normalización alteró evidencia en {filename}/{before['id']}"
        assert all(row["estado_verificacion"] == "verificado" for row in verified)
        assert all(
            row["estado_verificacion"] == "verificado" and row["estado_auditoria"] == "auditado"
            for row in audited
        )
        if not has_glossary and filename in CONCEPTUAL_FILES:
            assert raw == normalized == verified == audited == [], f"{obra_id}: {filename} no debe inferirse sin glosario"

    coverage_validator = atomic_validator(old_schema, "reporte_cobertura")
    coverages: list[dict] = []
    for filename in COVERAGES:
        rows = load_jsonl(work_root / filename)
        assert len(rows) == 1, filename
        row = rows[0]
        assert not list(coverage_validator.iter_errors(row)), filename
        assert row["obra_id"] == obra_id
        assert row["unidades_totales"] == row["unidades_procesadas"] == len(work_units)
        assert row["unidades_omitidas"] == [] and row["errores"] == []
        coverages.append(row)
    assert {row["motor"] for row in coverages} == EXPECTED_COVERAGE_MOTORS

    findings = load_jsonl(work_root / "hallazgos-auditoria.jsonl")
    finding_validator = atomic_validator(old_schema, "hallazgo_auditoria")
    for row in findings:
        assert not list(finding_validator.iter_errors(row)), row.get("id")
        assert row["obra_id"] == obra_id
        assert row["resolucion_doctrinal"] == "no_realizada"

    master = json.loads(master_path.read_text(encoding="utf-8"))
    new_schema = json.loads(MASTER_SCHEMA.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(new_schema)
    registry = Registry().with_resource(old_schema["$id"], Resource.from_contents(old_schema))
    errors = list(Draft202012Validator(new_schema, registry=registry).iter_errors(master))
    assert not errors, errors[0].message if errors else ""
    assert master["obra_id"] == obra_id
    assert master["fuentes"] == [source]
    assert master["unidades"] == sorted(work_units, key=lambda row: row["orden_textual"])
    assert master["controles_fase10"]["comparacion_interobra"] is False
    for filename, field in MASTER_FIELD.items():
        assert master[field] == load_jsonl(work_root / "auditados" / filename)
    assert master["hallazgos_auditoria"] == findings
    assert {row["motor"] for row in master["reportes_cobertura"]} == EXPECTED_COVERAGE_MOTORS
    if not has_glossary:
        assert not master["apariciones_conceptuales"]
        assert not master["conceptos"]
        assert not master["definiciones"]
        assert not master["relaciones_explicitas"]

    assembler = import_assembler()
    assembler.validate_traceability(master)
    for entry in master["trazabilidad_archivos"]:
        path = Path(entry["ruta"])
        if not path.is_absolute():
            path = ROOT / path
        assert path.is_file(), entry["ruta"]
        assert sha(path) == entry["sha256"], entry["ruta"]

    sidecar = master_path.with_suffix(master_path.suffix + ".sha256")
    digest, filename = sidecar.read_text(encoding="utf-8").strip().split("  ", 1)
    assert filename == master_path.name
    assert digest == sha(master_path)

    serialized = json.dumps(master, ensure_ascii=False, sort_keys=True)
    other_source_ids = {row["id"] for row in sources if row["id"] != obra_id}
    assert all(other_id not in serialized for other_id in other_source_ids), f"{obra_id}: contaminación interobra por ID de fuente"

    return {
        "obra_id": obra_id,
        "titulo": source["titulo"],
        "unidades": len(work_units),
        "perfil_conceptual": manifest["perfil_conceptual"],
        "registros_auditados": sum(len(master[field]) for field in MASTER_FIELD.values()),
        "hallazgos": len(findings),
        "maestro_sha256": sha(master_path),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--obra-id", required=True)
    args = parser.parse_args()
    if args.obra_id == PILOT:
        raise SystemExit("El piloto AA-SP-V1 conserva su cierre de Fase 9; use validar_maestro_fase9.py")

    work_root = ROOT / "analista/generado/obras" / args.obra_id
    master_path = ROOT / "analista/generado/maestros" / f"{args.obra_id}.json"
    execute_chain(args.obra_id, work_root, master_path)
    result = validate_work(args.obra_id, work_root, master_path)

    paths = expected_output_paths(work_root, master_path)
    first = {path: path.read_bytes() for path in paths}
    execute_chain(args.obra_id, work_root, master_path)
    second = {path: path.read_bytes() for path in paths}
    assert first == second, f"{args.obra_id}: la cadena no es byte-reproducible"
    result2 = validate_work(args.obra_id, work_root, master_path)
    assert result == result2

    print(json.dumps({"fase": 10, "estado": "obra_validada", **result}, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
