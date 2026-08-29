#!/usr/bin/env python3
"""Motor conservador de fórmulas candidatas — Fase 4D.

Usa las líneas con '=' del prototipo únicamente como semillas de recuperación.
Cada semilla se expande a su oración literal completa para no cortar fórmulas
por los saltos de línea de la fuente. El contexto conserva la unidad contenedora
y sus vecinas inmediatas del mismo archivo, sin interpretación matemática.
"""
from __future__ import annotations

import hashlib
import json
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
UNIDADES = ROOT / "analista/generado/unidades.jsonl"
SALIDA = ROOT / "analista/generado/formulas-candidatas.jsonl"
COBERTURA = ROOT / "analista/generado/cobertura-formulas.jsonl"
PILOTO_ID = "AA-SP-V1"
SCHEMA_VERSION = "1.0.0"
MOTOR_VERSION = "1.0.1"
TERMINATORS = ".!?"


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


def base(record_id: str, kind: str, literal: str | None, extraction: str, audit: str) -> dict:
    return {
        "id": record_id,
        "tipo_registro": kind,
        "schema_version": SCHEMA_VERSION,
        "texto_literal": literal,
        "normalizacion_formal": None,
        "normalizacion_lexica": None,
        "estatus_enunciativo": None,
        "estado_extraccion": extraction,
        "estado_verificacion": "pendiente",
        "estado_auditoria": audit,
        "producido_por": {"motor": "formulas", "version": MOTOR_VERSION},
    }


def main() -> int:
    unidades = load_jsonl(UNIDADES)
    pilot_units = sorted(
        (u for u in unidades if u.get("fuente_id") == PILOTO_ID),
        key=lambda u: u["orden_textual"],
    )
    if not pilot_units:
        raise SystemExit(f"No existen unidades de {PILOTO_ID}")

    formulas: list[dict] = []
    seen_spans: set[tuple[str, int, int]] = set()
    seed_count = 0
    for index, unit in enumerate(pilot_units):
        # El postproceso histórico de fórmulas trabajaba sobre párrafos. Un encabezado
        # que contiene '=' funciona como rótulo y duplica la fórmula desarrollada en
        # el cuerpo; no se eleva por sí mismo a fórmula candidata.
        if unit.get("tipo_estructural") == "encabezado":
            continue
        text = unit["texto_literal"]
        cursor = 0
        for line in text.splitlines():
            stripped = line.strip()
            line_start_char = cursor
            cursor += len(line) + 1
            if not stripped or "=" not in stripped or len(stripped) > 320 or "http" in stripped:
                continue
            seed_count += 1
            eq_in_line = line.index("=")
            position = line_start_char + eq_in_line
            start, end = sentence_span(text, position)
            key = (unit["id"], start, end)
            if key in seen_spans:
                continue
            seen_spans.add(key)
            literal = text[start:end]
            if "=" not in literal:
                raise SystemExit(f"Expansión perdió '=' en {unit['id']}")
            line_start, line_end = line_range(unit, text, start, end)
            record_id = stable_id("FOR", unit["id"], str(line_start), literal)
            record = base(record_id, "formula", literal, "candidato", "pendiente")
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
                    "clasificacion_formula": "formula_candidata",
                }
            )
            formulas.append(record)

    formulas.sort(key=lambda r: (r["localizacion"]["ruta"], r["localizacion"]["linea_inicio"], r["id"]))
    dump_jsonl(SALIDA, formulas)

    coverage = base(
        stable_id("COB", PILOTO_ID, "formulas", MOTOR_VERSION),
        "reporte_cobertura",
        None,
        "extraido",
        "no_aplica",
    )
    coverage.update(
        {
            "obra_id": PILOTO_ID,
            "motor": "formulas",
            "version_motor": MOTOR_VERSION,
            "unidades_totales": len(pilot_units),
            "unidades_procesadas": len(pilot_units),
            "unidades_omitidas": [],
            "errores": [],
        }
    )
    dump_jsonl(COBERTURA, [coverage])
    print(
        f"Fase 4D: {seed_count} semillas textuales elegibles con '=' expandidas a "
        f"{len(formulas)} fórmulas candidatas completas; {len(pilot_units)} unidades procesadas."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
