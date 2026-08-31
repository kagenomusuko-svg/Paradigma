#!/usr/bin/env python3
"""4A de Fase 10: identidad por evidencia explícita intraobra + candidatos formales.

El glosario técnico propio sigue siendo evidencia explícita privilegiada, pero no
es requisito epistemológico. El cuerpo de la misma obra puede establecer una
designación cuando una construcción declarativa inequívoca la identifica. Los
patrones solo localizan candidatos; una compuerta conservadora excluye contextos
condicionales, interrogativos, negativos, citados o referidos. No se fusionan
conceptos por semejanza, recurrencia, proximidad ni sinonimia.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GENERIC = ROOT / "analista/motores/conceptos_obra_fase10.py"
MOTOR = "conceptos_apariciones"
VERSION = "1.3.1"
GLOSSARY = "99-glosario.md"

ARROW = re.compile(r"^\s*→")
ROMAN = re.compile(r"^[IVXLCDM]+$", re.I)
ALPHA_HEADER = re.compile(r"^[A-ZÁÉÍÓÚÜÑ]$")
REFERENCE_DASH = re.compile(
    r"^(?P<t>.+?)\s+—\s+(?=(?:Vol\.|Cap(?:s)?\.|Parte\b|Ap[eé]ndice\b|passim\b|§|Afrodita Areia\b)).+$",
    re.I,
)
INLINE_COLON = re.compile(r"^(?P<t>[^:#]{1,100}?):\s+\S")
CLAUSE_RE = re.compile(r"[^.!?;\n]+(?:[.!?;]|$)")
LEAD_BLOCKERS = re.compile(
    r"^\s*(?:si\b|cuando\b|aunque\b|supongamos\b|imaginemos\b|por\s+ejemplo\b|quiz[aá]s\b|tal\s+vez\b)",
    re.I,
)
REPORTED = re.compile(r"\b(?:dice|dijo|afirma|afirmó|escribe|escribió|según|cita|citado)\b", re.I)
NEGATED = re.compile(r"\bno\s+(?:llamamos|denominamos|definimos|se\s+define|significa|designa)\b", re.I)
QUOTED = re.compile(r"^\s*[«“\"'].*[»”\"']\s*[.!?;]?$", re.S)
TERM = r"(?P<t>[\wÁÉÍÓÚÜÑáéíóúüñφΦψΨ₀-₉0-9][^,.;:!?\n]{0,78}?)"
BODY_PATTERNS = (
    ("llamamos_a", re.compile(r"^\s*llamamos\s+(?:a\s+)?" + TERM + r"\s+a\s+\S", re.I)),
    ("denominamos_a", re.compile(r"^\s*denominamos\s+(?:a\s+)?" + TERM + r"\s+a\s+\S", re.I)),
    ("definimos_como", re.compile(r"^\s*definimos\s+(?:a\s+)?" + TERM + r"\s+como\s+\S", re.I)),
    ("por_se_entiende", re.compile(r"^\s*por\s+" + TERM + r"\s+se\s+entiende\s+\S", re.I)),
    ("se_define_como", re.compile(r"^\s*" + TERM + r"\s+se\s+define\s+como\s+\S", re.I)),
    ("significa", re.compile(r"^\s*" + TERM + r"\s+significa\s+\S", re.I)),
    ("designa", re.compile(r"^\s*" + TERM + r"\s+designa\s+\S", re.I)),
)

spec = importlib.util.spec_from_file_location("conceptos_generico_fase10", GENERIC)
assert spec and spec.loader
g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)

PREAMBLE_PREFIXES = (
    "los términos ",
    "los terminos ",
    "este glosario ",
    "las remisiones ",
    "las entradas ",
    "entradas del ",
    "se indica ",
    "términos técnicos ",
    "terminos tecnicos ",
    "índice de ",
    "indice de ",
    "entre toda ",
    "cómo leer ",
    "como leer ",
    "construcción original",
    "construccion original",
    "operación principal",
    "operacion principal",
    "aplicaciones",
    "las referencias ",
    "los libros ",
    "en caracteres ",
    "los nombres propios ",
)
LINE_BLOCK_PREFIXES = (
    "afrodita areia:",
    "metrología causal",
    "metrologia causal",
)


def load(path: Path) -> list[dict]:
    return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x]


def dump(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in rows),
        encoding="utf-8",
    )


def producer(row: dict) -> dict:
    row["producido_por"] = {"motor": MOTOR, "version": VERSION}
    return row


def _is_structural(line: str) -> bool:
    s = line.strip()
    if not s or s.startswith("#") or s.startswith("<!--") or s == "---":
        return True
    if ROMAN.fullmatch(s) or ALPHA_HEADER.fullmatch(s):
        return True
    n = g.norm(s)
    return n.startswith(LINE_BLOCK_PREFIXES) or "· vol." in n


def _term_candidate(line: str) -> bool:
    s = line.strip()
    if _is_structural(s) or ARROW.match(s):
        return False
    if len(s) > 100 or s[-1:] in ".,;:!?":
        return False
    if "," in s or "—" in s:
        return False
    words = s.split()
    if not 1 <= len(words) <= 8:
        return False
    n = g.norm(s)
    if n.startswith(PREAMBLE_PREFIXES):
        return False
    first = s[0]
    return first.isupper() or first in "αΔφΦψΨ"


def _reference_index(lines: list[str], start: int) -> bool:
    lead = g.norm(" ".join(lines[start + 1 : min(len(lines), start + 45)]))
    return "este glosario localiza los términos del paradigma; no los define" in lead


def _append_unique(out: list[tuple[str, int, str]], seen: set[str], term: str, line: int, fmt: str) -> None:
    key = g.norm(term)
    if not key:
        return
    if key in seen:
        raise SystemExit(f"Lema duplicado: {term}")
    seen.add(key)
    out.append((term, line, fmt))


def _arrow_entries(lines: list[str], start: int) -> list[tuple[str, int, str]]:
    arrows = [i for i in range(start + 1, len(lines)) if ARROW.match(lines[i].strip())]
    out: list[tuple[str, int, str]] = []
    seen: set[str] = set()
    segment_start = start + 1
    for arrow_i in arrows:
        candidates = [
            i for i in range(segment_start, arrow_i)
            if _term_candidate(lines[i])
        ]
        if not candidates:
            segment_start = arrow_i + 1
            continue
        term_i = candidates[0]
        body = any(
            lines[j].strip()
            and not _is_structural(lines[j])
            and not ARROW.match(lines[j].strip())
            for j in range(term_i + 1, arrow_i)
        )
        if body:
            _append_unique(out, seen, lines[term_i].strip(), term_i + 1, "remision_flecha")
        segment_start = arrow_i + 1
    return out


def _reference_entries(lines: list[str], start: int) -> list[tuple[str, int, str]]:
    out: list[tuple[str, int, str]] = []
    seen: set[str] = set()
    for i in range(start + 1, len(lines)):
        m = REFERENCE_DASH.match(lines[i].strip())
        if m:
            term = m.group("t").strip()
            if _term_candidate(term):
                _append_unique(out, seen, term, i + 1, "remision_inline")
    return out


def _inline_colon_boundary(lines: list[str], i: int, start: int) -> bool:
    """Distingue una entrada ``Lema: cuerpo`` de dos puntos dentro del cuerpo."""
    if i <= start + 1:
        return True
    prev = lines[i - 1].strip()
    if not prev or _is_structural(prev) or ARROW.match(prev):
        return True
    if INLINE_COLON.match(prev):
        return True
    return prev.endswith((".", "!", "?"))


def _colon_entries(lines: list[str], start: int) -> list[tuple[str, int, str]]:
    out: list[tuple[str, int, str]] = []
    seen: set[str] = set()
    for i in range(start + 1, len(lines)):
        raw = lines[i].strip()
        if _is_structural(raw) or not _inline_colon_boundary(lines, i, start):
            continue
        m = INLINE_COLON.match(raw)
        if not m:
            continue
        term = m.group("t").strip()
        if _term_candidate(term):
            _append_unique(out, seen, term, i + 1, "definicion_inline")
    return out


def _previous_boundary(lines: list[str], i: int, start: int) -> bool:
    if i <= start + 1:
        return True
    prev = lines[i - 1].strip()
    if not prev or _is_structural(prev) or ARROW.match(prev):
        return True
    return prev.endswith((".", "!", "?"))


def _plain_entries(lines: list[str], start: int) -> list[tuple[str, int, str]]:
    out: list[tuple[str, int, str]] = []
    seen: set[str] = set()
    for i in range(start + 1, len(lines)):
        term = lines[i].strip()
        if not _term_candidate(term) or not _previous_boundary(lines, i, start):
            continue
        j = i + 1
        while j < len(lines) and _is_structural(lines[j]):
            j += 1
        if j >= len(lines):
            continue
        body = lines[j].strip()
        if not body or ARROW.match(body):
            continue
        _append_unique(out, seen, term, i + 1, "lema_definicion")
    return out


def glossary_entries(path: Path) -> list[tuple[str, int, str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    start = next((i for i, x in enumerate(lines) if "glosario" in g.norm(x)), None)
    if start is None:
        raise SystemExit(f"Glosario sin encabezado: {path}")
    if _reference_index(lines, start):
        return []

    tail = lines[start + 1 :]
    colon_terms = []
    for i in range(start + 1, len(lines)):
        raw = lines[i].strip()
        if _is_structural(raw) or not _inline_colon_boundary(lines, i, start):
            continue
        m = INLINE_COLON.match(raw)
        if m and _term_candidate(m.group("t").strip()):
            colon_terms.append(m.group("t").strip())

    if any(ARROW.match(x.strip()) for x in tail):
        out = _arrow_entries(lines, start)
    elif sum(bool(REFERENCE_DASH.match(x.strip())) for x in tail) >= 2:
        out = _reference_entries(lines, start)
    elif len(colon_terms) >= 3:
        out = _colon_entries(lines, start)
    else:
        out = _plain_entries(lines, start)

    if not out:
        raise SystemExit(f"Glosario sin entradas recuperables conservadoramente: {path}")
    return out


def _declared_on_line(raw_line: str, term: str, fmt: str) -> bool:
    s = raw_line.strip()
    if fmt in {"remision_flecha", "lema_definicion"}:
        return s == term
    if fmt == "remision_inline":
        m = REFERENCE_DASH.match(s)
        return bool(m and g.norm(m.group("t")) == g.norm(term))
    if fmt == "definicion_inline":
        m = INLINE_COLON.match(s)
        return bool(m and g.norm(m.group("t")) == g.norm(term))
    return False


def strict_records(
    obra_id: str, units: list[dict], glossary_rel: str
) -> tuple[list[dict], list[dict], set[str]]:
    entries = glossary_entries(ROOT / glossary_rel)
    lines = (ROOT / glossary_rel).read_text(encoding="utf-8").splitlines()
    apps: list[dict] = []
    concepts: list[dict] = []
    confirmed: set[str] = set()
    seen_ids: set[str] = set()

    for term, term_line, fmt in entries:
        key = g.norm(term)
        confirmed.add(key)
        cid = g.stable_id("CON", key)
        pattern = re.compile(
            r"(?<!\w)" + r"\s+".join(re.escape(x) for x in term.split()) + r"(?!\w)",
            re.I,
        )
        linked: list[str] = []
        evidence: list[str] = []

        for u in units:
            text = u["texto_literal"]
            for m in pattern.finditer(text):
                ls, le = g.line_range(u, text, m.start(), m.end())
                literal = m.group(0)
                line_prefix = text[text.rfind("\n", 0, m.start()) + 1 : m.start()]
                declaration = (
                    u["archivo"] == glossary_rel
                    and ls == le == term_line
                    and not line_prefix.strip()
                    and _declared_on_line(lines[term_line - 1], term, fmt)
                    and g.norm(literal) == key
                )
                linked_here = declaration or (len(term.split()) > 1 and g.norm(literal) == key)
                aid = g.stable_id("APC", cid, u["id"], str(ls), str(m.start()), literal)
                if aid in seen_ids:
                    raise SystemExit(f"Aparición duplicada: {aid}")
                seen_ids.add(aid)
                r = g.base_record(aid, "aparicion_conceptual", literal)
                producer(r)
                r["estado_extraccion"] = "extraido" if linked_here else "candidato"
                r.update(
                    {
                        "fuente_id": obra_id,
                        "unidad_id": u["id"],
                        "concepto_id": cid if linked_here else None,
                        "forma_literal": literal,
                        "variante_formal": None if literal == term else term,
                        "variantes_lexicas_busqueda": [],
                        "localizacion": {
                            "ruta": u["archivo"],
                            "linea_inicio": ls,
                            "linea_fin": le,
                        },
                        "criterio_deteccion": (
                            "lema_en_glosario_tecnico_explicito"
                            if declaration
                            else (
                                "designacion_tecnica_multilexema_exacta; sin_normalizacion_semantica"
                                if linked_here
                                else "coincidencia_formal_con_lema_glosario; identidad_conceptual_no_determinada"
                            )
                        ),
                    }
                )
                apps.append(r)
                if linked_here:
                    linked.append(aid)
                if declaration:
                    evidence.append(aid)

        if len(evidence) != 1:
            raise SystemExit(f"Lema {term!r}: evidencia declarativa={len(evidence)}")
        c = g.base_record(cid, "concepto", term)
        producer(c)
        c["estado_extraccion"] = "extraido"
        c.update(
            {
                "designacion_operativa": term,
                "aparicion_ids": sorted(linked),
                "formas_literales_observadas": [term],
                "estado_identidad_conceptual": "establecida_por_evidencia",
                "evidencia_identidad_ids": evidence,
            }
        )
        concepts.append(c)

    return apps, concepts, confirmed


def explicit_body_evidence(units: list[dict]) -> list[tuple[str, str, int, int, str]]:
    """Localiza designaciones solo en declaraciones textuales inequívocas."""
    found = []
    for unit in units:
        text = unit["texto_literal"]
        for cm in CLAUSE_RE.finditer(text):
            clause = cm.group(0)
            stripped = clause.strip()
            if (
                not stripped
                or "?" in stripped
                or LEAD_BLOCKERS.search(stripped)
                or NEGATED.search(stripped)
                or REPORTED.search(stripped)
                or QUOTED.match(stripped)
            ):
                continue
            for name, pattern in BODY_PATTERNS:
                match = pattern.search(clause)
                if not match:
                    continue
                raw = match.group("t")
                tokens = g.token_rows(raw)
                if not tokens or len(tokens) > 8:
                    continue
                trimmed = g.trim_candidate(tokens, 0, len(tokens))
                if trimmed is None:
                    continue
                a, b = trimmed
                off0, off1 = tokens[a][2], tokens[b - 1][3]
                literal = raw[off0:off1]
                key = g.norm(literal)
                start = cm.start() + match.start("t") + off0
                end = cm.start() + match.start("t") + off1
                if key:
                    found.append(
                        (
                            unit["id"],
                            key,
                            start,
                            end,
                            f"declaracion_designativa_explicita_en_cuerpo:{name}",
                        )
                    )
    return found


def promote_body_evidence(
    units: list[dict], apps: list[dict], concepts: list[dict], confirmed: set[str]
) -> int:
    by_key = {g.norm(c["designacion_operativa"]): c for c in concepts}
    by_unit_key: dict[tuple[str, str], list[dict]] = {}
    for app in apps:
        by_unit_key.setdefault((app["unidad_id"], g.norm(app["forma_literal"])), []).append(app)
    unit_by_id = {u["id"]: u for u in units}
    promoted: set[str] = set()

    for uid, key, start, end, criterion in explicit_body_evidence(units):
        if key in confirmed:
            continue
        concept = by_key.get(key)
        if concept is None:
            continue
        unit = unit_by_id[uid]
        literal = unit["texto_literal"][start:end]
        matches = [
            a for a in by_unit_key.get((uid, key), [])
            if a["forma_literal"] == literal
        ]
        if len(matches) != 1:
            continue
        app = matches[0]
        app["estado_extraccion"] = "extraido"
        app["criterio_deteccion"] = criterion
        evidence = concept.setdefault("evidencia_identidad_ids", [])
        if app["id"] not in evidence:
            evidence.append(app["id"])
        concept["estado_identidad_conceptual"] = "establecida_por_evidencia"
        concept["estado_extraccion"] = "extraido"
        promoted.add(concept["id"])

    for concept in concepts:
        if concept.get("estado_identidad_conceptual") == "establecida_por_evidencia":
            concept["evidencia_identidad_ids"] = sorted(
                set(concept.get("evidencia_identidad_ids", []))
            )
    return len(promoted)


def coverage(obra_id: str, n: int) -> dict:
    r = g.coverage_record(obra_id, n)
    producer(r)
    r["id"] = g.stable_id("COB", obra_id, MOTOR, VERSION)
    r["motor"] = MOTOR
    r["version_motor"] = VERSION
    return r


def run(
    *,
    obra_id: str,
    fuentes: Path,
    unidades: Path,
    apariciones: Path,
    conceptos: Path,
    cobertura: Path,
) -> dict:
    sources = [x for x in load(fuentes) if x.get("id") == obra_id]
    if len(sources) != 1:
        raise SystemExit(f"Fuente {obra_id}: {len(sources)}")
    units = [x for x in load(unidades) if x.get("fuente_id") == obra_id]
    if not units:
        raise SystemExit(f"Sin unidades: {obra_id}")
    gloss = [
        x for x in sources[0].get("rutas_derivadas", [])
        if str(x).endswith(GLOSSARY)
    ]
    if len(gloss) > 1:
        raise SystemExit(f"Glosarios ambiguos: {gloss}")

    sa: list[dict] = []
    sc: list[dict] = []
    confirmed: set[str] = set()
    glossary_mode = "sin_glosario"
    if gloss:
        glossary_path = ROOT / str(gloss[0])
        raw_lines = glossary_path.read_text(encoding="utf-8").splitlines()
        start = next((i for i, x in enumerate(raw_lines) if "glosario" in g.norm(x)), None)
        if start is None:
            raise SystemExit(f"Glosario sin encabezado: {glossary_path}")
        if _reference_index(raw_lines, start):
            glossary_mode = "indice_referencias_no_promovido"
        else:
            sa, sc, confirmed = strict_records(obra_id, units, str(gloss[0]))
            glossary_mode = "lemas_explicitos_promovidos"

    ga, gc = g.build_candidate_records(obra_id, units, confirmed_norms=confirmed)
    for r in ga + gc:
        producer(r)
    body_confirmed = promote_body_evidence(units, ga, gc, confirmed)

    all_a = sa + ga
    all_c = sc + gc
    all_a.sort(
        key=lambda r: (
            r["localizacion"]["ruta"],
            r["localizacion"]["linea_inicio"],
            r["id"],
        )
    )
    all_c.sort(key=lambda r: r["id"])
    ids = [r["id"] for r in all_a + all_c]
    if len(ids) != len(set(ids)):
        raise SystemExit("IDs conceptuales duplicados")

    dump(apariciones, all_a)
    dump(conceptos, all_c)
    dump(cobertura, [coverage(obra_id, len(units))])
    return {
        "version": VERSION,
        "obra_id": obra_id,
        "unidades": len(units),
        "glosario": gloss[0] if gloss else None,
        "modo_glosario": glossary_mode,
        "conceptos_confirmados_glosario": len(sc),
        "conceptos_confirmados_cuerpo": body_confirmed,
        "conceptos_confirmados": len(sc) + body_confirmed,
        "conceptos_candidatos": sum(
            c.get("estado_identidad_conceptual") == "no_determinada" for c in all_c
        ),
        "apariciones": len(all_a),
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--obra-id", required=True)
    p.add_argument("--fuentes", type=Path, required=True)
    p.add_argument("--unidades", type=Path, required=True)
    p.add_argument("--apariciones", type=Path, required=True)
    p.add_argument("--conceptos", type=Path, required=True)
    p.add_argument("--cobertura", type=Path, required=True)
    a = p.parse_args()
    print(
        json.dumps(
            run(
                obra_id=a.obra_id,
                fuentes=a.fuentes,
                unidades=a.unidades,
                apariciones=a.apariciones,
                conceptos=a.conceptos,
                cobertura=a.cobertura,
            ),
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())