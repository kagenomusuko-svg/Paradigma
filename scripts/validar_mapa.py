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

        axiom_structure_path = (
            ROOT / "corpus" / "libros" / "axiomatizacion-doble-mediacion" / "estructura.json"
        )
        require(axiom_structure_path.exists(), "Falta la estructura derivada de Axiomatización")
        axiom_structure = json.loads(axiom_structure_path.read_text(encoding="utf-8"))
        axiom_segments = {
            segment["path"]: (segment["start_line"], segment["end_line"])
            for segment in axiom_structure["segments"]
        }
        axiom_evidence = [ev for ev in evidence.values() if ev["work_id"] == "AXIOM-SDM"]
        axiom_covered_segments = {ev["segment"] for ev in axiom_evidence}
        require(
            set(axiom_segments) <= axiom_covered_segments,
            "La auditoría de Axiomatización debe cubrir preliminares, prólogo, once partes "
            "y cuatro apéndices; faltan: "
            f"{sorted(set(axiom_segments) - axiom_covered_segments)}",
        )
        require(
            len(axiom_evidence) >= 80,
            "La auditoría semántica de Axiomatización perdió granularidad: "
            f"{len(axiom_evidence)} evidencias",
        )
        for ev in axiom_evidence:
            require(
                ev["segment"] in axiom_segments,
                f"{ev['id']}: segmento de Axiomatización no declarado en estructura.json",
            )
            segment_start, segment_end = axiom_segments[ev["segment"]]
            line_start, line_end = ev["source_lines"]
            require(
                segment_start <= line_start <= line_end <= segment_end,
                f"{ev['id']}: rango fuera del segmento declarado {ev['segment']}",
            )

        required_axiom_nodes = {
            "formal.axiom.E",
            "formal.axiom.emb",
            "formal.axiom.collapse",
            "formal.phi1",
            "formal.phi2",
            "formal.I_t",
            "formal.axiom.RSC",
            "formal.axiom.Sop",
            "formal.axiom.Sest",
            "formal.axiom.gbridge",
            "formal.alpha",
            "formal.axiom.alpha_discrete",
            "formal.delta",
            "formal.G",
            "formal.W",
            "formal.rstar",
            "formal.axiom.Wepsilon",
            "formal.axiom.rstar_interval",
            "formal.axiom.REC",
            "formal.axiom.TIC",
            "formal.axiom.Iinv",
            "formal.axiom.MP",
            "formal.axiom.closure",
            "formal.axiom.Id",
            "formal.axiom.rstar_net",
            "formal.axiom.delta_net",
            "formal.axiom.counterfactual",
            "formal.axiom.impact",
            "formulation.axiom.consistency",
            "formulation.axiom.mode_ranges",
            "formulation.axiom.annona",
            "concept.axiom.bifurcation",
            "method.axiom.calibration",
            "method.axiom.case_verification",
        }
        require(
            required_axiom_nodes <= set(nodes),
            "Núcleo de Axiomatización incompleto; faltan nodos: "
            f"{sorted(required_axiom_nodes - set(nodes))}",
        )
        axiom_formal_nodes = {
            node_id
            for node_id in required_axiom_nodes
            if node_id.startswith("formal.axiom.")
            or node_id in {"formal.phi1", "formal.phi2", "formal.I_t", "formal.alpha", "formal.delta", "formal.G", "formal.W", "formal.rstar"}
        }
        for node_id in axiom_formal_nodes:
            spec = nodes[node_id].get("formal_spec", {})
            require(
                bool(spec.get("object_type"))
                and bool(spec.get("epistemic_status"))
                and bool(spec.get("ontological_correspondence")),
                f"{node_id}: debe conservar tipo, estatuto epistémico y correspondencia ontológica",
            )

        required_axiom_routes = {
            "route.axiom.architecture",
            "route.axiom.base_phi",
            "route.axiom.integral",
            "route.axiom.substitutability",
            "route.axiom.alpha_delta",
            "route.axiom.rstar",
            "route.axiom.rec",
            "route.axiom.tic",
            "route.axiom.predictability",
            "route.axiom.closure",
            "route.axiom.calibration",
            "route.axiom.extensions",
            "route.axiom.crosswork",
        }
        require(
            required_axiom_routes <= set(routes),
            "Rutas de Axiomatización incompletas: "
            f"{sorted(required_axiom_routes - set(routes))}",
        )
        required_axiom_reviews = {
            "review.axiom.hilbert_ontology",
            "review.axiom.embedding",
            "review.axiom.rsc_type",
            "review.axiom.irreversibility",
            "review.axiom.phi2_integration",
            "review.axiom.Sop_units",
            "review.axiom.Sest_KL",
            "review.axiom.S_bridge",
            "review.axiom.dirac",
            "review.axiom.alpha_forced",
            "review.axiom.alpha_sum",
            "review.axiom.delta_signal",
            "review.axiom.rstar_sink",
            "review.axiom.epsilon_dimension",
            "review.axiom.rstar_intervals",
            "review.axiom.fisher_model",
            "review.axiom.rec_factor",
            "review.axiom.rec_estimators",
            "review.axiom.tic_bound_E",
            "review.axiom.tic_bound_D",
            "review.axiom.tic_universality",
            "review.axiom.psi_domain",
            "review.axiom.Iinv_monotonicity",
            "review.axiom.MP_linearity",
            "review.axiom.closure",
            "review.axiom.perfect",
            "review.axiom.calibration_sources",
            "review.axiom.discrete_weights",
            "review.axiom.markov",
            "review.axiom.rstar_net_sign",
            "review.axiom.counterfactual_stability",
            "review.axiom.bifurcation",
        }
        require(
            required_axiom_reviews <= set(reviews),
            "Deben conservarse las revisiones formales, empíricas y editoriales de Axiomatización",
        )
        required_axiom_inferred_relations = {
            "rel.axiom.E.formalizes_caos",
            "rel.axiom.phi1.refines_tf",
            "rel.axiom.phi2.refines_tf",
            "rel.axiom.I.refines_tf",
            "rel.axiom.c.differs_tf_c",
            "rel.axiom.modes.reframe_tf_children",
            "rel.axiom.Sop.refines_tf_S",
            "rel.axiom.alpha.differs_tf_alpha",
            "rel.axiom.alpha_forced.contradicts_tf",
            "rel.axiom.delta.refines_tf",
            "rel.axiom.REC.formalizes_tf_limits",
            "rel.axiom.TIC.formalizes_tf_imputation",
            "rel.axiom.annona.elaborates_aa4",
            "rel.axiom.MP.operationalizes_tf_future",
            "rel.axiom.closure.formalizes_caos",
            "rel.axiom.rstar_net.replaces_tf_rnet",
        }
        require(
            all(
                relation_id in relations
                and relations[relation_id]["evidence_status"] == "inferred"
                and bool(relations[relation_id].get("rationale"))
                for relation_id in required_axiom_inferred_relations
            ),
            "Los cruces de Axiomatización con F2 y Transformación formal deben seguir inferidos",
        )
        require(
            nodes["formal.rstar"]["formal_spec"].get("expression")
            == "WᵀR* = λ₁R*, ΣᵢR*ᵢ = 1, R*ᵢ > 0",
            "No debe armonizarse silenciosamente la orientación Wᵀ de R* en Axiomatización",
        )
        require(
            nodes["formal.axiom.REC"]["formal_spec"].get("epistemic_status")
            == "authorial_theorem_internally_inconsistent",
            "La REC no puede promoverse a resultado validado sin resolver sus cotas incompatibles",
        )
        require(
            nodes["formal.axiom.closure"]["formal_spec"].get("epistemic_status")
            == "authorial_theorem_false_under_stated_hypotheses",
            "La clausura no puede promoverse a teorema válido bajo las hipótesis registradas",
        )
        require(
            {
                "review.axiom.rstar_sink",
                "review.axiom.epsilon_dimension",
                "review.axiom.rstar_intervals",
                "review.tf.rstar_orientation",
            }
            <= set(routes["route.axiom.rstar"].get("must_surface_review_items", [])),
            "La ruta R* de Axiomatización debe surfacer sus fallos de hipótesis y el cruce W/Wᵀ",
        )
        require(
            {
                "review.axiom.tic_bound_E",
                "review.axiom.tic_bound_D",
                "review.axiom.tic_universality",
                "review.axiom.psi_domain",
                "review.axiom.Iinv_monotonicity",
            }
            <= set(routes["route.axiom.tic"].get("must_surface_review_items", [])),
            "La ruta del TIC debe surfacer todos sus problemas demostrativos",
        )
        require(
            {"review.axiom.closure", "review.axiom.perfect"}
            <= set(routes["route.axiom.closure"].get("must_surface_review_items", [])),
            "La ruta de clausura debe impedir presentar sus resultados como validados",
        )

        # Invariantes ganadas al integrar Metrología Causal I en F3.
        mci_structure_path = (
            ROOT
            / "corpus"
            / "libros"
            / "metrologia-causal"
            / "01-la-ciencia-de-la-medicion-causal"
            / "estructura.json"
        )
        require(mci_structure_path.exists(), "Falta la estructura derivada de Metrología Causal I")
        mci_structure = json.loads(mci_structure_path.read_text(encoding="utf-8"))
        require(
            mci_structure.get("sha256")
            == "f5a154fbeb8e82c89cb8fd935af7741e2f961bc8347d76c6efe413966a0c370f",
            "La estructura de Metrología Causal I no corresponde al hash de la fuente canónica",
        )
        mci_segments = {
            segment["path"]: (segment["start_line"], segment["end_line"])
            for segment in mci_structure["segments"]
        }
        require(
            len(mci_segments) == 99,
            "Metrología Causal I debe conservar preliminares, prólogo, 88 capítulos, "
            "dos epílogos, seis apéndices y glosario",
        )
        mci_evidence = [ev for ev in evidence.values() if ev["work_id"] == "MC-I"]
        mci_covered_segments = {ev["segment"] for ev in mci_evidence}
        require(
            set(mci_segments) <= mci_covered_segments,
            "La auditoría de Metrología Causal I debe cubrir sus 99 segmentos; faltan: "
            f"{sorted(set(mci_segments) - mci_covered_segments)}",
        )
        require(
            len(mci_evidence) >= 175,
            "La auditoría semántica de Metrología Causal I perdió granularidad: "
            f"{len(mci_evidence)} evidencias",
        )
        for ev in mci_evidence:
            require(
                ev["segment"] in mci_segments,
                f"{ev['id']}: segmento de Metrología Causal I no declarado en estructura.json",
            )
            segment_start, segment_end = mci_segments[ev["segment"]]
            line_start, line_end = ev["source_lines"]
            require(
                segment_start <= line_start <= line_end <= segment_end,
                f"{ev['id']}: rango fuera del segmento declarado {ev['segment']}",
            )

        required_mci_nodes = {
            "concept.mci.causal_metrology",
            "formulation.mci.prior_validation_claims",
            "formulation.mci.structural_correspondence",
            "formulation.mci.integral_correspondence",
            "formulation.mci.quantum_scope",
            "formulation.mci.internal_measurement",
            "method.mci.operationalization",
            "formal.mci.necessary_node",
            "formal.mci.G",
            "formal.mci.W",
            "formal.mci.phi1",
            "formal.mci.phi2",
            "formal.mci.ego_update",
            "formal.mci.rstar",
            "formal.mci.rstar_net",
            "formal.mci.rstar_b",
            "formal.mci.S",
            "formulation.mci.s_ranges",
            "formulation.mci.s_designer_zero",
            "formulation.mci.s_nonestimable",
            "formal.mci.alpha",
            "formal.mci.delta",
            "formal.mci.weight_intervals",
            "formal.mci.declaration",
            "method.mci.children_classifier",
            "formal.mci.IIC",
            "formal.mci.w_iic",
            "formal.mci.fraud_annona",
            "formulation.mci.series",
            "method.mci.validity_levels",
            "formal.mci.shapley",
            "method.mci.time_expansion",
            "method.mci.dossier",
            "formal.mci.robustness",
            "concept.mci.application_limits",
            "case.mci.altamirano",
            "formal.mci.altamirano_graph",
            "formal.mci.altamirano_vector",
            "formulation.mci.pf_proof",
            "formulation.mci.spectral_claims",
            "formulation.mci.monotonicity",
            "method.mci.empirical_calibration",
            "formulation.mci.duality",
        }
        require(
            required_mci_nodes <= set(nodes),
            "Núcleo de Metrología Causal I incompleto; faltan nodos: "
            f"{sorted(required_mci_nodes - set(nodes))}",
        )
        for node_id in {
            node_id for node_id in required_mci_nodes if node_id.startswith("formal.mci.")
        }:
            spec = nodes[node_id].get("formal_spec", {})
            require(
                bool(spec.get("object_type"))
                and bool(spec.get("epistemic_status"))
                and bool(spec.get("ontological_correspondence")),
                f"{node_id}: debe conservar tipo, estatuto epistémico y correspondencia ontológica",
            )

        required_mci_routes = {
            "route.mci.architecture",
            "route.mci.correspondence",
            "route.mci.phi_ego",
            "route.mci.rstar",
            "route.mci.s_rnet",
            "route.mci.alpha_delta",
            "route.mci.classifier",
            "route.mci.iic_series",
            "route.mci.validity_uncertainty",
            "route.mci.dossier_case",
            "route.mci.appendices",
            "route.mci.crosswork",
        }
        require(
            required_mci_routes <= set(routes),
            "Rutas de Metrología Causal I incompletas: "
            f"{sorted(required_mci_routes - set(routes))}",
        )
        required_mci_reviews = {
            "review.mci.retroactive_isomorphism",
            "review.mci.integral_properties",
            "review.mci.phi_typing",
            "review.mci.necessary_eigenvector",
            "review.mci.graph_connectivity",
            "review.mci.rstar_orientation",
            "review.mci.pf_hypotheses",
            "review.mci.rnet_redistribution",
            "review.mci.s_probability",
            "review.mci.s_ranges_calibration",
            "review.mci.s_designer_conflict",
            "review.mci.alpha_calibration",
            "review.mci.alpha_observability",
            "review.mci.delta_crosswork",
            "review.mci.delta_impossible_cases",
            "review.mci.interval_widths",
            "review.mci.declaration_a_logic",
            "review.mci.classifier_bayesian",
            "review.mci.iic_definition",
            "review.mci.iic_circularity",
            "review.mci.w_iic_bounds",
            "review.mci.series_identity",
            "review.mci.annona_formula",
            "review.mci.normalization_closure",
            "review.mci.irreducibility_definition",
            "review.mci.epsilon_diagonal",
            "review.mci.correction_propagation",
            "review.mci.shapley_value_function",
            "review.mci.corner_exhaustiveness",
            "review.mci.robustness_statistic",
            "review.mci.case_sources",
            "review.mci.altamirano_graph_pf",
            "review.mci.altamirano_vector_reproduction",
            "review.mci.pf_proof",
            "review.mci.spectral_markov",
            "review.mci.rstar_monotonicity",
            "review.mci.empirical_calibration",
            "review.mci.duality_proof",
        }
        require(
            required_mci_reviews <= set(reviews),
            "Deben conservarse las revisiones formales, metrológicas y empíricas de MC-I",
        )
        required_mci_inferred_relations = {
            "rel.mci.correspondence.reclassifies_caos",
            "rel.mci.correspondence.reclassifies_tf",
            "rel.mci.phi1.refines_tf",
            "rel.mci.phi1.differs_axiom",
            "rel.mci.phi2.refines_tf",
            "rel.mci.phi2.differs_axiom",
            "rel.mci.rstar.operationalizes_tf",
            "rel.mci.rstar.reuses_axiom",
            "rel.mci.rnet.reuses_tf",
            "rel.mci.rnet.differs_axiom",
            "rel.mci.s.operationalizes_tf",
            "rel.mci.s.differs_axiom",
            "rel.mci.s_nonestimable.restricts_s",
            "rel.mci.alpha.operationalizes_tf",
            "rel.mci.alpha.differs_axiom",
            "rel.mci.delta.reuses_tf",
            "rel.mci.delta.differs_axiom",
            "rel.mci.classifier.operationalizes_children",
            "rel.mci.iic.operationalizes_tf",
            "rel.mci.w_iic.operationalizes_tf",
            "rel.mci.annona.elaborates_axiom",
            "rel.mci.robustness.elaborates_tf",
            "rel.mci.robustness.elaborates_axiom",
            "rel.mci.calibration.claims_tf_gap",
        }
        require(
            all(
                relation_id in relations
                and relations[relation_id]["evidence_status"] == "inferred"
                and bool(relations[relation_id].get("rationale"))
                for relation_id in required_mci_inferred_relations
            ),
            "Los cruces de MC-I con F2, TF y Axiomatización deben seguir inferidos",
        )
        require(
            nodes["formal.mci.rstar"]["formal_spec"].get("epistemic_status")
            == "authorial_operationalization_internally_inconsistent",
            "MC-I no puede presentar R* como cálculo validado mientras discrepen ecuación e iteración",
        )
        require(
            nodes["formal.mci.S"]["formal_spec"].get("codomain")
            == "[0,1] o no estimable",
            "La restricción de no estimabilidad de S debe permanecer visible",
        )
        require(
            nodes["formal.mci.delta"]["formal_spec"].get("expression") == "Δ=R*(1−α)",
            "No debe armonizarse la fórmula de Δ en MC-I con la resta de Axiomatización",
        )
        require(
            nodes["formal.mci.robustness"]["formal_spec"].get("epistemic_status")
            == "authorial_algorithm_with_invalid_exhaustiveness_claims",
            "El protocolo de vértices no puede promoverse a garantía universal",
        )
        require(
            {
                "review.rstar.sink_irreducibility",
                "review.tf.rstar_orientation",
                "review.axiom.rstar_sink",
                "review.mci.graph_connectivity",
                "review.mci.rstar_orientation",
                "review.mci.pf_hypotheses",
                "review.mci.normalization_closure",
            }
            <= set(routes["route.mci.rstar"].get("must_surface_review_items", [])),
            "La ruta R* de MC-I debe surfacer problemas heredados y propios",
        )
        require(
            {
                "review.tf.vertex_robustness",
                "review.axiom.rstar_intervals",
                "review.mci.interval_widths",
                "review.mci.declaration_a_logic",
                "review.mci.corner_exhaustiveness",
            }
            <= set(
                routes["route.mci.validity_uncertainty"].get(
                    "must_surface_review_items", []
                )
            ),
            "La ruta de incertidumbre de MC-I debe impedir confundir muestreo con garantía",
        )
        require(
            {
                "review.mci.case_sources",
                "review.mci.altamirano_graph_pf",
                "review.mci.altamirano_vector_reproduction",
            }
            <= set(routes["route.mci.dossier_case"].get("must_surface_review_items", [])),
            "La ruta del caso no puede presentar el vector publicado como reproducido",
        )

        # Invariantes ganadas al integrar Metrología Causal II en F3.
        require("MC-II" in works, "Falta Metrología Causal II en el inventario de F3")
        mcii_structure_path = (
            ROOT
            / "corpus"
            / "libros"
            / "metrologia-causal"
            / "02-vol-ii"
            / "estructura.json"
        )
        require(mcii_structure_path.exists(), "Falta la estructura derivada de Metrología Causal II")
        mcii_structure = json.loads(mcii_structure_path.read_text(encoding="utf-8"))
        mcii_segments = {
            segment["path"]: (segment["start_line"], segment["end_line"])
            for segment in mcii_structure["segments"]
        }
        mcii_evidence = [ev for ev in evidence.values() if ev["work_id"] == "MC-II"]
        mcii_covered_segments = {ev["segment"] for ev in mcii_evidence}
        require(
            set(mcii_segments) <= mcii_covered_segments,
            "La auditoría de Metrología Causal II debe cubrir introducción, "
            "diecinueve capítulos y dos apéndices; faltan: "
            f"{sorted(set(mcii_segments) - mcii_covered_segments)}",
        )
        require(
            len(mcii_evidence) >= 96,
            "La auditoría semántica y formal de Metrología Causal II perdió "
            f"granularidad: {len(mcii_evidence)} evidencias",
        )
        for ev in mcii_evidence:
            require(
                ev["segment"] in mcii_segments,
                f"{ev['id']}: segmento de Metrología Causal II no declarado en estructura.json",
            )
            segment_start, segment_end = mcii_segments[ev["segment"]]
            line_start, line_end = ev["source_lines"]
            require(
                segment_start <= line_start <= line_end <= segment_end,
                f"{ev['id']}: rango fuera del segmento declarado {ev['segment']}",
            )

        required_mcii_nodes = {
            "concept.mcii.operational_volume",
            "formulation.mcii.translation",
            "formulation.mcii.question_types",
            "method.mcii.workflow",
            "formal.mcii.G",
            "formal.mcii.W",
            "formal.mcii.rstar",
            "formal.mcii.S",
            "formulation.mcii.s_ranges",
            "formal.mcii.alpha",
            "method.mcii.alpha_routes",
            "method.mcii.method_selector",
            "formal.mcii.shapley",
            "formulation.mcii.series",
            "formal.mcii.series1_case",
            "formal.mcii.rstar_net",
            "formal.mcii.delta",
            "formal.mcii.D_total",
            "formal.mcii.AD",
            "formal.mcii.IIC",
            "formal.mcii.w_iic",
            "formal.mcii.fraud_annona",
            "formal.mcii.robustness",
            "method.mcii.integrated_protocol",
            "method.mcii.consistency_checks",
            "method.mcii.dossier",
            "concept.mcii.application_limits",
            "formal.mcii.axioms",
            "formulation.mcii.pf_lemma",
            "formulation.mcii.responsibility_theorem",
            "formal.mcii.delta_corollary",
            "formal.mcii.annona_corollary",
            "formal.mcii.shapley_extension",
            "formulation.mcii.unifying_operator",
            "method.mcii.empirical_calibration",
            "formal.mcii.forms",
            "formal.mcii.conversion",
            "method.mcii.child_classifier",
            "formal.mcii.kconv",
            "method.mcii.calibration_sheet",
            "method.mcii.equivalences",
        }
        require(
            required_mcii_nodes <= set(nodes),
            "Núcleo de Metrología Causal II incompleto; faltan nodos: "
            f"{sorted(required_mcii_nodes - set(nodes))}",
        )
        required_mcii_formal_nodes = {
            node_id
            for node_id in required_mcii_nodes
            if nodes[node_id].get("kind") == "formal_object"
        }
        for node_id in required_mcii_formal_nodes:
            spec = nodes[node_id].get("formal_spec", {})
            require(
                bool(spec.get("symbol"))
                and bool(spec.get("object_type"))
                and bool(spec.get("domain"))
                and bool(spec.get("codomain"))
                and isinstance(spec.get("dependencies"), list)
                and isinstance(spec.get("assumptions"), list)
                and bool(spec.get("epistemic_status"))
                and bool(spec.get("ontological_correspondence")),
                f"{node_id}: debe conservar símbolo, tipo, dominio, codominio, "
                "dependencias, supuestos, estatuto y correspondencia ontológica",
            )

        required_mcii_routes = {
            "route.mcii.architecture",
            "route.mcii.translation",
            "route.mcii.graph_rstar",
            "route.mcii.s_alpha_delta",
            "route.mcii.method_selector",
            "route.mcii.iic_annona",
            "route.mcii.robustness",
            "route.mcii.integrated",
            "route.mcii.theorem",
            "route.mcii.corollaries",
            "route.mcii.cou",
            "route.mcii.calibration",
            "route.mcii.crosswork",
        }
        require(
            required_mcii_routes <= set(routes),
            "Rutas de Metrología Causal II incompletas: "
            f"{sorted(required_mcii_routes - set(routes))}",
        )
        required_mcii_reviews = {
            "review.mcii.question_exhaustiveness",
            "review.mcii.translation_validity",
            "review.mcii.rstar_counterfactual",
            "review.mcii.series_dependencies",
            "review.mcii.phi2_observability",
            "review.mcii.s_range_arithmetic",
            "review.mcii.s_range_calibration",
            "review.mcii.alpha_route_b_sum",
            "review.mcii.alpha_opportunity_direction",
            "review.mcii.alpha_divergence",
            "review.mcii.method_selector",
            "review.mcii.irreducibility",
            "review.mcii.epsilon",
            "review.mcii.normalization",
            "review.mcii.series1_vector",
            "review.mcii.sink_normalization",
            "review.mcii.delta_sign",
            "review.mcii.delta_magnitude",
            "review.mcii.iic_codomain",
            "review.mcii.iic_correlation",
            "review.mcii.weight_adjustment_invariance",
            "review.mcii.annona_domain",
            "review.mcii.annona_derivation",
            "review.mcii.annona_arithmetic",
            "review.mcii.hypercube_sampling",
            "review.mcii.rho_estimation",
            "review.mcii.integrated_graph_identity",
            "review.mcii.consistency_c1",
            "review.mcii.consistency_c2",
            "review.mcii.axiom_independence",
            "review.mcii.axiom_indices",
            "review.mcii.pf_primitive",
            "review.mcii.theorem_a2",
            "review.mcii.theorem_monotonicity",
            "review.mcii.theorem_uniqueness",
            "review.mcii.delta_appendix",
            "review.mcii.shapley_value_function",
            "review.mcii.shapley_continuity",
            "review.mcii.cou_sources",
            "review.mcii.cou_definition",
            "review.mcii.instrument_validity",
            "review.mcii.conversion_values",
            "review.mcii.child_classifier",
            "review.mcii.kconv",
            "review.mcii.calibration_estimators",
            "review.mcii.cohort_precision",
        }
        require(
            required_mcii_reviews <= set(reviews),
            "Deben conservarse las revisiones formales, metrológicas, "
            "empíricas y de correspondencia de MC-II",
        )
        require(
            len([review for review in reviews if review.startswith("review.mcii.")]) >= 60,
            "La cola de MC-II no puede perder problemas auditados",
        )
        require(
            all(
                relation["evidence_status"] == "inferred"
                and bool(relation.get("rationale"))
                for relation in relations.values()
                if relation["id"].startswith("rel.mcii.")
            ),
            "Los cruces de MC-II con MC-I, TF y Axiomatización deben seguir inferidos",
        )
        require(
            nodes["formal.mcii.rstar"]["formal_spec"].get("epistemic_status")
            == "authorial_operationalization_not_reproduced_and_theorem_invalid",
            "El vector y el teorema de R* de MC-II no pueden presentarse como validados",
        )
        require(
            nodes["formal.mcii.IIC"]["formal_spec"].get("codomain") == "[-1,1]",
            "Debe conservarse el cambio de codominio del IIC en MC-II",
        )
        require(
            nodes["formal.mcii.delta"]["formal_spec"].get("expression")
            == "Δ_i=R*(i)(1−α_i); Δ_total=Σ_iΔ_i",
            "No debe armonizarse Δ de MC-II con la resta axiomática ni con Δ_sesión",
        )
        require(
            nodes["formal.mcii.conversion"]["formal_spec"].get("epistemic_status")
            == "authorial_scoring_rule_uncalibrated_and_redefines_delta",
            "La tabla de conversión no puede promoverse a calibración empírica realizada",
        )
        require(
            nodes["formulation.mcii.unifying_operator"]["formal_spec"].get(
                "epistemic_status"
            )
            == "explicitly_open_authorial_conjecture",
            "La C.O.U. debe permanecer registrada como conjetura abierta",
        )
        require(
            {
                "review.rstar.sink_irreducibility",
                "review.tf.rstar_orientation",
                "review.axiom.rstar_sink",
                "review.mci.rstar_orientation",
                "review.mci.pf_hypotheses",
                "review.mcii.irreducibility",
                "review.mcii.normalization",
                "review.mcii.series1_vector",
            }
            <= set(routes["route.mcii.graph_rstar"].get("must_surface_review_items", [])),
            "La ruta R* de MC-II debe surfacer revisiones heredadas y propias",
        )
        require(
            {
                "review.mci.empirical_calibration",
                "review.axiom.calibration_sources",
                "review.mcii.instrument_validity",
                "review.mcii.conversion_values",
                "review.mcii.kconv",
                "review.mcii.calibration_estimators",
            }
            <= set(routes["route.mcii.calibration"].get("must_surface_review_items", [])),
            "La ruta de calibración debe separar protocolo prospectivo y evidencia realizada",
        )

        # Invariantes ganadas al integrar El cálculo de la responsabilidad en F3.
        require("CALCULO-R" in works, "Falta El cálculo de la responsabilidad en F3")
        calc_structure_path = (
            ROOT
            / "corpus"
            / "libros"
            / "calculo-de-la-responsabilidad"
            / "estructura.json"
        )
        require(
            calc_structure_path.exists(),
            "Falta la estructura derivada de El cálculo de la responsabilidad",
        )
        calc_structure = json.loads(calc_structure_path.read_text(encoding="utf-8"))
        require(
            calc_structure.get("sha256") == works["CALCULO-R"]["sha256"],
            "La estructura de El cálculo no corresponde al hash de la fuente canónica",
        )
        calc_segments = {
            segment["path"]: (segment["start_line"], segment["end_line"])
            for segment in calc_structure["segments"]
        }
        require(
            len(calc_segments) == 25,
            "El cálculo debe conservar preliminares, prólogo, 18 capítulos y 5 apéndices",
        )
        calc_evidence = [
            ev for ev in evidence.values() if ev["work_id"] == "CALCULO-R"
        ]
        calc_covered_segments = {ev["segment"] for ev in calc_evidence}
        require(
            set(calc_segments) <= calc_covered_segments,
            "La auditoría de El cálculo debe cubrir sus 25 segmentos; faltan: "
            f"{sorted(set(calc_segments) - calc_covered_segments)}",
        )
        require(
            len(calc_evidence) >= 124,
            "La auditoría semántica, formal y aplicada de El cálculo perdió "
            f"granularidad: {len(calc_evidence)} evidencias",
        )
        for ev in calc_evidence:
            require(
                ev["segment"] in calc_segments,
                f"{ev['id']}: segmento de El cálculo no declarado en estructura.json",
            )
            segment_start, segment_end = calc_segments[ev["segment"]]
            line_start, line_end = ev["source_lines"]
            require(
                segment_start <= line_start <= line_end <= segment_end,
                f"{ev['id']}: rango fuera del segmento declarado {ev['segment']}",
            )

        required_calc_nodes = {
            "formal.calc.G",
            "formal.calc.W",
            "formal.calc.rstar",
            "formal.calc.power",
            "formal.calc.S",
            "formal.calc.alpha",
            "formal.calc.delta",
            "formal.calc.rnet",
            "formal.calc.Dtotal",
            "formal.calc.Dvital",
            "formal.calc.Btotal",
            "formal.calc.deltaB",
            "formal.calc.AD",
            "formal.calc.J",
            "formal.calc.IIC",
            "formal.calc.FA",
            "formal.calc.childprob",
            "formal.calc.childentropy",
            "formal.calc.egoito",
            "formal.calc.shapley",
            "formal.calc.rhist",
            "formal.calc.Iid",
            "formal.calc.prescription",
            "formal.calc.causal_inversion",
            "formal.calc.opacity",
            "formal.calc.inherited",
            "formal.calc.clinical",
            "formal.calc.R0",
            "formal.calc.tanatology",
            "formal.calc.DI",
            "formal.calc.ICRS",
            "formal.calc.PAC",
            "formal.calc.fine",
            "formal.calc.governance",
            "formal.calc.INCF",
            "formal.calc.IAS",
            "formal.calc.algorithmic",
            "formal.calc.education",
            "formal.calc.sports",
            "formal.calc.narrative",
            "method.calc.weight_protocol",
            "method.calc.domain_translation",
            "method.calc.library",
            "formulation.calc.banach",
            "formulation.calc.pf",
            "formulation.calc.ito",
            "formulation.calc.shapley",
            "case.calc.axis",
            "formulation.calc.domain_limits",
            "formulation.calc.source_status",
            "calculation.calc.published_graphs_spectral_check",
        }
        require(
            required_calc_nodes <= set(nodes),
            "Núcleo de El cálculo incompleto; faltan nodos: "
            f"{sorted(required_calc_nodes - set(nodes))}",
        )
        required_calc_formal_nodes = {
            node_id
            for node_id in required_calc_nodes
            if nodes[node_id].get("kind") == "formal_object"
        }
        for node_id in required_calc_formal_nodes:
            spec = nodes[node_id].get("formal_spec", {})
            require(
                bool(spec.get("symbol"))
                and bool(spec.get("object_type"))
                and bool(spec.get("expression"))
                and bool(spec.get("domain"))
                and bool(spec.get("codomain"))
                and isinstance(spec.get("dependencies"), list)
                and isinstance(spec.get("assumptions"), list)
                and bool(spec.get("epistemic_status"))
                and bool(spec.get("ontological_correspondence")),
                f"{node_id}: debe conservar símbolo, tipo, expresión, dominio, "
                "codominio, dependencias, supuestos, estatuto y correspondencia",
            )

        required_calc_routes = {
            "route.calc.core",
            "route.calc.rstar",
            "route.calc.weights",
            "route.calc.delta",
            "route.calc.damage",
            "route.calc.indices",
            "route.calc.proofs",
            "route.calc.health",
            "route.calc.finance",
            "route.calc.technology",
            "route.calc.humanities",
            "route.calc.case_axis",
            "route.calc.software",
            "route.calc.sources",
            "route.calc.crosswork",
        }
        require(
            required_calc_routes <= set(routes),
            "Rutas de El cálculo incompletas: "
            f"{sorted(required_calc_routes - set(routes))}",
        )
        required_calc_reviews = {
            "review.calc.rstar_equivalence",
            "review.calc.orientation",
            "review.calc.sinks",
            "review.calc.banach_contraction",
            "review.calc.pf_periodicity",
            "review.calc.self_loop_connectivity",
            "review.calc.weight_evidence_conflation",
            "review.calc.weight_interrater",
            "review.calc.S_loop",
            "review.calc.S_definedness",
            "review.calc.alpha_crossdomain",
            "review.calc.delta_history",
            "review.calc.deltaB_type",
            "review.calc.damage_units",
            "review.calc.dvital_normativity",
            "review.calc.J_domain",
            "review.calc.J_comparability",
            "review.calc.IIC_scale",
            "review.calc.IIC_measurement",
            "review.calc.child_calibration",
            "review.calc.child_entropy",
            "review.calc.ito_bridge",
            "review.calc.shapley_value",
            "review.calc.shapley_collapse",
            "review.calc.historical_probabilities",
            "review.calc.causal_inversion",
            "review.calc.opacity_redundancy",
            "review.calc.pld_arithmetic",
            "review.calc.R0_correspondence",
            "review.calc.ICRS_calibration",
            "review.calc.governance_dataset",
            "review.calc.algorithmic_additivity",
            "review.calc.case_sources",
            "review.calc.case_J",
            "review.calc.source_apparatus",
            "review.calc.code_artifact",
            "review.calc.FA_typing",
            "review.calc.prediction_status",
            "review.calc.published_vectors_reproduction",
        }
        require(
            required_calc_reviews <= set(reviews),
            "Deben conservarse las revisiones formales, metrológicas, empíricas, "
            "doctrinales y de fuentes de El cálculo",
        )
        require(
            len([review for review in reviews if review.startswith("review.calc.")])
            >= 67,
            "La cola de El cálculo no puede perder problemas auditados",
        )
        require(
            len(reviews) >= 413,
            "La integración de El cálculo no puede borrar las 346 revisiones heredadas",
        )
        require(
            all(
                relation["evidence_status"] == "inferred"
                and bool(relation.get("rationale"))
                for relation in relations.values()
                if relation["id"].startswith("rel.calc.")
            ),
            "Los cruces de El cálculo deben seguir marcados como inferencias auditables",
        )
        require(
            nodes["formal.calc.rstar"]["formal_spec"].get("epistemic_status")
            == "authorial_definition_with_unresolved_formal_and_causal_correspondence",
            "R* de El cálculo no puede presentarse como fracción causal validada",
        )
        require(
            nodes["formal.calc.delta"]["formal_spec"].get("expression")
            == "Δ_i=R*_i−α_i",
            "Debe conservarse la versión sustractiva de Δ en El cálculo",
        )
        require(
            nodes["formal.calc.deltaB"]["formal_spec"].get("epistemic_status")
            == "authorial_internal_type_conflict",
            "No debe armonizarse el conflicto resta/producto de Δ_B",
        )
        require(
            nodes["formal.calc.J"]["formal_spec"].get("codomain")
            == "(-∞,1] en general; el texto usa valores negativos",
            "J debe conservar el uso negativo que contradice la cota anterior",
        )
        require(
            nodes["formal.calc.IIC"]["formal_spec"].get("codomain")
            == "[-1,1] en capítulo; [0,1] en biblioteca/glosario",
            "No debe armonizarse el cambio interno de escala de IIC",
        )
        spectral = nodes["calculation.calc.published_graphs_spectral_check"]
        require(
            spectral.get("evidence_status") == "inferred"
            and all(
                result.get("spectral_radius") == 0.0
                for result in spectral.get("results", {}).values()
            )
            and set(spectral.get("results", {}))
            == {"caso_eje", "caso_clinico", "john_snow"},
            "La reproducción espectral de los tres grafos publicados debe permanecer visible",
        )
        require(
            relations["rel.calc.spectral_check.tests_power"]["evidence_status"]
            == "inferred",
            "La reproducción espectral es un resultado analítico, no lenguaje autoral",
        )
        require(
            {
                "review.rstar.sink_irreducibility",
                "review.tf.rstar_orientation",
                "review.axiom.rstar_sink",
                "review.mci.rstar_orientation",
                "review.mcii.sink_normalization",
                "review.calc.published_vectors_reproduction",
            }
            <= set(routes["route.calc.rstar"].get("must_surface_review_items", [])),
            "La ruta R* de El cálculo debe surfacer fallas heredadas y reproducción",
        )
        require(
            {
                "review.mci.delta_crosswork",
                "review.mcii.delta_sign",
                "review.mcii.delta_appendix",
                "review.calc.delta_history",
                "review.calc.deltaB_type",
            }
            <= set(routes["route.calc.delta"].get("must_surface_review_items", [])),
            "La ruta Δ debe preservar versiones históricas y conflicto de tipado",
        )
        require(
            {
                "review.calc.case_sources",
                "review.calc.case_J",
                "review.calc.case_alpha",
                "review.calc.published_vectors_reproduction",
            }
            <= set(routes["route.calc.case_axis"].get("must_surface_review_items", [])),
            "La ruta del Caso Eje debe surfacer fuentes, calibración, J y reproducción",
        )
        require(
            phase in {"F4", "F5", "MANT"},
            "Con las cinco obras de F3 integradas y validadas, la fase operativa no puede retroceder a F3",
        )
        f3_formal_prefixes = (
            "formal.tf.",
            "formal.axiom.",
            "formal.mci.",
            "formal.mcii.",
            "formal.calc.",
        )
        f3_formal_nodes = {
            node_id: item
            for node_id, item in nodes.items()
            if item.get("kind") == "formal_object"
            and node_id.startswith(f3_formal_prefixes)
        }
        require(
            len(f3_formal_nodes) >= 155,
            "El cierre de F3 debe conservar al menos 155 objetos formales auditados",
        )
        for node_id, item in f3_formal_nodes.items():
            spec = item.get("formal_spec", {})
            require(
                bool(spec.get("symbol"))
                and bool(spec.get("object_type"))
                and (bool(spec.get("expression")) or bool(spec.get("definition")))
                and bool(spec.get("domain"))
                and bool(spec.get("codomain"))
                and isinstance(spec.get("dependencies"), list)
                and isinstance(spec.get("assumptions"), list)
                and bool(spec.get("epistemic_status"))
                and bool(spec.get("ontological_correspondence"))
                and bool(item.get("evidence")),
                f"{node_id}: F3 exige símbolo, tipo, definición o expresión, dominio, "
                "codominio, dependencias, supuestos, estatuto, correspondencia y proveniencia",
            )
        f3_review_prefixes = (
            "review.tf.",
            "review.axiom.",
            "review.mci.",
            "review.mcii.",
            "review.calc.",
        )
        f3_reviews = {
            review_id
            for review_id in reviews
            if review_id.startswith(f3_review_prefixes)
        }
        surfaced_reviews = {
            review_id
            for route_item in routes.values()
            for review_id in route_item.get("must_surface_review_items", [])
        }
        require(
            len(f3_reviews) >= 269,
            "El cierre de F3 no puede perder revisiones heredadas o propias",
        )
        require(
            f3_reviews <= surfaced_reviews,
            "Toda revisión de F3 debe ser navegable desde al menos una ruta; faltan: "
            f"{sorted(f3_reviews - surfaced_reviews)}",
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
        f"{len([ev for ev in evidence.values() if ev['work_id'] == 'TRANSFORMACION-FORMAL'])} evidencias de La transformación formal,",
        f"{len([ev for ev in evidence.values() if ev['work_id'] == 'AXIOM-SDM'])} evidencias de Axiomatización,",
        f"{len([ev for ev in evidence.values() if ev['work_id'] == 'MC-I'])} evidencias de Metrología Causal I."
        f" {len([ev for ev in evidence.values() if ev['work_id'] == 'MC-II'])} evidencias de Metrología Causal II.",
        f"{len([ev for ev in evidence.values() if ev['work_id'] == 'CALCULO-R'])} evidencias de El cálculo de la responsabilidad."
    )
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValidationError, json.JSONDecodeError, KeyError, TypeError) as exc:
        print(f"ERROR DE VALIDACIÓN: {exc}", file=sys.stderr)
        raise SystemExit(1)
