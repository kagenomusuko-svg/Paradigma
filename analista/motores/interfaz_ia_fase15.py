#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Iterable

from consulta_literal_fase14 import canonical_bytes, execute_queries, sha256_file, source_contract

VERSION = "1.0.0"

RESTRICCIONES_RESPUESTA = {
    "usar_solo_registros_listados": True,
    "preservar_texto_literal": True,
    "preservar_estatus_enunciativo": True,
    "completar_lagunas": False,
    "reconciliar_formulaciones": False,
    "convertir_semejanza_en_equivalencia": False,
    "presentar_inferencias_como_corpus": False,
    "resolver_contradicciones": False,
    "abstenerse_sin_evidencia_suficiente": True,
}

CLAUSURA_F15 = {
    "solo_interfaz_documental": True,
    "generacion_doctrinal": False,
    "completar_lagunas": False,
    "reconciliar_formulaciones": False,
    "equivalencia_inferida": False,
    "complementariedad_inferida": False,
    "contradiccion_inferida": False,
    "sintesis_doctrinal": False,
    "presentar_inferencias_como_corpus": False,
    "resolucion_doctrinal": "no_realizada",
}


def stable_id(prefix: str, value: Any) -> str:
    return f"{prefix}-{hashlib.sha256(canonical_bytes(value)).hexdigest()[:12].upper()}"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def product_by_type(storage: dict[str, Any], product_type: str) -> dict[str, Any]:
    for row in storage.get("productos", []):
        if row.get("tipo") == product_type:
            return row
    raise SystemExit(f"Fase 14 no declara producto requerido: {product_type}")


def source_contract_f15(
    fase13_dir: Path,
    almacenamiento_fase13: Path,
    fase14_dir: Path,
    almacenamiento_fase14: Path,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any]]:
    storage13, closure13, master13 = source_contract(fase13_dir, almacenamiento_fase13)
    storage14 = load_json(almacenamiento_fase14)
    gate14 = storage14.get("gate", {})
    if storage14.get("fase") != 14 or gate14.get("fase14_cerrada") is not True:
        raise SystemExit("Fase 15 requiere Fase 14 cerrada")

    closure14_path = fase14_dir / "cierre-fase14.json"
    if not closure14_path.is_file() or sha256_file(closure14_path) != gate14.get("cierre_sha256"):
        raise SystemExit("Cierre F14 ausente o divergente")
    closure14 = load_json(closure14_path)
    if closure14.get("fase") != 14 or closure14.get("fase14_cerrada") is not True:
        raise SystemExit("Cierre F14 incompatible")
    if closure14.get("reproducible_byte_a_byte") is not True:
        raise SystemExit("Fase 15 requiere interfaz literal F14 reproducible")

    origin14 = storage14.get("origen_fase13", {})
    if origin14.get("cierre_sha256") != storage13.get("gate", {}).get("cierre_sha256"):
        raise SystemExit("Origen F13 declarado por F14 diverge del maestro restaurado")
    if origin14.get("maestro_id") != master13.get("id"):
        raise SystemExit("F14 y F13 divergen en maestro de corpus")

    sample_decl = product_by_type(storage14, "muestra_respuestas_consulta_literal")
    sample_path = fase14_dir / Path(sample_decl["ruta_en_zip"]).name
    if not sample_path.is_file() or sha256_file(sample_path) != sample_decl.get("sha256"):
        raise SystemExit("Muestra de respuestas F14 ausente o divergente")
    return storage13, closure13, storage14, closure14


def collect_context(
    conceptos_path: Path,
    responses: Iterable[dict[str, Any]],
) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    wanted_ids: set[str] = set()
    wanted_keys: set[str] = set()
    for response in responses:
        for result in response.get("resultados", []):
            expediente = result.get("expediente_fase13_id")
            if isinstance(expediente, str) and expediente:
                wanted_ids.add(expediente)
            key = result.get("clave_recuperacion")
            if isinstance(key, str) and key:
                wanted_keys.add(key)

    by_id: dict[str, dict[str, Any]] = {}
    by_key: dict[str, dict[str, Any]] = {}
    if not wanted_ids and not wanted_keys:
        return by_id, by_key
    with conceptos_path.open("r", encoding="utf-8") as f:
        for raw in f:
            if not raw.strip():
                continue
            row = json.loads(raw)
            rid = row.get("id")
            key = row.get("clave_recuperacion")
            if rid not in wanted_ids and key not in wanted_keys:
                continue
            context = {
                "expediente_fase13_id": rid,
                "clave_recuperacion": key,
                "hallazgos": row.get("hallazgos_auditoria", []),
                "restricciones": row.get("restricciones", []),
            }
            if isinstance(rid, str):
                by_id[rid] = context
            if isinstance(key, str):
                by_key[key] = context
            if wanted_ids.issubset(by_id) and wanted_keys.issubset(by_key):
                break
    return by_id, by_key


def use_record(result: dict[str, Any]) -> dict[str, Any]:
    ref = result.get("referencia")
    if not isinstance(ref, dict):
        raise SystemExit("Resultado F14 sin referencia documental")
    if ref.get("estado_verificacion") != "verificado" or ref.get("estado_auditoria") != "auditado":
        raise SystemExit("F15 rechazó referencia no verificada/auditada")
    for field in ("obra_id", "registro_id", "fuente_id", "unidad_id", "localizacion", "texto_literal"):
        if ref.get(field) in (None, "", {}):
            raise SystemExit(f"F15 requiere referencia completa con {field}")
    literal = ref["texto_literal"]
    if not isinstance(literal, str) or not literal.strip():
        raise SystemExit("F15 requiere texto literal no vacío")
    usage_id = stable_id("F15U", {
        "tipo": result.get("tipo_hallazgo"),
        "clave": result.get("clave_recuperacion"),
        "obra": ref["obra_id"],
        "registro": ref["registro_id"],
        "grupo": result.get("grupo_id") or result.get("grupo_fase11_id"),
    })
    metadata = {k: v for k, v in result.items() if k not in {"referencia", "tipo_hallazgo", "clave_recuperacion"}}
    return {
        "uso_id": usage_id,
        "registro_documental_id": f"{ref['obra_id']}:{ref['registro_id']}",
        "tipo_hallazgo": result.get("tipo_hallazgo"),
        "clave_recuperacion": result.get("clave_recuperacion", ""),
        "texto_literal": literal,
        "estatus_enunciativo": ref.get("estatus_enunciativo"),
        "estado_verificacion": "verificado",
        "estado_auditoria": "auditado",
        "referencia": ref,
        "metadatos_recuperacion": metadata,
    }


def relevant_contexts(
    response: dict[str, Any],
    by_id: dict[str, dict[str, Any]],
    by_key: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    seen: set[str] = set()
    rows: list[dict[str, Any]] = []
    for result in response.get("resultados", []):
        context = None
        expediente = result.get("expediente_fase13_id")
        if isinstance(expediente, str):
            context = by_id.get(expediente)
        if context is None:
            key = result.get("clave_recuperacion")
            if isinstance(key, str):
                context = by_key.get(key)
        if not context:
            continue
        cid = context.get("expediente_fase13_id") or context.get("clave_recuperacion")
        if cid in seen:
            continue
        seen.add(str(cid))
        rows.append(context)
    return sorted(rows, key=lambda x: (x.get("clave_recuperacion") or "", x.get("expediente_fase13_id") or ""))


def packet_from_response(
    response: dict[str, Any],
    storage14: dict[str, Any],
    contexts_by_id: dict[str, dict[str, Any]],
    contexts_by_key: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    if response.get("tipo_registro") != "respuesta_consulta_literal" or response.get("fase") != 14:
        raise SystemExit("F15 sólo acepta respuestas literales F14")
    records = [use_record(row) for row in response.get("resultados", [])]
    if response.get("conteo_resultados") != len(records):
        raise SystemExit("F15 detectó conteo F14 divergente")

    contexts = relevant_contexts(response, contexts_by_id, contexts_by_key)
    findings = [
        {
            "expediente_fase13_id": c["expediente_fase13_id"],
            "clave_recuperacion": c["clave_recuperacion"],
            "hallazgos": c["hallazgos"],
        }
        for c in contexts
    ]
    documentary_restrictions = [
        {
            "expediente_fase13_id": c["expediente_fase13_id"],
            "clave_recuperacion": c["clave_recuperacion"],
            "restricciones": c["restricciones"],
        }
        for c in contexts if c["restricciones"]
    ]

    if response.get("estado") == "hallazgo_auditado":
        if not records:
            raise SystemExit("F15 recibió hallazgo F14 sin registros")
        state = "evidencia_disponible"
        reason = None
        mode = "extractiva_con_referencias"
        text = "Evidencia auditada recuperada:\n" + "\n".join(
            f"[{row['uso_id']}] {row['texto_literal']}" for row in records
        )
    else:
        if records:
            raise SystemExit("F15 no puede abstenerse conservando registros como evidencia suficiente")
        if response.get("estado") not in {"sin_hallazgo_auditado", "no_determinado_por_el_corpus"}:
            raise SystemExit(f"Estado F14 no soportado por F15: {response.get('estado')}")
        message = response.get("mensaje")
        if not isinstance(message, str) or not message:
            raise SystemExit("Abstención F15 requiere mensaje negativo F14")
        state = "abstencion"
        reason = response["estado"]
        mode = "abstencion"
        text = message

    storage_info = storage14.get("almacenamiento", {})
    packet = {
        "id": stable_id("F15P", {"respuesta_f14": response["id"], "cierre_f14": storage14["gate"]["cierre_sha256"]}),
        "tipo_registro": "paquete_interfaz_ia",
        "schema_version": VERSION,
        "fase": 15,
        "solicitud": response["consulta"],
        "origen_fase14": {
            "cierre_sha256": storage14["gate"]["cierre_sha256"],
            "release_tag": storage_info.get("release_tag"),
            "asset_sha256": storage_info.get("asset_sha256"),
            "respuesta_fase14_id": response["id"],
            "estado_respuesta_fase14": response["estado"],
        },
        "estado": state,
        "motivo_abstencion": reason,
        "respuesta_controlada": {
            "modo": mode,
            "texto": text,
            "registros_utilizados_ids": [row["uso_id"] for row in records],
        },
        "registros_utilizados": records,
        "hallazgos_auditoria": findings,
        "restricciones_documentales": documentary_restrictions,
        "restricciones_respuesta": dict(RESTRICCIONES_RESPUESTA),
        "trazabilidad": [
            {
                "uso_id": row["uso_id"],
                "obra_id": row["referencia"]["obra_id"],
                "registro_id": row["referencia"]["registro_id"],
                "fuente_id": row["referencia"]["fuente_id"],
                "unidad_id": row["referencia"]["unidad_id"],
                "localizacion": row["referencia"]["localizacion"],
            }
            for row in records
        ],
        "clausura_descriptiva": dict(CLAUSURA_F15),
    }
    return packet


def build_packets(
    fase13_dir: Path,
    almacenamiento_fase13: Path,
    fase14_dir: Path,
    almacenamiento_fase14: Path,
    raw_queries: Iterable[dict[str, Any]],
) -> list[dict[str, Any]]:
    _, _, storage14, _ = source_contract_f15(
        fase13_dir, almacenamiento_fase13, fase14_dir, almacenamiento_fase14
    )
    queries = list(raw_queries)
    responses = execute_queries(fase13_dir, almacenamiento_fase13, queries)
    by_id, by_key = collect_context(fase13_dir / "conceptos-maestro-corpus.jsonl", responses)
    return [packet_from_response(r, storage14, by_id, by_key) for r in responses]


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
                    raise SystemExit(f"JSON inválido en solicitud {path}:{line_no}: {exc}") from exc
    return rows


def main() -> int:
    p = argparse.ArgumentParser(description="Interfaz documental F15 para sistemas de IA")
    p.add_argument("--fase13-dir", type=Path, required=True)
    p.add_argument("--almacenamiento-fase13", type=Path, required=True)
    p.add_argument("--fase14-dir", type=Path, required=True)
    p.add_argument("--almacenamiento-fase14", type=Path, required=True)
    source = p.add_mutually_exclusive_group(required=True)
    source.add_argument("--consulta-json")
    source.add_argument("--lote", type=Path)
    p.add_argument("--salida", type=Path)
    args = p.parse_args()

    queries = [json.loads(args.consulta_json)] if args.consulta_json else read_batch(args.lote)
    packets = build_packets(
        args.fase13_dir,
        args.almacenamiento_fase13,
        args.fase14_dir,
        args.almacenamiento_fase14,
        queries,
    )
    if args.salida:
        digest = write_jsonl(args.salida, packets)
        print(json.dumps({"fase": 15, "paquetes": len(packets), "sha256": digest}, ensure_ascii=False, sort_keys=True))
    else:
        for packet in packets:
            sys.stdout.buffer.write(canonical_bytes(packet))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
