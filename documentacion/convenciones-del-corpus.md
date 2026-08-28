# Convenciones del corpus

## 1. Fuente canónica

Cada archivo de `corpus/fuentes/` conserva el Markdown recibido sin modificaciones. Su suma SHA-256 queda registrada en `corpus/fuentes/SHA256SUMS.txt`.

## 2. Segmentación

La segmentación sirve para lectura, indexación y análisis automatizado. No sustituye a la fuente. Los cortes se realizan únicamente en encabezados estructurales identificados de forma conservadora. No se corta por cualquier cadena que contenga la palabra «Capítulo», porque la conversión de origen contiene encabezados espurios dentro de referencias y del cuerpo del texto.

## 3. Unidad de análisis

La unidad ordinaria será el capítulo. Prefacios, prólogos, epílogos, apéndices y glosarios se conservan como unidades independientes cuando la estructura de la obra los distingue. Las subsecciones internas permanecen dentro del capítulo.

## 4. Correcciones

No se corrige una fuente canónica por criterios estilísticos, doctrinales o editoriales. Si se detecta un error de conversión, la corrección debe quedar documentada y verificarse contra la edición fuente.

## 5. Capas futuras

Glosarios normalizados, mapas conceptuales, índices semánticos, axiomas, relaciones entre obras, notas analíticas y resultados de herramientas deberán vivir fuera de `corpus/fuentes/`.
