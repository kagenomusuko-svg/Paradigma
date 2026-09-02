#!/usr/bin/env python3
"""Valida la integridad referencial mínima del mapa maestro de Paradigma.

No interpreta doctrina. Comprueba que el JSON puede funcionar como mapa:
IDs únicos, proveniencia resoluble, relaciones trazables, rutas válidas y
presencia de los tres casos de estrés de F1.
"""
from __future__ import annotations
import json
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
MAP_PATH = ROOT / "mapa" / "mapa-maestro.json"
SCHEMA_PATH = ROOT / "mapa" / "esquema-f1.schema.json"
class ValidationError(Exception): pass
def require(condition: bool, message: str) -> None:
    if not condition: raise ValidationError(message)
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
    for key in schema["required"]: require(key in data, f"Falta clave superior obligatoria: {key}")
    require(data["phase"] == "F1", "Durante la prueba actual el mapa debe declarar phase=F1")
    require(data["schema_status"] == "draft", "El esquema no puede congelarse antes de superar F1")
    works = index_unique(data["works"], "works"); evidence = index_unique(data["evidence"], "evidence")
    nodes = index_unique(data["nodes"], "nodes"); relations = index_unique(data["relations"], "relations")
    routes = index_unique(data["routes"], "routes"); reviews = index_unique(data["review_queue"], "review_queue")
    tests = index_unique(data["tests"], "tests")
    for work in works.values():
        sha = work.get("sha256", "")
        require(len(sha) == 64 and all(c in "0123456789abcdef" for c in sha), f"Hash SHA-256 inválido en {work['id']}")
        require(str(work.get("source", "")).startswith("corpus/fuentes/"), f"Fuente no canónica en {work['id']}")
    for ev in evidence.values():
        require(ev["work_id"] in works, f"{ev['id']}: work_id inexistente {ev['work_id']}")
        require(str(ev["segment"]).startswith("corpus/libros/"), f"{ev['id']}: segment no apunta a corpus/libros/")
        lines = ev.get("source_lines"); require(isinstance(lines, list) and len(lines) == 2, f"{ev['id']}: source_lines debe ser [inicio, fin]")
        require(all(isinstance(n, int) and n > 0 for n in lines) and lines[0] <= lines[1], f"{ev['id']}: rango de líneas inválido")
    valid_status = {"explicit", "inferred", "editorial"}
    for node in nodes.values():
        for ev_id in node.get("evidence", []): require(ev_id in evidence, f"{node['id']}: evidencia inexistente {ev_id}")
        if "evidence_status" in node:
            require(node["evidence_status"] in valid_status, f"{node['id']}: evidence_status inválido")
            if node["evidence_status"] == "explicit": require(bool(node.get("evidence")), f"{node['id']}: nodo explícito sin evidencia")
        if node.get("subject") is not None: require(node["subject"] in nodes, f"{node['id']}: subject inexistente {node['subject']}")
    for rel in relations.values():
        require(rel["from"] in nodes, f"{rel['id']}: from inexistente {rel['from']}")
        require(rel["to"] in nodes, f"{rel['id']}: to inexistente {rel['to']}")
        require(rel["evidence_status"] in valid_status, f"{rel['id']}: evidence_status inválido")
        for ev_id in rel.get("evidence", []): require(ev_id in evidence, f"{rel['id']}: evidencia inexistente {ev_id}")
        if rel["evidence_status"] == "explicit": require(bool(rel.get("evidence")), f"{rel['id']}: relación explícita sin evidencia")
        if rel["evidence_status"] == "inferred": require(bool(rel.get("rationale")), f"{rel['id']}: relación inferida sin rationale")
    for route in routes.values():
        require(bool(route.get("steps")), f"{route['id']}: ruta sin pasos"); orders = []
        for step in route["steps"]:
            require(step["evidence_id"] in evidence, f"{route['id']}: evidencia inexistente {step['evidence_id']}"); orders.append(step["order"])
        require(orders == sorted(orders) and len(orders) == len(set(orders)), f"{route['id']}: orden de pasos inválido")
        for review_id in route.get("must_surface_review_items", []): require(review_id in reviews, f"{route['id']}: review inexistente {review_id}")
    for review in reviews.values():
        require(review["subject"] in nodes, f"{review['id']}: subject inexistente {review['subject']}")
        if review.get("related_relation"): require(review["related_relation"] in relations, f"{review['id']}: relation inexistente {review['related_relation']}")
    stress_cases = {test["stress_case"] for test in tests.values()}
    require(stress_cases == {"formula_del_ego", "rstar", "aego"}, f"F1 debe contener exactamente los tres casos de estrés; encontrados: {sorted(stress_cases)}")
    for test in tests.values():
        for route_id in test["required_routes"]: require(route_id in routes, f"{test['id']}: ruta requerida inexistente {route_id}")
    require("formulation.ego.caos" in nodes and "formulation.ego.bis.tf" in nodes, "Caso ego incompleto")
    require("formal.rstar" in nodes and "formal.W" in nodes and "formal.G" in nodes, "Caso R* incompleto")
    require("formulation.aego.aa1" in nodes and "formulation.aego.aa3" in nodes and "formulation.aego.sdo" in nodes, "Caso Aego incompleto")
    require(any(r["evidence_status"] == "inferred" and r["id"] == "rel.aego.aa3_refines_aa1" for r in relations.values()), "La diferencia doctrinal de Aego debe permanecer marcada como inferida")
    require("review.aego.formulation_change" in reviews, "La diferencia doctrinal de Aego debe quedar en cola de adjudicación")
    print("Mapa F1 válido:", f"{len(works)} obras,", f"{len(evidence)} evidencias,", f"{len(nodes)} nodos,", f"{len(relations)} relaciones,", f"{len(routes)} rutas,", f"{len(reviews)} revisiones pendientes,", f"{len(tests)} casos de prueba.")
    return 0
if __name__ == "__main__":
    try: raise SystemExit(main())
    except (ValidationError, json.JSONDecodeError, KeyError, TypeError) as exc:
        print(f"ERROR DE VALIDACIÓN: {exc}", file=sys.stderr); raise SystemExit(1)
