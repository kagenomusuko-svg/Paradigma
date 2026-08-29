#!/usr/bin/env python3
"""Valida 7A sobre registros reales verificados y mutaciones estructurales."""
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
INPUT = ROOT / "analista/generado/verificados"
OUTPUT = ROOT / "analista/generado/auditados"
UNIDADES = ROOT / "analista/generado/unidades.jsonl"
MOTOR = ROOT / "analista/motores/auditor_estructural.py"
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
    "definiciones.jsonl": 21,
    "afirmaciones-candidatas.jsonl": 73,
    "formulas-candidatas.jsonl": 20,
    "relaciones-explicitas.jsonl": 4,
    "distinciones.jsonl": 26,
    "negaciones.jsonl": 1509,
    "excepciones.jsonl": 1,
    "restricciones-alcance.jsonl": 3,
}


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def dump_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text(
        "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows),
        encoding="utf-8",
    )


def validator(schema: dict, name: str) -> Draft202012Validator:
    return Draft202012Validator(
        {"$schema": schema["$schema"], "$defs": schema["$defs"], "$ref": f"#/$defs/{name}"}
    )


def run(input_root: Path, output_root: Path, expected_code: int) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        [
            sys.executable,
            str(MOTOR),
            "--input-root",
            str(input_root),
            "--output-root",
            str(output_root),
            "--unidades",
            str(UNIDADES),
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert result.returncode == expected_code, (result.returncode, result.stdout, result.stderr)
    return result


def copy_inputs(destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    for filename in FILES:
        shutil.copy2(INPUT / filename, destination / filename)


def audit_status(root: Path, filename: str, record_id: str) -> str:
    return next(row["estado_auditoria"] for row in load_jsonl(root / filename) if row["id"] == record_id)


def main() -> int:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    validators = {filename: validator(schema, ref) for filename, ref in FILES.items()}

    result = run(INPUT, OUTPUT, 0)
    assert '"auditados": 4253' in result.stdout and '"rechazados": 0' in result.stdout

    snapshot: dict[str, bytes] = {}
    total = 0
    for filename, count in EXPECTED_COUNTS.items():
        source = load_jsonl(INPUT / filename)
        audited = load_jsonl(OUTPUT / filename)
        assert len(source) == len(audited) == count
        snapshot[filename] = (OUTPUT / filename).read_bytes()
        total += count
        for before, after in zip(source, audited):
            errors = list(validators[filename].iter_errors(after))
            assert not errors, f"Salida inválida {after['id']}: {errors[0].message}"
            changed = {key for key in set(before) | set(after) if before.get(key) != after.get(key)}
            assert changed == {"estado_auditoria"}, (filename, before["id"], changed)
            assert before["estado_verificacion"] == after["estado_verificacion"] == "verificado"
            assert after["estado_auditoria"] == "auditado"
    assert total == 4253

    run(INPUT, OUTPUT, 0)
    for filename, content in snapshot.items():
        assert (OUTPUT / filename).read_bytes() == content, f"Salida no reproducible: {filename}"

    with tempfile.TemporaryDirectory() as temporary:
        temporary = Path(temporary)

        mutated = temporary / "unverified"
        copy_inputs(mutated)
        rows = load_jsonl(mutated / "negaciones.jsonl")
        record_id = rows[0]["id"]
        rows[0]["estado_verificacion"] = "pendiente"
        dump_jsonl(mutated / "negaciones.jsonl", rows)
        rejected = temporary / "r1"
        run(mutated, rejected, 2)
        assert audit_status(rejected, "negaciones.jsonl", record_id) == "rechazado"

        mutated = temporary / "broken-ref"
        copy_inputs(mutated)
        rows = load_jsonl(mutated / "relaciones-explicitas.jsonl")
        record_id = rows[0]["id"]
        rows[0]["objeto_ref"] = "CON-INEXISTENTE"
        dump_jsonl(mutated / "relaciones-explicitas.jsonl", rows)
        rejected = temporary / "r2"
        run(mutated, rejected, 2)
        assert audit_status(rejected, "relaciones-explicitas.jsonl", record_id) == "rechazado"

        mutated = temporary / "force"
        copy_inputs(mutated)
        rows = load_jsonl(mutated / "negaciones.jsonl")
        record_id = rows[0]["id"]
        rows[0]["estado_extraccion"] = "extraido"
        dump_jsonl(mutated / "negaciones.jsonl", rows)
        rejected = temporary / "r3"
        run(mutated, rejected, 2)
        assert audit_status(rejected, "negaciones.jsonl", record_id) == "rechazado"

        mutated = temporary / "duplicate"
        copy_inputs(mutated)
        rows = load_jsonl(mutated / "excepciones.jsonl")
        record_id = rows[0]["id"]
        rows.append(dict(rows[0]))
        dump_jsonl(mutated / "excepciones.jsonl", rows)
        rejected = temporary / "r4"
        run(mutated, rejected, 2)
        assert all(row["estado_auditoria"] == "rechazado" for row in load_jsonl(rejected / "excepciones.jsonl"))

        mutated = temporary / "formula-context"
        copy_inputs(mutated)
        rows = load_jsonl(mutated / "formulas-candidatas.jsonl")
        record_id = rows[0]["id"]
        rows[0]["contexto_unidad_ids"] = []
        dump_jsonl(mutated / "formulas-candidatas.jsonl", rows)
        rejected = temporary / "r5"
        run(mutated, rejected, 2)
        assert audit_status(rejected, "formulas-candidatas.jsonl", record_id) == "rechazado"

    run(INPUT, OUTPUT, 0)
    print(
        "OK Fase 7A: 4253 registros auditados; 0 rechazados; salida reproducible; "
        "solo cambia estado_auditoria; evidencia pendiente, referencias rotas, fuerza "
        "incoherente, IDs duplicados y contexto de fórmula inválido son rechazados."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
