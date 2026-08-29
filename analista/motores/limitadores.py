#!/usr/bin/env python3
"""Motor conservador de limitadores documentales — Fase 4F.

Recupera candidatos de distinción, negación, excepción y restricción mediante
marcadores literales estrictos. No decide voz autoral, no vincula limitadores a
una afirmación previa y no completa fragmentos por interpretación.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
UNIDADES = ROOT / "analista/generado/unidades.jsonl"
DISTINCIONES = ROOT / "analista/generado/distinciones.jsonl"
NEGACIONES = ROOT / "analista/generado/negaciones.jsonl"
EXCEPCIONES = ROOT / "analista/generado/excepciones.jsonl"
RESTRICCIONES = ROOT / "analista/generado/restricciones-alcance.jsonl"
COBERTURA = ROOT / "analista/generado/cobertura-limitadores.jsonl"
PILOTO_ID = "AA-SP-V1"
SCHEMA_VERSION = "1.0.0"
MOTOR_VERSION = "1.0.0"

NO_RE = re.compile(r"(?<![\w-])no(?![\w-])", re.IGNORECASE)
DIST_RE = re.compile(
    r"\bno\s+(?:es|son)\s+(.+?)\s+sino\s+(.+?)(?=[.;]|$)", re.IGNORECASE
)
EXC_RE = re.compile(
    r"\b(?:a excepción de|con excepción de|excepto|salvo\s+(?:que|cuando|si|por|en|los|las|el|la|un|una))\b",
    re.IGNORECASE,
)
RES_RE = re.compile(
    r"\b(?:solo si|sólo si|únicamente|exclusivamente|siempre que|a menos que|en la medida en que)\b",
    re.IGNORECASE,
)


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


def base(record_id: str, kind: str, literal: str | None, audit: str = "pendiente") -> dict:
    return {
        "id": record_id,
        "tipo_registro": kind,
        "schema_version": SCHEMA_VERSION,
        "texto_literal": literal,
        "normalizacion_formal": None,
        "normalizacion_lexica": None,
        "estatus_enunciativo": "no_determinado" if literal is not None else None,
        "estado_extraccion": "candidato" if literal is not None else "extraido",
        "estado_verificacion": "pendiente",
        "estado_auditoria": audit,
        "producido_por": {"motor": "limitadores", "version": MOTOR_VERSION},
    }


def loc(unit: dict, line_no: int) -> dict:
    return {"ruta": unit["archivo"], "linea_inicio": line_no, "linea_fin": line_no}


def main() -> int:
    units = [u for u in load_jsonl(UNIDADES) if u.get("fuente_id") == PILOTO_ID]
    if not units:
        raise SystemExit(f"No hay unidades para {PILOTO_ID}")

    distinctions: list[dict] = []
    negations: list[dict] = []
    exceptions: list[dict] = []
    restrictions: list[dict] = []

    for unit in units:
        start = unit["localizacion"]["linea_inicio"]
        lines = unit["texto_literal"].splitlines()
        expected = unit["localizacion"]["linea_fin"] - start + 1
        if len(lines) != expected:
            raise SystemExit(f"Rango inconsistente en {unit['id']}")

        for line_no, literal in enumerate(lines, start=start):
            dm = DIST_RE.search(literal)
            if dm:
                term_a = dm.group(1).strip()
                term_b = dm.group(2).strip()
                record = base(
                    stable_id("DIS", unit["id"], str(line_no), literal, term_a, term_b),
                    "distincion",
                    literal,
                )
                record.update(
                    {
                        "fuente_id": PILOTO_ID,
                        "unidad_id": unit["id"],
                        "termino_a_literal": term_a,
                        "termino_b_literal": term_b,
                        "marcador_literal": dm.group(0),
                        "clasificacion_distincion": "distincion_candidata",
                        "localizacion": loc(unit, line_no),
                    }
                )
                distinctions.append(record)

            nm = NO_RE.search(literal)
            if nm:
                fragment = literal[nm.start():]
                record = base(
                    stable_id("NEG", unit["id"], str(line_no), literal, fragment),
                    "negacion",
                    literal,
                )
                record.update(
                    {
                        "fuente_id": PILOTO_ID,
                        "unidad_id": unit["id"],
                        "objeto_negado_literal": fragment,
                        "alcance_literal": literal,
                        "clasificacion_negacion": "negacion_candidata",
                        "localizacion": loc(unit, line_no),
                    }
                )
                negations.append(record)

            em = EXC_RE.search(literal)
            if em:
                fragment = literal[em.start():]
                record = base(
                    stable_id("EXC", unit["id"], str(line_no), literal, fragment),
                    "excepcion",
                    literal,
                )
                record.update(
                    {
                        "fuente_id": PILOTO_ID,
                        "unidad_id": unit["id"],
                        "afirmacion_limitada_id": None,
                        "fragmento_exceptivo_literal": fragment,
                        "clasificacion_excepcion": "excepcion_candidata",
                        "localizacion": loc(unit, line_no),
                    }
                )
                exceptions.append(record)

            rm = RES_RE.search(literal)
            if rm:
                fragment = literal[rm.start():]
                record = base(
                    stable_id("RES", unit["id"], str(line_no), literal, fragment),
                    "restriccion_alcance",
                    literal,
                )
                record.update(
                    {
                        "fuente_id": PILOTO_ID,
                        "unidad_id": unit["id"],
                        "afirmacion_limitada_id": None,
                        "tipo_restriccion": "no_determinada",
                        "fragmento_restriccion_literal": fragment,
                        "clasificacion_restriccion": "restriccion_candidata",
                        "localizacion": loc(unit, line_no),
                    }
                )
                restrictions.append(record)

    key = lambda row: (
        row["localizacion"]["ruta"],
        row["localizacion"]["linea_inicio"],
        row["id"],
    )
    for rows in (distinctions, negations, exceptions, restrictions):
        rows.sort(key=key)

    dump_jsonl(DISTINCIONES, distinctions)
    dump_jsonl(NEGACIONES, negations)
    dump_jsonl(EXCEPCIONES, exceptions)
    dump_jsonl(RESTRICCIONES, restrictions)

    coverage = base(
        stable_id("COB", PILOTO_ID, "limitadores", MOTOR_VERSION),
        "reporte_cobertura",
        None,
        "no_aplica",
    )
    coverage.update(
        {
            "obra_id": PILOTO_ID,
            "motor": "limitadores",
            "version_motor": MOTOR_VERSION,
            "unidades_totales": len(units),
            "unidades_procesadas": len(units),
            "unidades_omitidas": [],
            "errores": [],
        }
    )
    dump_jsonl(COBERTURA, [coverage])
    print(
        "Fase 4F: "
        f"{len(distinctions)} distinciones candidatas; "
        f"{len(negations)} negaciones candidatas; "
        f"{len(exceptions)} excepciones candidatas; "
        f"{len(restrictions)} restricciones candidatas; "
        f"{len(units)} unidades procesadas; voz autoral no determinada."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
