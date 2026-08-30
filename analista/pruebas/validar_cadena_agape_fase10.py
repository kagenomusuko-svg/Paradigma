#!/usr/bin/env python3
"""Replay integral de la cadena intraobra de Ágape en Fase 10.

Ejecuta, en el orden vinculante ya implementado, los validadores y productores
que componen el tramo actual de repetición controlada. No añade reglas de
extracción, no modifica configuraciones doctrinales y no sustituye la revisión
humana: únicamente ofrece un punto de entrada local reproducible equivalente al
workflow de GitHub Actions.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AGAPE = "FUE-2C28F35DD6CF"

ETAPAS: tuple[tuple[str, list[str]], ...] = (
    (
        "inventario_fase10",
        [sys.executable, "analista/pruebas/validar_inventario_fase10.py"],
    ),
    (
        "extraccion_4a_4f",
        [
            sys.executable,
            "analista/motores/ejecutar_extractores_obra_fase10.py",
            "--obra-id",
            AGAPE,
        ],
    ),
    (
        "muestra_precalibracion",
        [sys.executable, "analista/pruebas/validar_muestra_agape_fase10.py"],
    ),
    (
        "calibracion_formulas_4d",
        [sys.executable, "analista/pruebas/validar_formulas_agape_fase10.py"],
    ),
    (
        "repeticion_extractores",
        [sys.executable, "analista/pruebas/validar_repeticion_agape_fase10.py"],
    ),
    (
        "verificacion_evidencia",
        [sys.executable, "analista/pruebas/validar_verificacion_agape_fase10.py"],
    ),
    (
        "auditoria_intraobra",
        [sys.executable, "analista/pruebas/validar_auditoria_agape_fase10.py"],
    ),
)


def ejecutar(nombre: str, comando: list[str]) -> dict:
    print(f"\n=== Fase 10 Ágape: {nombre} ===", flush=True)
    result = subprocess.run(
        comando,
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.stdout:
        print(result.stdout, end="" if result.stdout.endswith("\n") else "\n")
    if result.stderr:
        print(result.stderr, end="" if result.stderr.endswith("\n") else "\n", file=sys.stderr)
    estado = {
        "etapa": nombre,
        "returncode": result.returncode,
        "comando": comando,
    }
    if result.returncode != 0:
        print(json.dumps({"estado": "fallo", **estado}, ensure_ascii=False, sort_keys=True))
        raise SystemExit(result.returncode)
    print(json.dumps({"estado": "ok", **estado}, ensure_ascii=False, sort_keys=True))
    return estado


def main() -> int:
    completadas = [ejecutar(nombre, comando) for nombre, comando in ETAPAS]
    print(
        json.dumps(
            {
                "estado": "cadena_intraobra_validada",
                "obra_id": AGAPE,
                "etapas": [row["etapa"] for row in completadas],
                "cantidad_etapas": len(completadas),
                "avance_fase10": "sin_cierre_global",
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
