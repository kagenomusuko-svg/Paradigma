#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OBRA = "FUE-2C28F35DD6CF"
OUT = ROOT / "analista/generado/obras" / OBRA
LOCK = ROOT / "analista/calibracion/fase10" / OBRA / "muestra-v1.1.0.lock.json"
MOTORS = {
    "conceptos_apariciones",
    "definiciones",
    "afirmaciones",
    "formulas",
    "relaciones_explicitas",
    "limitadores",
}
HEX64 = re.compile(r"^[0-9a-f]{64}$")


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


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


def formal_signal(unit: dict) -> bool:
    for line in unit["texto_literal"].splitlines():
        literal = line.strip()
        if not literal or literal.startswith("→") or "http" in literal or len(literal) > 320:
            continue
        if "=" in literal or "→" in literal:
            return True
    return False


def main() -> int:
    lock = json.loads(LOCK.read_text(encoding="utf-8"))
    assert lock["version"] == "1.1.0"
    assert lock["antecesor"] == "muestra.lock.json@1.0.0"
    assert lock["obra_id"] == OBRA
    assert lock["selector"] == "sha256-stratified-fase10-v1.1"
    assert set(lock["desafios"]) == MOTORS
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

    # Una vez congelados, los desafíos NO se vuelven a seleccionar desde las
    # predicciones actuales: eso permitiría que un cambio del extractor moviera
    # la prueba. Solo se comprueba pertenencia al corpus y unicidad.
    for motor, locked in lock["desafios"].items():
        assert len(set(locked)) == len(locked), motor
        assert set(locked) <= set(by_id), motor

    # Para 4D, v1.1 congeló antes de la corrección todas las unidades con señal
    # formal observable, independiente de que el extractor antiguo las emitiera.
    expected_formula_signal = sorted(
        (u["id"] for u in units if formal_signal(u)),
        key=lambda uid: key(OBRA, "formulas-senal-formal", uid),
    )
    assert lock["desafios"]["formulas"] == expected_formula_signal
    assert len(expected_formula_signal) == 17

    # Los hashes son procedencia histórica de los productos usados para la
    # estratificación original. No se comparan con salidas recalibradas actuales.
    expected_product_names = {
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
    }
    assert set(lock["productos_estratificacion_sha256"]) == expected_product_names
    assert all(HEX64.fullmatch(value) for value in lock["productos_estratificacion_sha256"].values())

    union = set(lock["general"])
    for ids in lock["desafios"].values():
        union.update(ids)
    assert len(union) == 96
    assert union <= set(by_id)

    print(
        "OK Fase 10 muestra Ágape v1.1: 20 unidades generales, 17 señales formales y desafíos congelados; "
        "96 unidades únicas; la recalibración no puede reseleccionar la muestra ni autogenerar oro."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
