#!/usr/bin/env python3
"""Prueba la infraestructura de Fase 8 sin fabricar un patrón de oro real.

Usa un fixture sintético construido a partir de tres relaciones ya extraídas solo
para comprobar el contador de TP/FP/FN del evaluador. Este archivo NO anota el
patrón de oro de producción.
"""
from __future__ import annotations

import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
CAL = ROOT / "analista/calibracion"
SELECTOR = CAL / "seleccionar_muestra.py"
EVALUATOR = CAL / "evaluar.py"
SCHEMA = CAL / "patron-oro-v1.0.0.schema.json"
GENERATED = ROOT / "analista/generado"
RELATION_UNIT = "UT-BEF6D53FB3C7"


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def dump_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows),
        encoding="utf-8",
    )


def import_evaluator():
    spec = importlib.util.spec_from_file_location("evaluar_calibracion", EVALUATOR)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_evaluator(
    gold: Path,
    generated: Path,
    output: Path,
    expected_code: int = 0,
    *,
    manifest: bool = False,
) -> dict:
    selector = "--manifiesto" if manifest else "--patron"
    result = subprocess.run(
        [
            sys.executable,
            str(EVALUATOR),
            selector,
            str(gold),
            "--generado",
            str(generated),
            "--salida",
            str(output),
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert result.returncode == expected_code, (result.returncode, result.stdout, result.stderr)
    if expected_code != 0:
        return {}
    return json.loads(output.read_text(encoding="utf-8"))


def gold_item(actual: dict) -> dict:
    return {
        "tipo_registro": actual["tipo_registro"],
        "texto_literal": actual["texto_literal"],
        "linea_inicio": actual["linea_inicio"],
        "linea_fin": actual["linea_fin"],
        "clasificacion": actual["clasificacion"],
        "estatus_enunciativo": actual["estatus_enunciativo"],
        "concepto_designacion": actual["concepto_designacion"],
        "sujeto_designacion": actual["sujeto_designacion"],
        "objeto_designacion": actual["objeto_designacion"],
        "termino_a_literal": actual["termino_a_literal"],
        "termino_b_literal": actual["termino_b_literal"],
        "objeto_negado_literal": actual["objeto_negado_literal"],
        "fragmento_literal": actual["fragmento_literal"],
    }


def report(payload: dict) -> dict:
    rows = payload["reportes"]
    return next(
        row
        for row in rows
        if row["motor"] == "relaciones_explicitas" and row["estrato"] == "combinado"
    )


def main() -> int:
    # El selector necesita los productos raros para reconstruir el mismo lock.
    subprocess.run([sys.executable, "analista/motores/formulas.py"], cwd=ROOT, check=True)
    subprocess.run([sys.executable, "analista/motores/limitadores.py"], cwd=ROOT, check=True)
    selected = subprocess.run(
        [sys.executable, str(SELECTOR)], cwd=ROOT, text=True, capture_output=True, check=True
    )
    selector_report = json.loads(selected.stdout.strip().splitlines()[-1])
    assert selector_report == {
        "lock_verificado": True,
        "unidades_unicas": 96,
        "general": 31,
        "desafios": {
            "conceptos_apariciones": 10,
            "definiciones": 7,
            "afirmaciones": 12,
            "formulas": 18,
            "relaciones_explicitas": 2,
            "limitadores": 27,
        },
    }

    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    evaluator = import_evaluator()

    with tempfile.TemporaryDirectory() as temporary:
        temporary = Path(temporary)
        fixture = temporary / "generado"
        fixture.mkdir()
        # Aislamiento real: para evaluar relaciones no se materializan salidas de
        # fórmulas, afirmaciones, definiciones, limitadores ni apariciones.
        shutil.copy2(GENERATED / "conceptos.jsonl", fixture / "conceptos.jsonl")
        shutil.copy2(GENERATED / "relaciones-explicitas.jsonl", fixture / "relaciones-explicitas.jsonl")

        actual = [
            item
            for item in evaluator.extracted_items(fixture, "relaciones_explicitas")
            if item["unidad_id"] == RELATION_UNIT
        ]
        assert len(actual) == 3, "El fixture de relaciones cambió; revisar la prueba de infraestructura."

        entry = {
            "version": "1.0.0",
            "obra_id": "AA-SP-V1",
            "unidad_id": RELATION_UNIT,
            "motor": "relaciones_explicitas",
            "estratos": ["desafio"],
            "revision_manual": True,
            "items_esperados": [gold_item(item) for item in actual],
            "observacion": "Fixture sintético exclusivo para probar el evaluador; no es patrón de oro de producción.",
        }
        assert not list(validator.iter_errors(entry))

        gold = temporary / "gold.jsonl"
        output = temporary / "report.json"
        dump_jsonl(gold, [entry])
        perfect = report(run_evaluator(gold, fixture, output))
        assert perfect["version"] == "1.1.0"
        assert perfect["positivos_esperados"] == 3
        assert perfect["predicciones_emitidas"] == 3
        assert perfect["verdaderos_positivos"] == 3
        assert perfect["precision"] == 1
        assert perfect["cobertura"] == 1
        assert perfect["falsos_positivos"] == 0
        assert perfect["falsos_negativos"] == 0

        # La misma única anotación a través de un manifiesto debe producir el
        # mismo reporte y no intentar abrir salidas de motores sin gold.
        manifest = temporary / "manifest.json"
        manifest.write_text(
            json.dumps(
                {"version": "1.0.0", "obra_id": "AA-SP-V1", "archivos": ["gold.jsonl"]},
                sort_keys=True,
            ) + "\n",
            encoding="utf-8",
        )
        manifest_payload = run_evaluator(manifest, fixture, output, manifest=True)
        assert report(manifest_payload) == perfect
        assert {row["motor"] for row in manifest_payload["reportes"]} == {"relaciones_explicitas"}

        fewer = dict(entry)
        fewer["items_esperados"] = entry["items_esperados"][:-1]
        dump_jsonl(gold, [fewer])
        fp = report(run_evaluator(gold, fixture, output))
        assert fp["positivos_esperados"] == 2
        assert fp["predicciones_emitidas"] == 3
        assert fp["verdaderos_positivos"] == 2
        assert fp["falsos_positivos"] == 1
        assert fp["falsos_negativos"] == 0

        extra = json.loads(json.dumps(entry))
        fake = dict(extra["items_esperados"][0])
        fake["texto_literal"] = fake["texto_literal"] + " [esperado inexistente]"
        extra["items_esperados"].append(fake)
        dump_jsonl(gold, [extra])
        fn = report(run_evaluator(gold, fixture, output))
        assert fn["positivos_esperados"] == 4
        assert fn["predicciones_emitidas"] == 3
        assert fn["verdaderos_positivos"] == 3
        assert fn["falsos_positivos"] == 0
        assert fn["falsos_negativos"] == 1

        dump_jsonl(gold, [entry, entry])
        run_evaluator(gold, fixture, output, expected_code=1)

    print(
        "OK infraestructura Fase 8: lock reproducible (96 unidades); esquema manual válido; "
        "manifiesto aislado por motor; reporte v1.1 expone denominadores y distingue TP/FP/FN; "
        "duplicados unidad–motor rechazados."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
