#!/usr/bin/env python3
"""Verifica que cada fuente Markdown canónica tenga derivados estructurales."""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
FUENTES = ROOT / "corpus" / "fuentes"
LIBROS = ROOT / "corpus" / "libros"
CATALOGO = ROOT / "corpus" / "catalogo-generado.json"


def main() -> None:
    fuentes = {f"corpus/fuentes/{path.name}" for path in FUENTES.glob("*.md")}
    catalogo = json.loads(CATALOGO.read_text(encoding="utf-8"))
    representadas = [item.get("source") for item in catalogo]

    duplicadas = sorted(source for source, count in Counter(representadas).items() if count > 1)
    faltantes = sorted(fuentes - set(representadas))
    extra = sorted(set(representadas) - fuentes)

    estructuras = list(LIBROS.rglob("estructura.json"))
    errores = []
    if duplicadas:
        errores.append("Fuentes duplicadas en catálogo:\n" + "\n".join(f"- {x}" for x in duplicadas))
    if faltantes:
        errores.append("Fuentes canónicas sin segmentación:\n" + "\n".join(f"- {x}" for x in faltantes))
    if extra:
        errores.append("Entradas de catálogo sin fuente canónica:\n" + "\n".join(f"- {x}" for x in extra))
    if len(estructuras) != len(catalogo):
        errores.append(
            f"Estructuras y catálogo no coinciden: {len(estructuras)} estructura.json frente a {len(catalogo)} entradas."
        )

    for item in catalogo:
        source = item.get("source")
        if not source or not (ROOT / source).is_file():
            errores.append(f"Fuente inexistente referenciada por catálogo: {source!r}")
        for segment in item.get("segments", []):
            path = segment.get("path")
            if not path or not (ROOT / path).is_file():
                errores.append(f"Segmento inexistente: {path!r} ({item.get('title')})")

    if errores:
        raise RuntimeError("\n\n".join(errores))

    print(
        f"Cobertura integral validada: {len(fuentes)} fuentes canónicas, "
        f"{len(catalogo)} obras catalogadas, {len(estructuras)} estructuras."
    )


if __name__ == "__main__":
    main()
