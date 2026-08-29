#!/usr/bin/env python3
"""Valida el expediente maestro piloto contra productos reales de Fases 2–8."""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[2]
OLD_SCHEMA = ROOT / "analista/esquema/contratos-v1.0.0.schema.json"
MASTER_SCHEMA = ROOT / "analista/esquema/expediente-maestro-v1.1.0.schema.json"
GENERATED = ROOT / "analista/generado"
MASTER = GENERATED / "maestros/AA-SP-V1.json"
ASSEMBLER = ROOT / "analista/motores/ensamblador_maestro.py"
PILOTO_ID = "AA-SP-V1"
EXPECTED = {
    "apariciones_conceptuales": 2575,
    "conceptos": 21,
    "definiciones": 60,
    "afirmaciones": 333,
    "formulas": 21,
    "relaciones_explicitas": 83,
    "distinciones": 233,
    "negaciones": 1346,
    "excepciones": 1,
    "restricciones_alcance": 16,
}
FILE_BY_FIELD = {
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
REF_BY_FIELD = {
    "apariciones_conceptuales": "aparicion_conceptual",
    "conceptos": "concepto",
    "definiciones": "definicion",
    "afirmaciones": "afirmacion",
    "formulas": "formula",
    "relaciones_explicitas": "relacion_explicita",
    "distinciones": "distincion",
    "negaciones": "negacion",
    "excepciones": "excepcion",
    "restricciones_alcance": "restriccion_alcance",
}


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def import_assembler():
    spec = importlib.util.spec_from_file_location("ensamblador_maestro", ASSEMBLER)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validator(old: dict, name: str) -> Draft202012Validator:
    return Draft202012Validator({"$schema": old["$schema"], "$defs": old["$defs"], "$ref": f"#/$defs/{name}"})


def expect_trace_failure(module, master: dict, text: str) -> None:
    try:
        module.validate_traceability(master)
    except AssertionError as exc:
        assert text in str(exc), (text, exc)
        return
    raise AssertionError(f"La mutación debía fallar: {text}")


def main() -> int:
    subprocess.run([sys.executable, str(ASSEMBLER)], cwd=ROOT, check=True)
    master = json.loads(MASTER.read_text(encoding="utf-8"))
    module = import_assembler()

    old = json.loads(OLD_SCHEMA.read_text(encoding="utf-8"))
    new = json.loads(MASTER_SCHEMA.read_text(encoding="utf-8"))
    registry = Registry().with_resource(old["$id"], Resource.from_contents(old))
    master_validator = Draft202012Validator(new, registry=registry)
    errors = list(master_validator.iter_errors(master))
    assert not errors, errors[0].message if errors else ""

    assert master["id"] == "MAE-AA-SP-V1"
    assert master["obra_id"] == PILOTO_ID
    assert master["titulo"] == "Afrodita Areia: Sobre la pasión"
    assert master["schema_version"] == "1.1.0"
    assert master["producido_por"] == {"motor": "ensamblador_maestro", "version": "1.0.0"}
    assert master["estado_verificacion"] == "verificado"
    assert master["estado_auditoria"] == "no_aplica"
    assert len(master["fuentes"]) == 1 and master["fuentes"][0]["id"] == PILOTO_ID
    assert len(master["unidades"]) == 836
    assert sum(EXPECTED.values()) == 4689

    source_validator = validator(old, "fuente")
    unit_validator = validator(old, "unidad_textual")
    assert not list(source_validator.iter_errors(master["fuentes"][0]))
    for unit in master["unidades"]:
        assert not list(unit_validator.iter_errors(unit))
        assert unit["fuente_id"] == PILOTO_ID

    for field, count in EXPECTED.items():
        rows = master[field]
        assert len(rows) == count, (field, len(rows), count)
        original = load_jsonl(GENERATED / "auditados" / FILE_BY_FIELD[field])
        assert rows == original, f"El ensamblador transformó {field}"
        v = validator(old, REF_BY_FIELD[field])
        for row in rows:
            errors = list(v.iter_errors(row))
            assert not errors, f"{field}/{row.get('id')}: {errors[0].message}"
            assert row["estado_verificacion"] == "verificado"
            assert row["estado_auditoria"] == "auditado"

    findings = master["hallazgos_auditoria"]
    assert len(findings) == 1313
    assert findings == load_jsonl(GENERATED / "hallazgos-auditoria.jsonl")
    finding_validator = validator(old, "hallazgo_auditoria")
    categories = Counter(row["categoria"] for row in findings)
    assert categories == Counter({
        "negacion_explicita": 1258,
        "restriccion_de_alcance": 16,
        "uso_singular": 13,
        "definiciones_multiples": 13,
        "variacion_de_objeto": 11,
        "relacion_repetida": 1,
        "excepcion_explicita": 1,
    })
    for row in findings:
        assert not list(finding_validator.iter_errors(row))
        assert row["resolucion_doctrinal"] == "no_realizada"

    coverage = master["reportes_cobertura"]
    assert len(coverage) == 7
    assert {row["motor"] for row in coverage} == {
        "unidades", "conceptos_apariciones", "definiciones", "afirmaciones",
        "formulas", "relaciones_explicitas", "limitadores",
    }
    assert all(row["unidades_totales"] == row["unidades_procesadas"] == 836 for row in coverage)
    assert all(not row["unidades_omitidas"] and not row["errores"] for row in coverage)

    metrics = master["metricas_calibracion"]["reportes"]
    assert len(metrics) == 18
    assert {(row["motor"], row["estrato"]) for row in metrics} == {
        (motor, stratum)
        for motor in {"conceptos_apariciones", "definiciones", "afirmaciones", "formulas", "relaciones_explicitas", "limitadores"}
        for stratum in {"general", "desafio", "combinado"}
    }
    assert master["cierre_calibracion"]["cierre_cuantitativo"] is True
    assert len(master["cierre_calibracion"]["detalle"]) == 12

    trace = master["trazabilidad_archivos"]
    assert len(trace) == 23
    for entry in trace:
        path = ROOT / entry["ruta"]
        assert path.is_file(), entry["ruta"]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == entry["sha256"]

    module.validate_traceability(master)
    all_producers = {
        f"{row['producido_por']['motor']}/{row['producido_por']['version']}"
        for field in EXPECTED
        for row in master[field]
    }
    history = {row["version"] for row in master["historial_versiones"]}
    assert all_producers <= history
    assert {"normalizacion/1.0.0", "calibracion/1.1.0", "umbrales/1.1.0", "ensamblador_maestro/1.0.0"} <= history

    sidecar = MASTER.with_suffix(MASTER.suffix + ".sha256")
    digest, filename = sidecar.read_text(encoding="utf-8").strip().split("  ", 1)
    assert filename == MASTER.name
    assert digest == hashlib.sha256(MASTER.read_bytes()).hexdigest()

    snapshot = MASTER.read_bytes(), sidecar.read_bytes()
    subprocess.run([sys.executable, str(ASSEMBLER)], cwd=ROOT, check=True)
    assert (MASTER.read_bytes(), sidecar.read_bytes()) == snapshot

    broken = copy.deepcopy(master)
    broken["relaciones_explicitas"][0]["objeto_ref"] = "CON-INEXISTENTE"
    expect_trace_failure(module, broken, "referente inexistente")
    broken = copy.deepcopy(master)
    broken["hallazgos_auditoria"][0]["resolucion_doctrinal"] = "armonizada"
    expect_trace_failure(module, broken, "resolución doctrinal")
    broken = copy.deepcopy(master)
    broken["cierre_calibracion"]["cierre_cuantitativo"] = False
    expect_trace_failure(module, broken, "Fase 8 no está cerrada")

    print(
        "OK Fase 9: maestro AA-SP-V1 validado; 836 unidades, 4689 registros auditados, "
        "1313 hallazgos, 7 coberturas, 18 reportes de calibración y 23 hashes de insumo; "
        "toda referencia remonta a evidencia y productor; salida byte-reproducible."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
