#!/usr/bin/env python3
"""Construye el registro de todas las fuentes canónicas sin producir contenido doctrinal."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FUENTES = ROOT / "corpus" / "fuentes"
CATALOGO = ROOT / "corpus" / "catalogo-generado.json"
SUMAS = FUENTES / "SHA256SUMS.txt"
SALIDA = ROOT / "analista" / "generado" / "fuentes.jsonl"
SCHEMA_VERSION = "1.0.0"
MOTOR_VERSION = "1.0.1"
LEGACY_IDS = {
    "corpus/fuentes/Afrodita_Areia_Sobre_la_Pasion.md": "AA-SP-V1",
}


def stable_id(ruta: str) -> str:
    if ruta in LEGACY_IDS:
        return LEGACY_IDS[ruta]
    digest = hashlib.sha256(ruta.encode("utf-8")).hexdigest()[:12].upper()
    return f"FUE-{digest}"


def load_sums() -> dict[str, str]:
    result: dict[str, str] = {}
    for line in SUMAS.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        digest, path = line.split(maxsplit=1)
        path = path.strip()
        if path in result:
            raise RuntimeError(f"Ruta duplicada en SHA256SUMS: {path}")
        result[path] = digest
    return result


def load_catalog() -> dict[str, dict]:
    items = json.loads(CATALOGO.read_text(encoding="utf-8"))
    result: dict[str, dict] = {}
    for item in items:
        ruta = item["source"]
        if ruta in result:
            raise RuntimeError(f"Fuente duplicada en catálogo generado: {ruta}")
        result[ruta] = item
    return result


def build_record(ruta: str, item: dict, sums: dict[str, str]) -> dict:
    source = ROOT / ruta
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    if item["sha256"] != digest:
        raise RuntimeError(f"Hash no coincide con catálogo generado: {ruta}")
    if sums.get(ruta) != digest:
        raise RuntimeError(f"Hash no coincide con SHA256SUMS: {ruta}")

    segments = item.get("segments") or []
    paths = [segment["path"] for segment in segments]
    if not paths:
        raise RuntimeError(f"Fuente sin segmentación registrada: {ruta}")
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
    catalog = load_catalog()
    sums = load_sums()
    source_paths = sorted(
        str(path.relative_to(ROOT))
        for path in FUENTES.glob("*.md")
        if path.is_file()
    )
    source_set = set(source_paths)
    catalog_set = set(catalog)
    sums_set = set(sums)
    if source_set != catalog_set:
        raise RuntimeError(
            "Catálogo generado no cubre exactamente corpus/fuentes: "
            f"sin_catalogar={sorted(source_set - catalog_set)} "
            f"sin_fuente={sorted(catalog_set - source_set)}"
        )
    if source_set != sums_set:
        raise RuntimeError(
            "SHA256SUMS no cubre exactamente corpus/fuentes: "
            f"sin_suma={sorted(source_set - sums_set)} "
            f"sin_fuente={sorted(sums_set - source_set)}"
        )

    records = [build_record(ruta, catalog[ruta], sums) for ruta in source_paths]
    ids = [record["id"] for record in records]
    if len(ids) != len(set(ids)):
        raise RuntimeError("Colisión de IDs de fuente")

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text(
        "".join(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n" for record in records),
        encoding="utf-8",
    )
    print(f"Registro de fuentes generado: {len(records)} fuentes; cobertura canónica completa y cadena de custodia reconstruida.")


if __name__ == "__main__":
    main()
