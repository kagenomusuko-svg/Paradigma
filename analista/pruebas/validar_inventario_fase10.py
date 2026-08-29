#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MOTOR = ROOT / "analista/motores/inventariar_obras_fase10.py"
FUENTES = ROOT / "analista/generado/fuentes.jsonl"
UNIDADES = ROOT / "analista/generado/unidades.jsonl"
PILOTO = "AA-SP-V1"


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def generar(path: Path) -> dict:
    subprocess.run(
        [
            sys.executable,
            str(MOTOR),
            "--fuentes",
            str(FUENTES),
            "--unidades",
            str(UNIDADES),
            "--salida",
            str(path),
        ],
        cwd=ROOT,
        check=True,
    )
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    fuentes = load_jsonl(FUENTES)
    unidades = load_jsonl(UNIDADES)
    assert len(fuentes) == 20, len(fuentes)
    assert len(unidades) == 17573, len(unidades)
    assert len({f["id"] for f in fuentes}) == 20
    assert {u["fuente_id"] for u in unidades} <= {f["id"] for f in fuentes}

    with tempfile.TemporaryDirectory() as td:
        p1 = Path(td) / "inventario-1.json"
        p2 = Path(td) / "inventario-2.json"
        d1 = generar(p1)
        d2 = generar(p2)
        assert p1.read_bytes() == p2.read_bytes(), "El inventario no es reproducible byte a byte"

    assert d1 == d2
    assert d1["version"] == "1.0.0"
    assert d1["fuentes"] == 20
    assert d1["unidades"] == 17573
    assert d1["obras_con_glosario"] == 8
    assert d1["obras_sin_glosario"] == 12
    assert d1["piloto_id"] == PILOTO
    assert len(d1["obras"]) == 20
    assert sum(o["unidades"] for o in d1["obras"]) == 17573
    assert len({o["obra_id"] for o in d1["obras"]}) == 20
    assert sum(o["glosario_tecnico"] is not None for o in d1["obras"]) == 8
    assert sum(o["glosario_tecnico"] is None for o in d1["obras"]) == 12

    pilot = next(o for o in d1["obras"] if o["obra_id"] == PILOTO)
    assert pilot["estado_fase10"] == "piloto_cerrado_fase9"
    assert all(
        o["estado_fase10"] == "pendiente_repeticion_controlada"
        for o in d1["obras"]
        if o["obra_id"] != PILOTO
    )

    agape = next(o for o in d1["obras"] if o["obra_id"] == "FUE-2C28F35DD6CF")
    assert agape["titulo"] == "Afrodita Areia: Ágape"
    assert agape["unidades"] == 643
    assert agape["perfil_conceptual"] == "glosario_tecnico_explicito"
    assert agape["glosario_tecnico"].endswith("99-glosario.md")

    print(
        "OK Fase 10 inventario: 20 obras, 17573 unidades, 8 con glosario y 12 sin glosario; "
        "perímetro reproducible y sin comparación interobra."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
