#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
MOTORES = ROOT / "motores"
sys.path.insert(0, str(MOTORES))

from afirmaciones_corpus_fase11 import MotorAfirmacionesCorpus
from conceptos_corpus_fase11 import MotorConceptosCorpus
from definiciones_corpus_fase11 import MotorDefinicionesCorpus
from distribucion_por_obra_fase11 import MotorDistribucionPorObra
from formulas_corpus_fase11 import MotorFormulasCorpus
from negaciones_excepciones_corpus_fase11 import MotorNegacionesExcepcionesCorpus
from orden_recurrencia_corpus_fase11 import MotorOrdenRecurrencia
from relaciones_explicitas_corpus_fase11 import MotorRelacionesExplicitasCorpus
from variantes_terminologicas_corpus_fase11 import MotorVariantesTerminologicasCorpus

SCHEMA = json.loads((ROOT / "esquema/comparacion-corpus-fase11-v1.0.0.schema.json").read_text(encoding="utf-8"))


def base(rid: str, typ: str, text: str | None = None, norm: str | None = None) -> dict:
    return {
        "id": rid,
        "tipo_registro": typ,
        "schema_version": "1.0.0",
        "texto_literal": text,
        "normalizacion_formal": norm,
        "normalizacion_lexica": [norm.casefold()] if norm else None,
        "estatus_enunciativo": None,
        "estado_extraccion": "extraido",
        "estado_verificacion": "verificado",
        "estado_auditoria": "auditado",
        "producido_por": {"motor": "prueba", "version": "1"},
    }


def make_master(obra: str, title: str, suffix: str) -> dict:
    c1 = base(f"CON-{suffix}A", "concepto", "Mediación", "Mediación")
    c1.update({
        "designacion_operativa": "Mediación",
        "aparicion_ids": [f"AP-{suffix}2", f"AP-{suffix}1"],
        "formas_literales_observadas": ["Mediación"],
        "estado_identidad_conceptual": "establecida_por_evidencia",
        "evidencia_identidad_ids": [f"AP-{suffix}1"],
        "normalizacion_lexica": ["mediación", "mediacion"],
    })
    c2 = base(f"CON-{suffix}B", "concepto", "Objeto", "Objeto")
    c2.update({
        "designacion_operativa": "Objeto",
        "aparicion_ids": [f"AP-{suffix}3"],
        "formas_literales_observadas": ["Objeto"],
        "estado_identidad_conceptual": "no_determinada",
        "evidencia_identidad_ids": [],
        "normalizacion_lexica": ["objeto"],
    })
    u1 = base(f"UT-{suffix}1", "unidad_textual", "uno")
    u1.update({"orden_textual": 0})
    u2 = base(f"UT-{suffix}2", "unidad_textual", "dos")
    u2.update({"orden_textual": 1})
    apps = []
    for aid, uid, line, cid, literal in [
        (f"AP-{suffix}2", u2["id"], 20, c1["id"], "Mediación"),
        (f"AP-{suffix}1", u1["id"], 10, c1["id"], "Mediación"),
        (f"AP-{suffix}3", u1["id"], 15, c2["id"], "Objeto"),
    ]:
        row = base(aid, "aparicion_conceptual", literal, literal)
        row.update({"unidad_id": uid, "fuente_id": obra, "concepto_id": cid, "localizacion": {"ruta": "x.md", "linea_inicio": line, "linea_fin": line}})
        apps.append(row)
    definition = base(f"DEF-{suffix}", "definicion", "Mediación es X", "Mediación es X")
    definition.update({"concepto_id": c1["id"], "unidad_id": u1["id"], "fuente_id": obra, "clasificacion_definicion": "definicion_explicita", "criterio_deteccion": "prueba"})
    assertion = base(f"AF-{suffix}", "afirmacion", "Mediación produce X", "Mediación produce X")
    assertion.update({"concepto_ids": [c1["id"], c2["id"]], "unidad_id": u1["id"], "fuente_id": obra, "clasificacion_afirmacion": "afirmacion_explicita", "criterio_deteccion": "prueba", "confianza_extraccion": 1.0, "sujeto_literal": "Mediación", "predicado_literal": "produce", "objeto_literal": "X"})
    formula = base(f"FOR-{suffix}", "formula", "A = B", "A = B")
    formula.update({"formula_literal": "A = B", "simbolos_literales": ["="], "contexto_unidad_ids": [u1["id"]], "unidad_id": u1["id"], "fuente_id": obra, "clasificacion_formula": "formula_explicita"})
    relation = base(f"REL-{suffix}", "relacion_explicita", "Mediación vincula Objeto", "Mediación vincula Objeto")
    relation.update({"sujeto_ref": c1["id"], "objeto_ref": c2["id"], "relacion_literal": "vincula", "clasificacion_relacion": "relacion_explicita", "unidad_id": u1["id"], "fuente_id": obra})
    neg = base(f"NEG-{suffix}", "negacion", "no X", "no X")
    neg.update({"objeto_negado_literal": "no X", "alcance_literal": None, "clasificacion_negacion": "negacion_explicita", "unidad_id": u1["id"], "fuente_id": obra})
    exc = base(f"EXC-{suffix}", "excepcion", "excepto Y", "excepto Y")
    exc.update({"fragmento_exceptivo_literal": "excepto Y", "afirmacion_limitada_id": assertion["id"], "clasificacion_excepcion": "excepcion_explicita", "unidad_id": u1["id"], "fuente_id": obra})
    master = base(f"MAE-{suffix}", "expediente_maestro_obra")
    master.update({
        "schema_version": "1.4.1",
        "obra_id": obra,
        "titulo": title,
        "unidades": [u2, u1],
        "apariciones_conceptuales": apps,
        "conceptos": [c1, c2],
        "definiciones": [definition],
        "afirmaciones": [assertion],
        "formulas": [formula],
        "relaciones_explicitas": [relation],
        "distinciones": [],
        "negaciones": [neg],
        "excepciones": [exc],
        "restricciones_alcance": [],
        "hallazgos_auditoria": [],
        "reportes_cobertura": [],
    })
    return master


def main() -> int:
    masters = [make_master("OBRA-A", "Obra A", "A"), make_master("OBRA-B", "Obra B", "B")]
    metas = [
        {"obra_id": m["obra_id"], "titulo": m["titulo"], "schema_version": m["schema_version"], "sha256": ("0" if i == 0 else "1") * 64}
        for i, m in enumerate(masters)
    ]
    motors = [
        MotorConceptosCorpus(), MotorDefinicionesCorpus(), MotorAfirmacionesCorpus(),
        MotorFormulasCorpus(), MotorRelacionesExplicitasCorpus(), MotorNegacionesExcepcionesCorpus(),
        MotorVariantesTerminologicasCorpus(), MotorDistribucionPorObra(), MotorOrdenRecurrencia(),
    ]
    outputs = {}
    for motor in motors:
        for master in masters:
            motor.consume(master)
        out = motor.output(metas)
        jsonschema.Draft202012Validator(SCHEMA).validate(out)
        assert out["clausura_descriptiva"]["identidad_interobra_inferida"] is False
        assert out["clausura_descriptiva"]["equivalencia_inferida"] is False
        assert out["clausura_descriptiva"]["contradiccion_inferida"] is False
        assert out["cobertura"]["obras_procesadas"] == 2
        outputs[motor.motor] = out

    cg = next(g for g in outputs["conceptos_corpus"]["grupos"] if g["clave_recuperacion"] == "Mediación")
    assert cg["obra_ids"] == ["OBRA-A", "OBRA-B"]
    assert cg["estado_identidad_interobra"] == "no_determinada"

    vg = next(g for g in outputs["variantes_terminologicas_corpus"]["grupos"] if g["clave_recuperacion"] == "mediación")
    assert vg["obra_ids"] == ["OBRA-A", "OBRA-B"]
    assert vg["estado_identidad_interobra"] == "no_determinada"

    assertion_pairs = {
        (
            group["clave_recuperacion"],
            ref["obra_id"],
            ref["registro_id"],
            ref["datos_documentales"].get("concepto_id_clave"),
        )
        for group in outputs["afirmaciones_corpus"]["grupos"]
        for ref in group["registros"]
    }
    assert assertion_pairs == {
        ("Mediación", "OBRA-A", "AF-A", "CON-AA"),
        ("Objeto", "OBRA-A", "AF-A", "CON-AB"),
        ("Mediación", "OBRA-B", "AF-B", "CON-BA"),
        ("Objeto", "OBRA-B", "AF-B", "CON-BB"),
    }
    for group in outputs["afirmaciones_corpus"]["grupos"]:
        for ref in group["registros"]:
            datos = ref["datos_documentales"]
            assert "concepto_ids_origen" not in datos
            assert datos["conceptos_referidos_total"] == 2

    ambiguous = make_master("OBRA-X", "Obra X", "X")
    ambiguous["conceptos"][1]["designacion_operativa"] = "Mediación"
    ambiguous["conceptos"][1]["normalizacion_formal"] = "Mediación"
    ambiguous["conceptos"][1]["normalizacion_lexica"] = ["mediación", "mediacion"]
    amotor = MotorAfirmacionesCorpus()
    amotor.consume(ambiguous)
    aout = amotor.output([{"obra_id": "OBRA-X", "titulo": "Obra X", "schema_version": "1.4.1", "sha256": "2" * 64}])
    ag = next(g for g in aout["grupos"] if g["clave_recuperacion"] == "Mediación")
    assert {
        ref["datos_documentales"]["concepto_id_clave"]
        for ref in ag["registros"]
        if ref["registro_id"] == "AF-X"
    } == {"CON-XA", "CON-XB"}

    og = next(g for g in outputs["orden_recurrencia"]["grupos"] if g["clave_recuperacion"] == "Mediación")
    for ref in og["registros"]:
        assert ref["datos_documentales"]["aparicion_ids_ordenados"][0].endswith("1")
        assert ref["datos_documentales"]["aparicion_ids_ordenados"][1].endswith("2")

    assert outputs["definiciones_corpus"]["cobertura"]["registros_origen"] == 2
    assert outputs["afirmaciones_corpus"]["cobertura"]["registros_origen"] == 2
    assert outputs["formulas_corpus"]["cobertura"]["registros_origen"] == 2
    assert outputs["relaciones_explicitas_corpus"]["cobertura"]["registros_origen"] == 2
    assert outputs["negaciones_excepciones_corpus"]["cobertura"]["registros_origen"] == 4
    assert outputs["distribucion_por_obra"]["cobertura"]["registros_origen"] == 2
    print("OK Fase 11: nueve comparadores conservan clausura descriptiva, pares documentados y orden intraobra")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
