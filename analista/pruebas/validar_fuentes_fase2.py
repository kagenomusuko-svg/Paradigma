#!/usr/bin/env python3
"""Valida el producto real del motor de fuentes contra el contrato y el corpus canónico."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

from jsonschema import Draft202012Validator
from jsonschema.exceptions import ValidationError

ROOT = Path(__file__).resolve().parents[2]
FUENTES = ROOT / "corpus" / "fuentes"
SCHEMA = ROOT / "analista" / "esquema" / "contratos-v1.0.0.schema.json"
REGISTRO = ROOT / "analista" / "generado" / "fuentes.jsonl"


def main() -> None:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)
    records = [
        json.loads(line)
        for line in REGISTRO.read_text(encoding="utf-8").splitlines()
        if line
    ]
    source_paths = {
        str(path.relative_to(ROOT))
        for path in FUENTES.glob("*.md")
        if path.is_file()
    }
    if not records:
        raise AssertionError("Registro de fuentes vacío")
    if len(records) != len(source_paths):
        raise AssertionError("El producto no cubre todas las fuentes canónicas")

    ids = set()
    canonical = set()
    for record in records:
        validator.validate(record)
        if record["id"] in ids or record["ruta_canonica"] in canonical:
            raise AssertionError("ID o ruta canónica duplicada")
        ids.add(record["id"])
        canonical.add(record["ruta_canonica"])
        source = ROOT / record["ruta_canonica"]
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        if digest != record["sha256"] or record["version_fuente"] != f"sha256:{digest}":
            raise AssertionError(f"Custodia hash fallida: {record['id']}")
        if record["segmentaciones"] != record["rutas_derivadas"] or not record["segmentaciones"]:
            raise AssertionError(f"Relación fuente-segmentación incompleta: {record['id']}")
        reconstructed = b"".join(
            (ROOT / path).read_bytes() for path in record["rutas_derivadas"]
        )
        if reconstructed != source.read_bytes():
            raise AssertionError(f"Reconstrucción fallida: {record['id']}")

    if canonical != source_paths:
        raise AssertionError(
            f"Cobertura canónica desigual: faltan={sorted(source_paths-canonical)} "
            f"sobran={sorted(canonical-source_paths)}"
        )

    pilot = next(
        r for r in records
        if r["ruta_canonica"].endswith("Afrodita_Areia_Sobre_la_Pasion.md")
    )
    if pilot["id"] != "AA-SP-V1":
        raise AssertionError("Se perdió el ID histórico estable del piloto")

    bad = copy.deepcopy(pilot)
    bad["solucion_doctrinal"] = "X"
    try:
        validator.validate(bad)
    except ValidationError:
        pass
    else:
        raise AssertionError("El contrato aceptó un campo doctrinal ajeno")

    print(
        f"OK Fase 2: {len(records)} fuentes canónicas verificadas; "
        "hashes, cobertura y reconstrucción exactos; piloto=AA-SP-V1"
    )


if __name__ == "__main__":
    main()
