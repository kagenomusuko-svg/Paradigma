#!/usr/bin/env python3
"""Materializa el patrón manual de fórmulas de una obra Fase 10.

Solo consulta política manual, muestra congelada y unidades de Fase 3. Nunca
abre `formulas-candidatas.jsonl` ni otra salida del extractor. El hash esperado
está congelado en la política para impedir reetiquetados silenciosos.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_UNITS = ROOT / "analista/generado/unidades.jsonl"
DEFAULT_SCHEMA = ROOT / "analista/calibracion/patron-oro-obra-v1.1.0.schema.json"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def item_for(unit: dict, literal: str) -> dict:
    text = unit["texto_literal"]
    count = text.count(literal)
    if count != 1:
        raise SystemExit(
            f"El literal manual debe aparecer exactamente una vez en {unit['id']}; "
            f"apariciones={count}; literal={literal!r}"
        )
    start = text.find(literal)
    line_start = unit["localizacion"]["linea_inicio"] + text[:start].count("\n")
    line_end = line_start + literal.count("\n")
    return {
        "tipo_registro": "formula",
        "texto_literal": literal,
        "linea_inicio": line_start,
        "linea_fin": line_end,
        "clasificacion": "formula_explicita",
        "estatus_enunciativo": None,
        "concepto_designacion": None,
        "sujeto_designacion": None,
        "objeto_designacion": None,
        "termino_a_literal": None,
        "termino_b_literal": None,
        "objeto_negado_literal": None,
        "fragmento_literal": None,
    }


def materialize(*, policy_path: Path, units_path: Path, schema_path: Path) -> bytes:
    policy = load_json(policy_path)
    lock_path = policy_path.parent / policy["muestra"]
    lock = load_json(lock_path)
    schema = load_json(schema_path)
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)

    obra_id = policy["obra_id"]
    if policy["motor"] != "formulas":
        raise SystemExit("Esta materialización solo admite motor=formulas")
    if lock["obra_id"] != obra_id:
        raise SystemExit("La política y la muestra no pertenecen a la misma obra")

    units = [u for u in load_jsonl(units_path) if u.get("fuente_id") == obra_id]
    by_id = {u["id"]: u for u in units}
    if len(by_id) != len(units):
        raise SystemExit("IDs de unidad duplicados")

    general = set(lock["general"])
    challenge = set(lock["desafios"]["formulas"])
    sample = general | challenge
    if not sample <= set(by_id):
        raise SystemExit("La muestra contiene unidades ausentes de Fase 3")
    if set(policy["decisiones"]) != challenge:
        raise SystemExit(
            "La política manual de fórmulas debe revisar explícitamente todas las unidades del desafío formal"
        )

    records: list[dict] = []
    for unit in sorted((by_id[uid] for uid in sample), key=lambda row: row["orden_textual"]):
        uid = unit["id"]
        strata: list[str] = []
        if uid in general:
            strata.append("general")
        if uid in challenge:
            strata.append("desafio")
        literals = policy["decisiones"].get(uid, [])
        items = [item_for(unit, literal) for literal in literals]
        observation = (
            "Revisión manual Fase 10: se conservan únicamente las expresiones formales visibles; "
            "la prosa explicativa y las remisiones documentales quedan fuera."
            if items
            else "Revisión manual Fase 10: no se observó una fórmula recuperable bajo la regla formal congelada."
        )
        record = {
            "version": "1.1.0",
            "obra_id": obra_id,
            "unidad_id": uid,
            "motor": "formulas",
            "estratos": strata,
            "revision_manual": True,
            "items_esperados": items,
            "observacion": observation,
        }
        errors = list(validator.iter_errors(record))
        if errors:
            raise SystemExit(f"Patrón manual inválido para {uid}: {errors[0].message}")
        records.append(record)

    raw = "".join(
        json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"
        for record in records
    ).encode("utf-8")
    expected = policy["patron_sha256"]
    actual = sha256(raw)
    if actual != expected:
        raise SystemExit(f"Hash del patrón manual no coincide: esperado={expected}; actual={actual}")
    return raw


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--politica", type=Path, required=True)
    ap.add_argument("--unidades", type=Path, default=DEFAULT_UNITS)
    ap.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    ap.add_argument("--salida", type=Path, required=True)
    args = ap.parse_args()
    raw = materialize(policy_path=args.politica, units_path=args.unidades, schema_path=args.schema)
    args.salida.parent.mkdir(parents=True, exist_ok=True)
    args.salida.write_bytes(raw)
    rows = [line for line in raw.splitlines() if line]
    items = sum(len(json.loads(line)["items_esperados"]) for line in rows)
    print(
        f"Patrón manual Fase 10 materializado: {len(rows)} unidades revisadas; "
        f"{items} fórmulas esperadas; sha256={sha256(raw)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
