#!/usr/bin/env python3
"""Regresión sintética del recuperador conceptual genérico de Fase 10."""
from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MOTOR = ROOT / "analista/motores/conceptos_obra_fase10.py"

spec = importlib.util.spec_from_file_location("conceptos_obra_fase10", MOTOR)
assert spec and spec.loader
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def unit(uid: str, order: int, text: str) -> dict:
    return {
        "id": uid,
        "fuente_id": "OBRA-X",
        "archivo": "corpus/libros/x/capitulo-01.md",
        "texto_literal": text,
        "localizacion": {
            "linea_inicio": order * 10 + 1,
            "linea_fin": order * 10 + text.count("\n") + 1,
        },
        "orden_textual": order,
    }


def main() -> int:
    units = [
        unit("UT-A", 0, "La primera mediación orienta la voluntad y el acto."),
        unit("UT-B", 1, "La primera mediación condiciona la voluntad."),
        unit("UT-C", 2, "Llamamos autodeterminación causal a esta estructura."),
    ]
    appearances, concepts = mod.build_candidate_records("OBRA-X", units)
    by_norm = {mod.norm(row["designacion_operativa"]): row for row in concepts}

    assert "primera mediación" in by_norm
    assert "voluntad" in by_norm
    assert "autodeterminación causal" in by_norm
    assert all(row["estado_extraccion"] == "candidato" for row in concepts)
    assert all(row["estado_identidad_conceptual"] == "no_determinada" for row in concepts)
    assert all(row["evidencia_identidad_ids"] == [] for row in concepts)
    assert all(row["fuente_id"] == "OBRA-X" for row in appearances)
    assert all(
        "identidad_conceptual_no_determinada" in row["criterio_deteccion"]
        for row in appearances
    )

    # Una designación ya confirmada por el motor calibrado no se duplica como
    # candidato genérico ni se debilita.
    _, filtered = mod.build_candidate_records(
        "OBRA-X", units, confirmed_norms={"primera mediación"}
    )
    assert "primera mediación" not in {
        mod.norm(row["designacion_operativa"]) for row in filtered
    }

    # Sin recurrencia ni marcador formal, una palabra aislada no asciende por sí sola.
    single = [unit("UT-D", 3, "Aparece xylófono una sola vez.")]
    _, single_concepts = mod.build_candidate_records("OBRA-X", single)
    assert "xylófono" not in {
        mod.norm(row["designacion_operativa"]) for row in single_concepts
    }

    print(
        "OK conceptos_obra_fase10: recuperación formal/recurrente sin identidad inferida"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
