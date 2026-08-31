#!/usr/bin/env python3
"""Repetición controlada de extractores 4A–4F para una obra de Fase 10.

Ejecuta todos los motores sobre las unidades de una sola obra. La recuperación
conceptual está habilitada con independencia de la presencia de glosario:

- un glosario técnico propio puede aportar evidencia explícita privilegiada;
- una declaración inequívoca del cuerpo de la misma obra también puede aportar
  evidencia de identidad;
- recurrencia, similitud, proximidad o patrones ambiguos permanecen candidatos.

Nunca reutiliza un glosario de otra obra ni compara obras.
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
VERSION = "1.4.0"

CONCEPTS_VERSION = "1.3.1"
DEFINITIONS_VERSION = "1.3.0"
ASSERTIONS_VERSION = "1.2.0"
RELATIONS_VERSION = "1.2.1"
LIMITERS_VERSION = "1.1.1"


def load_jsonl(path: Path) -> list[dict]:
    if not path.is_file():
        raise SystemExit(f"No existe insumo requerido: {path}")
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def dump_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows), encoding="utf-8")


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


def run_conceptos(obra_id: str, fuente: Path, unidades: Path, out: Path) -> dict:
    m = load_module("fase10_conceptos_compuesto", ROOT / "analista/motores/conceptos_compuesto_fase10.py")
    result = m.run(obra_id=obra_id, fuentes=fuente, unidades=unidades,
                   apariciones=out / "apariciones-conceptuales.jsonl", conceptos=out / "conceptos.jsonl",
                   cobertura=out / "cobertura-conceptos.jsonl")
    if result.get("version") != CONCEPTS_VERSION:
        raise SystemExit(f"Versión inesperada de 4A: {result.get('version')}")
    return result


def run_definiciones(obra_id: str, fuente: Path, unidades: Path, out: Path) -> dict:
    m = load_module("fase10_definiciones_compuesto", ROOT / "analista/motores/definiciones_compuesto_fase10.py")
    result = m.run(obra_id=obra_id, fuentes=fuente, unidades=unidades, conceptos=out / "conceptos.jsonl",
                   salida=out / "definiciones.jsonl", cobertura=out / "cobertura-definiciones.jsonl")
    if result.get("version") != DEFINITIONS_VERSION:
        raise SystemExit(f"Versión inesperada de 4B: {result.get('version')}")
    return result


def run_afirmaciones(obra_id: str, unidades: Path, out: Path) -> dict:
    m = load_module("fase10_afirmaciones_compuesto", ROOT / "analista/motores/afirmaciones_compuesto_fase10.py")
    result = m.run(obra_id=obra_id, unidades=unidades, conceptos=out / "conceptos.jsonl",
                   salida=out / "afirmaciones-candidatas.jsonl", cobertura=out / "cobertura-afirmaciones.jsonl")
    if result.get("version") != ASSERTIONS_VERSION:
        raise SystemExit(f"Versión inesperada de 4C: {result.get('version')}")
    return result


def run_formulas(obra_id: str, unidades: Path, out: Path) -> tuple[dict, Path | None]:
    m = load_module("fase10_formulas_produccion", ROOT / "analista/motores/formulas_perfil_fase10.py")
    profile = DEFAULT_CALIBRATION_ROOT / obra_id / "perfil-extractores.json"
    profile_arg = profile if profile.is_file() else None
    result = m.run(obra_id=obra_id, unidades=unidades, salida=out / "formulas-candidatas.jsonl",
                   cobertura=out / "cobertura-formulas.jsonl", perfil=profile_arg)
    return result, profile_arg


def run_relaciones(obra_id: str, unidades: Path, out: Path) -> dict:
    m = load_module("fase10_relaciones_compuesto", ROOT / "analista/motores/relaciones_compuesto_fase10.py")
    result = m.run(obra_id=obra_id, unidades=unidades, conceptos=out / "conceptos.jsonl",
                   salida=out / "relaciones-explicitas.jsonl", cobertura=out / "cobertura-relaciones.jsonl")
    if result.get("version") != RELATIONS_VERSION:
        raise SystemExit(f"Versión inesperada de 4E: {result.get('version')}")
    return result


def run_limitadores(obra_id: str, unidades: Path, out: Path) -> None:
    m = load_module("fase10_limitadores", ROOT / "analista/motores/limitadores.py")
    if getattr(m, "VERSION", None) != LIMITERS_VERSION:
        raise SystemExit(f"Versión inesperada de 4F: {getattr(m, 'VERSION', None)}")
    m.PILOTO = obra_id
    with argv_temporal([str(ROOT / "analista/motores/limitadores.py"), "--unidades", str(unidades), "--output-root", str(out)]):
        if m.main() != 0:
            raise SystemExit("Falló limitadores")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--obra-id", required=True)
    ap.add_argument("--fuentes", type=Path, default=DEFAULT_FUENTES)
    ap.add_argument("--unidades", type=Path, default=DEFAULT_UNIDADES)
    ap.add_argument("--output-root", type=Path)
    args = ap.parse_args()

    sources = load_jsonl(args.fuentes); units = load_jsonl(args.unidades)
    selected = [row for row in sources if row.get("id") == args.obra_id]
    if len(selected) != 1:
        raise SystemExit(f"Se esperaba una fuente para {args.obra_id}; encontradas={len(selected)}")
    source = selected[0]
    work_units = [row for row in units if row.get("fuente_id") == args.obra_id]
    if not work_units:
        raise SystemExit(f"La obra {args.obra_id} no tiene unidades de Fase 3")
    if len({row["id"] for row in work_units}) != len(work_units):
        raise SystemExit(f"IDs de unidad duplicados en {args.obra_id}")

    glossaries = [route for route in source.get("rutas_derivadas", []) if str(route).endswith("99-glosario.md")]
    if len(glossaries) > 1:
        raise SystemExit(f"Fase 10 controlada v{VERSION}: {args.obra_id} tiene más de un glosario técnico explícito; no se resolverá automáticamente.")

    out = (args.output_root or (DEFAULT_OBRAS_ROOT / args.obra_id)).resolve()
    global_root = (ROOT / "analista/generado").resolve()
    if out == global_root:
        raise SystemExit("La salida de Fase 10 no puede sobrescribir analista/generado")
    out.mkdir(parents=True, exist_ok=True)

    fuente_local = out / "fuente.jsonl"; unidades_local = out / "unidades.jsonl"
    dump_jsonl(fuente_local, [source]); dump_jsonl(unidades_local, work_units)

    concept_result = run_conceptos(args.obra_id, fuente_local, unidades_local, out)
    definition_result = run_definiciones(args.obra_id, fuente_local, unidades_local, out)
    assertion_result = run_afirmaciones(args.obra_id, unidades_local, out)
    formula_result, formula_profile = run_formulas(args.obra_id, unidades_local, out)
    relation_result = run_relaciones(args.obra_id, unidades_local, out)
    run_limitadores(args.obra_id, unidades_local, out)

    perfil_conceptual = "glosario_tecnico_explicito" if glossaries else "sin_glosario_tecnico_explicito"
    product_names = ["fuente.jsonl","unidades.jsonl","apariciones-conceptuales.jsonl","conceptos.jsonl","definiciones.jsonl",
        "afirmaciones-candidatas.jsonl","formulas-candidatas.jsonl","relaciones-explicitas.jsonl","distinciones.jsonl","negaciones.jsonl",
        "excepciones.jsonl","restricciones-alcance.jsonl","cobertura-conceptos.jsonl","cobertura-definiciones.jsonl","cobertura-afirmaciones.jsonl",
        "cobertura-formulas.jsonl","cobertura-relaciones.jsonl","cobertura-limitadores.jsonl"]
    missing = [name for name in product_names if not (out / name).is_file()]
    if missing:
        raise SystemExit(f"Productos faltantes tras extracción: {missing}")

    formula_calibration = {"perfil":None,"perfil_sha256":None,"version_produccion":formula_result.get("version"),
                           "perfil_calibrado":bool(formula_result.get("perfil_calibrado",False))}
    if formula_profile is not None:
        formula_calibration["perfil"] = str(formula_profile.relative_to(ROOT)); formula_calibration["perfil_sha256"] = sha256(formula_profile)

    extractor_versions = {"conceptos_apariciones":CONCEPTS_VERSION,"definiciones":DEFINITIONS_VERSION,"afirmaciones":ASSERTIONS_VERSION,
                          "formulas":formula_result.get("version"),"relaciones_explicitas":RELATIONS_VERSION,"limitadores":LIMITERS_VERSION}
    if not isinstance(extractor_versions["formulas"], str) or not extractor_versions["formulas"]:
        raise SystemExit("El motor de fórmulas no declaró versión de producción")

    manifest = {
        "version": VERSION, "obra_id": args.obra_id, "titulo": source.get("titulo"),
        "glosario_tecnico": glossaries[0] if glossaries else None, "perfil_conceptual": perfil_conceptual,
        "limitaciones_conceptuales": {
            "extraccion_conceptual_habilitada": True,
            "recuperacion_candidatos_habilitada": True,
            "identidad_confirmada_requiere_evidencia_explicita": True,
            "candidatos_sin_evidencia_permanecen_no_determinados": True,
            "identidades_conceptuales_inferidas": False,
            "glosario_interobra_reutilizado": False,
            "interpretacion_cero_registros": "no_autoriza_afirmar_ausencia_semantica",
        },
        "unidades": len(work_units), "fase": "4A-4F_repeticion_controlada", "comparacion_interobra": False,
        "versiones_extractores": extractor_versions, "calibracion": {"formulas": formula_calibration},
        "resumen_extraccion": {
            "conceptos_confirmados": concept_result.get("conceptos_confirmados", 0),
            "conceptos_confirmados_glosario": concept_result.get("conceptos_confirmados_glosario", 0),
            "conceptos_confirmados_cuerpo": concept_result.get("conceptos_confirmados_cuerpo", 0),
            "conceptos_candidatos": concept_result.get("conceptos_candidatos", 0),
            "apariciones_conceptuales": concept_result.get("apariciones", 0),
            "definiciones": definition_result.get("registros", 0), "afirmaciones": assertion_result.get("registros", 0),
            "relaciones": relation_result.get("registros", 0),
        },
        "productos": {name: sha256(out / name) for name in product_names},
    }
    manifest_path = out / "manifest-extractores.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"obra_id":args.obra_id,"titulo":source.get("titulo"),"unidades":len(work_units),"perfil_conceptual":perfil_conceptual,
                      "conceptos_confirmados":concept_result.get("conceptos_confirmados",0),"conceptos_candidatos":concept_result.get("conceptos_candidatos",0),
                      "productos":len(product_names),"versiones_extractores":extractor_versions,"manifest_sha256":sha256(manifest_path)},ensure_ascii=False,sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
