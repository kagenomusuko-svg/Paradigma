#!/usr/bin/env python3
"""Integra AA-VI (Nikomachos) al mapa maestro sin borrar la historia previa.

Es un migrador de mantenimiento de una sola ejecución. Conserva reviews históricas,
añade evidencia y formulaciones posteriores, y registra la única tensión nueva que
AA-VI no adjudica explícitamente: el crosswalk entre los dos usos históricos de `sum`.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / "mapa" / "mapa-maestro.json"
RESOLUTION = "documentacion/resolucion-nikomachos-dignidad-predicacion.md"
AA6_SHA256 = "5ad5ca58854ab1664dd41e6027ea30f29cc6e5217ee7210e14a612a684a08a21"


def ids(items: list[dict]) -> set[str]:
    return {item["id"] for item in items}


def append_unique(items: list[dict], new_items: list[dict], label: str) -> None:
    existing = ids(items)
    duplicates = [item["id"] for item in new_items if item["id"] in existing]
    if duplicates:
        raise RuntimeError(f"{label}: IDs ya existentes: {duplicates}")
    items.extend(new_items)


def get_by_id(items: list[dict], item_id: str) -> dict:
    for item in items:
        if item.get("id") == item_id:
            return item
    raise KeyError(item_id)


data = json.loads(MAP.read_text(encoding="utf-8"))
if data.get("map_version") != "2.11.0":
    raise RuntimeError(f"Versión inesperada del mapa: {data.get('map_version')}")
if "AA-VI" in ids(data["works"]):
    raise RuntimeError("AA-VI ya está integrado; no ejecutar este migrador de nuevo.")

# ── Obra ────────────────────────────────────────────────────────────────
data["works"].append({
    "id": "AA-VI",
    "title": "Afrodita Areia: Nikomachos — El límite de la predicación",
    "source": "corpus/fuentes/Afrodita_Areia_Nikomachos.md",
    "sha256": AA6_SHA256,
})

# ── Evidencia ───────────────────────────────────────────────────────────
evidence = [
    {
        "id": "ev.aa6.prologue",
        "work_id": "AA-VI",
        "segment": "corpus/libros/afrodita-areia/06-nikomachos/02-prologo.md",
        "source_lines": [7, 144],
        "section": "Prólogo · la pregunta antes del hombre",
        "evidence_type": "authorial_system_statement",
    },
    {
        "id": "ev.aa6.caos",
        "work_id": "AA-VI",
        "segment": "corpus/libros/afrodita-areia/06-nikomachos/capitulo-01.md",
        "source_lines": [145, 318],
        "section": "Capítulo I · Caos, colapso y frontera del no-ser",
        "evidence_type": "primary_text",
    },
    {
        "id": "ev.aa6.sum",
        "work_id": "AA-VI",
        "segment": "corpus/libros/afrodita-areia/06-nikomachos/capitulo-02.md",
        "source_lines": [319, 543],
        "section": "Capítulo II · ser, estar, sum y trayectoria",
        "evidence_type": "authorial_definition",
    },
    {
        "id": "ev.aa6.dignity",
        "work_id": "AA-VI",
        "segment": "corpus/libros/afrodita-areia/06-nikomachos/capitulo-03.md",
        "source_lines": [544, 769],
        "section": "Capítulo III · univocidad y dignidad",
        "evidence_type": "authorial_definition",
    },
    {
        "id": "ev.aa6.dignity_modes",
        "work_id": "AA-VI",
        "segment": "corpus/libros/afrodita-areia/06-nikomachos/capitulo-04.md",
        "source_lines": [770, 981],
        "section": "Capítulo IV · dignidad, diferencia y embargo",
        "evidence_type": "primary_text",
    },
    {
        "id": "ev.aa6.predication",
        "work_id": "AA-VI",
        "segment": "corpus/libros/afrodita-areia/06-nikomachos/capitulo-05.md",
        "source_lines": [982, 1237],
        "section": "Capítulo V · escala, dominio y jurisdicción de la predicación",
        "evidence_type": "authorial_definition",
    },
    {
        "id": "ev.aa6.bridges",
        "work_id": "AA-VI",
        "segment": "corpus/libros/afrodita-areia/06-nikomachos/capitulo-06.md",
        "source_lines": [1238, 1491],
        "section": "Capítulo VI · puentes rawlsianos y tautologías euclidianas",
        "evidence_type": "authorial_method",
    },
    {
        "id": "ev.aa6.knowledge",
        "work_id": "AA-VI",
        "segment": "corpus/libros/afrodita-areia/06-nikomachos/capitulo-07.md",
        "source_lines": [1492, 1761],
        "section": "Capítulo VII · rastros, modelos y medición",
        "evidence_type": "authorial_epistemology",
    },
    {
        "id": "ev.aa6.noumenon",
        "work_id": "AA-VI",
        "segment": "corpus/libros/afrodita-areia/06-nikomachos/capitulo-08.md",
        "source_lines": [1762, 2022],
        "section": "Capítulo VIII · Hume, Kant y el noúmeno",
        "evidence_type": "authorial_epistemology",
    },
    {
        "id": "ev.aa6.act",
        "work_id": "AA-VI",
        "segment": "corpus/libros/afrodita-areia/06-nikomachos/capitulo-09.md",
        "source_lines": [2023, 2270],
        "section": "Capítulo IX · sujeto, acto y trayectoria",
        "evidence_type": "primary_text",
    },
    {
        "id": "ev.aa6.critique",
        "work_id": "AA-VI",
        "segment": "corpus/libros/afrodita-areia/06-nikomachos/capitulo-10.md",
        "source_lines": [2271, 2530],
        "section": "Capítulo X · crítica, sentencia y exilio ontológico",
        "evidence_type": "authorial_distinction",
    },
    {
        "id": "ev.aa6.causality_norm",
        "work_id": "AA-VI",
        "segment": "corpus/libros/afrodita-areia/06-nikomachos/capitulo-11.md",
        "source_lines": [2531, 2770],
        "section": "Capítulo XI · causalidad, norma y jurisdicción",
        "evidence_type": "authorial_distinction",
    },
    {
        "id": "ev.aa6.responsibility",
        "work_id": "AA-VI",
        "segment": "corpus/libros/afrodita-areia/06-nikomachos/capitulo-12.md",
        "source_lines": [2771, 3060],
        "section": "Capítulo XII · responsabilidad sin juicio ontológico",
        "evidence_type": "authorial_synthesis",
    },
    {
        "id": "ev.aa6.epilogue",
        "work_id": "AA-VI",
        "segment": "corpus/libros/afrodita-areia/06-nikomachos/90-epilogo.md",
        "source_lines": [3061, 3185],
        "section": "Epílogo · el límite de la predicación",
        "evidence_type": "authorial_synthesis",
    },
]
append_unique(data["evidence"], evidence, "evidence")

# ── Nodos ───────────────────────────────────────────────────────────────
nodes = [
    {
        "id": "concept.sum.aa6",
        "kind": "concept",
        "label": "Sum en AA-VI",
        "summary": "Articulación de ser y estar como ejes intrínsecos del mismo fenómeno: no hay ser sin determinación ni estar sin algo que sea.",
        "evidence": ["ev.aa6.sum", "ev.aa6.dignity"],
        "evidence_status": "explicit",
    },
    {
        "id": "concept.univocidad_ser.aa6",
        "kind": "concept",
        "label": "Univocidad ontológica del ser",
        "summary": "El predicado ser conserva el mismo sentido entre modos de ser heterogéneos sin implicar identidad categorial, normativa ni práctica.",
        "evidence": ["ev.aa6.dignity", "ev.aa6.dignity_modes"],
        "evidence_status": "explicit",
    },
    {
        "id": "concept.dignidad_ser.aa6",
        "kind": "concept",
        "label": "Dignidad inherente al ser",
        "summary": "Explicitación de que aquello que es no puede ser deficitario respecto de su propio ser; no depende de racionalidad, conciencia, agencia, humanidad ni capacidad de sufrir.",
        "evidence": ["ev.aa6.dignity", "ev.aa6.dignity_modes"],
        "evidence_status": "explicit",
    },
    {
        "id": "concept.predicacion_localizada.aa6",
        "kind": "concept",
        "label": "Predicación localizada",
        "summary": "Predicación verdadera dentro de una escala, dominio e instrumentos declarados cuya jurisdicción no equivale a conocimiento exhaustivo del ser qua ser.",
        "evidence": ["ev.aa6.predication", "ev.aa6.knowledge"],
        "evidence_status": "explicit",
    },
    {
        "id": "method.puente_rawlsiano.aa6",
        "kind": "method",
        "label": "Puente rawlsiano",
        "summary": "Exigencia de declarar la mediación P que autoriza un tránsito A → B: A + P → B; P puede ser norma, criterio, convención, procedimiento, función, umbral o regla de imputación.",
        "evidence": ["ev.aa6.bridges"],
        "evidence_status": "explicit",
    },
    {
        "id": "method.tautologia_euclidiana.aa6",
        "kind": "method",
        "label": "Tautología euclidiana",
        "summary": "Auditoría interna de condiciones constitutivas: una operación que pretende ser X no puede incorporar aquello que destruye las condiciones por las que puede seguir siendo X.",
        "evidence": ["ev.aa6.bridges"],
        "evidence_status": "explicit",
    },
    {
        "id": "concept.conocimiento_situado.aa6",
        "kind": "concept",
        "label": "Conocimiento situado",
        "summary": "Conocimiento por rastros, modelos y mediciones que puede ser verdadero y preciso sin producir acceso exhaustivo al ser qua ser.",
        "evidence": ["ev.aa6.knowledge", "ev.aa6.noumenon"],
        "evidence_status": "explicit",
    },
    {
        "id": "concept.limite_noumenico.aa6",
        "kind": "concept",
        "label": "Noúmeno como frontera epistemológica",
        "summary": "Uso negativo del noúmeno como límite del conocimiento teórico: demarca lo que no puede conocerse exhaustivamente sin volver falso el conocimiento fenoménico localizado.",
        "evidence": ["ev.aa6.noumenon"],
        "evidence_status": "explicit",
    },
    {
        "id": "concept.sentencia_ontologica.aa6",
        "kind": "concept",
        "label": "Sentencia ontológica",
        "aliases": ["exilio ontológico"],
        "summary": "Migración de una evaluación localizada del acto o la trayectoria a una pretensión exhaustiva sobre el ser qua ser del agente.",
        "evidence": ["ev.aa6.critique", "ev.aa6.epilogue"],
        "evidence_status": "explicit",
    },
    {
        "id": "concept.ley_constitutiva.aa6",
        "kind": "concept",
        "label": "Ley constitutiva",
        "summary": "Descripción de condiciones bajo las que un fenómeno puede seguir siendo predicado como aquello que es; se distingue de la norma prescriptiva, que ordena o prohíbe a destinatarios normativos.",
        "evidence": ["ev.aa6.causality_norm"],
        "evidence_status": "explicit",
    },
    {
        "id": "concept.responsabilidad_sin_sentencia.aa6",
        "kind": "concept",
        "label": "Responsabilidad sin sentencia ontológica",
        "summary": "Imputación fundada en reconstrucción causal, condiciones de imputabilidad y jurisdicción normativa sin requerir una predicación exhaustiva de maldad o culpabilidad sobre el ser del agente.",
        "evidence": ["ev.aa6.causality_norm", "ev.aa6.responsibility", "ev.aa6.epilogue"],
        "evidence_status": "explicit",
    },
]
append_unique(data["nodes"], nodes, "nodes")

# ── Relaciones ──────────────────────────────────────────────────────────
relations = [
    {
        "id": "rel.aa6.sum_reframes_aa5",
        "from": "concept.sum.aa6",
        "to": "concept.sum.aa5",
        "type": "refines",
        "evidence_status": "inferred",
        "evidence": ["ev.aa6.sum", "ev.aa5.ego.formulas"],
        "rationale": "AA-VI usa sum para la intrinsequidad ser/estar, mientras AA-V lo presenta como identidad, voluntad y primera mediación antes del acto asumido; la relación histórica no queda adjudicada expresamente.",
    },
    {
        "id": "rel.aa6.sum_condition_univocity",
        "from": "concept.sum.aa6",
        "to": "concept.univocidad_ser.aa6",
        "type": "condition_of",
        "evidence_status": "explicit",
        "evidence": ["ev.aa6.dignity"],
    },
    {
        "id": "rel.aa6.univocity_condition_dignity",
        "from": "concept.univocidad_ser.aa6",
        "to": "concept.dignidad_ser.aa6",
        "type": "condition_of",
        "evidence_status": "explicit",
        "evidence": ["ev.aa6.dignity", "ev.aa6.dignity_modes"],
    },
    {
        "id": "rel.aa6.dignity_refines_telar",
        "from": "concept.dignidad_ser.aa6",
        "to": "concept.dignity.telar",
        "type": "refines",
        "evidence_status": "inferred",
        "evidence": ["ev.aa6.dignity", "ev.telar.ch4.dignity"],
        "rationale": "AA-VI fija explícitamente el ser, no la humanidad, subjetividad o agencia, como alcance de la dignidad ontológica y separa esa univocidad de las categorías normativas.",
    },
    {
        "id": "rel.aa6.predication_requires_bridge",
        "from": "concept.predicacion_localizada.aa6",
        "to": "method.puente_rawlsiano.aa6",
        "type": "requires",
        "evidence_status": "explicit",
        "evidence": ["ev.aa6.predication", "ev.aa6.bridges"],
        "note": "El puente es exigible cuando una conclusión pretende migrar entre escalas, dominios o registros y no se sigue por necesidad declarada dentro del mismo sistema.",
    },
    {
        "id": "rel.aa6.tautology_applies_bridge",
        "from": "method.tautologia_euclidiana.aa6",
        "to": "method.puente_rawlsiano.aa6",
        "type": "applies",
        "evidence_status": "explicit",
        "evidence": ["ev.aa6.bridges"],
        "note": "AA-VI somete incluso el propio puente rawlsiano al control de sus condiciones constitutivas.",
    },
    {
        "id": "rel.aa6.noumenon_limits_exhaustivity",
        "from": "concept.limite_noumenico.aa6",
        "to": "concept.predicacion_localizada.aa6",
        "type": "condition_of",
        "evidence_status": "explicit",
        "evidence": ["ev.aa6.noumenon", "ev.aa6.predication"],
        "note": "El límite no niega verdad fenoménica; impide convertirla en predicación exhaustiva del ser qua ser.",
    },
    {
        "id": "rel.aa6.knowledge_applies_predication",
        "from": "concept.conocimiento_situado.aa6",
        "to": "concept.predicacion_localizada.aa6",
        "type": "applies",
        "evidence_status": "explicit",
        "evidence": ["ev.aa6.knowledge", "ev.aa6.noumenon"],
    },
    {
        "id": "rel.aa6.sentence_distinguished_predication",
        "from": "concept.sentencia_ontologica.aa6",
        "to": "concept.predicacion_localizada.aa6",
        "type": "distinguished_from",
        "evidence_status": "explicit",
        "evidence": ["ev.aa6.critique"],
    },
    {
        "id": "rel.aa6.responsibility_distinguished_sentence",
        "from": "concept.responsabilidad_sin_sentencia.aa6",
        "to": "concept.sentencia_ontologica.aa6",
        "type": "distinguished_from",
        "evidence_status": "explicit",
        "evidence": ["ev.aa6.causality_norm", "ev.aa6.responsibility"],
    },
    {
        "id": "rel.aa6.responsibility_refines_causal",
        "from": "concept.responsabilidad_sin_sentencia.aa6",
        "to": "concept.responsabilidad_causal",
        "type": "refines",
        "evidence_status": "inferred",
        "evidence": ["ev.aa6.responsibility", "ev.caos.glossary_responsibility"],
        "rationale": "AA-VI conserva reconstrucción causal e imputación, pero explicita que ninguna de ellas requiere una sentencia sobre el ser qua ser del agente.",
    },
    {
        "id": "rel.aa6.constitutive_applies_sum",
        "from": "concept.ley_constitutiva.aa6",
        "to": "concept.sum.aa6",
        "type": "applies",
        "evidence_status": "explicit",
        "evidence": ["ev.aa6.causality_norm"],
    },
    {
        "id": "rel.aa6.constitutive_applies_dignity",
        "from": "concept.ley_constitutiva.aa6",
        "to": "concept.dignidad_ser.aa6",
        "type": "applies",
        "evidence_status": "explicit",
        "evidence": ["ev.aa6.causality_norm"],
    },
]
append_unique(data["relations"], relations, "relations")

# ── Review nueva: única adjudicación transversal que AA-VI deja abierta ─
reviews = [
    {
        "id": "review.aa6.sum_crosswalk",
        "status": "pending_authorial_adjudication",
        "subject": "concept.sum.aa6",
        "related_relation": "rel.aa6.sum_reframes_aa5",
        "question": "¿El sum de AA-VI —ser/estar como ejes intrínsecos del mismo fenómeno— sustituye o redefine el sum de AA-V —identidad, voluntad y primera mediación antes del acto asumido—, o deben conservarse como formulaciones históricas de alcance distinto?",
        "why_not_auto_resolved": "Las dos formulaciones son materialmente distintas y AA-VI es posterior, pero el texto no adjudica expresamente la relación histórica con el uso técnico de sum en AA-V.",
        "blocking": False,
        "blocking_for": [],
        "evidence": ["ev.aa6.sum", "ev.aa5.ego.formulas"],
    }
]
append_unique(data["review_queue"], reviews, "review_queue")

# ── Resoluciones de mantenimiento sobre reviews históricas ─────────────
for review_id in (
    "review.telar.equality_dignity",
    "review.telar.dignity_scope",
    "review.telar.nonviolence_inference",
):
    review = get_by_id(data["review_queue"], review_id)
    review["maintenance_resolution"] = RESOLUTION
    review["maintenance_note"] = (
        "AA-VI aporta formulación autoral posterior. Conservar esta review como hallazgo histórico y consultar la resolución antes de tratarla como contradicción doctrinal vigente."
    )

# ── Rutas ───────────────────────────────────────────────────────────────
routes = [
    {
        "id": "route.aa6.ontology",
        "purpose": "Recuperar la arquitectura ontológica de AA-VI: Caos, sum, univocidad y dignidad sin confundir modos de ser con identidad categorial.",
        "triggers": ["Nikomachos", "sum en Nikomachos", "ser y estar", "univocidad", "dignidad ontológica", "ser qua ser"],
        "steps": [
            {"order": 1, "evidence_id": "ev.aa6.caos", "reason": "Fija el suelo previo a la determinación."},
            {"order": 2, "evidence_id": "ev.aa6.sum", "reason": "Define ser/estar y sum."},
            {"order": 3, "evidence_id": "ev.aa6.dignity", "reason": "Deriva univocidad y dignidad."},
            {"order": 4, "evidence_id": "ev.aa6.dignity_modes", "reason": "Distingue univocidad de identidad categorial y embargo."},
        ],
        "must_surface_review_items": ["review.aa6.sum_crosswalk"],
    },
    {
        "id": "route.aa6.predication",
        "purpose": "Recuperar la gramática de predicación de AA-VI, sus puentes explícitos, límites epistémicos y control de exhaustividad.",
        "triggers": ["predicación", "escala", "jurisdicción", "puente rawlsiano", "tautología euclidiana", "noúmeno", "cosa en sí"],
        "steps": [
            {"order": 1, "evidence_id": "ev.aa6.predication", "reason": "Fija escala, dominio y jurisdicción."},
            {"order": 2, "evidence_id": "ev.aa6.bridges", "reason": "Hace explícitas las mediaciones entre premisa y conclusión."},
            {"order": 3, "evidence_id": "ev.aa6.knowledge", "reason": "Distingue conocimiento situado de agotamiento."},
            {"order": 4, "evidence_id": "ev.aa6.noumenon", "reason": "Fija el límite nouménico sin destruir el conocimiento fenoménico."},
        ],
        "must_surface_review_items": [],
    },
    {
        "id": "route.aa6.responsibility",
        "purpose": "Recuperar acto, crítica, causalidad, norma y responsabilidad sin convertir imputación en sentencia ontológica.",
        "triggers": ["sentencia ontológica", "monstruo", "maldad", "acto", "causalidad", "tornado", "responsabilidad", "Caelus", "coerción"],
        "steps": [
            {"order": 1, "evidence_id": "ev.aa6.act", "reason": "Sitúa acto y trayectoria."},
            {"order": 2, "evidence_id": "ev.aa6.critique", "reason": "Distingue crítica severa de esencialización."},
            {"order": 3, "evidence_id": "ev.aa6.causality_norm", "reason": "Distingue causar, imputar y prescribir."},
            {"order": 4, "evidence_id": "ev.aa6.responsibility", "reason": "Integra reconstrucción causal, sanción y dignidad no embargable."},
            {"order": 5, "evidence_id": "ev.aa6.epilogue", "reason": "Recupera la síntesis del libro."},
        ],
        "must_surface_review_items": [],
    },
]
append_unique(data["routes"], routes, "routes")

# ── Metadatos del mapa ─────────────────────────────────────────────────
data["map_version"] = "2.12.0"
data["scope_note"] = (
    data.get("scope_note", "")
    + " MANT integra incrementalmente AA-VI, Afrodita Areia: Nikomachos, como corpus posterior: conserva las formulaciones históricas, añade sus nuevos objetos y relaciones, registra resoluciones de dignidad/predicación y deja abierto el crosswalk de sum AA-V↔AA-VI para adjudicación autoral."
).strip()

MAP.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(
    "AA-VI integrado al mapa:",
    len(evidence), "evidencias,",
    len(nodes), "nodos,",
    len(relations), "relaciones,",
    len(routes), "rutas,",
    len(reviews), "review nueva."
)
