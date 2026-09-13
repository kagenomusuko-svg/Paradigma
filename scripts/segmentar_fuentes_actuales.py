#!/usr/bin/env python3
"""Ejecuta los segmentadores históricos contra los nombres canónicos vigentes.

Los parsers existentes se conservan sin refactorización. Este adaptador resuelve
los renombrados de fuentes y corrige únicamente incompatibilidades estructurales
comprobadas entre los parsers históricos y las ediciones canónicas vigentes.
"""

from __future__ import annotations

from collections import Counter
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
    "El_dilema_de_Aquiles_o_la_disociacion_del_ego.md": "El dilema de Aquiles o la disforia de la identidad.md".replace("disforia", "disociación"),
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


def _normalize_markdown_heading(raw: str) -> str:
    newline = "\n" if raw.endswith("\n") else ""
    text = raw.rstrip("\r\n")
    text = re.sub(r"^\s*#{1,6}\s+", "", text)
    stripped = text.strip()
    if len(stripped) >= 4 and stripped.startswith("**") and stripped.endswith("**"):
        text = stripped[2:-2]
    return text + newline


def boundaries_axiomatizacion_vigente(lines):
    result = []
    prologue = next(i for i, line in enumerate(lines) if line.strip() == "## Prólogo")
    result.append(segmentar_lote_02.unit(prologue, "prologo", "01-prologo.md", "PROLOGO", "Prólogo"))
    expected = ["0", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
    found = []
    for index, raw in enumerate(lines):
        match = re.fullmatch(r"#{1,6}\s+Parte\s+(0|[IVX]+)(?:\s*[·.]\s*.*)?", raw.strip())
        if not match:
            continue
        code = match.group(1)
        if len(found) < len(expected) and code == expected[len(found)]:
            found.append(code)
            number = 0 if code == "0" else segmentar_lote_02.roman_to_int(code)
            result.append(segmentar_lote_02.unit(index, "parte", f"parte-{number:02d}.md", f"PARTE-{code}", raw.strip()))
    if found != expected:
        raise RuntimeError(f"Secuencia de partes inesperada en Axiomatización: {found}")
    last_part = max(item["start"] for item in result if item["kind"] == "parte")
    for letter in "ABCD":
        pattern = re.compile(rf"#{{1,6}}\s+Apéndice\s+{letter}(?:\s*[·.]\s*.*)?", re.IGNORECASE)
        index = next(i for i in range(last_part + 1, len(lines)) if pattern.fullmatch(lines[i].strip()))
        result.append(segmentar_lote_02.unit(index, "apendice", f"apendice-{letter.lower()}.md", f"AP-{letter}", lines[index].strip()))
    return result


def boundaries_eco_vigente(lines):
    normalized = [_normalize_markdown_heading(line) for line in lines]
    return segmentar_lote_02.boundaries_eco(normalized)


def boundaries_calculo_vigente(lines):
    result = []
    prologue = next(i for i, line in enumerate(lines) if _normalize_markdown_heading(line).strip() == "PRÓLOGO")
    result.append(segmentar_lote_02.unit(prologue, "prologo", "01-prologo.md", "PROLOGO", "PRÓLOGO"))
    expected = 1
    chapter_pattern = re.compile(r"#{1,6}\s+Capítulo\s+(\d+)(?:\s+.*)?")
    for index, raw in enumerate(lines):
        match = chapter_pattern.fullmatch(raw.strip())
        if match and int(match.group(1)) == expected:
            start = segmentar_lote_02.prefix_start(lines, index, r"## PARTE .*", 4)
            result.append(segmentar_lote_02.unit(start, "capitulo", f"capitulo-{expected:02d}.md", str(expected), raw.strip()))
            expected += 1
            if expected == 19:
                break
    if expected != 19:
        raise RuntimeError(f"Se esperaban 18 capítulos en El cálculo; se detectaron {expected-1}")
    last = result[-1]["start"]
    for letter in "ABCDE":
        appendix_pattern = re.compile(rf"APÉNDICE\s+{letter}(?:\s+.*)?", re.IGNORECASE)
        index = next(i for i in range(last + 1, len(lines)) if appendix_pattern.fullmatch(_normalize_markdown_heading(lines[i]).strip()))
        result.append(segmentar_lote_02.unit(index, "apendice", f"apendice-{letter.lower()}.md", letter, f"APÉNDICE {letter}"))
    return result


def boundaries_prometeo_vigente(lines):
    result = []
    prologue = next(i for i, line in enumerate(lines) if re.match(r"^#{1,6}\s+Prólogo(?:\s|$)", line.strip(), re.IGNORECASE))
    result.append(segmentar_lote_02.unit(prologue, "prologo", "01-prologo.md", "PROLOGO", lines[prologue].strip()))
    chapters = []
    for index, raw in enumerate(lines):
        match = re.fullmatch(r"### Capítulo (\d+)(?:\s+.*)?", raw.strip())
        if not match:
            continue
        if any(previous == "EL MÉTODO PROMETEO · IMPUTACIÓN CAUSAL" for _, previous in segmentar_lote_02.previous_nonblank(lines, index, 5)):
            chapters.append((index, int(match.group(1)), raw.strip()))
    if not chapters:
        raise RuntimeError("Método Prometeo: no se detectaron capítulos con el patrón canónico vigente.")
    occurrences = Counter(number for _, number, _ in chapters)
    used = Counter()
    for index, number, heading in chapters:
        used[number] += 1
        suffix = ""
        if occurrences[number] > 1:
            suffix = chr(ord("a") + used[number] - 1)
        result.append(segmentar_lote_02.unit(index, "capitulo", f"capitulo-{number:02d}{suffix}.md", f"{number}{suffix}", heading))
    last = chapters[-1][0]
    for letter in "ABC":
        pattern = re.compile(rf"#{{1,6}}\s+Apéndice\s+{letter}(?:\s+.*)?", re.IGNORECASE)
        index = next(i for i in range(last + 1, len(lines)) if pattern.fullmatch(lines[i].strip()))
        result.append(segmentar_lote_02.unit(index, "apendice", f"apendice-{letter.lower()}.md", letter, lines[index].strip()))
    return result


def boundaries_histos_vigente(lines):
    """Conserva los cortes históricos de HISTOS y admite Markdown en los preliminares."""
    result = []
    for number in range(1, 6):
        pattern = re.compile(rf"#{{1,6}}\s+Capítulo\s+P·{number}(?:\s+.*)?", re.IGNORECASE)
        index = next(i for i, line in enumerate(lines) if pattern.fullmatch(line.strip()))
        start = segmentar_lote_02.prefix_start(lines, index, r"PARTE PRELIMINAR · Fundamentos del instrumento", 3)
        result.append(segmentar_lote_02.unit(start, "capitulo", f"capitulo-p-{number}.md", f"P·{number}", lines[index].strip()))
    for index, raw in enumerate(lines):
        match = re.fullmatch(r"### Capítulo ([IVX]+)·(\d+)(?:\s+.*)?", raw.strip())
        if not match:
            continue
        block = None
        for position, previous in segmentar_lote_02.previous_nonblank(lines, index, 3):
            if re.match(r"^BLOQUE [IVX]+ ·", previous):
                block = position
                break
        if block is None:
            continue
        roman, number = match.group(1), int(match.group(2))
        result.append(segmentar_lote_02.unit(block, "capitulo", f"capitulo-{segmentar_lote_02.roman_to_int(roman):02d}-{number:02d}.md", f"{roman}·{number}", raw.strip()))
    return result


def adapt_specs() -> None:
    for module in SEGMENTERS:
        for spec in module.SPECS:
            spec["source"] = SOURCE_ALIASES.get(spec["source"], spec["source"])
    segmentar_lote_02.PARSERS["axiomatizacion"] = boundaries_axiomatizacion_vigente
    segmentar_lote_02.PARSERS["eco"] = boundaries_eco_vigente
    segmentar_lote_02.PARSERS["calculo"] = boundaries_calculo_vigente
    segmentar_lote_02.PARSERS["prometeo"] = boundaries_prometeo_vigente
    segmentar_lote_02.PARSERS["histos"] = boundaries_histos_vigente


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
