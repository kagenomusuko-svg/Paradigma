#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
MOTOR_DIR = ROOT / "motores"
sys.path.insert(0, str(MOTOR_DIR))
from auditor_corpus_fase12 import (
    CLAUSURA_F12,
    EXPECTED_MOTORS,
    sha256_file,
    stable_id,
    stream_f11_product,
    write_json,
)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--fase11-dir", type=Path, required=True)
    p.add_argument("--almacenamiento-fase11", type=Path, required=True)
    p.add_argument("--salida-dir", type=Path, required=True)
    p.add_argument("--cierre", type=Path, required=True)
    p.add_argument("--schema-auditoria", type=Path)
    p.add_argument("--schema-expediente", type=Path)
    args = p.parse_args()

    schema_a_path = args.schema_auditoria or (ROOT / "esquema/auditoria-corpus-fase12-v1.0.0.schema.json")
    schema_e_path = args.schema_expediente or (ROOT / "esquema/expediente-transversal-fase12-v1.0.0.schema.json")
    schema_a = json.loads(schema_a_path.read_text(encoding="utf-8"))
    schema_e = json.loads(schema_e_path.read_text(encoding="utf-8"))

    storage = json.loads(args.almacenamiento_fase11.read_text(encoding="utf-8"))
    closure11 = json.loads((args.fase11_dir / "cierre-fase11.json").read_text(encoding="utf-8"))
    if storage.get("fase") != 11 or storage.get("gate", {}).get("fase11_cerrada") is not True:
        raise SystemExit("Fase 12 no puede cerrar sin Fase 11 persistida y cerrada")
    if closure11.get("fase11_cerrada") is not True or len(closure11.get("maestros", [])) != 20:
        raise SystemExit("Cierre de Fase 11 incompatible")

    audit_path = args.salida_dir / "auditoria-corpus.json"
    dossiers_path = args.salida_dir / "expedientes-transversales.jsonl"
    audit = json.loads(audit_path.read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator(schema_a).validate(audit)
    if audit.get("clausura_descriptiva") != CLAUSURA_F12:
        raise SystemExit("Auditoría F12 no conserva clausura descriptiva")
    expected_audit_id = stable_id("F12AUD", {"cierre_f11": storage["gate"]["cierre_sha256"], "expedientes": audit["expedientes"]["sha256"]})
    if audit.get("id") != expected_audit_id:
        raise SystemExit("ID de auditoría F12 no determinista")
    if audit["origen_fase11"]["cierre_sha256"] != storage["gate"]["cierre_sha256"]:
        raise SystemExit("Auditoría F12 no apunta al cierre F11 persistido")
    if audit["origen_fase11"]["asset_sha256"] != storage["almacenamiento"]["asset_sha256"]:
        raise SystemExit("Auditoría F12 no apunta al asset F11 persistido")
    if sha256_file(dossiers_path) != audit["expedientes"]["sha256"]:
        raise SystemExit("Hash de expedientes F12 divergente")

    closure_by_motor = {row["motor"]: row for row in closure11["motores"]}
    product_sets: dict[str, set[str]] = {m: set() for m in EXPECTED_MOTORS}
    concept_key_to_group: dict[str, str] = {}
    concept_source_to_key: dict[tuple[str, str], str] = {}
    definitions_by_key: dict[str, str] = {}
    assertions_by_key: dict[str, str] = {}
    order_by_key: dict[str, str] = {}
    assertion_to_keys: dict[tuple[str, str], set[str]] = defaultdict(set)
    expected_variants: dict[str, set[str]] = defaultdict(set)
    expected_relations: dict[str, set[str]] = defaultdict(set)
    relation_triplets: dict[str, tuple[str, str, str]] = {}
    expected_negations: dict[str, set[str]] = defaultdict(set)
    expected_exceptions: dict[str, set[str]] = defaultdict(set)

    product_rows = {row["motor"]: row for row in audit["productos_auditados"]}
    if set(product_rows) != set(EXPECTED_MOTORS):
        raise SystemExit("Auditoría F12 no cubre los nueve motores")

    for motor in ("conceptos_corpus", "definiciones_corpus", "afirmaciones_corpus", "orden_recurrencia"):
        source = closure_by_motor[motor]
        path = args.fase11_dir / source["ruta"]
        digest = sha256_file(path)
        if digest != source["sha256"] or digest != product_rows[motor]["sha256"]:
            raise SystemExit(f"Hash de producto F11 divergente en gate F12: {motor}")

        def cb(group: dict, motor=motor) -> None:
            gid = group["id"]
            key = group["clave_recuperacion"]
            product_sets[motor].add(gid)
            if motor == "conceptos_corpus":
                if key in concept_key_to_group:
                    raise SystemExit(f"Clave conceptual F11 duplicada: {key}")
                concept_key_to_group[key] = gid
                for ref in group["registros"]:
                    source_key = (ref["obra_id"], ref["registro_id"])
                    prev = concept_source_to_key.setdefault(source_key, key)
                    if prev != key:
                        raise SystemExit(f"Registro conceptual asociado a dos claves: {source_key}")
            elif motor == "definiciones_corpus":
                definitions_by_key[key] = gid
            elif motor == "afirmaciones_corpus":
                assertions_by_key[key] = gid
                for ref in group["registros"]:
                    assertion_to_keys[(ref["obra_id"], ref["registro_id"])].add(key)
            elif motor == "orden_recurrencia":
                order_by_key[key] = gid
        stream_f11_product(path, cb)

    for motor in ("variantes_terminologicas_corpus", "relaciones_explicitas_corpus", "negaciones_excepciones_corpus"):
        source = closure_by_motor[motor]
        path = args.fase11_dir / source["ruta"]
        digest = sha256_file(path)
        if digest != source["sha256"] or digest != product_rows[motor]["sha256"]:
            raise SystemExit(f"Hash de producto F11 divergente en gate F12: {motor}")

        def cb(group: dict, motor=motor) -> None:
            gid = group["id"]
            key = group["clave_recuperacion"]
            product_sets[motor].add(gid)
            if motor == "variantes_terminologicas_corpus":
                for ref in group["registros"]:
                    base = concept_source_to_key.get((ref["obra_id"], ref["registro_id"]))
                    if base:
                        expected_variants[base].add(gid)
            elif motor == "relaciones_explicitas_corpus":
                triplet = json.loads(key)
                if not isinstance(triplet, list) or len(triplet) != 3:
                    raise SystemExit(f"Tripleta F11 inválida en {gid}")
                skey, rkey, okey = triplet
                relation_triplets[gid] = (skey, rkey, okey)
                if skey in concept_key_to_group:
                    expected_relations[skey].add(gid)
                if okey in concept_key_to_group:
                    expected_relations[okey].add(gid)
            else:
                if key.startswith("negacion::"):
                    literal = key.split("::", 1)[1]
                    if literal in concept_key_to_group:
                        expected_negations[literal].add(gid)
                if key.startswith("excepcion::"):
                    for ref in group["registros"]:
                        limited = ref.get("datos_documentales", {}).get("afirmacion_limitada_id")
                        if not limited:
                            continue
                        for base in assertion_to_keys.get((ref["obra_id"], limited), set()):
                            if base in concept_key_to_group:
                                expected_exceptions[base].add(gid)
        stream_f11_product(path, cb)

    for motor in ("formulas_corpus", "distribucion_por_obra"):
        source = closure_by_motor[motor]
        path = args.fase11_dir / source["ruta"]
        digest = sha256_file(path)
        if digest != source["sha256"] or digest != product_rows[motor]["sha256"]:
            raise SystemExit(f"Hash de producto F11 divergente en gate F12: {motor}")
        stream_f11_product(path, lambda group, motor=motor: product_sets[motor].add(group["id"]))

    seen_keys: set[str] = set()
    seen_base_groups: set[str] = set()
    lines = 0
    validator = jsonschema.Draft202012Validator(schema_e)
    with dossiers_path.open("r", encoding="utf-8") as f:
        for raw in f:
            if not raw.strip():
                continue
            row = json.loads(raw)
            validator.validate(row)
            key = row["clave_recuperacion"]
            if key in seen_keys:
                raise SystemExit(f"Expediente F12 duplicado para clave {key!r}")
            seen_keys.add(key)
            expected_base = concept_key_to_group.get(key)
            if expected_base is None or row["fuentes_fase11"]["conceptos_corpus"] != expected_base:
                raise SystemExit(f"Expediente F12 sin grupo conceptual F11 exacto: {key!r}")
            seen_base_groups.add(expected_base)
            if row["id"] != stable_id("F12X", {"clave": key, "grupo_conceptos": expected_base}):
                raise SystemExit(f"ID F12 no determinista: {key!r}")
            if row["fuentes_fase11"]["definiciones_corpus"] != definitions_by_key.get(key):
                raise SystemExit(f"Fuente de definiciones F12 divergente: {key!r}")
            if row["fuentes_fase11"]["afirmaciones_corpus"] != assertions_by_key.get(key):
                raise SystemExit(f"Fuente de afirmaciones F12 divergente: {key!r}")
            if row["fuentes_fase11"]["orden_recurrencia"] != order_by_key.get(key):
                raise SystemExit(f"Fuente de orden/recurrencia F12 divergente: {key!r}")
            if {x["grupo_id"] for x in row["variaciones_terminologicas"]} != expected_variants.get(key, set()):
                raise SystemExit(f"Variantes F12 incompletas/extras: {key!r}")
            if {x["grupo_id"] for x in row["relaciones_explicitas"]} != expected_relations.get(key, set()):
                raise SystemExit(f"Relaciones F12 incompletas/extras: {key!r}")
            for rel in row["relaciones_explicitas"]:
                skey, rkey, okey = relation_triplets[rel["grupo_id"]]
                roles = set(rel["roles_de_la_clave"])
                expected_roles = ({"sujeto"} if skey == key else set()) | ({"objeto"} if okey == key else set())
                if roles != expected_roles or rel["clave_relacion"] != rkey:
                    raise SystemExit(f"Rol relacional F12 inventado: {key!r}:{rel['grupo_id']}")
            if {x["grupo_id"] for x in row["negaciones_recuperadas_por_forma"]} != expected_negations.get(key, set()):
                raise SystemExit(f"Negaciones F12 incompletas/extras: {key!r}")
            if {x["grupo_id"] for x in row["excepciones_vinculadas_a_predicaciones"]} != expected_exceptions.get(key, set()):
                raise SystemExit(f"Excepciones F12 incompletas/extras: {key!r}")
            if any(row[name] is not False for name in (
                "equivalencia_inferida", "complementariedad_inferida", "contradiccion_inferida",
                "evolucion_doctrinal_inferida", "definicion_preferida"
            )) or row["resolucion_doctrinal"] != "no_realizada":
                raise SystemExit(f"Clausura descriptiva violada en expediente {key!r}")
            lines += 1

    if seen_keys != set(concept_key_to_group) or seen_base_groups != set(concept_key_to_group.values()):
        raise SystemExit("Cobertura F12 no exhaustiva respecto de conceptos_corpus")
    if lines != audit["expedientes"]["registros"] or lines != audit["cobertura"]["expedientes_transversales"]:
        raise SystemExit("Conteo de expedientes F12 divergente")

    with tempfile.TemporaryDirectory(prefix="fase12-repro-") as tmp:
        repro = Path(tmp)
        auditor_path = MOTOR_DIR / "auditor_corpus_fase12.py"
        subprocess.run([
            sys.executable, str(auditor_path),
            "--fase11-dir", str(args.fase11_dir),
            "--almacenamiento", str(args.almacenamiento_fase11),
            "--salida-dir", str(repro),
        ], check=True)
        for name in ("auditoria-corpus.json", "expedientes-transversales.jsonl"):
            if sha256_file(repro / name) != sha256_file(args.salida_dir / name):
                raise SystemExit(f"Fase 12 no es reproducible byte a byte: {name}")

    closure12 = {
        "version": "1.0.0",
        "fase": 12,
        "fase12_cerrada": True,
        "criterio": "expediente_transversal_por_clave_documental_sin_sobrepasar_maestros_de_origen",
        "fuente_exclusiva": "productos_comparativos_fase11_auditados",
        "origen_fase11": audit["origen_fase11"],
        "productos_auditados": 9,
        "maestros_origen": 20,
        "expedientes_transversales": lines,
        "auditoria_sha256": sha256_file(audit_path),
        "expedientes_sha256": sha256_file(dossiers_path),
        "clausura_descriptiva": dict(CLAUSURA_F12),
    }
    digest = write_json(args.cierre, closure12)
    print(json.dumps({
        "fase": 12,
        "fase12_cerrada": True,
        "motores_auditados": 9,
        "maestros_origen": 20,
        "expedientes_transversales": lines,
        "cierre_sha256": digest,
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
