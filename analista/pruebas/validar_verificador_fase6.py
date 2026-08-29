#!/usr/bin/env python3
"""Valida Fase 6 sobre productos reales y fallos mecánicos inducidos."""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "analista/esquema/contratos-v1.0.0.schema.json"
FUENTES = ROOT / "analista/generado/fuentes.jsonl"
UNIDADES = ROOT / "analista/generado/unidades.jsonl"
INPUT = ROOT / "analista/generado/normalizados"
OUTPUT = ROOT / "analista/generado/verificados"
MOTOR = ROOT / "analista/motores/verificador_evidencia.py"

FILES = {
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
EXPECTED_COUNTS = {
    "apariciones-conceptuales.jsonl": 2575,
    "conceptos.jsonl": 21,
    "definiciones.jsonl": 60,
    "afirmaciones-candidatas.jsonl": 333,
    "formulas-candidatas.jsonl": 21,
    "relaciones-explicitas.jsonl": 83,
    "distinciones.jsonl": 26,
    "negaciones.jsonl": 1509,
    "excepciones.jsonl": 1,
    "restricciones-alcance.jsonl": 3,
}
TOTAL_ESPERADO = sum(EXPECTED_COUNTS.values())


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def dump_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows),
        encoding="utf-8",
    )


def validator_for(schema: dict, name: str) -> Draft202012Validator:
    return Draft202012Validator(
        {"$schema": schema["$schema"], "$defs": schema["$defs"], "$ref": f"#/$defs/{name}"}
    )


def run_verifier(
    *,
    input_root: Path = INPUT,
    output_root: Path = OUTPUT,
    fuentes: Path = FUENTES,
    unidades: Path = UNIDADES,
    expected_code: int = 0,
) -> subprocess.CompletedProcess[str]:
    command = [
        sys.executable,
        str(MOTOR),
        "--repo-root",
        str(ROOT),
        "--fuentes",
        str(fuentes),
        "--unidades",
        str(unidades),
        "--input-root",
        str(input_root),
        "--output-root",
        str(output_root),
    ]
    completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    assert completed.returncode == expected_code, (
        completed.returncode,
        completed.stdout,
        completed.stderr,
    )
    return completed


def status(output_root: Path, filename: str, record_id: str) -> str:
    return next(
        row["estado_verificacion"]
        for row in load_jsonl(output_root / filename)
        if row["id"] == record_id
    )


def copy_inputs(destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    for filename in FILES:
        shutil.copy2(INPUT / filename, destination / filename)


def main() -> int:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    validators = {filename: validator_for(schema, ref) for filename, ref in FILES.items()}

    completed = run_verifier()
    assert '"fallidos": 0' in completed.stdout
    assert f'"verificados": {TOTAL_ESPERADO}' in completed.stdout

    total = 0
    snapshot: dict[str, bytes] = {}
    for filename, expected_count in EXPECTED_COUNTS.items():
        source_rows = load_jsonl(INPUT / filename)
        verified_rows = load_jsonl(OUTPUT / filename)
        assert len(source_rows) == len(verified_rows) == expected_count, filename
        snapshot[filename] = (OUTPUT / filename).read_bytes()
        total += len(verified_rows)

        for source, verified in zip(source_rows, verified_rows):
            errors = list(validators[filename].iter_errors(verified))
            assert not errors, f"Registro verificado inválido {verified.get('id')}: {errors[0].message}"
            changed = {
                key
                for key in set(source) | set(verified)
                if source.get(key) != verified.get(key)
            }
            assert changed == {"estado_verificacion"}, (
                filename,
                source["id"],
                changed,
            )
            assert source["estado_verificacion"] == "pendiente"
            assert verified["estado_verificacion"] == "verificado"

    assert total == TOTAL_ESPERADO == 4632

    run_verifier()
    for filename, content in snapshot.items():
        assert (OUTPUT / filename).read_bytes() == content, f"Salida no reproducible: {filename}"

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)

        bad_sources = tmp / "fuentes.jsonl"
        source_rows = load_jsonl(FUENTES)
        for row in source_rows:
            if row["id"] == "AA-SP-V1":
                row["sha256"] = "0" * 64
                row["version_fuente"] = "sha256:" + "0" * 64
        dump_jsonl(bad_sources, source_rows)
        bad_output = tmp / "bad-hash"
        run_verifier(output_root=bad_output, fuentes=bad_sources, expected_code=2)
        assert all(
            row["estado_verificacion"] == "fallido"
            for filename in FILES
            for row in load_jsonl(bad_output / filename)
        )

        formula = load_jsonl(INPUT / "formulas-candidatas.jsonl")[0]
        bad_units = tmp / "unidades.jsonl"
        unit_rows = load_jsonl(UNIDADES)
        for row in unit_rows:
            if row["id"] == formula["unidad_id"]:
                row["sha256_texto"] = "0" * 64
        dump_jsonl(bad_units, unit_rows)
        bad_output = tmp / "bad-unit"
        run_verifier(output_root=bad_output, unidades=bad_units, expected_code=2)
        assert status(bad_output, "formulas-candidatas.jsonl", formula["id"]) == "fallido"

        mutated = tmp / "mut-text"
        copy_inputs(mutated)
        rows = load_jsonl(mutated / "formulas-candidatas.jsonl")
        record_id = rows[0]["id"]
        rows[0]["formula_literal"] += " X"
        rows[0]["texto_literal"] = rows[0]["formula_literal"]
        dump_jsonl(mutated / "formulas-candidatas.jsonl", rows)
        bad_output = tmp / "bad-text"
        run_verifier(input_root=mutated, output_root=bad_output, expected_code=2)
        assert status(bad_output, "formulas-candidatas.jsonl", record_id) == "fallido"

        mutated = tmp / "mut-range"
        copy_inputs(mutated)
        rows = load_jsonl(mutated / "definiciones.jsonl")
        record_id = rows[0]["id"]
        rows[0]["localizacion"]["linea_fin"] = 999999
        dump_jsonl(mutated / "definiciones.jsonl", rows)
        bad_output = tmp / "bad-range"
        run_verifier(input_root=mutated, output_root=bad_output, expected_code=2)
        assert status(bad_output, "definiciones.jsonl", record_id) == "fallido"

        mutated = tmp / "mut-ref"
        copy_inputs(mutated)
        rows = load_jsonl(mutated / "relaciones-explicitas.jsonl")
        record_id = rows[0]["id"]
        rows[0]["objeto_ref"] = "CON-INEXISTENTE"
        dump_jsonl(mutated / "relaciones-explicitas.jsonl", rows)
        bad_output = tmp / "bad-ref"
        run_verifier(input_root=mutated, output_root=bad_output, expected_code=2)
        assert status(bad_output, "relaciones-explicitas.jsonl", record_id) == "fallido"

        mutated = tmp / "mut-version"
        copy_inputs(mutated)
        rows = load_jsonl(mutated / "negaciones.jsonl")
        record_id = rows[0]["id"]
        rows[0]["producido_por"]["version"] = "9.9.9"
        dump_jsonl(mutated / "negaciones.jsonl", rows)
        bad_output = tmp / "bad-version"
        run_verifier(input_root=mutated, output_root=bad_output, expected_code=2)
        assert status(bad_output, "negaciones.jsonl", record_id) == "fallido"

    run_verifier()
    print(
        "OK Fase 6: 4632 registros verificados mecánicamente; 0 fallidos; "
        "salida reproducible; solo cambia estado_verificacion; hash, unidad, literal, "
        "rango, referencias y versiones incorrectas producen fallo expreso."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
