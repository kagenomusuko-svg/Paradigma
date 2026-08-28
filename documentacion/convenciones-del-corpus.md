# Convenciones del corpus

## 1. Fuente canónica

Cada archivo de `corpus/fuentes/` debe conservar el Markdown recibido sin modificaciones de contenido. Su suma SHA-256 se registrará para comprobar integridad.

## 2. Segmentación

La segmentación sirve para lectura, indexación y análisis automatizado. No sustituye a la fuente. Los cortes se realizan únicamente en encabezados estructurales identificados de forma conservadora.

No se corta por cualquier cadena que contenga la palabra «Capítulo». La conversión de origen puede contener encabezados espurios dentro de referencias, notas o del propio cuerpo del texto.

## 3. Unidad ordinaria de análisis

La unidad ordinaria será el capítulo. Prefacios, prólogos, epílogos, apéndices y glosarios se conservarán como unidades independientes cuando la estructura de la obra los distinga. Las subsecciones internas permanecerán dentro del capítulo para conservar contexto argumental.

## 4. Correcciones

No se corrige una fuente canónica por criterios estilísticos, doctrinales o editoriales. Si se detecta un error de conversión, la corrección debe documentarse y verificarse contra la edición fuente.

## 5. Capas derivadas

Glosarios normalizados, mapas conceptuales, índices semánticos, axiomas, relaciones entre obras, notas analíticas y resultados de herramientas deben vivir fuera de `corpus/fuentes/`.

## 6. Regla de precedencia

Ante cualquier discrepancia entre una copia segmentada y la fuente íntegra, prevalece la fuente íntegra.
