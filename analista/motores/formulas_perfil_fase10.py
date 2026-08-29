#!/usr/bin/env python3
"""Aplica una clasificación calibrada por obra sobre el detector 4D v1.2.

Sin perfil explícito, el detector conserva `formula_candidata`. Un perfil puede
promover los bloques formales ya detectados, pero esta capa no cambia literal,
rango, unidad ni cantidad de registros. La autorización es documental y queda
en `analista/calibracion/fase10/<obra_id>/perfil-extractores.json`.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DETECTOR = ROOT / "analista/motores/formulas_obra_fase10.py"
PRODUCTION_VERSION = "1.3.0"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"No se pudo cargar {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def dump_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text(
        "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows),
        encoding="utf-8",
    )


def profile_for(obra_id: str, profile_path: Path | None) -> dict | None:
    if profile_path is None or not profile_path.is_file():
        return None
    profile = load_json(profile_path)
    if profile.get("obra_id") != obra_id:
        raise SystemExit("El perfil de extractores no pertenece a la obra solicitada")
    return profile.get("formulas")


def run(
    *,
    obra_id: str,
    unidades: Path,
    salida: Path,
    cobertura: Path,
    perfil: Path | None = None,
) -> dict:
    detector = load_module("fase10_formulas_detector_v120", DETECTOR)
    result = detector.run(
        obra_id=obra_id,
        unidades=unidades,
        salida=salida,
        cobertura=cobertura,
    )
    formula_profile = profile_for(obra_id, perfil)
    if formula_profile is None:
        return result

    if formula_profile.get("detector_version") != "1.2.0":
        raise SystemExit("Perfil de fórmulas incompatible con el detector v1.2.0")
    mode = formula_profile.get("clasificacion_bloques_formales")
    if mode != "formula_explicita":
        raise SystemExit(f"Modo de clasificación no soportado: {mode!r}")
    if formula_profile.get("produccion_version") != PRODUCTION_VERSION:
        raise SystemExit("Versión de producción del perfil incompatible")
    if formula_profile.get("cobertura_revision") != "censo_completo_senales_formales":
        raise SystemExit("No se puede promover sin censo completo de señales formales")

    rows = load_jsonl(salida)
    expected_count = formula_profile.get("formulas_manual_esperadas")
    if len(rows) != expected_count:
        raise SystemExit(
            f"El perfil manual cubre {expected_count} fórmulas pero el detector emitió {len(rows)}; "
            "se requiere recalibración antes de promover."
        )

    # La promoción es exclusivamente clasificatoria. Las claves de detección y
    # los IDs permanecen idénticos al baseline v1.2.0.
    for row in rows:
        row["clasificacion_formula"] = "formula_explicita"
        row["estado_extraccion"] = "extraido"
        row["producido_por"] = {"motor": "formulas", "version": PRODUCTION_VERSION}
    dump_jsonl(salida, rows)

    coverage_rows = load_jsonl(cobertura)
    if len(coverage_rows) != 1:
        raise SystemExit("Cobertura de fórmulas inválida")
    cov = coverage_rows[0]
    base = detector.load_base()
    cov["id"] = base.stable_id("COB", obra_id, "formulas", PRODUCTION_VERSION)
    cov["version_motor"] = PRODUCTION_VERSION
    cov["producido_por"] = {"motor": "formulas", "version": PRODUCTION_VERSION}
    dump_jsonl(cobertura, [cov])

    result = dict(result)
    result.update(
        {
            "version": PRODUCTION_VERSION,
            "explicitas": len(rows),
            "candidatas": 0,
            "perfil_calibrado": True,
        }
    )
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return result


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--obra-id", required=True)
    ap.add_argument("--unidades", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    ap.add_argument("--cobertura", type=Path, required=True)
    ap.add_argument("--perfil", type=Path)
    args = ap.parse_args()
    run(
        obra_id=args.obra_id,
        unidades=args.unidades,
        salida=args.salida,
        cobertura=args.cobertura,
        perfil=args.perfil,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
