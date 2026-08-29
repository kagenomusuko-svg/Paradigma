#!/usr/bin/env python3
"""Auditor estructural intraobra — Fase 7A.

Solo comprueba invariantes mecánicos de registros ya verificados. No corrige,
reclasifica ni fusiona contenido doctrinal. Una entrada válida cambia únicamente
`estado_auditoria` de `pendiente` a `auditado`; una inconsistencia produce
`rechazado`.
"""
from __future__ import annotations

import argparse
import copy
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INPUT = ROOT / "analista/generado/verificados"
DEFAULT_OUTPUT = ROOT / "analista/generado/auditados"
DEFAULT_UNIDADES = ROOT / "analista/generado/unidades.jsonl"

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


def force_consistent(record: dict) -> bool:
    fields = (
        "clasificacion_definicion",
        "clasificacion_afirmacion",
        "clasificacion_formula",
        "clasificacion_relacion",
        "clasificacion_distincion",
        "clasificacion_negacion",
        "clasificacion_excepcion",
        "clasificacion_restriccion",
    )
    values = [record.get(field) for field in fields if record.get(field)]
    if not values:
        return True
    value = values[0]
    extraction = record.get("estado_extraccion")
    if value.endswith("_candidata"):
        return extraction == "candidato"
    if value.endswith("_explicita") or value == "relacion_explicita":
        return extraction == "extraido"
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-root", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--unidades", type=Path, default=DEFAULT_UNIDADES)
    args = parser.parse_args()

    by_file = {filename: load_jsonl(args.input_root / filename) for filename in FILES}
    records = [record for rows in by_file.values() for record in rows]
    id_counts = Counter(record["id"] for record in records)
    units = {row["id"]: row for row in load_jsonl(args.unidades)}
    appearances = {row["id"]: row for row in by_file["apariciones-conceptuales.jsonl"]}
    concepts = {row["id"]: row for row in by_file["conceptos.jsonl"]}
    assertions = {row["id"]: row for row in by_file["afirmaciones-candidatas.jsonl"]}

    verdicts: dict[str, bool] = {}
    reasons: dict[str, list[str]] = {}

    def fail(record_id: str, reason: str) -> None:
        reasons.setdefault(record_id, []).append(reason)

    for record in records:
        record_id = record["id"]
        kind = record["tipo_registro"]
        ok = True

        if id_counts[record_id] != 1:
            fail(record_id, "id_no_unico")
            ok = False
        if record.get("schema_version") != "1.0.0":
            fail(record_id, "schema")
            ok = False
        if record.get("estado_verificacion") != "verificado":
            fail(record_id, "evidencia_no_verificada")
            ok = False
        if record.get("estado_auditoria") not in {"pendiente", "no_aplica"}:
            fail(record_id, "estado_auditoria_entrada")
            ok = False
        if not force_consistent(record):
            fail(record_id, "fuerza_probatoria")
            ok = False

        unit_id = record.get("unidad_id")
        if unit_id is not None and unit_id not in units:
            fail(record_id, "unidad_inexistente")
            ok = False

        if kind == "aparicion_conceptual":
            concept_id = record.get("concepto_id")
            if concept_id is not None and concept_id not in concepts:
                fail(record_id, "concepto_inexistente")
                ok = False
        elif kind == "concepto":
            appearance_ids = record.get("aparicion_ids", [])
            evidence_ids = record.get("evidencia_identidad_ids", [])
            if any(item not in appearances for item in appearance_ids):
                fail(record_id, "aparicion_inexistente")
                ok = False
            if any(item not in appearance_ids for item in evidence_ids):
                fail(record_id, "evidencia_fuera_apariciones")
                ok = False
            if any(
                appearances[item].get("concepto_id") != record_id
                for item in appearance_ids
                if item in appearances
            ):
                fail(record_id, "retorno_aparicion")
                ok = False
        elif kind == "definicion":
            if record.get("concepto_id") not in concepts:
                fail(record_id, "concepto_inexistente")
                ok = False
        elif kind == "afirmacion":
            if any(item not in concepts for item in record.get("concepto_ids", [])):
                fail(record_id, "concepto_inexistente")
                ok = False
        elif kind == "formula":
            context_ids = record.get("contexto_unidad_ids", [])
            if not context_ids or any(item not in units for item in context_ids):
                fail(record_id, "contexto_unidad")
                ok = False
            if unit_id not in context_ids:
                fail(record_id, "ancla_fuera_contexto")
                ok = False
        elif kind == "relacion_explicita":
            if record.get("sujeto_ref") not in concepts or record.get("objeto_ref") not in concepts:
                fail(record_id, "referente_inexistente")
                ok = False
        elif kind in {"excepcion", "restriccion_alcance"}:
            assertion_id = record.get("afirmacion_limitada_id")
            if assertion_id is not None and assertion_id not in assertions:
                fail(record_id, "afirmacion_inexistente")
                ok = False

        verdicts[record_id] = ok

    total = rejected = 0
    for filename, rows in by_file.items():
        output: list[dict] = []
        for source in rows:
            record = copy.deepcopy(source)
            ok = verdicts[source["id"]]
            record["estado_auditoria"] = "auditado" if ok else "rechazado"
            total += 1
            rejected += int(not ok)
            output.append(record)
        dump_jsonl(args.output_root / filename, output)

    print(json.dumps({"total": total, "auditados": total - rejected, "rechazados": rejected}, sort_keys=True))
    for record_id in sorted(reasons):
        print(f"RECHAZADO {record_id}: {','.join(reasons[record_id])}")
    return 0 if rejected == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
