#!/usr/bin/env python3
"""Valida 4F sobre productos reales y evidencia literal de la obra piloto."""
from __future__ import annotations

import copy
import json
import re
import subprocess
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "analista/esquema/contratos-v1.0.0.schema.json"
UNIDADES = ROOT / "analista/generado/unidades.jsonl"
DISTINCIONES = ROOT / "analista/generado/distinciones.jsonl"
NEGACIONES = ROOT / "analista/generado/negaciones.jsonl"
EXCEPCIONES = ROOT / "analista/generado/excepciones.jsonl"
RESTRICCIONES = ROOT / "analista/generado/restricciones-alcance.jsonl"
COBERTURA = ROOT / "analista/generado/cobertura-limitadores.jsonl"
MOTOR = ROOT / "analista/motores/limitadores.py"
PILOTO_ID = "AA-SP-V1"

NO_RE = re.compile(r"(?<![\w-])no(?![\w-])", re.IGNORECASE)
DIST_RE = re.compile(r"\bno\s+(?:es|son)\s+(.+?)\s+sino\s+(.+?)(?=[.;]|$)", re.IGNORECASE)
EXC_RE = re.compile(
    r"\b(?:a excepción de|con excepción de|excepto|salvo\s+(?:que|cuando|si|por|en|los|las|el|la|un|una))\b",
    re.IGNORECASE,
)
RES_RE = re.compile(
    r"\b(?:solo si|sólo si|únicamente|exclusivamente|siempre que|a menos que|en la medida en que)\b",
    re.IGNORECASE,
)
EXPECTED_COUNTS = {
    "distincion": 26,
    "negacion": 1509,
    "excepcion": 1,
    "restriccion_alcance": 3,
}


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def validator_for(schema: dict, name: str) -> Draft202012Validator:
    return Draft202012Validator(
        {"$schema": schema["$schema"], "$defs": schema["$defs"], "$ref": f"#/$defs/{name}"}
    )


def source_line(record: dict, unit: dict) -> str:
    loc = record["localizacion"]
    assert loc["linea_inicio"] == loc["linea_fin"]
    assert loc["ruta"] == unit["archivo"]
    assert unit["localizacion"]["linea_inicio"] <= loc["linea_inicio"] <= unit["localizacion"]["linea_fin"]
    canonical = (ROOT / loc["ruta"]).read_text(encoding="utf-8").splitlines()[loc["linea_inicio"] - 1]
    offset = loc["linea_inicio"] - unit["localizacion"]["linea_inicio"]
    unit_line = unit["texto_literal"].splitlines()[offset]
    assert canonical == unit_line
    assert record["texto_literal"] in canonical
    return canonical


def expected_from_units(units: list[dict]) -> dict[str, set[tuple]]:
    out: dict[str, set[tuple]] = {
        "distincion": set(),
        "negacion": set(),
        "excepcion": set(),
        "restriccion_alcance": set(),
    }
    for unit in units:
        start = unit["localizacion"]["linea_inicio"]
        lines = unit["texto_literal"].splitlines()
        assert len(lines) == unit["localizacion"]["linea_fin"] - start + 1
        for line_no, literal in enumerate(lines, start=start):
            dm = DIST_RE.search(literal)
            if dm:
                out["distincion"].add(
                    (unit["id"], unit["archivo"], line_no, literal, dm.group(1).strip(), dm.group(2).strip())
                )
            nm = NO_RE.search(literal)
            if nm:
                out["negacion"].add(
                    (unit["id"], unit["archivo"], line_no, literal, literal[nm.start():])
                )
            em = EXC_RE.search(literal)
            if em:
                out["excepcion"].add(
                    (unit["id"], unit["archivo"], line_no, literal, literal[em.start():])
                )
            rm = RES_RE.search(literal)
            if rm:
                out["restriccion_alcance"].add(
                    (unit["id"], unit["archivo"], line_no, literal, literal[rm.start():])
                )
    return out


def assert_common(record: dict, unit_by_id: dict[str, dict]) -> str:
    assert record["fuente_id"] == PILOTO_ID
    assert record["unidad_id"] in unit_by_id
    assert record["estado_extraccion"] == "candidato"
    assert record["estado_verificacion"] == "pendiente"
    assert record["estado_auditoria"] == "pendiente"
    assert record["estatus_enunciativo"] == "no_determinado"
    assert record["normalizacion_formal"] is None
    assert record["normalizacion_lexica"] is None
    assert record["producido_por"] == {"motor": "limitadores", "version": "1.0.1"}
    return source_line(record, unit_by_id[record["unidad_id"]])


def assert_reproducible(paths: list[Path]) -> None:
    before = {path: path.read_bytes() for path in paths}
    subprocess.run([sys.executable, str(MOTOR)], cwd=ROOT, check=True)
    for path, content in before.items():
        assert path.read_bytes() == content, f"Salida no reproducible: {path.name}"


def main() -> int:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    validators = {
        "distincion": validator_for(schema, "distincion"),
        "negacion": validator_for(schema, "negacion"),
        "excepcion": validator_for(schema, "excepcion"),
        "restriccion_alcance": validator_for(schema, "restriccion_alcance"),
        "reporte_cobertura": validator_for(schema, "reporte_cobertura"),
    }
    units = [u for u in load_jsonl(UNIDADES) if u["fuente_id"] == PILOTO_ID]
    unit_by_id = {u["id"]: u for u in units}
    assert len(units) == 836

    rows = {
        "distincion": load_jsonl(DISTINCIONES),
        "negacion": load_jsonl(NEGACIONES),
        "excepcion": load_jsonl(EXCEPCIONES),
        "restriccion_alcance": load_jsonl(RESTRICCIONES),
    }
    expected = expected_from_units(units)
    for kind, records in rows.items():
        assert len(records) == EXPECTED_COUNTS[kind], (
            f"Línea base 4F alterada para {kind}: {len(records)} != {EXPECTED_COUNTS[kind]}"
        )
        assert len(expected[kind]) == EXPECTED_COUNTS[kind]
        ids: set[str] = set()
        observed: set[tuple] = set()
        for record in records:
            errors = list(validators[kind].iter_errors(record))
            assert not errors, f"{kind} inválida {record.get('id')}: {errors[0].message}"
            assert record["id"] not in ids
            ids.add(record["id"])
            literal = assert_common(record, unit_by_id)
            loc = record["localizacion"]

            if kind == "distincion":
                match = DIST_RE.search(literal)
                assert match
                assert record["texto_literal"] == match.group(0)
                assert record["termino_a_literal"] == match.group(1).strip()
                assert record["termino_b_literal"] == match.group(2).strip()
                assert record["marcador_literal"] == match.group(0)
                assert record["clasificacion_distincion"] == "distincion_candidata"
                observed.add(
                    (
                        record["unidad_id"], loc["ruta"], loc["linea_inicio"], literal,
                        record["termino_a_literal"], record["termino_b_literal"],
                    )
                )
            elif kind == "negacion":
                match = NO_RE.search(literal)
                assert match
                assert record["texto_literal"] == match.group(0)
                assert record["objeto_negado_literal"] == literal[match.start():]
                assert record["alcance_literal"] is None
                assert record["clasificacion_negacion"] == "negacion_candidata"
                observed.add(
                    (record["unidad_id"], loc["ruta"], loc["linea_inicio"], literal, record["objeto_negado_literal"])
                )
            elif kind == "excepcion":
                match = EXC_RE.search(literal)
                assert match
                assert record["afirmacion_limitada_id"] is None
                assert record["texto_literal"] == literal[match.start():]
                assert record["fragmento_exceptivo_literal"] == literal[match.start():]
                assert record["clasificacion_excepcion"] == "excepcion_candidata"
                observed.add(
                    (record["unidad_id"], loc["ruta"], loc["linea_inicio"], literal, record["fragmento_exceptivo_literal"])
                )
            else:
                match = RES_RE.search(literal)
                assert match
                assert record["afirmacion_limitada_id"] is None
                assert record["tipo_restriccion"] == "no_determinada"
                assert record["texto_literal"] == literal[match.start():]
                assert record["fragmento_restriccion_literal"] == literal[match.start():]
                assert record["clasificacion_restriccion"] == "restriccion_candidata"
                observed.add(
                    (record["unidad_id"], loc["ruta"], loc["linea_inicio"], literal, record["fragmento_restriccion_literal"])
                )
        assert observed == expected[kind], f"Cobertura de marcadores divergente para {kind}"

        forbidden = copy.deepcopy(records[0])
        forbidden["solucion_doctrinal"] = "X"
        assert not validators[kind].is_valid(forbidden), f"El contrato de {kind} aceptó campo doctrinal."

    coverage_rows = load_jsonl(COBERTURA)
    assert len(coverage_rows) == 1
    coverage = coverage_rows[0]
    errors = list(validators["reporte_cobertura"].iter_errors(coverage))
    assert not errors, errors[0].message if errors else ""
    assert coverage["obra_id"] == PILOTO_ID
    assert coverage["motor"] == "limitadores"
    assert coverage["version_motor"] == "1.0.1"
    assert coverage["unidades_totales"] == coverage["unidades_procesadas"] == len(units)
    assert coverage["unidades_omitidas"] == []
    assert coverage["errores"] == []
    assert coverage["estado_verificacion"] == "pendiente"

    assert all(r["estatus_enunciativo"] != "negacion_autoral" for r in rows["negacion"])
    assert all(r["afirmacion_limitada_id"] is None for r in rows["excepcion"] + rows["restriccion_alcance"])

    assert_reproducible([DISTINCIONES, NEGACIONES, EXCEPCIONES, RESTRICCIONES, COBERTURA])
    print(
        "OK Fase 4F: 26 distinciones candidatas; 1509 negaciones candidatas; "
        "1 excepción candidata; 3 restricciones candidatas; 836/836 unidades; "
        "voz autoral no determinada; 0 vínculos de afirmación inferidos."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
