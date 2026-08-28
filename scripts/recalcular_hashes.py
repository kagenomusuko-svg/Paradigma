#!/usr/bin/env python3
"""Recalcula SHA-256 de todas las fuentes Markdown canónicas."""
from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parents[1]
FUENTES = ROOT / "corpus" / "fuentes"
SALIDA = FUENTES / "SHA256SUMS.txt"

entries = []
for path in sorted(FUENTES.glob("*.md")):
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    entries.append(f"{digest}  corpus/fuentes/{path.name}")
SALIDA.write_text("\n".join(entries) + "\n", encoding="utf-8")
print(f"Sumas SHA-256 recalculadas: {len(entries)} fuentes.")
