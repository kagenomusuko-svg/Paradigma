#!/usr/bin/env python3
"""Construye un catálogo único a partir de todos los estructura.json derivados."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
LIBROS = ROOT / "corpus" / "libros"
SALIDA = ROOT / "corpus" / "catalogo-generado.json"

catalogo = []
for path in sorted(LIBROS.rglob("estructura.json")):
    catalogo.append(json.loads(path.read_text(encoding="utf-8")))

catalogo.sort(key=lambda item: (item.get("collection") or item.get("series") or "", item.get("volume") or 0, item.get("title") or ""))
SALIDA.write_text(json.dumps(catalogo, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Catálogo reconstruido: {len(catalogo)} obras.")
