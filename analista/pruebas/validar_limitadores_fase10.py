#!/usr/bin/env python3
"""Regresiones mecánicas de 4F para repetición controlada de Fase 10.

Los IDs deben identificar ocurrencias textuales, no solo contenido y línea. Dos
limitadores literales iguales en una misma línea siguen siendo dos ocurrencias
si ocupan posiciones distintas. Esta prueba no modifica clasificación ni
interpreta el contenido.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MOTOR = ROOT / "analista/motores/limitadores.py"

spec = importlib.util.spec_from_file_location("limitadores_fase10", MOTOR)
assert spec and spec.loader
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def unit(uid: str, text: str) -> dict:
    return {
        "id": uid,
        "fuente_id": "OBRA-X",
        "archivo": "corpus/libros/x/capitulo-01.md",
        "texto_literal": text,
        "localizacion": {"linea_inicio": 10, "linea_fin": 10 + text.count("\n")},
    }


def main() -> int:
    repeated = mod.negations(unit("UT-N", "No procede. No procede."))
    assert len(repeated) == 2, repeated
    assert [row["texto_literal"] for row in repeated] == ["No procede", "No procede"]
    assert len({row["id"] for row in repeated}) == 2, repeated
    assert all(row["unidad_id"] == "UT-N" for row in repeated)
    assert all(row["localizacion"]["linea_inicio"] == 10 for row in repeated)
    assert all(row["localizacion"]["linea_fin"] == 10 for row in repeated)
    assert all(row["clasificacion_negacion"] == "negacion_explicita" for row in repeated)
    assert all(row["producido_por"] == {"motor": "limitadores", "version": "1.1.1"} for row in repeated)

    print("OK Fase 10 4F: ocurrencias repetidas en una misma línea conservan IDs únicos")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
