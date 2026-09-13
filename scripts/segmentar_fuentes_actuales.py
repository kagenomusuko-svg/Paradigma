#!/usr/bin/env python3
"""Ejecuta los segmentadores históricos contra los nombres canónicos vigentes.

Los parsers existentes se conservan sin refactorización. Este adaptador sólo
resuelve los renombrados de las fuentes canónicas y exige que cada fuente
esperada exista antes de generar derivados.
"""

from __future__ import annotations

from pathlib import Path

import segmentar_corpus
import segmentar_lote_02
import segmentar_lote_03

ROOT = Path(__file__).resolve().parents[1]
FUENTES = ROOT / "corpus" / "fuentes"

SOURCE_ALIASES = {
    "Afrodita_Areia_Sobre_la_Pasion.md": "Afrodita Areia sobre la pasión.md",
    "Afrodita_Areia_Agape.md": "Afrodita Areia Ágape.md",
    "Afrodita_Areia_Damasen.md": "Afrodita Areia Damasén.md",
    "Afrodita_Areia_Areopopago.md": "Afrodita Areia Areópago.md",
    "Afrodita_Areia_Caelus.md": "Afrodita Areia Caelus.md",
    "El_dilema_de_Aquiles_o_la_disociacion_del_ego.md": "El dilema de Aquiles o la disociación del ego.md",
    "El_juego_de_las_mascaras_o_la_disforia_de_la_identidad.md": "El juego de las máscaras o la disforia de la identidad.md",
    "El_telar_de_las_Moiras_Ontologia_de_la_autodeterminacion_causal.md": "El telar de las Moiras Ontología de la autodeterminación causal.md",
    "Axiomatizacion_Sistema_Doble_Mediacion.md": "Axiomatización del sistema de la doble mediación.md",
    "ECO_Entrevista_Clinica_Ontologica.md": "ECO Entrevista Clínica Ontológica.md",
    "El_calculo_de_la_responsabilidad.md": "El cálculo de la responsabilidad una ontología matemática para sistemas causales complejos.md",
    "El_metodo_Prometeo_imputacion_causal_para_juristas_y_abogados.md": "El método Prometeo imputación causal para juristas y abogados.md",
    "HISTOS_Protocolo_de_Acompanamiento_Ontologico.md": "HISTOS Protocolo de Acompañamiento Ontológico.md",
    "La_transformacion_formal_ontologia_del_ego_como_fundamento_del_calculo_causal.md": "La transformación formal la ontología del ego como fundamento del cálculo causal.md",
    "Metrologia_Causal_La_ciencia_de_la_medicion_causal.md": "Metrología Causal La ciencia de la medición causal.md",
    "Metrologia_Causal_Vol_II.md": "Metrología Causal Vol II.md",
    "SDO_Sistema_de_diagnostico_ontologico.md": "SDO Sistema de diagnóstico ontológico.md",
    "Taxonomia_General_de_Aplicaciones.md": "Taxonomía General de Aplicaciones.md",
    "Arquitectura_Ontologica_Sistemas_Artificiales.md": "Arquitectura ontológica de sistemas artificiales.md",
}

SEGMENTERS = (segmentar_corpus, segmentar_lote_02, segmentar_lote_03)


def adapt_specs() -> None:
    for module in SEGMENTERS:
        for spec in module.SPECS:
            spec["source"] = SOURCE_ALIASES.get(spec["source"], spec["source"])


def validate_sources() -> None:
    missing = []
    for module in SEGMENTERS:
        for spec in module.SPECS:
            if not (FUENTES / spec["source"]).is_file():
                missing.append(spec["source"])
    if missing:
        formatted = "\n".join(f"- {name}" for name in sorted(set(missing)))
        raise RuntimeError(f"Fuentes esperadas no encontradas:\n{formatted}")


def main() -> None:
    adapt_specs()
    validate_sources()
    segmentar_corpus.main()
    segmentar_lote_02.main()
    segmentar_lote_03.main()


if __name__ == "__main__":
    main()
