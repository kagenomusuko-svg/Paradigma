#!/usr/bin/env python3
"""Normalización conservadora para recuperación — Fase 5.

La salida es un overlay: conserva cada registro de Fase 4 y modifica únicamente
`normalizacion_formal` y `normalizacion_lexica`. No crea equivalencias, no
fusiona conceptos, no cambia IDs ni referencias y no añade sinónimos.
"""
from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INPUT = ROOT / "analista/generado"
DEFAULT_OUTPUT = DEFAULT_INPUT / "normalizados"
MOTOR_VERSION = "1.0.0"

ARCHIVOS = (
    "apariciones-conceptuales.jsonl",
    "conceptos.jsonl",
    "definiciones.jsonl",
    "afirmaciones-candidatas.jsonl",
    "formulas-candidatas.jsonl",
    "relaciones-explicitas.jsonl",
    "distinciones.jsonl",
    "negaciones.jsonl",
    "excepciones.jsonl",
    "restricciones-alcance.jsonl",
)

SPACE_RE = re.compile(r"\s+")
DASH_SPACE_RE = re.compile(r"\s*-\s*")
DASH_TRANS = str.maketrans(
    {"‐": "-", "‑": "-", "‒": "-", "–": "-", "—": "-", "−": "-"}
)


def normalizacion_formal(texto: str) -> str:
    """Nivel 1: compatibilidad Unicode + espacio, sin reescritura conceptual."""
    return SPACE_RE.sub(" ", unicodedata.normalize("NFKC", texto)).strip()


def sin_diacriticos(texto: str) -> str:
    return "".join(
        ch
        for ch in unicodedata.normalize("NFD", texto)
        if unicodedata.category(ch) != "Mn"
    )


def variantes_lexicas(texto: str) -> list[str]:
    """Nivel 2: variantes mecánicas de búsqueda; no usa sinónimos ni lemas."""
    formal = normalizacion_formal(texto)
    variantes: list[str] = []

    def agregar(valor: str) -> None:
        valor = SPACE_RE.sub(" ", valor).strip()
        if valor and valor not in variantes:
            variantes.append(valor)

    plegada = formal.casefold()
    agregar(plegada)
    agregar(sin_diacriticos(plegada))

    guiones = DASH_SPACE_RE.sub("-", plegada.translate(DASH_TRANS))
    agregar(guiones)
    agregar(sin_diacriticos(guiones))
    return variantes


def texto_recuperacion(registro: dict) -> str:
    """Selecciona únicamente un campo literal ya presente en cada contrato."""
    campo_por_tipo = {
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
    }
    tipo = registro.get("tipo_registro")
    if tipo not in campo_por_tipo:
        raise ValueError(f"Tipo no normalizable en Fase 5: {tipo!r}")
    campo = campo_por_tipo[tipo]
    valor = registro.get(campo)
    if not isinstance(valor, str) or not valor.strip():
        raise ValueError(f"{registro.get('id')}: campo literal vacío {campo}")
    return valor


def cargar_jsonl(path: Path) -> list[dict]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def guardar_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows),
        encoding="utf-8",
    )


def normalizar_archivo(origen: Path, destino: Path) -> int:
    rows = cargar_jsonl(origen)
    for row in rows:
        texto = texto_recuperacion(row)
        # Únicas mutaciones autorizadas en este overlay.
        row["normalizacion_formal"] = normalizacion_formal(texto)
        row["normalizacion_lexica"] = variantes_lexicas(texto)
    guardar_jsonl(destino, rows)
    return len(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-root", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    faltantes = [name for name in ARCHIVOS if not (args.input_root / name).is_file()]
    if faltantes:
        raise SystemExit(
            "Faltan productos obligatorios de Fase 4: " + ", ".join(faltantes)
        )

    total = 0
    for name in ARCHIVOS:
        cantidad = normalizar_archivo(args.input_root / name, args.output_root / name)
        total += cantidad
        print(f"{name}: {cantidad} registros normalizados")

    print(
        f"Fase 5: {total} registros normalizados; IDs y referencias preservados; "
        "sin sinonimia, lematización ni fusión conceptual."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
