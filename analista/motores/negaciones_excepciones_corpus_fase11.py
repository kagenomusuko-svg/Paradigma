#!/usr/bin/env python3
from __future__ import annotations

from fase11_comun import BaseMotor, formal_key


class MotorNegacionesExcepcionesCorpus(BaseMotor):
    motor = "negaciones_excepciones_corpus"

    def consume(self, master: dict) -> None:
        self.mark_work(master)
        for section in ("negaciones", "excepciones"):
            for row in master.get(section, []):
                literal = (
                    row.get("normalizacion_formal")
                    or row.get("objeto_negado_literal")
                    or row.get("fragmento_exceptivo_literal")
                    or row.get("texto_literal")
                )
                key = f"{row['tipo_registro']}::{formal_key(literal)}"
                self.add(
                    key,
                    "tipo_y_forma_exacta_solo_para_recuperacion",
                    master,
                    row,
                    {
                        "clasificacion_negacion": row.get("clasificacion_negacion"),
                        "objeto_negado_literal": row.get("objeto_negado_literal"),
                        "alcance_literal": row.get("alcance_literal"),
                        "clasificacion_excepcion": row.get("clasificacion_excepcion"),
                        "fragmento_exceptivo_literal": row.get("fragmento_exceptivo_literal"),
                        "afirmacion_limitada_id": row.get("afirmacion_limitada_id"),
                    },
                    identity_state="no_aplica",
                )
