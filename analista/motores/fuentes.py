#!/usr/bin/env python3
"""Construye el registro de fuentes sin producir contenido doctrinal."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CATALOGO = ROOT / "corpus" / "catalogo.json"
SALIDA = ROOT / "analista" / "generado" / "fuentes.jsonl"
SCHEMA_VERSION = "1.0.0"
MOTOR_VERSION = "1.0.0"
LEGACY_IDS = {
    "corpus/fuentes/Afrodita_Areia_Sobre_la_Pasion.md": "AA-SP-V1",
}


def stable_id(ruta: str) -> str:
    if ruta in LEGACY_IDS:
        return LEGACY_IDS[ruta]
    digest = hashlib.sha256(ruta.encode("utf-8")).hexdigest()[:12].upper()
    return f"FUE-{digest}"


def build_record(item: dict) -> dict:
    ruta = item["source"]
    source = ROOT / ruta
    if not source.is_file():
        raise FileNotFoundError(ruta)
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    if digest != item["sha256"]:
        raise RuntimeError(f"Hash no coincide con catálogo: {ruta}")

    segments = item.get("segments") or []
    paths = [segment["path"] for segment in segments]
    if len(paths) != len(set(paths)):
        raise RuntimeError(f"Segmentación duplicada: {ruta}")
    missing = [path for path in paths if not (ROOT / path).is_file()]
    if missing:
        raise FileNotFoundError(f"Segmentos ausentes en {ruta}: {missing}")
    reconstructed = b"".join((ROOT / path).read_bytes() for path in paths)
    if reconstructed != source.read_bytes():
        raise RuntimeError(f"La segmentación no reconstruye exactamente la fuente: {ruta}")

    metadata = {
        key: value
        for key, value in item.items()
        if key not in {"source", "sha256", "segments"}
    }
    return {
        "id": stable_id(ruta),
        "tipo_registro": "fuente",
        "schema_version": SCHEMA_VERSION,
        "texto_literal": None,
        "normalizacion_formal": None,
        "normalizacion_lexica": None,
        "estatus_enunciativo": None,
        "estado_extraccion": "extraido",
        "estado_verificacion": "verificado",
        "estado_auditoria": "no_aplica",
        "producido_por": {"motor": "fuentes", "version": MOTOR_VERSION},
        "titulo": item["title"],
        "ruta_canonica": ruta,
        "rutas_derivadas": paths,
        "sha256": digest,
        "version_fuente": f"sha256:{digest}",
        "metadatos_documentales": metadata,
        "segmentaciones": paths,
    }


def main() -> None:
    catalog = json.loads(CATALOGO.read_text(encoding="utf-8"))
    records = [build_record(item) for item in catalog]
    ids = [record["id"] for record in records]
    if len(ids) != len(set(ids)):
        raise RuntimeError("Colisión de IDs de fuente")
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text(
        "".join(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n" for record in records),
        encoding="utf-8",
    )
    print(f"Registro de fuentes generado: {len(records)} fuentes; cadena de custodia reconstruida.")


if __name__ == "__main__":
    main()
