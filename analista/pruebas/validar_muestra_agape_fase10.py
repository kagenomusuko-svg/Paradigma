#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OBRA = "FUE-2C28F35DD6CF"
OUT = ROOT / "analista/generado/obras" / OBRA
LOCK = ROOT / "analista/calibracion/fase10" / OBRA / "muestra.lock.json"

FILES_BY_MOTOR = {
    "conceptos_apariciones": ["apariciones-conceptuales.jsonl"],
    "definiciones": ["definiciones.jsonl"],
    "afirmaciones": ["afirmaciones-candidatas.jsonl"],
    "formulas": ["formulas-candidatas.jsonl"],
    "relaciones_explicitas": ["relaciones-explicitas.jsonl"],
    "limitadores": ["distinciones.jsonl", "negaciones.jsonl", "excepciones.jsonl", "restricciones-alcance.jsonl"],
}


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def key(*parts: str) -> str:
    return hashlib.sha256("\x1f".join(parts).encode("utf-8")).hexdigest()


def no_auto_gold(value) -> None:
    if isinstance(value, dict):
        assert "items_esperados" not in value
        assert "etiquetas_oro" not in value
        for child in value.values():
            no_auto_gold(child)
    elif isinstance(value, list):
        for child in value:
            no_auto_gold(child)


def main() -> int:
    lock = json.loads(LOCK.read_text(encoding="utf-8"))
    assert lock["version"] == "1.0.0"
    assert lock["obra_id"] == OBRA
    assert lock["selector"] == "sha256-stratified-fase10-v1"
    no_auto_gold(lock)

    units = load_jsonl(OUT / "unidades.jsonl")
    assert len(units) == 643
    by_id = {u["id"]: u for u in units}
    assert len(by_id) == 643

    # Estrato general: exactamente una unidad por archivo, escogida sin mirar
    # predicciones mediante hash estable de obra/archivo/unidad.
    by_file: dict[str, list[dict]] = {}
    for unit in units:
        by_file.setdefault(unit["archivo"], []).append(unit)
    assert len(by_file) == 20
    expected_general = []
    for route, route_units in sorted(by_file.items()):
        chosen = min(route_units, key=lambda u: key(OBRA, "general", route, u["id"]))
        expected_general.append(chosen["id"])
    assert lock["general"] == expected_general
    assert len(lock["general"]) == 20

    # Los desafíos pueden estratificarse con las salidas, como en Fase 8, pero
    # el lock no contiene anotación de oro. La selección queda congelada aquí.
    for motor, filenames in FILES_BY_MOTOR.items():
        predicted_units: set[str] = set()
        for filename in filenames:
            for row in load_jsonl(OUT / filename):
                if row.get("unidad_id"):
                    predicted_units.add(row["unidad_id"])
        locked = lock["desafios"][motor]
        expected = sorted(predicted_units, key=lambda uid: key(OBRA, motor, uid))[: len(locked)]
        assert locked == expected, motor
        assert len(set(locked)) == len(locked)
        assert set(locked) <= set(by_id)

    # Congela exactamente los productos que se usaron solo para estratificar.
    for filename, expected_hash in lock["productos_estratificacion_sha256"].items():
        assert sha(OUT / filename) == expected_hash, filename

    union = set(lock["general"])
    for ids in lock["desafios"].values():
        union.update(ids)
    assert len(union) == 88
    assert union <= set(by_id)

    print(
        "OK Fase 10 muestra Ágape: 20 unidades generales + desafíos congelados, "
        "88 unidades únicas; hashes de estratificación exactos; sin items_esperados autogenerados."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
