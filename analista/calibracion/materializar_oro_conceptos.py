#!/usr/bin/env python3
"""Materializa el gold manual compacto de 4A y comprueba sus hashes congelados.

No consulta salidas de 4A. La decisión manual está en
`politica-oro-conceptos-v1.0.0.json`; este script solo enumera las coincidencias
literales exactas que esa política declara recuperables dentro de la muestra de
Fase 8.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CAL = ROOT / "analista/calibracion"
POLICY = CAL / "politica-oro-conceptos-v1.0.0.json"
LOCK = CAL / "muestra-fase8.lock.json"
UNITS = ROOT / "analista/generado/unidades.jsonl"
OUT_CHALLENGE = CAL / "patron-oro-conceptos-desafio.jsonl"
OUT_GENERAL = CAL / "patron-oro-conceptos-general.jsonl"
PILOTO_ID = "AA-SP-V1"


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def term_pattern(term: str) -> re.Pattern[str]:
    parts = re.split(r"\s+", term.strip())
    body = r"\s+".join(re.escape(part) for part in parts)
    return re.compile(rf"(?<!\w){body}(?!\w)", re.IGNORECASE)


def item(*, kind: str, literal: str, start: int, end: int, concept: str | None, classification: str | None = None) -> dict:
    return {
        "tipo_registro": kind,
        "texto_literal": literal,
        "linea_inicio": start,
        "linea_fin": end,
        "clasificacion": classification,
        "estatus_enunciativo": None,
        "concepto_designacion": concept,
        "sujeto_designacion": None,
        "objeto_designacion": None,
        "termino_a_literal": None,
        "termino_b_literal": None,
        "objeto_negado_literal": None,
        "fragmento_literal": None,
    }


def appearance_items(unit: dict, terms: list[str]) -> list[dict]:
    text = unit["texto_literal"]
    base = unit["localizacion"]["linea_inicio"]
    found: list[tuple[int, int, str, str]] = []
    for term in terms:
        for match in term_pattern(term).finditer(text):
            found.append((match.start(), match.end(), term, match.group(0)))
    found.sort()
    rows: list[dict] = []
    for start, _end, term, literal in found:
        line_start = base + text[:start].count("\n")
        line_end = line_start + literal.count("\n")
        rows.append(
            item(
                kind="aparicion_conceptual",
                literal=literal,
                start=line_start,
                end=line_end,
                concept=term if len(term.split()) > 1 else None,
            )
        )
    return rows


def row_for(unit_id: str, stratum: str, items: list[dict], observation: str) -> dict:
    return {
        "version": "1.0.0",
        "obra_id": PILOTO_ID,
        "unidad_id": unit_id,
        "motor": "conceptos_apariciones",
        "estratos": [stratum],
        "revision_manual": True,
        "items_esperados": items,
        "observacion": observation,
    }


def serialize(rows: list[dict]) -> bytes:
    return "".join(
        json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n"
        for row in rows
    ).encode("utf-8")


def materialize() -> tuple[bytes, bytes]:
    policy = json.loads(POLICY.read_text(encoding="utf-8"))
    lock = json.loads(LOCK.read_text(encoding="utf-8"))
    units = {
        row["id"]: row
        for row in load_jsonl(UNITS)
        if row.get("fuente_id") == PILOTO_ID
    }
    terms = policy["lemas"]
    assert len(terms) == len(set(terms)) == 21

    challenge_observation = (
        "Revisión manual 4A: toda coincidencia literal exacta con un lema técnico se conserva "
        "como aparición candidata; identidad solo cuando la propia unidad contiene la designación "
        "técnica multi-palabra exacta. No se resuelven sinónimos, plurales, abreviaturas ni palabras "
        "simples por contexto."
    )
    general_observation = (
        "Revisión manual 4A: censo de coincidencias literales exactas con lemas del glosario; "
        "identidad solo para designaciones técnicas multi-palabra exactas. Las declaraciones de "
        "glosario dentro de la muestra se anotan también como concepto establecido por evidencia."
    )

    challenge_rows = []
    for unit_id in lock["desafios"]["conceptos_apariciones"]:
        challenge_rows.append(
            row_for(unit_id, "desafio", appearance_items(units[unit_id], terms), challenge_observation)
        )

    declarations: dict[str, list[dict]] = {}
    for declaration in policy["declaraciones_en_muestra_general"]:
        declarations.setdefault(declaration["unidad_id"], []).append(declaration)

    general_rows = []
    for unit_id in lock["desafios"]["general"]:
        items = appearance_items(units[unit_id], terms)
        for declaration in declarations.get(unit_id, []):
            items.append(
                item(
                    kind="concepto",
                    literal=declaration["lema"],
                    start=declaration["linea"],
                    end=declaration["linea"],
                    concept=declaration["lema"],
                    classification="establecida_por_evidencia",
                )
            )
        general_rows.append(row_for(unit_id, "general", items, general_observation))

    return serialize(challenge_rows), serialize(general_rows)


def check_hash(payload: bytes, expected: str, label: str) -> None:
    actual = hashlib.sha256(payload).hexdigest()
    if actual != expected:
        raise AssertionError(f"Gold {label} no reproduce hash congelado: {actual} != {expected}")


def main() -> int:
    policy = json.loads(POLICY.read_text(encoding="utf-8"))
    challenge, general = materialize()
    expected = policy["producto_manual_congelado"]
    check_hash(challenge, expected["desafio"]["sha256_jsonl"], "desafio")
    check_hash(general, expected["general"]["sha256_jsonl"], "general")
    OUT_CHALLENGE.write_bytes(challenge)
    OUT_GENERAL.write_bytes(general)
    print(
        "OK gold 4A: 10 desafío/70 apariciones/8 identidades; "
        "31 general/111 apariciones/17 identidades/3 conceptos; hashes congelados reproducidos."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
