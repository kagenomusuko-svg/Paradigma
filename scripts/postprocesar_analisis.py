#!/usr/bin/env python3
"""Postprocesa la extracción sin añadir inferencias doctrinales.

Solo mejora:
- formas léxicas explícitas de lemas compuestos del glosario;
- clasificación del motivo por el que una afirmación fue candidata;
- captura contextual de fórmulas multilínea.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import unicodedata
from pathlib import Path

SPACE_RE = re.compile(r"\s+")


def norm(s: str) -> str:
    return SPACE_RE.sub(" ", unicodedata.normalize("NFKC", s).casefold()).strip()


def stable_id(prefix: str, *parts: str) -> str:
    payload = "\x1f".join(parts).encode("utf-8")
    return f"{prefix}-{hashlib.sha1(payload).hexdigest()[:12].upper()}"


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def dump_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text(
        "".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in rows),
        encoding="utf-8",
    )


def lexical_forms(lema: str) -> list[str]:
    forms = [lema.strip()]
    if " — " in lema:
        left, right = [x.strip() for x in lema.split(" — ", 1)]
        # El lado derecho suele ser una formulación alternativa explícita del lema.
        if right:
            forms.append(right)
        # Añadir el lado izquierdo solo si es suficientemente específico.
        # Evita que "Pasión — dimensión afrodítica" herede todas las menciones de "Pasión".
        if left and (len(left.split()) > 1 or re.search(r"[φ₁₂₃₄₅₆₇₈₉₀()\d]", left)):
            forms.append(left)
    # Preservar orden y eliminar duplicados normalizados.
    out = []
    seen = set()
    for f in forms:
        key = norm(f)
        if key and key not in seen:
            seen.add(key)
            out.append(f)
    return out


def classify_candidate(markers: list[str]) -> tuple[str, float]:
    ms = set(markers)
    if "la tesis central" in ms or "la tesis de este capítulo es" in ms:
        return "tesis_explicita_candidata", 0.95
    if "se define como" in ms or "la definición" in ms:
        return "definicion_candidata", 0.85
    if "este sistema rechaza" in ms:
        return "negacion_o_distincion_candidata", 0.80
    if "la posición de este libro es" in ms:
        return "posicion_explicita_candidata", 0.90
    return "tesis_o_relacion_candidata", 0.75


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--dir", required=True)
    args = p.parse_args()
    root = Path(args.dir)

    units = load_jsonl(root / "unidades.jsonl")
    concepts = json.loads((root / "conceptos.json").read_text(encoding="utf-8"))
    assertions = load_jsonl(root / "afirmaciones-candidatas.jsonl")
    report = json.loads((root / "reporte.json").read_text(encoding="utf-8"))

    paragraphs = [u for u in units if u.get("tipo") == "parrafo"]

    # Huella literal de cada unidad para distinguir identidad del texto de su ubicación editorial.
    for u in units:
        u["sha256_texto"] = hashlib.sha256(u["texto"].encode("utf-8")).hexdigest()
    dump_jsonl(root / "unidades.jsonl", units)

    # Índice conceptual por formas léxicas explícitas del propio lema.
    for c in concepts:
        forms = lexical_forms(c["lema"])
        c["formas_busqueda"] = forms
        appearances = []
        for u in paragraphs:
            text_n = norm(u["texto"])
            matched = [f for f in forms if norm(f) in text_n]
            if matched:
                appearances.append(
                    {
                        "unidad_id": u["id"],
                        "ruta": u["ruta"],
                        "linea_inicio": u["linea_inicio"],
                        "linea_fin": u["linea_fin"],
                        "formas_detectadas": matched,
                    }
                )
        c["apariciones"] = appearances
    (root / "conceptos.json").write_text(
        json.dumps(concepts, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    # Explicar el motivo de la candidatura, sin promoverla a tesis/definición revisada.
    for a in assertions:
        function, confidence = classify_candidate(a.get("marcadores", []))
        a["funcion_discursiva_candidata"] = function
        a["confianza_extraccion"] = confidence
    dump_jsonl(root / "afirmaciones-candidatas.jsonl", assertions)

    # Fórmulas: una candidatura por unidad textual, preservando el contexto completo.
    formulas = []
    for u in paragraphs:
        if "=" not in u["texto"]:
            continue
        linear = SPACE_RE.sub(" ", u["texto"]).strip()
        if len(linear) > 2500:
            continue
        formulas.append(
            {
                "id": stable_id("FOR", u["id"], linear),
                "tipo_registro": "formula_candidata",
                "verificacion": "pendiente",
                "fuente_id": report["fuente_id"],
                "unidad_id": u["id"],
                "ruta": u["ruta"],
                "linea_inicio": u["linea_inicio"],
                "linea_fin": u["linea_fin"],
                "texto_literal": u["texto"],
                "texto_lineal": linear,
                "interpretacion": None,
            }
        )
    dump_jsonl(root / "formulas-candidatas.jsonl", formulas)

    report["formulas_candidatas"] = len(formulas)
    report["postproceso"] = "0.1.0"
    (root / "reporte.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print(
        f"Postproceso: {len(concepts)} conceptos reindexados, "
        f"{len(assertions)} candidatos clasificados, {len(formulas)} fórmulas contextuales."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
