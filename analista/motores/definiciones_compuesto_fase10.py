#!/usr/bin/env python3
"""4B de Fase 10: definiciones genéricas ligadas a conceptos de la misma obra.

Usa el índice formal de designaciones producido por 4A. Las estructuras
claramente definicionales pueden registrarse como explícitas; la cópula simple y
la aposición quedan candidatas. No crea identidades, sinónimos ni equivalencias.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MOTOR = "definiciones"
VERSION = "1.2.0"
SCHEMA = "1.0.0"
GLOSSARY = "99-glosario.md"
HELPER = ROOT / "analista/motores/referencias_conceptuales_fase10.py"

spec = importlib.util.spec_from_file_location("refs_def_f10", HELPER)
assert spec and spec.loader
refs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(refs)

SPACE = re.compile(r"\s+")
BOUNDARY = re.compile(r"[.!?](?:[¹²³⁴⁵⁶⁷⁸⁹⁰]+)?(?=\s|$)|\n+")
STRONG_AFTER = ("se define como", "significa", "designa", "se denomina", "se entiende como")
STRONG_BEFORE = ("llamamos", "denominamos", "definimos", "defino", "denomino")


def norm(text: str) -> str:
    return SPACE.sub(" ", unicodedata.normalize("NFKC", text).casefold()).strip()


def sid(prefix: str, *parts: str) -> str:
    return f"{prefix}-{hashlib.sha1(chr(31).join(parts).encode()).hexdigest()[:12].upper()}"


def load(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def dump(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in rows), encoding="utf-8")


def base(rid: str, literal: str, status: str, classification: str) -> dict:
    return {
        "id": rid,
        "tipo_registro": "definicion",
        "schema_version": SCHEMA,
        "texto_literal": literal,
        "normalizacion_formal": None,
        "normalizacion_lexica": None,
        "estatus_enunciativo": status,
        "estado_extraccion": "extraido" if classification == "definicion_explicita" else "candidato",
        "estado_verificacion": "pendiente",
        "estado_auditoria": "pendiente",
        "producido_por": {"motor": MOTOR, "version": VERSION},
    }


def line_range(unit: dict, text: str, start: int, end: int) -> tuple[int, int]:
    first = unit["localizacion"]["linea_inicio"] + text[:start].count("\n")
    return first, first + text[start:end].count("\n")


def sentence_spans(text: str) -> list[tuple[int, int, str]]:
    out: list[tuple[int, int, str]] = []
    start = 0
    for match in BOUNDARY.finditer(text):
        end = match.end()
        a, b = start, end
        while a < b and text[a].isspace():
            a += 1
        while b > a and text[b - 1].isspace():
            b -= 1
        if a < b:
            out.append((a, b, text[a:b]))
        start = match.end()
    a = start
    while a < len(text) and text[a].isspace():
        a += 1
    if a < len(text):
        out.append((a, len(text), text[a:]))
    return out


def classify(sentence: str, start: int, end: int) -> tuple[str, str, str] | None:
    before = norm(sentence[:start])
    after = norm(sentence[end:])
    if after.startswith(STRONG_AFTER):
        return "definicion_explicita", "definicion", "estructura_definicional_fuerte_postnominal"
    if any(before.endswith(marker) for marker in STRONG_BEFORE):
        return "definicion_explicita", "definicion", "estructura_definicional_fuerte_prenominal"
    if before.endswith("por") and after.startswith("se entiende"):
        return "definicion_explicita", "definicion", "estructura_por_termino_se_entiende"
    if re.match(r"^(?:es|son)\b", after):
        return "definicion_candidata", "no_determinado", "copula_simple_no_autoriza_definicion_explicita"
    if after.startswith(":"):
        return "definicion_candidata", "no_determinado", "aposicion_dos_puntos_candidata"
    return None


def glossary_definitions(obra_id: str, source: dict, units: list[dict], concepts: list[dict]) -> list[dict]:
    gloss = [str(route) for route in source.get("rutas_derivadas", []) if str(route).endswith(GLOSSARY)]
    if len(gloss) != 1:
        return []
    rel = gloss[0]
    path = ROOT / rel
    if not path.is_file():
        raise SystemExit(f"Glosario inexistente: {rel}")
    lines = path.read_text(encoding="utf-8").splitlines()
    by = {
        norm(c["designacion_operativa"]): c
        for c in concepts
        if c.get("estado_identidad_conceptual") == "establecida_por_evidencia"
    }
    out: list[dict] = []
    for i, line in enumerate(lines):
        concept = by.get(norm(line.strip()))
        if concept is None:
            continue
        j = i + 1
        body: list[int] = []
        while j < len(lines) and not lines[j].lstrip().startswith("→"):
            if lines[j].strip() and not lines[j].startswith("#"):
                body.append(j)
            j += 1
        if not body or j >= len(lines):
            continue
        start, end = body[0] + 1, body[-1] + 1
        literal = "\n".join(lines[start - 1:end])
        holders = [
            u for u in units
            if u["archivo"] == rel
            and u["localizacion"]["linea_inicio"] <= start <= end <= u["localizacion"]["linea_fin"]
        ]
        if len(holders) != 1:
            raise SystemExit(f"Definición de glosario sin unidad única: {concept['id']}")
        rid = sid("DEF", obra_id, rel, str(start), str(end), concept["id"], literal)
        row = base(rid, literal, "definicion", "definicion_explicita")
        row.update({
            "fuente_id": obra_id,
            "unidad_id": holders[0]["id"],
            "concepto_id": concept["id"],
            "clasificacion_definicion": "definicion_explicita",
            "localizacion": {"ruta": rel, "linea_inicio": start, "linea_fin": end},
            "criterio_deteccion": "entrada_de_glosario_tecnico_explicito",
        })
        out.append(row)
    return out


def run(*, obra_id: str, fuentes: Path, unidades: Path, conceptos: Path, salida: Path, cobertura: Path) -> dict:
    source_rows = [row for row in load(fuentes) if row.get("id") == obra_id]
    if len(source_rows) != 1:
        raise SystemExit(f"Fuente {obra_id}: {len(source_rows)}")
    units = [row for row in load(unidades) if row.get("fuente_id") == obra_id]
    concepts = load(conceptos)
    if not units:
        raise SystemExit(f"Sin unidades: {obra_id}")
    index, by_id = refs.build_index(concepts)

    rows = glossary_definitions(obra_id, source_rows[0], units, concepts)
    seen = {(r["unidad_id"], r["concepto_id"], r["texto_literal"], r["localizacion"]["linea_inicio"]) for r in rows}

    for unit in units:
        if unit["archivo"].endswith(GLOSSARY) or unit.get("tipo_estructural") == "encabezado":
            continue
        text = unit["texto_literal"]
        for sentence_start, sentence_end, sentence in sentence_spans(text):
            for occurrence in refs.occurrences(sentence, index):
                concept = by_id[occurrence["concepto_id"]]
                result = classify(sentence, occurrence["inicio"], occurrence["fin"])
                if result is None:
                    continue
                classification, status, criterion = result
                key = (unit["id"], concept["id"], sentence, sentence_start)
                if key in seen:
                    continue
                seen.add(key)
                line_start, line_end = line_range(unit, text, sentence_start, sentence_end)
                rid = sid("DEF", obra_id, unit["id"], str(sentence_start), str(sentence_end), concept["id"], sentence)
                row = base(rid, sentence, status, classification)
                row.update({
                    "fuente_id": obra_id,
                    "unidad_id": unit["id"],
                    "concepto_id": concept["id"],
                    "clasificacion_definicion": classification,
                    "localizacion": {"ruta": unit["archivo"], "linea_inicio": line_start, "linea_fin": line_end},
                    "criterio_deteccion": criterion,
                })
                rows.append(row)

    rows.sort(key=lambda r: (r["localizacion"]["ruta"], r["localizacion"]["linea_inicio"], r["id"]))
    dump(salida, rows)
    cov = {
        "id": sid("COB", obra_id, MOTOR, VERSION),
        "tipo_registro": "reporte_cobertura",
        "schema_version": SCHEMA,
        "texto_literal": None,
        "normalizacion_formal": None,
        "normalizacion_lexica": None,
        "estatus_enunciativo": None,
        "estado_extraccion": "extraido",
        "estado_verificacion": "pendiente",
        "estado_auditoria": "no_aplica",
        "producido_por": {"motor": MOTOR, "version": VERSION},
        "obra_id": obra_id,
        "motor": MOTOR,
        "version_motor": VERSION,
        "unidades_totales": len(units),
        "unidades_procesadas": len(units),
        "unidades_omitidas": [],
        "errores": [],
    }
    dump(cobertura, [cov])
    return {
        "version": VERSION,
        "obra_id": obra_id,
        "registros": len(rows),
        "explicitas": sum(r["clasificacion_definicion"] == "definicion_explicita" for r in rows),
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--obra-id", required=True)
    p.add_argument("--fuentes", type=Path, required=True)
    p.add_argument("--unidades", type=Path, required=True)
    p.add_argument("--conceptos", type=Path, required=True)
    p.add_argument("--salida", type=Path, required=True)
    p.add_argument("--cobertura", type=Path, required=True)
    a = p.parse_args()
    print(json.dumps(run(
        obra_id=a.obra_id,
        fuentes=a.fuentes,
        unidades=a.unidades,
        conceptos=a.conceptos,
        salida=a.salida,
        cobertura=a.cobertura,
    ), ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
