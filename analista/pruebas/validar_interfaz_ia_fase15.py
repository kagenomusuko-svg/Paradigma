#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "motores"))
from interfaz_ia_fase15 import (
    CLAUSURA_F15,
    RESTRICCIONES_RESPUESTA,
    packet_from_response,
)


def main() -> int:
    schema = json.loads((ROOT / "esquema/paquete-interfaz-ia-fase15-v1.0.0.schema.json").read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema)
    storage14 = {
        "gate": {"cierre_sha256": "a" * 64},
        "almacenamiento": {"release_tag": "analista-fase14-cierre-v1.0.0", "asset_sha256": "b" * 64},
    }
    ref = {
        "obra_id": "A",
        "registro_id": "R1",
        "fuente_id": "SRC-A",
        "unidad_id": "U1",
        "localizacion": {"ruta": "a.txt", "linea_inicio": 1, "linea_fin": 1},
        "texto_literal": "X se afirma literalmente.",
        "estatus_enunciativo": "afirmacion_autoral",
        "estado_verificacion": "verificado",
        "estado_auditoria": "auditado",
    }
    response = {
        "id": "F14R-123456789ABC",
        "tipo_registro": "respuesta_consulta_literal",
        "fase": 14,
        "consulta": {"tipo": "predicaciones", "termino": "X"},
        "estado": "hallazgo_auditado",
        "mensaje": None,
        "resultados": [{
            "tipo_hallazgo": "predicacion",
            "clave_recuperacion": "X",
            "expediente_fase13_id": "F13C-AAA",
            "referencia": ref,
        }],
        "conteo_resultados": 1,
    }
    context = {
        "expediente_fase13_id": "F13C-AAA",
        "clave_recuperacion": "X",
        "hallazgos": [{"tipo": "multiplicidad_predicativa"}],
        "restricciones": [{"id": "F13R-1", "criterio_vinculo": "afirmacion_limitada_id_documentado"}],
    }
    packet = packet_from_response(response, storage14, {"F13C-AAA": context}, {"X": context})
    validator.validate(packet)
    assert packet["estado"] == "evidencia_disponible"
    assert packet["motivo_abstencion"] is None
    assert packet["respuesta_controlada"]["modo"] == "extractiva_con_referencias"
    assert len(packet["registros_utilizados"]) == 1
    use = packet["registros_utilizados"][0]
    assert use["texto_literal"] == ref["texto_literal"]
    assert use["referencia"] == ref
    assert packet["respuesta_controlada"]["registros_utilizados_ids"] == [use["uso_id"]]
    assert f"[{use['uso_id']}] {ref['texto_literal']}" in packet["respuesta_controlada"]["texto"]
    assert packet["hallazgos_auditoria"][0]["hallazgos"] == context["hallazgos"]
    assert packet["restricciones_documentales"][0]["restricciones"] == context["restricciones"]
    assert packet["restricciones_respuesta"] == RESTRICCIONES_RESPUESTA
    assert packet["clausura_descriptiva"] == CLAUSURA_F15

    negative = dict(response)
    negative["id"] = "F14R-ABCDEF123456"
    negative["consulta"] = {"tipo": "relacion_explicita", "termino": "X", "relacion": "=", "objeto": "Y"}
    negative["estado"] = "no_determinado_por_el_corpus"
    negative["mensaje"] = "NO DETERMINADO POR EL CORPUS."
    negative["resultados"] = []
    negative["conteo_resultados"] = 0
    abstention = packet_from_response(negative, storage14, {}, {})
    validator.validate(abstention)
    assert abstention["estado"] == "abstencion"
    assert abstention["motivo_abstencion"] == "no_determinado_por_el_corpus"
    assert abstention["respuesta_controlada"]["modo"] == "abstencion"
    assert abstention["respuesta_controlada"]["texto"] == "NO DETERMINADO POR EL CORPUS."
    assert abstention["respuesta_controlada"]["registros_utilizados_ids"] == []
    assert abstention["registros_utilizados"] == []
    assert abstention["trazabilidad"] == []

    print("OK Fase 15: respuesta extractiva trazable y abstención sin autoridad doctrinal")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
