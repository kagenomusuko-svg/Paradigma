#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
MOTOR_DIR = ROOT / "motores"
SCHEMA_DIR = ROOT / "esquema"
sys.path.insert(0, str(MOTOR_DIR))

from consulta_literal_fase14 import (
    NEGATIVE_EVIDENCE,
    NOT_DETERMINED,
    execute_queries,
    sha256_file,
)


def ref(rid: str, tipo: str, datos: dict | None = None, *, auditado: bool = True) -> dict:
    return {
        "obra_id": "A",
        "titulo_obra": "Obra A",
        "schema_maestro": "1.4.1",
        "registro_id": rid,
        "tipo_registro_origen": tipo,
        "estado_extraccion": "extraido",
        "estado_verificacion": "verificado",
        "estado_auditoria": "auditado" if auditado else None,
        "estatus_enunciativo": "afirmacion_autoral" if tipo == "afirmacion" else None,
        "fuente_id": "SRC-A",
        "unidad_id": "U1",
        "localizacion": {"ruta": "a.txt", "linea_inicio": 1, "linea_fin": 1},
        "texto_literal": rid,
        "normalizacion_formal": None,
        "normalizacion_lexica": None,
        "datos_documentales": datos or {},
    }


def concept_row(key: str, forms: list[str]) -> dict:
    return {
        "id": "F13C-" + key.replace(" ", "-").upper(),
        "tipo_registro": "concepto_maestro_corpus",
        "schema_version": "1.0.0",
        "clave_recuperacion": key,
        "formas_literales": forms,
        "definiciones_explicitas": [],
        "predicaciones": [],
        "negaciones": [],
        "variantes_recuperacion": [],
        "relaciones_explicitas": [],
        "excepciones": [],
        "trazabilidad": {"registros_conceptuales": []},
    }


def write_json(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n")


def persist_storage(base: Path, closure: dict) -> Path:
    closure_path = base / "cierre-fase13.json"
    write_json(closure_path, closure)
    products = []
    for name, tipo in (
        ("maestro-corpus.json", "maestro_corpus"),
        ("conceptos-maestro-corpus.jsonl", "conceptos_maestro_corpus"),
        ("formulas-corpus.jsonl", "formulas_corpus"),
        ("restricciones-corpus.jsonl", "restricciones_corpus"),
    ):
        products.append({"tipo": tipo, "ruta_en_zip": "fase13/" + name, "sha256": sha256_file(base / name)})
    storage = {
        "version": "1.0.0",
        "fase": 13,
        "gate": {"fase13_cerrada": True, "cierre_sha256": sha256_file(closure_path)},
        "productos": products,
    }
    path = base / "almacenamiento-fase13.json"
    write_json(path, storage)
    return path


def main() -> int:
    schema = json.loads((SCHEMA_DIR / "respuesta-consulta-literal-fase14-v1.0.0.schema.json").read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema)

    with tempfile.TemporaryDirectory(prefix="fase14-regresion-") as tmp:
        base = Path(tmp)
        ego = concept_row("ego", ["ego", "yo"])
        otro = concept_row("yo puro", ["yo puro"])
        ego["definiciones_explicitas"] = [ref("D1", "definicion", {"clasificacion_definicion": "definicion_explicita"})]
        ego["predicaciones"] = [ref("A1", "afirmacion", {"clasificacion_afirmacion": "afirmacion_explicita"})]
        ego["trazabilidad"]["registros_conceptuales"] = [ref("C1", "concepto", {"apariciones_totales": 2})]
        ego["negaciones"] = [{
            "grupo_id": "N1", "clave_recuperacion": "negacion::ego", "criterio_agrupacion": "regresion",
            "estado_identidad_interobra": "no_determinada", "registros": [ref("NREF1", "afirmacion")]
        }]
        ego["variantes_recuperacion"] = [{
            "grupo_id": "V1", "clave_recuperacion": "yo", "criterio_agrupacion": "forma_documentada",
            "estado_identidad_interobra": "no_determinada", "registros": [ref("VREF1", "concepto")]
        }]
        ego["relaciones_explicitas"] = [{
            "grupo_id": "REL1", "clave_recuperacion": json.dumps(["ego", "=", "yo puro"], ensure_ascii=False, separators=(",", ":")),
            "criterio_agrupacion": "tripleta_formal_sujeto_relacion_objeto_solo_para_recuperacion",
            "estado_identidad_interobra": "no_determinada", "registros": [ref("R1", "relacion_explicita")]
        }]
        ego["excepciones"] = [{
            "grupo_id": "E1", "clave_recuperacion": "excepcion::ego", "criterio_agrupacion": "afirmacion_limitada_id_documentado",
            "estado_identidad_interobra": "no_determinada", "registros": [ref("ERef1", "excepcion")]
        }]

        master = {
            "id": "F13M-REGRESION",
            "tipo_registro": "expediente_maestro_corpus",
            "fase": 13,
            "estado_auditoria": "auditado",
            "clausura_descriptiva": {"resolucion_doctrinal": "no_realizada"},
        }
        write_json(base / "maestro-corpus.json", master)
        write_jsonl(base / "conceptos-maestro-corpus.jsonl", [ego, otro])
        formula = {
            "id": "F13F-1",
            "tipo_registro": "formula_corpus_auditada",
            "grupo_fase11_id": "FG1",
            "clave_recuperacion": "E=ego+1",
            "criterio_agrupacion": "formula_formal_exacta",
            "estado_vinculo_conceptual": "no_determinado",
            "resolucion_doctrinal": "no_realizada",
            "registros": [ref("F1", "formula", {"formula_literal": "E = ego + 1"})],
        }
        write_jsonl(base / "formulas-corpus.jsonl", [formula])
        write_jsonl(base / "restricciones-corpus.jsonl", [])
        closure = {"fase": 13, "fase13_cerrada": True}
        storage = persist_storage(base, closure)

        queries = [
            {"tipo": "definiciones_explicitas", "termino": "ego"},
            {"tipo": "definiciones_explicitas", "termino": "yo"},
            {"tipo": "predicaciones", "termino": "ego"},
            {"tipo": "negaciones", "termino": "ego"},
            {"tipo": "apariciones", "termino": "ego"},
            {"tipo": "variantes_terminologicas", "termino": "ego"},
            {"tipo": "excepciones", "termino": "ego"},
            {"tipo": "formulas_contienen", "termino": "ego"},
            {"tipo": "relacion_explicita", "termino": "ego", "relacion": "=", "objeto": "yo puro"},
            {"tipo": "definiciones_explicitas", "termino": "ausente"},
            {"tipo": "relacion_explicita", "termino": "ego", "relacion": "=", "objeto": "yo"},
        ]
        responses = execute_queries(base, storage, queries)
        for response in responses:
            validator.validate(response)
            assert response["clausura_descriptiva"]["busqueda_semantica_inferida"] is False
            assert response["clausura_descriptiva"]["sintesis_doctrinal"] is False

        assert responses[0]["resultados"][0]["referencia"]["registro_id"] == "D1"
        assert responses[1]["estado"] == "hallazgo_auditado"
        assert responses[1]["resolucion_consulta"]["termino"]["criterio"] == "forma_literal_exacta_sin_fusion_conceptual"
        assert responses[7]["resultados"][0]["estado_vinculo_conceptual"] == "no_determinado"
        assert responses[8]["resultados"][0]["referencia"]["registro_id"] == "R1"
        assert responses[9]["estado"] == "sin_hallazgo_auditado"
        assert responses[9]["mensaje"] == NEGATIVE_EVIDENCE
        assert responses[10]["estado"] == "no_determinado_por_el_corpus"
        assert responses[10]["mensaje"] == NOT_DETERMINED
        assert responses[10]["resultados"] == []

        bad = concept_row("riesgo", ["riesgo"])
        bad["predicaciones"] = [ref("BAD1", "afirmacion", auditado=False)]
        write_jsonl(base / "conceptos-maestro-corpus.jsonl", [ego, otro, bad])
        storage = persist_storage(base, closure)
        try:
            execute_queries(base, storage, [{"tipo": "predicaciones", "termino": "riesgo"}])
        except SystemExit as exc:
            assert "no auditada/verificada" in str(exc)
        else:
            raise AssertionError("F14 aceptó una referencia no auditada")

    print("OK Fase 14: recuperación literal, negativas diferenciadas y ninguna equivalencia inferida")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
