#!/usr/bin/env python3
from __future__ import annotations

from fase11_comun import BaseMotor, formal_key


class MotorFormulasCorpus(BaseMotor):
    motor = "formulas_corpus"

    def consume(self, master: dict) -> None:
        self.mark_work(master)
        for row in master.get("formulas", []):
            key = formal_key(row.get("normalizacion_formal") or row.get("formula_literal"))
            if not key:
                key = f"__formula_local__:{master['obra_id']}:{row['id']}"
            self.add(
                key,
                "formula_formal_exacta_solo_para_recuperacion",
                master,
                row,
                {
                    "formula_literal": row.get("formula_literal"),
                    "simbolos_literales": row.get("simbolos_literales", []),
                    "contexto_unidad_ids": row.get("contexto_unidad_ids", []),
                    "clasificacion_formula": row.get("clasificacion_formula"),
                },
                identity_state="no_aplica",
            )
