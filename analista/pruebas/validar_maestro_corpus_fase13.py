#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
import tempfile
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "motores"))
from ensamblador_maestro_corpus_fase13 import (
    build_master_extras,
    concept_record,
    init_db,
    json_text,
    sha256_file,
    stable_id,
)


def ref(obra: str, rid: str, tipo: str, datos: dict | None = None) -> dict:
    return {
        "obra_id": obra,
        "titulo_obra": "Obra A",
        "schema_maestro": "1.4.1",
        "registro_id": rid,
        "tipo_registro_origen": tipo,
        "estado_extraccion": "extraido",
        "estado_verificacion": "verificado",
        "estado_auditoria": "auditado",
        "estatus_enunciativo": "afirmacion_autoral" if tipo == "afirmacion" else None,
        "fuente_id": "SRC-A",
        "unidad_id": "U1",
        "localizacion": {"ruta": "a.txt", "linea_inicio": 1, "linea_fin": 1},
        "texto_literal": rid,
        "normalizacion_formal": None,
        "normalizacion_lexica": None,
        "datos_documentales": datos or {},
    }


def group(motor: str, key: str, refs: list[dict], *, identity: str = "no_determinada") -> dict:
    return {
        "id": stable_id("F11G", {"motor": motor, "clave": key}),
        "clave_recuperacion": key,
        "criterio_agrupacion": "regresion_fase13",
        "estado_identidad_interobra": identity,
        "equivalencia_inferida": False,
        "complementariedad_inferida": False,
        "contradiccion_inferida": False,
        "resolucion_doctrinal": "no_realizada",
        "obra_ids": ["A"],
        "registros": refs,
    }


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="fase13-regresion-") as tmp:
        base = Path(tmp)
        masters = base / "maestros"
        masters.mkdir()
        db = init_db(base / "index.sqlite")

        cg = group("conceptos_corpus", "ego", [ref("A", "C1", "concepto", {"formas_literales_observadas": ["ego"]})])
        ag = group("afirmaciones_corpus", "ego", [ref("A", "A1", "afirmacion", {"clasificacion_afirmacion": "afirmacion_explicita"})])
        og = group("orden_recurrencia", "ego", [ref("A", "C1", "concepto", {"apariciones_totales": 1})])
        fg = group("formulas_corpus", "x=y", [ref("A", "F1", "formula", {"formula_literal": "x=y"})], identity="no_aplica")
        for motor, key, g in (
            ("conceptos_corpus", "ego", cg),
            ("afirmaciones_corpus", "ego", ag),
            ("orden_recurrencia", "ego", og),
            ("formulas_corpus", "x=y", fg),
        ):
            db.execute("INSERT INTO groups(motor,key,gid,payload) VALUES(?,?,?,?)", (motor, key, g["id"], json_text(g)))
        db.execute("INSERT INTO concept_source(obra,rid,key) VALUES('A','C1','ego')")
        db.execute("INSERT INTO assertion_source(obra,rid,key) VALUES('A','A1','ego')")
        db.execute("INSERT INTO formula_source(obra,rid,gid) VALUES('A','F1',?)", (fg["id"],))
        db.commit()

        master = {
            "id": "MASTER-A",
            "tipo_registro": "expediente_maestro_obra",
            "schema_version": "1.4.1",
            "estado_verificacion": "verificado",
            "obra_id": "A",
            "titulo": "Obra A",
            "apariciones_conceptuales": [
                {"id": "AP1", "concepto_id": "C1", "unidad_id": "U1"}
            ],
            "formulas": [
                {
                    "id": "F1", "tipo_registro": "formula", "estado_extraccion": "extraido",
                    "estado_verificacion": "verificado", "estado_auditoria": "auditado", "estatus_enunciativo": None,
                    "fuente_id": "SRC-A", "unidad_id": "U1", "localizacion": {"ruta":"a.txt","linea_inicio":1,"linea_fin":1},
                    "texto_literal": "x=y", "normalizacion_formal": "x=y", "normalizacion_lexica": None,
                    "formula_literal": "x=y", "simbolos_literales": ["x","y"], "contexto_unidad_ids": ["U1"], "clasificacion_formula": "formula_explicita"
                }
            ],
            "restricciones_alcance": [
                {
                    "id": "R1", "tipo_registro": "restriccion_alcance", "estado_extraccion": "extraido",
                    "estado_verificacion": "verificado", "estado_auditoria": "auditado", "estatus_enunciativo": None,
                    "fuente_id": "SRC-A", "unidad_id": "U1", "localizacion": {"ruta":"a.txt","linea_inicio":1,"linea_fin":1},
                    "texto_literal": "solo si p", "normalizacion_formal": None, "normalizacion_lexica": None,
                    "afirmacion_limitada_id": "A1", "tipo_restriccion": "condicional",
                    "fragmento_restriccion_literal": "solo si p", "clasificacion_restriccion": "restriccion_explicita"
                },
                {
                    "id": "R2", "tipo_registro": "restriccion_alcance", "estado_extraccion": "extraido",
                    "estado_verificacion": "verificado", "estado_auditoria": "auditado", "estatus_enunciativo": None,
                    "fuente_id": "SRC-A", "unidad_id": "U1", "localizacion": {"ruta":"a.txt","linea_inicio":1,"linea_fin":1},
                    "texto_literal": "en este caso", "normalizacion_formal": None, "normalizacion_lexica": None,
                    "afirmacion_limitada_id": None, "tipo_restriccion": "contextual",
                    "fragmento_restriccion_literal": "en este caso", "clasificacion_restriccion": "restriccion_explicita"
                }
            ]
        }
        master_path = masters / "A.json"
        master_path.write_text(json.dumps(master, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
        manifest = {"maestros": [{"obra_id": "A", "ruta_en_zip": "maestros/A.json", "sha256": sha256_file(master_path)}]}
        ptrs, formula_links, restrictions = build_master_extras(db, manifest, masters)
        assert formula_links == 1
        assert restrictions == 2

        dossier = {
            "id": stable_id("F12X", {"clave": "ego", "grupo_conceptos": cg["id"]}),
            "clave_recuperacion": "ego",
            "criterio_clave": "clave_documental_de_fase11_no_identidad_conceptual_interobra",
            "fuentes_fase11": {"conceptos_corpus": cg["id"], "definiciones_corpus": None, "afirmaciones_corpus": ag["id"], "orden_recurrencia": og["id"]},
            "multiplicidad": {"obras_con_clave":1,"conceptos_registrados_total":1,"apariciones_totales_documentadas":1,"definiciones_registros_total":0,"predicaciones_registros_total":1,"vinculos_predicacion_concepto_total":1},
            "obras": [{"obra_id":"A","conceptos_registrados":1,"apariciones_totales_documentadas":1,"definiciones_registros":0,"predicaciones_registros":1,"vinculos_predicacion_concepto":1,"relaciones_como_sujeto":0,"relaciones_como_objeto":0,"negaciones_recuperadas_por_forma":0,"excepciones_vinculadas_a_predicaciones":0,"formas_literales_observadas":["ego"]}],
            "formas_literales_observadas": ["ego"],
            "variaciones_terminologicas": [], "relaciones_explicitas": [],
            "negaciones_recuperadas_por_forma": [], "excepciones_vinculadas_a_predicaciones": [],
            "hallazgos": []
        }
        row = concept_record(db, dossier, ptrs)
        schema = json.loads((ROOT / "esquema/concepto-maestro-corpus-fase13-v1.0.0.schema.json").read_text(encoding="utf-8"))
        jsonschema.Draft202012Validator(schema).validate(row)
        assert len(row["formulas"]) == 1
        assert row["formulas"][0]["estado_vinculo_conceptual"] == "no_determinado"
        assert row["formulas"][0]["criterio_vinculo"] == "coocurrencia_en_unidad_documentada_solo_para_recuperacion"
        assert row["formula_concepto_inferida"] is False
        assert len(row["restricciones"]) == 1
        assert row["restricciones"][0]["referencia"]["registro_id"] == "R1"
        assert row["restricciones"][0]["criterio_vinculo"] == "afirmacion_limitada_id_documentado"
        unlinked = json.loads(db.execute("SELECT payload FROM restrictions WHERE rid='R2'").fetchone()[0])
        assert unlinked["claves_conceptuales_vinculadas"] == []
        assert unlinked["criterio_vinculo"] == "sin_vinculo_conceptual_documentado"
        assert row["resolucion_doctrinal"] == "no_realizada"

    print("OK Fase 13: fórmulas sólo por recuperación contextual y restricciones sólo por referencia explícita")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
