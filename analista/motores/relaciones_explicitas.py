#!/usr/bin/env python3
"""Motor conservador de relaciones explícitas — Fase 4E, v1.1.0.

Registra únicamente pares de conceptos 4A unidos por construcciones textuales
observables. La identidad de los referentes exige una designación conceptual
literal exacta (ignorando solo caja/NFKC y saltos de línea de maquetación), salvo
el lema técnico activo del glosario, que aporta el sujeto contextual de su propia
definición.

No resuelve abreviaturas, plurales, similitud semántica, transitividad ni
coaparición. Los patrones son familias sintácticas; no contienen IDs de la
muestra de Fase 8 ni consultan el patrón de oro.
"""
from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FUENTES = ROOT / "analista/generado/fuentes.jsonl"
UNIDADES = ROOT / "analista/generado/unidades.jsonl"
CONCEPTOS = ROOT / "analista/generado/conceptos.jsonl"
SALIDA = ROOT / "analista/generado/relaciones-explicitas.jsonl"
COBERTURA = ROOT / "analista/generado/cobertura-relaciones.jsonl"
PILOTO_ID = "AA-SP-V1"
GLOSARIO_SUFFIX = "99-glosario.md"
SCHEMA_VERSION = "1.0.0"
MOTOR_VERSION = "1.1.0"
CF_RE = re.compile(r"\bcf\.\s*(.+)$", re.IGNORECASE)
NOMBRE_TECNICO_RE = re.compile(r"^\s*Nombre técnico del\s+([^:.;]+)", re.IGNORECASE)


def norm(text: str) -> str:
    return " ".join(unicodedata.normalize("NFKC", text).casefold().split())


def concept_term_regex(name: str) -> str:
    """Patrón de una designación exacta con whitespace de maquetación flexible."""
    parts = name.split()
    body = r"\s+".join(re.escape(part) for part in parts)
    return rf"(?<!\w)(?:{body})(?!\w)"


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


def base(record_id: str, kind: str, literal: str | None, extraction: str, audit: str) -> dict:
    return {
        "id": record_id,
        "tipo_registro": kind,
        "schema_version": SCHEMA_VERSION,
        "texto_literal": literal,
        "normalizacion_formal": None,
        "normalizacion_lexica": None,
        "estatus_enunciativo": None,
        "estado_extraccion": extraction,
        "estado_verificacion": "pendiente",
        "estado_auditoria": audit,
        "producido_por": {"motor": "relaciones_explicitas", "version": MOTOR_VERSION},
    }


def line_range(unit: dict, text: str, start: int, end: int) -> tuple[int, int]:
    base_line = unit["localizacion"]["linea_inicio"]
    line_start = base_line + text[:start].count("\n")
    line_end = line_start + text[start:end].count("\n")
    return line_start, line_end


def expand_left_determiner(text: str, start: int) -> int:
    prefix = text[max(0, start - 18):start]
    match = re.search(r"(?:^|\s)(El|La|el|la|mi|Mi|Ese|Esa|ese|esa)\s+$", prefix)
    return start - (len(prefix) - match.start(1)) if match else start


def expand_terminal_period(text: str, end: int) -> int:
    return end + 1 if end < len(text) and text[end] == "." else end


def unit_for_span(units: list[dict], route: str, start_line: int, end_line: int) -> dict:
    matches = [
        unit for unit in units
        if unit["archivo"] == route
        and unit["localizacion"]["linea_inicio"] <= start_line
        and end_line <= unit["localizacion"]["linea_fin"]
    ]
    if len(matches) != 1:
        raise SystemExit(
            f"El rango {route}:{start_line}-{end_line} no tiene unidad contenedora única: "
            f"{[m['id'] for m in matches]}"
        )
    return matches[0]


@dataclass(frozen=True)
class Candidate:
    subject_id: str
    target_id: str
    start: int
    end: int
    priority: int


def main() -> int:
    fuentes = load_jsonl(FUENTES)
    unidades = load_jsonl(UNIDADES)
    conceptos = load_jsonl(CONCEPTOS)

    fuente = next((row for row in fuentes if row.get("id") == PILOTO_ID), None)
    if fuente is None:
        raise SystemExit(f"No existe fuente piloto {PILOTO_ID}")
    glosarios = [route for route in fuente.get("rutas_derivadas", []) if route.endswith(GLOSARIO_SUFFIX)]
    if len(glosarios) != 1:
        raise SystemExit(f"Glosario ambiguo o ausente: {glosarios}")
    glosario_rel = glosarios[0]
    glosario_lines = (ROOT / glosario_rel).read_text(encoding="utf-8").splitlines()
    pilot_units = sorted(
        (row for row in unidades if row.get("fuente_id") == PILOTO_ID),
        key=lambda row: row["orden_textual"],
    )

    concept_by_norm = {norm(row["designacion_operativa"]): row for row in conceptos}
    concept_by_id = {row["id"]: row for row in conceptos}
    if len(concept_by_norm) != len(conceptos):
        raise SystemExit("Designaciones conceptuales duplicadas tras normalización formal.")

    names = sorted((row["designacion_operativa"] for row in conceptos), key=len, reverse=True)
    term_alt = "(?:" + "|".join(concept_term_regex(name) for name in names) + ")"

    def concept_from_surface(surface: str) -> dict | None:
        return concept_by_norm.get(norm(surface))

    relations: list[dict] = []
    seen_records: set[tuple] = set()

    def emit(subject: dict, target: dict, literal: str, route: str, start_line: int, end_line: int) -> None:
        if subject["id"] == target["id"]:
            return
        unit = unit_for_span(pilot_units, route, start_line, end_line)
        identity = (unit["id"], subject["id"], target["id"], literal, start_line, end_line)
        if identity in seen_records:
            return
        seen_records.add(identity)
        record_id = stable_id(
            "REL", subject["id"], target["id"], route, str(start_line), str(end_line), literal
        )
        record = base(record_id, "relacion_explicita", literal, "extraido", "pendiente")
        record.update(
            {
                "fuente_id": PILOTO_ID,
                "unidad_id": unit["id"],
                "sujeto_ref": subject["id"],
                "objeto_ref": target["id"],
                "relacion_literal": literal,
                "clasificacion_relacion": "relacion_explicita",
                "localizacion": {
                    "ruta": route,
                    "linea_inicio": start_line,
                    "linea_fin": end_line,
                },
            }
        )
        relations.append(record)

    # --- Glosario: el lema técnico activo puede aportar el sujeto contextual. ---
    term_positions: list[tuple[int, dict]] = []
    seen_concepts: set[str] = set()
    for line_no, line in enumerate(glosario_lines, start=1):
        concept = concept_by_norm.get(norm(line.strip()))
        if concept is None:
            continue
        if concept["id"] in seen_concepts:
            raise SystemExit(
                f"El lema {concept['designacion_operativa']!r} aparece como línea autónoma más de una vez."
            )
        seen_concepts.add(concept["id"])
        term_positions.append((line_no, concept))
    if seen_concepts != set(concept_by_id):
        raise SystemExit("No todos los conceptos 4A tienen lema autónomo en el glosario.")

    contextual_templates = [
        rf"la acumulación de la (?P<o>{term_alt}) se detiene",
        rf"El recipiente [^;]{{0,180}}?(?P<o>{term_alt})[^;]{{0,100}}?sigue\s+existiendo",
        rf"pérdida del acceso al\s+instrumento que traducía la (?P<o>{term_alt}) en acto asumido\.",
        rf"la (?P<o>{term_alt}) opera",
        rf"a través de los ciclos de la\s+(?P<o>{term_alt})",
        rf"Distinguido de la (?P<o>{term_alt}), que es el\s+accidente del ego\.",
        rf"El ego que emerge en el evento único e irrepetible de la\s+(?P<o>{term_alt})",
        rf"Constituye el punto\s+de partida de la (?P<o>{term_alt})\.",
        rf"determinaciones producidas en el nivel de la\s+(?P<o>{term_alt})",
        rf"Accidente\s+del (?P<o>{term_alt}) en sentido aristotélico",
        rf"La función que orienta la voluntad desde la (?P<o>{term_alt})\s+\(el sesgo acumulado\) hacia el acto: φ₁ \(vₜ, cₜ\)\.",
        rf"Es la operación\s+de asunción que constituye al (?P<o>{term_alt})",
    ]
    contextual_res = [re.compile(pattern, re.IGNORECASE | re.DOTALL) for pattern in contextual_templates]
    inverse_trajectory_re = re.compile(
        rf"El\s+(?P<s>{term_alt})\s+no es ningún punto de la trayectoria: es la función\s+completa\.",
        re.IGNORECASE | re.DOTALL,
    )

    for index, (term_line, subject) in enumerate(term_positions):
        end_line = term_positions[index + 1][0] - 1 if index + 1 < len(term_positions) else len(glosario_lines)
        block_lines = glosario_lines[term_line:end_line]
        block = "\n".join(block_lines)
        block_base_line = term_line + 1

        # Remisiones y formulación "Nombre técnico" conservan el comportamiento v1.0.0.
        for offset, literal in enumerate(block_lines):
            line_no = block_base_line + offset
            direct = NOMBRE_TECNICO_RE.match(literal)
            if direct:
                target = concept_by_norm.get(norm(direct.group(1).strip()))
                if target is not None:
                    emit(subject, target, literal, glosario_rel, line_no, line_no)

            crossref = CF_RE.search(literal)
            if crossref:
                for raw_target in crossref.group(1).split(","):
                    target_text = raw_target.strip().rstrip(".;")
                    target = concept_by_norm.get(norm(target_text))
                    if target is not None:
                        emit(subject, target, literal, glosario_rel, line_no, line_no)

        for pattern in contextual_res:
            for match in pattern.finditer(block):
                target = concept_from_surface(match.group("o"))
                if target is None:
                    continue
                start, end = match.span()
                literal = block[start:end]
                start_line = block_base_line + block[:start].count("\n")
                end_line_match = start_line + literal.count("\n")
                emit(subject, target, literal, glosario_rel, start_line, end_line_match)

        # En la definición de Trayectoria del ego, la frase puede predicar del Ego
        # usando "la trayectoria" sin repetir el lema completo; el lema activo fija
        # inequívocamente el referente contextual, sin normalizar una variante léxica.
        if subject["designacion_operativa"] == "Trayectoria del ego":
            for match in inverse_trajectory_re.finditer(block):
                source = concept_from_surface(match.group("s"))
                if source is None:
                    continue
                start, end = match.span()
                literal = block[start:end]
                start_line = block_base_line + block[:start].count("\n")
                end_line_match = start_line + literal.count("\n")
                emit(source, subject, literal, glosario_rel, start_line, end_line_match)

    # --- Prosa: patrones sintácticos conservadores entre menciones exactas. ---
    # Este pase también recorre el glosario. Los registros coincidentes con el pase
    # contextual se deduplican por pareja, literal y rango; así puede recuperar una
    # predicación cuyo sujeto explícito no sea el lema activo del bloque.
    direct_re = re.compile(
        rf"(?P<s>{term_alt})(?P<m>(?:(?![.;]).){{0,140}}?\b(?:produce|produjo|producido|"
        rf"construye|construyó|determina|determinó|condiciona|constituye|crece)\b"
        rf"(?:(?![.;]).){{0,140}}?)(?P<o>{term_alt})",
        re.IGNORECASE | re.DOTALL,
    )
    es_de_re = re.compile(
        rf"(?P<s>{term_alt})\s+es\s+(?:(?![.;]).){{0,100}}?\b(?:del|de la|de los|de las)\s+"
        rf"(?P<o>{term_alt})",
        re.IGNORECASE | re.DOTALL,
    )
    como_re = re.compile(
        rf"(?P<s>{term_alt})\s+como\s+(?:(?![,.;]).){{1,90}}?\s+de\s+(?P<o>{term_alt})",
        re.IGNORECASE | re.DOTALL,
    )
    iteracion_re = re.compile(
        rf"la iteración de la\s+(?P<s>{term_alt})\s+describe: cada ciclo produce un\s+(?P<o>{term_alt})",
        re.IGNORECASE | re.DOTALL,
    )
    relative_re = re.compile(
        rf"la existencia de un\s+(?P<o>{term_alt})\s+que la\s+(?P<s>{term_alt})\s+"
        rf"(?:(?!\.).){{1,180}}?\.",
        re.IGNORECASE | re.DOTALL,
    )
    determined_re = re.compile(
        rf"(?P<s>{term_alt})(?:(?![.;]).){{0,100}}?(?:ha\s+determinado|determinó|determinado)"
        rf"(?:(?![.;]).){{0,100}}?(?P<o>{term_alt})\s+como propia",
        re.IGNORECASE | re.DOTALL,
    )

    for unit in pilot_units:
        if unit.get("tipo_estructural") == "encabezado":
            continue
        text = unit["texto_literal"]
        candidates: list[Candidate] = []

        def add_match(match: re.Match[str], priority: int, *, expand_left: bool = True) -> None:
            subject = concept_from_surface(match.group("s"))
            target = concept_from_surface(match.group("o"))
            if subject is None or target is None or subject["id"] == target["id"]:
                return
            start, end = match.span()
            if expand_left:
                start = expand_left_determiner(text, start)
            end = expand_terminal_period(text, end)
            candidates.append(Candidate(subject["id"], target["id"], start, end, priority))

        for match in determined_re.finditer(text):
            add_match(match, 100)
        for match in relative_re.finditer(text):
            add_match(match, 95, expand_left=False)
        for match in iteracion_re.finditer(text):
            add_match(match, 90, expand_left=False)
        for match in como_re.finditer(text):
            add_match(match, 85)
        for match in es_de_re.finditer(text):
            add_match(match, 80)
        for match in direct_re.finditer(text):
            add_match(match, 70)

        # Para una misma pareja y evidencia solapada conserva el patrón más
        # específico/largo; evita duplicar una relación por reglas anidadas.
        candidates.sort(key=lambda c: (-c.priority, c.start, -(c.end - c.start), c.subject_id, c.target_id))
        selected: list[Candidate] = []
        for candidate in candidates:
            overlaps = any(
                prior.subject_id == candidate.subject_id
                and prior.target_id == candidate.target_id
                and not (candidate.end <= prior.start or candidate.start >= prior.end)
                for prior in selected
            )
            if not overlaps:
                selected.append(candidate)

        for candidate in sorted(selected, key=lambda c: (c.start, c.end, c.subject_id, c.target_id)):
            literal = text[candidate.start:candidate.end]
            start_line, end_line = line_range(unit, text, candidate.start, candidate.end)
            emit(
                concept_by_id[candidate.subject_id],
                concept_by_id[candidate.target_id],
                literal,
                unit["archivo"],
                start_line,
                end_line,
            )

    relations.sort(
        key=lambda row: (
            row["localizacion"]["ruta"],
            row["localizacion"]["linea_inicio"],
            row["localizacion"]["linea_fin"],
            row["sujeto_ref"],
            row["objeto_ref"],
            row["id"],
        )
    )
    dump_jsonl(SALIDA, relations)

    coverage = base(
        stable_id("COB", PILOTO_ID, "relaciones_explicitas", MOTOR_VERSION),
        "reporte_cobertura",
        None,
        "extraido",
        "no_aplica",
    )
    coverage.update(
        {
            "obra_id": PILOTO_ID,
            "motor": "relaciones_explicitas",
            "version_motor": MOTOR_VERSION,
            "unidades_totales": len(pilot_units),
            "unidades_procesadas": len(pilot_units),
            "unidades_omitidas": [],
            "errores": [],
        }
    )
    dump_jsonl(COBERTURA, [coverage])
    print(
        f"Fase 4E v{MOTOR_VERSION}: {len(relations)} relaciones explícitas con referentes exactos; "
        f"{len(pilot_units)} unidades procesadas; sin transitividad, abreviaturas ni fusión léxica."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
