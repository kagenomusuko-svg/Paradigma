#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
MOTOR_DIR = ROOT / "motores"
sys.path.insert(0, str(MOTOR_DIR))
from ensamblador_maestro_corpus_fase13 import (
    CLAUSURA_F13,
    source_contract,
    sha256_file,
    stable_id,
    write_json,
)


def valid_ref(ref: dict, masters: dict[str, dict], *, require_location: bool = False) -> None:
    obra = ref.get("obra_id")
    if obra not in masters:
        raise SystemExit(f"Referencia F13 sin maestro de obra: {obra}")
    if ref.get("estado_verificacion") != "verificado" or ref.get("estado_auditoria") != "auditado":
        raise SystemExit(f"Referencia F13 no verificada/auditada: {obra}:{ref.get('registro_id')}")
    if require_location:
        if not ref.get("fuente_id") or not ref.get("unidad_id") or not isinstance(ref.get("localizacion"), dict):
            raise SystemExit(f"Cadena documental incompleta: {obra}:{ref.get('registro_id')}")
        if not isinstance(ref.get("texto_literal"), str) or not ref["texto_literal"]:
            raise SystemExit(f"Texto literal ausente en referencia trazable: {obra}:{ref.get('registro_id')}")


def iter_group_refs(groups: list[dict]):
    for group in groups:
        for ref in group["registros"]:
            yield ref


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--fase12-dir", type=Path, required=True)
    p.add_argument("--almacenamiento-fase12", type=Path, required=True)
    p.add_argument("--fase11-dir", type=Path, required=True)
    p.add_argument("--almacenamiento-fase11", type=Path, required=True)
    p.add_argument("--manifest-fase10", type=Path, required=True)
    p.add_argument("--maestros-dir", type=Path, required=True)
    p.add_argument("--salida-dir", type=Path, required=True)
    p.add_argument("--cierre", type=Path, required=True)
    p.add_argument("--schema-maestro", type=Path)
    p.add_argument("--schema-concepto", type=Path)
    args = p.parse_args()

    schema_master = json.loads((args.schema_maestro or ROOT / "esquema/maestro-corpus-fase13-v1.0.0.schema.json").read_text(encoding="utf-8"))
    schema_concept = json.loads((args.schema_concepto or ROOT / "esquema/concepto-maestro-corpus-fase13-v1.0.0.schema.json").read_text(encoding="utf-8"))
    master_validator = jsonschema.Draft202012Validator(schema_master)
    concept_validator = jsonschema.Draft202012Validator(schema_concept)

    storage12, closure12, storage11, closure11, manifest10, audit12 = source_contract(
        args.fase12_dir, args.almacenamiento_fase12, args.fase11_dir, args.almacenamiento_fase11, args.manifest_fase10
    )
    master_path = args.salida_dir / "maestro-corpus.json"
    master = json.loads(master_path.read_text(encoding="utf-8"))
    master_validator.validate(master)
    if master["clausura_descriptiva"] != CLAUSURA_F13:
        raise SystemExit("Maestro F13 no conserva clausura descriptiva")
    if master["origen_fase12"]["cierre_sha256"] != storage12["gate"]["cierre_sha256"]:
        raise SystemExit("Maestro F13 no apunta al cierre F12 persistido")
    if master["origen_fase11"]["cierre_sha256"] != storage11["gate"]["cierre_sha256"]:
        raise SystemExit("Maestro F13 no apunta al cierre F11 persistido")
    if master["origen_fase10"]["asset_sha256"] != manifest10["almacenamiento"]["asset_sha256"]:
        raise SystemExit("Maestro F13 no apunta al asset F10 persistido")

    products = master["productos"]
    for key, expected_name in (
        ("conceptos", "conceptos-maestro-corpus.jsonl"),
        ("formulas", "formulas-corpus.jsonl"),
        ("restricciones", "restricciones-corpus.jsonl"),
    ):
        row = products[key]
        if row["ruta"] != expected_name or sha256_file(args.salida_dir / expected_name) != row["sha256"]:
            raise SystemExit(f"Producto F13 divergente: {key}")

    master_by_work = {row["obra_id"]: row for row in master["obras"]}
    expected_by_work = {row["obra_id"]: row for row in manifest10["maestros"]}
    if set(master_by_work) != set(expected_by_work):
        raise SystemExit("Maestro F13 no contiene exactamente los 20 maestros de obra")
    for obra, ptr in master_by_work.items():
        expected = expected_by_work[obra]
        if ptr["sha256"] != expected["sha256"] or ptr["ruta_en_asset_fase10"] != expected["ruta_en_zip"]:
            raise SystemExit(f"Puntero de maestro F10 divergente: {obra}")

    concept_keys: set[str] = set()
    concepts_count = 0
    assertions_count = 0
    traceable_assertions = 0
    all_refs = 0
    f12_path = args.fase12_dir / "expedientes-transversales.jsonl"
    f13_path = args.salida_dir / "conceptos-maestro-corpus.jsonl"
    with f12_path.open("r", encoding="utf-8") as src, f13_path.open("r", encoding="utf-8") as dst:
        src_iter = (line for line in src if line.strip())
        dst_iter = (line for line in dst if line.strip())
        while True:
            try:
                raw12 = next(src_iter)
            except StopIteration:
                raw12 = None
            try:
                raw13 = next(dst_iter)
            except StopIteration:
                raw13 = None
            if raw12 is None and raw13 is None:
                break
            if raw12 is None or raw13 is None:
                raise SystemExit("F13 no conserva cardinalidad uno-a-uno con F12")
            dossier = json.loads(raw12)
            row = json.loads(raw13)
            concept_validator.validate(row)
            key = row["clave_recuperacion"]
            if key != dossier["clave_recuperacion"] or row["expediente_fase12_id"] != dossier["id"]:
                raise SystemExit(f"F13 no conserva expediente F12 exacto: {key!r}")
            if key in concept_keys:
                raise SystemExit(f"Clave duplicada en F13: {key!r}")
            concept_keys.add(key)
            expected_id = stable_id("F13C", {"expediente_fase12": dossier["id"], "clave": key})
            if row["id"] != expected_id:
                raise SystemExit(f"ID conceptual F13 no determinista: {key!r}")
            if row["formas_literales"] != dossier["formas_literales_observadas"] or row["hallazgos_auditoria"] != dossier["hallazgos"]:
                raise SystemExit(f"F13 altera datos auditados de F12: {key!r}")
            if row["multiplicidad"] != dossier["multiplicidad"] or row["fuentes_fase11"] != dossier["fuentes_fase11"]:
                raise SystemExit(f"F13 altera multiplicidad o fuentes F12: {key!r}")
            if [x["obra_id"] for x in row["obras"]] != [x["obra_id"] for x in dossier["obras"]]:
                raise SystemExit(f"F13 altera distribución por obra de F12: {key!r}")
            if any(row[name] is not False for name in (
                "equivalencia_inferida","complementariedad_inferida","contradiccion_inferida",
                "evolucion_doctrinal_inferida","definicion_preferida","formula_concepto_inferida"
            )) or row["resolucion_doctrinal"] != "no_realizada":
                raise SystemExit(f"Clausura descriptiva violada en concepto F13: {key!r}")

            for ref in row["trazabilidad"]["registros_conceptuales"]:
                valid_ref(ref, master_by_work)
                all_refs += 1
            for ref in row["definiciones"]:
                valid_ref(ref, master_by_work, require_location=True)
                all_refs += 1
            explicit_ids = {r["registro_id"] for r in row["definiciones_explicitas"]}
            expected_explicit = {
                r["registro_id"] for r in row["definiciones"]
                if r.get("datos_documentales", {}).get("clasificacion_definicion") == "definicion_explicita"
            }
            if explicit_ids != expected_explicit:
                raise SystemExit(f"Subconjunto de definiciones explícitas divergente: {key!r}")
            for ref in row["predicaciones"]:
                assertions_count += 1
                valid_ref(ref, master_by_work, require_location=True)
                traceable_assertions += 1
                all_refs += 1
            for collection in ("variantes_recuperacion","relaciones_explicitas","negaciones","excepciones"):
                for ref in iter_group_refs(row[collection]):
                    valid_ref(ref, master_by_work, require_location=collection != "variantes_recuperacion")
                    all_refs += 1
            for formula in row["formulas"]:
                if formula["estado_vinculo_conceptual"] != "no_determinado":
                    raise SystemExit(f"Fórmula vinculada doctrinalmente en F13: {key!r}")
                valid_ref(formula["referencia"], master_by_work, require_location=True)
                all_refs += 1
            for restriction in row["restricciones"]:
                if key not in restriction["claves_conceptuales_vinculadas"] or restriction["criterio_vinculo"] != "afirmacion_limitada_id_documentado":
                    raise SystemExit(f"Restricción F13 vinculada sin referencia explícita: {key!r}")
                valid_ref(restriction["referencia"], master_by_work, require_location=True)
                all_refs += 1
            concepts_count += 1

    if concepts_count != products["conceptos"]["registros"] or concepts_count != closure12["expedientes_transversales"]:
        raise SystemExit("Cobertura conceptual F13 divergente")
    if assertions_count != traceable_assertions:
        raise SystemExit("No todas las predicaciones F13 tienen cadena documental completa")

    formulas_count = 0
    with (args.salida_dir / "formulas-corpus.jsonl").open("r", encoding="utf-8") as f:
        for raw in f:
            if not raw.strip():
                continue
            row = json.loads(raw)
            if row.get("tipo_registro") != "formula_corpus_auditada" or row.get("estado_vinculo_conceptual") != "no_determinado":
                raise SystemExit("Registro global de fórmula F13 impropio")
            for ref in row["registros"]:
                valid_ref(ref, master_by_work, require_location=True)
                all_refs += 1
            formulas_count += 1
    if formulas_count != products["formulas"]["registros"]:
        raise SystemExit("Conteo global de fórmulas F13 divergente")

    restrictions_count = 0
    with (args.salida_dir / "restricciones-corpus.jsonl").open("r", encoding="utf-8") as f:
        for raw in f:
            if not raw.strip():
                continue
            row = json.loads(raw)
            linked = row["claves_conceptuales_vinculadas"]
            if any(key not in concept_keys for key in linked):
                raise SystemExit("Restricción F13 apunta a clave conceptual inexistente")
            if linked and row["criterio_vinculo"] != "afirmacion_limitada_id_documentado":
                raise SystemExit("Restricción vinculada sin afirmación limitada documentada")
            if not linked and row["criterio_vinculo"] != "sin_vinculo_conceptual_documentado":
                raise SystemExit("Restricción no vinculada con criterio impropio")
            valid_ref(row["referencia"], master_by_work, require_location=True)
            all_refs += 1
            restrictions_count += 1
    if restrictions_count != products["restricciones"]["registros"]:
        raise SystemExit("Conteo global de restricciones F13 divergente")

    expected_master_id = stable_id("F13M", {"cierre_f12": storage12["gate"]["cierre_sha256"], "productos": products})
    if master["id"] != expected_master_id:
        raise SystemExit("ID del maestro F13 no determinista")

    with tempfile.TemporaryDirectory(prefix="fase13-repro-") as tmp:
        repro = Path(tmp)
        subprocess.run([
            sys.executable, str(MOTOR_DIR / "ensamblador_maestro_corpus_fase13.py"),
            "--fase12-dir", str(args.fase12_dir),
            "--almacenamiento-fase12", str(args.almacenamiento_fase12),
            "--fase11-dir", str(args.fase11_dir),
            "--almacenamiento-fase11", str(args.almacenamiento_fase11),
            "--manifest-fase10", str(args.manifest_fase10),
            "--maestros-dir", str(args.maestros_dir),
            "--salida-dir", str(repro),
        ], check=True)
        for name in ("maestro-corpus.json","conceptos-maestro-corpus.jsonl","formulas-corpus.jsonl","restricciones-corpus.jsonl"):
            if sha256_file(repro / name) != sha256_file(args.salida_dir / name):
                raise SystemExit(f"Fase 13 no es reproducible byte a byte: {name}")

    closure13 = {
        "version": "1.0.0",
        "fase": 13,
        "fase13_cerrada": True,
        "criterio": "cadena_maestro_corpus_a_maestro_obra_registro_unidad_fuente_para_cada_predicacion",
        "fuente_exclusiva": "expedientes_fase12_y_registros_auditados_de_origen",
        "origen_fase12": master["origen_fase12"],
        "origen_fase11": master["origen_fase11"],
        "origen_fase10": master["origen_fase10"],
        "maestros_obra": 20,
        "conceptos": concepts_count,
        "predicaciones_trazables": traceable_assertions,
        "formulas": formulas_count,
        "restricciones": restrictions_count,
        "referencias_auditadas_verificadas": all_refs,
        "maestro_sha256": sha256_file(master_path),
        "productos": products,
        "clausura_descriptiva": dict(CLAUSURA_F13),
    }
    digest = write_json(args.cierre, closure13)
    print(json.dumps({
        "fase": 13,
        "fase13_cerrada": True,
        "conceptos": concepts_count,
        "predicaciones_trazables": traceable_assertions,
        "formulas": formulas_count,
        "restricciones": restrictions_count,
        "cierre_sha256": digest,
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
