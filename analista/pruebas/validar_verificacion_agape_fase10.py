#!/usr/bin/env python3
from __future__ import annotations

import copy
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AGAPE = "FUE-2C28F35DD6CF"
OBRA = ROOT / "analista/generado/obras" / AGAPE
NORMALIZADOR = ROOT / "analista/motores/normalizacion.py"
VERIFICADOR = ROOT / "analista/motores/verificador_evidencia.py"
NORMALIZADOS = OBRA / "normalizados"
VERIFICADOS = OBRA / "verificados"
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
PILOT_VERIFIED = ROOT / "analista/generado/verificados"


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


def run_normalizer(input_root: Path, output_root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(NORMALIZADOR),
            "--input-root",
            str(input_root),
            "--output-root",
            str(output_root),
        ],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )


def run_verifier(
    input_root: Path,
    output_root: Path,
    formula_version: str | None,
) -> subprocess.CompletedProcess[str]:
    cmd = [
        sys.executable,
        str(VERIFICADOR),
        "--repo-root",
        str(ROOT),
        "--fuentes",
        str(OBRA / "fuente.jsonl"),
        "--unidades",
        str(OBRA / "unidades.jsonl"),
        "--input-root",
        str(input_root),
        "--output-root",
        str(output_root),
    ]
    if formula_version is not None:
        cmd.extend(["--producer-version", f"formulas={formula_version}"])
    return subprocess.run(
        cmd,
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )


def comparable(record: dict) -> dict:
    result = copy.deepcopy(record)
    result.pop("estado_verificacion", None)
    return result


def main() -> int:
    assert (OBRA / "manifest-extractores.json").is_file(), "Primero debe existir la extracción aislada de Ágape"
    manifest = json.loads((OBRA / "manifest-extractores.json").read_text(encoding="utf-8"))
    assert manifest["obra_id"] == AGAPE
    formula_calibration = manifest["calibracion"]["formulas"]
    assert formula_calibration["version_produccion"] == "1.3.0"
    assert formula_calibration["perfil_calibrado"] is True

    pilot_hashes = {
        name: sha(PILOT_VERIFIED / name)
        for name in FILES
        if (PILOT_VERIFIED / name).is_file()
    }
    assert pilot_hashes, "No existe producto verificado del piloto para controlar aislamiento"

    normalized = run_normalizer(OBRA, NORMALIZADOS)
    assert normalized.returncode == 0, normalized.stderr + normalized.stdout

    # La versión calibrada no se acepta implícitamente: la autorización debe ser exacta.
    with tempfile.TemporaryDirectory() as td:
        rejected_root = Path(td) / "sin-autorizacion"
        rejected = run_verifier(NORMALIZADOS, rejected_root, formula_version=None)
        assert rejected.returncode == 2, rejected.stderr + rejected.stdout
        rejected_formulas = load_jsonl(rejected_root / "formulas-candidatas.jsonl")
        assert rejected_formulas
        assert all(row["estado_verificacion"] == "fallido" for row in rejected_formulas)
        assert "version_o_productor" in rejected.stdout

    verified = run_verifier(NORMALIZADOS, VERIFICADOS, formula_version="1.3.0")
    assert verified.returncode == 0, verified.stderr + verified.stdout

    total = 0
    for name in FILES:
        source_rows = load_jsonl(NORMALIZADOS / name)
        verified_rows = load_jsonl(VERIFICADOS / name)
        assert len(source_rows) == len(verified_rows), name
        total += len(verified_rows)
        for source_row, verified_row in zip(source_rows, verified_rows, strict=True):
            assert verified_row["id"] == source_row["id"]
            assert verified_row["estado_verificacion"] == "verificado"
            assert verified_row["estado_auditoria"] == "pendiente"
            assert comparable(verified_row) == comparable(source_row), verified_row["id"]

    formulas = load_jsonl(VERIFICADOS / "formulas-candidatas.jsonl")
    assert len(formulas) == 33
    assert all(row["producido_por"] == {"motor": "formulas", "version": "1.3.0"} for row in formulas)
    assert all(row["clasificacion_formula"] == "formula_explicita" for row in formulas)

    for name, before in pilot_hashes.items():
        assert sha(PILOT_VERIFIED / name) == before, f"La verificación de Ágape modificó el piloto: {name}"

    # Reproducibilidad exacta de normalización + verificación.
    with tempfile.TemporaryDirectory() as td:
        base = Path(td)
        replay_normalized = base / "normalizados"
        replay_verified = base / "verificados"
        replay_norm = run_normalizer(OBRA, replay_normalized)
        assert replay_norm.returncode == 0, replay_norm.stderr + replay_norm.stdout
        replay_ver = run_verifier(replay_normalized, replay_verified, formula_version="1.3.0")
        assert replay_ver.returncode == 0, replay_ver.stderr + replay_ver.stdout
        for name in FILES:
            assert (NORMALIZADOS / name).read_bytes() == (replay_normalized / name).read_bytes(), name
            assert (VERIFICADOS / name).read_bytes() == (replay_verified / name).read_bytes(), name

    # Prueba negativa de evidencia: adulterar un literal no puede conservar estado verificado.
    with tempfile.TemporaryDirectory() as td:
        altered_root = Path(td) / "normalizados-adulterados"
        for name in FILES:
            rows = load_jsonl(NORMALIZADOS / name)
            if name == "formulas-candidatas.jsonl":
                assert rows
                rows[0] = copy.deepcopy(rows[0])
                rows[0]["formula_literal"] = rows[0]["formula_literal"] + " [ADULTERADA]"
            dump_jsonl(altered_root / name, rows)
        altered_verified = Path(td) / "verificados-adulterados"
        altered = run_verifier(altered_root, altered_verified, formula_version="1.3.0")
        assert altered.returncode == 2
        altered_formulas = load_jsonl(altered_verified / "formulas-candidatas.jsonl")
        assert altered_formulas[0]["estado_verificacion"] == "fallido"
        assert "evidencia_directa" in altered.stdout or "excepcion_verificacion" in altered.stdout

    print(
        "OK Fase 10 Ágape verificación: "
        f"{total} registros normalizados y sellados contra fuente; "
        "4D v1.3 requiere autorización explícita; piloto intacto; "
        "reproducción exacta y adulteración literal rechazada."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
