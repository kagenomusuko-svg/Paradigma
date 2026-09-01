#!/usr/bin/env python3
from __future__ import annotations

import argparse
import gc
import json
from pathlib import Path

from afirmaciones_corpus_fase11 import MotorAfirmacionesCorpus
from conceptos_corpus_fase11 import MotorConceptosCorpus
from definiciones_corpus_fase11 import MotorDefinicionesCorpus
from distribucion_por_obra_fase11 import MotorDistribucionPorObra
from fase11_comun import load_manifest, load_master, master_metadata, write_json
from formulas_corpus_fase11 import MotorFormulasCorpus
from negaciones_excepciones_corpus_fase11 import MotorNegacionesExcepcionesCorpus
from orden_recurrencia_corpus_fase11 import MotorOrdenRecurrencia
from relaciones_explicitas_corpus_fase11 import MotorRelacionesExplicitasCorpus
from variantes_terminologicas_corpus_fase11 import MotorVariantesTerminologicasCorpus

OUTPUTS = {
    "conceptos_corpus": "conceptos-corpus.json",
    "definiciones_corpus": "definiciones-corpus.json",
    "afirmaciones_corpus": "afirmaciones-corpus.json",
    "formulas_corpus": "formulas-corpus.json",
    "relaciones_explicitas_corpus": "relaciones-explicitas-corpus.json",
    "negaciones_excepciones_corpus": "negaciones-excepciones-corpus.json",
    "variantes_terminologicas_corpus": "variantes-terminologicas-corpus.json",
    "distribucion_por_obra": "distribucion-por-obra.json",
    "orden_recurrencia": "orden-recurrencia.json",
}


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--manifest", type=Path, required=True)
    p.add_argument("--maestros-dir", type=Path, required=True)
    p.add_argument("--salida-dir", type=Path, required=True)
    args = p.parse_args()

    manifest = load_manifest(args.manifest)
    motors = [
        MotorConceptosCorpus(),
        MotorDefinicionesCorpus(),
        MotorAfirmacionesCorpus(),
        MotorFormulasCorpus(),
        MotorRelacionesExplicitasCorpus(),
        MotorNegacionesExcepcionesCorpus(),
        MotorVariantesTerminologicasCorpus(),
        MotorDistribucionPorObra(),
        MotorOrdenRecurrencia(),
    ]
    masters_meta = []
    for expected in sorted(manifest["maestros"], key=lambda x: x["obra_id"]):
        path = args.maestros_dir / f"{expected['obra_id']}.json"
        if not path.is_file():
            raise SystemExit(f"Maestro requerido ausente: {path}")
        master = load_master(path, expected)
        masters_meta.append(master_metadata(master, expected["sha256"]))
        for motor in motors:
            motor.consume(master)
        print(json.dumps({
            "obra_id": master["obra_id"],
            "schema": master["schema_version"],
            "conceptos": len(master.get("conceptos", [])),
            "apariciones": len(master.get("apariciones_conceptuales", [])),
        }, ensure_ascii=False, sort_keys=True))
        del master
        gc.collect()

    args.salida_dir.mkdir(parents=True, exist_ok=True)
    index = []
    for motor in motors:
        output = motor.output(masters_meta)
        filename = OUTPUTS[motor.motor]
        path = args.salida_dir / filename
        digest = write_json(path, output)
        index.append({
            "motor": motor.motor,
            "version": motor.version,
            "ruta": filename,
            "sha256": digest,
            "cobertura": output["cobertura"],
        })
        print(json.dumps(index[-1], ensure_ascii=False, sort_keys=True))

    index_payload = {
        "version": "1.0.0",
        "fase": 11,
        "fuente_exclusiva": "json_maestros_obra_auditados",
        "maestros": masters_meta,
        "motores": index,
        "clausura_descriptiva": {
            "identidad_interobra_inferida": False,
            "equivalencia_inferida": False,
            "complementariedad_inferida": False,
            "contradiccion_inferida": False,
            "sintesis_doctrinal": False,
            "resolucion_doctrinal": "no_realizada",
        },
    }
    write_json(args.salida_dir / "indice-fase11.json", index_payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
