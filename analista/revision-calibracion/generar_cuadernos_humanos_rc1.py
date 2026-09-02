#!/usr/bin/env python3
"""Genera cuadernos Markdown legibles desde el expediente técnico RC-1.

No modifica, reclasifica ni interpreta registros. Reduce únicamente la presentación
para que la auditoría humana pueda hacerse por lotes pequeños y temáticos.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Iterable

CATEGORIAS = [
    "correcto",
    "truncado_inicio",
    "truncado_final",
    "fragmentacion_indebida",
    "fusion_indebida",
    "tipo_registro_incorrecto",
    "estatus_enunciativo_incorrecto",
    "concepto_no_establecido_por_la_evidencia",
    "evidencia_insuficiente",
    "referencia_incorrecta",
    "trazabilidad_incorrecta",
    "corrupcion_conversion",
    "formula_incompleta",
    "duplicado_indebido",
    "otro_error_documental",
    "no_determinado",
]


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def esc(text: Any) -> str:
    if text is None:
        return "—"
    return str(text).replace("```", "` ` `")


def first(*vals: Any) -> Any:
    for v in vals:
        if v not in (None, "", [], {}):
            return v
    return None


def focused_context(row: dict[str, Any], max_lines: int = 10) -> str:
    ctx = row.get("contexto_fuente") or {}
    numbered = ctx.get("contexto_numerado")
    if not isinstance(numbered, str) or not numbered.strip():
        return esc(ctx.get("fragmento_rango") or "Contexto no disponible")
    lines = numbered.splitlines()
    flags = set(row.get("senales_diagnosticas") or [])
    if "contiene_cid" in flags or "formula_con_glifo_no_mapeado" in flags:
        hit = next((i for i, line in enumerate(lines) if "(cid:" in line or "\x00" in line), None)
        if hit is not None:
            lo = max(0, hit - 2)
            hi = min(len(lines), hit + 3)
            return "\n".join(lines[lo:hi])
    loc = ctx.get("localizacion") or {}
    start = loc.get("linea_inicio")
    end = loc.get("linea_fin")
    if isinstance(start, int):
        selected = []
        for line in lines:
            try:
                n = int(line.split(":", 1)[0])
            except Exception:
                continue
            if start - 2 <= n <= (end or start) + 2:
                selected.append(line)
        if selected:
            if len(selected) > max_lines:
                return "\n".join(selected[:max_lines]) + "\n… [contexto abreviado]"
            return "\n".join(selected)
    if len(lines) > max_lines:
        return "\n".join(lines[:max_lines]) + "\n… [contexto abreviado]"
    return "\n".join(lines)


def case_md(n: int, row: dict[str, Any]) -> str:
    reg = row.get("registro") or {}
    ctx = row.get("contexto_fuente") or {}
    loc = ctx.get("localizacion") or reg.get("localizacion") or {}
    produced = reg.get("producido_por") or {}
    classification = first(
        reg.get("clasificacion_definicion"),
        reg.get("clasificacion_afirmacion"),
        reg.get("clasificacion_relacion"),
        reg.get("estado_identidad_conceptual"),
        reg.get("tipo_registro"),
        row.get("seccion_maestro"),
    )
    literal = first(
        reg.get("texto_literal"),
        reg.get("formula_literal"),
        reg.get("forma_literal"),
        reg.get("designacion_operativa"),
    )
    flags = ", ".join(row.get("senales_diagnosticas") or []) or "sin señal automática"
    route = loc.get("ruta") or "—"
    span = f"{loc.get('linea_inicio', '?')}–{loc.get('linea_fin', loc.get('linea_inicio', '?'))}"
    criteria = first(reg.get("criterio_deteccion"), reg.get("criterio_identidad"), "—")
    status = reg.get("estatus_enunciativo")
    context = focused_context(row)
    decisions = "\n".join(f"- [ ] `{c}`" for c in CATEGORIAS)
    return f"""## Caso {n:02d} · `{esc(reg.get('id'))}`

**Qué produjo el motor**

- Tipo/sección: `{esc(row.get('seccion_maestro'))}`
- Clasificación: `{esc(classification)}`
- Criterio: `{esc(criteria)}`
- Estatus enunciativo: `{esc(status)}`
- Motor: `{esc(produced.get('motor'))}` v`{esc(produced.get('version'))}`
- Señal de revisión: `{esc(flags)}`

**Salida del motor**

> {esc(literal).replace(chr(10), chr(10) + '> ')}

**Dónde mirar**

`{esc(route)}` · líneas `{span}`

**Fuente alrededor del caso**

```text
{esc(context)}
```

**Nuestra decisión documental**

{decisions}

Comentario breve: _pendiente_

---
"""


def take(rows: Iterable[dict[str, Any]], section: str | None = None, signal: str | None = None, limit: int = 12) -> list[dict[str, Any]]:
    out = []
    for row in rows:
        if section and row.get("seccion_maestro") != section:
            continue
        if signal and signal not in (row.get("senales_diagnosticas") or []):
            continue
        out.append(row)
        if len(out) >= limit:
            break
    return out


def write_book(path: Path, title: str, purpose: str, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    head = f"""# {title}

{purpose}

Este cuaderno es una **vista humana** del expediente RC-1. El JSONL técnico sigue siendo la evidencia completa; aquí solo se reduce presentación. Ninguna señal automática constituye por sí misma un error confirmado.

Casos en este lote: **{len(rows)}**.

---

"""
    body = "".join(case_md(i, row) for i, row in enumerate(rows, 1))
    path.write_text(head + body, encoding="utf-8")


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--expediente", type=Path, required=True)
    p.add_argument("--salida-dir", type=Path, required=True)
    p.add_argument("--tamano-lote", type=int, default=12)
    args = p.parse_args()
    rows = read_jsonl(args.expediente)
    n = args.tamano_lote

    books = [
        (
            "01-definiciones-posible-truncamiento.md",
            "RC-1 · Definiciones con posible truncamiento",
            "Primera lectura recomendada. Revisamos si la salida definicional corta una continuidad textual visible.",
            take(rows, section="definiciones", signal="final_sin_puntuacion_terminal", limit=n),
        ),
        (
            "02-afirmaciones-estatus.md",
            "RC-1 · Afirmaciones y estatus enunciativo",
            "Revisamos preguntas, citas, condicionales u otras formas que no deben ascender automáticamente a tesis autoral.",
            take(rows, section="afirmaciones", signal="estatus_no_determinado", limit=n),
        ),
        (
            "03-conceptos-control.md",
            "RC-1 · Conceptos: controles de identidad",
            "Muestra de conceptos para comprobar si el motor conserva correctamente candidatos y grados de identidad sin exigir interpretación autoral.",
            take(rows, section="conceptos", limit=n),
        ),
        (
            "04-cid-y-formulas.md",
            "RC-1 · Conversión, CID y fórmulas",
            "Muestra focalizada en glifos no resueltos. El contexto se reduce a las líneas cercanas al artefacto para no obligar a leer unidades completas.",
            [r for r in rows if "contiene_cid" in (r.get("senales_diagnosticas") or [])][:n],
        ),
        (
            "05-excepciones-y-restricciones.md",
            "RC-1 · Excepciones y restricciones",
            "Muestra pequeña para comprobar si el marcador textual realmente sustenta la categoría y su alcance.",
            (take(rows, section="excepciones", limit=max(1, n // 2)) + take(rows, section="restricciones_alcance", limit=max(1, n // 2)))[:n],
        ),
    ]

    index = [
        "# RC-1 · Cuadernos de auditoría humana\n",
        "Lee estos archivos, no el JSONL técnico. Empieza por **01-definiciones-posible-truncamiento.md**.\n",
        "Cada cuaderno contiene lotes pequeños, salida del motor, ubicación exacta, contexto abreviado y categorías posibles de decisión.\n",
    ]
    for filename, title, purpose, selected in books:
        write_book(args.salida_dir / filename, title, purpose, selected)
        index.append(f"- [{title}]({filename}) — {len(selected)} casos")
    (args.salida_dir / "README.md").write_text("\n".join(index) + "\n", encoding="utf-8")
    print(json.dumps({"cuadernos": len(books), "salida": str(args.salida_dir)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
