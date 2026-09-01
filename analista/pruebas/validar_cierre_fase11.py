#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "motores"))
from fase11_comun import concept_key, load_manifest, load_master, sha256_file, write_json
from ejecutar_comparaciones_fase11 import OUTPUTS

SOURCE_SECTIONS = {
    "conceptos_corpus": ("conceptos",),
    "definiciones_corpus": ("definiciones",),
    "afirmaciones_corpus": ("afirmaciones",),
    "formulas_corpus": ("formulas",),
    "relaciones_explicitas_corpus": ("relaciones_explicitas",),
    "negaciones_excepciones_corpus": ("negaciones", "excepciones"),
    "variantes_terminologicas_corpus": ("conceptos",),
    "distribucion_por_obra": ("__maestro__",),
    "orden_recurrencia": ("conceptos",),
}


def sidecar_ok(path: Path) -> str:
    digest = sha256_file(path)
    side = path.with_name(path.name + ".sha256")
    if not side.is_file():
        raise SystemExit(f"Sidecar ausente: {side}")
    sd, name = side.read_text(encoding="utf-8").strip().split("  ", 1)
    if sd != digest or name != path.name:
        raise SystemExit(f"Sidecar inválido: {side}")
    return digest


def refs_in_output(output: dict) -> set[tuple[str, str]]:
    return {
        (ref["obra_id"], ref["registro_id"])
        for group in output["grupos"]
        for ref in group["registros"]
    }


def assert_closure(value: object, path: str = "$.") -> None:
    if isinstance(value, dict):
        for key, item in value.items():
            if key in {"equivalencia_inferida", "complementariedad_inferida", "contradiccion_inferida", "identidad_interobra_inferida", "sintesis_doctrinal"} and item is not False:
                raise SystemExit(f"Clausura descriptiva violada en {path}{key}: {item!r}")
            if key == "resolucion_doctrinal" and item != "no_realizada":
                raise SystemExit(f"Resolución doctrinal no permitida en {path}{key}: {item!r}")
            assert_closure(item, f"{path}{key}.")
    elif isinstance(value, list):
        for i, item in enumerate(value):
            assert_closure(item, f"{path}[{i}].")


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--manifest", type=Path, required=True)
    p.add_argument("--maestros-dir", type=Path, required=True)
    p.add_argument("--salida-dir", type=Path, required=True)
    p.add_argument("--cierre", type=Path, required=True)
    args = p.parse_args()

    manifest = load_manifest(args.manifest)
    schema = json.loads((ROOT / "esquema/comparacion-corpus-fase11-v1.0.0.schema.json").read_text(encoding="utf-8"))

    expected: dict[str, set[tuple[str, str]]] = {m: set() for m in SOURCE_SECTIONS}
    concepts_by_id: dict[tuple[str, str], dict] = {}
    expected_assertion_links: set[tuple[str, str, str, str]] = set()
    master_meta = []
    for meta in sorted(manifest["maestros"], key=lambda x: x["obra_id"]):
        path = args.maestros_dir / f"{meta['obra_id']}.json"
        master = load_master(path, meta)
        master_meta.append({
            "obra_id": master["obra_id"],
            "titulo": master["titulo"],
            "schema_version": master["schema_version"],
            "sha256": meta["sha256"],
        })
        for motor, sections in SOURCE_SECTIONS.items():
            for section in sections:
                if section == "__maestro__":
                    expected[motor].add((master["obra_id"], master["id"]))
                else:
                    expected[motor].update((master["obra_id"], row["id"]) for row in master.get(section, []))
        local_concepts = {concept["id"]: concept for concept in master.get("conceptos", [])}
        for concept in local_concepts.values():
            concepts_by_id[(master["obra_id"], concept["id"])] = concept
        for row in master.get("afirmaciones", []):
            for cid in dict.fromkeys(row.get("concepto_ids", [])):
                concept = local_concepts.get(cid)
                if concept is None:
                    raise SystemExit(f"Afirmación refiere concepto inexistente: {master['obra_id']}:{row['id']}:{cid}")
                key = concept_key(concept)
                if not key:
                    raise SystemExit(f"Afirmación refiere concepto sin clave formal: {master['obra_id']}:{row['id']}:{cid}")
                expected_assertion_links.add((master["obra_id"], row["id"], cid, key))
        del master

    summaries = []
    for motor, filename in OUTPUTS.items():
        path = args.salida_dir / filename
        if not path.is_file():
            raise SystemExit(f"Salida de Fase 11 ausente: {path}")
        digest = sidecar_ok(path)
        output = json.loads(path.read_text(encoding="utf-8"))
        jsonschema.Draft202012Validator(schema).validate(output)
        assert output["motor"] == motor
        assert output["cobertura"]["obras_totales"] == 20
        assert output["cobertura"]["obras_procesadas"] == 20
        assert output["maestros"] == sorted(master_meta, key=lambda x: x["obra_id"])
        assert_closure(output)
        actual = refs_in_output(output)
        missing = expected[motor] - actual
        extra = actual - expected[motor]
        if missing or extra:
            raise SystemExit(f"Cobertura no exhaustiva en {motor}: faltan={list(sorted(missing))[:5]} extras={list(sorted(extra))[:5]}")
        if output["cobertura"]["registros_origen"] != len(expected[motor]):
            raise SystemExit(f"Conteo de cobertura incompatible en {motor}")
        if motor == "afirmaciones_corpus":
            actual_assertion_links = {
                (
                    ref["obra_id"],
                    ref["registro_id"],
                    ref["datos_documentales"]["concepto_id_clave"],
                    group["clave_recuperacion"],
                )
                for group in output["grupos"]
                for ref in group["registros"]
                if ref["datos_documentales"].get("concepto_id_clave") is not None
            }
            missing_links = expected_assertion_links - actual_assertion_links
            extra_links = actual_assertion_links - expected_assertion_links
            if missing_links or extra_links:
                raise SystemExit(
                    "Vínculos afirmación→concepto no exhaustivos: "
                    f"faltan={list(sorted(missing_links))[:5]} extras={list(sorted(extra_links))[:5]}"
                )
        if motor == "orden_recurrencia":
            for group in output["grupos"]:
                for ref in group["registros"]:
                    source = concepts_by_id[(ref["obra_id"], ref["registro_id"])]
                    ordered = ref["datos_documentales"].get("aparicion_ids_ordenados", [])
                    if len(ordered) != len(source.get("aparicion_ids", [])) or set(ordered) != set(source.get("aparicion_ids", [])):
                        raise SystemExit(f"Orden/recurrencia incompleto: {ref['obra_id']}:{ref['registro_id']}")
        summaries.append({
            "motor": motor,
            "version": output["version_motor"],
            "ruta": filename,
            "sha256": digest,
            "registros_origen": len(expected[motor]),
            "grupos_emitidos": output["cobertura"]["grupos_emitidos"],
        })
        print(json.dumps(summaries[-1], ensure_ascii=False, sort_keys=True))

    closure = {
        "version": "1.0.0",
        "fase": 11,
        "fase11_cerrada": True,
        "criterio": "registros_relacionados_reunidos_exhaustivamente_sin_relaciones_no_documentadas",
        "fuente_exclusiva": "json_maestros_obra_auditados",
        "maestros": sorted(master_meta, key=lambda x: x["obra_id"]),
        "motores": sorted(summaries, key=lambda x: x["motor"]),
        "clausura_descriptiva": {
            "identidad_interobra_inferida": False,
            "equivalencia_inferida": False,
            "complementariedad_inferida": False,
            "contradiccion_inferida": False,
            "sintesis_doctrinal": False,
            "resolucion_doctrinal": "no_realizada",
        },
    }
    digest = write_json(args.cierre, closure)
    print(json.dumps({"fase": 11, "fase11_cerrada": True, "maestros": 20, "motores": 9, "cierre_sha256": digest}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
