#!/usr/bin/env python3
from __future__ import annotations

from fase11_comun import BaseMotor, concept_key, concept_map


class MotorAfirmacionesCorpus(BaseMotor):
    motor = "afirmaciones_corpus"

    def consume(self, master: dict) -> None:
        self.mark_work(master)
        cmap = concept_map(master)
        for row in master.get("afirmaciones", []):
            concept_ids = list(row.get("concepto_ids", []))
            keys = []
            for cid in concept_ids:
                concept = cmap.get(cid)
                key = concept_key(concept) if concept else ""
                if key:
                    keys.append((key, cid, concept.get("designacion_operativa")))
            if not keys:
                keys = [(f"__sin_clave_conceptual__:{master['obra_id']}:{row['id']}", None, None)]
            for key, cid, designation in keys:
                self.add(
                    key,
                    "designacion_formal_de_concepto_referenciado" if cid else "afirmacion_sin_clave_conceptual_interobra",
                    master,
                    row,
                    {
                        "concepto_id_clave": cid,
                        "concepto_designacion_clave": designation,
                        "concepto_ids_origen": concept_ids,
                        "clasificacion_afirmacion": row.get("clasificacion_afirmacion"),
                        "sujeto_literal": row.get("sujeto_literal"),
                        "predicado_literal": row.get("predicado_literal"),
                        "objeto_literal": row.get("objeto_literal"),
                        "criterio_deteccion": row.get("criterio_deteccion"),
                        "confianza_extraccion": row.get("confianza_extraccion"),
                    },
                )
