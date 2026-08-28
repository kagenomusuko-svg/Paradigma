# Paradigma

Repositorio documental para el corpus filosófico de Miguel Hilario Olvera Aguilar.

## Regla de integridad

Los archivos de `corpus/fuentes/` son las fuentes canónicas recibidas en Markdown. No deben modificarse para normalizar estilo, corregir contenido, reinterpretar conceptos ni facilitar análisis. Una corrección solo corresponde cuando se comprueba que el Markdown no reproduce fielmente la edición fuente.

Las carpetas de `corpus/libros/` contienen copias segmentadas para consulta y análisis. La segmentación es derivada: ante cualquier discrepancia, prevalece el archivo íntegro de `corpus/fuentes/`.

## Estructura inicial

- `corpus/fuentes/`: nueve textos íntegros y sus sumas SHA-256.
- `corpus/libros/afrodita-areia/`: los cinco volúmenes de *Afrodita Areia*, tratados como una obra articulada en cinco volúmenes.
- `corpus/libros/caos/`
- `corpus/libros/dilema-de-aquiles/`
- `corpus/libros/juego-de-las-mascaras/`
- `corpus/libros/telar-de-las-moiras/`
- `corpus/catalogo.json`: catálogo legible por programas con rutas, integridad y segmentación.
- `documentacion/convenciones-del-corpus.md`: reglas de edición y trabajo.

## Principio de trabajo

**Fuente íntegra → obra/volumen → capítulo → secciones internas.**

Las subsecciones internas permanecen dentro de su capítulo para conservar contexto argumental.
