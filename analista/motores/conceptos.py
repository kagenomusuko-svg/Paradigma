#!/usr/bin/env python3
"""Motor conservador de conceptos y apariciones — Fase 4A.

Registra conceptos únicamente cuando existe una declaración explícita en el
glosario técnico de la obra piloto. Fuera del glosario, una aparición solo se
vincula cuando reproduce literalmente una designación técnica multi-palabra;
las palabras simples y cualquier variante abreviada/sinónima siguen como
candidatas sin identidad conceptual.
"""
from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[2]
FUENTES = ROOT / "analista" / "generado" / "fuentes.jsonl"
UNIDADES = ROOT / "analista" / "generado" / "unidades.jsonl"
SALIDA_APARICIONES = ROOT / "analista" / "generado" / "apariciones-conceptuales.jsonl"
SALIDA_CONCEPTOS = ROOT / "analista" / "generado" / "conceptos.jsonl"
SALIDA_COBERTURA = ROOT / "analista" / "generado" / "cobertura-conceptos.jsonl"

PILOTO_ID = "AA-SP-V1"
GLOSARIO_SUFFIX = "99-glosario.md"
SCHEMA_VERSION = "1.0.0"
MOTOR_VERSION = "1.1.0"

ROMAN_RE = re.compile(r"^[IVXLCDM]+$")
ARROW_RE = re.compile(r"^\s*→")
SPACE_RE = re.compile(r"\s+")
PREAMBULO = ("los términos ", "sistema.", "introducido ")


def normalizacion_formal_busqueda(texto: str) -> str:
    """Solo NFKC, casefold y espacios para detección formal; no fusiona conceptos."""
    return SPACE_RE.sub(" ", unicodedata.normalize("NFKC", texto).casefold()).strip()


def stable_id(prefix: str, *parts: str) -> str:
    payload = "\x1f".join(parts).encode("utf-8")
    return f"{prefix}-{hashlib.sha1(payload).hexdigest()[:12].upper()}"


def load_jsonl(path: Path) -> list[dict]:
    if not path.is_file():
        raise SystemExit(f"No existe insumo requerido: {path.relative_to(ROOT)}")
    rows: list[dict] = []
    with path.open("r", encoding="utf-8") as fh:
        for n, raw in enumerate(fh, start=1):
            if not raw.strip():
                continue
            try:
                rows.append(json.loads(raw))
            except json.JSONDecodeError as exc:
                raise SystemExit(f"JSONL inválido en {path.relative_to(ROOT)}:{n}: {exc}") from exc
    return rows


def dump_jsonl(path: Path, rows: Iterable[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def parse_glossary(path: Path) -> list[dict]:
    lines = path.read_text(encoding="utf-8").splitlines()
    i = 0
    while i < len(lines) and "glosario" not in normalizacion_formal_busqueda(lines[i]):
        i += 1
    if i == len(lines):
        raise SystemExit(f"No se encontró encabezado de glosario en {path.relative_to(ROOT)}")
    i += 1

    entries: list[dict] = []
    seen: set[str] = set()
    while i < len(lines):
        candidate = lines[i].strip()
        if (
            not candidate
            or candidate.startswith("#")
            or ROMAN_RE.fullmatch(candidate)
            or normalizacion_formal_busqueda(candidate).startswith(PREAMBULO)
        ):
            i += 1
            continue

        term = candidate
        term_line = i + 1
        i += 1
        definition_seen = False
        arrow_line: int | None = None

        while i < len(lines):
            current = lines[i].strip()
            if ARROW_RE.match(current):
                arrow_line = i + 1
                i += 1
                break
            if current and not current.startswith("#") and not ROMAN_RE.fullmatch(current):
                definition_seen = True
            i += 1

        if not definition_seen or arrow_line is None:
            continue

        key = normalizacion_formal_busqueda(term)
        if key in seen:
            raise SystemExit(f"Lema duplicado en glosario: {term}")
        seen.add(key)
        entries.append(
            {
                "lema": term,
                "linea_lema": term_line,
                "linea_remision": arrow_line,
                "concepto_id": stable_id("CON", key),
            }
        )

    if not entries:
        raise SystemExit("No se recuperaron lemas explícitos del glosario.")
    return entries


def term_pattern(term: str) -> re.Pattern[str]:
    parts = re.split(r"\s+", term.strip())
    body = r"\s+".join(re.escape(part) for part in parts)
    return re.compile(rf"(?<!\w){body}(?!\w)", re.IGNORECASE)


def is_multitoken_designation(term: str) -> bool:
    return len(term.split()) > 1


def line_range(unit: dict, text: str, start: int, end: int) -> tuple[int, int]:
    base = unit["localizacion"]["linea_inicio"]
    line_start = base + text[:start].count("\n")
    line_end = line_start + text[start:end].count("\n")
    return line_start, line_end


def base_record(*, record_id: str, kind: str, literal: str | None, extraction: str, audit: str) -> dict:
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
        "producido_por": {"motor": "conceptos_apariciones", "version": MOTOR_VERSION},
    }


def coverage_record(total_units: int) -> dict:
    record = base_record(
        record_id=stable_id("COB", PILOTO_ID, "conceptos_apariciones", MOTOR_VERSION),
        kind="reporte_cobertura",
        literal=None,
        extraction="extraido",
        audit="no_aplica",
    )
    record.update(
        {
            "obra_id": PILOTO_ID,
            "motor": "conceptos_apariciones",
            "version_motor": MOTOR_VERSION,
            "unidades_totales": total_units,
            "unidades_procesadas": total_units,
            "unidades_omitidas": [],
            "errores": [],
        }
    )
    return record


def main() -> int:
    fuentes = load_jsonl(FUENTES)
    unidades = load_jsonl(UNIDADES)
    fuente = next((row for row in fuentes if row.get("id") == PILOTO_ID), None)
    if fuente is None:
        raise SystemExit(f"No existe la fuente piloto {PILOTO_ID}")

    rutas = fuente.get("rutas_derivadas") or []
    glosarios = [route for route in rutas if str(route).endswith(GLOSARIO_SUFFIX)]
    if len(glosarios) != 1:
        raise SystemExit(f"Se esperaba un glosario para {PILOTO_ID}; encontrados={glosarios}")
    glosario_rel = glosarios[0]
    glosario = ROOT / glosario_rel
    if not glosario.is_file():
        raise SystemExit(f"Glosario inexistente: {glosario_rel}")

    pilot_units = [u for u in unidades if u.get("fuente_id") == PILOTO_ID]
    if not pilot_units:
        raise SystemExit(f"No existen unidades para {PILOTO_ID}")
    unit_ids = {u["id"] for u in pilot_units}
    if len(unit_ids) != len(pilot_units):
        raise SystemExit("IDs de unidad duplicados en la obra piloto")

    glossary_lines = glosario.read_text(encoding="utf-8").splitlines()
    entries = parse_glossary(glosario)

    appearances: list[dict] = []
    concepts: list[dict] = []
    appearance_ids: set[str] = set()

    for entry in entries:
        term = entry["lema"]
        concept_id = entry["concepto_id"]
        declaration_ids: list[str] = []
        linked_ids: list[str] = []
        pattern = term_pattern(term)

        for unit in pilot_units:
            text = unit["texto_literal"]
            for match in pattern.finditer(text):
                start_line, end_line = line_range(unit, text, match.start(), match.end())
                matched = match.group(0)
                exact_form = normalizacion_formal_busqueda(matched) == normalizacion_formal_busqueda(term)
                is_declaration = (
                    unit["archivo"] == glosario_rel
                    and start_line == entry["linea_lema"]
                    and end_line == entry["linea_lema"]
                    and glossary_lines[entry["linea_lema"] - 1].strip() == term
                    and exact_form
                )
                is_exact_multitoken = exact_form and is_multitoken_designation(term)
                is_linked = is_declaration or is_exact_multitoken

                aid = stable_id(
                    "APC",
                    concept_id,
                    unit["id"],
                    str(start_line),
                    str(match.start()),
                    matched,
                )
                if aid in appearance_ids:
                    raise SystemExit(f"ID de aparición duplicado: {aid}")
                appearance_ids.add(aid)

                record = base_record(
                    record_id=aid,
                    kind="aparicion_conceptual",
                    literal=matched,
                    extraction="extraido" if is_linked else "candidato",
                    audit="pendiente",
                )
                if is_declaration:
                    criterion = "lema_en_glosario_tecnico_explicito"
                elif is_exact_multitoken:
                    criterion = "designacion_tecnica_multilexema_exacta; sin_normalizacion_semantica"
                else:
                    criterion = "coincidencia_formal_con_lema_glosario; identidad_conceptual_no_determinada"
                record.update(
                    {
                        "fuente_id": PILOTO_ID,
                        "unidad_id": unit["id"],
                        "concepto_id": concept_id if is_linked else None,
                        "forma_literal": matched,
                        "variante_formal": None if matched == term else term,
                        "variantes_lexicas_busqueda": [],
                        "localizacion": {
                            "ruta": unit["archivo"],
                            "linea_inicio": start_line,
                            "linea_fin": end_line,
                        },
                        "criterio_deteccion": criterion,
                    }
                )
                appearances.append(record)
                if is_linked:
                    linked_ids.append(aid)
                if is_declaration:
                    declaration_ids.append(aid)

        if len(declaration_ids) != 1:
            raise SystemExit(
                f"El lema {term!r} debe tener una única aparición declarativa; encontradas={len(declaration_ids)}"
            )
        if not linked_ids:
            raise SystemExit(f"El concepto {term!r} quedó sin apariciones vinculadas")

        concept = base_record(
            record_id=concept_id,
            kind="concepto",
            literal=term,
            extraction="extraido",
            audit="pendiente",
        )
        concept.update(
            {
                "designacion_operativa": term,
                "aparicion_ids": sorted(linked_ids),
                "formas_literales_observadas": [term],
                "estado_identidad_conceptual": "establecida_por_evidencia",
                "evidencia_identidad_ids": declaration_ids,
            }
        )
        concepts.append(concept)

    appearances.sort(
        key=lambda row: (
            row["localizacion"]["ruta"],
            row["localizacion"]["linea_inicio"],
            row["unidad_id"],
            row["id"],
        )
    )
    concepts.sort(key=lambda row: row["id"])

    dump_jsonl(SALIDA_APARICIONES, appearances)
    dump_jsonl(SALIDA_CONCEPTOS, concepts)
    dump_jsonl(SALIDA_COBERTURA, [coverage_record(len(pilot_units))])

    linked = sum(1 for row in appearances if row["concepto_id"] is not None)
    candidates = len(appearances) - linked
    print(
        f"Fase 4A v{MOTOR_VERSION} para {PILOTO_ID}: {len(concepts)} conceptos; "
        f"{len(appearances)} apariciones = {linked} vinculadas por evidencia formal exacta + "
        f"{candidates} candidatas sin identidad; {len(pilot_units)} unidades procesadas."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
