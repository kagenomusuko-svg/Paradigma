#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MOTOR = ROOT / "motores/auditor_corpus_fase12.py"
VALIDATOR = ROOT / "pruebas/validar_cierre_fase12.py"
SCHEMA_A = ROOT / "esquema/auditoria-corpus-fase12-v1.0.0.schema.json"
SCHEMA_E = ROOT / "esquema/expediente-transversal-fase12-v1.0.0.schema.json"
sys.path.insert(0, str(ROOT / "motores"))
from auditor_corpus_fase12 import CLAUSURA_F11, EXPECTED_MOTORS, audit_product, sha256_file, stable_id


def make_ref(
    obra: str,
    rid: str,
    tipo: str,
    datos: dict | None = None,
    texto: str = "x",
    estado_auditoria: str | None = "auditado",
) -> dict:
    return {
        "obra_id": obra,
        "titulo_obra": f"Obra {obra}",
        "schema_maestro": "1.4.1",
        "registro_id": rid,
        "tipo_registro_origen": tipo,
        "estado_extraccion": "extraido",
        "estado_verificacion": "verificado",
        "estado_auditoria": estado_auditoria,
        "estatus_enunciativo": None,
        "fuente_id": obra,
        "unidad_id": "U1",
        "localizacion": {"linea_inicio": 1, "linea_fin": 1},
        "texto_literal": texto,
        "normalizacion_formal": None,
        "normalizacion_lexica": None,
        "datos_documentales": datos or {},
    }


def make_group(motor: str, key: str, refs: list[dict], *, identity: str = "no_determinada") -> dict:
    return {
        "id": stable_id("F11G", {"motor": motor, "clave": key}),
        "clave_recuperacion": key,
        "criterio_agrupacion": "regresion_fase12",
        "estado_identidad_interobra": identity,
        "equivalencia_inferida": False,
        "complementariedad_inferida": False,
        "contradiccion_inferida": False,
        "resolucion_doctrinal": "no_realizada",
        "obra_ids": sorted({r["obra_id"] for r in refs}),
        "registros": refs,
    }


def write_product(root: Path, masters: list[dict], motor: str, groups: list[dict]) -> dict:
    source_ids = {(r["obra_id"], r["registro_id"]) for g in groups for r in g["registros"]}
    payload = {
        "tipo_registro": "salida_comparacion_corpus",
        "schema_version": "1.0.0",
        "motor": motor,
        "version_motor": "1.0.0",
        "fuente_exclusiva": "json_maestros_obra_auditados",
        "maestros": masters,
        "clausura_descriptiva": dict(CLAUSURA_F11),
        "cobertura": {
            "obras_totales": 20,
            "obras_procesadas": 20,
            "registros_origen": len(source_ids),
            "grupos_emitidos": len(groups),
        },
        "grupos": groups,
    }
    payload["id"] = stable_id("F11OUT", {"motor": motor, "maestros": masters, "grupos": len(groups)})
    path = root / f"{motor}.json"
    path.write_text(json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    return {
        "motor": motor,
        "ruta": path.name,
        "sha256": sha256_file(path),
        "version": "1.0.0",
        "registros_origen": len(source_ids),
        "grupos_emitidos": len(groups),
    }


def expect_audit_failure(
    root: Path,
    motor: str,
    expected: dict,
    masters: list[dict],
    message_fragment: str,
) -> None:
    try:
        audit_product(root / expected["ruta"], motor, expected, masters, lambda group: None)
    except SystemExit as exc:
        assert message_fragment in str(exc), str(exc)
    else:
        raise AssertionError(f"Se esperaba rechazo de auditoría para {motor}: {message_fragment}")


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="fase12-regresion-") as tmp:
        base = Path(tmp)
        fase11 = base / "fase11"
        fase12 = base / "fase12"
        negatives = base / "negatives"
        fase11.mkdir()
        negatives.mkdir()
        masters = []
        for i in range(20):
            obra = "A" if i == 0 else ("B" if i == 1 else f"W{i:02d}")
            masters.append({
                "obra_id": obra,
                "titulo": f"Obra {obra}",
                "schema_version": "1.4.1",
                "sha256": hashlib.sha256(obra.encode()).hexdigest(),
            })

        c1 = make_ref("A", "C1", "concepto", {
            "concepto_id": "C1", "designacion_operativa": "ego",
            "formas_literales_observadas": ["Ego"], "apariciones_totales": 3,
        })
        c1b = make_ref("A", "C1B", "concepto", {
            "concepto_id": "C1B", "designacion_operativa": "ego",
            "formas_literales_observadas": ["ego-forma"], "apariciones_totales": 2,
        })
        c2 = make_ref("B", "C2", "concepto", {
            "concepto_id": "C2", "designacion_operativa": "ego",
            "formas_literales_observadas": ["ego"], "apariciones_totales": 1,
        })
        products = {}
        products["conceptos_corpus"] = write_product(
            fase11, masters, "conceptos_corpus", [make_group("conceptos_corpus", "ego", [c1, c1b, c2])]
        )
        products["definiciones_corpus"] = write_product(
            fase11, masters, "definiciones_corpus", [make_group("definiciones_corpus", "ego", [
                make_ref("A", "D1", "definicion", {"concepto_id": "C1", "clasificacion_definicion": "definicion_explicita"}),
                make_ref("B", "D2", "definicion", {"concepto_id": "C2", "clasificacion_definicion": "definicion_explicita"}),
            ])]
        )
        af1a = make_ref("A", "AF1", "afirmacion", {"concepto_id_clave": "C1", "conceptos_referidos_total": 2}, "ego produce acto")
        af1b = make_ref("A", "AF1", "afirmacion", {"concepto_id_clave": "C1B", "conceptos_referidos_total": 2}, "ego produce acto")
        af2 = make_ref("B", "AF2", "afirmacion", {"concepto_id_clave": "C2", "conceptos_referidos_total": 1}, "ego actúa")
        products["afirmaciones_corpus"] = write_product(
            fase11, masters, "afirmaciones_corpus", [make_group("afirmaciones_corpus", "ego", [af1a, af1b, af2])]
        )
        products["formulas_corpus"] = write_product(
            fase11, masters, "formulas_corpus", [make_group("formulas_corpus", "x=y", [
                make_ref("A", "F1", "formula", {"formula_literal": "x=y"})
            ], identity="no_aplica")]
        )
        triplet = json.dumps(["ego", "produce", "acto"], ensure_ascii=False, separators=(",", ":"))
        products["relaciones_explicitas_corpus"] = write_product(
            fase11, masters, "relaciones_explicitas_corpus", [make_group("relaciones_explicitas_corpus", triplet, [
                make_ref("A", "R1", "relacion_explicita", {"sujeto_ref": "C1", "objeto_ref": "C3", "relacion_literal": "produce"})
            ])]
        )
        products["negaciones_excepciones_corpus"] = write_product(
            fase11, masters, "negaciones_excepciones_corpus", [
                make_group("negaciones_excepciones_corpus", "negacion::ego", [
                    make_ref("B", "N1", "negacion", {"clasificacion_negacion": "negacion_explicita", "objeto_negado_literal": "ego"})
                ], identity="no_aplica"),
                make_group("negaciones_excepciones_corpus", "excepcion::salvo x", [
                    make_ref("A", "E1", "excepcion", {"clasificacion_excepcion": "excepcion_explicita", "afirmacion_limitada_id": "AF1"})
                ], identity="no_aplica"),
            ]
        )
        products["variantes_terminologicas_corpus"] = write_product(
            fase11, masters, "variantes_terminologicas_corpus", [make_group("variantes_terminologicas_corpus", "yo", [c1])]
        )
        master_ref = make_ref("A", "M-A", "expediente_maestro_obra", estado_auditoria=None)
        products["distribucion_por_obra"] = write_product(
            fase11, masters, "distribucion_por_obra", [make_group("distribucion_por_obra", "A", [master_ref], identity="no_aplica")]
        )
        order_refs = [
            make_ref("A", "C1", "concepto", {"concepto_id": "C1", "apariciones_totales": 3}),
            make_ref("A", "C1B", "concepto", {"concepto_id": "C1B", "apariciones_totales": 2}),
            make_ref("B", "C2", "concepto", {"concepto_id": "C2", "apariciones_totales": 1}),
        ]
        products["orden_recurrencia"] = write_product(
            fase11, masters, "orden_recurrencia", [make_group("orden_recurrencia", "ego", order_refs)]
        )

        unaudited_concept = make_ref("A", "C-NA", "concepto", estado_auditoria=None)
        bad_concepts = write_product(
            negatives,
            masters,
            "conceptos_corpus",
            [make_group("conceptos_corpus", "sin-auditoria", [unaudited_concept])],
        )
        expect_audit_failure(negatives, "conceptos_corpus", bad_concepts, masters, "Registro no auditado")

        non_master_distribution = write_product(
            negatives,
            masters,
            "distribucion_por_obra",
            [make_group(
                "distribucion_por_obra",
                "A-invalida",
                [make_ref("A", "C-DIST", "concepto")],
                identity="no_aplica",
            )],
        )
        expect_audit_failure(
            negatives,
            "distribucion_por_obra",
            non_master_distribution,
            masters,
            "requiere expediente maestro",
        )

        unverified_master = make_ref("A", "M-NV", "expediente_maestro_obra", estado_auditoria=None)
        unverified_master["estado_verificacion"] = "pendiente"
        bad_master_distribution = write_product(
            negatives,
            masters,
            "distribucion_por_obra",
            [make_group("distribucion_por_obra", "A-no-verificada", [unverified_master], identity="no_aplica")],
        )
        expect_audit_failure(
            negatives,
            "distribucion_por_obra",
            bad_master_distribution,
            masters,
            "Registro no verificado",
        )

        closure = {
            "version": "1.0.0", "fase": 11, "fase11_cerrada": True,
            "criterio": "regresion", "fuente_exclusiva": "json_maestros_obra_auditados",
            "maestros": masters,
            "motores": [products[m] for m in EXPECTED_MOTORS],
            "clausura_descriptiva": {k: v for k, v in CLAUSURA_F11.items() if k != "solo_maestros_obra"},
        }
        closure_path = fase11 / "cierre-fase11.json"
        closure_path.write_text(json.dumps(closure, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")
        closure_sha = hashlib.sha256(closure_path.read_bytes()).hexdigest()
        storage = {
            "version": "1.0.0", "fase": 11, "estado": "evidencia_validada_persistida_fuera_de_blobs_git",
            "gate": {"fase11_cerrada": True, "head_sha": "0" * 40, "maestros": 20, "motores": 9, "cierre_sha256": closure_sha},
            "almacenamiento": {"tipo": "github_release_asset_zip", "release_tag": "synthetic", "asset": "synthetic.zip", "asset_sha256": "0" * 64},
            "productos": [{"motor": m, "ruta_en_zip": "fase11/" + products[m]["ruta"], "sha256": products[m]["sha256"]} for m in EXPECTED_MOTORS],
            "clausura_descriptiva": closure["clausura_descriptiva"],
        }
        storage_path = base / "almacenamiento-fase11.json"
        storage_path.write_text(json.dumps(storage, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")

        subprocess.run([sys.executable, str(MOTOR), "--fase11-dir", str(fase11), "--almacenamiento", str(storage_path), "--salida-dir", str(fase12)], check=True)
        dossier = json.loads((fase12 / "expedientes-transversales.jsonl").read_text(encoding="utf-8").strip())
        assert dossier["clave_recuperacion"] == "ego"
        assert dossier["estado_identidad_interobra"] == "no_determinada"
        assert dossier["multiplicidad"]["conceptos_registrados_total"] == 3
        assert dossier["multiplicidad"]["apariciones_totales_documentadas"] == 6
        assert dossier["multiplicidad"]["definiciones_registros_total"] == 2
        assert dossier["multiplicidad"]["predicaciones_registros_total"] == 2
        assert dossier["multiplicidad"]["vinculos_predicacion_concepto_total"] == 3
        assert dossier["variaciones_terminologicas"][0]["criterio_vinculo"] == "mismo_registro_conceptual_de_origen"
        assert dossier["relaciones_explicitas"][0]["roles_de_la_clave"] == ["sujeto"]
        assert dossier["negaciones_recuperadas_por_forma"][0]["estado_vinculo_conceptual"] == "no_determinado"
        assert dossier["excepciones_vinculadas_a_predicaciones"][0]["criterio_vinculo"] == "afirmacion_limitada_id_documentado"
        assert set(dossier["hallazgos"]) == {"definiciones_multiples", "multiplicidad_predicativa", "variacion_terminologica"}
        assert dossier["resolucion_doctrinal"] == "no_realizada"
        assert dossier["equivalencia_inferida"] is False
        assert dossier["evolucion_doctrinal_inferida"] is False
        assert dossier["definicion_preferida"] is False

        subprocess.run([
            sys.executable, str(VALIDATOR),
            "--fase11-dir", str(fase11),
            "--almacenamiento-fase11", str(storage_path),
            "--salida-dir", str(fase12),
            "--cierre", str(fase12 / "cierre-fase12.json"),
            "--schema-auditoria", str(SCHEMA_A),
            "--schema-expediente", str(SCHEMA_E),
        ], check=True)
        close = json.loads((fase12 / "cierre-fase12.json").read_text(encoding="utf-8"))
        assert close["fase12_cerrada"] is True
        assert close["expedientes_transversales"] == 1
        assert close["clausura_descriptiva"]["resolucion_doctrinal"] == "no_realizada"

    print("OK Fase 12: contrato especial de distribución preserva maestros verificados y auditoría estricta interna")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
