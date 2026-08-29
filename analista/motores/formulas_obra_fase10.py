#!/usr/bin/env python3
"""Motor de fórmulas por obra — Fase 10, familia `formulas` v1.2.0.

Reutiliza literalmente las familias explícitas cerradas de Fase 4D v1.1.0 y
añade una recuperación conservadora de bloques formales para repetición
intraobra. Las nuevas formas se mantienen como `formula_candidata`: detectar
`=` o `→` no autoriza equivalencia doctrinal ni clasificación explícita.

La ruta candidata conserva el bloque formal mínimo observable y evita absorber
prosa explicativa posterior. Las remisiones documentales que comienzan por `→`
se excluyen. No modifica `analista/motores/formulas.py`, por lo que el producto
piloto de Fase 9 permanece bajo v1.1.0.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE_PATH = ROOT / "analista/motores/formulas.py"
SCHEMA_VERSION = "1.0.0"
MOTOR_NAME = "formulas"
MOTOR_VERSION = "1.2.0"
STOP_CONTINUATION_RE = re.compile(
    r"(?i)^(?:donde|y\b|pero\b|porque\b|que\b|si\b|cuando\b|aunque\b|"
    r"lo\b|la\b|el\b|esa\b|ese\b|esta\b|este\b)"
)
LABELLED_FORMAL_RE = re.compile(r"^[A-ZÁÉÍÓÚÜÑΦφ][^:]{0,45}:")
MAPPING_SUBJECT_RE = re.compile(
    r"^[A-ZÁÉÍÓÚÜÑ][\wÁÉÍÓÚÜÑáéíóúüñ₂₁() -]{0,35}\s+→"
)


def load_base():
    spec = importlib.util.spec_from_file_location("fase10_formulas_base_v110", BASE_PATH)
    if spec is None or spec.loader is None:
        raise SystemExit(f"No se pudo cargar el motor base: {BASE_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def is_formal_seed(text: str) -> bool:
    literal = text.strip()
    if not literal or literal.startswith("→"):
        return False
    if "http" in literal or len(literal) > 320 or len(literal.split()) > 30:
        return False
    return "=" in literal or "→" in literal


def starts_new_formal_item(text: str) -> bool:
    literal = text.strip()
    if not is_formal_seed(literal):
        return False
    if LABELLED_FORMAL_RE.match(literal):
        return True
    if literal.startswith(("φ", "Φ")):
        return True
    return MAPPING_SUBJECT_RE.match(literal) is not None


def candidate_spans(text: str, explicit: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Recupera bloques formales candidatos sin interpretar sus símbolos.

    Un bloque parte de una línea con `=` o `→`. Una línea física posterior solo
    se incorpora como continuidad tipográfica si no inicia una nueva fórmula,
    no es remisión/encabezado/prosa y es breve. Esto conserva, por ejemplo,
    `Potós: ... → orientación\nsostenida → distancia temporal` sin absorber el
    párrafo explicativo siguiente.
    """
    lines: list[dict] = []
    cursor = 0
    for raw in text.splitlines(keepends=True):
        line = raw.rstrip("\r\n")
        lines.append(
            {
                "start": cursor,
                "end": cursor + len(line),
                "line": line,
                "stripped": line.strip(),
            }
        )
        cursor += len(raw)
    if not lines and text:
        lines.append({"start": 0, "end": len(text), "line": text, "stripped": text.strip()})

    spans: list[tuple[int, int]] = []
    i = 0
    while i < len(lines):
        current = lines[i]
        literal = current["stripped"]
        if not is_formal_seed(literal):
            i += 1
            continue

        start = current["start"] + len(current["line"]) - len(current["line"].lstrip())
        end = current["start"] + len(current["line"].rstrip())
        if any(not (end <= prior_start or start >= prior_end) for prior_start, prior_end in explicit):
            i += 1
            continue

        j = i + 1
        while j < len(lines):
            nxt = lines[j]["stripped"]
            if not nxt or nxt == "---" or nxt.startswith(("#", "→")):
                break
            if starts_new_formal_item(nxt):
                break
            if nxt.startswith(("φ", "Φ")) or nxt[0].isupper():
                break
            if STOP_CONTINUATION_RE.match(nxt) or len(nxt.split()) > 12:
                break
            end = lines[j]["end"]
            j += 1

        span = (start, end)
        if not any(not (span[1] <= a or span[0] >= b) for a, b in explicit):
            spans.append(span)
        i = max(i + 1, j)

    # La expansión anterior ya evita solapamientos; esta deduplicación protege
    # frente a saltos de línea no convencionales sin cambiar el orden textual.
    out: list[tuple[int, int]] = []
    for span in spans:
        if span not in out:
            out.append(span)
    return out


def base_record(base, record_id: str, literal: str, classification: str) -> dict:
    extraction = "extraido" if classification == "formula_explicita" else "candidato"
    record = base.base(record_id, literal, extraction)
    record["producido_por"] = {"motor": MOTOR_NAME, "version": MOTOR_VERSION}
    return record


def run(*, obra_id: str, unidades: Path, salida: Path, cobertura: Path) -> dict:
    base = load_base()
    all_units = base.load_jsonl(unidades)
    work_units = sorted(
        (unit for unit in all_units if unit.get("fuente_id") == obra_id),
        key=lambda unit: unit["orden_textual"],
    )
    if not work_units:
        raise SystemExit(f"No existen unidades de {obra_id}")

    formulas: list[dict] = []
    seen_ids: set[str] = set()
    equality_seeds = 0
    arrow_seeds = 0

    for index, unit in enumerate(work_units):
        if unit.get("tipo_estructural") == "encabezado":
            continue
        text = unit["texto_literal"]
        for line in text.splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith("→") or "http" in stripped or len(stripped) > 320:
                continue
            if "=" in stripped:
                equality_seeds += 1
            if "→" in stripped:
                arrow_seeds += 1

        explicit = base.non_overlapping_explicit_spans(text)
        candidates = candidate_spans(text, explicit)
        spans = [
            (start, end, "formula_explicita") for start, end in explicit
        ] + [
            (start, end, "formula_candidata") for start, end in candidates
        ]

        for start, end, classification in sorted(spans):
            literal = text[start:end]
            line_start, line_end = base.line_range(unit, text, start, end)
            record_id = base.stable_id("FOR", unit["id"], str(line_start), literal)
            if record_id in seen_ids:
                raise SystemExit(f"ID de fórmula duplicado: {record_id}")
            seen_ids.add(record_id)
            record = base_record(base, record_id, literal, classification)
            record.update(
                {
                    "fuente_id": obra_id,
                    "unidad_id": unit["id"],
                    "formula_literal": literal,
                    "contexto_unidad_ids": base.context_ids(work_units, index),
                    "simbolos_literales": base.literal_symbols(literal),
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
            row["localizacion"]["linea_fin"],
            row["id"],
        )
    )
    base.dump_jsonl(salida, formulas)

    coverage_record = {
        "id": base.stable_id("COB", obra_id, MOTOR_NAME, MOTOR_VERSION),
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
        "motor": MOTOR_NAME,
        "version_motor": MOTOR_VERSION,
        "unidades_totales": len(work_units),
        "unidades_procesadas": len(work_units),
        "unidades_omitidas": [],
        "errores": [],
    }
    base.dump_jsonl(cobertura, [coverage_record])

    result = {
        "obra_id": obra_id,
        "version": MOTOR_VERSION,
        "unidades": len(work_units),
        "formulas": len(formulas),
        "explicitas": sum(r["clasificacion_formula"] == "formula_explicita" for r in formulas),
        "candidatas": sum(r["clasificacion_formula"] == "formula_candidata" for r in formulas),
        "semillas_igual": equality_seeds,
        "semillas_flecha": arrow_seeds,
    }
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return result


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--obra-id", required=True)
    ap.add_argument("--unidades", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    ap.add_argument("--cobertura", type=Path, required=True)
    args = ap.parse_args()
    run(
        obra_id=args.obra_id,
        unidades=args.unidades,
        salida=args.salida,
        cobertura=args.cobertura,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
