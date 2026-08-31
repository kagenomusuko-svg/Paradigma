#!/usr/bin/env python3
"""Valida la muestra congelada de Fase 8 sin reseleccionarla desde extractores mutables.

El estrato general sí se reconstruye de forma determinista desde el snapshot
sellado de ``unidades.jsonl``. Los estratos de desafío son parte del lock
normativo: cambiar un extractor después del congelamiento no puede moverlos.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
UNIDADES = ROOT / "analista/generado/unidades.jsonl"
LOCK = ROOT / "analista/calibracion/muestra-fase8.lock.json"
ORIGEN = ROOT / "analista/calibracion/muestra-fase8.origen.json"

PILOTO_ID = "AA-SP-V1"
SELECTOR_ID = "sha256-stratified-v1"
EXPECTED_CHALLENGES = {
    "conceptos_apariciones": 10,
    "definiciones": 7,
    "afirmaciones": 12,
    "formulas": 18,
    "relaciones_explicitas": 2,
    "limitadores": 27,
}
EXPECTED_GENERAL = 31
EXPECTED_UNIQUE = 96


def load_jsonl(path: Path) -> list[dict]:
    if not path.is_file():
        raise AssertionError(f"No existe insumo requerido: {path}")
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    payload = f"blob {len(data)}\0".encode() + data
    return hashlib.sha1(payload).hexdigest()


def rank(seed: str, ids: list[str]) -> list[str]:
    return sorted(ids, key=lambda item: hashlib.sha256(f"{seed}|{item}".encode()).hexdigest())


def deterministic_general(units: dict[str, dict]) -> list[str]:
    by_file: dict[str, list[dict]] = {}
    for row in units.values():
        by_file.setdefault(row["archivo"], []).append(row)

    general: list[str] = []
    for filename in sorted(by_file):
        candidates = [row["id"] for row in by_file[filename] if row["tipo_estructural"] == "parrafo"]
        if not candidates:
            candidates = [row["id"] for row in by_file[filename]]
        general.append(rank("general-file", candidates)[0])
    general.extend(
        rank("general-header", [row["id"] for row in units.values() if row["tipo_estructural"] == "encabezado"])[:5]
    )
    general.extend(
        rank("general-sep", [row["id"] for row in units.values() if row["tipo_estructural"] == "separador"])[:3]
    )
    return list(dict.fromkeys(general))


def validate(units_path: Path, lock_path: Path, origin_path: Path) -> dict:
    if not lock_path.is_file() or not origin_path.is_file():
        raise AssertionError("Faltan lock u origen de la muestra de Fase 8")

    origin = json.loads(origin_path.read_text(encoding="utf-8"))
    expected_origin = {
        "version": "1.0.0",
        "obra_id": PILOTO_ID,
        "selector": SELECTOR_ID,
        "lock": "analista/calibracion/muestra-fase8.lock.json",
        "unidades": "analista/generado/unidades.jsonl",
    }
    for key, value in expected_origin.items():
        if origin.get(key) != value:
            raise AssertionError(f"Origen de muestra incompatible en {key}: {origin.get(key)!r}")
    if origin.get("lock_blob_git") != git_blob_sha(lock_path):
        raise AssertionError("El lock de Fase 8 no coincide con el blob Git congelado")
    if origin.get("unidades_blob_git") != git_blob_sha(units_path):
        raise AssertionError("unidades.jsonl no coincide con el snapshot usado para congelar Fase 8")

    locked = json.loads(lock_path.read_text(encoding="utf-8"))
    if locked.get("version") != "1.0.0" or locked.get("obra_id") != PILOTO_ID:
        raise AssertionError("Lock de muestra incompatible")
    if locked.get("selector") != SELECTOR_ID:
        raise AssertionError("Lock de muestra usa un selector inesperado")

    rows = load_jsonl(units_path)
    units = {row["id"]: row for row in rows if row.get("fuente_id") == PILOTO_ID}
    if not units:
        raise AssertionError(f"No hay unidades para {PILOTO_ID}")

    general = locked.get("general")
    if not isinstance(general, list) or len(general) != EXPECTED_GENERAL:
        raise AssertionError(f"Estrato general inválido: se esperaban {EXPECTED_GENERAL} unidades")
    regenerated_general = deterministic_general(units)
    if general != regenerated_general:
        raise AssertionError("El estrato general no reproduce sha256-stratified-v1 sobre el snapshot sellado de unidades")

    challenges = locked.get("desafios")
    if not isinstance(challenges, dict) or set(challenges) != set(EXPECTED_CHALLENGES):
        raise AssertionError("Estratos de desafío incompletos o desconocidos")
    for motor, expected_count in EXPECTED_CHALLENGES.items():
        ids = challenges[motor]
        if not isinstance(ids, list) or len(ids) != expected_count:
            raise AssertionError(f"Desafío {motor}: se esperaban {expected_count} unidades")
        if len(ids) != len(set(ids)):
            raise AssertionError(f"Desafío {motor}: contiene unidades duplicadas")
        unknown = [unit_id for unit_id in ids if unit_id not in units]
        if unknown:
            raise AssertionError(f"Desafío {motor}: unidades fuera del snapshot sellado: {unknown}")

    unique = set(general)
    for ids in challenges.values():
        unique.update(ids)
    if len(unique) != EXPECTED_UNIQUE:
        raise AssertionError(f"La unión congelada debe contener {EXPECTED_UNIQUE} unidades únicas; contiene {len(unique)}")

    return {
        "lock_verificado": True,
        "unidades_unicas": len(unique),
        "general": len(general),
        "desafios": {key: len(challenges[key]) for key in EXPECTED_CHALLENGES},
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--unidades", type=Path, default=UNIDADES)
    parser.add_argument("--lock", type=Path, default=LOCK)
    parser.add_argument("--origen", type=Path, default=ORIGEN)
    args = parser.parse_args()

    print(json.dumps(validate(args.unidades, args.lock, args.origen), ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
