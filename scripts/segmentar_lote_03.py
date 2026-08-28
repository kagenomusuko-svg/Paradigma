#!/usr/bin/env python3
"""Segmentación conservadora de Arquitectura ontológica de sistemas artificiales.

La fuente íntegra en corpus/fuentes/ es canónica. Este programa solo crea
copias derivadas y valida que su concatenación reproduzca exactamente la fuente.
"""

from __future__ import annotations

from pathlib import Path
import hashlib
import json
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
FUENTES = ROOT / "corpus" / "fuentes"

SPECS = [
    {
        "source": "Arquitectura_Ontologica_Sistemas_Artificiales.md",
        "dest": "corpus/libros/arquitectura-ontologica-sistemas-artificiales",
        "id": "AOSA",
        "title": "Arquitectura ontológica de sistemas artificiales",
        "collection": "Metrología Causal",
        "parser": "arquitectura_artificial",
    }
]


def previous_nonblank(lines, index, max_back=5):
    result = []
    for position in range(index - 1, max(-1, index - max_back - 1), -1):
        value = lines[position].strip()
        if value:
            result.append((position, value))
    return result


def chapter_start(lines, index):
    """Incluye la cabecera de Parte inmediatamente anterior, cuando existe."""
    for position, value in previous_nonblank(lines, index, 4):
        if re.fullmatch(r"(?:## )?Parte (?:0|[IVX]+) · .+", value):
            return position
    return index


def boundaries_architecture(lines):
    result = []

    notes = next(i for i, line in enumerate(lines) if line.strip() == "## Notas del autor")
    result.append({
        "start": notes,
        "kind": "notas",
        "filename": "01-notas-del-autor.md",
        "key": "NOTAS",
        "heading": "Notas del autor",
    })

    chapters = []
    for index, raw in enumerate(lines):
        match = re.fullmatch(r"### Capítulo (\d+)\.(\d+)", raw.strip())
        if match:
            major, minor = map(int, match.groups())
            chapters.append((index, major, minor, raw.strip()))

    expected = (
        [(0, 1), (0, 2)]
        + [(part, chapter) for part in range(1, 6) for chapter in range(1, 4)]
        + [(6, chapter) for chapter in range(1, 5)]
        + [(7, chapter) for chapter in range(1, 4)]
    )
    detected = [(major, minor) for _, major, minor, _ in chapters]
    if detected != expected:
        raise RuntimeError(f"Secuencia de capítulos inesperada: {detected}")

    for index, major, minor, heading in chapters:
        result.append({
            "start": chapter_start(lines, index),
            "kind": "capitulo",
            "filename": f"capitulo-{major:02d}-{minor:02d}.md",
            "key": f"{major}.{minor}",
            "heading": heading,
        })

    glossary = next(i for i, line in enumerate(lines) if line.strip() == "## Glosario de términos")
    result.append({
        "start": glossary,
        "kind": "glosario",
        "filename": "99-glosario.md",
        "key": "GLOSARIO",
        "heading": "Glosario de términos",
    })
    return result


def segment(spec):
    source = FUENTES / spec["source"]
    if not source.exists():
        return None

    text = source.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    boundaries = sorted(boundaries_architecture(lines), key=lambda item: item["start"])

    starts = [item["start"] for item in boundaries]
    if len(starts) != len(set(starts)):
        raise RuntimeError("Se detectaron límites de segmentación duplicados.")

    destination = ROOT / spec["dest"]
    if destination.exists():
        shutil.rmtree(destination)
    destination.mkdir(parents=True)

    first = boundaries[0]["start"]
    prelim = destination / "00-preliminares.md"
    prelim.write_text("".join(lines[:first]), encoding="utf-8", newline="")
    segments = [{
        "path": str(prelim.relative_to(ROOT)).replace("\\", "/"),
        "kind": "preliminares",
        "start_line": 1,
        "end_line": first,
    }]

    for position, item in enumerate(boundaries):
        start = item["start"]
        end = boundaries[position + 1]["start"] if position + 1 < len(boundaries) else len(lines)
        target = destination / item["filename"]
        target.write_text("".join(lines[start:end]), encoding="utf-8", newline="")
        segments.append({
            "path": str(target.relative_to(ROOT)).replace("\\", "/"),
            "kind": item["kind"],
            "key": item["key"],
            "heading": item["heading"],
            "start_line": start + 1,
            "end_line": end,
        })

    reconstructed = b"".join((ROOT / item["path"]).read_bytes() for item in segments)
    if reconstructed != source.read_bytes():
        raise RuntimeError(f"La segmentación no reconstruye exactamente {source.name}")

    metadata = {
        "id": spec["id"],
        "title": spec["title"],
        "source": str(source.relative_to(ROOT)).replace("\\", "/"),
        "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "collection": spec["collection"],
        "segmentation_rule": "Cortes estructurales conservadores; la fuente íntegra es canónica.",
        "segments": segments,
    }
    (destination / "estructura.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return metadata


def main():
    processed = []
    missing = []
    for spec in SPECS:
        metadata = segment(spec)
        if metadata is None:
            missing.append(spec["source"])
        else:
            processed.append(metadata["title"])
    print(f"Tercer lote segmentado y validado: {len(processed)} obras.")
    if missing:
        print(f"Fuentes del lote aún no presentes: {len(missing)}")


if __name__ == "__main__":
    main()
