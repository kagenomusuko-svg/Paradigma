#!/usr/bin/env python3
"""Repetición controlada de extractores 4A–4F para una obra de Fase 10.

No modifica los productos globales del piloto. Copia sin transformación la fuente
y sus unidades ya verificadas a un directorio por obra, parametriza en memoria
los motores cerrados de Fase 4 y registra hashes de todos los productos.

La primera ruta controlada exige un glosario técnico explícito porque 4A, 4B y
4E dependen documentalmente de ese soporte. Las obras sin glosario se rechazan
en vez de recibir conceptos inferidos desde otra obra.

Los perfiles de calibración son opt-in por obra. Si existe
`analista/calibracion/fase10/<obra_id>/perfil-extractores.json`, solo puede
clasificar detecciones que el detector de esa obra ya produjo; no puede añadir,
eliminar ni reubicar evidencia.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from contextlib import contextmanager
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_FUENTES = ROOT / "analista/generado/fuentes.jsonl"
DEFAULT_UNIDADES = ROOT / "analista/generado/unidades.jsonl"
DEFAULT_OBRAS_ROOT = ROOT / "analista/generado/obras"
DEFAULT_CALIBRATION_ROOT = ROOT / "analista/calibracion/fase10"
VERSION = "1.2.0"


def load_jsonl(path: Path) -> list[dict]:
    if not path.is_file():
        raise SystemExit(f"No existe insumo requerido: {path}")
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def dump_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows),
        encoding="utf-8",
    )


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"No se pudo cargar motor: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


@contextmanager
def argv_temporal(values: list[str]):
    original = sys.argv[:]
    sys.argv = values
    try:
        yield
    finally:
        sys.argv = original


def run_conceptos(obra_id: str, fuente: Path, unidades: Path, out: Path) -> None:
    m = load_module("fase10_conceptos", ROOT / "analista/motores/conceptos.py")
    m.PILOTO_ID = obra_id
    m.FUENTES = fuente
    m.UNIDADES = unidades
    m.SALIDA_APARICIONES = out / "apariciones-conceptuales.jsonl"
    m.SALIDA_CONCEPTOS = out / "conceptos.jsonl"
    m.SALIDA_COBERTURA = out / "cobertura-conceptos.jsonl"
    if m.main() != 0:
        raise SystemExit("Falló conceptos_apariciones")


def run_definiciones(obra_id: str, fuente: Path, unidades: Path, out: Path) -> None:
    m = load_module("fase10_definiciones", ROOT / "analista/motores/definiciones.py")
    m.PILOTO_ID = obra_id
    m.FUENTES = fuente
    m.UNIDADES = unidades
    m.CONCEPTOS = out / "conceptos.jsonl"
    m.SALIDA = out / "definiciones.jsonl"
    m.COBERTURA = out / "cobertura-definiciones.jsonl"
    if m.main() != 0:
        raise SystemExit("Falló definiciones")


def run_afirmaciones(obra_id: str, unidades: Path, out: Path) -> None:
    m = load_module("fase10_afirmaciones", ROOT / "analista/motores/afirmaciones.py")
    m.PILOTO_ID = obra_id
    m.UNIDADES = unidades
    m.SALIDA = out / "afirmaciones-candidatas.jsonl"
    m.COBERTURA = out / "cobertura-afirmaciones.jsonl"
    if m.main() != 0:
        raise SystemExit("Falló afirmaciones")


def run_formulas(obra_id: str, unidades: Path, out: Path) -> tuple[dict, Path | None]:
    """Ejecuta 4D y aplica únicamente un perfil calibrado de la misma obra.

    El adaptador de producción conserva la salida v1.2 cuando no hay perfil. Si
    existe un perfil, este valida su obra, detector de origen, censo manual y
    número exacto de detecciones antes de permitir una reclasificación.
    """
    m = load_module("fase10_formulas_produccion", ROOT / "analista/motores/formulas_perfil_fase10.py")
    profile = DEFAULT_CALIBRATION_ROOT / obra_id / "perfil-extractores.json"
    profile_arg = profile if profile.is_file() else None
    result = m.run(
        obra_id=obra_id,
        unidades=unidades,
        salida=out / "formulas-candidatas.jsonl",
        cobertura=out / "cobertura-formulas.jsonl",
        perfil=profile_arg,
    )
    return result, profile_arg


def run_relaciones(obra_id: str, fuente: Path, unidades: Path, out: Path) -> None:
    m = load_module("fase10_relaciones", ROOT / "analista/motores/relaciones_explicitas.py")
    m.PILOTO_ID = obra_id
    m.FUENTES = fuente
    m.UNIDADES = unidades
    m.CONCEPTOS = out / "conceptos.jsonl"
    m.SALIDA = out / "relaciones-explicitas.jsonl"
    m.COBERTURA = out / "cobertura-relaciones.jsonl"
    if m.main() != 0:
        raise SystemExit("Falló relaciones_explicitas")


def run_limitadores(obra_id: str, unidades: Path, out: Path) -> None:
    m = load_module("fase10_limitadores", ROOT / "analista/motores/limitadores.py")
    m.PILOTO = obra_id
    with argv_temporal(
        [
            str(ROOT / "analista/motores/limitadores.py"),
            "--unidades",
            str(unidades),
            "--output-root",
            str(out),
        ]
    ):
        if m.main() != 0:
            raise SystemExit("Falló limitadores")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--obra-id", required=True)
    ap.add_argument("--fuentes", type=Path, default=DEFAULT_FUENTES)
    ap.add_argument("--unidades", type=Path, default=DEFAULT_UNIDADES)
    ap.add_argument("--output-root", type=Path)
    args = ap.parse_args()

    sources = load_jsonl(args.fuentes)
    units = load_jsonl(args.unidades)
    selected = [row for row in sources if row.get("id") == args.obra_id]
    if len(selected) != 1:
        raise SystemExit(f"Se esperaba una fuente para {args.obra_id}; encontradas={len(selected)}")
    source = selected[0]
    work_units = [row for row in units if row.get("fuente_id") == args.obra_id]
    if not work_units:
        raise SystemExit(f"La obra {args.obra_id} no tiene unidades de Fase 3")
    if len({row["id"] for row in work_units}) != len(work_units):
        raise SystemExit(f"IDs de unidad duplicados en {args.obra_id}")

    glossaries = [
        route for route in source.get("rutas_derivadas", []) if str(route).endswith("99-glosario.md")
    ]
    if len(glossaries) != 1:
        raise SystemExit(
            f"Fase 10 controlada v{VERSION}: {args.obra_id} no tiene exactamente un glosario técnico explícito; "
            "no se fabricarán conceptos ni se reutilizará el glosario de otra obra."
        )

    out = args.output_root or (DEFAULT_OBRAS_ROOT / args.obra_id)
    out = out.resolve()
    global_root = (ROOT / "analista/generado").resolve()
    if out == global_root:
        raise SystemExit("La salida de Fase 10 no puede sobrescribir analista/generado")
    out.mkdir(parents=True, exist_ok=True)

    fuente_local = out / "fuente.jsonl"
    unidades_local = out / "unidades.jsonl"
    dump_jsonl(fuente_local, [source])
    dump_jsonl(unidades_local, work_units)

    run_conceptos(args.obra_id, fuente_local, unidades_local, out)
    run_definiciones(args.obra_id, fuente_local, unidades_local, out)
    run_afirmaciones(args.obra_id, unidades_local, out)
    formula_result, formula_profile = run_formulas(args.obra_id, unidades_local, out)
    run_relaciones(args.obra_id, fuente_local, unidades_local, out)
    run_limitadores(args.obra_id, unidades_local, out)

    product_names = [
        "fuente.jsonl",
        "unidades.jsonl",
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
        "cobertura-conceptos.jsonl",
        "cobertura-definiciones.jsonl",
        "cobertura-afirmaciones.jsonl",
        "cobertura-formulas.jsonl",
        "cobertura-relaciones.jsonl",
        "cobertura-limitadores.jsonl",
    ]
    missing = [name for name in product_names if not (out / name).is_file()]
    if missing:
        raise SystemExit(f"Productos faltantes tras extracción: {missing}")

    formula_calibration = {
        "perfil": None,
        "perfil_sha256": None,
        "version_produccion": formula_result.get("version"),
        "perfil_calibrado": bool(formula_result.get("perfil_calibrado", False)),
    }
    if formula_profile is not None:
        formula_calibration["perfil"] = str(formula_profile.relative_to(ROOT))
        formula_calibration["perfil_sha256"] = sha256(formula_profile)

    manifest = {
        "version": VERSION,
        "obra_id": args.obra_id,
        "titulo": source.get("titulo"),
        "glosario_tecnico": glossaries[0],
        "unidades": len(work_units),
        "fase": "4A-4F_repeticion_controlada",
        "comparacion_interobra": False,
        "calibracion": {"formulas": formula_calibration},
        "productos": {name: sha256(out / name) for name in product_names},
    }
    manifest_path = out / "manifest-extractores.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "obra_id": args.obra_id,
                "titulo": source.get("titulo"),
                "unidades": len(work_units),
                "productos": len(product_names),
                "formulas_version": formula_result.get("version"),
                "formulas_perfil_calibrado": bool(formula_result.get("perfil_calibrado", False)),
                "manifest_sha256": sha256(manifest_path),
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
