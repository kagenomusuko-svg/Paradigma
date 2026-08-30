#!/usr/bin/env python3
"""Auditor descriptivo intraobra — Fase 7B.

Agrupa únicamente referencias ya verificadas y auditadas. Conserva multiplicidad
y ausencia de resolución; no enlaza conceptos por similitud, no convierte
candidatos en hallazgos explícitos y no sintetiza doctrina.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INPUT = ROOT / "analista/generado/auditados"
DEFAULT_OUTPUT = ROOT / "analista/generado/hallazgos-auditoria.jsonl"
PILOTO_ID = "AA-SP-V1"
MOTOR_VERSION = "1.0.0"
FILES = (
    "apariciones-conceptuales.jsonl",
    "conceptos.jsonl",
    "definiciones.jsonl",
    "afirmaciones-candidatas.jsonl",
    "formulas-candidatas.jsonl",
    "relaciones-explicitas.jsonl",
    "distinciones.jsonl",
    "negaciones.jsonl",
    "excepciones.jsonl",
    "restricciones-alcance.jsonl",
)


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def dump_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows),
        encoding="utf-8",
    )


def stable_id(category: str, record_ids: list[str]) -> str:
    raw = "\x1f".join([category, *sorted(record_ids)]).encode("utf-8")
    return "HA-" + hashlib.sha1(raw).hexdigest()[:12].upper()


def finding(obra_id: str, category: str, record_ids: list[str], description: str) -> dict:
    return {
        "id": stable_id(category, record_ids),
        "tipo_registro": "hallazgo_auditoria",
        "schema_version": "1.0.0",
        "texto_literal": None,
        "normalizacion_formal": None,
        "normalizacion_lexica": None,
        "estatus_enunciativo": None,
        "estado_extraccion": "extraido",
        "estado_verificacion": "verificado",
        "estado_auditoria": "auditado",
        "producido_por": {"motor": "auditor_descriptivo", "version": MOTOR_VERSION},
        "obra_id": obra_id,
        "categoria": category,
        "registro_ids": sorted(record_ids),
        "descripcion_documental": description,
        "resolucion_doctrinal": "no_realizada",
    }


def records_for_concept(concept_id: str, by_file: dict[str, list[dict]]) -> list[dict]:
    """Devuelve solo registros con una referencia explícita al ID conceptual."""
    records: list[dict] = []
    for row in by_file["apariciones-conceptuales.jsonl"]:
        if row.get("concepto_id") == concept_id:
            records.append(row)
    for row in by_file["definiciones.jsonl"]:
        if row.get("concepto_id") == concept_id:
            records.append(row)
    for row in by_file["afirmaciones-candidatas.jsonl"]:
        if concept_id in row.get("concepto_ids", []):
            records.append(row)
    for row in by_file["relaciones-explicitas.jsonl"]:
        if row.get("sujeto_ref") == concept_id or row.get("objeto_ref") == concept_id:
            records.append(row)
    return sorted(records, key=lambda row: (row["tipo_registro"], row["id"]))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-root", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--obra-id",
        default=PILOTO_ID,
        help="ID documental de la obra auditada; por defecto conserva el piloto histórico.",
    )
    args = parser.parse_args()

    by_file = {filename: load_jsonl(args.input_root / filename) for filename in FILES}
    records = [record for rows in by_file.values() for record in rows]
    if any(
        record.get("estado_verificacion") != "verificado"
        or record.get("estado_auditoria") != "auditado"
        for record in records
    ):
        raise SystemExit("7B solo acepta registros verificados y auditados.")

    # El ID de obra es metadato de procedencia, no una fuente de contenido.
    source_ids = {record.get("fuente_id") for record in records if record.get("fuente_id")}
    if source_ids and source_ids != {args.obra_id}:
        raise SystemExit(
            f"7B recibió registros de una obra distinta: esperada={args.obra_id}; fuentes={sorted(source_ids)}"
        )

    concepts = {row["id"]: row for row in by_file["conceptos.jsonl"]}
    findings: list[dict] = []

    linked_appearances: dict[str, list[dict]] = defaultdict(list)
    for row in by_file["apariciones-conceptuales.jsonl"]:
        if row.get("concepto_id") in concepts:
            linked_appearances[row["concepto_id"]].append(row)
    for concept_id, concept in sorted(concepts.items()):
        rows = linked_appearances[concept_id]
        if len(rows) == 1:
            findings.append(
                finding(
                    args.obra_id,
                    "uso_singular",
                    [concept_id, rows[0]["id"]],
                    f"El concepto {concept_id} ({concept['designacion_operativa']}) tiene una sola "
                    "aparición vinculada en los registros auditados. Esto no afirma que la forma "
                    "sea única en el texto.",
                )
            )

    definitions: dict[str, list[dict]] = defaultdict(list)
    for row in by_file["definiciones.jsonl"]:
        definitions[row["concepto_id"]].append(row)
    for concept_id, rows in sorted(definitions.items()):
        if len(rows) > 1:
            findings.append(
                finding(
                    args.obra_id,
                    "definiciones_multiples",
                    [row["id"] for row in rows],
                    f"El concepto {concept_id} posee {len(rows)} definiciones auditadas distintas "
                    "por ID. No se sintetizan ni jerarquizan.",
                )
            )

    predications: dict[str, list[dict]] = defaultdict(list)
    for row in by_file["afirmaciones-candidatas.jsonl"]:
        for concept_id in row.get("concepto_ids", []):
            predications[concept_id].append(row)
    for concept_id, rows in sorted(predications.items()):
        if len(rows) > 1:
            findings.append(
                finding(
                    args.obra_id,
                    "multiplicidad_predicativa",
                    [row["id"] for row in rows],
                    f"El concepto {concept_id} está referenciado por {len(rows)} afirmaciones "
                    "auditadas. Se conservan como formulaciones separadas.",
                )
            )

    outgoing: dict[str, list[dict]] = defaultdict(list)
    for row in by_file["relaciones-explicitas.jsonl"]:
        outgoing[row["sujeto_ref"]].append(row)
    for concept_id, rows in sorted(outgoing.items()):
        objects = {row["objeto_ref"] for row in rows}
        if len(objects) > 1:
            findings.append(
                finding(
                    args.obra_id,
                    "variacion_de_objeto",
                    [row["id"] for row in rows],
                    f"El sujeto {concept_id} participa en relaciones explícitas auditadas con "
                    f"objetos distintos: {', '.join(sorted(objects))}. No se infiere relación "
                    "entre esos objetos.",
                )
            )

    repeated: dict[tuple[str, str, str], list[dict]] = defaultdict(list)
    for row in by_file["relaciones-explicitas.jsonl"]:
        repeated[(row["sujeto_ref"], row["objeto_ref"], row["relacion_literal"])].append(row)
    for _, rows in sorted(repeated.items()):
        if len(rows) > 1:
            findings.append(
                finding(
                    args.obra_id,
                    "relacion_repetida",
                    [row["id"] for row in rows],
                    f"Se registran {len(rows)} relaciones auditadas con el mismo sujeto, objeto "
                    "y literal. Se conserva la multiplicidad.",
                )
            )

    for row in by_file["negaciones.jsonl"]:
        if row.get("clasificacion_negacion") == "negacion_explicita":
            findings.append(
                finding(
                    args.obra_id,
                    "negacion_explicita",
                    [row["id"]],
                    f"El registro {row['id']} conserva una negación clasificada explícitamente "
                    "por el extractor; el auditor no amplía su alcance.",
                )
            )
    for row in by_file["excepciones.jsonl"]:
        if row.get("clasificacion_excepcion") == "excepcion_explicita":
            findings.append(
                finding(
                    args.obra_id,
                    "excepcion_explicita",
                    [row["id"]],
                    f"El registro {row['id']} conserva una excepción clasificada explícitamente "
                    "por el extractor; el auditor no resuelve su efecto doctrinal.",
                )
            )
    for row in by_file["restricciones-alcance.jsonl"]:
        if row.get("clasificacion_restriccion") == "restriccion_explicita":
            findings.append(
                finding(
                    args.obra_id,
                    "restriccion_de_alcance",
                    [row["id"]],
                    f"El registro {row['id']} conserva una restricción de alcance explícita; "
                    "el auditor no la extiende a otras afirmaciones.",
                )
            )

    for concept_id, concept in sorted(concepts.items()):
        forms = concept.get("formas_literales_observadas", [])
        if len(set(forms)) > 1:
            findings.append(
                finding(
                    args.obra_id,
                    "variacion_terminologica",
                    [concept_id],
                    f"El concepto {concept_id} conserva múltiples formas literales observadas: "
                    f"{forms}. No se declara equivalencia más allá del propio registro conceptual "
                    "auditado.",
                )
            )

    findings.sort(key=lambda row: (row["categoria"], row["id"]))
    dump_jsonl(args.output, findings)
    print(
        json.dumps(
            {
                "obra_id": args.obra_id,
                "hallazgos": len(findings),
                "categorias": dict(sorted(Counter(row["categoria"] for row in findings).items())),
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
