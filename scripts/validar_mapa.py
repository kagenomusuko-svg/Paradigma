#!/usr/bin/env python3
"""Valida la integridad estructural y las invariantes ya ganadas por el mapa.

No decide doctrina. Comprueba referencias, proveniencia, rutas y que las
pruebas de F1 y la cobertura incorporada en F2 no puedan degradarse
silenciosamente durante las fases posteriores.
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

    # Invariantes ganadas al integrar Caos sistemáticamente en F2.
    if phase != "F1":
        chaos_structure_path = ROOT / "corpus" / "libros" / "caos" / "estructura.json"
        require(chaos_structure_path.exists(), "Falta la estructura derivada de Caos")
        chaos_structure = json.loads(chaos_structure_path.read_text(encoding="utf-8"))
        chaos_segments = {
            segment["path"]: (segment["start_line"], segment["end_line"])
            for segment in chaos_structure["segments"]
        }
        chaos_evidence = [ev for ev in evidence.values() if ev["work_id"] == "CAOS"]
        covered_segments = {ev["segment"] for ev in chaos_evidence}
        require(
            set(chaos_segments) <= covered_segments,
            f"La auditoría de Caos debe cubrir preliminares, siete capítulos y tres apéndices; faltan: {sorted(set(chaos_segments) - covered_segments)}",
        )
        for ev in chaos_evidence:
            require(ev["segment"] in chaos_segments, f"{ev['id']}: segmento de Caos no declarado en estructura.json")
            segment_start, segment_end = chaos_segments[ev["segment"]]
            line_start, line_end = ev["source_lines"]
            require(
                segment_start <= line_start <= line_end <= segment_end,
                f"{ev['id']}: rango fuera del segmento declarado {ev['segment']}",
            )

        required_chaos_nodes = {
            "concept.sujeto",
            "concept.caos",
            "concept.colapso",
            "concept.mediacion",
            "concept.doble_mediacion",
            "concept.acto",
            "concept.integral_acumulativa",
            "concept.campo_accion",
            "concept.escala_colapso",
            "concept.accidente",
            "concept.tiempo_ego",
            "concept.imputacion",
            "concept.responsabilidad_ontologica",
            "formal.phi1.caos",
            "formal.phi2.caos",
            "formal.I.caos",
            "formal.ego.caos",
            "formulation.quantum_correspondence.caos",
        }
        require(
            required_chaos_nodes <= set(nodes),
            f"Núcleo de Caos incompleto; faltan nodos: {sorted(required_chaos_nodes - set(nodes))}",
        )

        required_chaos_routes = {
            "route.caos.architecture",
            "route.caos.subject_ego_identity",
            "route.caos.chaos_collapse",
            "route.caos.time_other_freedom",
            "route.caos.scales_accident_field",
            "route.caos.mediations",
            "route.caos.responsibility_imputation",
            "route.caos.god_conditional",
            "route.caos.formalization",
            "route.caos.quantum_correspondence",
        }
        require(
            required_chaos_routes <= set(routes),
            f"Rutas de Caos incompletas: {sorted(required_chaos_routes - set(routes))}",
        )

        chaos_formal_reviews = {
            "review.caos.formal_typing",
            "review.caos.accumulation_topology",
            "review.caos.local_derivative",
        }
        chaos_quantum_reviews = {
            "review.caos.quantum_isomorphism",
            "review.caos.quantum_interpretations",
        }
        require(chaos_formal_reviews <= set(reviews), "Deben conservarse las revisiones matemáticas pendientes de Caos")
        require(chaos_quantum_reviews <= set(reviews), "Deben conservarse las revisiones cuánticas pendientes de Caos")
        require(
            chaos_formal_reviews <= set(routes["route.caos.formalization"].get("must_surface_review_items", [])),
            "La ruta matemática de Caos debe surfacer todas sus revisiones formales",
        )
        require(
            chaos_quantum_reviews <= set(routes["route.caos.quantum_correspondence"].get("must_surface_review_items", [])),
            "La ruta cuántica de Caos debe surfacer sus revisiones de estatuto y consistencia",
        )

        # Invariantes ganadas al integrar Afrodita Areia I sistemáticamente en F2.
        aa1_structure_path = (
            ROOT
            / "corpus"
            / "libros"
            / "afrodita-areia"
            / "01-sobre-la-pasion"
            / "estructura.json"
        )
        require(aa1_structure_path.exists(), "Falta la estructura derivada de Afrodita Areia I")
        aa1_structure = json.loads(aa1_structure_path.read_text(encoding="utf-8"))
        aa1_segments = {
            segment["path"]: (segment["start_line"], segment["end_line"])
            for segment in aa1_structure["segments"]
        }
        aa1_evidence = [ev for ev in evidence.values() if ev["work_id"] == "AA-I"]
        aa1_covered_segments = {ev["segment"] for ev in aa1_evidence}
        require(
            set(aa1_segments) <= aa1_covered_segments,
            "La auditoría de Afrodita Areia I debe cubrir preliminares, prefacio, "
            "prólogo, dieciséis capítulos, tres apéndices y glosario; faltan: "
            f"{sorted(set(aa1_segments) - aa1_covered_segments)}",
        )
        require(
            len(aa1_evidence) >= 42,
            f"La auditoría semántica de Afrodita Areia I perdió granularidad: {len(aa1_evidence)} evidencias",
        )
        for ev in aa1_evidence:
            require(ev["segment"] in aa1_segments, f"{ev['id']}: segmento de AA-I no declarado en estructura.json")
            segment_start, segment_end = aa1_segments[ev["segment"]]
            line_start, line_end = ev["source_lines"]
            require(
                segment_start <= line_start <= line_end <= segment_end,
                f"{ev['id']}: rango fuera del segmento declarado {ev['segment']}",
            )

        required_aa1_nodes = {
            "concept.pasion_ontologica",
            "concept.tendencia_material",
            "concept.orden_emergente",
            "concept.afrodita_dominio",
            "concept.ares_conquista",
            "concept.mediacion_neutral",
            "concept.mediacion_fanes",
            "concept.mediacion_bis",
            "concept.identidad_sesgo.aa1",
            "concept.accidente_identidad.aa1",
            "concept.ego_primordial",
            "concept.asuncion_causal.aa1",
            "concept.posibilidades_negadas",
            "concept.disforia_identidad",
            "concept.disociacion_ego",
            "concept.razon_tardia",
            "concept.afasia_volitiva",
            "concept.singularidad_ontologica.aa1",
            "concept.aego_anterioridad",
            "concept.soberania_ego.aa1",
            "concept.suicidio_aego.aa1",
            "formulation.passion.aa1",
            "formulation.three_stages.aa1",
            "formulation.identity.aa1",
            "formulation.fanes.aa1",
            "formulation.bis.aa1",
            "formulation.responsibility.aa1",
            "formulation.cogito_inversion.aa1",
            "formulation.denied_possibilities.aa1",
            "formulation.zagreo.aa1",
            "formulation.narcissus.aa1",
            "formal.neutral.aa1",
            "formal.fanes.aa1",
            "formal.bis.aa1",
            "formal.aego.limit.aa1",
        }
        require(
            required_aa1_nodes <= set(nodes),
            f"Núcleo de Afrodita Areia I incompleto; faltan nodos: {sorted(required_aa1_nodes - set(nodes))}",
        )

        required_aa1_routes = {
            "route.aa1.architecture_method",
            "route.aa1.chaos_causality_order",
            "route.aa1.passion_definition_levels",
            "route.aa1.afrodita_ares_other",
            "route.aa1.three_mediations",
            "route.aa1.identity_distortions",
            "route.aa1.responsibility_assumption",
            "route.aa1.ego_trajectory_possibilities",
            "route.aa1.cogito_reason",
            "route.aa1.zagreo_sovereignty",
            "route.aa1.narcissus_suicide",
            "route.aa1.aego_limit_cases",
            "route.aa1.open_questions_downstream",
        }
        require(
            required_aa1_routes <= set(routes),
            f"Rutas de Afrodita Areia I incompletas: {sorted(required_aa1_routes - set(routes))}",
        )

        aa1_reviews = {
            "review.aa1.caos_crosswalk",
            "review.aa1.responsibility_grounding",
            "review.aa1.neutral_habits",
            "review.aa1.identity_change",
            "review.aa1.aego_zero_indeterminate",
            "review.aa1.aego_operator_agency",
        }
        require(aa1_reviews <= set(reviews), "Deben conservarse las seis revisiones pendientes de Afrodita Areia I")
        require(
            {"review.aa1.caos_crosswalk", "review.aa1.neutral_habits"}
            <= set(routes["route.aa1.three_mediations"].get("must_surface_review_items", [])),
            "La ruta de mediaciones de AA-I debe surfacer atribución terminológica y hábitos",
        )
        require(
            {"review.aa1.responsibility_grounding", "review.aa1.neutral_habits"}
            <= set(routes["route.aa1.responsibility_assumption"].get("must_surface_review_items", [])),
            "La ruta de responsabilidad de AA-I debe surfacer sus dos adjudicaciones",
        )
        require(
            "review.aa1.identity_change"
            in routes["route.aa1.identity_distortions"].get("must_surface_review_items", []),
            "La ruta de identidad de AA-I debe surfacer el cambio de uso respecto de Caos",
        )
        require(
            {"review.aa1.aego_zero_indeterminate", "review.aa1.aego_operator_agency"}
            <= set(routes["route.aa1.aego_limit_cases"].get("must_surface_review_items", [])),
            "La ruta de casos límite de Aego debe surfacer sus revisiones formal y de agencia",
        )
        require(
            relations["rel.responsibility_aa1.differs_caos_grounding"]["evidence_status"] == "inferred",
            "La diferencia de fundamento de responsabilidad AA-I/Caos no puede presentarse como adjudicación autoral",
        )
        require(
            relations["rel.identity_aa1.distinguished_caos_identity"]["evidence_status"] == "inferred",
            "La diferencia entre identidad-sesgo e identidad-continuidad debe seguir marcada como inferida",
        )
        require(
            "atribuida retrospectivamente a Caos" in nodes["term.caos.mediacion_prima_material"]["label"],
            "La terminología material no puede presentarse como vocabulario literal de Caos",
        )

        # Invariantes ganadas al integrar Afrodita Areia II sistemáticamente en F2.
        aa2_structure_path = (
            ROOT
            / "corpus"
            / "libros"
            / "afrodita-areia"
            / "02-agape"
            / "estructura.json"
        )
        require(aa2_structure_path.exists(), "Falta la estructura derivada de Afrodita Areia II")
        aa2_structure = json.loads(aa2_structure_path.read_text(encoding="utf-8"))
        aa2_segments = {
            segment["path"]: (segment["start_line"], segment["end_line"])
            for segment in aa2_structure["segments"]
        }
        aa2_evidence = [ev for ev in evidence.values() if ev["work_id"] == "AA-II"]
        aa2_covered_segments = {ev["segment"] for ev in aa2_evidence}
        require(
            set(aa2_segments) <= aa2_covered_segments,
            "La auditoría de Afrodita Areia II debe cubrir preliminares, prefacio, "
            "prólogo, quince capítulos, apéndice y glosario; faltan: "
            f"{sorted(set(aa2_segments) - aa2_covered_segments)}",
        )
        require(
            len(aa2_evidence) >= 35,
            f"La auditoría semántica de Afrodita Areia II perdió granularidad: {len(aa2_evidence)} evidencias",
        )
        for ev in aa2_evidence:
            require(ev["segment"] in aa2_segments, f"{ev['id']}: segmento de AA-II no declarado en estructura.json")
            segment_start, segment_end = aa2_segments[ev["segment"]]
            line_start, line_end = ev["source_lines"]
            require(
                segment_start <= line_start <= line_end <= segment_end,
                f"{ev['id']}: rango fuera del segmento declarado {ev['segment']}",
            )

        required_aa2_nodes = {
            "concept.agape.aa2",
            "concept.alteridad_activadora.aa2",
            "concept.hijos_agape.aa2",
            "concept.posicion_voluntad.aa2",
            "concept.eros.aa2",
            "concept.deimos.aa2",
            "concept.anteros.aa2",
            "concept.fobos.aa2",
            "concept.potos.aa2",
            "concept.harmonia.aa2",
            "concept.tension_umbral.aa2",
            "concept.tension_defensa.aa2",
            "concept.tension_tiempo.aa2",
            "concept.movilidad_relacional.aa2",
            "concept.fijacion_relacional.aa2",
            "concept.patologia_sistemica.aa2",
            "concept.himeno.aa2",
            "concept.integridad_forma_propia.aa2",
            "concept.retorno_himeno.aa2",
            "formulation.agape.aa2",
            "formulation.orientation.aa2",
            "formulation.children.aa2",
            "formulation.cross_levels.aa2",
            "formulation.mobility_health.aa2",
            "formulation.phi2.aa2",
            "formulation.himeno.aa2",
            "formulation.volume_crosswalk.aa2",
            "formal.alpha_alterity.aa2",
            "formal.transition_agape.aa2",
            "formal.phi1.aa2",
            "formal.phi2.aa2",
            "formal.harmonia.aa2",
        }
        require(
            required_aa2_nodes <= set(nodes),
            f"Núcleo de Afrodita Areia II incompleto; faltan nodos: {sorted(required_aa2_nodes - set(nodes))}",
        )

        required_aa2_routes = {
            "route.aa2.agape_orientation",
            "route.aa2.children_positions",
            "route.aa2.cross_level_status",
            "route.aa2.threshold",
            "route.aa2.defense",
            "route.aa2.time_presence",
            "route.aa2.phi2_mobility",
            "route.aa2.himeno",
            "route.aa2.formal_objects",
            "route.aa2.volume_continuity",
        }
        require(
            required_aa2_routes <= set(routes),
            f"Rutas de Afrodita Areia II incompletas: {sorted(required_aa2_routes - set(routes))}",
        )

        aa2_reviews = {
            "review.aa2.phi2_function_change",
            "review.aa2.volume_crosswalk",
            "review.aa2.cross_level_status",
            "review.aa2.alpha_symbol_collision",
        }
        require(aa2_reviews <= set(reviews), "Deben conservarse las cuatro revisiones pendientes de Afrodita Areia II")
        require(
            "review.aa2.phi2_function_change"
            in routes["route.aa2.phi2_mobility"].get("must_surface_review_items", []),
            "La ruta de φ₂ y movilidad de AA-II debe surfacer su cambio funcional pendiente",
        )
        require(
            "review.aa2.cross_level_status"
            in routes["route.aa2.cross_level_status"].get("must_surface_review_items", []),
            "La ruta transnivel de AA-II debe surfacer su estatuto pendiente",
        )
        require(
            "review.aa2.volume_crosswalk"
            in routes["route.aa2.volume_continuity"].get("must_surface_review_items", []),
            "La ruta de continuidad de AA-II debe surfacer sus discordancias editoriales",
        )
        require(
            "review.aa2.alpha_symbol_collision"
            in routes["route.aa2.formal_objects"].get("must_surface_review_items", []),
            "La ruta formal de AA-II debe surfacer la colisión del símbolo α",
        )
        require(
            relations["rel.phi2_aa2.differs_phi2_caos"]["evidence_status"] == "inferred"
            and relations["rel.phi2_aa2.differs_bis_aa1"]["evidence_status"] == "inferred",
            "La diferencia funcional de φ₂ en AA-II no puede presentarse como adjudicación autoral",
        )
        require(
            relations["rel.alpha_alterity.distinguished_assumption"]["evidence_status"] == "inferred",
            "La separación entre α-alteridad y α-coeficiente debe seguir marcada como inferida",
        )
        require(
            "review.aa2.phi2_function_change"
            in routes["route.ego.explicacion"].get("must_surface_review_items", []),
            "La ruta histórica del ego debe surfacer la variación relacional de φ₂",
        )
        require(
            "review.aego.formulation_change"
            in routes["route.aa2.himeno"].get("must_surface_review_items", []),
            "La distinción Himeno/Aego debe conservar visible la evolución histórica de Aego",
        )
        require(
            relations["rel.mobility_aa2.revised_by_himeno"]["evidence_status"] == "explicit",
            "Himeno debe conservarse como revisión autoral explícita del criterio de movilidad",
        )

        # Invariantes ganadas al integrar Afrodita Areia III sistemáticamente en F2.
        aa3_structure_path = (
            ROOT
            / "corpus"
            / "libros"
            / "afrodita-areia"
            / "03-damasen"
            / "estructura.json"
        )
        require(aa3_structure_path.exists(), "Falta la estructura derivada de Afrodita Areia III")
        aa3_structure = json.loads(aa3_structure_path.read_text(encoding="utf-8"))
        require(
            aa3_structure.get("sha256") == works["AA-III"]["sha256"],
            "La estructura de Afrodita Areia III no corresponde al hash de la fuente canónica",
        )
        aa3_segments = {
            segment["path"]: (segment["start_line"], segment["end_line"])
            for segment in aa3_structure["segments"]
        }
        require(len(aa3_segments) == 25, "La estructura de Afrodita Areia III debe conservar sus 25 segmentos")
        aa3_evidence = [ev for ev in evidence.values() if ev["work_id"] == "AA-III"]
        aa3_covered_segments = {ev["segment"] for ev in aa3_evidence}
        require(
            set(aa3_segments) <= aa3_covered_segments,
            "La auditoría de Afrodita Areia III debe cubrir preliminares, prefacio, "
            "prólogo, veinte capítulos, apéndice y glosario; faltan: "
            f"{sorted(set(aa3_segments) - aa3_covered_segments)}",
        )
        require(
            len(aa3_evidence) >= 49,
            f"La auditoría semántica de Afrodita Areia III perdió granularidad: {len(aa3_evidence)} evidencias",
        )
        for ev in aa3_evidence:
            require(ev["segment"] in aa3_segments, f"{ev['id']}: segmento de AA-III no declarado en estructura.json")
            segment_start, segment_end = aa3_segments[ev["segment"]]
            line_start, line_end = ev["source_lines"]
            require(
                segment_start <= line_start <= line_end <= segment_end,
                f"{ev['id']}: rango fuera del segmento declarado {ev['segment']}",
            )

        required_aa3_nodes = {
            "concept.aego_damasen",
            "concept.aego_peribea",
            "concept.autodeterminacion_causal.aa3",
            "concept.bordes_autodeterminacion.aa3",
            "concept.disfasia_volitiva.aa3",
            "concept.saturacion_expresiva.aa3",
            "concept.eje_propio.aa3",
            "concept.adominio.aa3",
            "concept.pax_damasen.aa3",
            "concept.vinculo_colapsado.aa3",
            "concept.encuentro_genuino.aa3",
            "concept.perturbacion_productiva.aa3",
            "concept.retorno_aego.aa3",
            "concept.mascarada.aa3",
            "concept.aego_colectivo.aa3",
            "concept.damasen_colectivo.aa3",
            "concept.peribea_colectivo.aa3",
            "concept.retorno_colectivo.aa3",
            "concept.soberania_colectiva.aa3",
            "concept.contrato_fiscal_aego.aa3",
            "concept.estado_damasen.aa3",
            "concept.contribuyente_peribea.aa3",
            "formulation.mediations.aa3",
            "formulation.aego_levels.aa3",
            "formulation.himeno_bridge.aa3",
            "formulation.identity.aa3",
            "formulation.agape.aa3",
            "formulation.damasen_dimension.aa3",
            "formulation.mythic_reading.aa3",
            "formulation.fiscal.aa3",
            "formal.aego.aa3",
            "formal.aego_applicability.aa3",
            "formal.aego_regimes.aa3",
        }
        require(
            required_aa3_nodes <= set(nodes),
            f"Núcleo de Afrodita Areia III incompleto; faltan nodos: {sorted(required_aa3_nodes - set(nodes))}",
        )

        required_aa3_routes = {
            "route.aa3.architecture_method",
            "route.aa3.aego_formal",
            "route.aa3.language_regimes",
            "route.aa3.damasen",
            "route.aa3.peribea",
            "route.aa3.volume_crosswalk",
            "route.aa3.collapsed_bond",
            "route.aa3.individual_return",
            "route.aa3.collective_identity",
            "route.aa3.collective_poles",
            "route.aa3.collective_return",
            "route.aa3.fiscal_contract",
            "route.aa3.editorial_issues",
        }
        require(
            required_aa3_routes <= set(routes),
            f"Rutas de Afrodita Areia III incompletas: {sorted(required_aa3_routes - set(routes))}",
        )

        aa3_reviews = {
            "review.aa3.aego_zero_locus",
            "review.aa3.aego_regime_derivative",
            "review.aa3.phi_functions",
            "review.aa3.himeno_crosswalk",
            "review.aa3.myth_sources",
            "review.aa3.damasen_dimension",
            "review.aa3.identity_masquerade",
            "review.aa3.agape_glossary",
            "review.aa3.nonhuman_boundary",
            "review.aa3.glossary_notation",
        }
        require(aa3_reviews <= set(reviews), "Deben conservarse las diez revisiones pendientes de Afrodita Areia III")
        require(
            {
                "review.aa3.aego_zero_locus",
                "review.aa3.aego_regime_derivative",
                "review.aa3.phi_functions",
                "review.aa3.nonhuman_boundary",
            }
            <= set(routes["route.aa3.aego_formal"].get("must_surface_review_items", [])),
            "La ruta formal de AA-III debe surfacer lugar del cero, derivada, mediaciones y límite no humano",
        )
        require(
            {"review.aa3.myth_sources", "review.aa3.damasen_dimension"}
            <= set(routes["route.aa3.damasen"].get("must_surface_review_items", [])),
            "La ruta de Damasén debe surfacer sus problemas mitográfico y dimensional",
        )
        require(
            {
                "review.aa3.himeno_crosswalk",
                "review.aa3.identity_masquerade",
                "review.aa3.agape_glossary",
                "review.aa3.phi_functions",
            }
            <= set(routes["route.aa3.volume_crosswalk"].get("must_surface_review_items", [])),
            "La ruta histórica de AA-III debe surfacer todas sus variaciones doctrinales entre volúmenes",
        )
        require(
            {"review.aa3.myth_sources", "review.aa3.glossary_notation"}
            <= set(routes["route.aa3.editorial_issues"].get("must_surface_review_items", [])),
            "La ruta editorial de AA-III debe surfacer fuente mítica y notación dañada",
        )
        require(
            "review.aa3.identity_masquerade"
            in routes["route.aa1.identity_distortions"].get("must_surface_review_items", []),
            "La ruta histórica de identidad debe conservar visible la reformulación de AA-III",
        )
        require(
            "review.aa3.agape_glossary"
            in routes["route.aa2.agape_orientation"].get("must_surface_review_items", []),
            "La ruta de Ágape debe conservar visible la definición divergente del glosario de AA-III",
        )
        require(
            "review.aa3.himeno_crosswalk"
            in routes["route.aa2.himeno"].get("must_surface_review_items", []),
            "La ruta de Himeno debe conservar visible el puente retrospectivo de AA-III",
        )
        require(
            relations["rel.mediations_aa3.differs_aa2"]["evidence_status"] == "inferred"
            and relations["rel.himeno_bridge_aa3.differs_aa2"]["evidence_status"] == "inferred"
            and relations["rel.identity_aa3.differs_aa1"]["evidence_status"] == "inferred"
            and relations["rel.agape_aa3.differs_aa2"]["evidence_status"] == "inferred",
            "Las diferencias históricas entre AA-III y volúmenes previos no pueden presentarse como adjudicaciones autorales",
        )
        require(
            "review.aa3.aego_zero_locus"
            in routes["route.aego.definicion_evolucion"].get("must_surface_review_items", []),
            "La ruta general de Aego debe conservar visible la atribución variable del producto nulo",
        )

        # Invariantes ganadas al integrar Afrodita Areia IV sistemáticamente en F2.
        aa4_structure_path = (
            ROOT
            / "corpus"
            / "libros"
            / "afrodita-areia"
            / "04-areopago"
            / "estructura.json"
        )
        require(aa4_structure_path.exists(), "Falta la estructura derivada de Afrodita Areia IV")
        aa4_structure = json.loads(aa4_structure_path.read_text(encoding="utf-8"))
        require(
            aa4_structure.get("sha256") == works["AA-IV"]["sha256"],
            "La estructura de Afrodita Areia IV no corresponde al hash de la fuente canónica",
        )
        require(
            aa4_structure.get("source") == works["AA-IV"]["source"],
            "La ruta canónica de Afrodita Areia IV debe conservar la grafía editorial registrada",
        )
        aa4_segments = {
            segment["path"]: (segment["start_line"], segment["end_line"])
            for segment in aa4_structure["segments"]
        }
        require(len(aa4_segments) == 19, "La estructura de Afrodita Areia IV debe conservar sus 19 segmentos")
        aa4_evidence = [ev for ev in evidence.values() if ev["work_id"] == "AA-IV"]
        aa4_covered_segments = {ev["segment"] for ev in aa4_evidence}
        require(
            set(aa4_segments) <= aa4_covered_segments,
            "La auditoría de Afrodita Areia IV debe cubrir preliminares, prólogo, "
            "trece capítulos, glosario y tres apéndices; faltan: "
            f"{sorted(set(aa4_segments) - aa4_covered_segments)}",
        )
        require(
            len(aa4_evidence) >= 42,
            f"La auditoría semántica de Afrodita Areia IV perdió granularidad: {len(aa4_evidence)} evidencias",
        )
        for ev in aa4_evidence:
            require(ev["segment"] in aa4_segments, f"{ev['id']}: segmento de AA-IV no declarado en estructura.json")
            segment_start, segment_end = aa4_segments[ev["segment"]]
            line_start, line_end = ev["source_lines"]
            require(
                segment_start <= line_start <= line_end <= segment_end,
                f"{ev['id']}: rango fuera del segmento declarado {ev['segment']}",
            )

        required_aa4_nodes = {
            "concept.imputacion_causal.aa4",
            "concept.cadena_causal.aa4",
            "concept.nodo_necesario.aa4",
            "concept.diseno_campo.aa4",
            "concept.sustituibilidad.aa4",
            "concept.jerarquia_causal.aa4",
            "concept.dolo.aa4",
            "concept.invisibilidades_dolo.aa4",
            "concept.externalizacion_causal.aa4",
            "concept.dano_secundario.aa4",
            "concept.eutaxia_utopica.aa4",
            "concept.dano_total.aa4",
            "concept.pena_tiempo_vida.aa4",
            "concept.deslinde_autoridad.aa4",
            "concept.limite_funcional_legal.aa4",
            "concept.quid_pro_quo.aa4",
            "concept.imputacion_acto_por_acto.aa4",
            "concept.delta_int.aa4",
            "concept.delta_ext.aa4",
            "concept.causalidad_acumulativa.aa4",
            "concept.dano_sin_nodo_individual.aa4",
            "concept.contrato_fiscal.aa4",
            "concept.soberano_ontologico.aa4",
            "concept.soberano_colectivo.aa4",
            "concept.ciudadano.aa4",
            "concept.derechos_activo.aa4",
            "concept.estado_deudor.aa4",
            "concept.fraude_annona.aa4",
            "concept.eutaxia_colectiva.aa4",
            "formulation.responsibility.aa4",
            "formulation.corporate_ego.aa4",
            "formulation.damasen_peribea_institutional.aa4",
            "formulation.normativity_limit.aa4",
            "formulation.subordinate_imputability.aa4",
            "formulation.fiscal.aa4",
            "formal.node_necessary.aa4",
            "formal.secondary_damage.aa4",
            "formal.total_damage.aa4",
            "formal.ego_iteration.aa4",
            "formal.derivatives.aa4",
            "formal.imputation_postulates.aa4",
        }
        require(
            required_aa4_nodes <= set(nodes),
            f"Núcleo de Afrodita Areia IV incompleto; faltan nodos: {sorted(required_aa4_nodes - set(nodes))}",
        )

        required_aa4_routes = {
            "route.aa4.architecture_method",
            "route.aa4.responsibility_causality",
            "route.aa4.corporate_ego",
            "route.aa4.node_hierarchy",
            "route.aa4.damasen_peribea",
            "route.aa4.dolo_externalization",
            "route.aa4.damage_penalty",
            "route.aa4.eutaxia",
            "route.aa4.subordinate",
            "route.aa4.derivatives_formal",
            "route.aa4.fiscal_contract",
            "route.aa4.open_limits",
        }
        require(
            required_aa4_routes <= set(routes),
            f"Rutas de Afrodita Areia IV incompletas: {sorted(required_aa4_routes - set(routes))}",
        )

        aa4_reviews = {
            "review.aa4.responsibility_crosswalk",
            "review.aa4.corporate_ego",
            "review.aa4.normative_derivation",
            "review.aa4.node_necessity",
            "review.aa4.overdetermination",
            "review.aa4.proportionality",
            "review.aa4.executor_necessity",
            "review.aa4.damasen_crosswalk",
            "review.aa4.secondary_damage_measure",
            "review.aa4.subordinate_criteria",
            "review.aa4.derivative_formalization",
            "review.aa4.postulate_inventory",
            "review.aa4.fiscal_crosswalk",
            "review.aa4.editorial_notation",
        }
        require(aa4_reviews <= set(reviews), "Deben conservarse las catorce revisiones pendientes de Afrodita Areia IV")
        require(
            {
                "review.aa4.node_necessity",
                "review.aa4.overdetermination",
                "review.aa4.proportionality",
                "review.aa4.executor_necessity",
            }
            <= set(routes["route.aa4.node_hierarchy"].get("must_surface_review_items", [])),
            "La ruta causal de AA-IV debe surfacer necesidad, sobredeterminación, proporcionalidad y ejecutor",
        )
        require(
            {
                "review.aa4.derivative_formalization",
                "review.aa4.postulate_inventory",
                "review.aa4.editorial_notation",
                "review.aa3.aego_zero_locus",
                "review.aa3.aego_regime_derivative",
            }
            <= set(routes["route.aa4.derivatives_formal"].get("must_surface_review_items", [])),
            "La ruta formal de AA-IV debe surfacer tipado, inventario, notación y tensiones heredadas de Aego",
        )
        require(
            {
                "review.aa4.fiscal_crosswalk",
                "review.aa4.normative_derivation",
                "review.aa3.aego_zero_locus",
            }
            <= set(routes["route.aa4.fiscal_contract"].get("must_surface_review_items", [])),
            "La ruta fiscal de AA-IV debe surfacer evolución, derivación normativa y Aego",
        )
        require(
            {"review.aa4.subordinate_criteria", "review.aa4.executor_necessity"}
            <= set(routes["route.aa4.subordinate"].get("must_surface_review_items", [])),
            "La ruta del subordinado debe surfacer sus criterios variables y el estatuto del ejecutor",
        )
        require(
            "review.aa4.responsibility_crosswalk"
            in routes["route.aa1.responsibility_assumption"].get("must_surface_review_items", []),
            "La ruta histórica de responsabilidad debe conservar visible la reformulación de AA-IV",
        )
        require(
            "review.aa4.damasen_crosswalk"
            in routes["route.aego.definicion_evolucion"].get("must_surface_review_items", []),
            "La ruta general de Aego debe conservar visible la aplicación institucional de AA-IV",
        )
        require(
            "review.aa4.fiscal_crosswalk"
            in routes["route.aa3.fiscal_contract"].get("must_surface_review_items", []),
            "La ruta fiscal de AA-III debe conservar visible la reformulación de AA-IV",
        )
        require(
            relations["rel.responsibility_aa4.differs_aa1"]["evidence_status"] == "inferred"
            and relations["rel.damasen_application_aa4.reframes_aa3"]["evidence_status"] == "inferred"
            and relations["rel.fiscal_aa4.reframes_aa3"]["evidence_status"] == "inferred",
            "Las diferencias históricas de AA-IV no pueden presentarse como adjudicaciones autorales",
        )
        require(
            nodes["formal.imputation_postulates.aa4"]["formal_spec"]["listed"]
            == ["I1", "I2", "I5", "I6", "I7", "I9", "I10"],
            "La omisión editorial de I3, I4 e I8 debe conservarse visible hasta revisión",
        )

        # Invariantes ganadas al integrar Afrodita Areia V sistemáticamente en F2.
        aa5_structure_path = (
            ROOT
            / "corpus"
            / "libros"
            / "afrodita-areia"
            / "05-caelus"
            / "estructura.json"
        )
        require(aa5_structure_path.exists(), "Falta la estructura derivada de Afrodita Areia V")
        aa5_structure = json.loads(aa5_structure_path.read_text(encoding="utf-8"))
        require(
            aa5_structure.get("sha256") == works["AA-V"]["sha256"],
            "La estructura de Afrodita Areia V no corresponde al hash de la fuente canónica",
        )
        require(
            aa5_structure.get("source") == works["AA-V"]["source"],
            "La ruta canónica de Afrodita Areia V debe conservarse sin sustituciones editoriales",
        )
        aa5_segments = {
            segment["path"]: (segment["start_line"], segment["end_line"])
            for segment in aa5_structure["segments"]
        }
        require(len(aa5_segments) == 18, "La estructura de Afrodita Areia V debe conservar sus 18 segmentos")
        aa5_evidence = [ev for ev in evidence.values() if ev["work_id"] == "AA-V"]
        aa5_covered_segments = {ev["segment"] for ev in aa5_evidence}
        require(
            set(aa5_segments) <= aa5_covered_segments,
            "La auditoría de Afrodita Areia V debe cubrir preliminares, prólogo, "
            "trece capítulos, epílogo, apéndice y glosario; faltan: "
            f"{sorted(set(aa5_segments) - aa5_covered_segments)}",
        )
        require(
            len(aa5_evidence) >= 50,
            f"La auditoría semántica de Afrodita Areia V perdió granularidad: {len(aa5_evidence)} evidencias",
        )
        for ev in aa5_evidence:
            require(ev["segment"] in aa5_segments, f"{ev['id']}: segmento de AA-V no declarado en estructura.json")
            segment_start, segment_end = aa5_segments[ev["segment"]]
            line_start, line_end = ev["source_lines"]
            require(
                segment_start <= line_start <= line_end <= segment_end,
                f"{ev['id']}: rango fuera del segmento declarado {ev['segment']}",
            )

        required_aa5_nodes = {
            "concept.scale.aa5",
            "concept.collective_collapse.aa5",
            "formulation.hume_scales.aa5",
            "concept.sum.aa5",
            "concept.ego_integral.aa5",
            "concept.sovereign_ego.aa5",
            "concept.freedom.aa5",
            "concept.fiscal_contract.aa5",
            "concept.state_ego.aa5",
            "concept.collective_identity.aa5",
            "concept.borrowed_will.aa5",
            "concept.state_phi1.aa5",
            "concept.state_act.aa5",
            "concept.state_phi2.aa5",
            "concept.state_bias.aa5",
            "concept.sovereign_collective.aa5",
            "concept.citizen.aa5",
            "concept.state_capital.aa5",
            "concept.citizen_assets.aa5",
            "concept.state_liability.aa5",
            "concept.material_conditions.aa5",
            "concept.recognized_rights.aa5",
            "concept.ontological_equality.aa5",
            "concept.politics.aa5",
            "concept.proselytism.aa5",
            "concept.state_legitimacy.aa5",
            "concept.friction.aa5",
            "concept.state_aego_damasen.aa5",
            "concept.state_aego_peribea.aa5",
            "concept.fraud_annona.aa5",
            "concept.fraud_forms.aa5",
            "concept.collective_eutaxia.aa5",
            "concept.audit_protocol.aa5",
            "concept.state_solvency.aa5",
            "concept.deferred_debt.aa5",
            "concept.debitor_adjustment.aa5",
            "concept.restorative_justice.aa5",
            "formulation.normative_descriptive.aa5",
            "formulation.responsibility.aa5",
            "formulation.human_rights.aa5",
            "formulation.redistribution.aa5",
            "formal.ego_state.aa5",
            "formal.double_entry.aa5",
            "formal.eutaxia.aa5",
            "formal.asymmetry.aa5",
            "formal.total_damage.aa5",
            "formal.adjustment_node.aa5",
        }
        require(
            required_aa5_nodes <= set(nodes),
            f"Núcleo de Afrodita Areia V incompleto; faltan nodos: {sorted(required_aa5_nodes - set(nodes))}",
        )

        required_aa5_routes = {
            "route.aa5.architecture_scales",
            "route.aa5.ego_freedom",
            "route.aa5.collective_contract",
            "route.aa5.philosophical_crosswalk",
            "route.aa5.state_formula",
            "route.aa5.capital_double_entry",
            "route.aa5.rights_conditions",
            "route.aa5.citizen_sovereign",
            "route.aa5.state_aego",
            "route.aa5.fraud_annona",
            "route.aa5.audit_protocol",
            "route.aa5.debitor_adjustment",
            "route.aa5.formal_editorial",
        }
        require(
            required_aa5_routes <= set(routes),
            f"Rutas de Afrodita Areia V incompletas: {sorted(required_aa5_routes - set(routes))}",
        )

        aa5_reviews = {
            "review.aa5.hume_crosswalk",
            "review.aa5.emergence_bridge",
            "review.aa5.scale_threshold",
            "review.aa5.freedom_transfer",
            "review.aa5.state_will",
            "review.aa5.state_formula",
            "review.aa5.contract_validity",
            "review.aa5.descriptive_normative",
            "review.aa5.responsibility_crosswalk",
            "review.aa5.equality_capital",
            "review.aa5.rights_scope",
            "review.aa5.double_entry",
            "review.aa5.audit_criterion",
            "review.aa5.eutaxia_formal",
            "review.aa5.counterfactual",
            "review.aa5.damage_formal",
            "review.aa5.actor_scope",
            "review.aa5.deduction_fiscal",
            "review.aa5.editorial_notation",
            "review.aa5.redistribution",
        }
        require(aa5_reviews <= set(reviews), "Deben conservarse las veinte revisiones pendientes de Afrodita Areia V")
        require(
            {
                "review.aa5.hume_crosswalk",
                "review.aa5.emergence_bridge",
                "review.aa5.scale_threshold",
                "review.aa5.descriptive_normative",
                "review.aa4.normative_derivation",
            }
            <= set(routes["route.aa5.architecture_scales"].get("must_surface_review_items", [])),
            "La ruta de escalas debe surfacer cambio humeano, emergencia, umbral y registro normativo",
        )
        require(
            {
                "review.aa5.state_formula",
                "review.aa5.state_will",
                "review.aa5.responsibility_crosswalk",
                "review.aa5.editorial_notation",
            }
            <= set(routes["route.aa5.state_formula"].get("must_surface_review_items", [])),
            "La ruta del ego estatal debe surfacer tipado, voluntad, responsabilidad y notación",
        )
        require(
            {
                "review.aa5.audit_criterion",
                "review.aa5.eutaxia_formal",
                "review.aa5.counterfactual",
                "review.aa4.proportionality",
            }
            <= set(routes["route.aa5.audit_protocol"].get("must_surface_review_items", [])),
            "La ruta de auditoría debe surfacer universalidad, cálculo estocástico, identificación y proporcionalidad",
        )
        require(
            {
                "review.aa5.damage_formal",
                "review.aa5.actor_scope",
                "review.aa5.deduction_fiscal",
                "review.aa5.descriptive_normative",
                "review.aa4.secondary_damage_measure",
            }
            <= set(routes["route.aa5.debitor_adjustment"].get("must_surface_review_items", [])),
            "La ruta del ajuste debe surfacer medida, sujeto obligado, variante glosada y salto normativo",
        )
        require(
            {
                "review.aa5.state_formula",
                "review.aa5.double_entry",
                "review.aa5.eutaxia_formal",
                "review.aa5.damage_formal",
                "review.aa5.actor_scope",
                "review.aa5.deduction_fiscal",
                "review.aa5.editorial_notation",
            }
            <= set(routes["route.aa5.formal_editorial"].get("must_surface_review_items", [])),
            "La ruta formal-editorial de AA-V debe conservar todas sus reservas técnicas y glosadas",
        )
        require(
            "review.aa5.responsibility_crosswalk"
            in routes["route.aa1.responsibility_assumption"].get("must_surface_review_items", []),
            "La ruta histórica de responsabilidad debe conservar visible la aplicación de AA-V",
        )
        require(
            "review.aa5.state_will"
            in routes["route.aego.definicion_evolucion"].get("must_surface_review_items", []),
            "La ruta histórica de Aego debe conservar visible la agencia atribuida al Estado en AA-V",
        )
        require(
            {"review.aa5.contract_validity", "review.aa5.actor_scope"}
            <= set(routes["route.aa3.fiscal_contract"].get("must_surface_review_items", [])),
            "La ruta fiscal de AA-III debe surfacer validez y sujeto obligado en AA-V",
        )
        require(
            {"review.aa5.hume_crosswalk", "review.aa5.descriptive_normative", "review.aa5.audit_criterion"}
            <= set(routes["route.aa4.fiscal_contract"].get("must_surface_review_items", [])),
            "La ruta fiscal de AA-IV debe surfacer la revisión humeana y operacional de AA-V",
        )
        require(
            relations["rel.hume_aa5.revises_aa4"]["evidence_status"] == "inferred"
            and relations["rel.responsibility_aa5.differs_aa1"]["evidence_status"] == "inferred"
            and relations["rel.fiscal_aa5.reframes_aa3"]["evidence_status"] == "inferred"
            and relations["rel.state_bias_aa5.overlaps_identity"]["evidence_status"] == "inferred",
            "Las diferencias históricas e internas de AA-V no pueden presentarse como adjudicaciones autorales",
        )
        require(
            nodes["formal.double_entry.aa5"]["formal_spec"].get("identity")
            == "Capital estatal ≡ Activo ciudadano + Pasivo estatal",
            "La identidad contable publicada por AA-V debe conservarse literalmente hasta revisión",
        )
        require(
            nodes["formal.eutaxia.aa5"]["formal_spec"].get("expression")
            == "EU(t) = E[dX/dt | F_t]",
            "La fórmula estocástica publicada por AA-V debe conservarse literalmente hasta revisión",
        )
        require(
            "review.aa5.deduction_fiscal"
            in routes["route.aa5.formal_editorial"].get("must_surface_review_items", []),
            "La deducción fiscal introducida solo en el glosario debe permanecer visible",
        )

        # Invariantes ganadas al integrar El dilema de Aquiles sistemáticamente en F2.
        require("AQUILES" in works, "Falta El dilema de Aquiles en el registro de obras")
        aquiles_structure_path = (
            ROOT
            / "corpus"
            / "libros"
            / "dilema-de-aquiles"
            / "estructura.json"
        )
        require(aquiles_structure_path.exists(), "Falta la estructura derivada de El dilema de Aquiles")
        aquiles_structure = json.loads(aquiles_structure_path.read_text(encoding="utf-8"))
        require(
            aquiles_structure.get("sha256") == works["AQUILES"]["sha256"],
            "La estructura de El dilema de Aquiles no corresponde al hash de la fuente canónica",
        )
        require(
            aquiles_structure.get("source") == works["AQUILES"]["source"],
            "La ruta canónica de El dilema de Aquiles debe conservarse sin sustituciones editoriales",
        )
        aquiles_segments = {
            segment["path"]: (segment["start_line"], segment["end_line"])
            for segment in aquiles_structure["segments"]
        }
        require(
            len(aquiles_segments) == 11,
            "La estructura de El dilema de Aquiles debe conservar preliminares, prólogo, ocho capítulos y epílogo",
        )
        aquiles_evidence = [ev for ev in evidence.values() if ev["work_id"] == "AQUILES"]
        aquiles_covered_segments = {ev["segment"] for ev in aquiles_evidence}
        require(
            set(aquiles_segments) <= aquiles_covered_segments,
            "La auditoría de El dilema de Aquiles debe cubrir sus once segmentos; faltan: "
            f"{sorted(set(aquiles_segments) - aquiles_covered_segments)}",
        )
        require(
            len(aquiles_evidence) >= 51,
            "La auditoría semántica de El dilema de Aquiles perdió granularidad: "
            f"{len(aquiles_evidence)} evidencias",
        )
        for ev in aquiles_evidence:
            require(
                ev["segment"] in aquiles_segments,
                f"{ev['id']}: segmento de El dilema de Aquiles no declarado en estructura.json",
            )
            segment_start, segment_end = aquiles_segments[ev["segment"]]
            line_start, line_end = ev["source_lines"]
            require(
                segment_start <= line_start <= line_end <= segment_end,
                f"{ev['id']}: rango fuera del segmento declarado {ev['segment']}",
            )

        required_aquiles_nodes = {
            "formulation.scope.aq",
            "concept.ego_axis.aq",
            "formulation.ego.aq",
            "concept.ego_image.aq",
            "concept.own_egolatry.aq",
            "concept.borrowed_egolatry.aq",
            "concept.egocentrism.aq",
            "concept.achilles_dilemma.aq",
            "concept.image_displacement.aq",
            "formulation.displacement_stages.aq",
            "concept.confirming_recognition.aq",
            "concept.constitutive_recognition.aq",
            "concept.performance_identity.aq",
            "concept.visibility_economy.aq",
            "formulation.achilles_myth.aq",
            "concept.kleos_image.aq",
            "concept.heel_blindspot.aq",
            "formulation.dissociation.aq",
            "concept.acting_self.aq",
            "concept.representing_self.aq",
            "formulation.dissociation_mechanisms.aq",
            "concept.body_witness.aq",
            "concept.image_fall.aq",
            "formulation.fall_stages.aq",
            "concept.return_self.aq",
            "concept.causal_selfdetermination.aq",
            "formulation.return_practices.aq",
            "concept.internal_sovereign_fear.aq",
            "concept.fear_forgiveness.aq",
            "concept.sovereign_forgiveness.aq",
            "formulation.forgiveness.aq",
            "concept.presence.aq",
            "concept.performance.aq",
            "concept.bounded_generosity.aq",
            "formulation.responsibility.aq",
            "concept.position_ethics.aq",
            "concept.excellence_without_image.aq",
            "formulation.authentic_ethics.aq",
            "concept.habited_tension.aq",
            "concept.return_within_return.aq",
            "formulation.narrative_identity.aq",
            "concept.phthia.aq",
        }
        require(
            required_aquiles_nodes <= set(nodes),
            "Núcleo de El dilema de Aquiles incompleto; faltan nodos: "
            f"{sorted(required_aquiles_nodes - set(nodes))}",
        )

        required_aquiles_routes = {
            "route.aq.scope_sources",
            "route.aq.ego_triad",
            "route.aq.displacement_recognition",
            "route.aq.myth_analysis",
            "route.aq.dissociation_fall",
            "route.aq.fear_forgiveness",
            "route.aq.return_autodetermination",
            "route.aq.authentic_ethics",
            "route.aq.tension_closure",
            "route.aq.crosswork_history",
        }
        require(
            required_aquiles_routes <= set(routes),
            "Rutas de El dilema de Aquiles incompletas: "
            f"{sorted(required_aquiles_routes - set(routes))}",
        )

        aquiles_reviews = {
            "review.aq.ego_crosswalk",
            "review.aq.ego_ownership",
            "review.aq.authenticity_criterion",
            "review.aq.clinical_boundary",
            "review.aq.empirical_support",
            "review.aq.myth_status",
            "review.aq.editorial_citations",
            "review.aq.dissociation_crosswalk",
            "review.aq.dissociation_operationalization",
            "review.aq.body_claims",
            "review.aq.fall_inevitability",
            "review.aq.return_ontology",
            "review.aq.hobbes_status",
            "review.aq.forgiveness_order",
            "review.aq.forgiveness_normativity",
            "review.aq.responsibility_crosswalk",
            "review.aq.freedom_crosswalk",
            "review.aq.identity_crosswalk",
            "review.aq.relational_generalization",
        }
        require(
            aquiles_reviews <= set(reviews),
            "Deben conservarse las diecinueve revisiones pendientes de El dilema de Aquiles",
        )
        require(
            {
                "review.aq.clinical_boundary",
                "review.aq.empirical_support",
                "review.aq.myth_status",
                "review.aq.editorial_citations",
            }
            <= set(routes["route.aq.scope_sources"].get("must_surface_review_items", [])),
            "La ruta de alcance de Aquiles debe conservar sus reservas clínicas, empíricas, míticas y editoriales",
        )
        require(
            {
                "review.aq.ego_crosswalk",
                "review.aq.ego_ownership",
                "review.aq.authenticity_criterion",
            }
            <= set(routes["route.aq.ego_triad"].get("must_surface_review_items", [])),
            "La ruta del ego de Aquiles debe surfacer formulación histórica, propiedad y criterio de autenticidad",
        )
        require(
            {
                "review.aq.clinical_boundary",
                "review.aq.dissociation_crosswalk",
                "review.aq.dissociation_operationalization",
                "review.aq.body_claims",
                "review.aq.fall_inevitability",
                "review.aq.return_ontology",
            }
            <= set(routes["route.aq.dissociation_fall"].get("must_surface_review_items", [])),
            "La ruta disociación-caída debe conservar todas sus reservas de alcance, medida y ontología",
        )
        require(
            {
                "review.aq.hobbes_status",
                "review.aq.forgiveness_order",
                "review.aq.forgiveness_normativity",
                "review.aq.relational_generalization",
            }
            <= set(routes["route.aq.fear_forgiveness"].get("must_surface_review_items", [])),
            "La ruta miedo-perdón debe conservar contradicción hobbesiana, orden, normatividad y alcance relacional",
        )
        require(
            {
                "review.aq.ego_crosswalk",
                "review.aq.ego_ownership",
                "review.aq.authenticity_criterion",
                "review.aq.clinical_boundary",
                "review.aq.empirical_support",
                "review.aq.return_ontology",
                "review.aq.freedom_crosswalk",
                "review.aq.identity_crosswalk",
            }
            <= set(routes["route.aq.return_autodetermination"].get("must_surface_review_items", [])),
            "La ruta de retorno debe conservar todas las reservas doctrinales, clínicas y metódicas",
        )
        require(
            {
                "review.aq.ego_crosswalk",
                "review.aq.dissociation_crosswalk",
                "review.aq.freedom_crosswalk",
                "review.aq.responsibility_crosswalk",
                "review.aq.identity_crosswalk",
            }
            <= set(routes["route.aq.crosswork_history"].get("must_surface_review_items", [])),
            "La ruta histórica de Aquiles no puede ocultar ninguna diferencia con el núcleo ontológico",
        )
        require(
            {
                "review.aq.ego_crosswalk",
                "review.aq.ego_ownership",
            }
            <= set(routes["route.ego.explicacion"].get("must_surface_review_items", [])),
            "La ruta general del ego debe conservar visible la formulación de Aquiles",
        )
        require(
            {
                "review.aq.dissociation_crosswalk",
                "review.aq.identity_crosswalk",
            }
            <= set(routes["route.aa1.identity_distortions"].get("must_surface_review_items", [])),
            "La ruta histórica de identidad y disociación debe incorporar las diferencias de Aquiles",
        )
        require(
            "review.aq.responsibility_crosswalk"
            in routes["route.aa4.responsibility_causality"].get("must_surface_review_items", []),
            "La ruta de responsabilidad causal debe conservar visible la condición de autoría de Aquiles",
        )
        require(
            "review.aq.freedom_crosswalk"
            in routes["route.aa5.ego_freedom"].get("must_surface_review_items", []),
            "La ruta histórica de libertad debe conservar visible la autodeterminación de Aquiles",
        )
        aquiles_inferred_relations = {
            "rel.ego_aq.differs_caos_process",
            "rel.dissociation_aq.differs_aa1",
            "rel.selfdetermination_aq.reframes_aa3",
            "rel.freedom_aq.differs_aa5",
            "rel.responsibility_aq.differs_aa4",
            "rel.narrative_identity_aq.differs_aa1",
            "rel.borrowed_egolatry_aq.overlaps_masquerade_aa3",
        }
        require(
            all(
                relation_id in relations
                and relations[relation_id]["evidence_status"] == "inferred"
                and bool(relations[relation_id].get("rationale"))
                for relation_id in aquiles_inferred_relations
            ),
            "Los cruces históricos de Aquiles deben seguir explícitamente marcados como inferidos",
        )
        require(
            nodes["formulation.dissociation.aq"].get("subject") == "concept.disociacion_ego",
            "La formulación de disociación de Aquiles debe conservarse como formulación histórica del término compartido",
        )
        require(
            "no diagnóstica" in nodes["formulation.dissociation.aq"].get("summary", ""),
            "El mapa no puede convertir la disociación filosófica de Aquiles en diagnóstico clínico",
        )

        # Invariantes ganadas al integrar El juego de las máscaras sistemáticamente en F2.
        require("MASCARAS" in works, "Falta El juego de las máscaras en el registro de obras")
        masks_structure_path = (
            ROOT
            / "corpus"
            / "libros"
            / "juego-de-las-mascaras"
            / "estructura.json"
        )
        require(masks_structure_path.exists(), "Falta la estructura derivada de El juego de las máscaras")
        masks_structure = json.loads(masks_structure_path.read_text(encoding="utf-8"))
        require(
            masks_structure.get("sha256") == works["MASCARAS"]["sha256"],
            "La estructura de El juego de las máscaras no corresponde al hash de la fuente canónica",
        )
        require(
            masks_structure.get("source") == works["MASCARAS"]["source"],
            "La ruta canónica de El juego de las máscaras debe conservarse sin sustituciones editoriales",
        )
        masks_segments = {
            segment["path"]: (segment["start_line"], segment["end_line"])
            for segment in masks_structure["segments"]
        }
        require(
            len(masks_segments) == 14,
            "La estructura de El juego de las máscaras debe conservar preliminares, prólogo, diez capítulos, epílogo y glosario",
        )
        masks_evidence = [ev for ev in evidence.values() if ev["work_id"] == "MASCARAS"]
        masks_covered_segments = {ev["segment"] for ev in masks_evidence}
        require(
            set(masks_segments) <= masks_covered_segments,
            "La auditoría de El juego de las máscaras debe cubrir sus catorce segmentos; faltan: "
            f"{sorted(set(masks_segments) - masks_covered_segments)}",
        )
        require(
            len(masks_evidence) >= 59,
            "La auditoría semántica de El juego de las máscaras perdió granularidad: "
            f"{len(masks_evidence)} evidencias",
        )
        for ev in masks_evidence:
            require(
                ev["segment"] in masks_segments,
                f"{ev['id']}: segmento de El juego de las máscaras no declarado en estructura.json",
            )
            segment_start, segment_end = masks_segments[ev["segment"]]
            line_start, line_end = ev["source_lines"]
            require(
                segment_start <= line_start <= line_end <= segment_end,
                f"{ev['id']}: rango fuera del segmento declarado {ev['segment']}",
            )

        required_masks_nodes = {
            "formulation.scope.mask",
            "concept.mask.mask",
            "concept.social_code.mask",
            "concept.modulation.mask",
            "concept.substitution.mask",
            "concept.ontological_masking.mask",
            "concept.mask_institution.mask",
            "concept.will_operator.mask",
            "formal.first_formula.mask",
            "formal.second_formula.mask",
            "concept.factical_sum.mask",
            "concept.identity_dysphoria.mask",
            "formulation.dysphoria_modes.mask",
            "formulation.dissociation.mask",
            "concept.productive_grief.mask",
            "concept.obsessive_grief.mask",
            "formulation.catharsis.mask",
            "formulation.identity.mask",
            "concept.own_bias.mask",
            "concept.implanted_bias.mask",
            "formulation.identity_inertia.mask",
            "formulation.odysseus.mask",
            "concept.nobody_transit.mask",
            "concept.surrender.mask",
            "formulation.surrender_paradox.mask",
            "concept.own_time.mask",
            "concept.genuine_collapse.mask",
            "concept.sovereign_vanity.mask",
            "concept.ontological_equality.mask",
            "concept.encounter_without_negotiation.mask",
            "concept.presence_without_program.mask",
            "formulation.ethical_ontological_planes.mask",
            "concept.causal_imputation.mask",
            "formulation.responsibility.mask",
            "formulation.penalty_time.mask",
            "formulation.damage_scope.mask",
            "concept.collective_bias.mask",
            "concept.collective_ego.mask",
            "concept.collective_dysphoria.mask",
            "concept.institutional_mask.mask",
            "concept.collective_surrender.mask",
            "formulation.story_release.mask",
        }
        require(
            required_masks_nodes <= set(nodes),
            "Núcleo de El juego de las máscaras incompleto; faltan nodos: "
            f"{sorted(required_masks_nodes - set(nodes))}",
        )

        required_masks_routes = {
            "route.mask.scope",
            "route.mask.institution_formulas",
            "route.mask.dysphoria_dissociation",
            "route.mask.grief_catharsis",
            "route.mask.identity_bias",
            "route.mask.odysseus",
            "route.mask.surrender",
            "route.mask.sovereign_vanity",
            "route.mask.encounter",
            "route.mask.causal_imputation",
            "route.mask.collective",
            "route.mask.epilogue_glossary",
            "route.mask.crosswork_history",
        }
        require(
            required_masks_routes <= set(routes),
            "Rutas de El juego de las máscaras incompletas: "
            f"{sorted(required_masks_routes - set(routes))}",
        )

        masks_reviews = {
            "review.mask.universal_masking",
            "review.mask.clinical_boundary",
            "review.mask.formula_crosswalk",
            "review.mask.will_opportunity",
            "review.mask.dysphoria_crosswalk",
            "review.mask.dissociation_crosswalk",
            "review.mask.ego_persistence",
            "review.mask.grief_claims",
            "review.mask.therapy_claims",
            "review.mask.identity_ownership",
            "review.mask.identity_ego_inertia",
            "review.mask.myth_sources",
            "review.mask.series_order",
            "review.mask.surrender_paradox",
            "review.mask.vanity_term",
            "review.mask.relational_claims",
            "review.mask.equality_crosswalk",
            "review.mask.responsibility_crosswalk",
            "review.mask.legal_dolo",
            "review.mask.causal_necessity",
            "review.mask.penalty_time",
            "review.mask.damage_measure",
            "review.mask.disassociated_culpability",
            "review.mask.collective_agent",
            "review.mask.collective_scale",
            "review.mask.collective_crosswalk",
            "review.mask.nonaction_responsibility",
            "review.mask.political_generalization",
            "review.mask.editorial_notation",
        }
        require(
            masks_reviews <= set(reviews),
            "Deben conservarse las veintinueve revisiones pendientes de El juego de las máscaras",
        )
        require(
            {
                "review.mask.universal_masking",
                "review.mask.formula_crosswalk",
                "review.mask.will_opportunity",
                "review.mask.identity_ego_inertia",
            }
            <= set(routes["route.mask.institution_formulas"].get("must_surface_review_items", [])),
            "La ruta máscara-fórmulas debe conservar universalización, cambio formal, voluntad e inercia",
        )
        require(
            {
                "review.mask.clinical_boundary",
                "review.mask.dysphoria_crosswalk",
                "review.mask.dissociation_crosswalk",
                "review.mask.ego_persistence",
                "review.mask.grief_claims",
            }
            <= set(routes["route.mask.dysphoria_dissociation"].get("must_surface_review_items", [])),
            "La ruta de disforia debe conservar alcance, homónimos, persistencia y criterio del duelo",
        )
        require(
            {
                "review.mask.clinical_boundary",
                "review.mask.grief_claims",
                "review.mask.therapy_claims",
                "review.mask.ego_persistence",
            }
            <= set(routes["route.mask.grief_catharsis"].get("must_surface_review_items", [])),
            "La ruta duelo-catarsis debe conservar todas sus reservas clínicas y empíricas",
        )
        require(
            {
                "review.mask.will_opportunity",
                "review.mask.identity_ownership",
                "review.mask.identity_ego_inertia",
                "review.mask.dysphoria_crosswalk",
            }
            <= set(routes["route.mask.identity_bias"].get("must_surface_review_items", [])),
            "La ruta identidad-sesgo debe conservar propiedad, circularidad, velocidad e historia",
        )
        require(
            {
                "review.mask.responsibility_crosswalk",
                "review.mask.legal_dolo",
                "review.mask.causal_necessity",
                "review.mask.penalty_time",
                "review.mask.damage_measure",
                "review.mask.disassociated_culpability",
                "review.mask.nonaction_responsibility",
            }
            <= set(routes["route.mask.causal_imputation"].get("must_surface_review_items", [])),
            "La ruta de imputación debe conservar todas sus reservas causales, legales, metrológicas y normativas",
        )
        require(
            {
                "review.mask.collective_agent",
                "review.mask.collective_scale",
                "review.mask.collective_crosswalk",
                "review.mask.political_generalization",
                "review.mask.nonaction_responsibility",
                "review.mask.causal_necessity",
            }
            <= set(routes["route.mask.collective"].get("must_surface_review_items", [])),
            "La ruta colectiva debe conservar agencia, escala, cruces, política y causalidad",
        )
        require(
            {
                "review.mask.formula_crosswalk",
                "review.mask.dysphoria_crosswalk",
                "review.mask.dissociation_crosswalk",
                "review.mask.identity_ego_inertia",
                "review.mask.responsibility_crosswalk",
                "review.mask.collective_crosswalk",
                "review.mask.equality_crosswalk",
            }
            <= set(routes["route.mask.crosswork_history"].get("must_surface_review_items", [])),
            "La ruta histórica de Máscaras no puede ocultar diferencias ontológicas o jurídicas",
        )
        require(
            {"review.mask.formula_crosswalk", "review.mask.identity_ego_inertia"}
            <= set(routes["route.ego.explicacion"].get("must_surface_review_items", [])),
            "La ruta general del ego debe incorporar el cambio formal de Máscaras",
        )
        require(
            {
                "review.mask.dysphoria_crosswalk",
                "review.mask.dissociation_crosswalk",
                "review.mask.identity_ownership",
            }
            <= set(routes["route.aa1.identity_distortions"].get("must_surface_review_items", [])),
            "La ruta de identidad y perturbaciones debe incorporar las formulaciones de Máscaras",
        )
        require(
            {
                "review.mask.responsibility_crosswalk",
                "review.mask.legal_dolo",
                "review.mask.causal_necessity",
                "review.mask.penalty_time",
            }
            <= set(routes["route.aa4.responsibility_causality"].get("must_surface_review_items", [])),
            "La ruta histórica de responsabilidad debe conservar la extensión penal de Máscaras",
        )
        require(
            {"review.mask.collective_agent", "review.mask.collective_crosswalk"}
            <= set(routes["route.aa4.corporate_ego"].get("must_surface_review_items", [])),
            "La ruta del ego corporativo debe conservar la diferencia del ego colectivo de Máscaras",
        )
        require(
            {"review.mask.dysphoria_crosswalk", "review.mask.dissociation_crosswalk", "review.mask.ego_persistence"}
            <= set(routes["route.aq.dissociation_fall"].get("must_surface_review_items", [])),
            "La ruta de Aquiles debe surfacer la disociación anestesiada posterior",
        )
        masks_inferred_relations = {
            "rel.formula_mask.differs_core_order",
            "rel.identity_mask.elaborates_aa1_bias",
            "rel.dysphoria_mask.differs_aa1",
            "rel.dissociation_mask.differs_aquiles",
            "rel.identity_inertia_mask.differs_ego_integral",
            "rel.responsibility_mask.reframes_aa4",
            "rel.responsibility_mask.differs_aquiles",
            "rel.collective_ego_mask.differs_aa3",
            "rel.collective_ego_mask.differs_aa4",
            "rel.ontological_equality_mask.differs_aa5",
            "rel.collective_bias_mask.differs_rstar",
        }
        require(
            all(
                relation_id in relations
                and relations[relation_id]["evidence_status"] == "inferred"
                and bool(relations[relation_id].get("rationale"))
                for relation_id in masks_inferred_relations
            ),
            "Los cruces históricos de Máscaras deben seguir marcados como inferidos",
        )
        require(
            nodes["formal.first_formula.mask"]["formal_spec"].get("expression")
            == "Sesgo → Voluntad → Primera mediación → Acto → Segunda mediación → Ego",
            "La primera fórmula publicada por Máscaras debe conservarse literalmente hasta revisión",
        )
        require(
            nodes["formal.second_formula.mask"]["formal_spec"].get("expression")
            == "Sesgo (suma fáctica) → Primera mediación → Acto → Segunda mediación → Ego disociado",
            "La segunda fórmula publicada por Máscaras debe conservarse literalmente hasta revisión",
        )
        require(
            nodes["formulation.dissociation.mask"].get("subject") == "concept.disociacion_ego",
            "La disociación de Máscaras debe conservarse como formulación histórica diferenciada",
        )

        # Invariantes ganadas al integrar El telar de las Moiras y cerrar F2.
        require("TELAR" in works, "Falta El telar de las Moiras en el registro de obras")
        telar_structure_path = (
            ROOT / "corpus" / "libros" / "telar-de-las-moiras" / "estructura.json"
        )
        require(telar_structure_path.exists(), "Falta la estructura derivada de El telar de las Moiras")
        telar_structure = json.loads(telar_structure_path.read_text(encoding="utf-8"))
        require(
            telar_structure.get("sha256") == works["TELAR"]["sha256"],
            "La estructura de El telar de las Moiras no corresponde al hash de la fuente canónica",
        )
        require(
            telar_structure.get("source") == works["TELAR"]["source"],
            "La ruta canónica de El telar de las Moiras debe conservarse sin sustituciones editoriales",
        )
        telar_segments = {
            segment["path"]: (segment["start_line"], segment["end_line"])
            for segment in telar_structure["segments"]
        }
        require(
            len(telar_segments) == 15,
            "La estructura de El telar debe conservar preliminares, presentación, diez capítulos, epílogo y dos apéndices",
        )
        telar_evidence = [ev for ev in evidence.values() if ev["work_id"] == "TELAR"]
        telar_covered_segments = {ev["segment"] for ev in telar_evidence}
        require(
            set(telar_segments) <= telar_covered_segments,
            "La auditoría de El telar debe cubrir sus quince segmentos; faltan: "
            f"{sorted(set(telar_segments) - telar_covered_segments)}",
        )
        require(
            len(telar_evidence) >= 88,
            "La auditoría semántica de El telar perdió granularidad: "
            f"{len(telar_evidence)} evidencias",
        )
        for ev in telar_evidence:
            require(
                ev["segment"] in telar_segments,
                f"{ev['id']}: segmento de El telar no declarado en estructura.json",
            )
            segment_start, segment_end = telar_segments[ev["segment"]]
            line_start, line_end = ev["source_lines"]
            require(
                segment_start <= line_start <= line_end <= segment_end,
                f"{ev['id']}: rango fuera del segmento declarado {ev['segment']}",
            )

        required_telar_nodes = {
            "formulation.scope.telar",
            "concept.autodetermination.telar",
            "formulation.identity_process.telar",
            "concept.existential_anesthesia.telar",
            "concept.indirect_listening.telar",
            "concept.ego_reference.telar",
            "formulation.ego_distinctions.telar",
            "concept.ego_resistance.telar",
            "formulation.being_condition.telar",
            "concept.ego_permanence.telar",
            "concept.identity_content.telar",
            "formulation.argos.telar",
            "concept.emotional_map.telar",
            "formulation.melancholy_knowledge.telar",
            "concept.ego_mediation.telar",
            "formulation.being_before_thought.telar",
            "concept.otherness.telar",
            "concept.ontological_equality.telar",
            "concept.ego_measure.telar",
            "concept.eternal_return.telar",
            "formulation.relational_closure.telar",
            "formulation.justice_retribution.telar",
            "concept.memento_mori.telar",
            "concept.relational_coherence.telar",
            "concept.fiscal_contract.telar",
            "formulation.rights_conditions.telar",
            "formulation.state_breach.telar",
            "concept.dignity.telar",
            "formulation.law_morality.telar",
            "formulation.banality.telar",
            "concept.expanded_judgment.telar",
            "concept.conflict_discomfort.telar",
            "formulation.reaction_responsibility.telar",
            "concept.ontological_limit.telar",
            "concept.non_annulment_ethics.telar",
            "concept.ethical_conflict_resolution.telar",
            "formulation.false_resolutions.telar",
            "formulation.conflict_attitudes.telar",
            "concept.respect.telar",
            "concept.self_respect.telar",
            "formulation.respect_agency.telar",
            "formulation.relationship_nonuse.telar",
            "formulation.law_as_respect.telar",
            "concept.fear_submission.telar",
            "formulation.forgiveness_modes.telar",
            "concept.forgiveness_release.telar",
            "formulation.restorative_forgiveness.telar",
            "concept.love_catastrophe.telar",
            "concept.affective_selfdetermination.telar",
            "formulation.self_love.telar",
            "concept.domestication.telar",
            "formulation.love_modification.telar",
            "formulation.separation.telar",
            "formulation.love_act.telar",
            "concept.existential_anguish.telar",
            "formulation.freedom_response.telar",
            "formulation.responsibility_remainder.telar",
            "formulation.limit_autobiography.telar",
            "formulation.anguish_evasions.telar",
            "concept.false_ego.telar",
            "formulation.achilles.telar",
            "formulation.odysseus.telar",
            "concept.authentic_ego.telar",
            "formulation.cave_selfknowledge.telar",
            "formulation.experience_understanding.telar",
            "concept.ontological_empathy.telar",
            "formulation.nonviolence.telar",
            "formulation.pain_boundary.telar",
            "formulation.knowing_other.telar",
            "formulation.practice.telar",
        }
        require(
            required_telar_nodes <= set(nodes),
            "Núcleo de El telar incompleto; faltan nodos: "
            f"{sorted(required_telar_nodes - set(nodes))}",
        )

        required_telar_routes = {
            "route.telar.scope",
            "route.telar.identity_ego_being",
            "route.telar.otherness_equality",
            "route.telar.fiscal_dignity",
            "route.telar.conflict_limits",
            "route.telar.respect",
            "route.telar.fear_forgiveness",
            "route.telar.love",
            "route.telar.anguish_false_ego",
            "route.telar.cave_empathy",
            "route.telar.epilogue_glossary",
            "route.telar.interlocutors",
            "route.telar.crosswork_history",
        }
        require(
            required_telar_routes <= set(routes),
            "Rutas de El telar incompletas: "
            f"{sorted(required_telar_routes - set(routes))}",
        )

        telar_reviews = {
            "review.telar.scope_prescription",
            "review.telar.architecture_consistency",
            "review.telar.selfdetermination_crosswalk",
            "review.telar.ego_crosswalk",
            "review.telar.identity_crosswalk",
            "review.telar.continuity_claims",
            "review.telar.emotion_epistemology",
            "review.telar.equality_dignity",
            "review.telar.social_generalizations",
            "review.telar.eternal_return_normativity",
            "review.telar.justice_retribution",
            "review.telar.fiscal_crosswalk",
            "review.telar.fiscal_legal_basis",
            "review.telar.fiscal_damage",
            "review.telar.dignity_scope",
            "review.telar.law_model",
            "review.telar.arendt_attribution",
            "review.telar.conflict_reaction",
            "review.telar.conflict_generalization",
            "review.telar.limit_permission",
            "review.telar.respect_agency",
            "review.telar.forgiveness_order",
            "review.telar.forgiveness_normativity",
            "review.telar.collective_forgiveness",
            "review.telar.love_generalizations",
            "review.telar.love_ego_modification",
            "review.telar.clinical_boundary",
            "review.telar.animal_agency",
            "review.telar.responsibility_constraints",
            "review.telar.myth_sources",
            "review.telar.empathy_claims",
            "review.telar.nonviolence_inference",
            "review.telar.cave_attribution",
            "review.telar.editorial_notation",
            "review.telar.appendix_consistency",
        }
        require(
            telar_reviews <= set(reviews),
            "Deben conservarse las treinta y cinco revisiones pendientes de El telar",
        )
        require(
            {
                "review.telar.selfdetermination_crosswalk",
                "review.telar.ego_crosswalk",
                "review.telar.identity_crosswalk",
                "review.telar.continuity_claims",
                "review.telar.emotion_epistemology",
                "review.telar.love_ego_modification",
            }
            <= set(routes["route.telar.identity_ego_being"].get("must_surface_review_items", [])),
            "La ruta identidad-ego-ser debe conservar cruces, continuidad, emociones y modificación amorosa",
        )
        require(
            {
                "review.telar.fiscal_crosswalk",
                "review.telar.fiscal_legal_basis",
                "review.telar.fiscal_damage",
                "review.telar.dignity_scope",
                "review.telar.equality_dignity",
                "review.telar.law_model",
                "review.telar.arendt_attribution",
            }
            <= set(routes["route.telar.fiscal_dignity"].get("must_surface_review_items", [])),
            "La ruta fiscal-dignidad debe conservar todos sus límites doctrinales, jurídicos y metrológicos",
        )
        require(
            {
                "review.telar.conflict_reaction",
                "review.telar.conflict_generalization",
                "review.telar.limit_permission",
                "review.telar.respect_agency",
                "review.telar.nonviolence_inference",
            }
            <= set(routes["route.telar.conflict_limits"].get("must_surface_review_items", [])),
            "La ruta conflicto-límite debe conservar agencia, causalidad y puente normativo",
        )
        require(
            {
                "review.aq.forgiveness_order",
                "review.aq.forgiveness_normativity",
                "review.telar.forgiveness_order",
                "review.telar.forgiveness_normativity",
                "review.telar.collective_forgiveness",
                "review.telar.arendt_attribution",
            }
            <= set(routes["route.telar.fear_forgiveness"].get("must_surface_review_items", [])),
            "La ruta miedo-perdón debe conservar secuencia, normatividad, escala y atribución",
        )
        require(
            {
                "review.telar.love_generalizations",
                "review.telar.love_ego_modification",
                "review.telar.clinical_boundary",
                "review.telar.scope_prescription",
            }
            <= set(routes["route.telar.love"].get("must_surface_review_items", [])),
            "La ruta del amor debe conservar generalización, niveles del ego y alcance clínico",
        )
        require(
            {
                "review.telar.clinical_boundary",
                "review.telar.animal_agency",
                "review.telar.responsibility_constraints",
                "review.telar.myth_sources",
                "review.telar.ego_crosswalk",
                "review.telar.selfdetermination_crosswalk",
            }
            <= set(routes["route.telar.anguish_false_ego"].get("must_surface_review_items", [])),
            "La ruta angustia-falso ego debe conservar clínica, agencia, responsabilidad, mito y cruces",
        )
        require(
            {
                "review.telar.empathy_claims",
                "review.telar.nonviolence_inference",
                "review.telar.cave_attribution",
                "review.telar.scope_prescription",
            }
            <= set(routes["route.telar.cave_empathy"].get("must_surface_review_items", [])),
            "La ruta caverna-empatía debe conservar epistemología, atribución y puente normativo",
        )
        require(
            {
                "review.telar.selfdetermination_crosswalk",
                "review.telar.ego_crosswalk",
                "review.telar.identity_crosswalk",
                "review.telar.fiscal_crosswalk",
                "review.telar.forgiveness_order",
                "review.telar.collective_forgiveness",
                "review.telar.myth_sources",
                "review.telar.responsibility_constraints",
            }
            <= set(routes["route.telar.crosswork_history"].get("must_surface_review_items", [])),
            "La ruta histórica de El telar no puede ocultar cruces ontológicos, jurídicos o mitográficos",
        )
        require(
            {
                "review.telar.selfdetermination_crosswalk",
                "review.telar.ego_crosswalk",
                "review.telar.identity_crosswalk",
            }
            <= set(routes["route.ego.explicacion"].get("must_surface_review_items", [])),
            "La ruta general del ego debe incorporar las formulaciones de El telar",
        )
        require(
            {"review.telar.ego_crosswalk", "review.telar.identity_crosswalk"}
            <= set(routes["route.caos.subject_ego_identity"].get("must_surface_review_items", [])),
            "La ruta sujeto-ego-identidad debe conservar la separación tardía de El telar",
        )
        require(
            {"review.telar.identity_crosswalk", "review.telar.ego_crosswalk"}
            <= set(routes["route.aa1.identity_distortions"].get("must_surface_review_items", [])),
            "La ruta histórica de identidad debe incorporar El telar",
        )
        require(
            {"review.telar.fiscal_crosswalk", "review.telar.fiscal_legal_basis", "review.telar.fiscal_damage"}
            <= set(routes["route.aa5.collective_contract"].get("must_surface_review_items", [])),
            "La ruta histórica del contrato fiscal debe incorporar El telar",
        )
        require(
            {"review.telar.forgiveness_order", "review.telar.forgiveness_normativity", "review.telar.collective_forgiveness"}
            <= set(routes["route.aq.fear_forgiveness"].get("must_surface_review_items", [])),
            "La ruta histórica del perdón debe incorporar El telar",
        )

        telar_inferred_relations = {
            "rel.selfdetermination_telar.differs_caos_ego",
            "rel.selfdetermination_telar.reframes_aa3",
            "rel.identity_telar.differs_caos",
            "rel.identity_telar.differs_aa1",
            "rel.identity_telar.differs_aquiles",
            "rel.identity_telar.differs_masks",
            "rel.ego_telar.differs_integral",
            "rel.ego_telar.differs_masks_inertia",
            "rel.equality_telar.differs_aa5",
            "rel.fiscal_telar.reframes_aa3",
            "rel.fiscal_telar.differs_aa4",
            "rel.fiscal_telar.elaborates_aa5",
            "rel.forgiveness_telar.elaborates_aquiles",
            "rel.achilles_telar.reframes_aquiles",
            "rel.false_ego_telar.differs_dissociation_aquiles",
            "rel.responsibility_telar.differs_aa4",
            "rel.responsibility_telar.differs_masks",
        }
        require(
            all(
                relation_id in relations
                and relations[relation_id]["evidence_status"] == "inferred"
                and bool(relations[relation_id].get("rationale"))
                for relation_id in telar_inferred_relations
            ),
            "Los cruces históricos de El telar deben seguir marcados como inferidos",
        )
        require(
            {"ev.telar.ch7.political", "ev.telar.ch7.synthesis"}
            <= set(nodes["formulation.restorative_forgiveness.telar"].get("evidence", [])),
            "La formulación restaurativa debe conservar juntas las dos secuencias incompatibles",
        )
        require(
            "review.telar.forgiveness_order"
            in routes["route.telar.fear_forgiveness"].get("must_surface_review_items", []),
            "La contradicción de orden entre perdón y justicia debe permanecer visible",
        )

    # Invariantes ganadas al integrar La transformación formal en F3.
    if phase in {"F3", "F4", "F5", "MANT"}:
        tf_structure_path = (
            ROOT / "corpus" / "libros" / "transformacion-formal" / "estructura.json"
        )
        require(tf_structure_path.exists(), "Falta la estructura derivada de La transformación formal")
        tf_structure = json.loads(tf_structure_path.read_text(encoding="utf-8"))
        tf_segments = {
            segment["path"]: (segment["start_line"], segment["end_line"])
            for segment in tf_structure["segments"]
        }
        tf_evidence = [
            ev for ev in evidence.values() if ev["work_id"] == "TRANSFORMACION-FORMAL"
        ]
        tf_covered_segments = {ev["segment"] for ev in tf_evidence}
        require(
            set(tf_segments) <= tf_covered_segments,
            "La auditoría de La transformación formal debe cubrir preliminares, prólogo, "
            "dieciséis capítulos y epílogo; faltan: "
            f"{sorted(set(tf_segments) - tf_covered_segments)}",
        )
        require(
            len(tf_evidence) >= 100,
            "La auditoría semántica de La transformación formal perdió granularidad: "
            f"{len(tf_evidence)} evidencias",
        )
        for ev in tf_evidence:
            require(
                ev["segment"] in tf_segments,
                f"{ev['id']}: segmento de La transformación formal no declarado en estructura.json",
            )
            segment_start, segment_end = tf_segments[ev["segment"]]
            line_start, line_end = ev["source_lines"]
            require(
                segment_start <= line_start <= line_end <= segment_end,
                f"{ev['id']}: rango fuera del segmento declarado {ev['segment']}",
            )

        required_tf_nodes = {
            "formal.tf.v_t",
            "formal.tf.c",
            "formal.tf.phi1",
            "formal.tf.phi2",
            "formal.tf.I",
            "formal.tf.w",
            "formal.tf.G",
            "formal.tf.rstar",
            "formal.tf.rstar_net",
            "formal.tf.S",
            "formal.tf.alpha",
            "formal.tf.delta",
            "formal.tf.rstar_b",
            "formal.tf.delta_b",
            "formal.tf.I_col",
            "formal.tf.IIC",
            "formal.tf.w_adjusted",
            "formal.tf.P_children",
            "formal.tf.S_interval",
            "formal.tf.rstar_net_interval",
            "formal.tf.delta_interval",
            "formal.tf.priority_criterion",
            "formal.tf.T_i",
            "formal.tf.delta_net",
            "formal.tf.feedback_alpha",
            "formal.tf.robustness_extended",
            "formulation.aego.tf",
            "formulation.tf.state_ego",
            "formulation.tf.rights_phi2",
            "formulation.tf.sdo_axes_crosswalk",
            "concept.tf.collective_ego",
            "concept.tf.uncertainty_calibration",
            "concept.tf.volume2_program",
        }
        require(
            required_tf_nodes <= set(nodes),
            "Núcleo de La transformación formal incompleto; faltan nodos: "
            f"{sorted(required_tf_nodes - set(nodes))}",
        )
        tf_formal_nodes = {
            node_id for node_id in required_tf_nodes if node_id.startswith("formal.tf.")
        }
        for node_id in tf_formal_nodes:
            spec = nodes[node_id].get("formal_spec", {})
            require(
                bool(spec.get("object_type"))
                and bool(spec.get("epistemic_status"))
                and bool(spec.get("ontological_correspondence")),
                f"{node_id}: debe conservar tipo, estatuto epistémico y correspondencia ontológica",
            )

        required_tf_routes = {
            "route.tf.architecture",
            "route.tf.formulas_crosswalk",
            "route.tf.identity_claim",
            "route.tf.rstar",
            "route.tf.s",
            "route.tf.alpha",
            "route.tf.delta_aego",
            "route.tf.collective_iic",
            "route.tf.iic_adjustment",
            "route.tf.state_fiscal",
            "route.tf.uncertainty",
            "route.tf.limits",
            "route.tf.sdo",
            "route.tf.eco",
            "route.tf.implementation",
        }
        require(
            required_tf_routes <= set(routes),
            "Rutas de La transformación formal incompletas: "
            f"{sorted(required_tf_routes - set(routes))}",
        )

        required_tf_reviews = {
            "review.tf.proof_status",
            "review.tf.phi1_typing",
            "review.tf.phi2_typing",
            "review.tf.rstar_orientation",
            "review.tf.normalization_completeness",
            "review.tf.s_weights",
            "review.tf.alpha_comparability",
            "review.tf.aego_crosswalk",
            "review.tf.iic_correlation",
            "review.tf.iic_aego_reverse",
            "review.tf.w_adjustment_bounds",
            "review.tf.adjustment_variants",
            "review.tf.state_force_alpha",
            "review.tf.fiscal_function",
            "review.tf.interval_dependencies",
            "review.tf.vertex_robustness",
            "review.tf.priority_formula",
            "review.tf.eco_clinical_safety",
            "review.tf.feedback_freedom",
            "review.tf.volume2_validation",
        }
        require(
            required_tf_reviews <= set(reviews),
            "Deben conservarse las revisiones formales, doctrinales y empíricas de "
            "La transformación formal",
        )
        require(
            {
                "review.tf.rstar_orientation",
                "review.tf.rstar_target_centrality",
                "review.tf.pf_epsilon",
                "review.tf.normalization_completeness",
                "review.tf.rnet_redistribution",
            }
            <= set(routes["route.tf.rstar"].get("must_surface_review_items", [])),
            "La ruta de R* en La transformación formal debe surfacer sus problemas formales",
        )
        require(
            {
                "review.tf.probability_calibration",
                "review.tf.interval_mixture",
                "review.tf.interval_dependencies",
                "review.tf.vertex_robustness",
                "review.tf.priority_formula",
            }
            <= set(routes["route.tf.uncertainty"].get("must_surface_review_items", [])),
            "La ruta de incertidumbre debe surfacer límites de intervalos y robustez",
        )
        require(
            {
                "review.tf.rstar_orientation",
                "review.tf.phi1_typing",
                "review.tf.phi2_typing",
                "review.tf.adjustment_variants",
                "review.tf.delta_thresholds",
                "review.tf.volume2_validation",
            }
            <= set(routes["route.tf.implementation"].get("must_surface_review_items", [])),
            "La ruta de implementación no puede ocultar formalizaciones no adjudicadas",
        )

        tf_crosswork_relations = {
            "rel.tf.vt.elaborates_children_aa2",
            "rel.tf.c.reframes_identity_aa1",
            "rel.tf.phi1.refines_aa2",
            "rel.tf.phi2.refines_aa2",
            "rel.tf.rstar.differs_axiom",
            "rel.tf.aego.reframes_aa1",
            "rel.tf.aego.reframes_aa3",
            "rel.tf.collective_ego.elaborates_aa4",
            "rel.tf.collective_ego.elaborates_aa5",
            "rel.tf.fiscal.elaborates_aa4",
            "rel.tf.state_ego.elaborates_aa5",
            "rel.tf.hume.elaborates_aa5",
            "rel.tf.rights.reframes_aa5",
            "rel.tf.rights.differs_telar",
            "rel.tf.imputation.elaborates_aa4",
            "rel.tf.imputation.elaborates_masks",
            "rel.tf.identity.differs_telar",
            "rel.tf.derivative.reframes_aa4",
            "rel.tf.sdo.extends_aego_sdo",
            "rel.tf.fiscal_function.elaborates_contract",
        }
        require(
            all(
                relation_id in relations
                and relations[relation_id]["evidence_status"] == "inferred"
                and bool(relations[relation_id].get("rationale"))
                for relation_id in tf_crosswork_relations
            ),
            "Los cruces históricos de La transformación formal con F2 deben seguir "
            "marcados como inferidos",
        )
        require(
            nodes["formal.tf.rstar"]["formal_spec"].get("expression")
            == "W·R*=λ_max·R*; Σ_i R*_i=1",
            "No debe armonizarse silenciosamente la orientación W de R* en Transformación formal",
        )
        require(
            relations["rel.tf.rstar.differs_axiom"]["evidence_status"] == "inferred",
            "La diferencia W/Wᵀ debe conservarse como cruce analítico no adjudicado",
        )
        require(
            {
                "review.tf.aego_crosswalk",
                "review.tf.aego_clinical",
            }
            <= set(routes["route.aego.definicion_evolucion"].get("must_surface_review_items", [])),
            "La ruta histórica de Aego debe incorporar la reformulación de F3",
        )

    print(
        "Mapa válido:",
        f"fase={phase}, schema={schema_status};",
        f"{len(works)} obras,",
        f"{len(evidence)} evidencias,",
        f"{len(nodes)} nodos,",
        f"{len(relations)} relaciones,",
        f"{len(routes)} rutas,",
        f"{len(reviews)} revisiones pendientes,",
        f"{len(tests)} pruebas F1 preservadas,",
        f"{len([ev for ev in evidence.values() if ev['work_id'] == 'CAOS'])} evidencias de Caos,",
        f"{len([ev for ev in evidence.values() if ev['work_id'] == 'AA-I'])} evidencias de Afrodita Areia I,",
        f"{len([ev for ev in evidence.values() if ev['work_id'] == 'AA-II'])} evidencias de Afrodita Areia II,",
        f"{len([ev for ev in evidence.values() if ev['work_id'] == 'AA-III'])} evidencias de Afrodita Areia III,",
        f"{len([ev for ev in evidence.values() if ev['work_id'] == 'AA-IV'])} evidencias de Afrodita Areia IV,",
        f"{len([ev for ev in evidence.values() if ev['work_id'] == 'AA-V'])} evidencias de Afrodita Areia V,",
        f"{len([ev for ev in evidence.values() if ev['work_id'] == 'AQUILES'])} evidencias de El dilema de Aquiles,",
        f"{len([ev for ev in evidence.values() if ev['work_id'] == 'MASCARAS'])} evidencias de El juego de las máscaras,",
        f"{len([ev for ev in evidence.values() if ev['work_id'] == 'TELAR'])} evidencias de El telar de las Moiras,",
        f"{len([ev for ev in evidence.values() if ev['work_id'] == 'TRANSFORMACION-FORMAL'])} evidencias de La transformación formal."
    )
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValidationError, json.JSONDecodeError, KeyError, TypeError) as exc:
        print(f"ERROR DE VALIDACIÓN: {exc}", file=sys.stderr)
        raise SystemExit(1)
