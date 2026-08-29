#!/usr/bin/env python3
"""Materializa el patrón manual compacto de 4C y comprueba su hash congelado.

La decisión manual está en `politica-oro-afirmaciones-v1.0.0.json`. Este script
solo resuelve los anclajes literales declarados contra unidades de Fase 3; no
consulta `afirmaciones-candidatas.jsonl` ni ninguna salida de 4C.
"""
from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CAL = ROOT / "analista/calibracion"
POLICY = CAL / "politica-oro-afirmaciones-v1.0.0.json"
LOCK = CAL / "muestra-fase8.lock.json"
UNITS = ROOT / "analista/generado/unidades.jsonl"
OUTPUT = CAL / "patron-oro-afirmaciones.jsonl"
PILOTO_ID = "AA-SP-V1"


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def flex(pattern: str) -> re.Pattern[str]:
    return re.compile(r"\s+".join(re.escape(part) for part in pattern.split()))


def literal_span(unit: dict, start_pattern: str, end_pattern: str) -> tuple[str, int, int]:
    text = unit["texto_literal"]
    start_match = flex(start_pattern).search(text)
    if start_match is None:
        raise AssertionError(f"Inicio manual no localizado en {unit['id']}: {start_pattern!r}")
    end_match = flex(end_pattern).search(text, start_match.start())
    if end_match is None:
        raise AssertionError(f"Fin manual no localizado en {unit['id']}: {end_pattern!r}")
    literal = text[start_match.start():end_match.end()]
    base = unit["localizacion"]["linea_inicio"]
    line_start = base + text[:start_match.start()].count("\n")
    line_end = line_start + literal.count("\n")
    return literal, line_start, line_end


def item(literal: str, start: int, end: int, classification: str, status: str) -> dict:
    return {
        "tipo_registro": "afirmacion",
        "texto_literal": literal,
        "linea_inicio": start,
        "linea_fin": end,
        "clasificacion": classification,
        "estatus_enunciativo": status,
        "concepto_designacion": None,
        "sujeto_designacion": None,
        "objeto_designacion": None,
        "termino_a_literal": None,
        "termino_b_literal": None,
        "objeto_negado_literal": None,
        "fragmento_literal": None,
    }


def serialize(rows: list[dict]) -> bytes:
    return "".join(
        json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n"
        for row in rows
    ).encode("utf-8")


def materialize() -> bytes:
    policy = json.loads(POLICY.read_text(encoding="utf-8"))
    lock = json.loads(LOCK.read_text(encoding="utf-8"))
    units = {
        row["id"]: row
        for row in load_jsonl(UNITS)
        if row.get("fuente_id") == PILOTO_ID
    }
    general = lock["desafios"]["general"]
    challenge = lock["desafios"]["afirmaciones"]
    ordered: list[str] = []
    for unit_id in [*general, *challenge]:
        if unit_id not in ordered:
            ordered.append(unit_id)
    if len(ordered) != 42:
        raise AssertionError(f"Unión de muestra 4C inesperada: {len(ordered)}")

    declared = policy["anotaciones"]
    if any(unit_id not in ordered for unit_id in declared):
        raise AssertionError("La política 4C contiene una unidad fuera de la muestra congelada")

    rows: list[dict] = []
    observation = (
        "Revisión manual 4C: proposiciones delimitadas por continuidad de voz y fuerza "
        "enunciativa; se excluyen mobiliario, definiciones estructurales del glosario y "
        "metadiscurso sin tesis material."
    )
    for unit_id in ordered:
        unit = units[unit_id]
        strata = []
        if unit_id in general:
            strata.append("general")
        if unit_id in challenge:
            strata.append("desafio")
        expected = []
        for spec in declared.get(unit_id, []):
            literal, start, end = literal_span(unit, spec["inicio"], spec["fin"])
            expected.append(item(literal, start, end, spec["clasificacion"], spec["estatus_enunciativo"]))
        rows.append(
            {
                "version": "1.0.0",
                "obra_id": PILOTO_ID,
                "unidad_id": unit_id,
                "motor": "afirmaciones",
                "estratos": strata,
                "revision_manual": True,
                "items_esperados": expected,
                "observacion": observation,
            }
        )
    return serialize(rows)


def main() -> int:
    policy = json.loads(POLICY.read_text(encoding="utf-8"))
    payload = materialize()
    actual = hashlib.sha256(payload).hexdigest()
    expected = policy["producto_manual_congelado"]["sha256_jsonl"]
    if actual != expected:
        raise AssertionError(f"Gold 4C no reproduce hash congelado: {actual} != {expected}")
    OUTPUT.write_bytes(payload)
    rows = [json.loads(line) for line in payload.decode("utf-8").splitlines() if line]
    items = [item for row in rows for item in row["items_esperados"]]
    frozen = policy["producto_manual_congelado"]
    assert len(rows) == frozen["unidades_unicas"] == 42
    assert len(items) == frozen["items_totales"] == 58
    assert Counter(item["estatus_enunciativo"] for item in items) == Counter(frozen["estatus"])
    assert Counter(item["clasificacion"] for item in items) == Counter(frozen["clasificaciones"])
    print(
        "OK gold 4C: 42 unidades únicas/58 proposiciones; general 31/34, desafío 12/26; "
        "49 explícitas/9 candidatas; 7 estatus enunciativos representados; hash congelado reproducido."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
