#!/usr/bin/env python3
from __future__ import annotations

import json

from fase11_comun import BaseMotor, concept_key, concept_map, formal_key


class MotorRelacionesExplicitasCorpus(BaseMotor):
    motor = "relaciones_explicitas_corpus"

    def consume(self, master: dict) -> None:
        self.mark_work(master)
        cmap = concept_map(master)
        for row in master.get("relaciones_explicitas", []):
            subject = cmap.get(row.get("sujeto_ref"))
            obj = cmap.get(row.get("objeto_ref"))
            skey = concept_key(subject) if subject else formal_key(row.get("sujeto_ref"))
            okey = concept_key(obj) if obj else formal_key(row.get("objeto_ref"))
            rkey = formal_key(row.get("normalizacion_formal") or row.get("relacion_literal"))
            key = json.dumps([skey, rkey, okey], ensure_ascii=False, separators=(",", ":"))
            self.add(
                key,
                "tripleta_formal_sujeto_relacion_objeto_solo_para_recuperacion",
                master,
                row,
                {
                    "sujeto_ref": row.get("sujeto_ref"),
                    "sujeto_designacion": subject.get("designacion_operativa") if subject else None,
                    "objeto_ref": row.get("objeto_ref"),
                    "objeto_designacion": obj.get("designacion_operativa") if obj else None,
                    "relacion_literal": row.get("relacion_literal"),
                    "clasificacion_relacion": row.get("clasificacion_relacion"),
                },
            )
