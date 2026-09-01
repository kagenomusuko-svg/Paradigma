#!/usr/bin/env python3
from __future__ import annotations

from fase11_comun import BaseMotor, concept_key


class MotorOrdenRecurrencia(BaseMotor):
    motor = "orden_recurrencia"

    def consume(self, master: dict) -> None:
        self.mark_work(master)
        unit_order = {row["id"]: row.get("orden_textual", 0) for row in master.get("unidades", [])}
        appearances = {row["id"]: row for row in master.get("apariciones_conceptuales", [])}
        for concept in master.get("conceptos", []):
            ids = list(concept.get("aparicion_ids", []))
            missing = [aid for aid in ids if aid not in appearances]
            if missing:
                raise SystemExit(f"Apariciones ausentes en {master['obra_id']}:{concept['id']}: {missing[:5]}")
            ordered = sorted(
                ids,
                key=lambda aid: (
                    unit_order.get(appearances[aid].get("unidad_id"), 10**12),
                    (appearances[aid].get("localizacion") or {}).get("linea_inicio", 10**12),
                    (appearances[aid].get("localizacion") or {}).get("linea_fin", 10**12),
                    aid,
                ),
            )
            first = appearances[ordered[0]] if ordered else None
            last = appearances[ordered[-1]] if ordered else None
            key = concept_key(concept) or concept["id"]
            self.add(
                key,
                "designacion_formal_con_secuencia_intraobra_de_apariciones",
                master,
                concept,
                {
                    "concepto_id": concept["id"],
                    "designacion_operativa": concept.get("designacion_operativa"),
                    "apariciones_totales": len(ordered),
                    "aparicion_ids_ordenados": ordered,
                    "primera_aparicion": {
                        "id": first["id"],
                        "unidad_id": first.get("unidad_id"),
                        "orden_textual_unidad": unit_order.get(first.get("unidad_id")),
                        "localizacion": first.get("localizacion"),
                    } if first else None,
                    "ultima_aparicion": {
                        "id": last["id"],
                        "unidad_id": last.get("unidad_id"),
                        "orden_textual_unidad": unit_order.get(last.get("unidad_id")),
                        "localizacion": last.get("localizacion"),
                    } if last else None,
                },
            )
