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
        f"{len([ev for ev in evidence.values() if ev['work_id'] == 'AA-IV'])} evidencias de Afrodita Areia IV."
    )
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValidationError, json.JSONDecodeError, KeyError, TypeError) as exc:
        print(f"ERROR DE VALIDACIÓN: {exc}", file=sys.stderr)
        raise SystemExit(1)
