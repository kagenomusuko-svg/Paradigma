#!/usr/bin/env python3
"""Genera un expediente de auditoría RC-1 desde un maestro F10 cerrado.

Esta herramienta NO modifica motores ni reclasifica doctrina. Solo proyecta los
registros ya producidos por F10, añade contexto documental desde el checkout y
marca señales diagnósticas para priorizar lectura humana posterior.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any, Iterable
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[2]
SECTIONS = (
    "unidades",
    "apariciones_conceptuales",
    "conceptos",
    "definiciones",
    "afirmaciones",
    "formulas",
    "relaciones_explicitas",
    "distinciones",
    "negaciones",
    "excepciones",
    "restricciones_alcance",
    "hallazgos_auditoria",
    "reportes_cobertura",
)
TEXTUAL_SECTIONS = {
    "apariciones_conceptuales",
    "definiciones",
    "afirmaciones",
    "formulas",
    "relaciones_explicitas",
    "distinciones",
    "negaciones",
    "excepciones",
    "restricciones_alcance",
}
TERMINAL = set('.!?…:;»”\"')


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def write_json(path: Path, value: Any) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()
    path.write_bytes(raw)
    return sha256_bytes(raw)


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> tuple[int, str]:
    path.parent.mkdir(parents=True, exist_ok=True)
    h = hashlib.sha256()
    count = 0
    with path.open("wb") as f:
        for row in rows:
            raw = (json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n").encode()
            f.write(raw)
            h.update(raw)
            count += 1
    return count, h.hexdigest()


def load_source_lines(rel: str | None, cache: dict[str, list[str]]) -> list[str] | None:
    if not rel or rel.startswith("/") or ".." in Path(rel).parts:
        return None
    if rel not in cache:
        path = ROOT / rel
        if not path.is_file():
            return None
        cache[rel] = path.read_text(encoding="utf-8").splitlines()
    return cache[rel]


def location_for(row: dict[str, Any], unit_by_id: dict[str, dict[str, Any]]) -> dict[str, Any] | None:
    loc = row.get("localizacion")
    if isinstance(loc, dict) and loc.get("linea_inicio"):
        out = dict(loc)
        if not out.get("ruta"):
            out["ruta"] = row.get("archivo")
        return out
    unit = unit_by_id.get(str(row.get("unidad_id") or ""))
    if not unit:
        return None
    uloc = unit.get("localizacion")
    if not isinstance(uloc, dict):
        return None
    return {
        "ruta": unit.get("archivo") or uloc.get("ruta"),
        "linea_inicio": uloc.get("linea_inicio"),
        "linea_fin": uloc.get("linea_fin"),
    }


def source_context(
    row: dict[str, Any],
    unit_by_id: dict[str, dict[str, Any]],
    cache: dict[str, list[str]],
    margin: int,
) -> dict[str, Any]:
    loc = location_for(row, unit_by_id)
    if not loc:
        return {"disponible": False, "motivo": "sin_localizacion_documental"}
    rel = loc.get("ruta")
    lines = load_source_lines(rel, cache)
    if lines is None:
        return {"disponible": False, "motivo": "ruta_no_disponible_en_checkout", "localizacion": loc}
    try:
        start = int(loc.get("linea_inicio"))
        end = int(loc.get("linea_fin") or start)
    except (TypeError, ValueError):
        return {"disponible": False, "motivo": "rango_invalido", "localizacion": loc}
    if start < 1 or end < start or start > len(lines):
        return {"disponible": False, "motivo": "rango_fuera_de_archivo", "localizacion": loc}
    end = min(end, len(lines))
    lo = max(1, start - margin)
    hi = min(len(lines), end + margin)
    fragment = "\n".join(lines[start - 1 : end])
    context = "\n".join(f"{n}: {lines[n - 1]}" for n in range(lo, hi + 1))
    literal = row.get("texto_literal")
    if literal is None and isinstance(row.get("formula_literal"), str):
        literal = row.get("formula_literal")
    literal_in_fragment = None
    if isinstance(literal, str) and literal:
        literal_in_fragment = literal in fragment or " ".join(literal.split()) in " ".join(fragment.split())
    return {
        "disponible": True,
        "localizacion": {"ruta": rel, "linea_inicio": start, "linea_fin": end},
        "lineas_contexto_inicio": lo,
        "lineas_contexto_fin": hi,
        "fragmento_rango": fragment,
        "contexto_numerado": context,
        "texto_literal_localizable_en_rango": literal_in_fragment,
    }


def diagnostics(section: str, row: dict[str, Any], context: dict[str, Any]) -> list[str]:
    flags: list[str] = []
    literal = row.get("texto_literal")
    if not isinstance(literal, str):
        literal = row.get("formula_literal") if isinstance(row.get("formula_literal"), str) else ""
    stripped = literal.strip()
    if stripped:
        if "(cid:" in stripped:
            flags.append("contiene_cid")
        if section in {"definiciones", "afirmaciones"} and stripped[-1] not in TERMINAL:
            flags.append("final_sin_puntuacion_terminal")
        if section in {"definiciones", "afirmaciones"} and stripped[:1].islower():
            flags.append("inicio_minuscula")
        if "?" in stripped and section == "afirmaciones":
            flags.append("afirmacion_con_interrogacion")
    if section == "afirmaciones" and row.get("estatus_enunciativo") in {None, "no_determinado"}:
        flags.append("estatus_no_determinado")
    if section == "formulas" and "(cid:" in stripped:
        flags.append("formula_con_glifo_no_mapeado")
    if context.get("disponible") and context.get("texto_literal_localizable_en_rango") is False:
        flags.append("literal_no_localizable_en_rango_declarado")
    if not context.get("disponible") and section in TEXTUAL_SECTIONS:
        flags.append("sin_contexto_fuente_disponible")
    return sorted(set(flags))


def compact_related(row: dict[str, Any], index: dict[str, dict[str, Any]], max_refs: int = 8) -> list[dict[str, Any]]:
    ids: list[str] = []
    for key in ("evidencia_identidad_ids", "aparicion_ids", "concepto_ids"):
        value = row.get(key)
        if isinstance(value, list):
            ids.extend(str(x) for x in value if isinstance(x, str))
    for key in ("concepto_id", "afirmacion_limitada_id"):
        value = row.get(key)
        if isinstance(value, str):
            ids.append(value)
    out = []
    for rid in ids[:max_refs]:
        target = index.get(rid)
        if target:
            out.append({
                "id": target.get("id"),
                "tipo_registro": target.get("tipo_registro"),
                "texto_literal": target.get("texto_literal"),
                "forma_literal": target.get("forma_literal"),
                "designacion_operativa": target.get("designacion_operativa"),
                "localizacion": target.get("localizacion"),
            })
        else:
            out.append({"id": rid, "no_resuelto_en_maestro": True})
    return out


def audit_projection(
    section: str,
    row: dict[str, Any],
    unit_by_id: dict[str, dict[str, Any]],
    index: dict[str, dict[str, Any]],
    cache: dict[str, list[str]],
    margin: int,
) -> dict[str, Any]:
    context = source_context(row, unit_by_id, cache, margin)
    keep = (
        "id", "tipo_registro", "fuente_id", "unidad_id", "texto_literal",
        "normalizacion_formal", "normalizacion_lexica", "estatus_enunciativo",
        "estado_extraccion", "estado_verificacion", "estado_auditoria",
        "designacion_operativa", "estado_identidad_conceptual", "criterio_identidad",
        "forma_literal", "variante_formal", "clasificacion_definicion",
        "clasificacion_afirmacion", "clasificacion_relacion", "criterio_deteccion",
        "sujeto_literal", "predicado_literal", "objeto_literal", "relacion_literal",
        "formula_literal", "objeto_negado_literal", "fragmento_exceptivo_literal",
        "fragmento_restriccion_literal", "alcance_literal", "tipo_restriccion",
        "afirmacion_limitada_id", "concepto_id", "concepto_ids", "localizacion",
        "producido_por",
    )
    projected = {k: row.get(k) for k in keep if k in row}
    return {
        "seccion_maestro": section,
        "registro": projected,
        "contexto_fuente": context,
        "referencias_relacionadas": compact_related(row, index),
        "senales_diagnosticas": diagnostics(section, row, context),
        "auditoria_humana": {
            "estado": "pendiente",
            "categoria": None,
            "comentario_documental": None,
            "causa_raiz": None,
        },
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--zip-fase10", type=Path, required=True)
    p.add_argument("--obra-id", required=True)
    p.add_argument("--salida-dir", type=Path, required=True)
    p.add_argument("--zip-sha256-esperado")
    p.add_argument("--maestro-sha256-esperado")
    p.add_argument("--margen-contexto", type=int, default=3)
    p.add_argument("--prioridad-max-por-senal", type=int, default=80)
    args = p.parse_args()

    zip_sha = sha256_file(args.zip_fase10)
    if args.zip_sha256_esperado and zip_sha != args.zip_sha256_esperado:
        raise SystemExit(f"ZIP F10 divergente: {zip_sha}")

    member = f"maestros/{args.obra_id}.json"
    with ZipFile(args.zip_fase10) as z:
        if member not in z.namelist():
            raise SystemExit(f"Maestro ausente en F10: {member}")
        master_raw = z.read(member)
    master_sha = sha256_bytes(master_raw)
    if args.maestro_sha256_esperado and master_sha != args.maestro_sha256_esperado:
        raise SystemExit(f"Maestro divergente: {master_sha}")
    master = json.loads(master_raw)
    if master.get("fuente", {}).get("id") not in {None, args.obra_id} and master.get("obra_id") not in {None, args.obra_id}:
        raise SystemExit("Identidad de obra inesperada en maestro")

    section_rows = {sec: master.get(sec, []) for sec in SECTIONS}
    unit_by_id = {
        str(r.get("id")): r for r in section_rows.get("unidades", [])
        if isinstance(r, dict) and r.get("id")
    }
    index: dict[str, dict[str, Any]] = {}
    for rows in section_rows.values():
        if not isinstance(rows, list):
            continue
        for row in rows:
            if isinstance(row, dict) and row.get("id"):
                index[str(row["id"])] = row

    cache: dict[str, list[str]] = {}
    counts = {sec: len(rows) if isinstance(rows, list) else 0 for sec, rows in section_rows.items()}
    signals = Counter()
    priority_counts = Counter()
    all_rows: list[dict[str, Any]] = []
    priority_rows: list[dict[str, Any]] = []

    for section in SECTIONS:
        rows = section_rows.get(section, [])
        if not isinstance(rows, list):
            continue
        for row in rows:
            if not isinstance(row, dict):
                continue
            projected = audit_projection(section, row, unit_by_id, index, cache, args.margen_contexto)
            all_rows.append(projected)
            for flag in projected["senales_diagnosticas"]:
                signals[flag] += 1
            priority = bool(projected["senales_diagnosticas"]) or section in {
                "conceptos", "definiciones", "negaciones", "excepciones", "restricciones_alcance", "formulas"
            }
            if priority:
                key = projected["senales_diagnosticas"][0] if projected["senales_diagnosticas"] else f"seccion:{section}"
                if priority_counts[key] < args.prioridad_max_por_senal:
                    priority_rows.append(projected)
                    priority_counts[key] += 1

    args.salida_dir.mkdir(parents=True, exist_ok=True)
    total, all_sha = write_jsonl(args.salida_dir / "expediente-revision.jsonl", all_rows)
    ptotal, priority_sha = write_jsonl(args.salida_dir / "expediente-prioritario.jsonl", priority_rows)
    summary = {
        "version": "1.0.0",
        "fase": "RC-1",
        "estado": "baseline_proyectado_para_auditoria",
        "obra_id": args.obra_id,
        "titulo": master.get("titulo"),
        "schema_maestro": master.get("schema_version"),
        "origen": {
            "release": "analista-fase10-cierre-v1.2.2",
            "zip_sha256": zip_sha,
            "maestro_ruta": member,
            "maestro_sha256": master_sha,
        },
        "conteos_secciones": counts,
        "registros_expediente": total,
        "registros_prioritarios": ptotal,
        "senales_diagnosticas": dict(sorted(signals.items())),
        "expediente_sha256": all_sha,
        "prioritario_sha256": priority_sha,
        "motores_modificados": False,
        "senales_son_veredictos_de_auditoria": False,
        "auditoria_humana": "pendiente",
    }
    summary_sha = write_json(args.salida_dir / "resumen-baseline.json", summary)
    manifest = {
        "fase": "RC-1",
        "obra_id": args.obra_id,
        "productos": [
            {"ruta": "expediente-revision.jsonl", "sha256": all_sha, "registros": total},
            {"ruta": "expediente-prioritario.jsonl", "sha256": priority_sha, "registros": ptotal},
            {"ruta": "resumen-baseline.json", "sha256": summary_sha},
        ],
    }
    write_json(args.salida_dir / "manifest.json", manifest)
    print(json.dumps(summary, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
