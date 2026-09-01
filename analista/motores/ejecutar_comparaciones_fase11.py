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


def memory_kib() -> dict[str, int | None]:
    values: dict[str, int | None] = {"rss_kib": None, "hwm_kib": None}
    status = Path("/proc/self/status")
    if not status.is_file():
        return values
    for line in status.read_text(encoding="utf-8").splitlines():
        if line.startswith("VmRSS:"):
            values["rss_kib"] = int(line.split()[1])
        elif line.startswith("VmHWM:"):
            values["hwm_kib"] = int(line.split()[1])
    return values


def log_event(event: str, **data: object) -> None:
    payload = {"evento": event, **memory_kib(), **data}
    print(json.dumps(payload, ensure_ascii=False, sort_keys=True), flush=True)


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
        log_event("inicio_obra", obra_id=expected["obra_id"], bytes_maestro=path.stat().st_size)
        master = load_master(path, expected)
        log_event(
            "maestro_cargado",
            obra_id=master["obra_id"],
            schema=master["schema_version"],
            conceptos=len(master.get("conceptos", [])),
            apariciones=len(master.get("apariciones_conceptuales", [])),
        )
        masters_meta.append(master_metadata(master, expected["sha256"]))
        for motor in motors:
            motor.consume(master)
        log_event(
            "obra_consumida",
            obra_id=master["obra_id"],
            schema=master["schema_version"],
            conceptos=len(master.get("conceptos", [])),
            apariciones=len(master.get("apariciones_conceptuales", [])),
        )
        del master
        gc.collect()
        log_event("obra_liberada", obra_id=expected["obra_id"])

    args.salida_dir.mkdir(parents=True, exist_ok=True)
    index = []
    for motor in motors:
        log_event("inicio_ensamblado", motor=motor.motor)
        output = motor.output(masters_meta)
        log_event("salida_ensamblada", motor=motor.motor, grupos=output["cobertura"]["grupos_emitidos"])
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
        log_event("salida_escrita", motor=motor.motor, bytes_salida=path.stat().st_size, sha256=digest)
        del output
        motor.release()
        gc.collect()
        log_event("motor_liberado", motor=motor.motor)

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
    log_event("fin_fase11", motores=len(index))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
