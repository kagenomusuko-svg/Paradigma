#!/usr/bin/env python3
"""Validación de cierre de la Fase 3 sobre productos reales."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "analista" / "esquema" / "contratos-v1.0.0.schema.json"
FUENTES_PATH = ROOT / "analista" / "generado" / "fuentes.jsonl"
UNIDADES_PATH = ROOT / "analista" / "generado" / "unidades.jsonl"
COBERTURA_PATH = ROOT / "analista" / "generado" / "cobertura-unidades.jsonl"
LEGACY_PILOTO = ROOT / "analisis" / "generado" / "sobre-la-pasion" / "unidades.jsonl"
MOTOR_PATH = ROOT / "analista" / "motores" / "unidades.py"


def load_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    with path.open("r", encoding="utf-8") as fh:
        for n, raw in enumerate(fh, start=1):
            if not raw.strip():
                continue
            try:
                rows.append(json.loads(raw))
            except json.JSONDecodeError as exc:
                raise AssertionError(f"JSONL inválido {path}:{n}: {exc}") from exc
    return rows


def stable_id(prefix: str, *parts: str) -> str:
    payload = "\x1f".join(parts).encode("utf-8")
    return f"{prefix}-{hashlib.sha1(payload).hexdigest()[:12].upper()}"


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def assert_reproducible() -> None:
    before_units = UNIDADES_PATH.read_bytes()
    before_coverage = COBERTURA_PATH.read_bytes()
    subprocess.run([sys.executable, str(MOTOR_PATH)], cwd=ROOT, check=True)
    assert UNIDADES_PATH.read_bytes() == before_units, "unidades.jsonl no es reproducible"
    assert (
        COBERTURA_PATH.read_bytes() == before_coverage
    ), "cobertura-unidades.jsonl no es reproducible"


def main() -> int:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    unit_validator = Draft202012Validator(
        {
            "$schema": schema["$schema"],
            "$defs": schema["$defs"],
            "$ref": "#/$defs/unidad_textual",
        }
    )
    coverage_validator = Draft202012Validator(
        {
            "$schema": schema["$schema"],
            "$defs": schema["$defs"],
            "$ref": "#/$defs/reporte_cobertura",
        }
    )

    fuentes = load_jsonl(FUENTES_PATH)
    unidades = load_jsonl(UNIDADES_PATH)
    reportes = load_jsonl(COBERTURA_PATH)

    assert fuentes, "No hay fuentes."
    assert unidades, "No hay unidades."
    assert len(reportes) == len(fuentes), "Debe existir un reporte por fuente."

    fuente_por_id = {row["id"]: row for row in fuentes}
    assert len(fuente_por_id) == len(fuentes), "IDs de fuente duplicados."

    unidades_por_fuente: dict[str, list[dict]] = defaultdict(list)
    for unit in unidades:
        errors = sorted(unit_validator.iter_errors(unit), key=lambda e: list(e.absolute_path))
        assert not errors, f"Unidad inválida {unit.get('id')}: {errors[0].message}"
        assert unit["tipo_registro"] == "unidad_textual"
        assert unit["fuente_id"] in fuente_por_id, f"Fuente desconocida en {unit['id']}"
        assert unit["texto_literal"]
        assert unit["normalizacion_formal"] is None
        assert unit["normalizacion_lexica"] is None
        assert unit["estatus_enunciativo"] is None
        assert unit["estado_verificacion"] == "verificado"
        assert unit["estado_auditoria"] == "no_aplica"
        assert unit["localizacion"]["ruta"] == unit["archivo"]
        assert unit["sha256_texto"] == sha256_text(unit["texto_literal"])
        expected_id = stable_id(
            "UT",
            unit["archivo"],
            str(unit["localizacion"]["linea_inicio"]),
            unit["texto_literal"].strip(),
        )
        assert unit["id"] == expected_id, f"ID no reproducible: {unit['id']}"
        unidades_por_fuente[unit["fuente_id"]].append(unit)

    unit_ids = [u["id"] for u in unidades]
    assert len(unit_ids) == len(set(unit_ids)), "IDs de unidad duplicados."

    reportes_por_obra = {}
    for report in reportes:
        errors = sorted(coverage_validator.iter_errors(report), key=lambda e: list(e.absolute_path))
        assert not errors, f"Reporte inválido {report.get('id')}: {errors[0].message}"
        assert report["tipo_registro"] == "reporte_cobertura"
        assert report["obra_id"] in fuente_por_id
        assert report["obra_id"] not in reportes_por_obra, "Reporte duplicado por fuente."
        reportes_por_obra[report["obra_id"]] = report

    assert set(reportes_por_obra) == set(fuente_por_id), "Cobertura incompleta por fuente."

    total_eligible_lines = 0
    total_covered_lines = 0

    for fuente_id, fuente in fuente_por_id.items():
        source_units = unidades_por_fuente.get(fuente_id, [])
        report = reportes_por_obra[fuente_id]

        assert report["motor"] == "unidades"
        assert report["unidades_totales"] == len(source_units)
        assert report["unidades_procesadas"] == len(source_units)
        assert report["unidades_omitidas"] == []
        assert report["errores"] == []

        assert [u["orden_textual"] for u in source_units] == list(
            range(len(source_units))
        ), f"Orden textual discontinuo en {fuente_id}"

        expected_files = fuente["rutas_derivadas"]
        actual_files = {u["archivo"] for u in source_units}
        files_with_text = set()

        by_file: dict[str, list[dict]] = defaultdict(list)
        for unit in source_units:
            assert unit["archivo"] in expected_files, (
                f"Archivo ajeno a la fuente {fuente_id}: {unit['archivo']}"
            )
            by_file[unit["archivo"]].append(unit)

        for rel in expected_files:
            path = ROOT / rel
            lines = path.read_text(encoding="utf-8").splitlines()
            eligible = {n for n, line in enumerate(lines, start=1) if line.strip()}
            total_eligible_lines += len(eligible)
            if eligible:
                files_with_text.add(rel)

            covered_counter: Counter[int] = Counter()
            file_units = by_file.get(rel, [])
            for unit in file_units:
                loc = unit["localizacion"]
                start = loc["linea_inicio"]
                end = loc["linea_fin"]
                assert 1 <= start <= end <= len(lines), (
                    f"Rango inválido {unit['id']} en {rel}"
                )
                expected_text = "\n".join(lines[start - 1 : end])
                assert unit["texto_literal"] == expected_text, (
                    f"Texto no literal en {unit['id']}"
                )
                for line_no in range(start, end + 1):
                    assert lines[line_no - 1].strip(), (
                        f"Unidad {unit['id']} incluye línea vacía {line_no}"
                    )
                    covered_counter[line_no] += 1

            duplicated = [n for n, count in covered_counter.items() if count != 1]
            assert not duplicated, f"Solapamiento de líneas en {rel}: {duplicated[:5]}"
            covered = set(covered_counter)
            assert covered == eligible, (
                f"Cobertura incompleta en {rel}: "
                f"faltan={sorted(eligible - covered)[:5]} "
                f"sobran={sorted(covered - eligible)[:5]}"
            )
            total_covered_lines += len(covered)

        assert actual_files == files_with_text, (
            f"Archivos textuales no representados en {fuente_id}: "
            f"esperados={sorted(files_with_text)} actuales={sorted(actual_files)}"
        )

    assert total_eligible_lines == total_covered_lines

    # Preservación de referencias del prototipo: mismos límites y texto => mismo ID.
    if LEGACY_PILOTO.is_file():
        legacy = load_jsonl(LEGACY_PILOTO)
        new_index = {
            (
                u["archivo"],
                u["localizacion"]["linea_inicio"],
                u["localizacion"]["linea_fin"],
            ): u
            for u in unidades_por_fuente["AA-SP-V1"]
        }
        assert len(legacy) == len(new_index), (
            "La nueva segmentación del piloto cambió el número de unidades históricas."
        )
        for old in legacy:
            key = (old["ruta"], old["linea_inicio"], old["linea_fin"])
            assert key in new_index, f"Unidad histórica no preservada: {old['id']}"
            new = new_index[key]
            assert new["texto_literal"].strip() == old["texto"]
            assert new["id"] == old["id"], f"ID histórico alterado: {old['id']}"

    # La clausura descriptiva sigue activa en el contrato.
    mutated = dict(unidades[0])
    mutated["solucion_doctrinal"] = "X"
    assert not unit_validator.is_valid(mutated), "El esquema aceptó un campo doctrinal prohibido."

    assert_reproducible()

    print(
        "OK Fase 3: "
        f"{len(unidades)} unidades verificadas en {len(fuentes)} fuentes; "
        f"{total_covered_lines} líneas textuales cubiertas exactamente una vez; "
        "0 omitidas; 0 errores; IDs históricos del piloto preservados."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
