#!/usr/bin/env python3
"""Incorpora a corpus/fuentes/ los Markdown registrados subidos a la raíz.

Las obras multipartes expresamente registradas se ensamblan de forma reproducible
antes de ingresar al corpus canónico. Las piezas fuente se retiran de la raíz sólo
cuando el ensamblado se ha escrito o coincide byte a byte con el destino existente.
"""
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

MULTIPART = {
    "Afrodita_Areia_Nikomachos.md": [
        "Nikomachos_prologo.md",
        "Nikomachos_PartI_CapI.md",
        "Nikomachos_PartI_CapII.md",
        "Nikomachos_PartII_CapIII.md",
        "Nikomachos_PartII_CapIV.md",
        "Nikomachos_PartIII_CapV.md",
        "Nikomachos_PartIII_CapVI.md",
        "Nikomachos_PartIV_CapVII.md",
        "Nikomachos_PartIV_CapVIII.md",
        "Nikomachos_PartV_CapIX.md",
        "Nikomachos_PartV_CapX.md",
        "Nikomachos_PartVI_CapXI.md",
        "Nikomachos_PartVI_CapXII.md",
        "Nikomachos_epilogo.md",
    ],
}


def assemble_parts(names: list[str]) -> bytes:
    chunks: list[bytes] = []
    for name in names:
        data = (ROOT / name).read_bytes()
        chunks.append(data)
        if data and not data.endswith(b"\n"):
            chunks.append(b"\n")
    return b"".join(chunks)


moved = 0
for target_name, part_names in MULTIPART.items():
    parts = [ROOT / name for name in part_names]
    present = [part.exists() for part in parts]
    if not any(present):
        continue
    if not all(present):
        missing = [part.name for part, exists in zip(parts, present) if not exists]
        raise RuntimeError(
            f"Fuente multipartes incompleta para {target_name}; faltan: {', '.join(missing)}"
        )

    payload = assemble_parts(part_names)
    target = FUENTES / target_name
    if target.exists() and target.read_bytes() != payload:
        raise RuntimeError(
            f"Conflicto: {target_name} ya existe en corpus/fuentes/ con contenido distinto."
        )
    if not target.exists():
        target.write_bytes(payload)
        moved += 1
        print(f"Fuente multipartes incorporada: {target_name}")
    else:
        print(f"Fuente multipartes ya canónica: {target_name}")

    for part in parts:
        part.unlink()
    print(f"Piezas retiradas de la raíz: {len(parts)}")

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