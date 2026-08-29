#!/usr/bin/env python3
"""Valida Fase 5 sobre los productos reales de Fase 4."""
from __future__ import annotations

import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "analista/esquema/contratos-v1.0.0.schema.json"
INPUT = ROOT / "analista/generado"
OUTPUT = INPUT / "normalizados"
MOTOR = ROOT / "analista/motores/normalizacion.py"

ARCHIVOS = {
    "apariciones-conceptuales.jsonl": ("aparicion_conceptual", 2575),
    "conceptos.jsonl": ("concepto", 21),
    "definiciones.jsonl": ("definicion", 21),
    "afirmaciones-candidatas.jsonl": ("afirmacion", 73),
    "formulas-candidatas.jsonl": ("formula", 20),
    "relaciones-explicitas.jsonl": ("relacion_explicita", 4),
    "distinciones.jsonl": ("distincion", 26),
    "negaciones.jsonl": ("negacion", 1509),
    "excepciones.jsonl": ("excepcion", 1),
    "restricciones-alcance.jsonl": ("restriccion_alcance", 3),
}
TOTAL_ESPERADO = sum(cantidad for _, cantidad in ARCHIVOS.values())
SPACE_RE = re.compile(r"\s+")
DASH_SPACE_RE = re.compile(r"\s*-\s*")
DASH_TRANS = str.maketrans(
    {"‐": "-", "‑": "-", "‒": "-", "–": "-", "—": "-", "−": "-"}
)


def cargar(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def formal(texto: str) -> str:
    return SPACE_RE.sub(" ", unicodedata.normalize("NFKC", texto)).strip()


def sin_diacriticos(texto: str) -> str:
    return "".join(
        ch for ch in unicodedata.normalize("NFD", texto) if unicodedata.category(ch) != "Mn"
    )


def variantes_esperadas(texto: str) -> list[str]:
    base = formal(texto).casefold()
    valores = [base, sin_diacriticos(base)]
    guiones = DASH_SPACE_RE.sub("-", base.translate(DASH_TRANS))
    valores += [guiones, sin_diacriticos(guiones)]
    out: list[str] = []
    for valor in valores:
        valor = SPACE_RE.sub(" ", valor).strip()
        if valor and valor not in out:
            out.append(valor)
    return out


def texto_recuperacion(registro: dict) -> str:
    campo = {
        "aparicion_conceptual": "forma_literal",
        "concepto": "designacion_operativa",
        "definicion": "texto_literal",
        "afirmacion": "texto_literal",
        "formula": "formula_literal",
        "relacion_explicita": "relacion_literal",
        "distincion": "texto_literal",
        "negacion": "objeto_negado_literal",
        "excepcion": "fragmento_exceptivo_literal",
        "restriccion_alcance": "fragmento_restriccion_literal",
    }[registro["tipo_registro"]]
    return registro[campo]


def validator_for(schema: dict, name: str) -> Draft202012Validator:
    return Draft202012Validator(
        {"$schema": schema["$schema"], "$defs": schema["$defs"], "$ref": f"#/$defs/{name}"}
    )


def main() -> int:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    total = 0
    entradas: dict[str, list[dict]] = {}
    salidas: dict[str, list[dict]] = {}

    for name, (tipo, cantidad) in ARCHIVOS.items():
        origen = INPUT / name
        destino = OUTPUT / name
        assert origen.is_file(), f"Falta entrada de Fase 4: {name}"
        assert destino.is_file(), f"Falta salida normalizada: {name}"
        antes = cargar(origen)
        despues = cargar(destino)
        entradas[name] = antes
        salidas[name] = despues
        assert len(antes) == len(despues) == cantidad, (
            f"Conteo inesperado en {name}: {len(antes)} / {len(despues)} != {cantidad}"
        )
        assert [r["id"] for r in antes] == [r["id"] for r in despues], (
            f"Fase 5 modificó IDs u orden en {name}"
        )

        validador = validator_for(schema, tipo)
        for original, normalizado in zip(antes, despues):
            errors = list(validador.iter_errors(normalizado))
            assert not errors, f"Salida inválida {normalizado['id']}: {errors[0].message}"
            assert set(original) == set(normalizado), (
                f"Fase 5 añadió/eliminó campos en {normalizado['id']}"
            )
            for key in original:
                if key not in {"normalizacion_formal", "normalizacion_lexica"}:
                    assert original[key] == normalizado[key], (
                        f"Mutación no autorizada {name}/{normalizado['id']}/{key}"
                    )
            texto = texto_recuperacion(original)
            assert normalizado["normalizacion_formal"] == formal(texto)
            assert normalizado["normalizacion_lexica"] == variantes_esperadas(texto)
            assert normalizado["normalizacion_lexica"], normalizado["id"]
        total += cantidad

    assert total == TOTAL_ESPERADO == 4253

    # Invariantes conceptuales: Fase 5 recupera, pero no decide identidad.
    c0 = {r["id"]: r for r in entradas["conceptos.jsonl"]}
    c1 = {r["id"]: r for r in salidas["conceptos.jsonl"]}
    assert set(c0) == set(c1) and len(c0) == 21
    for concepto_id in c0:
        assert c0[concepto_id]["aparicion_ids"] == c1[concepto_id]["aparicion_ids"]
        assert c0[concepto_id]["estado_identidad_conceptual"] == c1[concepto_id]["estado_identidad_conceptual"]
        assert c0[concepto_id]["evidencia_identidad_ids"] == c1[concepto_id]["evidencia_identidad_ids"]

    a0 = entradas["apariciones-conceptuales.jsonl"]
    a1 = salidas["apariciones-conceptuales.jsonl"]
    assert [r["concepto_id"] for r in a0] == [r["concepto_id"] for r in a1]

    # Pruebas reales de variantes permitidas.
    por_nombre = {r["designacion_operativa"]: r for r in salidas["conceptos.jsonl"]}
    assert "pasion" in por_nombre["Pasión"]["normalizacion_lexica"]
    assert por_nombre["φ₁ — Primera mediación"]["normalizacion_formal"].startswith("φ1")
    assert "φ1-primera mediacion" in por_nombre["φ₁ — Primera mediación"]["normalizacion_lexica"]

    # Clausura: no se generan equivalencias, abreviaciones semánticas ni sinónimos.
    assert "aego" not in por_nombre["Afasia volitiva"]["normalizacion_lexica"]
    assert "integral" not in por_nombre["Integral del ego — I(t)"]["normalizacion_lexica"]
    assert all("amor" not in v and "eros" not in v for v in por_nombre["Pasión"]["normalizacion_lexica"])

    # Reproducibilidad byte a byte.
    antes_bytes = {name: (OUTPUT / name).read_bytes() for name in ARCHIVOS}
    subprocess.run([sys.executable, str(MOTOR)], cwd=ROOT, check=True)
    for name, content in antes_bytes.items():
        assert (OUTPUT / name).read_bytes() == content, f"Salida no reproducible: {name}"

    print(
        "OK Fase 5: 4253 registros reales normalizados; 21 IDs conceptuales y todas las "
        "referencias preservados; variantes Unicode/casefold/diacríticas/tipográficas recuperadas; "
        "0 sinónimos, 0 fusiones conceptuales."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
