#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
UNIDADES = ROOT / "analista/generado/unidades.jsonl"
OBRA = "FUE-2C28F35DD6CF"
PILOTO = "AA-SP-V1"
OUT = ROOT / "analista/generado/obras" / OBRA
CALIBRATION = ROOT / "analista/calibracion/fase10" / OBRA
LOCK = CALIBRATION / "muestra-v1.1.0.lock.json"
PROFILE = CALIBRATION / "perfil-extractores.json"
BASELINE = CALIBRATION / "baseline-formulas-v1.2.0.json"
POLICY = CALIBRATION / "politica-oro-formulas-v1.0.0.json"
GOLD_SCHEMA = ROOT / "analista/calibracion/patron-oro-obra-v1.1.0.schema.json"
BASE_MOTOR = ROOT / "analista/motores/formulas.py"
DETECTOR = ROOT / "analista/motores/formulas_obra_fase10.py"
PRODUCTION = ROOT / "analista/motores/formulas_perfil_fase10.py"
EVALUATOR = ROOT / "analista/calibracion/evaluar_formulas_fase10.py"
PILOT_FORMULAS_SHA256 = "cfa027bd64262a13947ffb0ffc964cb5c6e00657e98962b922753fe7a74ca63d"
PILOT_COVERAGE_SHA256 = "e5eb87f74c33dea1a10c7b4ab96e8aa35a6cbbdd30a737f9d18c45c396325eb3"


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise AssertionError(f"No se pudo cargar {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def detection_view(row: dict) -> dict:
    """Campos que una calibración clasificatoria no tiene autoridad para cambiar."""
    excluded = {"clasificacion_formula", "estado_extraccion", "producido_por"}
    return {key: value for key, value in row.items() if key not in excluded}


def main() -> int:
    all_units = load_jsonl(UNIDADES)
    pilot_units = [u for u in all_units if u["fuente_id"] == PILOTO]
    agape_units = [u for u in all_units if u["fuente_id"] == OBRA]
    assert len(pilot_units) == 836
    assert len(agape_units) == 643
    agape_by_id = {u["id"]: u for u in agape_units}

    # Regresión fuerte: el motor piloto cerrado no se modifica ni indirectamente.
    with tempfile.TemporaryDirectory() as td:
        t = Path(td)
        base = load_module("fase10_test_formulas_base", BASE_MOTOR)
        base.PILOTO_ID = PILOTO
        base.UNIDADES = UNIDADES
        base.SALIDA = t / "pilot-formulas.jsonl"
        base.COBERTURA = t / "pilot-cobertura.jsonl"
        assert base.main() == 0
        assert sha(base.SALIDA) == PILOT_FORMULAS_SHA256
        assert sha(base.COBERTURA) == PILOT_COVERAGE_SHA256
        pilot_rows = load_jsonl(base.SALIDA)
        assert len(pilot_rows) == 21
        assert all(r["clasificacion_formula"] == "formula_explicita" for r in pilot_rows)

    detector = load_module("fase10_test_formulas_detector", DETECTOR)
    with tempfile.TemporaryDirectory() as td:
        t = Path(td)
        first = t / "first.jsonl"
        first_cov = t / "first-cov.jsonl"
        second = t / "second.jsonl"
        second_cov = t / "second-cov.jsonl"
        detector.run(obra_id=OBRA, unidades=UNIDADES, salida=first, cobertura=first_cov)
        detector.run(obra_id=OBRA, unidades=UNIDADES, salida=second, cobertura=second_cov)
        assert first.read_bytes() == second.read_bytes()
        assert first_cov.read_bytes() == second_cov.read_bytes()
        detector_rows = load_jsonl(first)
        detector_coverage = load_jsonl(first_cov)

    # Baseline v1.2: detección exhaustiva según el patrón, clasificación aún conservadora.
    assert len(detector_rows) == 33, len(detector_rows)
    assert sum(r["clasificacion_formula"] == "formula_explicita" for r in detector_rows) == 3
    assert sum(r["clasificacion_formula"] == "formula_candidata" for r in detector_rows) == 30
    assert all(r["fuente_id"] == OBRA for r in detector_rows)
    assert all(r["estado_verificacion"] == "pendiente" for r in detector_rows)
    assert all(r["estado_auditoria"] == "pendiente" for r in detector_rows)
    assert all(r["producido_por"] == {"motor": "formulas", "version": "1.2.0"} for r in detector_rows)

    lock = json.loads(LOCK.read_text(encoding="utf-8"))
    expected_signal_units = set(lock["desafios"]["formulas"])
    emitted_signal_units = {r["unidad_id"] for r in detector_rows}
    assert emitted_signal_units == expected_signal_units
    assert len(emitted_signal_units) == 17

    literals = [r["formula_literal"] for r in detector_rows]
    assert "Ágape + α → h" in literals
    assert "Eros = φ₁ (Ágape, α) → primer colapso en dirección" in literals
    assert "Fobos = dimensión arética con distancia colapsada" in literals
    assert any(
        literal == "Potós: voluntad + objeto que tuvo forma + ausencia → orientación\nsostenida → distancia temporal"
        for literal in literals
    )
    assert all(not literal.lstrip().startswith("→") for literal in literals)
    assert all("Esa fórmula" not in literal for literal in literals)
    assert all("donde α es la alteridad" not in literal for literal in literals)

    for row in detector_rows:
        unit = agape_by_id[row["unidad_id"]]
        literal = row["texto_literal"]
        assert row["formula_literal"] == literal
        assert literal in unit["texto_literal"]
        assert row["localizacion"]["ruta"] == unit["archivo"]
        start = unit["texto_literal"].find(literal)
        assert start >= 0
        expected_start = unit["localizacion"]["linea_inicio"] + unit["texto_literal"][:start].count("\n")
        expected_end = expected_start + literal.count("\n")
        assert row["localizacion"]["linea_inicio"] == expected_start
        assert row["localizacion"]["linea_fin"] == expected_end
        assert row["unidad_id"] in row["contexto_unidad_ids"]

    assert len(detector_coverage) == 1
    base_cov = detector_coverage[0]
    assert base_cov["obra_id"] == OBRA
    assert base_cov["motor"] == "formulas"
    assert base_cov["version_motor"] == "1.2.0"
    assert base_cov["unidades_totales"] == 643
    assert base_cov["unidades_procesadas"] == 643
    assert base_cov["unidades_omitidas"] == []
    assert base_cov["errores"] == []
    assert base_cov["estado_verificacion"] == "pendiente"

    # Producción v1.3: el perfil humano solo reclasifica las mismas 33 detecciones.
    production = load_module("fase10_test_formulas_production", PRODUCTION)
    with tempfile.TemporaryDirectory() as td:
        t = Path(td)
        prod_a = t / "a"
        prod_b = t / "b"
        prod_a.mkdir()
        prod_b.mkdir()
        a = prod_a / "formulas-candidatas.jsonl"
        a_cov = prod_a / "cobertura-formulas.jsonl"
        b = prod_b / "formulas-candidatas.jsonl"
        b_cov = prod_b / "cobertura-formulas.jsonl"
        result_a = production.run(
            obra_id=OBRA,
            unidades=UNIDADES,
            salida=a,
            cobertura=a_cov,
            perfil=PROFILE,
        )
        result_b = production.run(
            obra_id=OBRA,
            unidades=UNIDADES,
            salida=b,
            cobertura=b_cov,
            perfil=PROFILE,
        )
        assert a.read_bytes() == b.read_bytes()
        assert a_cov.read_bytes() == b_cov.read_bytes()
        production_rows = load_jsonl(a)
        production_coverage = load_jsonl(a_cov)

        evaluator = load_module("fase10_test_formulas_evaluator", EVALUATOR)
        evaluation = evaluator.evaluate(
            policy=POLICY,
            generated_root=prod_a,
            units=UNIDADES,
            schema=GOLD_SCHEMA,
        )

        if (OUT / "formulas-candidatas.jsonl").is_file():
            assert (OUT / "formulas-candidatas.jsonl").read_bytes() == a.read_bytes()
            assert (OUT / "cobertura-formulas.jsonl").read_bytes() == a_cov.read_bytes()

    assert result_a["version"] == "1.3.0"
    assert result_a["perfil_calibrado"] is True
    assert result_a["explicitas"] == 33
    assert result_a["candidatas"] == 0
    assert result_a == result_b

    assert len(production_rows) == 33
    assert [detection_view(r) for r in production_rows] == [detection_view(r) for r in detector_rows]
    assert all(r["clasificacion_formula"] == "formula_explicita" for r in production_rows)
    assert all(r["estado_extraccion"] == "extraido" for r in production_rows)
    assert all(r["producido_por"] == {"motor": "formulas", "version": "1.3.0"} for r in production_rows)
    assert {r["unidad_id"] for r in production_rows} == expected_signal_units

    assert len(production_coverage) == 1
    prod_cov = production_coverage[0]
    for key in (
        "obra_id",
        "motor",
        "unidades_totales",
        "unidades_procesadas",
        "unidades_omitidas",
        "errores",
        "estado_verificacion",
    ):
        assert prod_cov[key] == base_cov[key], key
    assert prod_cov["version_motor"] == "1.3.0"
    assert prod_cov["producido_por"] == {"motor": "formulas", "version": "1.3.0"}

    profile = json.loads(PROFILE.read_text(encoding="utf-8"))
    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    formula_profile = profile["formulas"]
    assert profile["obra_id"] == OBRA
    assert formula_profile["detector_version"] == "1.2.0"
    assert formula_profile["produccion_version"] == "1.3.0"
    assert formula_profile["cobertura_revision"] == "censo_completo_senales_formales"
    assert formula_profile["unidades_con_senal_formal_revisadas"] == 17
    assert formula_profile["formulas_manual_esperadas"] == 33
    assert formula_profile["patron_manual_sha256"] == baseline["patron_manual_sha256"]
    assert evaluation["patron_manual_sha256"] == formula_profile["patron_manual_sha256"]

    for stratum, positives in (("general", 1), ("desafio", 33)):
        metrics = evaluation["estratos"][stratum]
        assert metrics["positivos_esperados"] == positives
        assert metrics["predicciones_emitidas"] == positives
        assert metrics["falsos_positivos"] == 0
        assert metrics["falsos_negativos"] == 0
        assert metrics["precision"] == 1.0
        assert metrics["cobertura"] == 1.0
        assert metrics["exactitud_clasificacion"] == 1.0

    print(
        "OK Fase 10 4D Ágape: piloto v1.1 byte-idéntico; detector v1.2 conserva 33 detecciones "
        "(3 explícitas + 30 candidatas); perfil humano v1.3 reclasifica esas mismas 33 sin cambiar "
        "ID, literal, unidad ni localización; precisión, cobertura y clasificación = 1.0."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
