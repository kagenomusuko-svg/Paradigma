#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import unicodedata
from collections import defaultdict
from pathlib import Path
from typing import Any, Callable, Iterator

VERSION = "1.0.0"
EXPECTED_MOTORS = (
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
CLAUSURA_F11 = {
    "solo_maestros_obra": True,
    "identidad_interobra_inferida": False,
    "equivalencia_inferida": False,
    "complementariedad_inferida": False,
    "contradiccion_inferida": False,
    "sintesis_doctrinal": False,
    "resolucion_doctrinal": "no_realizada",
}
CLAUSURA_F12 = {
    "identidad_interobra_inferida": False,
    "equivalencia_inferida": False,
    "complementariedad_inferida": False,
    "contradiccion_inferida": False,
    "sintesis_doctrinal": False,
    "reconciliacion_interobra": False,
    "evolucion_doctrinal_inferida": False,
    "definicion_preferida": False,
    "resolucion_doctrinal": "no_realizada",
}


def canonical_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def stable_id(prefix: str, value: Any) -> str:
    return f"{prefix}-{hashlib.sha256(canonical_bytes(value)).hexdigest()[:12].upper()}"


def formal_key(value: Any) -> str:
    if value is None:
        return ""
    return " ".join(unicodedata.normalize("NFKC", str(value)).split())


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def write_json(path: Path, value: dict[str, Any]) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(value, f, ensure_ascii=False, sort_keys=True, indent=2)
        f.write("\n")
    digest = sha256_file(path)
    path.with_name(path.name + ".sha256").write_text(f"{digest}  {path.name}\n", encoding="utf-8")
    return digest


class JSONStream:
    """Decodificador incremental suficiente para los JSON deterministas de Fase 11."""

    def __init__(self, path: Path, chunk_size: int = 1024 * 1024) -> None:
        self.file = path.open("r", encoding="utf-8")
        self.chunk_size = chunk_size
        self.buffer = ""
        self.pos = 0
        self.eof = False
        self.decoder = json.JSONDecoder()

    def close(self) -> None:
        self.file.close()

    def _compact(self) -> None:
        if self.pos > self.chunk_size:
            self.buffer = self.buffer[self.pos :]
            self.pos = 0

    def _fill(self) -> bool:
        if self.eof:
            return False
        chunk = self.file.read(self.chunk_size)
        if chunk:
            if self.pos:
                self.buffer = self.buffer[self.pos :] + chunk
                self.pos = 0
            else:
                self.buffer += chunk
            return True
        self.eof = True
        return False

    def skip_ws(self) -> None:
        while True:
            while self.pos < len(self.buffer) and self.buffer[self.pos].isspace():
                self.pos += 1
            if self.pos < len(self.buffer) or self.eof:
                self._compact()
                return
            self._fill()

    def peek(self) -> str:
        self.skip_ws()
        while self.pos >= len(self.buffer) and not self.eof:
            self._fill()
            self.skip_ws()
        if self.pos >= len(self.buffer):
            raise ValueError("JSON truncado")
        return self.buffer[self.pos]

    def expect(self, char: str) -> None:
        if self.peek() != char:
            raise ValueError(f"Se esperaba {char!r} en JSON")
        self.pos += 1
        self._compact()

    def decode(self) -> Any:
        self.skip_ws()
        while True:
            try:
                value, end = self.decoder.raw_decode(self.buffer, self.pos)
                self.pos = end
                self._compact()
                return value
            except json.JSONDecodeError:
                if self.eof:
                    raise
                self._fill()

    def iter_array(self) -> Iterator[Any]:
        self.expect("[")
        first = True
        while True:
            c = self.peek()
            if c == "]":
                self.pos += 1
                self._compact()
                return
            if not first:
                self.expect(",")
            yield self.decode()
            first = False


def stream_f11_product(path: Path, on_group: Callable[[dict[str, Any]], None]) -> dict[str, Any]:
    stream = JSONStream(path)
    metadata: dict[str, Any] = {}
    try:
        stream.expect("{")
        first = True
        while True:
            c = stream.peek()
            if c == "}":
                stream.pos += 1
                break
            if not first:
                stream.expect(",")
            key = stream.decode()
            if not isinstance(key, str):
                raise ValueError("Clave superior no textual")
            stream.expect(":")
            if key == "grupos":
                for group in stream.iter_array():
                    if not isinstance(group, dict):
                        raise ValueError("Grupo F11 no es objeto")
                    on_group(group)
            else:
                metadata[key] = stream.decode()
            first = False
        stream.skip_ws()
        if not stream.eof:
            stream._fill()
            stream.skip_ws()
        if stream.pos < len(stream.buffer):
            raise ValueError("Contenido residual tras objeto JSON")
        return metadata
    finally:
        stream.close()


def count_by_work(refs: list[dict[str, Any]], *, unique_records: bool = False) -> dict[str, int]:
    if unique_records:
        seen: dict[str, set[str]] = defaultdict(set)
        for ref in refs:
            seen[ref["obra_id"]].add(ref["registro_id"])
        return {obra: len(ids) for obra, ids in sorted(seen.items())}
    counts: dict[str, int] = defaultdict(int)
    for ref in refs:
        counts[ref["obra_id"]] += 1
    return dict(sorted(counts.items()))


def merge_count(target: dict[str, dict[str, Any]], field: str, counts: dict[str, int]) -> None:
    for obra, count in counts.items():
        target.setdefault(obra, {})[field] = target.setdefault(obra, {}).get(field, 0) + count


def load_source(fase11_dir: Path, storage_path: Path) -> tuple[dict[str, Any], dict[str, Any], dict[str, dict[str, Any]]]:
    storage = json.loads(storage_path.read_text(encoding="utf-8"))
    closure_path = fase11_dir / "cierre-fase11.json"
    closure = json.loads(closure_path.read_text(encoding="utf-8"))
    gate = storage.get("gate", {})
    if storage.get("fase") != 11 or gate.get("fase11_cerrada") is not True:
        raise SystemExit("Fase 12 requiere almacenamiento persistido con Fase 11 cerrada")
    if closure.get("fase") != 11 or closure.get("fase11_cerrada") is not True:
        raise SystemExit("Cierre Fase 11 ausente o no cerrado")
    if gate.get("maestros") != 20 or len(closure.get("maestros", [])) != 20:
        raise SystemExit("Fase 12 requiere exactamente 20 maestros de origen")
    if gate.get("motores") != 9 or len(closure.get("motores", [])) != 9:
        raise SystemExit("Fase 12 requiere los nueve comparadores cerrados")
    closure_digest = hashlib.sha256(closure_path.read_bytes()).hexdigest()
    if closure_digest != gate.get("cierre_sha256"):
        raise SystemExit("Hash del cierre de Fase 11 no coincide con su manifiesto")
    if storage.get("clausura_descriptiva") != closure.get("clausura_descriptiva"):
        raise SystemExit("Clausura Fase 11 divergente entre cierre y almacenamiento")
    if closure.get("clausura_descriptiva") != {k: v for k, v in CLAUSURA_F11.items() if k != "solo_maestros_obra"}:
        raise SystemExit("El cierre Fase 11 no conserva clausura descriptiva")
    by_motor = {row["motor"]: row for row in closure["motores"]}
    if set(by_motor) != set(EXPECTED_MOTORS):
        raise SystemExit("Conjunto de motores Fase 11 inesperado")
    storage_products = {row["motor"]: row for row in storage.get("productos", [])}
    if set(storage_products) != set(EXPECTED_MOTORS):
        raise SystemExit("Manifiesto Fase 11 incompleto")
    for motor in EXPECTED_MOTORS:
        expected = by_motor[motor]
        stored = storage_products[motor]
        if stored.get("sha256") != expected.get("sha256"):
            raise SystemExit(f"Hash divergente para {motor}")
        if stored.get("ruta_en_zip") != "fase11/" + expected.get("ruta", ""):
            raise SystemExit(f"Ruta divergente para {motor}")
    return storage, closure, by_motor


def audit_product(
    path: Path,
    motor: str,
    expected: dict[str, Any],
    masters: list[dict[str, Any]],
    on_group: Callable[[dict[str, Any]], None],
) -> dict[str, Any]:
    actual_sha = sha256_file(path)
    if actual_sha != expected["sha256"]:
        raise SystemExit(f"Hash F11 inválido en {motor}: {actual_sha}")
    master_ids = {row["obra_id"] for row in masters}
    group_ids: set[str] = set()
    source_ids: set[tuple[str, str]] = set()
    groups = 0

    def inspect(group: dict[str, Any]) -> None:
        nonlocal groups
        groups += 1
        key = group.get("clave_recuperacion")
        if not isinstance(key, str) or formal_key(key) != key:
            raise SystemExit(f"Clave F11 no normalizada en {motor}")
        expected_id = stable_id("F11G", {"motor": motor, "clave": key})
        if group.get("id") != expected_id or expected_id in group_ids:
            raise SystemExit(f"ID de grupo inválido o duplicado en {motor}: {group.get('id')}")
        group_ids.add(expected_id)
        if group.get("estado_identidad_interobra") not in {"no_determinada", "no_aplica"}:
            raise SystemExit(f"Identidad interobra impropia en {motor}:{key}")
        if any(group.get(name) is not False for name in ("equivalencia_inferida", "complementariedad_inferida", "contradiccion_inferida")):
            raise SystemExit(f"Inferencia doctrinal prohibida en {motor}:{key}")
        if group.get("resolucion_doctrinal") != "no_realizada":
            raise SystemExit(f"Resolución doctrinal impropia en {motor}:{key}")
        refs = group.get("registros")
        if not isinstance(refs, list) or not refs:
            raise SystemExit(f"Grupo sin registros en {motor}:{key}")
        obras = set()
        for ref in refs:
            obra = ref.get("obra_id")
            rid = ref.get("registro_id")
            if obra not in master_ids or not isinstance(rid, str) or not rid:
                raise SystemExit(f"Referencia de origen inválida en {motor}:{key}")
            if ref.get("estado_verificacion") != "verificado" or ref.get("estado_auditoria") != "auditado":
                raise SystemExit(f"Registro no verificado/auditado en {motor}:{key}:{rid}")
            obras.add(obra)
            source_ids.add((obra, rid))
        if group.get("obra_ids") != sorted(obras):
            raise SystemExit(f"obra_ids divergente en {motor}:{key}")
        on_group(group)

    metadata = stream_f11_product(path, inspect)
    if metadata.get("tipo_registro") != "salida_comparacion_corpus" or metadata.get("schema_version") != "1.0.0":
        raise SystemExit(f"Contrato F11 incompatible en {motor}")
    if metadata.get("motor") != motor or metadata.get("version_motor") != "1.0.0":
        raise SystemExit(f"Motor/version F11 incompatible en {motor}")
    if metadata.get("fuente_exclusiva") != "json_maestros_obra_auditados":
        raise SystemExit(f"Fuente F11 impropia en {motor}")
    if metadata.get("maestros") != masters:
        raise SystemExit(f"Metadatos de maestros divergentes en {motor}")
    if metadata.get("clausura_descriptiva") != CLAUSURA_F11:
        raise SystemExit(f"Clausura F11 alterada en {motor}")
    coverage = metadata.get("cobertura", {})
    if coverage.get("obras_totales") != 20 or coverage.get("obras_procesadas") != 20:
        raise SystemExit(f"Cobertura de obras incompleta en {motor}")
    if coverage.get("grupos_emitidos") != groups or coverage.get("registros_origen") != len(source_ids):
        raise SystemExit(f"Cobertura cuantitativa divergente en {motor}")
    expected_out = stable_id("F11OUT", {"motor": motor, "maestros": masters, "grupos": groups})
    if metadata.get("id") != expected_out:
        raise SystemExit(f"ID de salida F11 inválido en {motor}")
    return {
        "motor": motor,
        "ruta": path.name,
        "sha256": actual_sha,
        "grupos_auditados": groups,
        "registros_origen_unicos": len(source_ids),
        "estado_auditoria": "auditado",
    }


def make_dossier(key: str, group: dict[str, Any]) -> dict[str, Any]:
    works: dict[str, dict[str, Any]] = {}
    forms: dict[str, set[str]] = defaultdict(set)
    for ref in group["registros"]:
        obra = ref["obra_id"]
        work = works.setdefault(obra, {"obra_id": obra})
        work["conceptos_registrados"] = work.get("conceptos_registrados", 0) + 1
        for form in ref.get("datos_documentales", {}).get("formas_literales_observadas", []) or []:
            if isinstance(form, str) and form:
                forms[obra].add(form)
    for obra, values in forms.items():
        works[obra]["formas_literales_observadas"] = sorted(values)
    return {
        "id": stable_id("F12X", {"clave": key, "grupo_conceptos": group["id"]}),
        "tipo_registro": "expediente_transversal_auditado",
        "schema_version": VERSION,
        "clave_recuperacion": key,
        "criterio_clave": "clave_documental_de_fase11_no_identidad_conceptual_interobra",
        "estado_identidad_interobra": "no_determinada",
        "fuentes_fase11": {
            "conceptos_corpus": group["id"],
            "definiciones_corpus": None,
            "afirmaciones_corpus": None,
            "orden_recurrencia": None,
        },
        "obras": works,
        "variaciones_terminologicas": {},
        "relaciones_explicitas": {},
        "negaciones_recuperadas_por_forma": {},
        "excepciones_vinculadas_a_predicaciones": {},
        "hallazgos": set(),
        "equivalencia_inferida": False,
        "complementariedad_inferida": False,
        "contradiccion_inferida": False,
        "evolucion_doctrinal_inferida": False,
        "definicion_preferida": False,
        "resolucion_doctrinal": "no_realizada",
    }


def finalize_dossier(d: dict[str, Any]) -> dict[str, Any]:
    works_out = []
    totals = defaultdict(int)
    defaults = (
        "conceptos_registrados",
        "apariciones_totales_documentadas",
        "definiciones_registros",
        "predicaciones_registros",
        "vinculos_predicacion_concepto",
        "relaciones_como_sujeto",
        "relaciones_como_objeto",
        "negaciones_recuperadas_por_forma",
        "excepciones_vinculadas_a_predicaciones",
    )
    for obra in sorted(d["obras"]):
        work = d["obras"][obra]
        for field in defaults:
            work.setdefault(field, 0)
            totals[field] += work[field]
        work.setdefault("formas_literales_observadas", [])
        works_out.append(work)
    unique_forms = sorted({form for work in works_out for form in work["formas_literales_observadas"]})
    variants = [d["variaciones_terminologicas"][k] for k in sorted(d["variaciones_terminologicas"])]
    relations = [d["relaciones_explicitas"][k] for k in sorted(d["relaciones_explicitas"])]
    negations = [d["negaciones_recuperadas_por_forma"][k] for k in sorted(d["negaciones_recuperadas_por_forma"])]
    exceptions = [d["excepciones_vinculadas_a_predicaciones"][k] for k in sorted(d["excepciones_vinculadas_a_predicaciones"])]
    findings = set(d["hallazgos"])
    if totals["predicaciones_registros"] > 1:
        findings.add("multiplicidad_predicativa")
    if totals["definiciones_registros"] > 1:
        findings.add("definiciones_multiples")
    if len(unique_forms) > 1 or len(variants) > 1:
        findings.add("variacion_terminologica")
    return {
        "id": d["id"],
        "tipo_registro": d["tipo_registro"],
        "schema_version": d["schema_version"],
        "clave_recuperacion": d["clave_recuperacion"],
        "criterio_clave": d["criterio_clave"],
        "estado_identidad_interobra": d["estado_identidad_interobra"],
        "fuentes_fase11": d["fuentes_fase11"],
        "multiplicidad": {
            "obras_con_clave": sum(1 for work in works_out if work["conceptos_registrados"] > 0),
            "conceptos_registrados_total": totals["conceptos_registrados"],
            "apariciones_totales_documentadas": totals["apariciones_totales_documentadas"],
            "definiciones_registros_total": totals["definiciones_registros"],
            "predicaciones_registros_total": totals["predicaciones_registros"],
            "vinculos_predicacion_concepto_total": totals["vinculos_predicacion_concepto"],
        },
        "obras": works_out,
        "formas_literales_observadas": unique_forms,
        "variaciones_terminologicas": variants,
        "relaciones_explicitas": relations,
        "negaciones_recuperadas_por_forma": negations,
        "excepciones_vinculadas_a_predicaciones": exceptions,
        "hallazgos": sorted(findings),
        "equivalencia_inferida": False,
        "complementariedad_inferida": False,
        "contradiccion_inferida": False,
        "evolucion_doctrinal_inferida": False,
        "definicion_preferida": False,
        "resolucion_doctrinal": "no_realizada",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fase11-dir", type=Path, required=True)
    parser.add_argument("--almacenamiento", type=Path, required=True)
    parser.add_argument("--salida-dir", type=Path, required=True)
    args = parser.parse_args()

    storage, closure, by_motor = load_source(args.fase11_dir, args.almacenamiento)
    masters = closure["maestros"]
    dossiers: dict[str, dict[str, Any]] = {}
    concept_source_to_key: dict[tuple[str, str], str] = {}
    assertion_to_keys: dict[tuple[str, str], set[str]] = defaultdict(set)
    products: list[dict[str, Any]] = []
    groups_without_dossier: dict[str, int] = defaultdict(int)

    def concepts_cb(group: dict[str, Any]) -> None:
        key = group["clave_recuperacion"]
        if key in dossiers:
            raise SystemExit(f"Clave conceptual duplicada en F11: {key}")
        dossiers[key] = make_dossier(key, group)
        for ref in group["registros"]:
            source = (ref["obra_id"], ref["registro_id"])
            previous = concept_source_to_key.setdefault(source, key)
            if previous != key:
                raise SystemExit(f"Concepto de origen asociado a dos claves F11: {source}")

    callbacks: dict[str, Callable[[dict[str, Any]], None]] = {"conceptos_corpus": concepts_cb}

    def definitions_cb(group: dict[str, Any]) -> None:
        key = group["clave_recuperacion"]
        d = dossiers.get(key)
        if d is None:
            groups_without_dossier["definiciones_corpus"] += 1
            return
        d["fuentes_fase11"]["definiciones_corpus"] = group["id"]
        merge_count(d["obras"], "definiciones_registros", count_by_work(group["registros"], unique_records=True))

    callbacks["definiciones_corpus"] = definitions_cb

    def assertions_cb(group: dict[str, Any]) -> None:
        key = group["clave_recuperacion"]
        d = dossiers.get(key)
        if d is None:
            groups_without_dossier["afirmaciones_corpus"] += 1
            return
        d["fuentes_fase11"]["afirmaciones_corpus"] = group["id"]
        merge_count(d["obras"], "predicaciones_registros", count_by_work(group["registros"], unique_records=True))
        merge_count(d["obras"], "vinculos_predicacion_concepto", count_by_work(group["registros"], unique_records=False))
        for ref in group["registros"]:
            assertion_to_keys[(ref["obra_id"], ref["registro_id"])].add(key)

    callbacks["afirmaciones_corpus"] = assertions_cb

    callbacks["formulas_corpus"] = lambda group: None

    def relations_cb(group: dict[str, Any]) -> None:
        try:
            triplet = json.loads(group["clave_recuperacion"])
        except json.JSONDecodeError as exc:
            raise SystemExit(f"Clave de relación F11 no es tripleta JSON: {group['id']}") from exc
        if not isinstance(triplet, list) or len(triplet) != 3 or not all(isinstance(x, str) for x in triplet):
            raise SystemExit(f"Tripleta relacional inválida: {group['id']}")
        skey, rkey, okey = triplet
        roles: list[tuple[str, str, str]] = []
        if skey in dossiers:
            roles.append((skey, "sujeto", okey))
        if okey in dossiers:
            roles.append((okey, "objeto", skey))
        if not roles:
            groups_without_dossier["relaciones_explicitas_corpus"] += 1
        for key, role, other in roles:
            d = dossiers[key]
            entry = d["relaciones_explicitas"].setdefault(
                group["id"],
                {
                    "grupo_id": group["id"],
                    "clave_relacion": rkey,
                    "otra_clave": other,
                    "roles_de_la_clave": [],
                    "conteos_por_obra": count_by_work(group["registros"], unique_records=True),
                },
            )
            if role not in entry["roles_de_la_clave"]:
                entry["roles_de_la_clave"].append(role)
                entry["roles_de_la_clave"].sort()
            merge_count(d["obras"], f"relaciones_como_{role}", count_by_work(group["registros"], unique_records=True))

    callbacks["relaciones_explicitas_corpus"] = relations_cb

    def neg_exc_cb(group: dict[str, Any]) -> None:
        refs = group["registros"]
        handled = False
        if group["clave_recuperacion"].startswith("negacion::"):
            literal_key = group["clave_recuperacion"].split("::", 1)[1]
            d = dossiers.get(literal_key)
            if d is not None:
                handled = True
                d["negaciones_recuperadas_por_forma"][group["id"]] = {
                    "grupo_id": group["id"],
                    "criterio_vinculo": "coincidencia_formal_exclusivamente_para_recuperacion",
                    "estado_vinculo_conceptual": "no_determinado",
                    "conteos_por_obra": count_by_work(refs, unique_records=True),
                    "clasificaciones": sorted({
                        ref.get("datos_documentales", {}).get("clasificacion_negacion")
                        for ref in refs
                        if ref.get("datos_documentales", {}).get("clasificacion_negacion")
                    }),
                }
                merge_count(d["obras"], "negaciones_recuperadas_por_forma", count_by_work(refs, unique_records=True))
        if group["clave_recuperacion"].startswith("excepcion::"):
            targets: dict[str, list[dict[str, Any]]] = defaultdict(list)
            for ref in refs:
                limited = ref.get("datos_documentales", {}).get("afirmacion_limitada_id")
                if not limited:
                    continue
                for key in assertion_to_keys.get((ref["obra_id"], limited), set()):
                    targets[key].append(ref)
            for key, matched in targets.items():
                handled = True
                d = dossiers[key]
                d["excepciones_vinculadas_a_predicaciones"][group["id"]] = {
                    "grupo_id": group["id"],
                    "criterio_vinculo": "afirmacion_limitada_id_documentado",
                    "conteos_por_obra": count_by_work(matched, unique_records=True),
                    "clasificaciones": sorted({
                        ref.get("datos_documentales", {}).get("clasificacion_excepcion")
                        for ref in matched
                        if ref.get("datos_documentales", {}).get("clasificacion_excepcion")
                    }),
                }
                merge_count(d["obras"], "excepciones_vinculadas_a_predicaciones", count_by_work(matched, unique_records=True))
        if not handled:
            groups_without_dossier["negaciones_excepciones_corpus"] += 1

    callbacks["negaciones_excepciones_corpus"] = neg_exc_cb

    def variants_cb(group: dict[str, Any]) -> None:
        targets: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for ref in group["registros"]:
            key = concept_source_to_key.get((ref["obra_id"], ref["registro_id"]))
            if key:
                targets[key].append(ref)
        if not targets:
            groups_without_dossier["variantes_terminologicas_corpus"] += 1
        for key, refs in targets.items():
            d = dossiers[key]
            d["variaciones_terminologicas"][group["id"]] = {
                "grupo_id": group["id"],
                "clave_lexica_recuperacion": group["clave_recuperacion"],
                "criterio_vinculo": "mismo_registro_conceptual_de_origen",
                "conteos_por_obra": count_by_work(refs, unique_records=True),
            }

    callbacks["variantes_terminologicas_corpus"] = variants_cb
    callbacks["distribucion_por_obra"] = lambda group: None

    def order_cb(group: dict[str, Any]) -> None:
        key = group["clave_recuperacion"]
        d = dossiers.get(key)
        if d is None:
            groups_without_dossier["orden_recurrencia"] += 1
            return
        d["fuentes_fase11"]["orden_recurrencia"] = group["id"]
        by_work: dict[str, int] = defaultdict(int)
        for ref in group["registros"]:
            total = ref.get("datos_documentales", {}).get("apariciones_totales")
            if not isinstance(total, int) or total < 0:
                raise SystemExit(f"apariciones_totales inválido en {group['id']}")
            by_work[ref["obra_id"]] += total
        merge_count(d["obras"], "apariciones_totales_documentadas", dict(by_work))

    callbacks["orden_recurrencia"] = order_cb

    for motor in EXPECTED_MOTORS:
        expected = by_motor[motor]
        path = args.fase11_dir / expected["ruta"]
        products.append(audit_product(path, motor, expected, masters, callbacks[motor]))

    args.salida_dir.mkdir(parents=True, exist_ok=True)
    dossiers_path = args.salida_dir / "expedientes-transversales.jsonl"
    h = hashlib.sha256()
    lines = 0
    with dossiers_path.open("wb") as f:
        for key in sorted(dossiers):
            record = finalize_dossier(dossiers[key])
            raw = canonical_bytes(record)
            f.write(raw)
            h.update(raw)
            lines += 1
    dossiers_sha = h.hexdigest()
    dossiers_path.with_name(dossiers_path.name + ".sha256").write_text(
        f"{dossiers_sha}  {dossiers_path.name}\n", encoding="utf-8"
    )

    audit = {
        "id": stable_id("F12AUD", {"cierre_f11": storage["gate"]["cierre_sha256"], "expedientes": dossiers_sha}),
        "tipo_registro": "auditoria_corpus",
        "schema_version": VERSION,
        "fase": 12,
        "version_auditor": VERSION,
        "fuente_exclusiva": "productos_comparativos_fase11_auditados",
        "origen_fase11": {
            "cierre_sha256": storage["gate"]["cierre_sha256"],
            "head_sha": storage["gate"]["head_sha"],
            "release_tag": storage["almacenamiento"]["release_tag"],
            "asset": storage["almacenamiento"]["asset"],
            "asset_sha256": storage["almacenamiento"]["asset_sha256"],
            "maestros": 20,
            "motores": 9,
        },
        "productos_auditados": sorted(products, key=lambda row: row["motor"]),
        "cobertura": {
            "motores_previstos": 9,
            "motores_auditados": len(products),
            "maestros_origen": 20,
            "expedientes_transversales": lines,
            "grupos_sin_expediente_conceptual_por_motor": dict(sorted(groups_without_dossier.items())),
        },
        "expedientes": {
            "ruta": dossiers_path.name,
            "sha256": dossiers_sha,
            "registros": lines,
        },
        "clausura_descriptiva": dict(CLAUSURA_F12),
        "estado_auditoria": "auditado",
    }
    audit_sha = write_json(args.salida_dir / "auditoria-corpus.json", audit)
    print(json.dumps({
        "fase": 12,
        "motores_auditados": len(products),
        "expedientes_transversales": lines,
        "expedientes_sha256": dossiers_sha,
        "auditoria_sha256": audit_sha,
    }, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
