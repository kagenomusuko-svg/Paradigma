#!/usr/bin/env python3
"""Verificador mecánico de evidencia — Fase 6. No reclasifica contenido.

La política de productor es cerrada por defecto. En Fase 10 puede autorizarse
explícitamente una versión de productor distinta mediante ``--producer-version``;
la autorización solo cambia la versión esperada del motor nombrado y no relaja
ninguna comprobación de evidencia, esquema, fuente, unidad o referencia.
"""
from __future__ import annotations

import argparse
import collections
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DF = ROOT / "analista/generado/fuentes.jsonl"
DU = ROOT / "analista/generado/unidades.jsonl"
DI = ROOT / "analista/generado/normalizados"
DO = ROOT / "analista/generado/verificados"

FILES = (
    "apariciones-conceptuales.jsonl",
    "conceptos.jsonl",
    "definiciones.jsonl",
    "afirmaciones-candidatas.jsonl",
    "formulas-candidatas.jsonl",
    "relaciones-explicitas.jsonl",
    "distinciones.jsonl",
    "negaciones.jsonl",
    "excepciones.jsonl",
    "restricciones-alcance.jsonl",
)
PRODUCER = {
    "aparicion_conceptual": ("conceptos_apariciones", "1.1.0"),
    "concepto": ("conceptos_apariciones", "1.1.0"),
    "definicion": ("definiciones", "1.1.0"),
    "afirmacion": ("afirmaciones", "1.1.0"),
    "formula": ("formulas", "1.1.0"),
    "relacion_explicita": ("relaciones_explicitas", "1.1.0"),
    "distincion": ("limitadores", "1.1.0"),
    "negacion": ("limitadores", "1.1.0"),
    "excepcion": ("limitadores", "1.1.0"),
    "restriccion_alcance": ("limitadores", "1.1.0"),
}


def load(path: Path) -> list[dict]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line
    ]


def dump(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows),
        encoding="utf-8",
    )


def excerpt(repo: Path, loc: dict, cache: dict[str, list[str]]) -> str:
    route = loc["ruta"]
    cache.setdefault(route, (repo / route).read_text(encoding="utf-8").splitlines())
    start, end = loc["linea_inicio"], loc["linea_fin"]
    lines = cache[route]
    if not isinstance(start, int) or not isinstance(end, int) or not 1 <= start <= end <= len(lines):
        raise ValueError("rango")
    return "\n".join(lines[start - 1 : end])


def literal_excerpt(literal: str, source_excerpt: str) -> bool:
    if not literal:
        return False
    pos = source_excerpt.find(literal)
    return pos >= 0 and "\n" not in source_excerpt[:pos] and "\n" not in source_excerpt[pos + len(literal) :]


def occurrences(unit: dict, literal: str) -> list[tuple[int, int]]:
    if not literal:
        return []
    text = unit["texto_literal"]
    base = unit["localizacion"]["linea_inicio"]
    out: list[tuple[int, int]] = []
    start = 0
    while True:
        pos = text.find(literal, start)
        if pos < 0:
            break
        line_start = base + text[:pos].count("\n")
        out.append((line_start, line_start + literal.count("\n")))
        start = pos + 1
    return out


def located(unit: dict, literal: str, loc: dict) -> bool:
    return (loc["linea_inicio"], loc["linea_fin"]) in occurrences(unit, literal)


def producer_policy(overrides: list[str]) -> dict[str, tuple[str, str]]:
    """Construye una política exacta; ninguna versión adicional se acepta implícitamente."""
    policy = dict(PRODUCER)
    motor_to_types: dict[str, list[str]] = collections.defaultdict(list)
    for record_type, (motor, _version) in policy.items():
        motor_to_types[motor].append(record_type)

    for spec in overrides:
        if "=" not in spec:
            raise SystemExit(
                f"--producer-version inválido {spec!r}; formato requerido MOTOR=VERSION"
            )
        motor, version = spec.split("=", 1)
        motor = motor.strip()
        version = version.strip()
        if not motor or not version:
            raise SystemExit(
                f"--producer-version inválido {spec!r}; formato requerido MOTOR=VERSION"
            )
        record_types = motor_to_types.get(motor)
        if not record_types:
            raise SystemExit(f"Motor no autorizado en política de verificación: {motor}")
        for record_type in record_types:
            policy[record_type] = (motor, version)
    return policy


def producer(record: dict, policy: dict[str, tuple[str, str]]) -> bool:
    expected = policy.get(record.get("tipo_registro"))
    return bool(
        expected
        and record.get("schema_version") == "1.0.0"
        and record.get("producido_por")
        == {"motor": expected[0], "version": expected[1]}
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    parser.add_argument("--fuentes", type=Path, default=DF)
    parser.add_argument("--unidades", type=Path, default=DU)
    parser.add_argument("--input-root", type=Path, default=DI)
    parser.add_argument("--output-root", type=Path, default=DO)
    parser.add_argument(
        "--producer-version",
        action="append",
        default=[],
        metavar="MOTOR=VERSION",
        help=(
            "Autoriza de forma explícita una versión exacta para un motor ya permitido. "
            "Puede repetirse; no añade motores ni tipos de registro nuevos."
        ),
    )
    args = parser.parse_args()
    policy = producer_policy(args.producer_version)

    sources = {row["id"]: row for row in load(args.fuentes)}
    units = {row["id"]: row for row in load(args.unidades)}
    by = {name: load(args.input_root / name) for name in FILES}
    flat = [row for rows in by.values() for row in rows]
    counts = collections.Counter(row.get("id") for row in flat)
    apps = {row["id"]: row for row in by["apariciones-conceptuales.jsonl"]}
    concepts = {row["id"]: row for row in by["conceptos.jsonl"]}
    affirm = {row["id"]: row for row in by["afirmaciones-candidatas.jsonl"]}
    cache: dict[str, list[str]] = {}

    used = {row.get("fuente_id") for row in flat if row.get("fuente_id")}
    source_ok: dict[str, bool] = {}
    for source_id in used:
        source = sources.get(source_id)
        ok = bool(source)
        try:
            if ok:
                digest = hashlib.sha256((args.repo_root / source["ruta_canonica"]).read_bytes()).hexdigest()
                ok = (
                    source.get("schema_version") == "1.0.0"
                    and source.get("producido_por") == {"motor": "fuentes", "version": "1.0.1"}
                    and source.get("sha256") == digest
                    and source.get("version_fuente") == f"sha256:{digest}"
                    and set(source.get("rutas_derivadas", []))
                    == set(source.get("segmentaciones", []))
                )
        except Exception:
            ok = False
        source_ok[source_id] = bool(ok)

    unit_ok: dict[str, bool] = {}

    def verify_unit(unit_id: str) -> bool:
        if unit_id in unit_ok:
            return unit_ok[unit_id]
        unit = units.get(unit_id)
        ok = bool(unit)
        try:
            if ok:
                source = sources.get(unit["fuente_id"])
                loc = unit["localizacion"]
                ok = (
                    unit.get("schema_version") == "1.0.0"
                    and unit.get("producido_por") == {"motor": "unidades", "version": "1.0.0"}
                    and source_ok.get(unit["fuente_id"], False)
                    and source is not None
                    and unit["archivo"] == loc["ruta"]
                    and unit["archivo"] in source.get("rutas_derivadas", [])
                    and excerpt(args.repo_root, loc, cache) == unit["texto_literal"]
                    and hashlib.sha256(unit["texto_literal"].encode()).hexdigest()
                    == unit["sha256_texto"]
                )
        except Exception:
            ok = False
        unit_ok[unit_id] = bool(ok)
        return bool(ok)

    verdict: dict[str, bool] = {}
    reasons: dict[str, list[str]] = {}

    def fail(record_id: str, why: str) -> None:
        reasons.setdefault(record_id, []).append(why)

    for name, rows in by.items():
        if name == "conceptos.jsonl":
            continue
        for record in rows:
            record_id = record.get("id", "")
            kind = record["tipo_registro"]
            ok = True
            source_id = record.get("fuente_id")
            unit_id = record.get("unidad_id")
            unit = units.get(unit_id)

            if counts[record_id] != 1:
                fail(record_id, "id_no_unico")
                ok = False
            if not producer(record, policy):
                fail(record_id, "version_o_productor")
                ok = False
            if not source_ok.get(source_id, False):
                fail(record_id, "fuente_o_hash")
                ok = False
            if not verify_unit(unit_id):
                fail(record_id, "unidad")
                ok = False

            try:
                loc = record["localizacion"]
                source_excerpt = excerpt(args.repo_root, loc, cache)
                if (
                    unit is None
                    or unit.get("fuente_id") != source_id
                    or loc["ruta"] != unit.get("archivo")
                ):
                    fail(record_id, "unidad_fuente_ruta")
                    ok = False

                if kind == "aparicion_conceptual":
                    ok = (
                        ok
                        and record["texto_literal"] == record["forma_literal"]
                        and located(unit, record["forma_literal"], loc)
                        and (
                            record.get("concepto_id") is None
                            or record["concepto_id"] in concepts
                        )
                    )
                elif kind == "definicion":
                    ok = (
                        ok
                        and unit["localizacion"]["linea_inicio"]
                        <= loc["linea_inicio"]
                        <= unit["localizacion"]["linea_fin"]
                        and literal_excerpt(record["texto_literal"], source_excerpt)
                        and record.get("concepto_id") in concepts
                    )
                elif kind == "afirmacion":
                    ok = (
                        ok
                        and unit["localizacion"]["linea_inicio"]
                        <= loc["linea_inicio"]
                        <= loc["linea_fin"]
                        <= unit["localizacion"]["linea_fin"]
                        and literal_excerpt(record["texto_literal"], source_excerpt)
                        and all(concept_id in concepts for concept_id in record.get("concepto_ids", []))
                    )
                elif kind == "formula":
                    ok = (
                        ok
                        and record["texto_literal"] == record["formula_literal"]
                        and located(unit, record["formula_literal"], loc)
                        and unit["id"] in record.get("contexto_unidad_ids", [])
                        and all(
                            verify_unit(context_id)
                            and units[context_id]["fuente_id"] == source_id
                            and units[context_id]["archivo"] == unit["archivo"]
                            for context_id in record.get("contexto_unidad_ids", [])
                        )
                    )
                elif kind == "relacion_explicita":
                    ok = (
                        ok
                        and record["texto_literal"] == record["relacion_literal"]
                        and literal_excerpt(record["relacion_literal"], source_excerpt)
                        and record.get("sujeto_ref") in concepts
                        and record.get("objeto_ref") in concepts
                    )
                elif kind == "distincion":
                    ok = (
                        ok
                        and located(unit, record["texto_literal"], loc)
                        and record["termino_a_literal"] in record["texto_literal"]
                        and record["termino_b_literal"] in record["texto_literal"]
                        and (
                            record.get("marcador_literal") is None
                            or record["marcador_literal"] in source_excerpt
                        )
                    )
                elif kind == "negacion":
                    ok = (
                        ok
                        and located(unit, record["texto_literal"], loc)
                        and record["objeto_negado_literal"] in source_excerpt
                        and (
                            record.get("alcance_literal") is None
                            or record["alcance_literal"] in source_excerpt
                        )
                    )
                elif kind == "excepcion":
                    ok = (
                        ok
                        and record["texto_literal"] == record["fragmento_exceptivo_literal"]
                        and located(unit, record["texto_literal"], loc)
                        and (
                            record.get("afirmacion_limitada_id") is None
                            or record["afirmacion_limitada_id"] in affirm
                        )
                    )
                elif kind == "restriccion_alcance":
                    ok = (
                        ok
                        and record["texto_literal"] == record["fragmento_restriccion_literal"]
                        and located(unit, record["texto_literal"], loc)
                        and (
                            record.get("afirmacion_limitada_id") is None
                            or record["afirmacion_limitada_id"] in affirm
                        )
                    )
            except Exception:
                ok = False
                fail(record_id, "excepcion_verificacion")

            if not ok and record_id not in reasons:
                fail(record_id, "evidencia_directa")
            verdict[record_id] = bool(ok)

    for concept in by["conceptos.jsonl"]:
        record_id = concept["id"]
        ok = counts[record_id] == 1 and producer(concept, policy)
        appearance_ids = concept.get("aparicion_ids", [])
        evidence_ids = concept.get("evidencia_identidad_ids", [])
        ok = (
            ok
            and bool(appearance_ids)
            and all(
                appearance_id in apps
                and verdict.get(appearance_id, False)
                and apps[appearance_id].get("concepto_id") == record_id
                for appearance_id in appearance_ids
            )
            and all(evidence_id in appearance_ids for evidence_id in evidence_ids)
        )
        if concept.get("estado_identidad_conceptual") == "establecida_por_evidencia":
            ok = ok and bool(evidence_ids) and all(
                verdict.get(evidence_id, False) for evidence_id in evidence_ids
            )
        if not ok:
            fail(record_id, "version_o_productor_o_evidencia_identidad")
        verdict[record_id] = bool(ok)

    total = 0
    failed = 0
    for name, rows in by.items():
        out: list[dict] = []
        for source_record in rows:
            record = copy.deepcopy(source_record)
            good = verdict.get(record["id"], False)
            record["estado_verificacion"] = "verificado" if good else "fallido"
            total += 1
            failed += int(not good)
            out.append(record)
        dump(args.output_root / name, out)

    print(
        json.dumps(
            {
                "total": total,
                "verificados": total - failed,
                "fallidos": failed,
                "fuentes": source_ok,
                "unidades_comprobadas": len(unit_ok),
                "unidades_validas": sum(unit_ok.values()),
                "politica_productores": {
                    record_type: {"motor": motor, "version": version}
                    for record_type, (motor, version) in sorted(policy.items())
                },
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    if failed:
        for record_id in sorted(reasons):
            print(f"FALLO {record_id}: {','.join(reasons[record_id])}")
    return 0 if failed == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
