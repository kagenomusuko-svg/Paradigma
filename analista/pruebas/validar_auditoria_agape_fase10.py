#!/usr/bin/env python3
from __future__ import annotations

import copy
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
AGAPE = "FUE-2C28F35DD6CF"
OBRA = ROOT / "analista/generado/obras" / AGAPE
VERIFICADOS = OBRA / "verificados"
AUDITADOS = OBRA / "auditados"
HALLAZGOS = OBRA / "hallazgos-auditoria.jsonl"
UNIDADES = OBRA / "unidades.jsonl"
ESTRUCTURAL = ROOT / "analista/motores/auditor_estructural.py"
DESCRIPTIVO = ROOT / "analista/motores/auditor_descriptivo.py"
SCHEMA = ROOT / "analista/esquema/contratos-v1.0.0.schema.json"
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
ALLOWED_FINDING_CATEGORIES = {
    "uso_singular",
    "definiciones_multiples",
    "multiplicidad_predicativa",
    "variacion_de_objeto",
    "relacion_repetida",
    "negacion_explicita",
    "excepcion_explicita",
    "restriccion_de_alcance",
    "variacion_terminologica",
}


def load_jsonl(path: Path) -> list[dict]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line
    ]


def dump_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows),
        encoding="utf-8",
    )


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validator_for(schema: dict, def_name: str) -> Draft202012Validator:
    return Draft202012Validator(
        {
            "$schema": schema["$schema"],
            "$defs": schema["$defs"],
            "$ref": f"#/$defs/{def_name}",
        }
    )


def run_structural(
    input_root: Path,
    output_root: Path,
    unidades: Path = UNIDADES,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(ESTRUCTURAL),
            "--input-root",
            str(input_root),
            "--output-root",
            str(output_root),
            "--unidades",
            str(unidades),
        ],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )


def run_descriptive(
    input_root: Path,
    output: Path,
    obra_id: str = AGAPE,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(DESCRIPTIVO),
            "--input-root",
            str(input_root),
            "--output",
            str(output),
            "--obra-id",
            obra_id,
        ],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )


def main() -> int:
    for name in FILES:
        assert (VERIFICADOS / name).is_file(), f"Falta verificación previa de Ágape: {name}"
    assert UNIDADES.is_file()

    pilot_root = ROOT / "analista/generado/auditados"
    pilot_hashes = {
        name: sha(pilot_root / name)
        for name in FILES
        if (pilot_root / name).is_file()
    }
    assert pilot_hashes, "No existen auditados del piloto para comprobar aislamiento"
    pilot_findings = ROOT / "analista/generado/hallazgos-auditoria.jsonl"
    pilot_findings_hash = sha(pilot_findings) if pilot_findings.is_file() else None

    structural = run_structural(VERIFICADOS, AUDITADOS)
    assert structural.returncode == 0, structural.stderr + structural.stdout

    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    all_audited: dict[str, dict] = {}
    total = 0
    for filename, def_name in FILES.items():
        before = load_jsonl(VERIFICADOS / filename)
        after = load_jsonl(AUDITADOS / filename)
        assert len(before) == len(after), filename
        total += len(after)
        validator = validator_for(schema, def_name)
        for source, audited in zip(before, after, strict=True):
            assert source["id"] == audited["id"]
            errors = list(validator.iter_errors(audited))
            assert not errors, f"{audited['id']}: {errors[0].message if errors else ''}"
            changed = {
                key
                for key in set(source) | set(audited)
                if source.get(key) != audited.get(key)
            }
            assert changed == {"estado_auditoria"}, (audited["id"], changed)
            assert source["estado_verificacion"] == audited["estado_verificacion"] == "verificado"
            assert source["estado_auditoria"] == "pendiente"
            assert audited["estado_auditoria"] == "auditado"
            if "fuente_id" in audited:
                assert audited["fuente_id"] == AGAPE
            all_audited[audited["id"]] = audited

    descriptive = run_descriptive(AUDITADOS, HALLAZGOS)
    assert descriptive.returncode == 0, descriptive.stderr + descriptive.stdout
    findings = load_jsonl(HALLAZGOS)
    finding_validator = validator_for(schema, "hallazgo_auditoria")
    counts = Counter()
    for finding in findings:
        errors = list(finding_validator.iter_errors(finding))
        assert not errors, f"{finding['id']}: {errors[0].message if errors else ''}"
        assert finding["obra_id"] == AGAPE
        assert finding["categoria"] in ALLOWED_FINDING_CATEGORIES
        counts[finding["categoria"]] += 1
        assert finding["resolucion_doctrinal"] == "no_realizada"
        assert finding["texto_literal"] is None
        assert finding["estatus_enunciativo"] is None
        assert finding["estado_verificacion"] == "verificado"
        assert finding["estado_auditoria"] == "auditado"
        assert finding["producido_por"] == {"motor": "auditor_descriptivo", "version": "1.0.0"}
        assert finding["registro_ids"]
        assert all(record_id in all_audited for record_id in finding["registro_ids"])

    # No debe filtrarse identidad del piloto a productos intraobra de Ágape.
    serialized = HALLAZGOS.read_text(encoding="utf-8") + "\n" + "\n".join(
        (AUDITADOS / name).read_text(encoding="utf-8") for name in FILES
    )
    assert "AA-SP-V1" not in serialized

    for name, before in pilot_hashes.items():
        assert sha(pilot_root / name) == before, f"La auditoría de Ágape modificó el piloto: {name}"
    if pilot_findings_hash is not None:
        assert sha(pilot_findings) == pilot_findings_hash

    # Reproducibilidad exacta de 7A y 7B.
    audited_snapshot = {name: (AUDITADOS / name).read_bytes() for name in FILES}
    findings_snapshot = HALLAZGOS.read_bytes()
    second_structural = run_structural(VERIFICADOS, AUDITADOS)
    assert second_structural.returncode == 0
    second_descriptive = run_descriptive(AUDITADOS, HALLAZGOS)
    assert second_descriptive.returncode == 0
    for name, content in audited_snapshot.items():
        assert (AUDITADOS / name).read_bytes() == content, name
    assert HALLAZGOS.read_bytes() == findings_snapshot

    with tempfile.TemporaryDirectory() as td_raw:
        td = Path(td_raw)

        # 7A debe rechazar una entrada cuya evidencia deje de estar verificada.
        mutated = td / "verificados-mutados"
        mutated.mkdir()
        for name in FILES:
            shutil.copy2(VERIFICADOS / name, mutated / name)
        target_file = next(name for name in FILES if load_jsonl(mutated / name))
        rows = load_jsonl(mutated / target_file)
        rows[0] = copy.deepcopy(rows[0])
        rows[0]["estado_verificacion"] = "pendiente"
        target_id = rows[0]["id"]
        dump_jsonl(mutated / target_file, rows)
        rejected_root = td / "auditados-rechazados"
        rejected = run_structural(mutated, rejected_root)
        assert rejected.returncode == 2
        rejected_row = next(
            row for row in load_jsonl(rejected_root / target_file) if row["id"] == target_id
        )
        assert rejected_row["estado_auditoria"] == "rechazado"

        # 7B debe rechazar una identidad de obra incompatible con sus registros.
        wrong_output = td / "hallazgos-obra-incorrecta.jsonl"
        wrong = run_descriptive(AUDITADOS, wrong_output, obra_id="AA-SP-V1")
        assert wrong.returncode != 0
        assert not wrong_output.exists()
        assert "obra distinta" in wrong.stderr + wrong.stdout

    print(
        "OK Fase 10 Ágape auditoría intraobra: "
        f"{total} registros auditados estructuralmente; "
        f"{len(findings)} hallazgos descriptivos en {len(counts)} categorías; "
        "sin resolución doctrinal, sin identidad del piloto, reproducibilidad exacta y mutaciones rechazadas."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
