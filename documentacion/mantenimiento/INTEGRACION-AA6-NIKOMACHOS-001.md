# Integración AA-VI — Nikomachos

- **FASE:** MANT — mantenimiento posterior al mapa maestro v1
- **OBJETO:** `AA-VI` — *Afrodita Areia: Nikomachos — El límite de la predicación*
- **ESTADO:** HECHO

## Fuente canónica

La obra quedó incorporada como:

`corpus/fuentes/Afrodita_Areia_Nikomachos.md`

SHA-256:

`5ad5ca58854ab1664dd41e6027ea30f29cc6e5217ee7210e14a612a684a08a21`

Las piezas multipartes usadas para la transferencia no son autoridad paralela dentro de `Paradigma`.

## Estructura derivada

La obra quedó segmentada en:

`corpus/libros/afrodita-areia/06-nikomachos/`

La estructura conserva preliminares, prólogo, doce capítulos y epílogo. `corpus/catalogo.json` y `corpus/fuentes/SHA256SUMS.txt` fueron regenerados por los mecanismos ordinarios del repositorio.

## Integración al mapa maestro

La integración incremental del mapa quedó registrada en:

`901fb0c80cf1584f1ef98f80ab0dc665588b4a71`

El mapa incorpora AA-VI sin reconstruir ni reemplazar las formulaciones históricas previas. Se añadieron evidencia, nodos, relaciones y rutas propias de Nikomachos.

Se conserva la cola histórica de reviews. Cuando AA-VI aporta una respuesta textual posterior, la review histórica puede quedar vinculada a esa resolución sin borrarse como rastro de auditoría.

La resolución específica sobre dignidad y predicación queda en:

`documentacion/resolucion-nikomachos-dignidad-predicacion.md`

AA-VI deja además explícitamente abierto el crosswalk entre el uso de `sum` en AA-V y su formulación posterior en AA-VI; no se adjudicó retrospectivamente por inferencia.

## Validación

La integración fue ejecutada en CI y `scripts/validar_mapa.py` concluyó correctamente antes del commit del mapa.

No se modificaron las fuentes canónicas históricas anteriores para acomodar AA-VI.

## Consecuencia

`Paradigma` vuelve a quedar como autoridad histórica completa para el corpus que entra a la campaña de normalización.

La segunda edición no se escribe aquí. `kagenomusuko-svg/normalizacion` debe consumir el mapa maestro actualizado y volver a las fuentes canónicas sólo cuando una decisión concreta lo requiera.

## SIGUIENTE

> **`normalizacion` — N1: recorrer directamente el mapa maestro actualizado, resolver las tensiones con consecuencia 2E y crear reglas de normalización mínimas; no crear inventarios paralelos.**
