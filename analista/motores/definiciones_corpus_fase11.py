#!/usr/bin/env python3
from __future__ import annotations

from fase11_comun import BaseMotor, concept_key, concept_map


class MotorDefinicionesCorpus(BaseMotor):
    motor = "definiciones_corpus"

    def consume(self, master: dict) -> None:
        self.mark_work(master)
        cmap = concept_map(master)
        for row in master.get("definiciones", []):
            concept = cmap.get(row.get("concepto_id"))
            key = concept_key(concept) if concept else ""
            criterion = "designacion_formal_del_concepto_referenciado"
            if not key:
                key = f"__concepto_local__:{row.get('concepto_id', '')}:{row['id']}"
                criterion = "sin_designacion_interobra_recuperable"
            self.add(
                key,
                criterion,
                master,
                row,
                {
                    "concepto_id": row.get("concepto_id"),
                    "concepto_designacion": concept.get("designacion_operativa") if concept else None,
                    "clasificacion_definicion": row.get("clasificacion_definicion"),
                    "criterio_deteccion": row.get("criterio_deteccion"),
                },
            )
