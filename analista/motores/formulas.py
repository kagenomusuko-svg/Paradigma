#!/usr/bin/env python3
"""Motor formal de fórmulas — Fase 4D, calibrado en Fase 8.

Las familias formales inequívocas de la obra piloto se recuperan como la
expresión literal mínima completa y se marcan explícitas. Un signo '=' que no
encaje en esos patrones se conserva como candidato mediante el fallback
histórico de oración, sin interpretación matemática ni equivalencias inferidas.
"""
from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
UNIDADES = ROOT / "analista/generado/unidades.jsonl"
SALIDA = ROOT / "analista/generado/formulas-candidatas.jsonl"
COBERTURA = ROOT / "analista/generado/cobertura-formulas.jsonl"
PILOTO_ID = "AA-SP-V1"
SCHEMA_VERSION = "1.0.0"
MOTOR_VERSION = "1.1.0"
TERMINATORS = ".!?"

# Patrones puramente formales observados en la obra piloto. No declaran
# equivalencia entre variantes: cada coincidencia produce su propio registro.
EXPLICIT_PATTERNS = [
    re.compile(
        r"Ego\(t\)\s*=\s*φ₂\s*\(\s*φ₁\s*\(\s*v(?:ₜ|_t)?\s*,\s*c(?:ₜ|_t)?\s*\)\s*,\s*I\(t\)\s*\)"
    ),
    re.compile(r"Ego\(t\)\s*=\s*∫\s*f\(v\)\s*dv"),
    re.compile(r"d/dt\s*\[Ego\(t\)\]\s*=\s*f\(vₜ\)"),
    re.compile(r"Voluntad\s*\+\s*Acto\s*\+\s*Mediación\s*=\s*ser/existir"),
    re.compile(
        r"Identidad\s*\+\s*Voluntad\s*\+\s*"
        r"(?:Primera\s+mediación|φ₁\s*\(\s*v\s*,\s*c\s*\))\s*\+\s*Acto\s*\+\s*"
        r"(?:Segunda\s+mediación|φ₂\s*\(\s*Acto\s*,\s*I\s*\))\s*=\s*Ego\s+primordial"
    ),
    re.compile(
        r"\(Identidad\s*\+\s*Voluntad\s*\+\s*φ₁(?:\s*\([^)]*\))?\s*\+\s*Acto\s*\+\s*"
        r"φ₂(?:\s*\([^)]*\))?\s*=\s*Ego\)\s*ⁿ"
    ),
    re.compile(
        r"\(Identidad\s*\+\s*Voluntad\s*\+\s*φ₁\s*\(\s*v\s*,\s*c\s*\)\s*\+\s*Acto\s*\+\s*"
        r"φ₂\s*\(\s*Acto\s*,\s*I\s*\)\s*\)\s*ⁿ"
    ),
    re.compile(
        r"Si\s+f\(vₜ\)\s*→\s*0,\s*entonces\s*Ego\(t\)\s*=\s*∫\s*0\s*dv\s*=\s*C\s*"
        r"\(constante\s+nula\)"
    ),
    re.compile(r"φ₂\s+interrumpida\s*=\s*la\s+unión\s+entre\s+ambos,\s*disuelta"),
]


def stable_id(prefix: str, *parts: str) -> str:
    raw = "\x1f".join(parts).encode("utf-8")
    return f"{prefix}-{hashlib.sha1(raw).hexdigest()[:12].upper()}"


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def dump_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows),
        encoding="utf-8",
    )


def sentence_span(text: str, position: int) -> tuple[int, int]:
    left = 0
    for i in range(position - 1, -1, -1):
        if text[i] in TERMINATORS and (i + 1 == len(text) or text[i + 1].isspace()):
            left = i + 1
            break
    right = len(text)
    for i in range(position, len(text)):
        if text[i] in TERMINATORS and (i + 1 == len(text) or text[i + 1].isspace()):
            right = i + 1
            break
    while left < right and text[left].isspace():
        left += 1
    while right > left and text[right - 1].isspace():
        right -= 1
    return left, right


def literal_symbols(text: str) -> list[str]:
    out: list[str] = []
    for ch in text:
        name = unicodedata.name(ch, "")
        category = unicodedata.category(ch)
        if category == "Sm" or "GREEK" in name or "SUBSCRIPT" in name:
            if ch not in out:
                out.append(ch)
    return out


def line_range(unit: dict, text: str, start: int, end: int) -> tuple[int, int]:
    base = unit["localizacion"]["linea_inicio"]
    line_start = base + text[:start].count("\n")
    line_end = line_start + text[start:end].count("\n")
    return line_start, line_end


def context_ids(units: list[dict], index: int) -> list[str]:
    current = units[index]
    result: list[str] = []
    if index > 0 and units[index - 1]["archivo"] == current["archivo"]:
        result.append(units[index - 1]["id"])
    result.append(current["id"])
    if index + 1 < len(units) and units[index + 1]["archivo"] == current["archivo"]:
        result.append(units[index + 1]["id"])
    return result


def non_overlapping_explicit_spans(text: str) -> list[tuple[int, int]]:
    spans: list[tuple[int, int]] = []
    for pattern in EXPLICIT_PATTERNS:
        for match in pattern.finditer(text):
            spans.append((match.start(), match.end()))
    # Si dos patrones llegaran a solaparse, conserva el más largo que empieza antes.
    spans.sort(key=lambda span: (span[0], -(span[1] - span[0])))
    selected: list[tuple[int, int]] = []
    for start, end in spans:
        if any(not (end <= prior_start or start >= prior_end) for prior_start, prior_end in selected):
            continue
        selected.append((start, end))
    return sorted(selected)


def fallback_spans(text: str, explicit: list[tuple[int, int]]) -> list[tuple[int, int]]:
    spans: list[tuple[int, int]] = []
    cursor = 0
    for line in text.splitlines():
        stripped = line.strip()
        line_start_char = cursor
        cursor += len(line) + 1
        if not stripped or "=" not in stripped or len(stripped) > 320 or "http" in stripped:
            continue
        position = line_start_char + line.index("=")
        if any(start <= position < end for start, end in explicit):
            continue
        span = sentence_span(text, position)
        if span not in spans:
            spans.append(span)
    return spans


def base(record_id: str, literal: str, extraction: str) -> dict:
    return {
        "id": record_id,
        "tipo_registro": "formula",
        "schema_version": SCHEMA_VERSION,
        "texto_literal": literal,
        "normalizacion_formal": None,
        "normalizacion_lexica": None,
        "estatus_enunciativo": None,
        "estado_extraccion": extraction,
        "estado_verificacion": "pendiente",
        "estado_auditoria": "pendiente",
        "producido_por": {"motor": "formulas", "version": MOTOR_VERSION},
    }


def main() -> int:
    unidades = load_jsonl(UNIDADES)
    pilot_units = sorted(
        (unit for unit in unidades if unit.get("fuente_id") == PILOTO_ID),
        key=lambda unit: unit["orden_textual"],
    )
    if not pilot_units:
        raise SystemExit(f"No existen unidades de {PILOTO_ID}")

    formulas: list[dict] = []
    seen_ids: set[str] = set()
    equality_seeds = 0
    explicit_without_equals = 0

    for index, unit in enumerate(pilot_units):
        if unit.get("tipo_estructural") == "encabezado":
            continue
        text = unit["texto_literal"]
        equality_seeds += sum(
            1
            for line in text.splitlines()
            if line.strip() and "=" in line.strip() and len(line.strip()) <= 320 and "http" not in line
        )
        explicit = non_overlapping_explicit_spans(text)
        fallback = fallback_spans(text, explicit)

        spans: list[tuple[int, int, str]] = [
            (start, end, "formula_explicita") for start, end in explicit
        ] + [
            (start, end, "formula_candidata") for start, end in fallback
        ]

        for start, end, classification in sorted(spans):
            literal = text[start:end]
            if classification == "formula_explicita" and "=" not in literal:
                explicit_without_equals += 1
            line_start, line_end = line_range(unit, text, start, end)
            record_id = stable_id("FOR", unit["id"], str(line_start), literal)
            if record_id in seen_ids:
                raise SystemExit(f"ID de fórmula duplicado: {record_id}")
            seen_ids.add(record_id)
            extraction = "extraido" if classification == "formula_explicita" else "candidato"
            record = base(record_id, literal, extraction)
            record.update(
                {
                    "fuente_id": PILOTO_ID,
                    "unidad_id": unit["id"],
                    "formula_literal": literal,
                    "contexto_unidad_ids": context_ids(pilot_units, index),
                    "simbolos_literales": literal_symbols(literal),
                    "localizacion": {
                        "ruta": unit["archivo"],
                        "linea_inicio": line_start,
                        "linea_fin": line_end,
                    },
                    "clasificacion_formula": classification,
                }
            )
            formulas.append(record)

    formulas.sort(
        key=lambda row: (
            row["localizacion"]["ruta"],
            row["localizacion"]["linea_inicio"],
            row["id"],
        )
    )
    dump_jsonl(SALIDA, formulas)

    coverage = {
        "id": stable_id("COB", PILOTO_ID, "formulas", MOTOR_VERSION),
        "tipo_registro": "reporte_cobertura",
        "schema_version": SCHEMA_VERSION,
        "texto_literal": None,
        "normalizacion_formal": None,
        "normalizacion_lexica": None,
        "estatus_enunciativo": None,
        "estado_extraccion": "extraido",
        "estado_verificacion": "pendiente",
        "estado_auditoria": "no_aplica",
        "producido_por": {"motor": "formulas", "version": MOTOR_VERSION},
        "obra_id": PILOTO_ID,
        "motor": "formulas",
        "version_motor": MOTOR_VERSION,
        "unidades_totales": len(pilot_units),
        "unidades_procesadas": len(pilot_units),
        "unidades_omitidas": [],
        "errores": [],
    }
    dump_jsonl(COBERTURA, [coverage])

    explicit_count = sum(row["clasificacion_formula"] == "formula_explicita" for row in formulas)
    candidate_count = len(formulas) - explicit_count
    print(
        f"Fase 4D v{MOTOR_VERSION}: {len(formulas)} fórmulas; {explicit_count} explícitas, "
        f"{candidate_count} candidatas; {equality_seeds} semillas '='; "
        f"{explicit_without_equals} fórmula explícita sin '='; {len(pilot_units)} unidades procesadas."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
