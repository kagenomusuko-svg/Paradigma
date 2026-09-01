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

from consulta_literal_fase14 import canonical_bytes, execute_queries, sha256_file
from interfaz_ia_fase15 import (
    CLAUSURA_F15,
    RESTRICCIONES_RESPUESTA,
    build_packets,
    product_by_type,
    source_contract_f15,
    write_jsonl,
)


def write_json(path: Path, value: dict[str, Any]) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(value, f, ensure_ascii=False, sort_keys=True, indent=2)
        f.write("\n")
    digest = sha256_file(path)
    path.with_name(path.name + ".sha256").write_text(f"{digest}  {path.name}\n", encoding="utf-8")
    return digest


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for raw in f:
            if raw.strip():
                rows.append(json.loads(raw))
    return rows


def exact_contexts(conceptos_path: Path, responses: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    wanted: set[str] = set()
    for response in responses:
        for result in response.get("resultados", []):
            expediente = result.get("expediente_fase13_id")
            if isinstance(expediente, str) and expediente:
                wanted.add(expediente)
    found: dict[str, dict[str, Any]] = {}
    if not wanted:
        return found
    with conceptos_path.open("r", encoding="utf-8") as f:
        for raw in f:
            if not raw.strip():
                continue
            row = json.loads(raw)
            if row.get("id") in wanted:
                found[row["id"]] = {
                    "clave_recuperacion": row.get("clave_recuperacion"),
                    "hallazgos": row.get("hallazgos_auditoria", []),
                    "restricciones": row.get("restricciones", []),
                }
                if len(found) == len(wanted):
                    break
    if set(found) != wanted:
        raise SystemExit("F15 no pudo resolver todos los expedientes F13 referenciados por F14")
    return found


def validate_packet(
    packet: dict[str, Any],
    response: dict[str, Any],
    expected_context: dict[str, dict[str, Any]],
    validator: jsonschema.Draft202012Validator,
) -> tuple[int, int]:
    validator.validate(packet)
    if packet["solicitud"] != response["consulta"]:
        raise SystemExit("Paquete F15 alteró la solicitud F14")
    if packet["origen_fase14"]["respuesta_fase14_id"] != response["id"]:
        raise SystemExit("Paquete F15 perdió identidad de respuesta F14")
    if packet["origen_fase14"]["estado_respuesta_fase14"] != response["estado"]:
        raise SystemExit("Paquete F15 alteró estado F14")
    if packet["restricciones_respuesta"] != RESTRICCIONES_RESPUESTA:
        raise SystemExit("Paquete F15 no conserva restricciones de respuesta")
    if packet["clausura_descriptiva"] != CLAUSURA_F15:
        raise SystemExit("Paquete F15 no conserva clausura descriptiva")

    records = packet["registros_utilizados"]
    traces = packet["trazabilidad"]
    used_ids = packet["respuesta_controlada"]["registros_utilizados_ids"]
    if len(records) != len(response["resultados"]) or len(traces) != len(records) or len(used_ids) != len(records):
        raise SystemExit("F15 no expone exactamente los registros utilizados")
    if used_ids != [row["uso_id"] for row in records]:
        raise SystemExit("IDs de registros utilizados F15 divergentes")

    for result, record, trace in zip(response["resultados"], records, traces):
        ref = result["referencia"]
        if record["referencia"] != ref:
            raise SystemExit("F15 alteró una referencia F14")
        if record["texto_literal"] != ref.get("texto_literal"):
            raise SystemExit("F15 alteró texto literal")
        if record["estado_verificacion"] != "verificado" or record["estado_auditoria"] != "auditado":
            raise SystemExit("F15 emitió registro sin estados auditados")
        if trace["uso_id"] != record["uso_id"]:
            raise SystemExit("Traza F15 no apunta al registro utilizado")
        for field in ("obra_id", "registro_id", "fuente_id", "unidad_id", "localizacion"):
            if trace[field] != ref[field]:
                raise SystemExit(f"Traza F15 divergente en {field}")
        marker = f"[{record['uso_id']}] {record['texto_literal']}"
        if marker not in packet["respuesta_controlada"]["texto"]:
            raise SystemExit("Respuesta controlada F15 no muestra texto literal e ID de uso")

    for context in packet["hallazgos_auditoria"]:
        exp = context["expediente_fase13_id"]
        expected = expected_context.get(exp)
        if not expected:
            raise SystemExit("F15 añadió hallazgo sin expediente F13 referenciado")
        if context["clave_recuperacion"] != expected["clave_recuperacion"] or context["hallazgos"] != expected["hallazgos"]:
            raise SystemExit("F15 alteró hallazgos de auditoría F13")
    for context in packet["restricciones_documentales"]:
        exp = context["expediente_fase13_id"]
        expected = expected_context.get(exp)
        if not expected or context["restricciones"] != expected["restricciones"] or not expected["restricciones"]:
            raise SystemExit("F15 alteró restricciones documentales F13")

    if response["estado"] == "hallazgo_auditado":
        if packet["estado"] != "evidencia_disponible" or packet["motivo_abstencion"] is not None:
            raise SystemExit("F15 se abstuvo pese a evidencia F14 disponible")
        if packet["respuesta_controlada"]["modo"] != "extractiva_con_referencias":
            raise SystemExit("F15 no usa respuesta extractiva con evidencia")
        return len(records), 0

    if packet["estado"] != "abstencion" or packet["motivo_abstencion"] != response["estado"]:
        raise SystemExit("F15 no se abstuvo ante insuficiencia F14")
    if packet["respuesta_controlada"]["modo"] != "abstencion":
        raise SystemExit("F15 no marcó modo de abstención")
    if packet["respuesta_controlada"]["texto"] != response["mensaje"]:
        raise SystemExit("F15 alteró la respuesta negativa F14")
    if records or traces or used_ids:
        raise SystemExit("F15 inventó registros durante abstención")
    return 0, 1


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--fase13-dir", type=Path, required=True)
    p.add_argument("--almacenamiento-fase13", type=Path, required=True)
    p.add_argument("--fase14-dir", type=Path, required=True)
    p.add_argument("--almacenamiento-fase14", type=Path, required=True)
    p.add_argument("--salida-dir", type=Path, required=True)
    p.add_argument("--cierre", type=Path, required=True)
    p.add_argument("--schema-paquete", type=Path)
    args = p.parse_args()

    storage13, _, storage14, closure14 = source_contract_f15(
        args.fase13_dir, args.almacenamiento_fase13, args.fase14_dir, args.almacenamiento_fase14
    )
    sample_decl = product_by_type(storage14, "muestra_respuestas_consulta_literal")
    sample_path = args.fase14_dir / Path(sample_decl["ruta_en_zip"]).name
    sample_responses = read_jsonl(sample_path)
    if len(sample_responses) != storage14["gate"]["consultas_ejecutadas"]:
        raise SystemExit("Muestra F14 no coincide con gate persistido")
    queries = [row["consulta"] for row in sample_responses]

    fresh_responses = execute_queries(args.fase13_dir, args.almacenamiento_fase13, queries)
    if [canonical_bytes(x) for x in fresh_responses] != [canonical_bytes(x) for x in sample_responses]:
        raise SystemExit("F15 no reproduce exactamente las respuestas cerradas de Fase 14")

    packets = build_packets(
        args.fase13_dir,
        args.almacenamiento_fase13,
        args.fase14_dir,
        args.almacenamiento_fase14,
        queries,
    )
    schema_path = args.schema_paquete or SCHEMA_DIR / "paquete-interfaz-ia-fase15-v1.0.0.schema.json"
    validator = jsonschema.Draft202012Validator(json.loads(schema_path.read_text(encoding="utf-8")))
    contexts = exact_contexts(args.fase13_dir / "conceptos-maestro-corpus.jsonl", fresh_responses)

    records_total = 0
    abstentions = 0
    states: Counter[str] = Counter()
    for packet, response in zip(packets, fresh_responses):
        used, abstained = validate_packet(packet, response, contexts, validator)
        records_total += used
        abstentions += abstained
        states[packet["estado"]] += 1
    if records_total != storage14["gate"]["referencias_auditadas_verificadas_emitidas"]:
        raise SystemExit("F15 no conserva la cardinalidad de referencias emitidas por F14")
    if abstentions < 1 or states["evidencia_disponible"] < 1:
        raise SystemExit("F15 debe demostrar tanto respuesta con evidencia como abstención")

    args.salida_dir.mkdir(parents=True, exist_ok=True)
    packets_path = args.salida_dir / "muestra-paquetes-ia-fase15.jsonl"
    packets_sha = write_jsonl(packets_path, packets)

    with tempfile.TemporaryDirectory(prefix="fase15-repro-") as tmp:
        tmpdir = Path(tmp)
        batch = tmpdir / "consultas.jsonl"
        with batch.open("wb") as f:
            for query in queries:
                f.write(canonical_bytes(query))
        repro = tmpdir / "paquetes.jsonl"
        subprocess.run([
            sys.executable,
            str(MOTOR_DIR / "interfaz_ia_fase15.py"),
            "--fase13-dir", str(args.fase13_dir),
            "--almacenamiento-fase13", str(args.almacenamiento_fase13),
            "--fase14-dir", str(args.fase14_dir),
            "--almacenamiento-fase14", str(args.almacenamiento_fase14),
            "--lote", str(batch),
            "--salida", str(repro),
        ], check=True)
        if repro.read_bytes() != packets_path.read_bytes():
            raise SystemExit("Fase 15 no es reproducible byte a byte por su interfaz CLI")

    audit = {
        "version": "1.0.0",
        "fase": 15,
        "tipo_registro": "auditoria_interfaz_ia",
        "fuente_exclusiva": "respuestas_fase14_cerradas_y_contexto_fase13_auditado",
        "origen_fase14": {
            "cierre_sha256": storage14["gate"]["cierre_sha256"],
            "release_tag": storage14["almacenamiento"]["release_tag"],
            "asset": storage14["almacenamiento"]["asset"],
            "asset_sha256": storage14["almacenamiento"]["asset_sha256"],
            "consultas": closure14["consultas_ejecutadas"],
        },
        "origen_fase13": {
            "cierre_sha256": storage13["gate"]["cierre_sha256"],
            "release_tag": storage13["almacenamiento"]["release_tag"],
            "asset_sha256": storage13["almacenamiento"]["asset_sha256"],
        },
        "paquetes_generados": len(packets),
        "registros_utilizados_expuestos": records_total,
        "textos_literales_expuestos": records_total,
        "abstenciones": abstentions,
        "estados_paquete": dict(sorted(states.items())),
        "registros_utilizados_identificables": True,
        "abstencion_demostrada": True,
        "respuestas_fase14_reproducidas_exactamente": True,
        "reproducible_byte_a_byte": True,
        "restricciones_respuesta": dict(RESTRICCIONES_RESPUESTA),
        "paquetes_sha256": packets_sha,
        "clausura_descriptiva": dict(CLAUSURA_F15),
    }
    audit_path = args.salida_dir / "auditoria-interfaz-ia-fase15.json"
    audit_sha = write_json(audit_path, audit)

    closure15 = {
        "version": "1.0.0",
        "fase": 15,
        "fase15_cerrada": True,
        "criterio": "respuesta_generada_expone_registros_utilizados_y_se_abstiene_sin_evidencia_suficiente",
        "fuente_exclusiva": audit["fuente_exclusiva"],
        "origen_fase14": audit["origen_fase14"],
        "origen_fase13": audit["origen_fase13"],
        "paquetes_generados": len(packets),
        "registros_utilizados_expuestos": records_total,
        "abstenciones": abstentions,
        "paquetes_sha256": packets_sha,
        "auditoria_sha256": audit_sha,
        "reproducible_byte_a_byte": True,
        "registros_utilizados_identificables": True,
        "abstencion_demostrada": True,
        "clausura_descriptiva": dict(CLAUSURA_F15),
    }
    closure_sha = write_json(args.cierre, closure15)
    print(json.dumps({
        "fase": 15,
        "fase15_cerrada": True,
        "paquetes": len(packets),
        "registros_utilizados": records_total,
        "abstenciones": abstentions,
        "paquetes_sha256": packets_sha,
        "cierre_sha256": closure_sha,
    }, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
