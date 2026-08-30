#!/usr/bin/env python3
"""Ensamblador descriptivo de un maestro independiente — Fase 10.

Opera exclusivamente sobre productos de una sola obra que ya pasaron
normalización de recuperación, verificación de evidencia y auditoría intraobra.
No compara obras, no sintetiza doctrina y no introduce registros nuevos.

El maestro transporta además el alcance conceptual declarado por el manifest de
la propia obra. Esto evita que una etapa posterior interprete un conjunto vacío
como ausencia semántica cuando la extracción conceptual no estuvo habilitada por
falta de glosario técnico explícito.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_VERSION = "1.3.0"
MOTOR_VERSION = "1.1.0"

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
    "cobertura-conceptos.jsonl",
    "cobertura-definiciones.jsonl",
    "cobertura-afirmaciones.jsonl",
    "cobertura-formulas.jsonl",
    "cobertura-relaciones.jsonl",
    "cobertura-limitadores.jsonl",
)
EXPECTED_COVERAGE_MOTORS = {
    "conceptos_apariciones",
    "definiciones",
    "afirmaciones",
    "formulas",
    "relaciones_explicitas",
    "limitadores",
}
CONCEPTUAL_FIELDS = (
    "apariciones_conceptuales",
    "conceptos",
    "definiciones",
    "relaciones_explicitas",
)


def load_jsonl(path: Path) -> list[dict]:
    if not path.is_file():
        raise SystemExit(f"Insumo inexistente: {path}")
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line
    ]


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


def comparable_chain_rows(rows: list[dict]) -> list[tuple[str, str]]:
    return [(row["id"], row["tipo_registro"]) for row in rows]


def conceptual_scope_from_manifest(manifest: dict) -> dict:
    profile = manifest.get("perfil_conceptual")
    glossary = manifest.get("glosario_tecnico")
    limitations = manifest.get("limitaciones_conceptuales")
    if not isinstance(limitations, dict):
        raise AssertionError("Manifest sin limitaciones conceptuales explícitas")

    expected_common = {
        "identidades_conceptuales_inferidas": False,
        "glosario_interobra_reutilizado": False,
        "interpretacion_cero_registros": "no_autoriza_afirmar_ausencia_semantica",
    }
    for key, expected in expected_common.items():
        if limitations.get(key) != expected:
            raise AssertionError(f"Limitación conceptual inválida en manifest: {key}")

    enabled = limitations.get("extraccion_conceptual_habilitada")
    if profile == "glosario_tecnico_explicito":
        if not isinstance(glossary, str) or not glossary or enabled is not True:
            raise AssertionError("Perfil conceptual con glosario inconsistente")
    elif profile == "sin_glosario_tecnico_explicito":
        if glossary is not None or enabled is not False:
            raise AssertionError("Perfil conceptual sin glosario inconsistente")
    else:
        raise AssertionError(f"Perfil conceptual no autorizado: {profile!r}")

    allowed_keys = {
        "extraccion_conceptual_habilitada",
        "identidades_conceptuales_inferidas",
        "glosario_interobra_reutilizado",
        "interpretacion_cero_registros",
    }
    if set(limitations) != allowed_keys:
        raise AssertionError("Manifest contiene campos conceptuales no autorizados")

    return {
        "perfil": profile,
        "glosario_tecnico": glossary,
        "extraccion_conceptual_habilitada": enabled,
        **expected_common,
    }


def validate_traceability(master: dict) -> None:
    obra_id = master.get("obra_id")
    if not isinstance(obra_id, str) or not obra_id:
        raise AssertionError("Maestro sin obra_id")

    sources = {row["id"]: row for row in master["fuentes"]}
    if set(sources) != {obra_id}:
        raise AssertionError("El maestro debe contener solo la fuente de su obra")

    units = {row["id"]: row for row in master["unidades"]}
    if not units or any(row.get("fuente_id") != obra_id for row in units.values()):
        raise AssertionError("Unidad fuera de la obra del maestro")

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
        if uid is not None and (uid not in units or units[uid]["fuente_id"] != obra_id):
            raise AssertionError(f"Unidad rota en {row['id']}")
        sid = row.get("fuente_id")
        if sid is not None and sid != obra_id:
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
        raise AssertionError("Cobertura incompleta de motores Fase 10")
    total_units = len(units)
    for row in coverage:
        if row.get("obra_id") != obra_id:
            raise AssertionError(f"Cobertura de otra obra: {row.get('id')}")
        if row.get("unidades_totales") != total_units or row.get("unidades_procesadas") != total_units:
            raise AssertionError(f"Cobertura incompleta: {row.get('id')}")
        if row.get("unidades_omitidas") or row.get("errores"):
            raise AssertionError(f"Cobertura con omisiones/errores: {row.get('id')}")

    controls = master["controles_fase10"]
    if controls.get("version") != "1.1.0":
        raise AssertionError("Versión de controles Fase 10 no autorizada")
    if controls.get("obra_id") != obra_id or controls.get("fase") != 10:
        raise AssertionError("Controles Fase 10 ajenos a la obra")
    if controls.get("comparacion_interobra") is not False:
        raise AssertionError("Fase 10 no permite comparación interobra")
    for key in (
        "maestro_independiente",
        "normalizacion_recuperacion",
        "verificacion_evidencia",
        "auditoria_intraobra",
    ):
        if controls.get(key) is not True:
            raise AssertionError(f"Control Fase 10 no satisfecho: {key}")

    scope = controls.get("alcance_conceptual")
    if not isinstance(scope, dict):
        raise AssertionError("Maestro sin alcance conceptual explícito")
    if scope.get("identidades_conceptuales_inferidas") is not False:
        raise AssertionError("El maestro no puede declarar identidades conceptuales inferidas")
    if scope.get("glosario_interobra_reutilizado") is not False:
        raise AssertionError("El maestro no puede reutilizar glosarios interobra")
    if scope.get("interpretacion_cero_registros") != "no_autoriza_afirmar_ausencia_semantica":
        raise AssertionError("El maestro debe preservar la semántica conservadora de cero registros")
    profile = scope.get("perfil")
    enabled = scope.get("extraccion_conceptual_habilitada")
    glossary = scope.get("glosario_tecnico")
    if profile == "sin_glosario_tecnico_explicito":
        if enabled is not False or glossary is not None:
            raise AssertionError("Alcance conceptual sin glosario inconsistente")
        if any(master[field] for field in CONCEPTUAL_FIELDS):
            raise AssertionError("Obra sin glosario contiene productos de identidad conceptual")
    elif profile == "glosario_tecnico_explicito":
        if enabled is not True or not isinstance(glossary, str) or not glossary:
            raise AssertionError("Alcance conceptual con glosario inconsistente")
    else:
        raise AssertionError("Perfil conceptual del maestro no autorizado")


def history(records: list[dict]) -> list[dict]:
    pairs = sorted(
        {
            (row["producido_por"]["motor"], row["producido_por"]["version"])
            for row in records
            if row.get("producido_por")
        }
    )
    result = [
        {
            "version": f"{motor}/{version}",
            "descripcion": "Versión declarada por un producto incluido en el expediente.",
        }
        for motor, version in pairs
    ]
    extras = [
        (
            "normalizacion/1.0.0",
            "Overlay de recuperación aplicado sin alterar evidencia ni productor original.",
        ),
        (
            "expediente-maestro-fase10/1.3.0",
            "Contrato de maestro independiente que conserva el alcance conceptual de la obra.",
        ),
        (
            "ensamblador_maestro_obra_fase10/1.1.0",
            "Ensamblador descriptivo parametrizado por obra; transporta limitaciones conceptuales y no compara ni sintetiza.",
        ),
    ]
    seen = {row["version"] for row in result}
    for version, description in extras:
        if version not in seen:
            result.append({"version": version, "descripcion": description})
    return sorted(result, key=lambda row: row["version"])


def assemble(obra_id: str, obra_root: Path, output: Path) -> dict:
    obra_root = obra_root.resolve()
    source_path = obra_root / "fuente.jsonl"
    units_path = obra_root / "unidades.jsonl"
    manifest_path = obra_root / "manifest-extractores.json"
    manifest = load_json(manifest_path)
    if manifest.get("obra_id") != obra_id:
        raise AssertionError("Manifest de extractores corresponde a otra obra")
    if manifest.get("comparacion_interobra") is not False:
        raise AssertionError("Manifest de Fase 10 habilita comparación interobra")
    scope = conceptual_scope_from_manifest(manifest)

    source_rows = [row for row in load_jsonl(source_path) if row.get("id") == obra_id]
    if len(source_rows) != 1:
        raise AssertionError("Fuente de obra ausente o duplicada")
    unit_rows = [row for row in load_jsonl(units_path) if row.get("fuente_id") == obra_id]
    if not unit_rows:
        raise AssertionError("Obra sin unidades")
    unit_rows.sort(key=lambda row: row["orden_textual"])

    input_specs: list[tuple[Path, str, int]] = [
        (source_path, "fuente", len(source_rows)),
        (units_path, "unidades", len(unit_rows)),
        (manifest_path, "manifest", 1),
    ]

    audited_root = obra_root / "auditados"
    normalized_root = obra_root / "normalizados"
    verified_root = obra_root / "verificados"
    arrays: dict[str, list[dict]] = {}
    for field, filename in AUDITED_FILES.items():
        normalized_path = normalized_root / filename
        verified_path = verified_root / filename
        audited_path = audited_root / filename
        normalized = load_jsonl(normalized_path)
        verified = load_jsonl(verified_path)
        audited = load_jsonl(audited_path)
        if comparable_chain_rows(normalized) != comparable_chain_rows(verified):
            raise AssertionError(f"Verificación cambió identidad/orden de registros: {filename}")
        if comparable_chain_rows(verified) != comparable_chain_rows(audited):
            raise AssertionError(f"Auditoría cambió identidad/orden de registros: {filename}")
        arrays[field] = audited
        input_specs.extend(
            [
                (normalized_path, "producto_normalizado", len(normalized)),
                (verified_path, "producto_verificado", len(verified)),
                (audited_path, "producto_auditado", len(audited)),
            ]
        )

    if scope["perfil"] == "sin_glosario_tecnico_explicito" and any(
        arrays[field] for field in CONCEPTUAL_FIELDS
    ):
        raise AssertionError("Manifest sin glosario no puede ensamblar productos conceptuales")

    findings_path = obra_root / "hallazgos-auditoria.jsonl"
    findings = load_jsonl(findings_path)
    input_specs.append((findings_path, "hallazgos", len(findings)))

    coverage: list[dict] = []
    for filename in COVERAGE_FILES:
        path = obra_root / filename
        selected = [row for row in load_jsonl(path) if row.get("obra_id") == obra_id]
        if len(selected) != 1:
            raise AssertionError(f"Cobertura ausente/duplicada: {filename}")
        coverage.extend(selected)
        input_specs.append((path, "cobertura", 1))

    formula_calibration = manifest.get("calibracion", {}).get("formulas", {})
    profile_path_text = formula_calibration.get("perfil")
    if profile_path_text:
        profile_path = ROOT / profile_path_text
        if not profile_path.is_file():
            raise AssertionError("Perfil de calibración de fórmulas ausente")
        declared_hash = formula_calibration.get("perfil_sha256")
        if declared_hash != sha256_file(profile_path):
            raise AssertionError("Hash de perfil de calibración de fórmulas no coincide")
        input_specs.append((profile_path, "calibracion_obra", 1))

    all_versioned = (
        source_rows
        + unit_rows
        + [row for rows in arrays.values() for row in rows]
        + findings
        + coverage
    )
    master = {
        "id": f"MAE-{obra_id}",
        "tipo_registro": "expediente_maestro_obra",
        "schema_version": SCHEMA_VERSION,
        "texto_literal": None,
        "normalizacion_formal": None,
        "normalizacion_lexica": None,
        "estatus_enunciativo": None,
        "estado_extraccion": "extraido",
        "estado_verificacion": "verificado",
        "estado_auditoria": "no_aplica",
        "producido_por": {
            "motor": "ensamblador_maestro_obra_fase10",
            "version": MOTOR_VERSION,
        },
        "obra_id": obra_id,
        "titulo": source_rows[0]["titulo"],
        "fuentes": source_rows,
        "unidades": unit_rows,
        **arrays,
        "hallazgos_auditoria": findings,
        "reportes_cobertura": sorted(coverage, key=lambda row: row["motor"]),
        "controles_fase10": {
            "version": "1.1.0",
            "obra_id": obra_id,
            "fase": 10,
            "comparacion_interobra": False,
            "maestro_independiente": True,
            "normalizacion_recuperacion": True,
            "verificacion_evidencia": True,
            "auditoria_intraobra": True,
            "alcance_conceptual": scope,
            "calibracion_formulas": {
                "perfil_calibrado": bool(formula_calibration.get("perfil_calibrado", False)),
                "version_produccion": formula_calibration.get("version_produccion"),
                "perfil": profile_path_text,
                "perfil_sha256": formula_calibration.get("perfil_sha256"),
            },
        },
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
    payload = (
        json.dumps(master, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        + "\n"
    ).encode("utf-8")
    output.write_bytes(payload)
    digest = hashlib.sha256(payload).hexdigest()
    output.with_suffix(output.suffix + ".sha256").write_text(
        f"{digest}  {output.name}\n",
        encoding="utf-8",
    )
    return master


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--obra-id", required=True)
    parser.add_argument("--obra-root", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    obra_root = args.obra_root or ROOT / "analista/generado/obras" / args.obra_id
    output = args.output or ROOT / "analista/generado/maestros" / f"{args.obra_id}.json"
    master = assemble(args.obra_id, obra_root, output)
    counts = {field: len(master[field]) for field in AUDITED_FILES}
    print(
        json.dumps(
            {
                "obra_id": args.obra_id,
                "unidades": len(master["unidades"]),
                "hallazgos": len(master["hallazgos_auditoria"]),
                "registros_auditados": sum(counts.values()),
                "conteos": counts,
                "perfil_conceptual": master["controles_fase10"]["alcance_conceptual"]["perfil"],
                "comparacion_interobra": False,
                "salida": relative(output),
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
