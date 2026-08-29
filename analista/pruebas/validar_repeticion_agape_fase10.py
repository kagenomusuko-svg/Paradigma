#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
MOTOR = ROOT / "analista/motores/ejecutar_extractores_obra_fase10.py"
FUENTES = ROOT / "analista/generado/fuentes.jsonl"
UNIDADES = ROOT / "analista/generado/unidades.jsonl"
SCHEMA = ROOT / "analista/esquema/contratos-v1.0.0.schema.json"
AGAPE = "FUE-2C28F35DD6CF"
OUT = ROOT / "analista/generado/obras" / AGAPE

PRODUCT_TYPES = {
    "apariciones-conceptuales.jsonl": "aparicion_conceptual",
    "conceptos.jsonl": "concepto",
    "definiciones.jsonl": "definicion",
    "afirmaciones-candidatas.jsonl": "afirmacion",
    "formulas-candidatas.jsonl": "formula",
    "relaciones-explicitas.jsonl": "relacion_explicita",
    "distinciones.jsonl": "distincion",
    "negaciones.jsonl": "negacion",
    "excepciones.jsonl": "excepcion",
    "restricciones-alcance.jsonl": "restriccion_alcance",
}
COVERAGES = [
    "cobertura-conceptos.jsonl",
    "cobertura-definiciones.jsonl",
    "cobertura-afirmaciones.jsonl",
    "cobertura-formulas.jsonl",
    "cobertura-relaciones.jsonl",
    "cobertura-limitadores.jsonl",
]
PILOT_PRODUCTS = [
    "apariciones-conceptuales.jsonl",
    "conceptos.jsonl",
    "definiciones.jsonl",
    "afirmaciones-candidatas.jsonl",
    "formulas-candidatas.jsonl",
    "relaciones-explicitas.jsonl",
    "distinciones.jsonl",
    "negaciones.jsonl",
    "excepciones.jsonl",
    "restricciones-alcance.jsonl",
    *COVERAGES,
]


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(obra_id: str, output_root: Path, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(MOTOR),
            "--obra-id",
            obra_id,
            "--fuentes",
            str(FUENTES),
            "--unidades",
            str(UNIDADES),
            "--output-root",
            str(output_root),
        ],
        cwd=ROOT,
        check=check,
        text=True,
        capture_output=True,
    )


def validator_for(def_name: str, schema: dict) -> Draft202012Validator:
    wrapped = {
        "$schema": schema["$schema"],
        "$id": schema.get("$id", "https://example.invalid/contratos-fase10.json"),
        "$defs": schema["$defs"],
        "$ref": f"#/$defs/{def_name}",
    }
    return Draft202012Validator(wrapped)


def main() -> int:
    sources = load_jsonl(FUENTES)
    units = load_jsonl(UNIDADES)
    agape_source = [s for s in sources if s["id"] == AGAPE]
    assert len(agape_source) == 1
    agape_units = [u for u in units if u["fuente_id"] == AGAPE]
    assert len(agape_units) == 643, len(agape_units)
    assert len({u["id"] for u in agape_units}) == 643
    assert len([r for r in agape_source[0].get("rutas_derivadas", []) if r.endswith("99-glosario.md")]) == 1

    pilot_hashes = {
        name: sha(ROOT / "analista/generado" / name)
        for name in PILOT_PRODUCTS
        if (ROOT / "analista/generado" / name).is_file()
    }
    assert pilot_hashes, "No hay productos globales del piloto para controlar aislamiento"

    result = run(AGAPE, OUT)
    assert result.returncode == 0

    for name, before in pilot_hashes.items():
        assert sha(ROOT / "analista/generado" / name) == before, f"El piloto fue modificado: {name}"

    assert load_jsonl(OUT / "fuente.jsonl") == agape_source
    assert load_jsonl(OUT / "unidades.jsonl") == agape_units

    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    by_file: dict[str, list[dict]] = {}
    for filename, def_name in PRODUCT_TYPES.items():
        rows = load_jsonl(OUT / filename)
        by_file[filename] = rows
        validator = validator_for(def_name, schema)
        for row in rows:
            errors = list(validator.iter_errors(row))
            assert not errors, f"{filename}:{row.get('id')}: {errors[0].message if errors else ''}"
            if "fuente_id" in row:
                assert row["fuente_id"] == AGAPE
            assert row["estado_verificacion"] == "pendiente"
            assert row["estado_auditoria"] == "pendiente"

    coverage_validator = validator_for("reporte_cobertura", schema)
    for filename in COVERAGES:
        rows = load_jsonl(OUT / filename)
        assert len(rows) == 1, filename
        cov = rows[0]
        assert not list(coverage_validator.iter_errors(cov)), filename
        assert cov["obra_id"] == AGAPE
        assert cov["unidades_totales"] == 643
        assert cov["unidades_procesadas"] == 643
        assert cov["unidades_omitidas"] == []
        assert cov["errores"] == []
        assert cov["estado_verificacion"] == "pendiente"

    concepts = {r["id"]: r for r in by_file["conceptos.jsonl"]}
    appearances = {r["id"]: r for r in by_file["apariciones-conceptuales.jsonl"]}
    assert concepts, "Ágape debe recuperar los lemas de su glosario técnico explícito"
    assert appearances
    for concept in concepts.values():
        assert concept["estado_identidad_conceptual"] == "establecida_por_evidencia"
        assert concept["evidencia_identidad_ids"]
        assert concept["aparicion_ids"]
        for aid in concept["evidencia_identidad_ids"] + concept["aparicion_ids"]:
            assert aid in appearances
        assert all(appearances[aid]["concepto_id"] == concept["id"] for aid in concept["aparicion_ids"])

    for definition in by_file["definiciones.jsonl"]:
        assert definition["concepto_id"] in concepts
    for relation in by_file["relaciones-explicitas.jsonl"]:
        assert relation["sujeto_ref"] in concepts
        assert relation["objeto_ref"] in concepts

    manifest = json.loads((OUT / "manifest-extractores.json").read_text(encoding="utf-8"))
    assert manifest["obra_id"] == AGAPE
    assert manifest["unidades"] == 643
    assert manifest["comparacion_interobra"] is False
    for filename, digest in manifest["productos"].items():
        assert sha(OUT / filename) == digest

    serialized = "\n".join(
        (OUT / name).read_text(encoding="utf-8")
        for name in [*PRODUCT_TYPES, *COVERAGES, "manifest-extractores.json"]
    )
    assert "AA-SP-V1" not in serialized, "La repetición de Ágape filtró identidad del piloto"

    with tempfile.TemporaryDirectory() as td:
        replay = Path(td) / AGAPE
        run(AGAPE, replay)
        expected = [
            "fuente.jsonl",
            "unidades.jsonl",
            *PRODUCT_TYPES.keys(),
            *COVERAGES,
            "manifest-extractores.json",
        ]
        for filename in expected:
            assert (OUT / filename).read_bytes() == (replay / filename).read_bytes(), filename

        without_glossary = next(
            source
            for source in sources
            if not any(str(route).endswith("99-glosario.md") for route in source.get("rutas_derivadas", []))
        )
        rejected = run(without_glossary["id"], Path(td) / "sin-glosario", check=False)
        assert rejected.returncode != 0
        assert "no tiene exactamente un glosario técnico explícito" in (rejected.stderr + rejected.stdout)

    counts = {name: len(rows) for name, rows in by_file.items()}
    print(
        "OK Fase 10 Ágape: 643 unidades aisladas; contratos 4A–4F válidos; "
        f"conteos={json.dumps(counts, ensure_ascii=False, sort_keys=True)}; "
        "reproducibilidad exacta; piloto intacto; obra sin glosario rechazada sin inferencia."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
