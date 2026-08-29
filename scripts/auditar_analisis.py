#!/usr/bin/env python3
"""Auditor de invariantes para la capa generada del análisis textual."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_jsonl(path: Path) -> list[dict]:
    rows = []
    with path.open(encoding="utf-8") as fh:
        for n, line in enumerate(fh, 1):
            if line.strip():
                try:
                    rows.append(json.loads(line))
                except json.JSONDecodeError as exc:
                    raise SystemExit(f"{path}:{n}: JSON inválido: {exc}") from exc
    return rows


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--dir", required=True)
    args = p.parse_args()
    root = Path(args.dir)

    units = load_jsonl(root / "unidades.jsonl")
    definitions = load_jsonl(root / "definiciones.jsonl")
    assertions = load_jsonl(root / "afirmaciones-candidatas.jsonl")
    formulas = load_jsonl(root / "formulas-candidatas.jsonl")
    concepts = json.loads((root / "conceptos.json").read_text(encoding="utf-8"))
    report = json.loads((root / "reporte.json").read_text(encoding="utf-8"))

    errors: list[str] = []

    def unique(rows: list[dict], label: str) -> set[str]:
        ids = [r.get("id") for r in rows]
        if None in ids:
            errors.append(f"{label}: hay registros sin id")
        if len(ids) != len(set(ids)):
            errors.append(f"{label}: ids duplicados")
        return {x for x in ids if x is not None}

    unit_ids = unique(units, "unidades")
    def_ids = unique(definitions, "definiciones")
    con_ids = unique(concepts, "conceptos")
    unique(assertions, "afirmaciones")
    unique(formulas, "formulas")

    for d in definitions:
        ev = d.get("evidencia") or {}
        if d.get("estatus_epistemico") == "explicita" and not ev.get("texto_literal"):
            errors.append(f"{d['id']}: definición explícita sin texto literal")
        if d.get("verificacion") != "pendiente":
            errors.append(f"{d['id']}: la capa generada no puede autoaprobar definiciones")
        if d.get("concepto_id") not in con_ids:
            errors.append(f"{d['id']}: concepto inexistente {d.get('concepto_id')}")

    for c in concepts:
        for did in c.get("definiciones_explicitas", []):
            if did not in def_ids:
                errors.append(f"{c['id']}: definición inexistente {did}")
        for a in c.get("apariciones", []):
            if a.get("unidad_id") not in unit_ids:
                errors.append(f"{c['id']}: aparición refiere unidad inexistente")
        if c.get("equivalencias_confirmadas"):
            errors.append(f"{c['id']}: la extracción automática no puede confirmar equivalencias")
        if c.get("relaciones"):
            errors.append(f"{c['id']}: la extracción automática no puede establecer relaciones")

    for a in assertions:
        if a.get("unidad_id") not in unit_ids:
            errors.append(f"{a['id']}: unidad de evidencia inexistente")
        if a.get("verificacion") != "pendiente":
            errors.append(f"{a['id']}: afirmación candidata autoaprobada")
        if a.get("puente_inferencial") is not None:
            errors.append(f"{a['id']}: una heurística no puede crear puente inferencial")

    for f in formulas:
        if f.get("unidad_id") not in unit_ids:
            errors.append(f"{f['id']}: unidad de evidencia inexistente")
        if f.get("interpretacion") is not None:
            errors.append(f"{f['id']}: la capa generada no puede interpretar fórmulas")

    rules = report.get("reglas", {})
    for forbidden in ("crea_inferencias", "crea_equivalencias", "crea_contradicciones", "modifica_fuentes"):
        if rules.get(forbidden) is not False:
            errors.append(f"reporte: {forbidden} debe ser false")

    if errors:
        print("AUDITORÍA FALLIDA")
        for e in errors:
            print(f"- {e}")
        return 1

    print(
        "AUDITORÍA APROBADA: "
        f"{len(unit_ids)} unidades, {len(con_ids)} conceptos, {len(def_ids)} definiciones; "
        "sin inferencias/equivalencias/contradicciones automáticas."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
