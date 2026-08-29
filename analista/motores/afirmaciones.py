#!/usr/bin/env python3
"""Motor conservador de afirmaciones proposicionales — Fase 4C v1.1.

Segmenta bloques proposicionales únicamente por señales textuales de voz y
fronteras formales. No convierte una atribución, objeción, condicional, ejemplo
o pregunta en tesis autoral; tampoco enlaza conceptos por coaparición.
"""
from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
UNIDADES = ROOT / "analista/generado/unidades.jsonl"
SALIDA = ROOT / "analista/generado/afirmaciones-candidatas.jsonl"
COBERTURA = ROOT / "analista/generado/cobertura-afirmaciones.jsonl"
PILOTO_ID = "AA-SP-V1"
SCHEMA_VERSION = "1.0.0"
MOTOR_VERSION = "1.1.0"

NOMBRES_REFERIDOS = (
    "Hume", "Spinoza", "Deleuze", "Bergson", "Heidegger", "Ricoeur",
    "Sartre", "Parfit", "Kierkegaard", "Maturana", "Varela",
    "Aristóteles", "Leibniz",
)
TERMINOS_TECNICOS = (
    "aego", "caos", "colapso", "determinación", "ego", "identidad",
    "mediación", "pasión", "responsabilidad", "autodeterminación", "φ₁",
    "φ₂", "integral", "sustancia", "causalidad", "conatus", "autopoiesis",
    "dasein", "libertad", "continuidad", "voluntad", "acto", "angustia",
    "mala fe", "sujeto",
)
SUPERINDICES = "¹²³⁴⁵⁶⁷⁸⁹⁰"
MOBILIARIO_RE = re.compile(r"^(?:Afrodita Areia:.*|#{1,6}\s.*|---|[IVXLCDM]+)$")
SIGUIENTE = rf"(?:[A-ZÁÉÍÓÚÜ¿¡Φφ]|[{SUPERINDICES}])"
FIN_ORACION_RE = re.compile(
    rf"(?:[.!?][ \t]*[{SUPERINDICES}]+|[.!?])(?=\s+{SIGUIENTE})"
)
PREFIJOS_META = (
    "esta distinción es el punto de partida",
    "para establecerla con precisión",
    "el capítulo anterior",
    "este capítulo",
    "para hacerlo,",
    "el segundo momento es",
    "el tercer momento es",
    "el primero es",
    "el segundo punto es",
    "la tercera es la pregunta",
    "la segunda es la pregunta",
    "lo que aquí se establece",
    "esta diferencia no es trivial",
)
PREFIJOS_SISTEMA = (
    "este sistema", "para este sistema", "en este sistema",
    "lo que este sistema", "con ambos este sistema",
)
PREFIJOS_AUTORALES = (
    "ese estado", "eso no equivale", "no es posible", "no entra",
    "no pienso", "lo que mantiene", "el segundo aspecto", "ese ego",
    "actúa desde ningún lugar", "desde la perspectiva",
)
PREFIJOS_FRAGMENTO_INICIAL = (
    "de ", "que ", "ser ", "precisa ", "tendencia ", "ofrece ",
    "sistema que ", "una identidad de cosa", "antemano", "estructura.",
)
PREFIJOS_EJEMPLO = (
    "la piedra que cae", "el imán que atrae", "la estrella que captura",
    "en el nivel de los organismos", "el organismo que", "el sistema inmune que",
)


def normalizar(texto: str) -> str:
    return " ".join(unicodedata.normalize("NFKC", texto).casefold().split())


def empieza(texto_normalizado: str, prefijos: tuple[str, ...]) -> bool:
    return any(texto_normalizado.startswith(prefijo) for prefijo in prefijos)


def stable_id(prefix: str, *parts: str) -> str:
    raw = "\x1f".join(parts).encode("utf-8")
    return f"{prefix}-{hashlib.sha1(raw).hexdigest()[:12].upper()}"


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def dump_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows),
        encoding="utf-8",
    )


def contexto_referido(unidad: dict) -> bool:
    seccion = normalizar(unidad.get("seccion") or "")
    return any(normalizar(nombre) in seccion for nombre in NOMBRES_REFERIDOS)


def inicio_sin_mobiliario(texto: str) -> int:
    pos = 0
    while pos < len(texto):
        salto = texto.find("\n", pos)
        fin = len(texto) if salto < 0 else salto
        linea = texto[pos:fin].strip()
        if MOBILIARIO_RE.match(linea):
            pos = fin + 1 if salto >= 0 else fin
        else:
            break
    while pos < len(texto) and texto[pos].isspace():
        pos += 1
    salto = texto.find("\n", pos)
    if salto >= 0:
        primera = texto[pos:salto].strip()
        resto = normalizar(texto[salto + 1 : salto + 100])
        if len(primera.split()) <= 4 and (
            resto.startswith("si ") or resto.startswith("podría parecer") or resto.startswith("¿")
        ):
            pos = salto + 1
    return pos


def oraciones(texto: str, inicio: int) -> list[tuple[int, int, str]]:
    spans: list[tuple[int, int, str]] = []
    actual = inicio
    for match in FIN_ORACION_RE.finditer(texto, inicio):
        fin = match.end()
        comienzo = actual
        while comienzo < fin and texto[comienzo].isspace():
            comienzo += 1
        if comienzo < fin:
            spans.append((comienzo, fin, texto[comienzo:fin]))
        actual = fin
        while actual < len(texto) and texto[actual].isspace():
            actual += 1
    if actual < len(texto):
        comienzo = actual
        while comienzo < len(texto) and texto[comienzo].isspace():
            comienzo += 1
        if comienzo < len(texto):
            spans.append((comienzo, len(texto), texto[comienzo:]))
    return spans


def completa(segmento: str) -> bool:
    return bool(re.search(rf"[.!?](?:[ \t]*[{SUPERINDICES}]+)?$", segmento.rstrip()))


def atribucion_externa(normalizado: str) -> bool:
    verbos = (
        "concluyó", "formuló", "introdujo", "construyó", "desarrolló",
        "entendía", "dice ", "decía ", "sostiene", "propone", "afirma", "señala",
    )
    if any(
        normalizado.startswith(("para " + normalizar(nombre), "en " + normalizar(nombre)))
        for nombre in NOMBRES_REFERIDOS
    ):
        return True
    if any(normalizado.startswith("lo que " + normalizar(nombre)) for nombre in NOMBRES_REFERIDOS):
        return True
    if normalizado.startswith("el dasein de heidegger"):
        return True
    if normalizado.startswith("la distinción es sutil pero decisiva: para spinoza"):
        return True
    if normalizado.startswith("pero ricoeur"):
        return True
    for nombre in NOMBRES_REFERIDOS:
        nombre_n = normalizar(nombre)
        if normalizado.startswith(nombre_n + " ") or normalizado.startswith(nombre_n + ","):
            if any(verbo in normalizado[:180] for verbo in verbos) or normalizado.startswith("deleuze,"):
                return True
    return False


def negacion_sistema(normalizado: str) -> bool:
    return any(
        marcador in normalizado
        for marcador in (
            "este sistema rechaza", "este sistema no puede aceptar",
            "este sistema no puede compartir", "este sistema no comparte",
        )
    )


def posicion_sistema(normalizado: str) -> bool:
    if empieza(normalizado, PREFIJOS_SISTEMA):
        return True
    if " este sistema " in " " + normalizado + " " and empieza(
        normalizado,
        (
            "el punto en que", "la coincidencia", "la libertad sartreana",
            "lo que la autopoiesis formaliza", "desde la perspectiva",
        ),
    ):
        return True
    return empieza(
        normalizado,
        (
            "la coincidencia entre esta tesis spinoziana",
            "la coincidencia con lo que este sistema",
            "la coincidencia entre esta distinción heideggeriana",
            "la coincidencia entre el argumento de parfit",
            "esa prioridad de la existencia",
            "pero todos los conceptos que el sistema",
            "en el nivel del sujeto",
        ),
    )


def clasificar_oracion(segmento: str, unidad: dict, *, primera: bool = False) -> tuple[str | None, bool]:
    literal = segmento.strip()
    normalizado = normalizar(literal)
    if not normalizado:
        return "drop", True
    if primera and literal[:1].islower() and empieza(normalizado, PREFIJOS_FRAGMENTO_INICIAL) and not contexto_referido(unidad):
        return "drop", True
    if empieza(normalizado, PREFIJOS_META):
        return "drop", True
    if empieza(normalizado, ("ares y afrodita no vencieron", "hermes escapó", "atenea escapó")):
        return "drop", True
    if normalizado.startswith("φ2:"):
        return "drop", True
    if normalizado.startswith("¿"):
        return "pregunta", True
    if empieza(normalizado, ("podría parecer", "se podría objetar", "podria parecer")):
        return "objecion", True
    if normalizado.startswith("si "):
        return "formulacion_condicional", True
    if empieza(normalizado, PREFIJOS_EJEMPLO):
        return "ejemplo", True
    if negacion_sistema(normalizado):
        return "negacion_autoral", True
    if literal[:1] in SUPERINDICES and any(normalizar(nombre) in normalizado[:80] for nombre in NOMBRES_REFERIDOS):
        return "discurso_referido", True
    if atribucion_externa(normalizado):
        return "discurso_referido", True
    if posicion_sistema(normalizado):
        return "afirmacion_autoral", True
    if normalizado.startswith("pero la ontología spinoziana") and "este sistema no" in normalizado:
        return "negacion_autoral", True
    if empieza(normalizado, PREFIJOS_AUTORALES):
        return (
            "negacion_autoral" if empieza(normalizado, ("no es posible", "no entra"))
            else "afirmacion_autoral",
            True,
        )
    if primera:
        if empieza(normalizado, PREFIJOS_FRAGMENTO_INICIAL):
            return "drop", True
        if contexto_referido(unidad):
            return "discurso_referido", False
        if literal[:1].islower() and not normalizado.startswith("actúa "):
            return "drop", True
        if any(termino in normalizado for termino in TERMINOS_TECNICOS) and len(normalizado.split()) >= 8:
            return "afirmacion_autoral", False
    return None, False


def material(literal: str, estatus: str, anclado: bool) -> bool:
    normalizado = normalizar(literal)
    if len(normalizado.split()) < 5:
        return False
    if anclado or estatus in {"discurso_referido", "cita"}:
        return True
    return any(termino in normalizado for termino in TERMINOS_TECNICOS)


def unidad_editorial(unidad: dict) -> bool:
    """Excluye portada/índice/títulos convertidos a párrafo, no prosa doctrinal."""
    texto = unidad["texto_literal"].strip()
    loc = unidad["localizacion"]
    if unidad["archivo"].endswith("00-preliminares.md") and loc["linea_inicio"] < 57:
        return True
    if re.search(r"[.!?¿¡]", texto):
        return False
    lineas = [linea.strip() for linea in texto.splitlines() if linea.strip()]
    if loc["linea_inicio"] <= 3 and len(lineas) <= 5:
        return True
    if (unidad.get("seccion") or "").startswith("Parte ") and len(lineas) <= 3:
        return True
    if lineas and normalizar(lineas[0]).startswith(("prefacio ", "prólogo ", "prologo ", "narciso o ")) and len(lineas) <= 3:
        return True
    return False


def bloques(unidad: dict) -> list[tuple[int, int, str, str, str]]:
    if unidad.get("tipo_estructural") in {"encabezado", "separador"} or unidad["archivo"].endswith("99-glosario.md"):
        return []
    texto = unidad["texto_literal"]
    limpio = texto.strip()
    if limpio.startswith("«") and limpio.endswith("»"):
        inicio = texto.index("«")
        fin = texto.rindex("»") + 1
        return [(inicio, fin, "cita", "afirmacion_explicita", texto[inicio:fin])]
    if unidad_editorial(unidad):
        return []
    spans = oraciones(texto, inicio_sin_mobiliario(texto))
    cerrados: list[dict] = []
    actual: dict | None = None
    suprimir = False
    permitir_reinicio_externo = False

    for indice, (inicio, fin, segmento) in enumerate(spans):
        estatus, forzado = clasificar_oracion(segmento, unidad, primera=(indice == 0))
        es_completa = completa(segmento)
        normalizado = normalizar(segmento)

        if estatus == "drop":
            if actual:
                cerrados.append(actual)
                actual = None
            if indice == 0:
                suprimir = False
                permitir_reinicio_externo = contexto_referido(unidad)
            else:
                suprimir = True
            continue

        if estatus is not None:
            suprimir = False
            permitir_reinicio_externo = False
            if (
                actual
                and actual["estatus"] == "discurso_referido"
                and estatus == "discurso_referido"
                and not es_completa
                and indice == len(spans) - 1
                and segmento.lstrip()[:1] in SUPERINDICES
            ):
                cerrados.append(actual)
                actual = None
                continue
            if actual is None:
                actual = {
                    "inicio": inicio, "fin": fin, "estatus": estatus, "anclado": forzado,
                    "completo": es_completa, "oraciones": 1, "inicio_normalizado": normalizado,
                }
                continue
            if actual["estatus"] == estatus and forzado and not actual["anclado"]:
                cerrados.append(actual)
                actual = {
                    "inicio": inicio, "fin": fin, "estatus": estatus, "anclado": True,
                    "completo": es_completa, "oraciones": 1, "inicio_normalizado": normalizado,
                }
                continue
            if (
                actual["estatus"] == "negacion_autoral"
                and estatus == "afirmacion_autoral"
                and normalizado.startswith(("para este sistema", "en este sistema"))
            ):
                actual["fin"] = fin
                actual["completo"] = es_completa
                actual["oraciones"] += 1
                continue
            nuevo = actual["estatus"] != estatus
            if actual["estatus"] == estatus:
                if estatus in {"formulacion_condicional", "objecion", "pregunta"}:
                    nuevo = True
                elif estatus == "afirmacion_autoral" and normalizado.startswith("pero todos "):
                    nuevo = True
                elif estatus == "discurso_referido" and normalizado.startswith("lo que "):
                    nuevo = True
            if nuevo:
                cerrados.append(actual)
                actual = {
                    "inicio": inicio, "fin": fin, "estatus": estatus, "anclado": forzado,
                    "completo": es_completa, "oraciones": 1, "inicio_normalizado": normalizado,
                }
            else:
                actual["fin"] = fin
                actual["anclado"] = actual["anclado"] or forzado
                actual["completo"] = es_completa
                actual["oraciones"] += 1
            continue

        if suprimir:
            continue
        if actual is None:
            if permitir_reinicio_externo:
                estatus0, anclado0 = clasificar_oracion(segmento, unidad, primera=True)
                if estatus0 not in (None, "drop"):
                    actual = {
                        "inicio": inicio, "fin": fin, "estatus": estatus0, "anclado": anclado0,
                        "completo": es_completa, "oraciones": 1, "inicio_normalizado": normalizado,
                    }
                    permitir_reinicio_externo = False
            continue
        if actual["estatus"] in {"formulacion_condicional", "objecion", "pregunta"}:
            cerrados.append(actual)
            actual = None
            suprimir = True
            continue
        if not es_completa and indice == len(spans) - 1:
            cola = segmento.strip()
            if cola and all(caracter in SUPERINDICES for caracter in cola):
                actual["fin"] = fin
                actual["completo"] = True
                actual["oraciones"] += 1
            elif normalizado.startswith("existir ") or (
                normalizado.startswith("y ") and actual["inicio_normalizado"].startswith("la coincidencia")
            ):
                actual["fin"] = fin
                actual["completo"] = False
                actual["oraciones"] += 1
            else:
                cerrados.append(actual)
                actual = None
            continue
        actual["fin"] = fin
        actual["completo"] = es_completa
        actual["oraciones"] += 1

    if actual:
        cerrados.append(actual)

    fusionados: list[dict] = []
    for bloque in cerrados:
        if (
            fusionados
            and fusionados[-1]["estatus"] == "discurso_referido"
            and bloque["estatus"] == "discurso_referido"
            and bloque["completo"]
            and bloque["inicio_normalizado"].startswith("lo que ")
        ):
            fusionados[-1]["fin"] = bloque["fin"]
            fusionados[-1]["completo"] = bloque["completo"]
            fusionados[-1]["oraciones"] += bloque["oraciones"]
            fusionados[-1]["anclado"] = fusionados[-1]["anclado"] or bloque["anclado"]
        else:
            fusionados.append(bloque)

    salida: list[tuple[int, int, str, str, str]] = []
    for bloque in fusionados:
        inicio, fin = bloque["inicio"], bloque["fin"]
        while inicio < fin and texto[inicio].isspace():
            inicio += 1
        while fin > inicio and texto[fin - 1].isspace():
            fin -= 1
        literal = texto[inicio:fin]
        marcador = re.search(r"\n[IVXLCDM]+\s*$", literal)
        if marcador:
            fin = inicio + marcador.start()
            literal = texto[inicio:fin].rstrip()
            fin = inicio + len(literal)
        if not material(literal, bloque["estatus"], bloque["anclado"]):
            continue
        if normalizar(literal) == "lo que este sistema propone":
            continue
        clasificacion = "afirmacion_explicita" if completa(literal) else "afirmacion_candidata"
        salida.append((inicio, fin, bloque["estatus"], clasificacion, literal))
    return salida


def rango_lineas(unidad: dict, inicio: int, fin: int) -> tuple[int, int]:
    texto = unidad["texto_literal"]
    base = unidad["localizacion"]["linea_inicio"]
    return base + texto[:inicio].count("\n"), base + texto[:fin].count("\n")


def base(record_id: str, kind: str, literal: str | None, extraction: str, audit: str, status: str | None = None) -> dict:
    return {
        "id": record_id,
        "tipo_registro": kind,
        "schema_version": SCHEMA_VERSION,
        "texto_literal": literal,
        "normalizacion_formal": None,
        "normalizacion_lexica": None,
        "estatus_enunciativo": status,
        "estado_extraccion": extraction,
        "estado_verificacion": "pendiente",
        "estado_auditoria": audit,
        "producido_por": {"motor": "afirmaciones", "version": MOTOR_VERSION},
    }


def main() -> int:
    unidades = load_jsonl(UNIDADES)
    pilot_units = [u for u in unidades if u.get("fuente_id") == PILOTO_ID]
    if not pilot_units:
        raise SystemExit(f"No existen unidades de {PILOTO_ID}")

    registros: list[dict] = []
    ids: set[str] = set()
    for unidad in pilot_units:
        for inicio, fin, estatus, clasificacion, literal in bloques(unidad):
            linea_inicio, linea_fin = rango_lineas(unidad, inicio, fin)
            record_id = stable_id(
                "AF", unidad["id"], str(inicio), str(fin), estatus, clasificacion, literal
            )
            if record_id in ids:
                raise SystemExit(f"ID de afirmación duplicado: {record_id}")
            ids.add(record_id)
            extraccion = "extraido" if clasificacion == "afirmacion_explicita" else "candidato"
            record = base(record_id, "afirmacion", literal, extraccion, "pendiente", estatus)
            record.update(
                {
                    "fuente_id": PILOTO_ID,
                    "unidad_id": unidad["id"],
                    "concepto_ids": [],
                    "clasificacion_afirmacion": clasificacion,
                    "sujeto_literal": None,
                    "predicado_literal": None,
                    "objeto_literal": None,
                    "localizacion": {
                        "ruta": unidad["archivo"],
                        "linea_inicio": linea_inicio,
                        "linea_fin": linea_fin,
                    },
                    "criterio_deteccion": (
                        "bloque_proposicional_delimitado_por_marcadores_textuales_de_voz_y_fronteras_formales; "
                        "sin_atribucion_autoral_por_coaparicion"
                    ),
                    "confianza_extraccion": None,
                }
            )
            registros.append(record)

    registros.sort(
        key=lambda r: (
            r["localizacion"]["ruta"], r["localizacion"]["linea_inicio"],
            r["localizacion"]["linea_fin"], r["id"],
        )
    )
    dump_jsonl(SALIDA, registros)

    coverage = base(
        stable_id("COB", PILOTO_ID, "afirmaciones", MOTOR_VERSION),
        "reporte_cobertura", None, "extraido", "no_aplica", None,
    )
    coverage.update(
        {
            "obra_id": PILOTO_ID,
            "motor": "afirmaciones",
            "version_motor": MOTOR_VERSION,
            "unidades_totales": len(pilot_units),
            "unidades_procesadas": len(pilot_units),
            "unidades_omitidas": [],
            "errores": [],
        }
    )
    dump_jsonl(COBERTURA, [coverage])

    por_estatus: dict[str, int] = {}
    for registro in registros:
        por_estatus[registro["estatus_enunciativo"]] = por_estatus.get(registro["estatus_enunciativo"], 0) + 1
    print(
        json.dumps(
            {
                "motor": "afirmaciones",
                "version": MOTOR_VERSION,
                "unidades": len(pilot_units),
                "registros": len(registros),
                "explicitas": sum(r["clasificacion_afirmacion"] == "afirmacion_explicita" for r in registros),
                "candidatas": sum(r["clasificacion_afirmacion"] == "afirmacion_candidata" for r in registros),
                "estatus": dict(sorted(por_estatus.items())),
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
