#!/usr/bin/env python3
"""Valida 7B: hallazgos conservadores sobre registros auditados reales."""
from __future__ import annotations

import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "analista/esquema/contratos-v1.0.0.schema.json"
INPUT = ROOT / "analista/generado/auditados"
OUTPUT = ROOT / "analista/generado/hallazgos-auditoria.jsonl"
MOTOR = ROOT / "analista/motores/auditor_descriptivo.py"
FILES = (
    "apariciones-conceptuales.jsonl",
    "conceptos.jsonl",
    "definiciones.jsonl",
    "afirmaciones-candidatas.jsonl",
    "formulas-candidatas.jsonl",
    "relaciones-explicitas.jsonl",
    "distinciones.jsonl",
    "negaciones.jsonl",
    "excepciones.jsonl",
    "restricciones-alcance.jsonl",
)


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def run(input_root: Path, output: Path, expected_code: int = 0) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        [sys.executable, str(MOTOR), "--input-root", str(input_root), "--output", str(output)],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert result.returncode == expected_code, (result.returncode, result.stdout, result.stderr)
    return result


def import_motor():
    spec = importlib.util.spec_from_file_location("auditor_descriptivo", MOTOR)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    validator = Draft202012Validator(
        {"$schema": schema["$schema"], "$defs": schema["$defs"], "$ref": "#/$defs/hallazgo_auditoria"}
    )

    first = run(INPUT, OUTPUT)
    assert '"hallazgos": 22' in first.stdout
    findings = load_jsonl(OUTPUT)
    assert len(findings) == 22
    assert Counter(row["categoria"] for row in findings) == {
        "uso_singular": 21,
        "variacion_de_objeto": 1,
    }

    all_audited = {
        row["id"]: row
        for filename in FILES
        for row in load_jsonl(INPUT / filename)
    }
    for row in findings:
        errors = list(validator.iter_errors(row))
        assert not errors, f"Hallazgo inválido {row['id']}: {errors[0].message}"
        assert row["estado_verificacion"] == "verificado"
        assert row["estado_auditoria"] == "auditado"
        assert row["resolucion_doctrinal"] == "no_realizada"
        assert row["producido_por"] == {"motor": "auditor_descriptivo", "version": "1.0.0"}
        assert all(record_id in all_audited for record_id in row["registro_ids"])

    assert not any(
        row["categoria"] in {"negacion_explicita", "excepcion_explicita", "restriccion_de_alcance"}
        for row in findings
    ), "Candidatos de 4F no pueden ascender a hallazgos explícitos."

    variation = next(row for row in findings if row["categoria"] == "variacion_de_objeto")
    relation_rows = [all_audited[record_id] for record_id in variation["registro_ids"]]
    assert {row["sujeto_ref"] for row in relation_rows} == {"CON-7D09D3ECB550"}
    assert {row["objeto_ref"] for row in relation_rows} == {
        "CON-463D458232DE",
        "CON-D850F9DB83FB",
    }

    module = import_motor()
    by_file = {filename: load_jsonl(INPUT / filename) for filename in FILES}
    concepts = {row["id"]: row for row in by_file["conceptos.jsonl"]}
    for concept_id in concepts:
        dossier = module.records_for_concept(concept_id, by_file)
        expected = []
        expected.extend(
            row for row in by_file["apariciones-conceptuales.jsonl"] if row.get("concepto_id") == concept_id
        )
        expected.extend(row for row in by_file["definiciones.jsonl"] if row.get("concepto_id") == concept_id)
        expected.extend(
            row for row in by_file["afirmaciones-candidatas.jsonl"] if concept_id in row.get("concepto_ids", [])
        )
        expected.extend(
            row
            for row in by_file["relaciones-explicitas.jsonl"]
            if row.get("sujeto_ref") == concept_id or row.get("objeto_ref") == concept_id
        )
        assert {row["id"] for row in dossier} == {row["id"] for row in expected}

    aego_id = next(
        concept_id
        for concept_id, row in concepts.items()
        if row["designacion_operativa"] == "Aego"
    )
    assert {
        row["tipo_registro"] for row in module.records_for_concept(aego_id, by_file)
    } == {"aparicion_conceptual", "definicion", "relacion_explicita"}
    assert len(module.records_for_concept(aego_id, by_file)) == 5

    snapshot = OUTPUT.read_bytes()
    run(INPUT, OUTPUT)
    assert OUTPUT.read_bytes() == snapshot, "Hallazgos no reproducibles."

    with tempfile.TemporaryDirectory() as temporary:
        temporary = Path(temporary)
        mutated = temporary / "auditados"
        mutated.mkdir()
        for filename in FILES:
            shutil.copy2(INPUT / filename, mutated / filename)
        rows = load_jsonl(mutated / "negaciones.jsonl")
        rows[0]["estado_auditoria"] = "pendiente"
        (mutated / "negaciones.jsonl").write_text(
            "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows),
            encoding="utf-8",
        )
        rejected = temporary / "hallazgos.jsonl"
        run(mutated, rejected, expected_code=1)
        assert not rejected.exists(), "7B no debe producir hallazgos desde entradas no auditadas."

    run(INPUT, OUTPUT)
    print(
        "OK Fase 7B: 22 hallazgos descriptivos reproducibles; 21 usos singulares "
        "registrados y 1 variación de objeto; candidatos de 4F no fueron promovidos; "
        "consulta conceptual exhaustiva solo por referencias explícitas auditadas."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
