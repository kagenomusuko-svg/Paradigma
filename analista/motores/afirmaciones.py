#!/usr/bin/env python3
"""Motor conservador de afirmaciones candidatas — Fase 4C.

Recupera unidades por marcadores lingüísticos históricos de alta precisión,
pero no convierte el hallazgo automático en tesis autoral. El estatus
enunciativo queda no_determinado hasta clasificación sustentada posterior.
"""
from __future__ import annotations

import hashlib
import json
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
UNIDADES = ROOT / "analista/generado/unidades.jsonl"
SALIDA = ROOT / "analista/generado/afirmaciones-candidatas.jsonl"
COBERTURA = ROOT / "analista/generado/cobertura-afirmaciones.jsonl"
PILOTO_ID = "AA-SP-V1"
SCHEMA_VERSION = "1.0.0"
MOTOR_VERSION = "1.0.0"

MARCADORES = (
    "la tesis de este capítulo es",
    "la tesis central",
    "este sistema sostiene",
    "este sistema propone",
    "este sistema afirma",
    "este sistema rechaza",
    "la posición de este libro es",
    "puede formularse así",
    "se define como",
    "la definición",
)


def norm(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).casefold()
    return " ".join(text.split())


def stable_id(prefix: str, *parts: str) -> str:
    raw = "\x1f".join(parts).encode("utf-8")
    return f"{prefix}-{hashlib.sha1(raw).hexdigest()[:12].upper()}"


def load_jsonl(path: Path) -> list[dict]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line
    ]


def dump_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(
            json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n"
            for row in rows
        ),
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
        "estatus_enunciativo": "no_determinado" if kind == "afirmacion" else None,
        "estado_extraccion": extraction,
        "estado_verificacion": "pendiente",
        "estado_auditoria": audit,
        "producido_por": {"motor": "afirmaciones", "version": MOTOR_VERSION},
    }


def main() -> int:
    unidades = load_jsonl(UNIDADES)
    pilot_units = [u for u in unidades if u.get("fuente_id") == PILOTO_ID]
    if not pilot_units:
        raise SystemExit(f"No existen unidades de {PILOTO_ID}")

    candidates: list[dict] = []
    ids: set[str] = set()
    for unit in pilot_units:
        if unit.get("tipo_estructural") == "encabezado":
            continue
        normalized = norm(unit["texto_literal"])
        markers = [marker for marker in MARCADORES if marker in normalized]
        if not markers:
            continue

        record_id = stable_id("AF", unit["id"], "|".join(markers))
        if record_id in ids:
            raise SystemExit(f"ID de afirmación duplicado: {record_id}")
        ids.add(record_id)
        record = base(record_id, "afirmacion", unit["texto_literal"], "candidato", "pendiente")
        record.update(
            {
                "fuente_id": PILOTO_ID,
                "unidad_id": unit["id"],
                "concepto_ids": [],
                "clasificacion_afirmacion": "afirmacion_candidata",
                "sujeto_literal": None,
                "predicado_literal": None,
                "objeto_literal": None,
                "localizacion": dict(unit["localizacion"]),
                "criterio_deteccion": (
                    "marcadores_linguisticos=" + "|".join(markers)
                    + "; estatus_enunciativo_no_determinado_hasta_clasificacion_sustentada"
                ),
                "confianza_extraccion": None,
            }
        )
        candidates.append(record)

    candidates.sort(key=lambda r: (r["localizacion"]["ruta"], r["localizacion"]["linea_inicio"], r["id"]))
    dump_jsonl(SALIDA, candidates)

    coverage = base(
        stable_id("COB", PILOTO_ID, "afirmaciones", MOTOR_VERSION),
        "reporte_cobertura",
        None,
        "extraido",
        "no_aplica",
    )
    coverage.update(
        {
            "obra_id": PILOTO_ID,
            "motor": "afirmaciones",
            "version_motor": MOTOR_VERSION,
            "unidades_totales": len(pilot_units),
            "unidades_procesadas": len(pilot_units),
            "unidades_omitidas": [],
            "errores": [],
        }
    )
    dump_jsonl(COBERTURA, [coverage])
    print(
        f"Fase 4C: {len(candidates)} afirmaciones candidatas recuperadas en "
        f"{len(pilot_units)} unidades; 0 ascendidas automáticamente a tesis autoral."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
