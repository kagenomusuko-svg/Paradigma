#!/usr/bin/env python3
"""Replay de compatibilidad para Ágape sobre la cadena genérica de Fase 10.

Conserva un punto de entrada específico para el primer caso de repetición, pero
la lógica de cierre ya es la misma que se aplica a todas las obras no piloto.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AGAPE = "FUE-2C28F35DD6CF"


def run(script: str, *args: str) -> None:
    subprocess.run([sys.executable, str(ROOT / script), *args], cwd=ROOT, check=True)


def main() -> int:
    run("analista/motores/inventariar_obras_fase10.py")
    run("analista/pruebas/validar_inventario_fase10.py")
    run("analista/pruebas/validar_obra_fase10.py", "--obra-id", AGAPE)
    print(
        json.dumps(
            {
                "obra_id": AGAPE,
                "fase": 10,
                "estado": "cadena_intraobra_con_maestro_validada",
                "maestro_independiente": True,
                "comparacion_interobra": False,
                "avance_fase10": "sin_cierre_global",
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
