#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
import tempfile
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable

from auditor_corpus_fase12 import canonical_bytes, formal_key, sha256_file, stable_id, stream_f11_product, write_json

VERSION = "1.0.0"
CLAUSURA_F13 = {
    "identidad_interobra_inferida": False,
    "equivalencia_inferida": False,
    "complementariedad_inferida": False,
    "contradiccion_inferida": False,
    "sintesis_doctrinal": False,
    "reconciliacion_interobra": False,
    "evolucion_doctrinal_inferida": False,
    "definicion_preferida": False,
    "formula_concepto_inferida": False,
    "resolucion_doctrinal": "no_realizada",
}
MOTORS = (
    "conceptos_corpus",
    "definiciones_corpus",
    "afirmaciones_corpus",
    "formulas_corpus",
    "relaciones_explicitas_corpus",
    "negaciones_excepciones_corpus",
    "variantes_terminologicas_corpus",
    "distribucion_por_obra",
    "orden_recurrencia",
)


def json_text(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> tuple[str, int]:
    path.parent.mkdir(parents=True, exist_ok=True)
    h = hashlib.sha256()
    count = 0
    with path.open("wb") as f:
        for row in rows:
            raw = canonical_bytes(row)
            f.write(raw)
            h.update(raw)
            count += 1
    digest = h.hexdigest()
    path.with_name(path.name + ".sha256").write_text(f"{digest}  {path.name}\n", encoding="utf-8")
    return digest, count


def compact_master_ref(master: dict[str, Any], row: dict[str, Any], datos: dict[str, Any] | None = None) -> dict[str, Any]:
    return {
        "obra_id": master["obra_id"],
        "titulo_obra": master["titulo"],
        "schema_maestro": master["schema_version"],
        "registro_id": row["id"],
        "tipo_registro_origen": row["tipo_registro"],
        "estado_extraccion": row.get("estado_extraccion"),
        "estado_verificacion": row.get("estado_verificacion"),
        "estado_auditoria": row.get("estado_auditoria"),
        "estatus_enunciativo": row.get("estatus_enunciativo"),
        "fuente_id": row.get("fuente_id"),
        "unidad_id": row.get("unidad_id"),
        "localizacion": row.get("localizacion"),
        "texto_literal": row.get("texto_literal"),
        "normalizacion_formal": row.get("normalizacion_formal"),
        "normalizacion_lexica": row.get("normalizacion_lexica"),
        "datos_documentales": datos or {},
    }


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require_hash(path: Path, expected: str, label: str) -> None:
    actual = sha256_file(path)
    if actual != expected:
        raise SystemExit(f"Hash divergente en {label}: {actual} != {expected}")


def source_contract(
    fase12_dir: Path,
    storage12_path: Path,
    fase11_dir: Path,
    storage11_path: Path,
    manifest10_path: Path,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any]]:
    storage12 = load_json(storage12_path)
    closure12_path = fase12_dir / "cierre-fase12.json"
    closure12 = load_json(closure12_path)
    if storage12.get("fase") != 12 or storage12.get("gate", {}).get("fase12_cerrada") is not True:
        raise SystemExit("Fase 13 requiere Fase 12 persistida y cerrada")
    if closure12.get("fase") != 12 or closure12.get("fase12_cerrada") is not True:
        raise SystemExit("Cierre de Fase 12 ausente o incompatible")
    if hashlib.sha256(closure12_path.read_bytes()).hexdigest() != storage12["gate"]["cierre_sha256"]:
        raise SystemExit("Hash del cierre F12 no coincide con su almacenamiento")
    if storage12.get("clausura_descriptiva") != closure12.get("clausura_descriptiva"):
        raise SystemExit("Clausura F12 divergente entre cierre y almacenamiento")

    products12 = {row["tipo"]: row for row in storage12.get("productos", [])}
    for tipo, name in (("auditoria_corpus", "auditoria-corpus.json"), ("expedientes_transversales", "expedientes-transversales.jsonl")):
        row = products12.get(tipo)
        if not row:
            raise SystemExit(f"Producto F12 no persistido: {tipo}")
        require_hash(fase12_dir / name, row["sha256"], f"F12:{tipo}")

    storage11 = load_json(storage11_path)
    closure11_path = fase11_dir / "cierre-fase11.json"
    closure11 = load_json(closure11_path)
    if storage11.get("fase") != 11 or storage11.get("gate", {}).get("fase11_cerrada") is not True:
        raise SystemExit("Fase 13 requiere Fase 11 persistida y cerrada")
    if closure11.get("fase11_cerrada") is not True:
        raise SystemExit("Cierre de Fase 11 ausente")
    if storage12.get("origen_fase11", {}).get("cierre_sha256") != storage11["gate"]["cierre_sha256"]:
        raise SystemExit("Fase 12 no apunta al cierre F11 suministrado")
    if storage12.get("origen_fase11", {}).get("asset_sha256") != storage11["almacenamiento"]["asset_sha256"]:
        raise SystemExit("Fase 12 no apunta al asset F11 suministrado")
    if hashlib.sha256(closure11_path.read_bytes()).hexdigest() != storage11["gate"]["cierre_sha256"]:
        raise SystemExit("Hash del cierre F11 no coincide con su almacenamiento")

    manifest10 = load_json(manifest10_path)
    if manifest10.get("fase") != 10 or manifest10.get("gate", {}).get("fase10_cerrada") is not True:
        raise SystemExit("Fase 13 requiere manifiesto persistido de Fase 10 cerrada")
    if manifest10.get("gate", {}).get("obras") != 20 or len(manifest10.get("maestros", [])) != 20:
        raise SystemExit("Fase 13 requiere los 20 maestros cerrados de Fase 10")
    f10_by_work = {row["obra_id"]: row for row in manifest10["maestros"]}
    f11_masters = {row["obra_id"]: row for row in closure11.get("maestros", [])}
    if set(f10_by_work) != set(f11_masters):
        raise SystemExit("Conjunto de maestros F10/F11 divergente")
    for obra, row in f10_by_work.items():
        if row["sha256"] != f11_masters[obra]["sha256"]:
            raise SystemExit(f"Hash de maestro F10/F11 divergente: {obra}")

    audit12 = load_json(fase12_dir / "auditoria-corpus.json")
    audited = {row["motor"]: row for row in audit12.get("productos_auditados", [])}
    stored11 = {row["motor"]: row for row in storage11.get("productos", [])}
    if set(audited) != set(MOTORS) or set(stored11) != set(MOTORS):
        raise SystemExit("Fase 13 requiere los nueve productos F11 auditados por F12")
    for motor in MOTORS:
        if audited[motor]["sha256"] != stored11[motor]["sha256"]:
            raise SystemExit(f"F12 y almacenamiento F11 divergen para {motor}")
        rel = stored11[motor]["ruta_en_zip"].split("/", 1)[1]
        require_hash(fase11_dir / rel, stored11[motor]["sha256"], f"F11:{motor}")

    return storage12, closure12, storage11, closure11, manifest10, audit12


def init_db(path: Path) -> sqlite3.Connection:
    db = sqlite3.connect(path)
    db.executescript(
        """
        PRAGMA journal_mode=OFF;
        PRAGMA synchronous=OFF;
        CREATE TABLE groups (motor TEXT NOT NULL, key TEXT NOT NULL, gid TEXT NOT NULL, payload TEXT NOT NULL, PRIMARY KEY (motor,key));
        CREATE UNIQUE INDEX groups_gid ON groups(gid);
        CREATE TABLE concept_source (obra TEXT NOT NULL, rid TEXT NOT NULL, key TEXT NOT NULL, PRIMARY KEY (obra,rid));
        CREATE TABLE assertion_source (obra TEXT NOT NULL, rid TEXT NOT NULL, key TEXT NOT NULL, PRIMARY KEY (obra,rid,key));
        CREATE TABLE links (kind TEXT NOT NULL, base_key TEXT NOT NULL, gid TEXT NOT NULL, PRIMARY KEY (kind,base_key,gid));
        CREATE TABLE formula_source (obra TEXT NOT NULL, rid TEXT NOT NULL, gid TEXT NOT NULL, PRIMARY KEY (obra,rid));
        CREATE TABLE formula_links (base_key TEXT NOT NULL, obra TEXT NOT NULL, rid TEXT NOT NULL, gid TEXT NOT NULL, payload TEXT NOT NULL, PRIMARY KEY (base_key,obra,rid));
        CREATE TABLE restrictions (obra TEXT NOT NULL, rid TEXT NOT NULL, payload TEXT NOT NULL, linked_keys TEXT NOT NULL, PRIMARY KEY (obra,rid));
        CREATE INDEX restrictions_key_dummy ON restrictions(obra);
        CREATE TABLE restriction_links (base_key TEXT NOT NULL, obra TEXT NOT NULL, rid TEXT NOT NULL, PRIMARY KEY (base_key,obra,rid));
        """
    )
    return db


def group_path(storage11: dict[str, Any], fase11_dir: Path, motor: str) -> Path:
    row = next(x for x in storage11["productos"] if x["motor"] == motor)
    return fase11_dir / row["ruta_en_zip"].split("/", 1)[1]


def index_f11(db: sqlite3.Connection, fase11_dir: Path, storage11: dict[str, Any]) -> set[str]:
    concept_keys: set[str] = set()

    def ingest_simple(motor: str) -> None:
        def cb(group: dict[str, Any]) -> None:
            key = group["clave_recuperacion"]
            db.execute("INSERT INTO groups(motor,key,gid,payload) VALUES(?,?,?,?)", (motor, key, group["id"], json_text(group)))
            if motor == "conceptos_corpus":
                concept_keys.add(key)
                for ref in group["registros"]:
                    db.execute("INSERT INTO concept_source(obra,rid,key) VALUES(?,?,?)", (ref["obra_id"], ref["registro_id"], key))
            elif motor == "afirmaciones_corpus":
                for ref in group["registros"]:
                    db.execute("INSERT OR IGNORE INTO assertion_source(obra,rid,key) VALUES(?,?,?)", (ref["obra_id"], ref["registro_id"], key))
            elif motor == "formulas_corpus":
                for ref in group["registros"]:
                    db.execute("INSERT INTO formula_source(obra,rid,gid) VALUES(?,?,?)", (ref["obra_id"], ref["registro_id"], group["id"]))
        stream_f11_product(group_path(storage11, fase11_dir, motor), cb)
        db.commit()

    for motor in ("conceptos_corpus", "definiciones_corpus", "afirmaciones_corpus", "orden_recurrencia", "formulas_corpus", "distribucion_por_obra"):
        ingest_simple(motor)

    def variants_cb(group: dict[str, Any]) -> None:
        key = group["clave_recuperacion"]
        db.execute("INSERT INTO groups(motor,key,gid,payload) VALUES(?,?,?,?)", ("variantes_terminologicas_corpus", key, group["id"], json_text(group)))
        bases: set[str] = set()
        for ref in group["registros"]:
            row = db.execute("SELECT key FROM concept_source WHERE obra=? AND rid=?", (ref["obra_id"], ref["registro_id"])).fetchone()
            if row:
                bases.add(row[0])
        for base in bases:
            db.execute("INSERT INTO links(kind,base_key,gid) VALUES(?,?,?)", ("variante", base, group["id"]))
    stream_f11_product(group_path(storage11, fase11_dir, "variantes_terminologicas_corpus"), variants_cb)
    db.commit()

    def relations_cb(group: dict[str, Any]) -> None:
        key = group["clave_recuperacion"]
        db.execute("INSERT INTO groups(motor,key,gid,payload) VALUES(?,?,?,?)", ("relaciones_explicitas_corpus", key, group["id"], json_text(group)))
        triplet = json.loads(key)
        if not isinstance(triplet, list) or len(triplet) != 3 or not all(isinstance(x, str) for x in triplet):
            raise SystemExit(f"Tripleta relacional F11 inválida: {group['id']}")
        for base in {triplet[0], triplet[2]} & concept_keys:
            db.execute("INSERT INTO links(kind,base_key,gid) VALUES(?,?,?)", ("relacion", base, group["id"]))
    stream_f11_product(group_path(storage11, fase11_dir, "relaciones_explicitas_corpus"), relations_cb)
    db.commit()

    def negexc_cb(group: dict[str, Any]) -> None:
        key = group["clave_recuperacion"]
        db.execute("INSERT INTO groups(motor,key,gid,payload) VALUES(?,?,?,?)", ("negaciones_excepciones_corpus", key, group["id"], json_text(group)))
        if key.startswith("negacion::"):
            base = key.split("::", 1)[1]
            if base in concept_keys:
                db.execute("INSERT INTO links(kind,base_key,gid) VALUES(?,?,?)", ("negacion", base, group["id"]))
        elif key.startswith("excepcion::"):
            bases: set[str] = set()
            for ref in group["registros"]:
                limited = ref.get("datos_documentales", {}).get("afirmacion_limitada_id")
                if not limited:
                    continue
                for row in db.execute("SELECT key FROM assertion_source WHERE obra=? AND rid=?", (ref["obra_id"], limited)):
                    if row[0] in concept_keys:
                        bases.add(row[0])
            for base in bases:
                db.execute("INSERT INTO links(kind,base_key,gid) VALUES(?,?,?)", ("excepcion", base, group["id"]))
    stream_f11_product(group_path(storage11, fase11_dir, "negaciones_excepciones_corpus"), negexc_cb)
    db.commit()
    return concept_keys


def get_group(db: sqlite3.Connection, motor: str, key: str) -> dict[str, Any] | None:
    row = db.execute("SELECT payload FROM groups WHERE motor=? AND key=?", (motor, key)).fetchone()
    return json.loads(row[0]) if row else None


def linked_groups(db: sqlite3.Connection, kind: str, base_key: str) -> list[dict[str, Any]]:
    rows = db.execute(
        "SELECT g.payload FROM links l JOIN groups g ON g.gid=l.gid WHERE l.kind=? AND l.base_key=? ORDER BY l.gid",
        (kind, base_key),
    ).fetchall()
    return [json.loads(row[0]) for row in rows]


def build_master_extras(
    db: sqlite3.Connection,
    manifest10: dict[str, Any],
    masters_dir: Path,
) -> tuple[dict[str, dict[str, Any]], int, int]:
    master_ptrs: dict[str, dict[str, Any]] = {}
    formulas_linked = 0
    restrictions_total = 0
    for expected in manifest10["maestros"]:
        obra = expected["obra_id"]
        path = masters_dir / Path(expected["ruta_en_zip"]).name
        require_hash(path, expected["sha256"], f"maestro F10:{obra}")
        master = load_json(path)
        if master.get("obra_id") != obra or master.get("tipo_registro") != "expediente_maestro_obra":
            raise SystemExit(f"Maestro F10 incompatible: {obra}")
        if master.get("estado_verificacion") != "verificado":
            raise SystemExit(f"Maestro F10 no verificado: {obra}")
        master_ptrs[obra] = {
            "obra_id": obra,
            "titulo": master["titulo"],
            "schema_version": master["schema_version"],
            "ruta_en_asset_fase10": expected["ruta_en_zip"],
            "sha256": expected["sha256"],
        }

        concept_by_id = {rid: key for rid, key in db.execute("SELECT rid,key FROM concept_source WHERE obra=?", (obra,))}
        unit_to_keys: dict[str, set[str]] = defaultdict(set)
        for appearance in master.get("apariciones_conceptuales", []):
            key = concept_by_id.get(appearance.get("concepto_id"))
            unit = appearance.get("unidad_id")
            if key and unit:
                unit_to_keys[unit].add(key)

        for formula in master.get("formulas", []):
            if formula.get("estado_verificacion") != "verificado" or formula.get("estado_auditoria") != "auditado":
                continue
            units = set(formula.get("contexto_unidad_ids", []) or [])
            if formula.get("unidad_id"):
                units.add(formula["unidad_id"])
            keys = sorted({key for unit in units for key in unit_to_keys.get(unit, set())})
            source = db.execute("SELECT gid FROM formula_source WHERE obra=? AND rid=?", (obra, formula["id"])).fetchone()
            if not source:
                raise SystemExit(f"Fórmula auditada sin grupo F11: {obra}:{formula['id']}")
            ref = compact_master_ref(
                master,
                formula,
                {
                    "formula_literal": formula.get("formula_literal"),
                    "simbolos_literales": formula.get("simbolos_literales", []),
                    "contexto_unidad_ids": formula.get("contexto_unidad_ids", []),
                    "clasificacion_formula": formula.get("clasificacion_formula"),
                },
            )
            for base in keys:
                payload = {
                    "grupo_fase11_id": source[0],
                    "criterio_vinculo": "coocurrencia_en_unidad_documentada_solo_para_recuperacion",
                    "estado_vinculo_conceptual": "no_determinado",
                    "referencia": ref,
                }
                db.execute(
                    "INSERT INTO formula_links(base_key,obra,rid,gid,payload) VALUES(?,?,?,?,?)",
                    (base, obra, formula["id"], source[0], json_text(payload)),
                )
                formulas_linked += 1

        assertion_keys: dict[str, list[str]] = defaultdict(list)
        for rid, key in db.execute("SELECT rid,key FROM assertion_source WHERE obra=? ORDER BY rid,key", (obra,)):
            assertion_keys[rid].append(key)
        for restriction in master.get("restricciones_alcance", []):
            if restriction.get("estado_verificacion") != "verificado" or restriction.get("estado_auditoria") != "auditado":
                continue
            limited = restriction.get("afirmacion_limitada_id")
            keys = sorted(set(assertion_keys.get(limited, []))) if limited else []
            ref = compact_master_ref(
                master,
                restriction,
                {
                    "afirmacion_limitada_id": limited,
                    "tipo_restriccion": restriction.get("tipo_restriccion"),
                    "fragmento_restriccion_literal": restriction.get("fragmento_restriccion_literal"),
                    "clasificacion_restriccion": restriction.get("clasificacion_restriccion"),
                },
            )
            payload = {
                "id": stable_id("F13R", {"obra": obra, "registro": restriction["id"]}),
                "tipo_registro": "restriccion_corpus_auditada",
                "schema_version": VERSION,
                "criterio_vinculo": "afirmacion_limitada_id_documentado" if keys else "sin_vinculo_conceptual_documentado",
                "claves_conceptuales_vinculadas": keys,
                "referencia": ref,
            }
            db.execute(
                "INSERT INTO restrictions(obra,rid,payload,linked_keys) VALUES(?,?,?,?)",
                (obra, restriction["id"], json_text(payload), json_text(keys)),
            )
            for base in keys:
                db.execute("INSERT INTO restriction_links(base_key,obra,rid) VALUES(?,?,?)", (base, obra, restriction["id"]))
            restrictions_total += 1
        db.commit()
    return master_ptrs, formulas_linked, restrictions_total


def refs(group: dict[str, Any] | None) -> list[dict[str, Any]]:
    return list(group.get("registros", [])) if group else []


def grouped_refs(groups: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        {
            "grupo_id": g["id"],
            "clave_recuperacion": g["clave_recuperacion"],
            "criterio_agrupacion": g["criterio_agrupacion"],
            "estado_identidad_interobra": g["estado_identidad_interobra"],
            "registros": g["registros"],
        }
        for g in groups
    ]


def formula_rows(db: sqlite3.Connection, base_key: str) -> list[dict[str, Any]]:
    return [json.loads(row[0]) for row in db.execute("SELECT payload FROM formula_links WHERE base_key=? ORDER BY obra,rid", (base_key,))]


def restriction_rows(db: sqlite3.Connection, base_key: str) -> list[dict[str, Any]]:
    return [
        json.loads(row[0])
        for row in db.execute(
            "SELECT r.payload FROM restriction_links l JOIN restrictions r ON r.obra=l.obra AND r.rid=l.rid WHERE l.base_key=? ORDER BY l.obra,l.rid",
            (base_key,),
        )
    ]


def concept_record(
    db: sqlite3.Connection,
    dossier: dict[str, Any],
    master_ptrs: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    key = dossier["clave_recuperacion"]
    concepts = get_group(db, "conceptos_corpus", key)
    if concepts is None or concepts["id"] != dossier["fuentes_fase11"]["conceptos_corpus"]:
        raise SystemExit(f"Expediente F12 sin grupo conceptual F11 exacto: {key!r}")
    definitions = get_group(db, "definiciones_corpus", key)
    assertions = get_group(db, "afirmaciones_corpus", key)
    order = get_group(db, "orden_recurrencia", key)
    if (definitions["id"] if definitions else None) != dossier["fuentes_fase11"]["definiciones_corpus"]:
        raise SystemExit(f"Fuente de definiciones divergente en F13: {key!r}")
    if (assertions["id"] if assertions else None) != dossier["fuentes_fase11"]["afirmaciones_corpus"]:
        raise SystemExit(f"Fuente de afirmaciones divergente en F13: {key!r}")
    if (order["id"] if order else None) != dossier["fuentes_fase11"]["orden_recurrencia"]:
        raise SystemExit(f"Fuente de recurrencia divergente en F13: {key!r}")

    variants = linked_groups(db, "variante", key)
    relations = linked_groups(db, "relacion", key)
    negations = linked_groups(db, "negacion", key)
    exceptions = linked_groups(db, "excepcion", key)
    if {g["id"] for g in variants} != {x["grupo_id"] for x in dossier["variaciones_terminologicas"]}:
        raise SystemExit(f"Variantes F12/F13 divergentes: {key!r}")
    if {g["id"] for g in relations} != {x["grupo_id"] for x in dossier["relaciones_explicitas"]}:
        raise SystemExit(f"Relaciones F12/F13 divergentes: {key!r}")
    if {g["id"] for g in negations} != {x["grupo_id"] for x in dossier["negaciones_recuperadas_por_forma"]}:
        raise SystemExit(f"Negaciones F12/F13 divergentes: {key!r}")
    if {g["id"] for g in exceptions} != {x["grupo_id"] for x in dossier["excepciones_vinculadas_a_predicaciones"]}:
        raise SystemExit(f"Excepciones F12/F13 divergentes: {key!r}")

    works = []
    for summary in dossier["obras"]:
        obra = summary["obra_id"]
        if obra not in master_ptrs:
            raise SystemExit(f"Obra F12 sin maestro F10 persistido: {obra}")
        works.append({"obra_id": obra, "maestro_obra": master_ptrs[obra], "resumen_auditoria_fase12": summary})

    definitions_refs = refs(definitions)
    explicit_definitions = [r for r in definitions_refs if r.get("datos_documentales", {}).get("clasificacion_definicion") == "definicion_explicita"]
    assertions_refs = refs(assertions)
    return {
        "id": stable_id("F13C", {"expediente_fase12": dossier["id"], "clave": key}),
        "tipo_registro": "concepto_maestro_corpus",
        "schema_version": VERSION,
        "clave_recuperacion": key,
        "criterio_clave": dossier["criterio_clave"],
        "estado_identidad_interobra": "no_determinada",
        "expediente_fase12_id": dossier["id"],
        "fuentes_fase11": dossier["fuentes_fase11"],
        "multiplicidad": dossier["multiplicidad"],
        "obras": works,
        "formas_literales": dossier["formas_literales_observadas"],
        "variantes_recuperacion": grouped_refs(variants),
        "definiciones": definitions_refs,
        "definiciones_explicitas": explicit_definitions,
        "predicaciones": assertions_refs,
        "relaciones_explicitas": grouped_refs(relations),
        "formulas": formula_rows(db, key),
        "criterio_formulas": "coocurrencia_en_unidad_documentada_solo_para_recuperacion_no_identidad_conceptual",
        "negaciones": grouped_refs(negations),
        "excepciones": grouped_refs(exceptions),
        "restricciones": restriction_rows(db, key),
        "hallazgos_auditoria": dossier["hallazgos"],
        "trazabilidad": {
            "grupo_conceptos_fase11": concepts["id"],
            "grupo_orden_recurrencia_fase11": order["id"] if order else None,
            "registros_conceptuales": refs(concepts),
        },
        "equivalencia_inferida": False,
        "complementariedad_inferida": False,
        "contradiccion_inferida": False,
        "evolucion_doctrinal_inferida": False,
        "definicion_preferida": False,
        "formula_concepto_inferida": False,
        "resolucion_doctrinal": "no_realizada",
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--fase12-dir", type=Path, required=True)
    p.add_argument("--almacenamiento-fase12", type=Path, required=True)
    p.add_argument("--fase11-dir", type=Path, required=True)
    p.add_argument("--almacenamiento-fase11", type=Path, required=True)
    p.add_argument("--manifest-fase10", type=Path, required=True)
    p.add_argument("--maestros-dir", type=Path, required=True)
    p.add_argument("--salida-dir", type=Path, required=True)
    args = p.parse_args()

    storage12, closure12, storage11, closure11, manifest10, audit12 = source_contract(
        args.fase12_dir, args.almacenamiento_fase12, args.fase11_dir, args.almacenamiento_fase11, args.manifest_fase10
    )
    args.salida_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="fase13-index-") as tmp:
        db = init_db(Path(tmp) / "index.sqlite")
        concept_keys = index_f11(db, args.fase11_dir, storage11)
        master_ptrs, formula_links_count, restrictions_count = build_master_extras(db, manifest10, args.maestros_dir)

        concept_path = args.salida_dir / "conceptos-maestro-corpus.jsonl"
        seen: set[str] = set()
        def concept_rows() -> Iterable[dict[str, Any]]:
            with (args.fase12_dir / "expedientes-transversales.jsonl").open("r", encoding="utf-8") as f:
                for raw in f:
                    if not raw.strip():
                        continue
                    dossier = json.loads(raw)
                    key = dossier["clave_recuperacion"]
                    if key in seen:
                        raise SystemExit(f"Expediente F12 duplicado: {key!r}")
                    seen.add(key)
                    yield concept_record(db, dossier, master_ptrs)
        concepts_sha, concepts_count = write_jsonl(concept_path, concept_rows())
        if seen != concept_keys or concepts_count != closure12["expedientes_transversales"]:
            raise SystemExit("Cobertura conceptual F13 no exhaustiva respecto de F12/F11")

        formulas_path = args.salida_dir / "formulas-corpus.jsonl"
        def formula_groups() -> Iterable[dict[str, Any]]:
            for key, payload in db.execute("SELECT key,payload FROM groups WHERE motor='formulas_corpus' ORDER BY key"):
                group = json.loads(payload)
                yield {
                    "id": stable_id("F13F", {"grupo_fase11": group["id"]}),
                    "tipo_registro": "formula_corpus_auditada",
                    "schema_version": VERSION,
                    "grupo_fase11_id": group["id"],
                    "clave_recuperacion": key,
                    "criterio_agrupacion": group["criterio_agrupacion"],
                    "registros": group["registros"],
                    "estado_vinculo_conceptual": "no_determinado",
                    "resolucion_doctrinal": "no_realizada",
                }
        formulas_sha, formulas_count = write_jsonl(formulas_path, formula_groups())

        restrictions_path = args.salida_dir / "restricciones-corpus.jsonl"
        def restrictions_rows_all() -> Iterable[dict[str, Any]]:
            for (payload,) in db.execute("SELECT payload FROM restrictions ORDER BY obra,rid"):
                yield json.loads(payload)
        restrictions_sha, restrictions_written = write_jsonl(restrictions_path, restrictions_rows_all())
        if restrictions_written != restrictions_count:
            raise SystemExit("Conteo de restricciones F13 divergente")

    origin12 = {
        "cierre_sha256": storage12["gate"]["cierre_sha256"],
        "release_tag": storage12["almacenamiento"]["release_tag"],
        "asset": storage12["almacenamiento"]["asset"],
        "asset_sha256": storage12["almacenamiento"]["asset_sha256"],
        "expedientes_transversales": closure12["expedientes_transversales"],
    }
    origin11 = {
        "cierre_sha256": storage11["gate"]["cierre_sha256"],
        "release_tag": storage11["almacenamiento"]["release_tag"],
        "asset": storage11["almacenamiento"]["asset"],
        "asset_sha256": storage11["almacenamiento"]["asset_sha256"],
        "motores": 9,
    }
    origin10 = {
        "reporte_sha256": manifest10["gate"]["reporte_sha256"],
        "release_tag": manifest10["almacenamiento"]["release_tag"],
        "asset": manifest10["almacenamiento"]["asset"],
        "asset_sha256": manifest10["almacenamiento"]["asset_sha256"],
        "maestros": 20,
    }
    products = {
        "conceptos": {"ruta": concept_path.name, "sha256": concepts_sha, "registros": concepts_count},
        "formulas": {"ruta": formulas_path.name, "sha256": formulas_sha, "registros": formulas_count, "vinculos_recuperacion_conceptual": formula_links_count},
        "restricciones": {"ruta": restrictions_path.name, "sha256": restrictions_sha, "registros": restrictions_written},
    }
    master = {
        "id": stable_id("F13M", {"cierre_f12": origin12["cierre_sha256"], "productos": products}),
        "tipo_registro": "expediente_maestro_corpus",
        "schema_version": VERSION,
        "fase": 13,
        "fuente_exclusiva": "expedientes_fase12_y_registros_auditados_de_origen",
        "origen_fase12": origin12,
        "origen_fase11": origin11,
        "origen_fase10": origin10,
        "obras": [master_ptrs[k] for k in sorted(master_ptrs)],
        "productos": products,
        "criterios_vinculo": {
            "conceptos": "clave_documental_fase11_auditada_por_fase12",
            "formulas": "coocurrencia_en_unidad_documentada_solo_para_recuperacion",
            "restricciones": "afirmacion_limitada_id_documentado",
        },
        "clausura_descriptiva": dict(CLAUSURA_F13),
        "estado_auditoria": "auditado",
    }
    master_sha = write_json(args.salida_dir / "maestro-corpus.json", master)
    print(json.dumps({
        "fase": 13,
        "conceptos": concepts_count,
        "formulas": formulas_count,
        "restricciones": restrictions_written,
        "vinculos_formula_recuperacion": formula_links_count,
        "maestro_sha256": master_sha,
    }, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
