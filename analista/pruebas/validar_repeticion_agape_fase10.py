#!/usr/bin/env python3
"""Compatibilidad de la repetición Ágape y de la ruta conservadora sin glosario.

La validación integral de Ágape vive en ``validar_obra_fase10.py``. Este archivo
conserva el punto de entrada histórico y añade una regresión específica para la
ruta sin glosario: procesar una obra sin glosario técnico explícito debe tener
éxito sin inferir identidades conceptuales ni reutilizar evidencia de otra obra.
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GENERIC = ROOT / "analista/pruebas/validar_obra_fase10.py"
EXTRACTOR = ROOT / "analista/motores/ejecutar_extractores_obra_fase10.py"
FUENTES = ROOT / "analista/generado/fuentes.jsonl"
UNIDADES = ROOT / "analista/generado/unidades.jsonl"
AGAPE = "FUE-2C28F35DD6CF"
CONCEPTUAL_FILES = (
    "apariciones-conceptuales.jsonl",
    "conceptos.jsonl",
    "definiciones.jsonl",
    "relaciones-explicitas.jsonl",
)
CONCEPTUAL_COVERAGES = (
    ("cobertura-conceptos.jsonl", "conceptos_apariciones"),
    ("cobertura-definiciones.jsonl", "definiciones"),
    ("cobertura-relaciones.jsonl", "relaciones_explicitas"),
)


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, cwd=ROOT, check=True)


def main() -> int:
    # El punto de entrada histórico sigue validando Ágape, pero delega en la
    # cadena genérica que se usa para las 19 repeticiones de Fase 10.
    run([sys.executable, str(GENERIC), "--obra-id", AGAPE])

    sources = load_jsonl(FUENTES)
    units = load_jsonl(UNIDADES)
    without_glossary = next(
        source
        for source in sources
        if not any(str(route).endswith("99-glosario.md") for route in source.get("rutas_derivadas", []))
    )
    obra_id = without_glossary["id"]
    work_units = [unit for unit in units if unit.get("fuente_id") == obra_id]
    assert work_units, f"{obra_id}: la regresión sin glosario requiere unidades"

    with tempfile.TemporaryDirectory() as td:
        out = Path(td) / obra_id
        run(
            [
                sys.executable,
                str(EXTRACTOR),
                "--obra-id",
                obra_id,
                "--fuentes",
                str(FUENTES),
                "--unidades",
                str(UNIDADES),
                "--output-root",
                str(out),
            ]
        )

        manifest = json.loads((out / "manifest-extractores.json").read_text(encoding="utf-8"))
        assert manifest["version"] == "1.3.0"
        assert manifest["obra_id"] == obra_id
        assert manifest["glosario_tecnico"] is None
        assert manifest["perfil_conceptual"] == "sin_glosario_tecnico_explicito"
        assert manifest["comparacion_interobra"] is False
        assert manifest["limitaciones_conceptuales"] == {
            "extraccion_conceptual_habilitada": False,
            "identidades_conceptuales_inferidas": False,
            "glosario_interobra_reutilizado": False,
            "interpretacion_cero_registros": "no_autoriza_afirmar_ausencia_semantica",
        }

        for filename in CONCEPTUAL_FILES:
            assert load_jsonl(out / filename) == [], (
                f"{obra_id}: {filename} no puede contener identidades o relaciones "
                "conceptuales inferidas sin glosario explícito"
            )

        seen_motors: set[str] = set()
        for filename, expected_motor in CONCEPTUAL_COVERAGES:
            rows = load_jsonl(out / filename)
            assert len(rows) == 1, filename
            coverage = rows[0]
            seen_motors.add(coverage["motor"])
            assert coverage["motor"] == expected_motor
            assert coverage["obra_id"] == obra_id
            assert coverage["unidades_totales"] == len(work_units)
            assert coverage["unidades_procesadas"] == len(work_units)
            assert coverage["unidades_omitidas"] == []
            assert coverage["errores"] == []
        assert seen_motors == {"conceptos_apariciones", "definiciones", "relaciones_explicitas"}

    print(
        "OK Fase 10 compatibilidad: Ágape valida por la cadena genérica y una obra "
        "sin glosario se procesa conservadoramente sin inferir identidad conceptual, "
        "sin reutilizar glosarios interobra y con cobertura mecánica completa."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
