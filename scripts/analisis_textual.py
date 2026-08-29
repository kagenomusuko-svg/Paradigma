#!/usr/bin/env python3
"""Extractor textual determinista para el corpus Paradigma.

v0.1 no "comprende" el paradigma. Construye evidencia auditable:
- unidades textuales con líneas y contexto de encabezados;
- conceptos explícitos tomados del glosario;
- definiciones explícitas del glosario;
- afirmaciones candidatas por marcadores de alta precisión;
- fórmulas candidatas literales;
- índice de apariciones.

No crea equivalencias, contradicciones, dependencias ni inferencias.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import unicodedata
from pathlib import Path
from typing import Iterable

VERSION = "0.1.0"

ROMAN_RE = re.compile(r"^[IVXLCDM]+$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
ARROW_RE = re.compile(r"^\s*→")
FORMULA_RE = re.compile(r"[=]")
SPACE_RE = re.compile(r"\s+")
EXPLICIT_MARKERS = (
    "la tesis de este capítulo es",
    "la tesis central",
    "este sistema sostiene",
    "este sistema propone",
    "este sistema afirma",
    "este sistema rechaza",
    "la posición de este libro es",
    "puede formularse así",
    "se define como",
    "la definición",
)


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s).casefold()
    return SPACE_RE.sub(" ", s).strip()


def stable_id(prefix: str, *parts: str) -> str:
    payload = "\x1f".join(parts).encode("utf-8")
    return f"{prefix}-{hashlib.sha1(payload).hexdigest()[:12].upper()}"


def dump_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def dump_jsonl(path: Path, rows: Iterable[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def paragraphs(path: Path, root: Path) -> list[dict]:
    lines = path.read_text(encoding="utf-8").splitlines()
    rel = path.relative_to(root).as_posix()
    heading_stack: list[tuple[int, str]] = []
    out: list[dict] = []
    buf: list[str] = []
    start = 0

    def current_context() -> list[str]:
        return [title for _, title in heading_stack]

    def flush(end_line: int) -> None:
        nonlocal buf, start
        if not buf:
            return
        text = "\n".join(buf).strip()
        if text:
            uid = stable_id("UT", rel, str(start), text)
            out.append(
                {
                    "id": uid,
                    "tipo": "parrafo",
                    "ruta": rel,
                    "linea_inicio": start,
                    "linea_fin": end_line,
                    "encabezados": current_context(),
                    "texto": text,
                }
            )
        buf = []
        start = 0

    for n, raw in enumerate(lines, start=1):
        m = HEADING_RE.match(raw)
        if m:
            flush(n - 1)
            level = len(m.group(1))
            title = m.group(2).strip()
            heading_stack = [(l, t) for l, t in heading_stack if l < level]
            heading_stack.append((level, title))
            uid = stable_id("UT", rel, str(n), raw)
            out.append(
                {
                    "id": uid,
                    "tipo": "encabezado",
                    "ruta": rel,
                    "linea_inicio": n,
                    "linea_fin": n,
                    "encabezados": current_context(),
                    "texto": raw,
                }
            )
            continue
        if not raw.strip():
            flush(n - 1)
            continue
        if not buf:
            start = n
        buf.append(raw)
    flush(len(lines))
    return out


def parse_glossary(path: Path, root: Path) -> list[dict]:
    lines = path.read_text(encoding="utf-8").splitlines()
    rel = path.relative_to(root).as_posix()
    entries: list[dict] = []
    i = 0
    while i < len(lines) and "glosario" not in norm(lines[i]):
        i += 1
    i += 1

    while i < len(lines):
        candidate = lines[i].strip()
        if not candidate or candidate.startswith("#") or ROMAN_RE.match(candidate):
            i += 1
            continue
        if norm(candidate).startswith(("los términos ", "sistema.", "introducido ")):
            i += 1
            continue

        term = candidate
        term_line = i + 1
        i += 1
        definition_lines: list[str] = []
        def_start = None
        arrow_line = None

        while i < len(lines):
            s = lines[i].strip()
            if ARROW_RE.match(s):
                arrow_line = i + 1
                i += 1
                break
            if s and not ROMAN_RE.match(s) and not s.startswith("#"):
                if def_start is None:
                    def_start = i + 1
                definition_lines.append(s)
            i += 1

        if not definition_lines or arrow_line is None:
            continue

        text = " ".join(definition_lines)
        cid = stable_id("CON", norm(term))
        did = stable_id("DEF", rel, str(term_line), term, text)
        entries.append(
            {
                "concepto_id": cid,
                "definicion_id": did,
                "lema": term,
                "ruta": rel,
                "linea_lema": term_line,
                "linea_inicio": def_start,
                "linea_fin": arrow_line - 1,
                "texto_literal": text,
                "remision": lines[arrow_line - 1].strip(),
            }
        )
    return entries


def candidate_assertions(units: list[dict], source_id: str) -> list[dict]:
    rows = []
    for u in units:
        if u["tipo"] != "parrafo":
            continue
        ntext = norm(u["texto"])
        markers = [m for m in EXPLICIT_MARKERS if m in ntext]
        if not markers:
            continue
        aid = stable_id("AF", u["id"], "|".join(markers))
        rows.append(
            {
                "id": aid,
                "tipo_registro": "afirmacion_candidata",
                "estatus_epistemico": "candidata_explicita",
                "verificacion": "pendiente",
                "fuente_id": source_id,
                "unidad_id": u["id"],
                "ruta": u["ruta"],
                "linea_inicio": u["linea_inicio"],
                "linea_fin": u["linea_fin"],
                "marcadores": markers,
                "texto_fuente": u["texto"],
                "contenido_normalizado": None,
                "conceptos": [],
                "depende_de": [],
                "conduce_a": [],
                "puente_inferencial": None,
                "confianza_extraccion": 0.75,
                "observaciones": [
                    "Candidato generado por marcador lingüístico; requiere revisión."
                ],
            }
        )
    return rows


def formula_candidates(units: list[dict], source_id: str) -> list[dict]:
    rows = []
    for u in units:
        for offset, line in enumerate(u["texto"].splitlines()):
            s = line.strip()
            if not s or not FORMULA_RE.search(s) or len(s) > 320 or "http" in s:
                continue
            fid = stable_id("FOR", u["id"], str(offset), s)
            rows.append(
                {
                    "id": fid,
                    "tipo_registro": "formula_candidata",
                    "verificacion": "pendiente",
                    "fuente_id": source_id,
                    "unidad_id": u["id"],
                    "ruta": u["ruta"],
                    "linea_aproximada": u["linea_inicio"] + offset,
                    "texto_literal": s,
                    "interpretacion": None,
                }
            )
    return rows


def build_concepts(glossary: list[dict], units: list[dict], source_id: str) -> list[dict]:
    concepts = []
    for entry in glossary:
        term_n = norm(entry["lema"])
        pattern = re.compile(re.escape(term_n), re.IGNORECASE)
        appearances = []
        for u in units:
            if u["tipo"] != "parrafo":
                continue
            if pattern.search(norm(u["texto"])):
                appearances.append(
                    {
                        "unidad_id": u["id"],
                        "ruta": u["ruta"],
                        "linea_inicio": u["linea_inicio"],
                        "linea_fin": u["linea_fin"],
                    }
                )
        concepts.append(
            {
                "id": entry["concepto_id"],
                "tipo_registro": "concepto",
                "lema": entry["lema"],
                "fuente_descubrimiento": "glosario_explicito",
                "fuente_id": source_id,
                "definiciones_explicitas": [entry["definicion_id"]],
                "apariciones": appearances,
                "equivalencias_confirmadas": [],
                "equivalencias_candidatas": [],
                "relaciones": [],
                "tensiones": [],
                "estado": "extraido_no_revisado",
            }
        )
    return concepts


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()

    repo = Path(".").resolve()
    config = json.loads(Path(args.config).read_text(encoding="utf-8"))
    source_id = config["id"]
    book_dir = repo / config["directorio"]
    out_dir = repo / config["salida"]
    glossary_path = book_dir / config["glosario"]

    if not book_dir.is_dir():
        raise SystemExit(f"No existe el directorio de obra: {book_dir}")
    if not glossary_path.is_file():
        raise SystemExit(f"No existe el glosario: {glossary_path}")

    md_files = sorted(book_dir.glob("*.md"))
    units: list[dict] = []
    for path in md_files:
        units.extend(paragraphs(path, repo))

    glossary = parse_glossary(glossary_path, repo)
    if not glossary:
        raise SystemExit("No se extrajo ninguna entrada del glosario; abortando.")

    definitions = []
    for e in glossary:
        definitions.append(
            {
                "id": e["definicion_id"],
                "tipo_registro": "definicion",
                "estatus_epistemico": "explicita",
                "verificacion": "pendiente",
                "fuente_id": source_id,
                "concepto_id": e["concepto_id"],
                "lema": e["lema"],
                "evidencia": {
                    "ruta": e["ruta"],
                    "linea_inicio": e["linea_inicio"],
                    "linea_fin": e["linea_fin"],
                    "texto_literal": e["texto_literal"],
                    "remision": e["remision"],
                },
                "contenido_normalizado": None,
                "observaciones": [
                    "Clasificada como explícita porque proviene del glosario técnico de la obra.",
                    "No equivale todavía a una definición doctrinal consolidada entre obras.",
                ],
            }
        )

    concepts = build_concepts(glossary, units, source_id)
    assertions = candidate_assertions(units, source_id)
    formulas = formula_candidates(units, source_id)

    out_dir.mkdir(parents=True, exist_ok=True)
    dump_jsonl(out_dir / "unidades.jsonl", units)
    dump_json(out_dir / "conceptos.json", concepts)
    dump_jsonl(out_dir / "definiciones.jsonl", definitions)
    dump_jsonl(out_dir / "afirmaciones-candidatas.jsonl", assertions)
    dump_jsonl(out_dir / "formulas-candidatas.jsonl", formulas)
    dump_json(
        out_dir / "reporte.json",
        {
            "extractor_version": VERSION,
            "fuente_id": source_id,
            "titulo": config["titulo"],
            "fuente_canonica": config["fuente_canonica"],
            "directorio_analizado": config["directorio"],
            "archivos_markdown": len(md_files),
            "unidades": len(units),
            "conceptos_glosario": len(concepts),
            "definiciones_explicitas_glosario": len(definitions),
            "afirmaciones_candidatas": len(assertions),
            "formulas_candidatas": len(formulas),
            "reglas": {
                "crea_inferencias": False,
                "crea_equivalencias": False,
                "crea_contradicciones": False,
                "modifica_fuentes": False,
            },
        },
    )
    print(
        f"Análisis v{VERSION}: {len(units)} unidades, {len(concepts)} conceptos, "
        f"{len(definitions)} definiciones explícitas, {len(assertions)} afirmaciones candidatas, "
        f"{len(formulas)} fórmulas candidatas."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
