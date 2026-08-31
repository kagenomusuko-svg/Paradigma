#!/usr/bin/env python3
"""Valida la muestra congelada de Fase 8 sin reseleccionarla retroactivamente.

La muestra normativa es ``muestra-fase8.lock.json``. Su procedencia sella tanto
el blob del lock como el snapshot de ``unidades.jsonl`` sobre el que se congeló.
El identificador histórico ``sha256-stratified-v1`` no se usa para recalcular la
muestra: el lock fue creado antes que la implementación del selector y esa
implementación posterior no reproduce exactamente el estrato general congelado.
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
REPRODUCTION_MODE = "snapshot-sellado-v1"
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


def validate(units_path: Path, lock_path: Path, origin_path: Path) -> dict:
    if not lock_path.is_file() or not origin_path.is_file():
        raise AssertionError("Faltan lock u origen de la muestra de Fase 8")

    origin = json.loads(origin_path.read_text(encoding="utf-8"))
    expected_origin = {
        "version": "1.0.0",
        "obra_id": PILOTO_ID,
        "selector": SELECTOR_ID,
        "modo_reproduccion": REPRODUCTION_MODE,
        "selector_recalculable": False,
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
    if len(general) != len(set(general)):
        raise AssertionError("El estrato general contiene unidades duplicadas")
    unknown_general = [unit_id for unit_id in general if unit_id not in units]
    if unknown_general:
        raise AssertionError(f"Estrato general: unidades fuera del snapshot sellado: {unknown_general}")

    # El propósito declarado del estrato general exige cobertura de todos los
    # archivos de la obra piloto; se valida la propiedad del snapshot, no una
    # reselección posterior de qué unidad representa cada archivo.
    all_files = {row["archivo"] for row in units.values()}
    general_files = {units[unit_id]["archivo"] for unit_id in general}
    missing_files = sorted(all_files - general_files)
    if missing_files:
        raise AssertionError(f"Estrato general sin representación de archivos del piloto: {missing_files}")

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
