#!/usr/bin/env python3
"""Inventario mecánico de obras previstas para Fase 10.

Deriva únicamente de los registros de fuente (Fase 2) y unidades (Fase 3).
Clasifica rasgos editoriales y la ruta prevista de procesamiento, pero no afirma
cierres de fase que este inventariador no verifica.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PILOT = "AA-SP-V1"
VERSION = "1.1.0"


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fuentes", type=Path, default=ROOT / "analista/generado/fuentes.jsonl")
    parser.add_argument("--unidades", type=Path, default=ROOT / "analista/generado/unidades.jsonl")
    parser.add_argument("--salida", type=Path, default=ROOT / "analista/generado/fase10/inventario-obras.json")
    args = parser.parse_args()

    sources = load_jsonl(args.fuentes)
    units = load_jsonl(args.unidades)
    counts = Counter(unit["fuente_id"] for unit in units)
    source_ids = {source["id"] for source in sources}
    if any(unit["fuente_id"] not in source_ids for unit in units):
        raise AssertionError("Unidad con fuente fuera del inventario")

    works: list[dict] = []
    for source in sorted(sources, key=lambda row: (row["titulo"], row["id"])):
        derived = list(source.get("rutas_derivadas", []))
        glossaries = [route for route in derived if str(route).endswith("99-glosario.md")]
        if len(glossaries) > 1:
            raise AssertionError(f"Más de un glosario técnico en {source['id']}: {glossaries}")
        is_pilot = source["id"] == PILOT
        works.append(
            {
                "obra_id": source["id"],
                "titulo": source["titulo"],
                "ruta_canonica": source["ruta_canonica"],
                "sha256_fuente": source["sha256"],
                "unidades": counts[source["id"]],
                "rutas_derivadas": len(derived),
                "glosario_tecnico": glossaries[0] if glossaries else None,
                "perfil_conceptual": "glosario_tecnico_explicito" if glossaries else "sin_glosario_tecnico_explicito",
                "rol_fase10": "piloto_reutilizado" if is_pilot else "obra_repeticion_controlada",
                "ruta_procesamiento_prevista": "reutilizar_maestro_fase9_tras_validacion" if is_pilot else "ejecutar_cadena_fase10_independiente",
                "estado_verificado": "no_verificado_por_inventario",
            }
        )

    document = {
        "version": VERSION,
        "fuentes": len(sources),
        "unidades": len(units),
        "obras_con_glosario": sum(work["glosario_tecnico"] is not None for work in works),
        "obras_sin_glosario": sum(work["glosario_tecnico"] is None for work in works),
        "piloto_id": PILOT,
        "alcance_estado": "inventario_no_certifica_cierres_de_fase",
        "obras": works,
    }
    payload = (json.dumps(document, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
    args.salida.parent.mkdir(parents=True, exist_ok=True)
    args.salida.write_bytes(payload)
    print(json.dumps({"obras": len(works), "unidades": len(units), "con_glosario": document["obras_con_glosario"],
                      "sin_glosario": document["obras_sin_glosario"], "sha256": hashlib.sha256(payload).hexdigest()}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
