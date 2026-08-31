#!/usr/bin/env python3
"""Recuperación conceptual genérica por obra para Fase 10.

Este motor NO interpreta el corpus ni establece identidad conceptual por
semejanza. Recupera designaciones candidatas mediante señales formales y
recurrencia literal dentro de una sola obra. Cada agrupación usa únicamente
NFKC + casefold + normalización de espacios; por ello se mantiene como
``estado_identidad_conceptual = no_determinada``.

Las obras con glosario técnico explícito conservan el motor 4A calibrado para
las identidades declaradas. Este módulo está destinado a ampliar recuperación,
no a sustituir ni debilitar esas identidades verificadas.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_VERSION = "1.0.0"
MOTOR_VERSION = "1.0.0"
MOTOR_NAME = "conceptos_apariciones_fase10"

TOKEN_RE = re.compile(r"[^\W_]+(?:[-‐‑][^\W_]+)*|[φΦψΨ][₀-₉0-9]*", re.UNICODE)
MARKED_RES = (
    re.compile(r"`(?P<t>[^`\n]{1,100})`"),
    re.compile(r"\*\*(?P<t>[^*\n]{1,100})\*\*"),
    re.compile(r"«(?P<t>[^»\n]{1,100})»"),
    re.compile(r"“(?P<t>[^”\n]{1,100})”"),
)
DEFINITIONAL_RES = (
    re.compile(
        r"\b(?:concepto|noción|término|categoría)\s+(?:de\s+|del\s+)?(?P<t>[\wÁÉÍÓÚÜÑáéíóúüñφΦψΨ₀-₉0-9][^,.;:!?\n]{0,78})",
        re.IGNORECASE,
    ),
    re.compile(
        r"\b(?:llamamos|denominamos|denomino|definimos|defino)\s+(?:a\s+)?(?P<t>[\wÁÉÍÓÚÜÑáéíóúüñφΦψΨ₀-₉0-9][^,.;:!?\n]{0,78}?)(?=\s+(?:a|como|cuando|si|el|la|un|una)\b|[,.;:!?]|$)",
        re.IGNORECASE,
    ),
    re.compile(
        r"\bpor\s+(?P<t>[\wÁÉÍÓÚÜÑáéíóúüñφΦψΨ₀-₉0-9][^,.;:!?\n]{0,78}?)\s+se\s+entiende\b",
        re.IGNORECASE,
    ),
    re.compile(
        r"(?P<t>[\wÁÉÍÓÚÜÑáéíóúüñφΦψΨ₀-₉0-9][^,.;:!?\n]{0,78}?)\s+(?:se\s+define\s+como|significa|designa|se\s+denomina)\b",
        re.IGNORECASE,
    ),
)
SENTENCE_BREAK_RE = re.compile(r"[.!?;:\n]")
ROMAN_RE = re.compile(r"^[IVXLCDM]+$", re.IGNORECASE)

# Palabras funcionales: se usan solo para evitar que una secuencia puramente
# gramatical ascienda a candidato. No se lematiza ni se introducen sinónimos.
STOPWORDS = {
    "a", "al", "algo", "ante", "bajo", "cada", "como", "con", "contra", "cual",
    "cuando", "de", "del", "desde", "donde", "dos", "e", "el", "ella", "ellas",
    "ellos", "en", "entre", "era", "es", "esa", "ese", "eso", "esta", "este",
    "esto", "fue", "ha", "hacia", "hasta", "hay", "la", "las", "le", "lo", "los",
    "más", "me", "mi", "mientras", "muy", "ni", "no", "nos", "o", "otra", "otro",
    "para", "pero", "por", "porque", "que", "se", "ser", "si", "sin", "sobre",
    "son", "su", "sus", "también", "te", "toda", "todo", "tras", "tu", "un", "una",
    "uno", "y", "ya",
}


def norm(text: str) -> str:
    return " ".join(unicodedata.normalize("NFKC", text).casefold().split())


def stable_id(prefix: str, *parts: str) -> str:
    payload = "\x1f".join(parts).encode("utf-8")
    return f"{prefix}-{hashlib.sha1(payload).hexdigest()[:12].upper()}"


def load_jsonl(path: Path) -> list[dict]:
    if not path.is_file():
        raise SystemExit(f"No existe insumo requerido: {path}")
    rows: list[dict] = []
    for n, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        try:
            rows.append(json.loads(raw))
        except json.JSONDecodeError as exc:
            raise SystemExit(f"JSONL inválido en {path}:{n}: {exc}") from exc
    return rows


def dump_jsonl(path: Path, rows: Iterable[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows),
        encoding="utf-8",
    )


def base_record(record_id: str, kind: str, literal: str | None) -> dict:
    return {
        "id": record_id,
        "tipo_registro": kind,
        "schema_version": SCHEMA_VERSION,
        "texto_literal": literal,
        "normalizacion_formal": None,
        "normalizacion_lexica": None,
        "estatus_enunciativo": None,
        "estado_extraccion": "candidato",
        "estado_verificacion": "pendiente",
        "estado_auditoria": "pendiente",
        "producido_por": {"motor": MOTOR_NAME, "version": MOTOR_VERSION},
    }


def token_rows(text: str) -> list[tuple[str, str, int, int]]:
    return [(m.group(0), norm(m.group(0)), m.start(), m.end()) for m in TOKEN_RE.finditer(text)]


def valid_token(token_norm: str) -> bool:
    if not token_norm or token_norm in STOPWORDS or ROMAN_RE.fullmatch(token_norm):
        return False
    if token_norm.isdigit():
        return False
    if token_norm.startswith(("φ", "ψ")):
        return True
    return len(token_norm) >= 3


def trim_candidate(tokens: list[tuple[str, str, int, int]], i: int, j: int) -> tuple[int, int] | None:
    while i < j and tokens[i][1] in STOPWORDS:
        i += 1
    while i < j and tokens[j - 1][1] in STOPWORDS:
        j -= 1
    if i >= j:
        return None
    norms = [row[1] for row in tokens[i:j]]
    if not any(valid_token(value) for value in norms):
        return None
    return i, j


def lexical_spans(text: str, max_tokens: int = 4) -> list[tuple[int, int, str, str]]:
    """Secuencias literales candidatas unidas solo por espacio blanco."""
    tokens = token_rows(text)
    spans: list[tuple[int, int, str, str]] = []
    for i in range(len(tokens)):
        for width in range(1, max_tokens + 1):
            j = i + width
            if j > len(tokens):
                break
            trimmed = trim_candidate(tokens, i, j)
            if trimmed is None:
                continue
            a, b = trimmed
            start, end = tokens[a][2], tokens[b - 1][3]
            if end - start > 100:
                continue
            gaps = [text[tokens[k][3]:tokens[k + 1][2]] for k in range(a, b - 1)]
            if any(not gap.isspace() for gap in gaps):
                continue
            between = text[start:end]
            if SENTENCE_BREAK_RE.search(between):
                continue
            literal = between.strip()
            key = norm(literal)
            if not key:
                continue
            spans.append((start, end, key, literal))
    return list(dict.fromkeys(spans))


def formal_spans(text: str) -> list[tuple[int, int, str, str, str]]:
    spans: list[tuple[int, int, str, str, str]] = []
    for pattern in MARKED_RES:
        for match in pattern.finditer(text):
            start, end = match.span("t")
            literal = match.group("t").strip()
            key = norm(literal)
            if literal and 1 <= len(literal.split()) <= 8 and any(valid_token(n) for _, n, _, _ in token_rows(literal)):
                spans.append((start, end, key, literal, "marcador_tipografico_explicito"))
    for pattern in DEFINITIONAL_RES:
        for match in pattern.finditer(text):
            start, end = match.span("t")
            literal = match.group("t").strip()
            tokenized = token_rows(literal)
            if not tokenized:
                continue
            trimmed = trim_candidate(tokenized, 0, len(tokenized))
            if trimmed is None:
                continue
            a, b = trimmed
            offset_start, offset_end = tokenized[a][2], tokenized[b - 1][3]
            literal = literal[offset_start:offset_end]
            start += offset_start
            end = start + len(literal)
            key = norm(literal)
            if literal and 1 <= len(literal.split()) <= 8:
                spans.append((start, end, key, literal, "marcador_definicional_formal"))
    return list(dict.fromkeys(spans))


def line_range(unit: dict, text: str, start: int, end: int) -> tuple[int, int]:
    base = unit["localizacion"]["linea_inicio"]
    line_start = base + text[:start].count("\n")
    line_end = line_start + text[start:end].count("\n")
    return line_start, line_end


def discover_designations(units: list[dict], confirmed_norms: set[str]) -> tuple[set[str], dict[str, str]]:
    unit_counts: Counter[str] = Counter()
    forced: dict[str, str] = {}
    first_literal: dict[str, str] = {}

    for unit in units:
        text = unit["texto_literal"]
        seen_in_unit: set[str] = set()
        for _, _, key, literal in lexical_spans(text):
            if key in confirmed_norms:
                continue
            seen_in_unit.add(key)
            first_literal.setdefault(key, literal)
        for _, _, key, literal, criterion in formal_spans(text):
            if key in confirmed_norms:
                continue
            forced.setdefault(key, criterion)
            first_literal.setdefault(key, literal)
        unit_counts.update(seen_in_unit)

    selected = set(forced)
    selected.update(key for key, count in unit_counts.items() if count >= 2)
    return selected, first_literal


def build_candidate_records(
    obra_id: str,
    units: list[dict],
    *,
    confirmed_norms: set[str] | None = None,
) -> tuple[list[dict], list[dict]]:
    confirmed = confirmed_norms or set()
    selected, first_literal = discover_designations(units, confirmed)
    concept_id_by_key = {key: stable_id("CONC", obra_id, key) for key in selected}
    appearance_rows: list[dict] = []
    appearances_by_concept: dict[str, list[str]] = defaultdict(list)
    forms_by_concept: dict[str, set[str]] = defaultdict(set)
    seen_appearances: set[tuple[str, int, int, str]] = set()

    for unit in units:
        text = unit["texto_literal"]
        candidate_spans: dict[tuple[int, int, str], tuple[str, str]] = {}
        for start, end, key, literal in lexical_spans(text):
            if key in selected:
                candidate_spans[(start, end, key)] = (literal, "recurrencia_literal_intraobra")
        for start, end, key, literal, criterion in formal_spans(text):
            if key in selected:
                candidate_spans[(start, end, key)] = (literal, criterion)

        for (start, end, key), (literal, criterion) in sorted(candidate_spans.items()):
            identity = (unit["id"], start, end, key)
            if identity in seen_appearances:
                continue
            seen_appearances.add(identity)
            cid = concept_id_by_key[key]
            line_start, line_end = line_range(unit, text, start, end)
            aid = stable_id("APC", obra_id, unit["id"], str(start), str(end), key)
            row = base_record(aid, "aparicion_conceptual", literal)
            row.update(
                {
                    "fuente_id": obra_id,
                    "unidad_id": unit["id"],
                    "concepto_id": cid,
                    "forma_literal": literal,
                    "variante_formal": None,
                    "variantes_lexicas_busqueda": [],
                    "localizacion": {
                        "ruta": unit["archivo"],
                        "linea_inicio": line_start,
                        "linea_fin": line_end,
                    },
                    "criterio_deteccion": f"{criterion}; identidad_conceptual_no_determinada",
                }
            )
            appearance_rows.append(row)
            appearances_by_concept[cid].append(aid)
            forms_by_concept[cid].add(literal)

    concept_rows: list[dict] = []
    for key in sorted(selected):
        cid = concept_id_by_key[key]
        aids = appearances_by_concept.get(cid, [])
        if not aids:
            continue
        literal = first_literal[key]
        row = base_record(cid, "concepto", literal)
        row.update(
            {
                "designacion_operativa": literal,
                "aparicion_ids": sorted(aids),
                "formas_literales_observadas": sorted(forms_by_concept[cid], key=lambda value: (norm(value), value)),
                "estado_identidad_conceptual": "no_determinada",
                "evidencia_identidad_ids": [],
            }
        )
        concept_rows.append(row)

    appearance_rows.sort(
        key=lambda row: (
            row["localizacion"]["ruta"],
            row["localizacion"]["linea_inicio"],
            row["localizacion"]["linea_fin"],
            row["unidad_id"],
            row["id"],
        )
    )
    concept_rows.sort(key=lambda row: row["id"])
    return appearance_rows, concept_rows


def coverage_record(obra_id: str, total_units: int) -> dict:
    return {
        "id": stable_id("COB", obra_id, MOTOR_NAME, MOTOR_VERSION),
        "tipo_registro": "reporte_cobertura",
        "schema_version": SCHEMA_VERSION,
        "texto_literal": None,
        "normalizacion_formal": None,
        "normalizacion_lexica": None,
        "estatus_enunciativo": None,
        "estado_extraccion": "extraido",
        "estado_verificacion": "pendiente",
        "estado_auditoria": "no_aplica",
        "producido_por": {"motor": MOTOR_NAME, "version": MOTOR_VERSION},
        "obra_id": obra_id,
        "motor": "conceptos_apariciones",
        "version_motor": MOTOR_VERSION,
        "unidades_totales": total_units,
        "unidades_procesadas": total_units,
        "unidades_omitidas": [],
        "errores": [],
    }


def run(
    *,
    obra_id: str,
    unidades: Path,
    salida_apariciones: Path,
    salida_conceptos: Path,
    cobertura: Path,
    confirmed_norms: set[str] | None = None,
) -> dict:
    rows = load_jsonl(unidades)
    work_units = [row for row in rows if row.get("fuente_id") == obra_id]
    if not work_units:
        raise SystemExit(f"No existen unidades para {obra_id}")
    if len({row["id"] for row in work_units}) != len(work_units):
        raise SystemExit(f"IDs de unidad duplicados en {obra_id}")
    appearances, concepts = build_candidate_records(obra_id, work_units, confirmed_norms=confirmed_norms)
    dump_jsonl(salida_apariciones, appearances)
    dump_jsonl(salida_conceptos, concepts)
    dump_jsonl(cobertura, [coverage_record(obra_id, len(work_units))])
    return {
        "version": MOTOR_VERSION,
        "obra_id": obra_id,
        "unidades": len(work_units),
        "conceptos_candidatos": len(concepts),
        "apariciones_candidatas": len(appearances),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--obra-id", required=True)
    parser.add_argument("--unidades", type=Path, required=True)
    parser.add_argument("--apariciones", type=Path, required=True)
    parser.add_argument("--conceptos", type=Path, required=True)
    parser.add_argument("--cobertura", type=Path, required=True)
    args = parser.parse_args()
    result = run(
        obra_id=args.obra_id,
        unidades=args.unidades,
        salida_apariciones=args.apariciones,
        salida_conceptos=args.conceptos,
        cobertura=args.cobertura,
    )
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
