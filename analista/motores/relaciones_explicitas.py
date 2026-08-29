#!/usr/bin/env python3
"""Motor conservador de relaciones explícitas — Fase 4E.

Solo registra relaciones cuando una línea del glosario conecta literalmente dos
conceptos ya documentados por 4A. No resuelve abreviaturas, similitudes,
transitividad ni equivalencias implícitas.
"""
from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FUENTES = ROOT / "analista/generado/fuentes.jsonl"
UNIDADES = ROOT / "analista/generado/unidades.jsonl"
CONCEPTOS = ROOT / "analista/generado/conceptos.jsonl"
SALIDA = ROOT / "analista/generado/relaciones-explicitas.jsonl"
COBERTURA = ROOT / "analista/generado/cobertura-relaciones.jsonl"
PILOTO_ID = "AA-SP-V1"
GLOSARIO_SUFFIX = "99-glosario.md"
SCHEMA_VERSION = "1.0.0"
MOTOR_VERSION = "1.0.0"
CF_RE = re.compile(r"\bcf\.\s*(.+)$", re.IGNORECASE)
NOMBRE_TECNICO_RE = re.compile(r"^\s*Nombre técnico del\s+([^:.;]+)", re.IGNORECASE)


def norm(text: str) -> str:
    return " ".join(unicodedata.normalize("NFKC", text).casefold().split())


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
        "producido_por": {"motor": "relaciones_explicitas", "version": MOTOR_VERSION},
    }


def unit_for_line(units: list[dict], route: str, line_no: int) -> dict:
    matches = [
        unit for unit in units
        if unit["archivo"] == route
        and unit["localizacion"]["linea_inicio"] <= line_no <= unit["localizacion"]["linea_fin"]
    ]
    if len(matches) != 1:
        raise SystemExit(
            f"La línea {route}:{line_no} no tiene una unidad contenedora única: "
            f"{[m['id'] for m in matches]}"
        )
    return matches[0]


def main() -> int:
    fuentes = load_jsonl(FUENTES)
    unidades = load_jsonl(UNIDADES)
    conceptos = load_jsonl(CONCEPTOS)

    fuente = next((row for row in fuentes if row.get("id") == PILOTO_ID), None)
    if fuente is None:
        raise SystemExit(f"No existe fuente piloto {PILOTO_ID}")
    glosarios = [route for route in fuente.get("rutas_derivadas", []) if route.endswith(GLOSARIO_SUFFIX)]
    if len(glosarios) != 1:
        raise SystemExit(f"Glosario ambiguo o ausente: {glosarios}")
    glosario_rel = glosarios[0]
    lines = (ROOT / glosario_rel).read_text(encoding="utf-8").splitlines()
    pilot_units = [row for row in unidades if row.get("fuente_id") == PILOTO_ID]

    concept_by_norm = {norm(row["designacion_operativa"]): row for row in conceptos}
    if len(concept_by_norm) != len(conceptos):
        raise SystemExit("Designaciones conceptuales duplicadas tras normalización formal.")

    term_positions: list[tuple[int, dict]] = []
    seen_concepts: set[str] = set()
    for line_no, line in enumerate(lines, start=1):
        concept = concept_by_norm.get(norm(line.strip()))
        if concept is None:
            continue
        if concept["id"] in seen_concepts:
            raise SystemExit(
                f"El lema {concept['designacion_operativa']!r} aparece como línea autónoma más de una vez."
            )
        seen_concepts.add(concept["id"])
        term_positions.append((line_no, concept))
    if seen_concepts != {row["id"] for row in conceptos}:
        raise SystemExit("No todos los conceptos 4A tienen lema autónomo en el glosario.")

    relations: list[dict] = []
    relation_ids: set[str] = set()

    def emit(subject: dict, target: dict, line_no: int) -> None:
        literal = lines[line_no - 1]
        unit = unit_for_line(pilot_units, glosario_rel, line_no)
        record_id = stable_id(
            "REL", subject["id"], target["id"], glosario_rel, str(line_no), literal
        )
        if record_id in relation_ids:
            return
        relation_ids.add(record_id)
        record = base(record_id, "relacion_explicita", literal, "extraido", "pendiente")
        record.update(
            {
                "fuente_id": PILOTO_ID,
                "unidad_id": unit["id"],
                "sujeto_ref": subject["id"],
                "objeto_ref": target["id"],
                "relacion_literal": literal,
                "clasificacion_relacion": "relacion_explicita",
                "localizacion": {
                    "ruta": glosario_rel,
                    "linea_inicio": line_no,
                    "linea_fin": line_no,
                },
            }
        )
        relations.append(record)

    for index, (term_line, subject) in enumerate(term_positions):
        end_line = term_positions[index + 1][0] - 1 if index + 1 < len(term_positions) else len(lines)
        for line_no in range(term_line + 1, end_line + 1):
            literal = lines[line_no - 1]

            direct = NOMBRE_TECNICO_RE.match(literal)
            if direct:
                target = concept_by_norm.get(norm(direct.group(1).strip()))
                if target is not None:
                    emit(subject, target, line_no)

            crossref = CF_RE.search(literal)
            if crossref:
                for raw_target in crossref.group(1).split(","):
                    target_text = raw_target.strip().rstrip(".;")
                    target = concept_by_norm.get(norm(target_text))
                    if target is not None:
                        emit(subject, target, line_no)

    relations.sort(
        key=lambda row: (
            row["localizacion"]["linea_inicio"],
            row["sujeto_ref"],
            row["objeto_ref"],
        )
    )
    dump_jsonl(SALIDA, relations)

    coverage = base(
        stable_id("COB", PILOTO_ID, "relaciones_explicitas", MOTOR_VERSION),
        "reporte_cobertura",
        None,
        "extraido",
        "no_aplica",
    )
    coverage.update(
        {
            "obra_id": PILOTO_ID,
            "motor": "relaciones_explicitas",
            "version_motor": MOTOR_VERSION,
            "unidades_totales": len(pilot_units),
            "unidades_procesadas": len(pilot_units),
            "unidades_omitidas": [],
            "errores": [],
        }
    )
    dump_jsonl(COBERTURA, [coverage])
    print(
        f"Fase 4E: {len(relations)} relaciones explícitas con referentes conceptuales exactos; "
        f"{len(pilot_units)} unidades procesadas; sin transitividad ni resolución aproximada."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
