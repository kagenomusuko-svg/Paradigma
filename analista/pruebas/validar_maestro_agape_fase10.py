#!/usr/bin/env python3
"""Regresión específica del maestro de Ágape sobre la cadena genérica Fase 10."""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AGAPE = "FUE-2C28F35DD6CF"
PILOTO = "AA-SP-V1"
OBRA = ROOT / "analista/generado/obras" / AGAPE
MASTER = ROOT / "analista/generado/maestros" / f"{AGAPE}.json"
GENERIC = ROOT / "analista/pruebas/validar_obra_fase10.py"
ASSEMBLER = ROOT / "analista/motores/ensamblador_maestro_obra_fase10.py"
PROFILE = ROOT / "analista/calibracion/fase10" / AGAPE / "perfil-extractores.json"


def import_assembler():
    spec = importlib.util.spec_from_file_location("ensamblador_maestro_obra_fase10", ASSEMBLER)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def expect_trace_failure(module, master: dict, text: str) -> None:
    try:
        module.validate_traceability(master)
    except AssertionError as exc:
        assert text in str(exc), (text, exc)
        return
    raise AssertionError(f"La mutación debía fallar: {text}")


def main() -> int:
    subprocess.run(
        [sys.executable, str(GENERIC), "--obra-id", AGAPE],
        cwd=ROOT,
        check=True,
    )
    master = json.loads(MASTER.read_text(encoding="utf-8"))
    module = import_assembler()

    assert master["id"] == f"MAE-{AGAPE}"
    assert master["obra_id"] == AGAPE
    assert master["titulo"] == "Afrodita Areia: Ágape"
    assert master["schema_version"] == "1.3.0"
    assert master["producido_por"] == {
        "motor": "ensamblador_maestro_obra_fase10",
        "version": "1.1.0",
    }
    assert len(master["fuentes"]) == 1 and master["fuentes"][0]["id"] == AGAPE
    assert len(master["unidades"]) == 643

    formulas = master["formulas"]
    assert len(formulas) == 33
    assert all(
        row["producido_por"] == {"motor": "formulas", "version": "1.3.0"}
        for row in formulas
    )

    controls = master["controles_fase10"]
    assert controls["version"] == "1.1.0"
    assert controls["comparacion_interobra"] is False
    scope = controls["alcance_conceptual"]
    assert scope["perfil"] == "glosario_tecnico_explicito"
    assert isinstance(scope["glosario_tecnico"], str) and scope["glosario_tecnico"].endswith("99-glosario.md")
    assert scope["extraccion_conceptual_habilitada"] is True
    assert scope["identidades_conceptuales_inferidas"] is False
    assert scope["glosario_interobra_reutilizado"] is False
    assert scope["interpretacion_cero_registros"] == "no_autoriza_afirmar_ausencia_semantica"

    calibration = controls["calibracion_formulas"]
    assert calibration["perfil_calibrado"] is True
    assert calibration["version_produccion"] == "1.3.0"
    assert calibration["perfil"] == f"analista/calibracion/fase10/{AGAPE}/perfil-extractores.json"
    assert PROFILE.is_file()
    assert calibration["perfil_sha256"] == hashlib.sha256(PROFILE.read_bytes()).hexdigest()

    findings = master["hallazgos_auditoria"]
    assert all(row["resolucion_doctrinal"] == "no_realizada" for row in findings)
    coverage = master["reportes_cobertura"]
    assert len(coverage) == 6
    assert all(row["obra_id"] == AGAPE for row in coverage)
    assert all(row["unidades_totales"] == row["unidades_procesadas"] == 643 for row in coverage)
    assert all(not row["unidades_omitidas"] and not row["errores"] for row in coverage)

    trace = master["trazabilidad_archivos"]
    assert len(trace) == 41
    for entry in trace:
        path = Path(entry["ruta"])
        if not path.is_absolute():
            path = ROOT / path
        assert path.is_file(), entry["ruta"]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == entry["sha256"]

    assert PILOTO not in MASTER.read_text(encoding="utf-8")
    module.validate_traceability(master)

    broken = copy.deepcopy(master)
    broken["fuentes"][0]["id"] = PILOTO
    expect_trace_failure(module, broken, "solo la fuente de su obra")

    broken = copy.deepcopy(master)
    broken["controles_fase10"]["comparacion_interobra"] = True
    expect_trace_failure(module, broken, "no permite comparación interobra")

    broken = copy.deepcopy(master)
    broken["controles_fase10"]["alcance_conceptual"]["glosario_interobra_reutilizado"] = True
    expect_trace_failure(module, broken, "reutilizar glosarios interobra")

    broken = copy.deepcopy(master)
    broken["controles_fase10"]["alcance_conceptual"]["interpretacion_cero_registros"] = "ausencia_semantica"
    expect_trace_failure(module, broken, "semántica conservadora")

    if findings:
        broken = copy.deepcopy(master)
        broken["hallazgos_auditoria"][0]["resolucion_doctrinal"] = "armonizada"
        expect_trace_failure(module, broken, "resolución doctrinal")

    print(
        "OK Fase 10 Ágape maestro v1.3: 643 unidades, 33 fórmulas calibradas, "
        "alcance conceptual explícito, trazabilidad íntegra, sin comparación interobra "
        "y mutaciones epistemológicamente indebidas rechazadas."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
