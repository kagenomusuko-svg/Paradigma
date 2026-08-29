#!/usr/bin/env python3
"""Motor determinista de unidades textuales — Fase 3.

Responsabilidad única: segmentar y localizar texto ya custodiado por el motor
de fuentes. No interpreta contenido ni asigna estatus enunciativos.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[2]
FUENTES = ROOT / "analista" / "generado" / "fuentes.jsonl"
SALIDA_UNIDADES = ROOT / "analista" / "generado" / "unidades.jsonl"
SALIDA_COBERTURA = ROOT / "analista" / "generado" / "cobertura-unidades.jsonl"

SCHEMA_VERSION = "1.0.0"
MOTOR_VERSION = "1.0.0"

HEADING_RE = re.compile(r"^(#{1,6})[ \t]+(.+?)\s*$")
FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")
BLOCKQUOTE_RE = re.compile(r"^\s*>")
UL_RE = re.compile(r"^\s{0,3}[-+*]\s+")
OL_RE = re.compile(r"^\s{0,3}\d+[.)]\s+")
HR_RE = re.compile(r"^\s{0,3}(?:(?:\*\s*){3,}|(?:-\s*){3,}|(?:_\s*){3,})\s*$")
TABLE_SEPARATOR_RE = re.compile(
    r"^\s*\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)+\|?\s*$"
)


def stable_id(prefix: str, *parts: str) -> str:
    """Conserva el algoritmo histórico de IDs de unidades."""
    payload = "\x1f".join(parts).encode("utf-8")
    return f"{prefix}-{hashlib.sha1(payload).hexdigest()[:12].upper()}"


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


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
                raise SystemExit(
                    f"JSONL inválido en {path.relative_to(ROOT)}:{n}: {exc}"
                ) from exc
    return rows


def dump_jsonl(path: Path, rows: Iterable[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def structural_type(text: str) -> str:
    """Clasificación puramente formal; no atribuye función doctrinal."""
    lines = text.split("\n")
    first = lines[0] if lines else ""

    if HEADING_RE.match(first):
        return "encabezado"
    if FENCE_RE.match(first):
        return "bloque_codigo"
    if len(lines) == 1 and HR_RE.match(first):
        return "separador"
    if all(BLOCKQUOTE_RE.match(line) for line in lines if line.strip()):
        return "bloque_cita"
    if UL_RE.match(first):
        return "lista_no_ordenada"
    if OL_RE.match(first):
        return "lista_ordenada"
    if len(lines) >= 2 and "|" in lines[0] and TABLE_SEPARATOR_RE.match(lines[1]):
        return "tabla_markdown"
    return "parrafo"


def segment_file(path: Path, fuente_id: str, orden_inicial: int) -> tuple[list[dict], int]:
    rel = path.relative_to(ROOT).as_posix()
    lines = path.read_text(encoding="utf-8").splitlines()
    heading_stack: list[tuple[int, str]] = []
    units: list[dict] = []
    buf: list[str] = []
    start = 0
    order = orden_inicial

    def section_context() -> str | None:
        if not heading_stack:
            return None
        return " > ".join(title for _, title in heading_stack)

    def append_unit(text: str, line_start: int, line_end: int, section: str | None) -> None:
        nonlocal order
        if not text or not text.strip():
            return
        # El ID usa strip() para conservar compatibilidad con el prototipo v0.1;
        # el campo texto_literal conserva el fragmento exacto de las líneas.
        unit_id = stable_id("UT", rel, str(line_start), text.strip())
        units.append(
            {
                "id": unit_id,
                "tipo_registro": "unidad_textual",
                "schema_version": SCHEMA_VERSION,
                "texto_literal": text,
                "normalizacion_formal": None,
                "normalizacion_lexica": None,
                "estatus_enunciativo": None,
                "estado_extraccion": "extraido",
                "estado_verificacion": "verificado",
                "estado_auditoria": "no_aplica",
                "producido_por": {"motor": "unidades", "version": MOTOR_VERSION},
                "fuente_id": fuente_id,
                "archivo": rel,
                "seccion": section,
                "localizacion": {
                    "ruta": rel,
                    "linea_inicio": line_start,
                    "linea_fin": line_end,
                },
                "orden_textual": order,
                "tipo_estructural": structural_type(text),
                "sha256_texto": sha256_text(text),
            }
        )
        order += 1

    def flush(end_line: int) -> None:
        nonlocal buf, start
        if not buf:
            return
        append_unit("\n".join(buf), start, end_line, section_context())
        buf = []
        start = 0

    for n, raw in enumerate(lines, start=1):
        heading = HEADING_RE.match(raw)
        if heading:
            flush(n - 1)
            level = len(heading.group(1))
            title = heading.group(2).strip()
            heading_stack = [(l, t) for l, t in heading_stack if l < level]
            heading_stack.append((level, title))
            append_unit(raw, n, n, section_context())
            continue

        if not raw.strip():
            flush(n - 1)
            continue

        if not buf:
            start = n
        buf.append(raw)

    flush(len(lines))
    return units, order


def coverage_record(fuente_id: str, total: int) -> dict:
    return {
        "id": stable_id("COB", fuente_id, "unidades", MOTOR_VERSION),
        "tipo_registro": "reporte_cobertura",
        "schema_version": SCHEMA_VERSION,
        "texto_literal": None,
        "normalizacion_formal": None,
        "normalizacion_lexica": None,
        "estatus_enunciativo": None,
        "estado_extraccion": "extraido",
        "estado_verificacion": "verificado",
        "estado_auditoria": "no_aplica",
        "producido_por": {"motor": "unidades", "version": MOTOR_VERSION},
        "obra_id": fuente_id,
        "motor": "unidades",
        "version_motor": MOTOR_VERSION,
        "unidades_totales": total,
        "unidades_procesadas": total,
        "unidades_omitidas": [],
        "errores": [],
    }


def main() -> int:
    fuentes = load_jsonl(FUENTES)
    if not fuentes:
        raise SystemExit("El registro de fuentes está vacío.")

    source_ids: set[str] = set()
    all_units: list[dict] = []
    coverage: list[dict] = []
    unit_ids: set[str] = set()

    for fuente in fuentes:
        fuente_id = fuente.get("id")
        if not isinstance(fuente_id, str) or not fuente_id:
            raise SystemExit("Registro de fuente sin ID válido.")
        if fuente_id in source_ids:
            raise SystemExit(f"ID de fuente duplicado: {fuente_id}")
        source_ids.add(fuente_id)

        rutas = fuente.get("rutas_derivadas")
        if not isinstance(rutas, list) or not rutas:
            raise SystemExit(f"Fuente {fuente_id} sin rutas derivadas.")

        source_units: list[dict] = []
        order = 0
        for rel in rutas:
            if not isinstance(rel, str) or not rel:
                raise SystemExit(f"Ruta derivada inválida en {fuente_id}: {rel!r}")
            path = ROOT / rel
            if not path.is_file():
                raise SystemExit(f"Ruta derivada inexistente en {fuente_id}: {rel}")
            file_units, order = segment_file(path, fuente_id, order)
            source_units.extend(file_units)

        for unit in source_units:
            if unit["id"] in unit_ids:
                raise SystemExit(f"ID de unidad duplicado: {unit['id']}")
            unit_ids.add(unit["id"])

        all_units.extend(source_units)
        coverage.append(coverage_record(fuente_id, len(source_units)))

    dump_jsonl(SALIDA_UNIDADES, all_units)
    dump_jsonl(SALIDA_COBERTURA, coverage)

    print(
        "Unidades generadas: "
        f"{len(all_units)} unidades en {len(fuentes)} fuentes; "
        "cobertura textual no vacía preparada para verificación."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
