# Paradigma

Repositorio documental del corpus filosófico de Miguel Hilario Olvera Aguilar.

## Principio de trabajo

**Fuente íntegra → obra/volumen → capítulo → secciones internas.**

Los archivos que se incorporen a `corpus/fuentes/` serán la referencia canónica. Las carpetas de `corpus/libros/` contendrán copias segmentadas para lectura, indexación y análisis automatizado. Ante cualquier discrepancia, prevalece siempre la fuente íntegra.

## Corpus inicial

El primer lote está formado por nueve textos:

- *Caos: El abismo del ego y la doble mediación*.
- *Afrodita Areia: Sobre la pasión* — Vol. I.
- *Afrodita Areia: Ágape* — Vol. II.
- *Afrodita Areia: Damasén* — Vol. III.
- *Afrodita Areia: Areópago* — Vol. IV.
- *Afrodita Areia: Caelus* — Vol. V.
- *El dilema de Aquiles o la disociación del ego*.
- *El juego de las máscaras o la disforia de la identidad*.
- *El telar de las Moiras: Ontología de la autodeterminación causal*.

Los cinco volúmenes de *Afrodita Areia* se mantienen agrupados como una sola obra articulada en cinco volúmenes.

## Integridad

Las fuentes no deben normalizarse, resumirse ni corregirse silenciosamente. Si una conversión a Markdown contiene un error respecto de la edición fuente, la corrección deberá quedar documentada. Cada fuente incorporada tendrá una suma SHA-256 para permitir comprobaciones de integridad.

## Estructura prevista

```text
corpus/
├── fuentes/
├── libros/
│   ├── afrodita-areia/
│   ├── caos/
│   ├── dilema-de-aquiles/
│   ├── juego-de-las-mascaras/
│   └── telar-de-las-moiras/
└── catalogo.json

documentacion/
scripts/
```

Las subsecciones internas permanecerán dentro de su capítulo para conservar el contexto argumental. Prefacios, prólogos, epílogos, apéndices y glosarios podrán mantenerse como unidades independientes cuando la obra los distinga estructuralmente.
