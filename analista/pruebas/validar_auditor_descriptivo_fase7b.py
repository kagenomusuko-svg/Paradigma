#!/usr/bin/env python3
"""Valida 7B: hallazgos conservadores sobre registros auditados reales."""
from __future__ import annotations

import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
from collections import Counter, defaultdict
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
EXPECTED_CATEGORIES = {
    "uso_singular": 21,
    "definiciones_multiples": 13,
    "variacion_de_objeto": 11,
    "relacion_repetida": 1,
}


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
    assert '"hallazgos": 46' in first.stdout
    findings = load_jsonl(OUTPUT)
    assert len(findings) == 46
    assert Counter(row["categoria"] for row in findings) == EXPECTED_CATEGORIES

    by_file = {filename: load_jsonl(INPUT / filename) for filename in FILES}
    all_audited = {row["id"]: row for rows in by_file.values() for row in rows}
    concepts = {row["id"]: row for row in by_file["conceptos.jsonl"]}

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

    # Cada hallazgo de definiciones múltiples debe referir definiciones del mismo concepto.
    definitions_by_id = {row["id"]: row for row in by_file["definiciones.jsonl"]}
    for finding in (row for row in findings if row["categoria"] == "definiciones_multiples"):
        rows = [definitions_by_id[record_id] for record_id in finding["registro_ids"]]
        assert len(rows) > 1
        assert len({row["concepto_id"] for row in rows}) == 1

    # Cada variación de objeto conserva un único sujeto y al menos dos objetos, sin relacionarlos entre sí.
    relations_by_id = {row["id"]: row for row in by_file["relaciones-explicitas.jsonl"]}
    variations = [row for row in findings if row["categoria"] == "variacion_de_objeto"]
    assert len(variations) == 11
    for finding in variations:
        rows = [relations_by_id[record_id] for record_id in finding["registro_ids"]]
        assert len({row["sujeto_ref"] for row in rows}) == 1
        assert len({row["objeto_ref"] for row in rows}) > 1

    aego_id = next(cid for cid, row in concepts.items() if row["designacion_operativa"] == "Aego")
    aego_variation = next(
        finding for finding in variations
        if {relations_by_id[rid]["sujeto_ref"] for rid in finding["registro_ids"]} == {aego_id}
    )
    aego_objects = {
        concepts[relations_by_id[record_id]["objeto_ref"]]["designacion_operativa"]
        for record_id in aego_variation["registro_ids"]
    }
    assert aego_objects == {
        "Afasia volitiva", "Ego", "Mediación bis", "Mediación neutral", "Singularidad ontológica"
    }

    repeated = next(row for row in findings if row["categoria"] == "relacion_repetida")
    repeated_rows = [relations_by_id[record_id] for record_id in repeated["registro_ids"]]
    assert len(repeated_rows) == 2
    assert len({(r["sujeto_ref"], r["objeto_ref"], r["relacion_literal"]) for r in repeated_rows}) == 1
    subject, obj, literal = next(iter({(r["sujeto_ref"], r["objeto_ref"], r["relacion_literal"]) for r in repeated_rows}))
    assert concepts[subject]["designacion_operativa"] == "Pasión"
    assert concepts[obj]["designacion_operativa"] == "Determinación"
    assert literal == "la pasión como tendencia de determinación"

    module = import_motor()
    for concept_id in concepts:
        dossier = module.records_for_concept(concept_id, by_file)
        expected = []
        expected.extend(row for row in by_file["apariciones-conceptuales.jsonl"] if row.get("concepto_id") == concept_id)
        expected.extend(row for row in by_file["definiciones.jsonl"] if row.get("concepto_id") == concept_id)
        expected.extend(row for row in by_file["afirmaciones-candidatas.jsonl"] if concept_id in row.get("concepto_ids", []))
        expected.extend(
            row for row in by_file["relaciones-explicitas.jsonl"]
            if row.get("sujeto_ref") == concept_id or row.get("objeto_ref") == concept_id
        )
        assert {row["id"] for row in dossier} == {row["id"] for row in expected}

    # Aego ahora reúne más evidencia explícita, pero los tipos siguen siendo solo referencias existentes.
    aego_dossier = module.records_for_concept(aego_id, by_file)
    assert {row["tipo_registro"] for row in aego_dossier} == {"aparicion_conceptual", "definicion", "relacion_explicita"}
    assert len([row for row in aego_dossier if row["tipo_registro"] == "definicion"]) == 3
    assert len([row for row in aego_dossier if row["tipo_registro"] == "relacion_explicita"]) == 6

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
        "OK Fase 7B: 46 hallazgos descriptivos reproducibles; 21 usos singulares, "
        "13 multiplicidades definicionales, 11 variaciones de objeto y 1 relación repetida; "
        "candidatos de 4F no fueron promovidos y no se realizó resolución doctrinal."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
