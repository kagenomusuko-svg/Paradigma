#!/usr/bin/env python3
"""Segmenta conservadoramente las fuentes Markdown del corpus.

Regla fundamental: `corpus/fuentes/` es canónico. Este programa solo genera
copias derivadas en `corpus/libros/` y metadatos de estructura.
"""

from __future__ import annotations

from pathlib import Path
import hashlib
import json
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
FUENTES = ROOT / "corpus" / "fuentes"

ROMAN = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roman_to_int(value: str) -> int:
    total = 0
    previous = 0
    for char in reversed(value):
        number = ROMAN[char]
        if number < previous:
            total -= number
        else:
            total += number
            previous = number
    return total


def exact(value: str):
    return lambda line: line == value


def regex(pattern: str):
    compiled = re.compile(pattern)
    return lambda line: bool(compiled.fullmatch(line))


SPECS = [
    {
        "source": "Afrodita_Areia_Sobre_la_Pasion.md",
        "dest": "corpus/libros/afrodita-areia/01-sobre-la-pasion",
        "title": "Afrodita Areia: Sobre la pasión",
        "series": "Afrodita Areia",
        "volume": 1,
        "markers": [
            ("prefacio", exact("## Prefacio")),
            ("prologo", exact("Prólogo filosófico")),
            ("chapter", regex(r"### Capítulo \d+")),
            ("appendix", regex(r"## Apéndice [ABC]")),
            ("glossary", exact("## Glosario de términos")),
        ],
    },
    {
        "source": "Afrodita_Areia_Agape.md",
        "dest": "corpus/libros/afrodita-areia/02-agape",
        "title": "Afrodita Areia: Ágape",
        "series": "Afrodita Areia",
        "volume": 2,
        "markers": [
            ("prefacio", exact("## Prefacio")),
            ("prologo", exact("## Prólogo Filosófico")),
            ("chapter", regex(r"### CAPÍTULO \d+")),
            ("appendix", exact("## APÉNDICE")),
            ("glossary", exact("## Glosario de términos")),
        ],
    },
    {
        "source": "Afrodita_Areia_Damasen.md",
        "dest": "corpus/libros/afrodita-areia/03-damasen",
        "title": "Afrodita Areia: Damasén",
        "series": "Afrodita Areia",
        "volume": 3,
        "markers": [
            ("prefacio", exact("## Prefacio")),
            ("prologo", exact("PRÓLOGO FILOSÓFICO")),
            ("chapter", regex(r"### CAPÍTULO \d+")),
            ("appendix", exact("## APÉNDICE")),
            ("glossary", exact("## Glosario")),
        ],
    },
    {
        "source": "Afrodita_Areia_Areopopago.md",
        "dest": "corpus/libros/afrodita-areia/04-areopago",
        "title": "Afrodita Areia: Areópago",
        "series": "Afrodita Areia",
        "volume": 4,
        "markers": [
            ("prologo", exact("## Prólogo")),
            ("chapter", regex(r"### CAPÍTULO \d+")),
            ("glossary", exact("## Glosario")),
            ("appendix", regex(r"## APÉNDICE [IVX]+")),
        ],
    },
    {
        "source": "Afrodita_Areia_Caelus.md",
        "dest": "corpus/libros/afrodita-areia/05-caelus",
        "title": "Afrodita Areia: Caelus",
        "series": "Afrodita Areia",
        "volume": 5,
        "markers": [
            ("prologo", exact("## Prólogo")),
            ("chapter", regex(r"### Capítulo \d+")),
            ("epilogo", exact("Epílogo")),
            ("appendix", exact("## Apéndice")),
            ("glossary", exact("## Glosario de términos")),
        ],
    },
    {
        "source": "Afrodita_Areia_Nikomachos.md",
        "dest": "corpus/libros/afrodita-areia/06-nikomachos",
        "title": "Afrodita Areia: Nikomachos — El límite de la predicación",
        "series": "Afrodita Areia",
        "volume": 6,
        "markers": [
            ("prologo", exact("## Prólogo")),
            ("chapter", regex(r"## Capítulo [IVXLCDM]+")),
            ("epilogo", exact("## Epílogo")),
        ],
    },
    {
        "source": "Caos_El_abismo_del_ego_y_la_doble_mediacion.md",
        "dest": "corpus/libros/caos",
        "title": "Caos: El abismo del ego y la doble mediación",
        "markers": [
            ("chapter", regex(r"### Capítulo [IVXLCDM]+")),
            ("appendix", regex(r"### Apéndice [IVXLCDM]+")),
        ],
    },
    {
        "source": "El_dilema_de_Aquiles_o_la_disociacion_del_ego.md",
        "dest": "corpus/libros/dilema-de-aquiles",
        "title": "El dilema de Aquiles o la disociación del ego",
        "markers": [
            ("prologo", exact("PRÓLOGO")),
            ("chapter", regex(r"### CAPÍTULO [IVXLCDM]+")),
            ("epilogo", exact("EPÍLOGO")),
        ],
    },
    {
        "source": "El_juego_de_las_mascaras_o_la_disforia_de_la_identidad.md",
        "dest": "corpus/libros/juego-de-las-mascaras",
        "title": "El juego de las máscaras o la disforia de la identidad",
        "markers": [
            ("prologo", exact("Prólogo")),
            ("chapter", regex(r"### Capítulo [IVXLCDM]+")),
            ("epilogo", exact("Epílogo")),
            ("glossary", exact("## Glosario")),
        ],
    },
    {
        "source": "El_telar_de_las_Moiras_Ontologia_de_la_autodeterminacion_causal.md",
        "dest": "corpus/libros/telar-de-las-moiras",
        "title": "El telar de las Moiras: Ontología de la autodeterminación causal",
        "markers": [
            ("presentacion", exact("Presentación")),
            ("chapter", regex(r"### Capítulo [IVXLCDM]+")),
            ("epilogo", lambda line: line.startswith("Epílogo:")),
            ("appendix", regex(r"### APÉNDICE [IVXLCDM]+")),
        ],
    },
]


def unit_number(heading: str) -> int:
    raw = re.search(r"(\d+|[IVXLCDM]+)$", heading).group(1)
    return int(raw) if raw.isdigit() else roman_to_int(raw)


def filename(kind: str, heading: str) -> str:
    if kind == "prefacio":
        return "01-prefacio.md"
    if kind == "presentacion":
        return "01-presentacion.md"
    if kind == "prologo":
        return "02-prologo.md"
    if kind == "epilogo":
        return "90-epilogo.md"
    if kind == "glossary":
        return "99-glosario.md"
    if kind == "chapter":
        return f"capitulo-{unit_number(heading):02d}.md"
    if kind == "appendix":
        match = re.search(r"(?:Apéndice|APÉNDICE)\s+([A-C]|[IVXLCDM]+)$", heading)
        if not match:
            return "apendice.md"
        value = match.group(1)
        if value in {"A", "B", "C"}:
            return f"apendice-{value.lower()}.md"
        return f"apendice-{roman_to_int(value):02d}.md"
    raise ValueError(kind)


def detect_boundaries(lines: list[str], spec: dict) -> list[tuple[int, str, str]]:
    candidates = []
    special_seen = set()
    for index, raw_line in enumerate(lines):
        line = raw_line.strip()
        for kind, predicate in spec["markers"]:
            if not predicate(line):
                continue
            if kind in {"prefacio", "prologo", "presentacion", "epilogo", "glossary"}:
                if kind == "glossary" and not any(item[1] == "chapter" for item in candidates):
                    break
                if kind in special_seen:
                    break
                special_seen.add(kind)
            candidates.append((index, kind, line))
            break

    result = []
    expected_chapter = 1
    expected_appendix = 1
    for item in sorted(candidates):
        index, kind, heading = item
        if kind == "chapter":
            number = unit_number(heading)
            if number != expected_chapter:
                continue
            expected_chapter += 1
        elif kind == "appendix":
            match = re.search(r"(?:Apéndice|APÉNDICE)\s+([A-C]|[IVXLCDM]+)$", heading)
            if match and match.group(1) not in {"A", "B", "C"}:
                number = roman_to_int(match.group(1))
                if number != expected_appendix:
                    continue
                expected_appendix += 1
        result.append(item)
    return result


def segment(spec: dict) -> dict:
    source = FUENTES / spec["source"]
    if not source.exists():
        raise FileNotFoundError(source)

    text = source.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    boundaries = detect_boundaries(lines, spec)
    destination = ROOT / spec["dest"]
    if destination.exists():
        shutil.rmtree(destination)
    destination.mkdir(parents=True)

    first = boundaries[0][0] if boundaries else len(lines)
    prelim = destination / "00-preliminares.md"
    prelim.write_text("".join(lines[:first]), encoding="utf-8")
    segments = [{"path": str(prelim.relative_to(ROOT)), "kind": "preliminares", "start_line": 1, "end_line": first}]

    for position, (start, kind, heading) in enumerate(boundaries):
        end = boundaries[position + 1][0] if position + 1 < len(boundaries) else len(lines)
        target = destination / filename(kind, heading)
        target.write_text("".join(lines[start:end]), encoding="utf-8")
        segments.append({
            "path": str(target.relative_to(ROOT)),
            "kind": kind,
            "heading": heading,
            "start_line": start + 1,
            "end_line": end,
        })

    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    metadata = {
        "title": spec["title"],
        "source": str(source.relative_to(ROOT)),
        "sha256": digest,
        "series": spec.get("series"),
        "volume": spec.get("volume"),
        "segmentation_rule": "Cortes conservadores; la fuente íntegra es canónica.",
        "segments": segments,
    }
    (destination / "estructura.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    reconstructed = b"".join((ROOT / item["path"]).read_bytes() for item in segments)
    if reconstructed != source.read_bytes():
        raise RuntimeError(f"La segmentación no reconstruye exactamente {source.name}")
    return metadata


def main() -> None:
    catalog = []
    hashes = []
    for spec in SPECS:
        metadata = segment(spec)
        catalog.append(metadata)
        hashes.append((metadata["sha256"], metadata["source"]))

    (FUENTES / "SHA256SUMS.txt").write_text(
        "\n".join(f"{digest}  {path}" for digest, path in hashes) + "\n",
        encoding="utf-8",
    )
    (ROOT / "corpus" / "catalogo-generado.json").write_text(
        json.dumps(catalog, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Segmentación validada: {len(catalog)} obras.")


if __name__ == "__main__":
    main()
