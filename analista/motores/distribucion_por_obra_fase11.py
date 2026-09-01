#!/usr/bin/env python3
from __future__ import annotations

from fase11_comun import BaseMotor


SECTIONS = (
    "apariciones_conceptuales",
    "conceptos",
    "definiciones",
    "afirmaciones",
    "formulas",
    "relaciones_explicitas",
    "distinciones",
    "negaciones",
    "excepciones",
    "restricciones_alcance",
    "hallazgos_auditoria",
    "reportes_cobertura",
)


class MotorDistribucionPorObra(BaseMotor):
    motor = "distribucion_por_obra"

    def consume(self, master: dict) -> None:
        self.mark_work(master)
        counts = {section: len(master.get(section, [])) for section in SECTIONS}
        concept_states = {"establecida_por_evidencia": 0, "no_determinada": 0}
        for row in master.get("conceptos", []):
            state = row.get("estado_identidad_conceptual")
            if state in concept_states:
                concept_states[state] += 1
        self.add(
            master["obra_id"],
            "obra_id_del_maestro",
            master,
            master,
            {
                "schema_maestro": master.get("schema_version"),
                "conteos": counts,
                "conceptos_por_estado_identidad_intraobra": concept_states,
                "unidades": len(master.get("unidades", [])),
            },
            identity_state="no_aplica",
        )
