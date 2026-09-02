#!/usr/bin/env python3
"""Valida la integridad estructural y las invariantes ya ganadas por el mapa.

No decide doctrina. Comprueba referencias, proveniencia, rutas y que las
pruebas de F1 no puedan degradarse silenciosamente durante F2–F5.
"""
from __future__ import annotations
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
MAP_PATH = ROOT / "mapa" / "mapa-maestro.json"
SCHEMA_PATH = ROOT / "mapa" / "esquema-f1.schema.json"

class ValidationError(Exception):
    pass

def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)

def index_unique(items: list[dict], label: str) -> dict[str, dict]:
    result = {}
    for item in items:
        item_id = item.get("id")
        require(isinstance(item_id, str) and item_id, f"{label}: elemento sin id válido")
        require(item_id not in result, f"{label}: id duplicado {item_id}")
        result[item_id] = item
    return result

def main() -> int:
    require(MAP_PATH.exists(), f"No existe {MAP_PATH.relative_to(ROOT)}")
    require(SCHEMA_PATH.exists(), f"No existe {SCHEMA_PATH.relative_to(ROOT)}")
    data = json.loads(MAP_PATH.read_text(encoding="utf-8"))
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    for key in schema["required"]:
        require(key in data, f"Falta clave superior obligatoria: {key}")

    phase = data.get("phase")
    schema_status = data.get("schema_status")
    require(phase in {"F1", "F2", "F3", "F4", "F5", "MANT"}, f"Fase inválida: {phase}")
    if phase == "F1":
        require(schema_status == "draft", "Durante F1 el esquema debe seguir en draft")
    else:
        require(schema_status == "frozen", "Después de F1 el esquema v1 debe permanecer frozen")

    works = index_unique(data["works"], "works")
    evidence = index_unique(data["evidence"], "evidence")
    nodes = index_unique(data["nodes"], "nodes")
    relations = index_unique(data["relations"], "relations")
    routes = index_unique(data["routes"], "routes")
    reviews = index_unique(data["review_queue"], "review_queue")
    tests = index_unique(data["tests"], "tests")

    for work in works.values():
        sha = work.get("sha256", "")
        require(len(sha) == 64 and all(c in "0123456789abcdef" for c in sha), f"Hash SHA-256 inválido en {work['id']}")
        require(str(work.get("source", "")).startswith("corpus/fuentes/"), f"Fuente no canónica en {work['id']}")

    for ev in evidence.values():
        require(ev["work_id"] in works, f"{ev['id']}: work_id inexistente {ev['work_id']}")
        require(str(ev["segment"]).startswith("corpus/libros/"), f"{ev['id']}: segment no apunta a corpus/libros/")
        lines = ev.get("source_lines")
        require(isinstance(lines, list) and len(lines) == 2, f"{ev['id']}: source_lines debe ser [inicio, fin]")
        require(all(isinstance(n, int) and n > 0 for n in lines) and lines[0] <= lines[1], f"{ev['id']}: rango de líneas inválido")

    valid_status = {"explicit", "inferred", "editorial"}
    for node in nodes.values():
        for ev_id in node.get("evidence", []):
            require(ev_id in evidence, f"{node['id']}: evidencia inexistente {ev_id}")
        if "evidence_status" in node:
            require(node["evidence_status"] in valid_status, f"{node['id']}: evidence_status inválido")
            if node["evidence_status"] == "explicit":
                require(bool(node.get("evidence")), f"{node['id']}: nodo explícito sin evidencia")
        if node.get("subject") is not None:
            require(node["subject"] in nodes, f"{node['id']}: subject inexistente {node['subject']}")

    for rel in relations.values():
        require(rel["from"] in nodes, f"{rel['id']}: from inexistente {rel['from']}")
        require(rel["to"] in nodes, f"{rel['id']}: to inexistente {rel['to']}")
        require(rel["evidence_status"] in valid_status, f"{rel['id']}: evidence_status inválido")
        for ev_id in rel.get("evidence", []):
            require(ev_id in evidence, f"{rel['id']}: evidencia inexistente {ev_id}")
        if rel["evidence_status"] == "explicit":
            require(bool(rel.get("evidence")), f"{rel['id']}: relación explícita sin evidencia")
        if rel["evidence_status"] == "inferred":
            require(bool(rel.get("rationale")), f"{rel['id']}: relación inferida sin rationale")

    for route in routes.values():
        require(bool(route.get("steps")), f"{route['id']}: ruta sin pasos")
        orders = []
        for step in route["steps"]:
            require(step["evidence_id"] in evidence, f"{route['id']}: evidencia inexistente {step['evidence_id']}")
            orders.append(step["order"])
        require(orders == sorted(orders) and len(orders) == len(set(orders)), f"{route['id']}: orden de pasos inválido")
        for review_id in route.get("must_surface_review_items", []):
            require(review_id in reviews, f"{route['id']}: review inexistente {review_id}")

    for review in reviews.values():
        require(review["subject"] in nodes, f"{review['id']}: subject inexistente {review['subject']}")
        if review.get("related_relation"):
            require(review["related_relation"] in relations, f"{review['id']}: relation inexistente {review['related_relation']}")
        for ev_id in review.get("evidence", []):
            require(ev_id in evidence, f"{review['id']}: evidencia inexistente {ev_id}")

    stress_cases = {test["stress_case"] for test in tests.values()}
    require(stress_cases == {"formula_del_ego", "rstar", "aego"}, f"Deben conservarse los tres casos de estrés F1; encontrados: {sorted(stress_cases)}")
    for test in tests.values():
        for route_id in test["required_routes"]:
            require(route_id in routes, f"{test['id']}: ruta requerida inexistente {route_id}")
        if phase != "F1":
            require(str(test.get("status", "")).startswith("pass"), f"{test['id']}: F1 no puede cerrarse sin resultado aprobatorio")

    # Invariantes ganadas durante F1.
    require("formulation.ego.caos" in nodes and "formulation.ego.bis.tf" in nodes, "Caso ego incompleto")
    require("term.caos.mediacion_prima_material" in nodes, "Debe conservarse el uso terminológico material de Caos como nodo separado")
    require("primera mediación en sentido material (Caos)" not in nodes["concept.primera_mediacion"].get("aliases", []), "No fusionar la mediación material/neutral con primera mediación/φ₁")
    require("rel.caos.material_to_neutral" in relations, "Falta correspondencia material de Caos → mediación neutral")

    require("formal.rstar" in nodes and "formal.W" in nodes and "formal.G" in nodes, "Caso R* incompleto")
    require("ev.mci.rstar_validity" in evidence, "R* debe conservar su ruta metrológica de validez")
    require("review.rstar.sink_irreducibility" in reviews, "La tensión formal de R* debe permanecer visible hasta su resolución")
    require("review.rstar.sink_irreducibility" in routes["route.rstar.definicion_calculo"].get("must_surface_review_items", []), "La ruta de R* debe surfacer su revisión formal")

    require("formulation.aego.aa1" in nodes and "formulation.aego.aa3" in nodes and "formulation.aego.sdo" in nodes, "Caso Aego incompleto")
    require(any(r["evidence_status"] == "inferred" and r["id"] == "rel.aego.aa3_refines_aa1" for r in relations.values()), "La relación entre formulaciones de Aego debe seguir marcada como inferida")
    require("review.aego.formulation_change" in reviews, "La diferencia doctrinal de Aego debe quedar en cola de adjudicación")
    require("review.aego.formulation_change" in routes["route.aego.definicion_evolucion"].get("must_surface_review_items", []), "La ruta de Aego debe surfacer la adjudicación pendiente")

    print(
        "Mapa válido:",
        f"fase={phase}, schema={schema_status};",
        f"{len(works)} obras,",
        f"{len(evidence)} evidencias,",
        f"{len(nodes)} nodos,",
        f"{len(relations)} relaciones,",
        f"{len(routes)} rutas,",
        f"{len(reviews)} revisiones pendientes,",
        f"{len(tests)} pruebas F1 preservadas."
    )
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValidationError, json.JSONDecodeError, KeyError, TypeError) as exc:
        print(f"ERROR DE VALIDACIÓN: {exc}", file=sys.stderr)
        raise SystemExit(1)
