#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path
from typing import Any

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
MOTOR_DIR = ROOT / "motores"
SCHEMA_DIR = ROOT / "esquema"
sys.path.insert(0, str(MOTOR_DIR))

from consulta_literal_fase14 import (
    CLAUSURA_F14,
    NEGATIVE_EVIDENCE,
    NOT_DETERMINED,
    QUERY_TYPES,
    canonical_bytes,
    execute_queries,
    formal_key,
    sha256_file,
    source_contract,
    write_jsonl,
)

SENTINEL = "__fase14_sin_hallazgo_2f0cbd5d__"


def write_json(path: Path, value: dict[str, Any]) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(value, f, ensure_ascii=False, sort_keys=True, indent=2)
        f.write("\n")
    digest = sha256_file(path)
    path.with_name(path.name + ".sha256").write_text(f"{digest}  {path.name}\n", encoding="utf-8")
    return digest


def first_ref(groups: list[dict[str, Any]]) -> tuple[dict[str, Any], dict[str, Any]] | None:
    for group in groups:
        refs = group.get("registros", [])
        if refs:
            return group, refs[0]
    return None


def discover_fixtures(fase13_dir: Path) -> dict[str, dict[str, Any]]:
    fixtures: dict[str, dict[str, Any]] = {}
    with (fase13_dir / "conceptos-maestro-corpus.jsonl").open("r", encoding="utf-8") as f:
        for raw in f:
            if not raw.strip():
                continue
            row = json.loads(raw)
            key = row["clave_recuperacion"]
            if "definiciones_explicitas" not in fixtures and row.get("definiciones_explicitas"):
                ref = row["definiciones_explicitas"][0]
                fixtures["definiciones_explicitas"] = {"query": {"tipo": "definiciones_explicitas", "termino": key}, "registro_id": ref["registro_id"]}
            if "predicaciones" not in fixtures and row.get("predicaciones"):
                ref = row["predicaciones"][0]
                fixtures["predicaciones"] = {"query": {"tipo": "predicaciones", "termino": key}, "registro_id": ref["registro_id"]}
            if "apariciones" not in fixtures and row.get("trazabilidad", {}).get("registros_conceptuales"):
                ref = row["trazabilidad"]["registros_conceptuales"][0]
                fixtures["apariciones"] = {"query": {"tipo": "apariciones", "termino": key}, "registro_id": ref["registro_id"]}
            for qtype, field in (
                ("negaciones", "negaciones"),
                ("variantes_terminologicas", "variantes_recuperacion"),
                ("excepciones", "excepciones"),
            ):
                if qtype not in fixtures:
                    found = first_ref(row.get(field, []))
                    if found:
                        group, ref = found
                        fixtures[qtype] = {
                            "query": {"tipo": qtype, "termino": key},
                            "registro_id": ref["registro_id"],
                            "grupo_id": group.get("grupo_id"),
                        }
            if "relacion_explicita" not in fixtures:
                found = first_ref(row.get("relaciones_explicitas", []))
                if found:
                    group, ref = found
                    try:
                        triplet = json.loads(group["clave_recuperacion"])
                    except (KeyError, json.JSONDecodeError):
                        triplet = None
                    if isinstance(triplet, list) and len(triplet) == 3 and all(isinstance(x, str) and formal_key(x) for x in triplet):
                        fixtures["relacion_explicita"] = {
                            "query": {"tipo": "relacion_explicita", "termino": triplet[0], "relacion": triplet[1], "objeto": triplet[2]},
                            "registro_id": ref["registro_id"],
                            "grupo_id": group.get("grupo_id"),
                        }
            if len(fixtures) >= 7:
                break

    with (fase13_dir / "formulas-corpus.jsonl").open("r", encoding="utf-8") as f:
        for raw in f:
            if not raw.strip():
                continue
            group = json.loads(raw)
            for ref in group.get("registros", []):
                literal = ref.get("datos_documentales", {}).get("formula_literal")
                if isinstance(literal, str) and formal_key(literal):
                    fixtures["formulas_contienen"] = {
                        "query": {"tipo": "formulas_contienen", "termino": formal_key(literal)},
                        "registro_id": ref["registro_id"],
                        "grupo_fase11_id": group.get("grupo_fase11_id"),
                    }
                    return fixtures
    return fixtures


def default_negative_query(qtype: str) -> dict[str, Any]:
    if qtype == "relacion_explicita":
        return {"tipo": qtype, "termino": SENTINEL + "-s", "relacion": "=", "objeto": SENTINEL + "-o"}
    return {"tipo": qtype, "termino": SENTINEL}


def reference_ids(response: dict[str, Any]) -> set[str]:
    return {row["referencia"]["registro_id"] for row in response["resultados"]}


def validate_responses(
    responses: list[dict[str, Any]],
    fixtures_by_index: list[dict[str, Any] | None],
    validator: jsonschema.Draft202012Validator,
) -> tuple[int, Counter[str]]:
    refs = 0
    states: Counter[str] = Counter()
    for i, response in enumerate(responses):
        validator.validate(response)
        if response["conteo_resultados"] != len(response["resultados"]):
            raise SystemExit("Conteo de resultados F14 divergente")
        if response["clausura_descriptiva"] != CLAUSURA_F14:
            raise SystemExit("Respuesta F14 no conserva clausura descriptiva")
        states[response["estado"]] += 1
        fixture = fixtures_by_index[i]
        qtype = response["consulta"]["tipo"]
        if fixture:
            if response["estado"] != "hallazgo_auditado":
                raise SystemExit(f"Consulta real F14 no recuperó su evidencia documentada: {qtype}")
            if fixture["registro_id"] not in reference_ids(response):
                raise SystemExit(f"Consulta real F14 perdió referencia esperada: {qtype}:{fixture['registro_id']}")
        elif qtype == "relacion_explicita":
            if response["estado"] != "no_determinado_por_el_corpus" or response["mensaje"] != NOT_DETERMINED:
                raise SystemExit("Negativa relacional F14 no usa NO DETERMINADO POR EL CORPUS")
        else:
            if response["estado"] != "sin_hallazgo_auditado" or response["mensaje"] != NEGATIVE_EVIDENCE:
                raise SystemExit("Negativa documental F14 no distingue ausencia de hallazgo auditado")

        for result in response["resultados"]:
            ref = result["referencia"]
            if ref.get("estado_verificacion") != "verificado" or ref.get("estado_auditoria") != "auditado":
                raise SystemExit("Respuesta F14 contiene referencia no auditada/verificada")
            refs += 1
            if result["tipo_hallazgo"] == "formula_literal":
                if result.get("estado_vinculo_conceptual") != "no_determinado" or result.get("resolucion_doctrinal") != "no_realizada":
                    raise SystemExit("F14 convirtió recuperación literal de fórmula en vínculo conceptual")
    return refs, states


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--fase13-dir", type=Path, required=True)
    p.add_argument("--almacenamiento-fase13", type=Path, required=True)
    p.add_argument("--salida-dir", type=Path, required=True)
    p.add_argument("--cierre", type=Path, required=True)
    p.add_argument("--schema-respuesta", type=Path)
    args = p.parse_args()

    storage13, _, master13 = source_contract(args.fase13_dir, args.almacenamiento_fase13)
    schema_path = args.schema_respuesta or SCHEMA_DIR / "respuesta-consulta-literal-fase14-v1.0.0.schema.json"
    validator = jsonschema.Draft202012Validator(json.loads(schema_path.read_text(encoding="utf-8")))

    fixtures = discover_fixtures(args.fase13_dir)
    queries: list[dict[str, Any]] = []
    fixtures_by_index: list[dict[str, Any] | None] = []
    for qtype in sorted(QUERY_TYPES):
        fixture = fixtures.get(qtype)
        queries.append(fixture["query"] if fixture else default_negative_query(qtype))
        fixtures_by_index.append(fixture)

    queries.append({"tipo": "definiciones_explicitas", "termino": SENTINEL + "-evidencia"})
    fixtures_by_index.append(None)
    queries.append({"tipo": "relacion_explicita", "termino": SENTINEL + "-x", "relacion": "=", "objeto": SENTINEL + "-y"})
    fixtures_by_index.append(None)

    responses = execute_queries(args.fase13_dir, args.almacenamiento_fase13, queries)
    refs_count, states = validate_responses(responses, fixtures_by_index, validator)

    args.salida_dir.mkdir(parents=True, exist_ok=True)
    responses_path = args.salida_dir / "muestra-respuestas-fase14.jsonl"
    responses_sha = write_jsonl(responses_path, responses)

    with tempfile.TemporaryDirectory(prefix="fase14-repro-") as tmp:
        tmpdir = Path(tmp)
        batch = tmpdir / "consultas.jsonl"
        with batch.open("wb") as f:
            for q in queries:
                f.write(canonical_bytes(q))
        repro = tmpdir / "respuestas.jsonl"
        subprocess.run([
            sys.executable,
            str(MOTOR_DIR / "consulta_literal_fase14.py"),
            "--fase13-dir", str(args.fase13_dir),
            "--almacenamiento-fase13", str(args.almacenamiento_fase13),
            "--lote", str(batch),
            "--salida", str(repro),
        ], check=True)
        if repro.read_bytes() != responses_path.read_bytes():
            raise SystemExit("Fase 14 no es reproducible byte a byte por su interfaz CLI")

    audit = {
        "version": "1.0.0",
        "fase": 14,
        "tipo_registro": "auditoria_consulta_literal",
        "fuente_exclusiva": "json_maestro_corpus_fase13_cerrado",
        "origen_fase13": {
            "cierre_sha256": storage13["gate"]["cierre_sha256"],
            "release_tag": storage13.get("almacenamiento", {}).get("release_tag"),
            "asset": storage13.get("almacenamiento", {}).get("asset"),
            "asset_sha256": storage13.get("almacenamiento", {}).get("asset_sha256"),
            "maestro_id": master13["id"],
        },
        "consultas_ejecutadas": len(queries),
        "tipos_consulta_ejercitados": sorted({q["tipo"] for q in queries}),
        "tipos_con_hallazgo_real": sorted(fixtures),
        "tipos_sin_hallazgo_real_disponible": sorted(set(QUERY_TYPES) - set(fixtures)),
        "estados_respuesta": dict(sorted(states.items())),
        "referencias_auditadas_verificadas_emitidas": refs_count,
        "respuestas_sha256": responses_sha,
        "reproducible_byte_a_byte": True,
        "negativas_diferenciadas": True,
        "clausura_descriptiva": dict(CLAUSURA_F14),
    }
    audit_path = args.salida_dir / "auditoria-consulta-fase14.json"
    audit_sha = write_json(audit_path, audit)

    closure14 = {
        "version": "1.0.0",
        "fase": 14,
        "fase14_cerrada": True,
        "criterio": "respuestas_mediante_registros_auditados_y_referencias_sin_generar_doctrina_nueva",
        "fuente_exclusiva": "json_maestro_corpus_fase13_cerrado",
        "origen_fase13": audit["origen_fase13"],
        "consultas_ejecutadas": len(queries),
        "tipos_consulta_ejercitados": audit["tipos_consulta_ejercitados"],
        "referencias_auditadas_verificadas_emitidas": refs_count,
        "estados_respuesta": audit["estados_respuesta"],
        "respuestas_sha256": responses_sha,
        "auditoria_sha256": audit_sha,
        "reproducible_byte_a_byte": True,
        "clausura_descriptiva": dict(CLAUSURA_F14),
    }
    closure_sha = write_json(args.cierre, closure14)
    print(json.dumps({
        "fase": 14,
        "fase14_cerrada": True,
        "consultas": len(queries),
        "referencias": refs_count,
        "respuestas_sha256": responses_sha,
        "cierre_sha256": closure_sha,
    }, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
