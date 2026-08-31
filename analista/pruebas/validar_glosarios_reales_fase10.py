#!/usr/bin/env python3
"""Regresión temprana de 4A sobre los glosarios reales inventariados en Fase 10.

No sustituye el cierre E2E de cada obra. Comprueba antes del recorrido costoso que
la detección del formato editorial no fabrica lemas y que cada declaración de
lema recuperada remonta a una única unidad real de Fase 3.
"""
from __future__ import annotations

import importlib.util
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MOTOR = ROOT / "analista/motores/conceptos_compuesto_fase10.py"
FUENTES = ROOT / "analista/generado/fuentes.jsonl"
UNIDADES = ROOT / "analista/generado/unidades.jsonl"


def load(path: Path) -> list[dict]:
    return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x]


def module():
    spec = importlib.util.spec_from_file_location("conceptos_compuesto_real_f10", MOTOR)
    assert spec and spec.loader
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main() -> int:
    c = module()
    sources = load(FUENTES)
    units = load(UNIDADES)
    by_source_route: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for unit in units:
        by_source_route[(unit["fuente_id"], unit["archivo"])].append(unit)

    glossaries: list[tuple[str, str]] = []
    for source in sources:
        routes = [str(x) for x in source.get("rutas_derivadas", []) if str(x).endswith("99-glosario.md")]
        assert len(routes) <= 1, (source["id"], routes)
        if routes:
            glossaries.append((source["id"], routes[0]))
    assert len(glossaries) == 8, len(glossaries)

    recovered = 0
    reference_indexes = 0
    summary = []
    for obra_id, route in glossaries:
        path = ROOT / route
        lines = path.read_text(encoding="utf-8").splitlines()
        start = next((i for i, line in enumerate(lines) if "glosario" in c.g.norm(line)), None)
        assert start is not None, route

        if c._reference_index(lines, start):
            assert c.glossary_entries(path) == []
            reference_indexes += 1
            summary.append({"obra_id": obra_id, "ruta": route, "modo": "indice_referencias", "lemas": 0})
            continue

        entries = c.glossary_entries(path)
        assert entries, route
        keys = [c.g.norm(term) for term, _line, _fmt in entries]
        assert len(keys) == len(set(keys)), (route, "lemas_normalizados_duplicados")

        route_units = by_source_route[(obra_id, route)]
        assert route_units, (obra_id, route, "sin_unidades_fase3")
        for term, line_no, fmt in entries:
            assert c._declared_on_line(lines[line_no - 1], term, fmt), (route, term, line_no, fmt)
            owners = [
                unit for unit in route_units
                if unit["localizacion"]["linea_inicio"] <= line_no <= unit["localizacion"]["linea_fin"]
            ]
            assert len(owners) == 1, (route, term, line_no, "unidades_que_cubren", [u["id"] for u in owners])
            unit = owners[0]
            relative = line_no - unit["localizacion"]["linea_inicio"]
            unit_lines = unit["texto_literal"].splitlines()
            assert 0 <= relative < len(unit_lines), (route, term, unit["id"], relative)
            assert unit_lines[relative].strip() == lines[line_no - 1].strip(), (route, term, unit["id"])

        recovered += len(entries)
        summary.append({"obra_id": obra_id, "ruta": route, "modo": entries[0][2], "lemas": len(entries)})

    print(json.dumps({"fase": 10, "glosarios": len(glossaries), "indices_referencia": reference_indexes,
                      "lemas_reales_verificados": recovered, "detalle": summary}, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
