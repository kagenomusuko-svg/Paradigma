#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, re, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FUENTES = ROOT / "analista/generado/fuentes.jsonl"
UNIDADES = ROOT / "analista/generado/unidades.jsonl"
CONCEPTOS = ROOT / "analista/generado/conceptos.jsonl"
SALIDA = ROOT / "analista/generado/definiciones.jsonl"
COBERTURA = ROOT / "analista/generado/cobertura-definiciones.jsonl"
PILOTO_ID = "AA-SP-V1"
SCHEMA_VERSION = "1.0.0"
MOTOR_VERSION = "1.0.0"
ROMAN_RE = re.compile(r"^[IVXLCDM]+$")
ARROW_RE = re.compile(r"^\s*→")
SPACE_RE = re.compile(r"\s+")
PREAMBULO = ("los términos ", "sistema.", "introducido ")


def norm(text: str) -> str:
    return SPACE_RE.sub(" ", unicodedata.normalize("NFKC", text).casefold()).strip()


def sid(prefix: str, *parts: str) -> str:
    raw = "\x1f".join(parts).encode("utf-8")
    return f"{prefix}-{hashlib.sha1(raw).hexdigest()[:12].upper()}"


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def dump_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in rows), encoding="utf-8")


def parse_glossary(path: Path) -> list[dict]:
    lines = path.read_text(encoding="utf-8").splitlines()
    rel = path.relative_to(ROOT).as_posix()
    i = next((n for n, line in enumerate(lines) if "glosario" in norm(line)), None)
    if i is None:
        raise SystemExit("Glosario sin encabezado")
    i += 1
    out = []
    while i < len(lines):
        candidate = lines[i].strip()
        if not candidate or candidate.startswith("#") or ROMAN_RE.fullmatch(candidate) or norm(candidate).startswith(PREAMBULO):
            i += 1
            continue
        term = candidate
        term_line = i + 1
        i += 1
        content = []
        arrow = None
        while i < len(lines):
            current = lines[i].strip()
            if ARROW_RE.match(current):
                arrow = i + 1
                i += 1
                break
            if current and not current.startswith("#") and not ROMAN_RE.fullmatch(current):
                content.append((i + 1, current))
            i += 1
        if not content or arrow is None:
            continue
        start, end = content[0][0], content[-1][0]
        legacy_flat = " ".join(text for _, text in content)
        out.append({
            "lema": term,
            "linea_inicio": start,
            "linea_fin": end,
            "texto_literal": "\n".join(lines[start - 1:end]),
            "id": sid("DEF", rel, str(term_line), term, legacy_flat),
        })
    return out


def base(record_id: str, kind: str, literal: str | None, audit: str) -> dict:
    return {
        "id": record_id,
        "tipo_registro": kind,
        "schema_version": SCHEMA_VERSION,
        "texto_literal": literal,
        "normalizacion_formal": None,
        "normalizacion_lexica": None,
        "estatus_enunciativo": "definicion" if kind == "definicion" else None,
        "estado_extraccion": "extraido",
        "estado_verificacion": "pendiente",
        "estado_auditoria": audit,
        "producido_por": {"motor": "definiciones", "version": MOTOR_VERSION},
    }


def main() -> int:
    fuentes, unidades, conceptos = load_jsonl(FUENTES), load_jsonl(UNIDADES), load_jsonl(CONCEPTOS)
    fuente = next(r for r in fuentes if r["id"] == PILOTO_ID)
    glosarios = [r for r in fuente["rutas_derivadas"] if r.endswith("99-glosario.md")]
    if len(glosarios) != 1:
        raise SystemExit(f"Glosario ambiguo: {glosarios}")
    glosario_rel = glosarios[0]
    entries = parse_glossary(ROOT / glosario_rel)
    pilot_units = [u for u in unidades if u["fuente_id"] == PILOTO_ID]
    concepts_by_term = {c["designacion_operativa"]: c for c in conceptos}
    definitions = []
    for entry in entries:
        concept = concepts_by_term.get(entry["lema"])
        if concept is None:
            raise SystemExit(f"Lema sin concepto 4A: {entry['lema']}")
        containers = [u for u in pilot_units if u["archivo"] == glosario_rel and u["localizacion"]["linea_inicio"] <= entry["linea_inicio"] <= u["localizacion"]["linea_fin"]]
        if len(containers) != 1:
            raise SystemExit(f"Inicio sin unidad única: {entry['lema']}")
        rec = base(entry["id"], "definicion", entry["texto_literal"], "pendiente")
        rec.update({
            "fuente_id": PILOTO_ID,
            "unidad_id": containers[0]["id"],
            "concepto_id": concept["id"],
            "clasificacion_definicion": "definicion_explicita",
            "localizacion": {"ruta": glosario_rel, "linea_inicio": entry["linea_inicio"], "linea_fin": entry["linea_fin"]},
            "criterio_deteccion": "entrada_de_glosario_bajo_declaracion_explicita_de_definicion_tecnica",
        })
        definitions.append(rec)
    definitions.sort(key=lambda r: r["id"])
    dump_jsonl(SALIDA, definitions)
    cov = base(sid("COB", PILOTO_ID, "definiciones", MOTOR_VERSION), "reporte_cobertura", None, "no_aplica")
    cov.update({"obra_id": PILOTO_ID, "motor": "definiciones", "version_motor": MOTOR_VERSION, "unidades_totales": len(pilot_units), "unidades_procesadas": len(pilot_units), "unidades_omitidas": [], "errores": []})
    dump_jsonl(COBERTURA, [cov])
    print(f"Fase 4B: {len(definitions)} definiciones explícitas del glosario; {len(pilot_units)} unidades examinadas.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
