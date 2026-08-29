#!/usr/bin/env python3
"""Ensamblador descriptivo del expediente maestro — Fase 9.

No extrae, normaliza ni reinterpreta doctrina. Reúne únicamente productos ya
verificados/auditados, cobertura y calibración cerrada. Rechaza referencias
rotas o entradas no auditadas y registra SHA-256 de cada archivo de insumo.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PILOTO_ID = "AA-SP-V1"
MASTER_VERSION = "1.1.0"
MOTOR_VERSION = "1.0.0"

AUDITED_FILES = {
    "apariciones_conceptuales": "apariciones-conceptuales.jsonl",
    "conceptos": "conceptos.jsonl",
    "definiciones": "definiciones.jsonl",
    "afirmaciones": "afirmaciones-candidatas.jsonl",
    "formulas": "formulas-candidatas.jsonl",
    "relaciones_explicitas": "relaciones-explicitas.jsonl",
    "distinciones": "distinciones.jsonl",
    "negaciones": "negaciones.jsonl",
    "excepciones": "excepciones.jsonl",
    "restricciones_alcance": "restricciones-alcance.jsonl",
}
COVERAGE_FILES = (
    "cobertura-unidades.jsonl",
    "cobertura-conceptos.jsonl",
    "cobertura-definiciones.jsonl",
    "cobertura-afirmaciones.jsonl",
    "cobertura-formulas.jsonl",
    "cobertura-relaciones.jsonl",
    "cobertura-limitadores.jsonl",
)
EXPECTED_COVERAGE_MOTORS = {
    "unidades", "conceptos_apariciones", "definiciones", "afirmaciones",
    "formulas", "relaciones_explicitas", "limitadores",
}
CALIBRATION_MOTORS = {
    "conceptos_apariciones", "definiciones", "afirmaciones", "formulas",
    "relaciones_explicitas", "limitadores",
}


def load_jsonl(path: Path) -> list[dict]:
    if not path.is_file():
        raise SystemExit(f"Insumo inexistente: {path}")
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def load_json(path: Path) -> dict:
    if not path.is_file():
        raise SystemExit(f"Insumo inexistente: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        return path.resolve().as_posix()


def metric_consistent(row: dict) -> bool:
    fields = ("positivos_esperados", "predicciones_emitidas", "verdaderos_positivos", "falsos_positivos", "falsos_negativos")
    if any(not isinstance(row.get(field), int) or isinstance(row.get(field), bool) or row[field] < 0 for field in fields):
        return False
    return (
        row["positivos_esperados"] == row["verdaderos_positivos"] + row["falsos_negativos"]
        and row["predicciones_emitidas"] == row["verdaderos_positivos"] + row["falsos_positivos"]
    )


def validate_traceability(master: dict) -> None:
    if master.get("obra_id") != PILOTO_ID:
        raise AssertionError("Maestro de obra incorrecta")
    sources = {row["id"]: row for row in master["fuentes"]}
    if set(sources) != {PILOTO_ID}:
        raise AssertionError("El maestro piloto debe contener solo su fuente canónica")
    units = {row["id"]: row for row in master["unidades"]}
    if not units or any(row.get("fuente_id") != PILOTO_ID for row in units.values()):
        raise AssertionError("Unidad fuera de la fuente piloto")

    arrays = [master[name] for name in AUDITED_FILES]
    records = [row for rows in arrays for row in rows]
    ids = [row["id"] for row in records]
    if len(ids) != len(set(ids)):
        raise AssertionError("ID duplicado entre productos auditados")
    by_id = {row["id"]: row for row in records}
    appearances = {row["id"]: row for row in master["apariciones_conceptuales"]}
    concepts = {row["id"]: row for row in master["conceptos"]}
    assertions = {row["id"]: row for row in master["afirmaciones"]}

    for row in records:
        if row.get("estado_verificacion") != "verificado" or row.get("estado_auditoria") != "auditado":
            raise AssertionError(f"Registro no sellado antes del maestro: {row.get('id')}")
        uid = row.get("unidad_id")
        if uid is not None:
            if uid not in units or units[uid]["fuente_id"] != PILOTO_ID:
                raise AssertionError(f"Unidad rota en {row['id']}")
        sid = row.get("fuente_id")
        if sid is not None and sid != PILOTO_ID:
            raise AssertionError(f"Fuente rota en {row['id']}")

        kind = row["tipo_registro"]
        if kind == "aparicion_conceptual":
            cid = row.get("concepto_id")
            if cid is not None and cid not in concepts:
                raise AssertionError(f"Concepto inexistente en {row['id']}")
        elif kind == "concepto":
            if any(aid not in appearances for aid in row.get("aparicion_ids", [])):
                raise AssertionError(f"Aparición inexistente en {row['id']}")
            if any(aid not in row.get("aparicion_ids", []) for aid in row.get("evidencia_identidad_ids", [])):
                raise AssertionError(f"Evidencia conceptual fuera de apariciones en {row['id']}")
        elif kind == "definicion":
            if row.get("concepto_id") not in concepts:
                raise AssertionError(f"Definición sin concepto: {row['id']}")
        elif kind == "afirmacion":
            if any(cid not in concepts for cid in row.get("concepto_ids", [])):
                raise AssertionError(f"Afirmación con concepto inexistente: {row['id']}")
        elif kind == "formula":
            if row.get("unidad_id") not in row.get("contexto_unidad_ids", []):
                raise AssertionError(f"Fórmula sin unidad ancla: {row['id']}")
            if any(uid not in units for uid in row.get("contexto_unidad_ids", [])):
                raise AssertionError(f"Fórmula con contexto inexistente: {row['id']}")
        elif kind == "relacion_explicita":
            if row.get("sujeto_ref") not in concepts or row.get("objeto_ref") not in concepts:
                raise AssertionError(f"Relación con referente inexistente: {row['id']}")
        elif kind in {"excepcion", "restriccion_alcance"}:
            aid = row.get("afirmacion_limitada_id")
            if aid is not None and aid not in assertions:
                raise AssertionError(f"Limitador con afirmación inexistente: {row['id']}")

    for finding in master["hallazgos_auditoria"]:
        if finding.get("estado_verificacion") != "verificado" or finding.get("estado_auditoria") != "auditado":
            raise AssertionError(f"Hallazgo no auditado: {finding.get('id')}")
        if any(rid not in by_id and rid not in concepts for rid in finding.get("registro_ids", [])):
            raise AssertionError(f"Hallazgo con referencia inexistente: {finding['id']}")
        if finding.get("resolucion_doctrinal") != "no_realizada":
            raise AssertionError(f"Hallazgo con resolución doctrinal: {finding['id']}")

    coverage = master["reportes_cobertura"]
    if {row["motor"] for row in coverage} != EXPECTED_COVERAGE_MOTORS:
        raise AssertionError("Cobertura incompleta de motores")
    for row in coverage:
        if row.get("obra_id") != PILOTO_ID or row.get("unidades_procesadas") != 836:
            raise AssertionError(f"Cobertura ajena o incompleta: {row.get('id')}")
        if row.get("unidades_omitidas") or row.get("errores"):
            raise AssertionError(f"Cobertura con omisiones/errores: {row.get('id')}")

    metrics = master["metricas_calibracion"]["reportes"]
    required = {(motor, stratum) for motor in CALIBRATION_MOTORS for stratum in ("general", "desafio")}
    available = {(row.get("motor"), row.get("estrato")) for row in metrics}
    if not required <= available or any(not metric_consistent(row) for row in metrics):
        raise AssertionError("Métricas de calibración incompletas o inconsistentes")
    closure = master["cierre_calibracion"]
    if closure.get("cierre_cuantitativo") is not True or closure.get("obra_id") != PILOTO_ID:
        raise AssertionError("Fase 8 no está cerrada cuantitativamente")
    detail = {(row.get("motor"), row.get("estrato")): row for row in closure.get("detalle", [])}
    if not required <= set(detail):
        raise AssertionError("Gate de calibración incompleto")
    allowed = {"cumple", "cumple_control_negativo"}
    if any(detail[key].get("estado") not in allowed for key in required):
        raise AssertionError("Algún motor no supera el gate de Fase 8")


def history(records: list[dict]) -> list[dict]:
    pairs = sorted({(row["producido_por"]["motor"], row["producido_por"]["version"]) for row in records if row.get("producido_por")})
    result = [
        {"version": f"{motor}/{version}", "descripcion": "Versión declarada por un producto incluido en el expediente."}
        for motor, version in pairs
    ]
    extras = [
        ("normalizacion/1.0.0", "Overlay de recuperación aplicado sin alterar IDs ni productor original."),
        ("calibracion/1.1.0", "Patrón de oro y métricas de Fase 8."),
        ("umbrales/1.1.0", "Umbrales de producción aplicados por el gate de Fase 8."),
        ("expediente-maestro/1.1.0", "Contrato del maestro piloto de Fase 9."),
        ("ensamblador_maestro/1.0.0", "Ensamblador descriptivo de Fase 9."),
    ]
    seen = {row["version"] for row in result}
    for version, description in extras:
        if version not in seen:
            result.append({"version": version, "descripcion": description})
    return sorted(result, key=lambda row: row["version"])


def assemble(generated: Path, output: Path) -> dict:
    audited_root = generated / "auditados"
    source_path = generated / "fuentes.jsonl"
    units_path = generated / "unidades.jsonl"
    source_rows = [row for row in load_jsonl(source_path) if row["id"] == PILOTO_ID]
    if len(source_rows) != 1:
        raise AssertionError("Fuente piloto ausente o duplicada")
    unit_rows = [row for row in load_jsonl(units_path) if row.get("fuente_id") == PILOTO_ID]
    unit_rows.sort(key=lambda row: row["orden_textual"])

    arrays: dict[str, list[dict]] = {}
    input_specs: list[tuple[Path, str, int]] = [
        (source_path, "fuente", len(source_rows)),
        (units_path, "unidades", len(unit_rows)),
    ]
    for field, filename in AUDITED_FILES.items():
        path = audited_root / filename
        rows = load_jsonl(path)
        arrays[field] = rows
        input_specs.append((path, "producto_auditado", len(rows)))

    findings_path = generated / "hallazgos-auditoria.jsonl"
    findings = load_jsonl(findings_path)
    input_specs.append((findings_path, "hallazgos", len(findings)))

    coverage: list[dict] = []
    for filename in COVERAGE_FILES:
        path = generated / filename
        selected = [row for row in load_jsonl(path) if row.get("obra_id") == PILOTO_ID]
        if len(selected) != 1:
            raise AssertionError(f"Cobertura piloto ausente/duplicada: {filename}")
        coverage.extend(selected)
        input_specs.append((path, "cobertura", 1))

    calibration_path = generated / "reporte-calibracion.json"
    calibration = load_json(calibration_path)
    calibration_rows = calibration.get("reportes", [])
    input_specs.append((calibration_path, "calibracion", len(calibration_rows)))
    closure_path = generated / "cierre-fase8.json"
    closure = load_json(closure_path)
    input_specs.append((closure_path, "calibracion", 1))
    thresholds_path = ROOT / "analista/calibracion/umbrales-v1.1.0.json"
    input_specs.append((thresholds_path, "umbrales", 1))

    all_versioned = source_rows + unit_rows + [row for rows in arrays.values() for row in rows] + findings + coverage
    master = {
        "id": "MAE-AA-SP-V1",
        "tipo_registro": "expediente_maestro_obra",
        "schema_version": MASTER_VERSION,
        "texto_literal": None,
        "normalizacion_formal": None,
        "normalizacion_lexica": None,
        "estatus_enunciativo": None,
        "estado_extraccion": "extraido",
        "estado_verificacion": "verificado",
        "estado_auditoria": "no_aplica",
        "producido_por": {"motor": "ensamblador_maestro", "version": MOTOR_VERSION},
        "obra_id": PILOTO_ID,
        "titulo": source_rows[0]["titulo"],
        "fuentes": source_rows,
        "unidades": unit_rows,
        **arrays,
        "hallazgos_auditoria": findings,
        "reportes_cobertura": sorted(coverage, key=lambda row: row["motor"]),
        "metricas_calibracion": {"version": "1.1.0", "reportes": calibration_rows},
        "cierre_calibracion": closure,
        "trazabilidad_archivos": sorted(
            [
                {
                    "ruta": relative(path),
                    "sha256": sha256_file(path),
                    "funcion": function,
                    "registros_incluidos": count,
                }
                for path, function, count in input_specs
            ],
            key=lambda row: row["ruta"],
        ),
        "historial_versiones": history(all_versioned),
    }
    validate_traceability(master)
    output.parent.mkdir(parents=True, exist_ok=True)
    payload = (json.dumps(master, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
    output.write_bytes(payload)
    digest = hashlib.sha256(payload).hexdigest()
    output.with_suffix(output.suffix + ".sha256").write_text(f"{digest}  {output.name}\n", encoding="utf-8")
    return master


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--generated", type=Path, default=ROOT / "analista/generado")
    parser.add_argument("--output", type=Path, default=ROOT / "analista/generado/maestros/AA-SP-V1.json")
    args = parser.parse_args()
    master = assemble(args.generated, args.output)
    counts = {field: len(master[field]) for field in AUDITED_FILES}
    print(json.dumps({"obra_id": PILOTO_ID, "unidades": len(master["unidades"]), "hallazgos": len(master["hallazgos_auditoria"]), "registros_auditados": sum(counts.values()), "conteos": counts}, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
