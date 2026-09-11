#!/usr/bin/env python3
"""Mueve a corpus/fuentes/ los Markdown registrados que hayan sido subidos a la raíz."""
from pathlib import Path
from segmentar_corpus import SPECS as BASE_SPECS
from segmentar_lote_02 import SPECS as LOTE_02_SPECS
from segmentar_lote_03 import SPECS as LOTE_03_SPECS

ROOT = Path(__file__).resolve().parents[1]
FUENTES = ROOT / "corpus" / "fuentes"
FUENTES.mkdir(parents=True, exist_ok=True)
REGISTERED = (
    {spec["source"] for spec in BASE_SPECS}
    | {spec["source"] for spec in LOTE_02_SPECS}
    | {spec["source"] for spec in LOTE_03_SPECS}
)

moved = 0
for name in sorted(REGISTERED):
    source = ROOT / name
    if not source.exists():
        continue
    target = FUENTES / name
    if target.exists():
        if source.read_bytes() != target.read_bytes():
            raise RuntimeError(f"Conflicto: {name} ya existe en corpus/fuentes/ con contenido distinto.")
        source.unlink()
        print(f"Duplicado idéntico retirado de la raíz: {name}")
        continue
    source.replace(target)
    moved += 1
    print(f"Fuente incorporada: {name}")

print(f"Fuentes nuevas movidas: {moved}")
