#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import unicodedata
from collections import defaultdict
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "1.0.0"
MOTOR_VERSION = "1.0.0"
MASTER_SCHEMAS = {"1.1.0", "1.4.1"}

CLAUSURA = {
    "solo_maestros_obra": True,
    "identidad_interobra_inferida": False,
    "equivalencia_inferida": False,
    "complementariedad_inferida": False,
    "contradiccion_inferida": False,
    "sintesis_doctrinal": False,
    "resolucion_doctrinal": "no_realizada",
}


def canonical_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def stable_id(prefix: str, value: Any) -> str:
    return f"{prefix}-{hashlib.sha256(canonical_bytes(value)).hexdigest()[:12].upper()}"


def formal_key(value: Any) -> str:
    if value is None:
        return ""
    text = unicodedata.normalize("NFKC", str(value))
    return " ".join(text.split())


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_manifest(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    gate = data.get("gate", {})
    if data.get("fase") != 10 or gate.get("fase10_cerrada") is not True:
        raise SystemExit("Fase 11 requiere manifiesto persistido con Fase 10 cerrada")
    if gate.get("obras") != 20 or len(data.get("maestros", [])) != 20:
        raise SystemExit("Fase 11 requiere exactamente los 20 maestros cerrados de Fase 10")
    if gate.get("comparacion_interobra") is not False:
        raise SystemExit("El origen de Fase 11 no conserva la clausura interobra de Fase 10")
    return data


def load_master(path: Path, expected: dict[str, Any]) -> dict[str, Any]:
    actual = sha256_file(path)
    if actual != expected["sha256"]:
        raise SystemExit(f"Hash de maestro inválido: {expected['obra_id']} {actual} != {expected['sha256']}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("obra_id") != expected["obra_id"]:
        raise SystemExit(f"obra_id incompatible en {path}")
    if data.get("schema_version") not in MASTER_SCHEMAS:
        raise SystemExit(f"Schema maestro no soportado en Fase 11: {data.get('schema_version')}")
    if data.get("tipo_registro") != "expediente_maestro_obra":
        raise SystemExit(f"Entrada no es maestro de obra: {path}")
    if data.get("estado_verificacion") != "verificado":
        raise SystemExit(f"Maestro no verificado: {expected['obra_id']}")
    return data


def master_metadata(master: dict[str, Any], sha256: str) -> dict[str, Any]:
    return {
        "obra_id": master["obra_id"],
        "titulo": master["titulo"],
        "schema_version": master["schema_version"],
        "sha256": sha256,
    }


def concept_map(master: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {row["id"]: row for row in master.get("conceptos", [])}


def concept_key(row: dict[str, Any]) -> str:
    return formal_key(row.get("normalizacion_formal") or row.get("designacion_operativa"))


def compact_origin(
    master: dict[str, Any],
    row: dict[str, Any],
    datos: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "obra_id": master["obra_id"],
        "titulo_obra": master["titulo"],
        "schema_maestro": master["schema_version"],
        "registro_id": row["id"],
        "tipo_registro_origen": row["tipo_registro"],
        "estado_extraccion": row.get("estado_extraccion"),
        "estado_verificacion": row.get("estado_verificacion"),
        "estado_auditoria": row.get("estado_auditoria"),
        "estatus_enunciativo": row.get("estatus_enunciativo"),
        "fuente_id": row.get("fuente_id"),
        "unidad_id": row.get("unidad_id"),
        "localizacion": row.get("localizacion"),
        "texto_literal": row.get("texto_literal"),
        "normalizacion_formal": row.get("normalizacion_formal"),
        "normalizacion_lexica": row.get("normalizacion_lexica"),
        "datos_documentales": datos or {},
    }


class BaseMotor:
    motor: str = ""
    version: str = MOTOR_VERSION

    def __init__(self) -> None:
        self._groups: dict[str, dict[str, Any]] = {}
        self._source_ids: set[tuple[str, str]] = set()
        self._processed_works: set[str] = set()

    def consume(self, master: dict[str, Any]) -> None:
        raise NotImplementedError

    def mark_work(self, master: dict[str, Any]) -> None:
        self._processed_works.add(master["obra_id"])

    def add(
        self,
        key: str,
        criterion: str,
        master: dict[str, Any],
        row: dict[str, Any],
        datos: dict[str, Any] | None = None,
        identity_state: str = "no_determinada",
    ) -> None:
        normalized_key = formal_key(key)
        source_key = (master["obra_id"], row["id"])
        self._source_ids.add(source_key)
        bucket = self._groups.setdefault(
            normalized_key,
            {
                "criterion": criterion,
                "identity": identity_state,
                "refs": [],
                "seen": set(),
            },
        )
        if bucket["criterion"] != criterion or bucket["identity"] != identity_state:
            raise SystemExit(f"Clave de recuperación ambigua en {self.motor}: {normalized_key!r}")
        ref_key = (master["obra_id"], row["id"])
        if ref_key not in bucket["seen"]:
            bucket["seen"].add(ref_key)
            bucket["refs"].append(compact_origin(master, row, datos))

    def output(self, masters: list[dict[str, Any]]) -> dict[str, Any]:
        groups = []
        for key in sorted(self._groups):
            bucket = self._groups[key]
            refs = sorted(bucket["refs"], key=lambda r: (r["obra_id"], r["registro_id"]))
            groups.append(
                {
                    "id": stable_id("F11G", {"motor": self.motor, "clave": key}),
                    "clave_recuperacion": key,
                    "criterio_agrupacion": bucket["criterion"],
                    "estado_identidad_interobra": bucket["identity"],
                    "equivalencia_inferida": False,
                    "complementariedad_inferida": False,
                    "contradiccion_inferida": False,
                    "resolucion_doctrinal": "no_realizada",
                    "obra_ids": sorted({r["obra_id"] for r in refs}),
                    "registros": refs,
                }
            )
        metadata = sorted(masters, key=lambda x: x["obra_id"])
        payload = {
            "tipo_registro": "salida_comparacion_corpus",
            "schema_version": SCHEMA_VERSION,
            "motor": self.motor,
            "version_motor": self.version,
            "fuente_exclusiva": "json_maestros_obra_auditados",
            "maestros": metadata,
            "clausura_descriptiva": dict(CLAUSURA),
            "cobertura": {
                "obras_totales": len(metadata),
                "obras_procesadas": len(self._processed_works),
                "registros_origen": len(self._source_ids),
                "grupos_emitidos": len(groups),
            },
            "grupos": groups,
        }
        payload["id"] = stable_id("F11OUT", {"motor": self.motor, "maestros": metadata, "grupos": len(groups)})
        return payload


def write_json(path: Path, value: dict[str, Any]) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
    path.write_bytes(payload)
    digest = hashlib.sha256(payload).hexdigest()
    path.with_name(path.name + ".sha256").write_text(f"{digest}  {path.name}\n", encoding="utf-8")
    return digest
