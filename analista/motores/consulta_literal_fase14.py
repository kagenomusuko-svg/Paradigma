#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import unicodedata
from pathlib import Path
from typing import Any, Iterable

VERSION = "1.0.0"
NEGATIVE_EVIDENCE = "No se encontró evidencia auditada en el expediente disponible."
NOT_DETERMINED = "NO DETERMINADO POR EL CORPUS."

CONCEPT_QUERY_TYPES = {
    "definiciones_explicitas",
    "predicaciones",
    "negaciones",
    "apariciones",
    "variantes_terminologicas",
    "excepciones",
}
QUERY_TYPES = CONCEPT_QUERY_TYPES | {"formulas_contienen", "relacion_explicita"}

CLAUSURA_F14 = {
    "solo_recuperacion_documental": True,
    "busqueda_semantica_inferida": False,
    "identidad_interobra_inferida": False,
    "equivalencia_inferida": False,
    "complementariedad_inferida": False,
    "contradiccion_inferida": False,
    "evolucion_doctrinal_inferida": False,
    "definicion_preferida": False,
    "formula_concepto_inferida": False,
    "sintesis_doctrinal": False,
    "resolucion_doctrinal": "no_realizada",
}


def formal_key(value: Any) -> str:
    if value is None:
        return ""
    return " ".join(unicodedata.normalize("NFKC", str(value)).split())


def canonical_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def stable_id(prefix: str, value: Any) -> str:
    return f"{prefix}-{hashlib.sha256(canonical_bytes(value)).hexdigest()[:12].upper()}"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def product_by_name(storage: dict[str, Any], name: str) -> dict[str, Any]:
    for row in storage.get("productos", []):
        if Path(row.get("ruta_en_zip", "")).name == name:
            return row
    raise SystemExit(f"Fase 13 no declara producto requerido: {name}")


def source_contract(fase13_dir: Path, almacenamiento_fase13: Path) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    storage = load_json(almacenamiento_fase13)
    gate = storage.get("gate", {})
    if storage.get("fase") != 13 or gate.get("fase13_cerrada") is not True:
        raise SystemExit("Fase 14 requiere Fase 13 cerrada")

    closure_path = fase13_dir / "cierre-fase13.json"
    if not closure_path.is_file() or sha256_file(closure_path) != gate.get("cierre_sha256"):
        raise SystemExit("Cierre F13 ausente o divergente")
    closure = load_json(closure_path)
    if closure.get("fase") != 13 or closure.get("fase13_cerrada") is not True:
        raise SystemExit("Cierre F13 incompatible")

    required = ("maestro-corpus.json", "conceptos-maestro-corpus.jsonl", "formulas-corpus.jsonl", "restricciones-corpus.jsonl")
    for name in required:
        declared = product_by_name(storage, name)
        path = fase13_dir / name
        if not path.is_file() or sha256_file(path) != declared.get("sha256"):
            raise SystemExit(f"Producto F13 ausente o divergente: {name}")

    master = load_json(fase13_dir / "maestro-corpus.json")
    if master.get("fase") != 13 or master.get("tipo_registro") != "expediente_maestro_corpus":
        raise SystemExit("Maestro F13 incompatible")
    if master.get("estado_auditoria") != "auditado":
        raise SystemExit("Maestro F13 no auditado")
    if master.get("clausura_descriptiva", {}).get("resolucion_doctrinal") != "no_realizada":
        raise SystemExit("Maestro F13 no conserva clausura descriptiva")
    return storage, closure, master


def validate_query(query: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(query, dict):
        raise SystemExit("Consulta F14 no es objeto JSON")
    qtype = query.get("tipo")
    if qtype not in QUERY_TYPES:
        raise SystemExit(f"Tipo de consulta F14 no soportado: {qtype!r}")
    if qtype == "relacion_explicita":
        for field in ("termino", "relacion", "objeto"):
            if not isinstance(query.get(field), str) or not formal_key(query[field]):
                raise SystemExit(f"Consulta relacional F14 requiere {field}")
    else:
        if not isinstance(query.get("termino"), str) or not formal_key(query["termino"]):
            raise SystemExit("Consulta F14 requiere termino no vacío")
    allowed = {"tipo", "termino", "relacion", "objeto"}
    extra = set(query) - allowed
    if extra:
        raise SystemExit(f"Campos de consulta F14 no soportados: {sorted(extra)}")
    return {k: query[k] for k in ("tipo", "termino", "relacion", "objeto") if k in query}


def validate_ref(ref: dict[str, Any]) -> None:
    if ref.get("estado_verificacion") != "verificado" or ref.get("estado_auditoria") != "auditado":
        raise SystemExit(f"F14 intentó emitir referencia no auditada/verificada: {ref.get('obra_id')}:{ref.get('registro_id')}")
    if not ref.get("obra_id") or not ref.get("registro_id"):
        raise SystemExit("F14 intentó emitir referencia sin identidad documental")


def result_from_ref(kind: str, key: str, ref: dict[str, Any], **extra: Any) -> dict[str, Any]:
    validate_ref(ref)
    row: dict[str, Any] = {
        "tipo_hallazgo": kind,
        "clave_recuperacion": key,
        "referencia": ref,
    }
    for name, value in extra.items():
        if value is not None:
            row[name] = value
    return row


def grouped_results(kind: str, concept_key: str, groups: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for group in groups:
        for ref in group.get("registros", []):
            out.append(result_from_ref(
                kind,
                concept_key,
                ref,
                grupo_id=group.get("grupo_id"),
                clave_grupo=group.get("clave_recuperacion"),
                criterio_agrupacion=group.get("criterio_agrupacion"),
                estado_identidad_interobra=group.get("estado_identidad_interobra"),
            ))
    return out


def scan_concepts(
    path: Path, normalized_terms: set[str]
) -> tuple[dict[str, dict[str, list[dict[str, Any]]]], dict[str, dict[str, Any]]]:
    matches = {term: {"exactas": [], "formas": []} for term in normalized_terms}
    relation_groups: dict[str, dict[str, Any]] = {}
    with path.open("r", encoding="utf-8") as f:
        for raw in f:
            if not raw.strip():
                continue
            row = json.loads(raw)
            key = formal_key(row.get("clave_recuperacion"))
            if key in matches:
                matches[key]["exactas"].append(row)
            forms = {formal_key(x) for x in row.get("formas_literales", []) if formal_key(x)}
            for term in forms & normalized_terms:
                if key != term:
                    matches[term]["formas"].append(row)
            for group in row.get("relaciones_explicitas", []):
                gid = group.get("grupo_id")
                if not isinstance(gid, str) or not gid:
                    raise SystemExit("Grupo relacional F13 sin grupo_id")
                previous = relation_groups.setdefault(gid, group)
                if previous != group:
                    raise SystemExit(f"Grupo relacional F13 divergente entre expedientes: {gid}")
    return matches, relation_groups


def resolved_rows(term: str, matches: dict[str, dict[str, list[dict[str, Any]]]]) -> tuple[list[dict[str, Any]], str]:
    normalized = formal_key(term)
    bucket = matches.get(normalized, {"exactas": [], "formas": []})
    if bucket["exactas"]:
        return bucket["exactas"], "clave_recuperacion_exacta"
    if bucket["formas"]:
        rows = sorted(bucket["formas"], key=lambda x: x["clave_recuperacion"])
        return rows, "forma_literal_exacta_sin_fusion_conceptual"
    return [], "sin_coincidencia_documental"


def resolution(term: str, rows: list[dict[str, Any]], criterion: str) -> dict[str, Any]:
    return {
        "entrada": term,
        "normalizacion_recuperacion": formal_key(term),
        "criterio": criterion,
        "claves": sorted({row["clave_recuperacion"] for row in rows}),
    }


def concept_results(qtype: str, rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for row in rows:
        key = row["clave_recuperacion"]
        if qtype == "definiciones_explicitas":
            for ref in row.get("definiciones_explicitas", []):
                out.append(result_from_ref("definicion_explicita", key, ref, expediente_fase13_id=row.get("id")))
        elif qtype == "predicaciones":
            for ref in row.get("predicaciones", []):
                out.append(result_from_ref("predicacion", key, ref, expediente_fase13_id=row.get("id")))
        elif qtype == "negaciones":
            out.extend(grouped_results("negacion", key, row.get("negaciones", [])))
        elif qtype == "apariciones":
            for ref in row.get("trazabilidad", {}).get("registros_conceptuales", []):
                out.append(result_from_ref("registro_conceptual", key, ref, expediente_fase13_id=row.get("id")))
        elif qtype == "variantes_terminologicas":
            out.extend(grouped_results("variante_recuperacion", key, row.get("variantes_recuperacion", [])))
        elif qtype == "excepciones":
            out.extend(grouped_results("excepcion", key, row.get("excepciones", [])))
        else:
            raise SystemExit(f"Consulta conceptual no soportada: {qtype}")
    return sorted(out, key=result_sort_key)


def endpoint_candidates(term: str, rows: list[dict[str, Any]]) -> set[str]:
    keys = {formal_key(row["clave_recuperacion"]) for row in rows}
    return keys or {formal_key(term)}


def relation_results(
    query: dict[str, Any],
    subject_rows: list[dict[str, Any]],
    object_rows: list[dict[str, Any]],
    groups: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    subject_keys = endpoint_candidates(query["termino"], subject_rows)
    object_keys = endpoint_candidates(query["objeto"], object_rows)
    relation = formal_key(query["relacion"])
    out: list[dict[str, Any]] = []
    for _, group in sorted(groups.items()):
        try:
            triplet = json.loads(group.get("clave_recuperacion", ""))
        except json.JSONDecodeError:
            raise SystemExit(f"Tripleta relacional F13 inválida: {group.get('grupo_id')}")
        if not isinstance(triplet, list) or len(triplet) != 3:
            raise SystemExit(f"Tripleta relacional F13 inválida: {group.get('grupo_id')}")
        if formal_key(triplet[0]) not in subject_keys or formal_key(triplet[1]) != relation or formal_key(triplet[2]) not in object_keys:
            continue
        for ref in group.get("registros", []):
            out.append(result_from_ref(
                "relacion_explicita",
                formal_key(triplet[0]),
                ref,
                grupo_id=group.get("grupo_id"),
                clave_grupo=group.get("clave_recuperacion"),
                criterio_agrupacion=group.get("criterio_agrupacion"),
                estado_identidad_interobra=group.get("estado_identidad_interobra"),
            ))
    return sorted(out, key=result_sort_key)


def formula_results(path: Path, terms: set[str]) -> dict[str, list[dict[str, Any]]]:
    results = {term: [] for term in terms}
    if not terms:
        return results
    with path.open("r", encoding="utf-8") as f:
        for raw in f:
            if not raw.strip():
                continue
            group = json.loads(raw)
            if group.get("estado_vinculo_conceptual") != "no_determinado" or group.get("resolucion_doctrinal") != "no_realizada":
                raise SystemExit(f"Grupo de fórmula F13 impropio: {group.get('id')}")
            for ref in group.get("registros", []):
                literal = ref.get("datos_documentales", {}).get("formula_literal") or ref.get("texto_literal") or ""
                normalized_literal = formal_key(literal)
                for term in terms:
                    if term and term in normalized_literal:
                        results[term].append(result_from_ref(
                            "formula_literal",
                            group.get("clave_recuperacion", ""),
                            ref,
                            grupo_fase11_id=group.get("grupo_fase11_id"),
                            criterio_agrupacion=group.get("criterio_agrupacion"),
                            estado_vinculo_conceptual="no_determinado",
                            resolucion_doctrinal="no_realizada",
                        ))
    for term in results:
        results[term].sort(key=result_sort_key)
    return results


def result_sort_key(row: dict[str, Any]) -> tuple[str, str, str, str]:
    ref = row["referencia"]
    return (
        row.get("clave_recuperacion", ""),
        row.get("grupo_id", row.get("grupo_fase11_id", "")),
        ref.get("obra_id", ""),
        ref.get("registro_id", ""),
    )


def response_base(query: dict[str, Any], storage: dict[str, Any], master: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": stable_id("F14R", {"consulta": query, "cierre_f13": storage["gate"]["cierre_sha256"]}),
        "tipo_registro": "respuesta_consulta_literal",
        "schema_version": VERSION,
        "fase": 14,
        "consulta": query,
        "origen_fase13": {
            "cierre_sha256": storage["gate"]["cierre_sha256"],
            "maestro_id": master["id"],
            "maestro_sha256": product_by_name(storage, "maestro-corpus.json")["sha256"],
        },
        "clausura_descriptiva": dict(CLAUSURA_F14),
    }


def finalize_response(base: dict[str, Any], results: list[dict[str, Any]], *, relation_query: bool = False) -> dict[str, Any]:
    base["resultados"] = results
    base["conteo_resultados"] = len(results)
    if results:
        base["estado"] = "hallazgo_auditado"
        base["mensaje"] = None
    elif relation_query:
        base["estado"] = "no_determinado_por_el_corpus"
        base["mensaje"] = NOT_DETERMINED
    else:
        base["estado"] = "sin_hallazgo_auditado"
        base["mensaje"] = NEGATIVE_EVIDENCE
    return base


def execute_queries(fase13_dir: Path, almacenamiento_fase13: Path, raw_queries: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    storage, _, master = source_contract(fase13_dir, almacenamiento_fase13)
    queries = [validate_query(q) for q in raw_queries]

    concept_terms: set[str] = set()
    formula_terms: set[str] = set()
    for q in queries:
        if q["tipo"] in CONCEPT_QUERY_TYPES:
            concept_terms.add(formal_key(q["termino"]))
        elif q["tipo"] == "relacion_explicita":
            concept_terms.add(formal_key(q["termino"]))
            concept_terms.add(formal_key(q["objeto"]))
        elif q["tipo"] == "formulas_contienen":
            formula_terms.add(formal_key(q["termino"]))

    concept_matches, relation_groups = scan_concepts(fase13_dir / "conceptos-maestro-corpus.jsonl", concept_terms)
    formula_matches = formula_results(fase13_dir / "formulas-corpus.jsonl", formula_terms)

    responses: list[dict[str, Any]] = []
    for q in queries:
        base = response_base(q, storage, master)
        qtype = q["tipo"]
        if qtype in CONCEPT_QUERY_TYPES:
            rows, criterion = resolved_rows(q["termino"], concept_matches)
            base["criterio_recuperacion"] = "clave_documental_o_forma_literal_exacta_sin_similitud_semantica"
            base["resolucion_consulta"] = {"termino": resolution(q["termino"], rows, criterion)}
            responses.append(finalize_response(base, concept_results(qtype, rows)))
        elif qtype == "formulas_contienen":
            term = formal_key(q["termino"])
            base["criterio_recuperacion"] = "subcadena_literal_nfkc_en_formula_documentada"
            base["resolucion_consulta"] = {
                "termino": {
                    "entrada": q["termino"],
                    "normalizacion_recuperacion": term,
                    "criterio": "subcadena_literal",
                    "claves": [],
                }
            }
            responses.append(finalize_response(base, formula_matches.get(term, [])))
        elif qtype == "relacion_explicita":
            subject_rows, subject_criterion = resolved_rows(q["termino"], concept_matches)
            object_rows, object_criterion = resolved_rows(q["objeto"], concept_matches)
            base["criterio_recuperacion"] = "tripleta_formal_exacta_sujeto_relacion_objeto_sin_equivalencia_inferida"
            base["resolucion_consulta"] = {
                "termino": resolution(q["termino"], subject_rows, subject_criterion),
                "objeto": resolution(q["objeto"], object_rows, object_criterion),
            }
            responses.append(finalize_response(base, relation_results(q, subject_rows, object_rows, relation_groups), relation_query=True))
        else:
            raise AssertionError(qtype)
    return responses


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    h = hashlib.sha256()
    with path.open("wb") as f:
        for row in rows:
            payload = canonical_bytes(row)
            f.write(payload)
            h.update(payload)
    digest = h.hexdigest()
    path.with_name(path.name + ".sha256").write_text(f"{digest}  {path.name}\n", encoding="utf-8")
    return digest


def read_batch(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line_no, raw in enumerate(f, 1):
            if raw.strip():
                try:
                    rows.append(json.loads(raw))
                except json.JSONDecodeError as exc:
                    raise SystemExit(f"JSON inválido en consulta {path}:{line_no}: {exc}") from exc
    return rows


def main() -> int:
    p = argparse.ArgumentParser(description="Consulta literal y auditada del maestro de corpus F13")
    p.add_argument("--fase13-dir", type=Path, required=True)
    p.add_argument("--almacenamiento-fase13", type=Path, required=True)
    source = p.add_mutually_exclusive_group(required=True)
    source.add_argument("--consulta-json")
    source.add_argument("--lote", type=Path)
    p.add_argument("--salida", type=Path)
    args = p.parse_args()

    queries = [json.loads(args.consulta_json)] if args.consulta_json else read_batch(args.lote)
    responses = execute_queries(args.fase13_dir, args.almacenamiento_fase13, queries)
    if args.salida:
        digest = write_jsonl(args.salida, responses)
        print(json.dumps({"fase": 14, "respuestas": len(responses), "sha256": digest}, ensure_ascii=False, sort_keys=True))
    else:
        for response in responses:
            sys.stdout.buffer.write(canonical_bytes(response))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
