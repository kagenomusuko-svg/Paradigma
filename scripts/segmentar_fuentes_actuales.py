#!/usr/bin/env python3
"""Ejecuta los segmentadores históricos contra los nombres canónicos vigentes.

Los parsers existentes se conservan sin refactorización. Este adaptador resuelve
los renombrados de fuentes y corrige únicamente incompatibilidades estructurales
comprobadas entre los parsers históricos y las ediciones canónicas vigentes.
"""

from __future__ import annotations

from pathlib import Path
import re

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


def boundaries_axiomatizacion_vigente(lines):
    """Reconoce las Partes/Apéndices como encabezados Markdown de la edición vigente."""
    result = []
    prologue = next(i for i, line in enumerate(lines) if line.strip() == "## Prólogo")
    result.append(segmentar_lote_02.unit(prologue, "prologo", "01-prologo.md", "PROLOGO", "Prólogo"))

    expected = ["0", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
    found = []
    for index, raw in enumerate(lines):
        match = re.fullmatch(r"#{1,6}\s+Parte\s+(0|[IVX]+)", raw.strip())
        if not match:
            continue
        code = match.group(1)
        if len(found) < len(expected) and code == expected[len(found)]:
            found.append(code)
            number = 0 if code == "0" else segmentar_lote_02.roman_to_int(code)
            result.append(
                segmentar_lote_02.unit(index, "parte", f"parte-{number:02d}.md", f"PARTE-{code}", raw.strip())
            )
    if found != expected:
        raise RuntimeError(f"Secuencia de partes inesperada en Axiomatización: {found}")

    last_part = max(item["start"] for item in result if item["kind"] == "parte")
    for letter in "ABCD":
        pattern = re.compile(rf"#{{1,6}}\s+Apéndice\s+{letter}", re.IGNORECASE)
        index = next(
            i for i in range(last_part + 1, len(lines)) if pattern.fullmatch(lines[i].strip())
        )
        result.append(
            segmentar_lote_02.unit(index, "apendice", f"apendice-{letter.lower()}.md", f"AP-{letter}", lines[index].strip())
        )
    return result


def adapt_specs() -> None:
    for module in SEGMENTERS:
        for spec in module.SPECS:
            spec["source"] = SOURCE_ALIASES.get(spec["source"], spec["source"])

    # La edición canónica actual usa encabezados «### Parte N»; el parser
    # histórico esperaba texto plano. La corrección vive aquí para conservar
    # estable el segmentador de lote y limitar el cambio al formato comprobado.
    segmentar_lote_02.PARSERS["axiomatizacion"] = boundaries_axiomatizacion_vigente


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
