#!/usr/bin/env python3
"""Gate global y reproducible de cierre administrativo de Fase 10.

Solo emite ``fase10_cerrada=true`` después de ejecutar y validar de forma
independiente las veinte obras previstas. No compara contenidos entre obras ni
produce síntesis doctrinal. Para las diecinueve repeticiones, el propio maestro
transporta el alcance conceptual de la obra para que una etapa posterior no
confunda ausencia de extracción autorizada con ausencia semántica.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INVENTORY_ENGINE = ROOT / "analista/motores/inventariar_obras_fase10.py"
INVENTORY_VALIDATOR = ROOT / "analista/pruebas/validar_inventario_fase10.py"
WORK_VALIDATOR = ROOT / "analista/pruebas/validar_obra_fase10.py"
PILOT_VALIDATOR = ROOT / "analista/pruebas/validar_maestro_fase9.py"
INVENTORY = ROOT / "analista/generado/fase10/inventario-obras.json"
MASTERS = ROOT / "analista/generado/maestros"
REPORT = ROOT / "analista/generado/fase10/cierre-fase10.json"
PILOT = "AA-SP-V1"
VERSION = "1.1.0"


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, cwd=ROOT, check=True)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    run([sys.executable, str(INVENTORY_ENGINE)])
    run([sys.executable, str(INVENTORY_VALIDATOR)])
    inventory = json.loads(INVENTORY.read_text(encoding="utf-8"))
    works = inventory["obras"]
    assert len(works) == inventory["fuentes"] == 20
    assert inventory["obras_con_glosario"] == 8
    assert inventory["obras_sin_glosario"] == 12
    assert inventory["piloto_id"] == PILOT
    ids = [work["obra_id"] for work in works]
    assert len(ids) == len(set(ids)) == 20
    assert ids.count(PILOT) == 1

    # El piloto conserva su cierre completo de Fase 9. Las otras diecinueve
    # obras se regeneran y validan mediante la cadena parametrizada de Fase 10.
    run([sys.executable, str(PILOT_VALIDATOR)])
    for work in works:
        obra_id = work["obra_id"]
        if obra_id != PILOT:
            run([sys.executable, str(WORK_VALIDATOR), "--obra-id", obra_id])

    expected_master_names = {f"{obra_id}.json" for obra_id in ids}
    found_master_names = {path.name for path in MASTERS.glob("*.json")}
    assert found_master_names == expected_master_names, {
        "faltantes": sorted(expected_master_names - found_master_names),
        "extras": sorted(found_master_names - expected_master_names),
    }

    closure_works: list[dict] = []
    for work in works:
        obra_id = work["obra_id"]
        master_path = MASTERS / f"{obra_id}.json"
        sidecar = master_path.with_suffix(master_path.suffix + ".sha256")
        assert master_path.is_file() and sidecar.is_file()
        master = json.loads(master_path.read_text(encoding="utf-8"))
        assert master["tipo_registro"] == "expediente_maestro_obra"
        assert master["obra_id"] == obra_id
        assert master["titulo"] == work["titulo"]
        assert len(master["fuentes"]) == 1 and master["fuentes"][0]["id"] == obra_id
        assert len(master["unidades"]) == work["unidades"]
        digest, filename = sidecar.read_text(encoding="utf-8").strip().split("  ", 1)
        assert filename == master_path.name
        assert digest == sha(master_path)

        if obra_id == PILOT:
            assert master["schema_version"] == "1.1.0"
            route = "piloto_cerrado_fase9"
            comparison = False
            conceptual_enabled = True
        else:
            assert master["schema_version"] == "1.3.0"
            assert master["producido_por"] == {
                "motor": "ensamblador_maestro_obra_fase10",
                "version": "1.1.0",
            }
            controls = master["controles_fase10"]
            assert controls["version"] == "1.1.0"
            assert controls["obra_id"] == obra_id
            assert controls["comparacion_interobra"] is False
            assert controls["maestro_independiente"] is True
            assert controls["normalizacion_recuperacion"] is True
            assert controls["verificacion_evidencia"] is True
            assert controls["auditoria_intraobra"] is True

            scope = controls["alcance_conceptual"]
            assert scope["perfil"] == work["perfil_conceptual"]
            assert scope["glosario_tecnico"] == work["glosario_tecnico"]
            assert scope["identidades_conceptuales_inferidas"] is False
            assert scope["glosario_interobra_reutilizado"] is False
            assert scope["interpretacion_cero_registros"] == "no_autoriza_afirmar_ausencia_semantica"

            manifest = json.loads(
                (ROOT / "analista/generado/obras" / obra_id / "manifest-extractores.json").read_text(encoding="utf-8")
            )
            assert manifest["version"] == "1.3.0"
            assert manifest["obra_id"] == obra_id
            assert manifest["comparacion_interobra"] is False
            assert manifest["perfil_conceptual"] == scope["perfil"]
            assert manifest["glosario_tecnico"] == scope["glosario_tecnico"]
            limits = manifest["limitaciones_conceptuales"]
            assert scope["extraccion_conceptual_habilitada"] == limits["extraccion_conceptual_habilitada"]
            assert limits["identidades_conceptuales_inferidas"] is False
            assert limits["glosario_interobra_reutilizado"] is False
            assert limits["interpretacion_cero_registros"] == "no_autoriza_afirmar_ausencia_semantica"

            if work["glosario_tecnico"] is None:
                assert scope["perfil"] == "sin_glosario_tecnico_explicito"
                assert scope["extraccion_conceptual_habilitada"] is False
                assert not master["apariciones_conceptuales"]
                assert not master["conceptos"]
                assert not master["definiciones"]
                assert not master["relaciones_explicitas"]
            else:
                assert scope["perfil"] == "glosario_tecnico_explicito"
                assert scope["extraccion_conceptual_habilitada"] is True

            assert all(
                finding.get("resolucion_doctrinal") == "no_realizada"
                for finding in master["hallazgos_auditoria"]
            )
            route = "repeticion_controlada_fase10"
            comparison = controls["comparacion_interobra"]
            conceptual_enabled = scope["extraccion_conceptual_habilitada"]

        closure_works.append({
            "obra_id": obra_id,
            "titulo": work["titulo"],
            "ruta_cierre": route,
            "schema_maestro": master["schema_version"],
            "perfil_conceptual": work["perfil_conceptual"],
            "extraccion_conceptual_habilitada": conceptual_enabled,
            "unidades": work["unidades"],
            "maestro": master_path.relative_to(ROOT).as_posix(),
            "maestro_sha256": sha(master_path),
            "comparacion_interobra": comparison,
        })

    report = {
        "version": VERSION,
        "fase": 10,
        "fase10_cerrada": True,
        "criterio": "todas_las_obras_previstas_con_maestro_independiente_validado",
        "inventario": {
            "obras": len(works),
            "con_glosario_tecnico_explicito": inventory["obras_con_glosario"],
            "sin_glosario_tecnico_explicito": inventory["obras_sin_glosario"],
            "piloto_id": PILOT,
        },
        "clausura_descriptiva": {
            "comparacion_interobra": False,
            "sintesis_doctrinal": False,
            "resolucion_doctrinal": "no_realizada",
            "ausencia_de_registros_implica_ausencia_semantica": False,
        },
        "obras": closure_works,
    }
    payload = (json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_bytes(payload)
    sidecar = REPORT.with_suffix(REPORT.suffix + ".sha256")
    sidecar.write_text(f"{hashlib.sha256(payload).hexdigest()}  {REPORT.name}\n", encoding="utf-8")

    persisted = json.loads(REPORT.read_text(encoding="utf-8"))
    assert persisted == report and persisted["fase10_cerrada"] is True
    assert len(persisted["obras"]) == 20
    assert all(row["comparacion_interobra"] is False for row in persisted["obras"])
    digest, filename = sidecar.read_text(encoding="utf-8").strip().split("  ", 1)
    assert filename == REPORT.name and digest == sha(REPORT)

    print(json.dumps({
        "fase": 10,
        "fase10_cerrada": True,
        "obras": len(closure_works),
        "maestros": len(found_master_names),
        "repeticiones_fase10": len(closure_works) - 1,
        "comparacion_interobra": False,
        "reporte_sha256": sha(REPORT),
    }, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
