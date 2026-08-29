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
LOCK = ROOT / "analista/calibracion/fase10" / OBRA / "muestra-v1.1.0.lock.json"
BASE_MOTOR = ROOT / "analista/motores/formulas.py"
ADAPTER = ROOT / "analista/motores/formulas_obra_fase10.py"
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

    adapter = load_module("fase10_test_formulas_adapter", ADAPTER)
    with tempfile.TemporaryDirectory() as td:
        t = Path(td)
        first = t / "first.jsonl"
        first_cov = t / "first-cov.jsonl"
        second = t / "second.jsonl"
        second_cov = t / "second-cov.jsonl"
        adapter.run(obra_id=OBRA, unidades=UNIDADES, salida=first, cobertura=first_cov)
        adapter.run(obra_id=OBRA, unidades=UNIDADES, salida=second, cobertura=second_cov)
        assert first.read_bytes() == second.read_bytes()
        assert first_cov.read_bytes() == second_cov.read_bytes()
        rows = load_jsonl(first)
        coverage = load_jsonl(first_cov)

    assert len(rows) == 33, len(rows)
    assert sum(r["clasificacion_formula"] == "formula_explicita" for r in rows) == 3
    assert sum(r["clasificacion_formula"] == "formula_candidata" for r in rows) == 30
    assert all(r["fuente_id"] == OBRA for r in rows)
    assert all(r["estado_verificacion"] == "pendiente" for r in rows)
    assert all(r["estado_auditoria"] == "pendiente" for r in rows)
    assert all(r["producido_por"] == {"motor": "formulas", "version": "1.2.0"} for r in rows)

    lock = json.loads(LOCK.read_text(encoding="utf-8"))
    expected_signal_units = set(lock["desafios"]["formulas"])
    emitted_signal_units = {r["unidad_id"] for r in rows}
    assert emitted_signal_units == expected_signal_units
    assert len(emitted_signal_units) == 17

    literals = [r["formula_literal"] for r in rows]
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

    for row in rows:
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

    assert len(coverage) == 1
    cov = coverage[0]
    assert cov["obra_id"] == OBRA
    assert cov["motor"] == "formulas"
    assert cov["version_motor"] == "1.2.0"
    assert cov["unidades_totales"] == 643
    assert cov["unidades_procesadas"] == 643
    assert cov["unidades_omitidas"] == []
    assert cov["errores"] == []
    assert cov["estado_verificacion"] == "pendiente"

    # Cuando el workflow haya materializado el producto aislado, debe coincidir
    # con la ejecución independiente del adaptador.
    if (OUT / "formulas-candidatas.jsonl").is_file():
        assert (OUT / "formulas-candidatas.jsonl").read_bytes() == first.read_bytes()
        assert (OUT / "cobertura-formulas.jsonl").read_bytes() == first_cov.read_bytes()

    print(
        "OK Fase 10 4D Ágape: piloto v1.1 byte-idéntico; Ágape v1.2 = 33 fórmulas "
        "(3 explícitas + 30 candidatas), 17/17 unidades con señal formal cubiertas; sin remisiones ni prosa absorbida."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
