#!/usr/bin/env python3
from __future__ import annotations

from fase11_comun import BaseMotor, formal_key


class MotorVariantesTerminologicasCorpus(BaseMotor):
    motor = "variantes_terminologicas_corpus"

    def consume(self, master: dict) -> None:
        self.mark_work(master)
        for row in master.get("conceptos", []):
            lexical = [formal_key(x) for x in (row.get("normalizacion_lexica") or []) if formal_key(x)]
            if not lexical:
                lexical = [formal_key(row.get("normalizacion_formal") or row.get("designacion_operativa"))]
            for key in sorted(set(k for k in lexical if k)):
                self.add(
                    key,
                    "clave_lexica_de_recuperacion_proveniente_del_maestro_no_identidad",
                    master,
                    row,
                    {
                        "concepto_id": row["id"],
                        "designacion_operativa": row.get("designacion_operativa"),
                        "formas_literales_observadas": row.get("formas_literales_observadas", []),
                        "clave_lexica_origen": key,
                        "estado_identidad_conceptual_intraobra": row.get("estado_identidad_conceptual"),
                    },
                )
