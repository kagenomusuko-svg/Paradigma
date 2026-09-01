#!/usr/bin/env python3
from __future__ import annotations

from fase11_comun import BaseMotor, concept_key


class MotorConceptosCorpus(BaseMotor):
    motor = "conceptos_corpus"

    def consume(self, master: dict) -> None:
        self.mark_work(master)
        for row in master.get("conceptos", []):
            key = concept_key(row) or row["id"]
            self.add(
                key,
                "designacion_formal_exacta_solo_para_recuperacion",
                master,
                row,
                {
                    "concepto_id": row["id"],
                    "designacion_operativa": row.get("designacion_operativa"),
                    "formas_literales_observadas": row.get("formas_literales_observadas", []),
                    "estado_identidad_conceptual_intraobra": row.get("estado_identidad_conceptual"),
                    "evidencia_identidad_ids": row.get("evidencia_identidad_ids", []),
                    "apariciones_totales": len(row.get("aparicion_ids", [])),
                },
            )
