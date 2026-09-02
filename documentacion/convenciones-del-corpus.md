# Convenciones del corpus

## 1. Fuente canónica

Cada archivo de `corpus/fuentes/` conserva el Markdown recibido sin modificaciones. Su suma SHA-256 queda registrada en `corpus/fuentes/SHA256SUMS.txt`.

## 2. Segmentación

La segmentación sirve para lectura, indexación y análisis automatizado. No sustituye a la fuente. Los cortes se realizan únicamente en encabezados estructurales identificados de forma conservadora. No se corta por cualquier cadena que contenga la palabra «Capítulo», porque la conversión de origen contiene encabezados espurios dentro de referencias y del cuerpo del texto.

## 3. Unidad de análisis

La unidad ordinaria de segmentación será el capítulo. Prefacios, prólogos, epílogos, apéndices y glosarios se conservan como unidades independientes cuando la estructura de la obra los distingue. Las subsecciones internas permanecen dentro del capítulo.

La unidad ordinaria del mapa semántico no es necesariamente el capítulo: es la unidad conceptual relevante. Cada unidad semántica debe conservar proveniencia suficiente para regresar a la estructura documental y a la fuente canónica.

## 4. Correcciones

No se corrige una fuente canónica por criterios estilísticos, doctrinales o editoriales. Si se detecta un error de conversión, la corrección debe quedar documentada y verificarse contra la edición fuente.

Las propuestas de corrección doctrinal o estilística se trabajan como productos separados. No se incorporan silenciosamente a la fuente ni a las capas derivadas.

## 5. Capas derivadas

Glosarios normalizados, mapas conceptuales, índices semánticos, axiomas, relaciones entre obras, notas analíticas y resultados de herramientas viven fuera de `corpus/fuentes/`.

El mapa maestro vive en `mapa/` y se rige por `documentacion/protocolo-mapa-maestro.md`.

## 6. Precedencia

Ante discrepancia:

1. prevalece la fuente canónica para establecer qué dice el texto;
2. `estructura.json` y el catálogo sirven para localizarlo;
3. el mapa semántico sirve para navegar e interpretar relaciones, pero debe declarar cuándo una relación es inferida;
4. los productos derivados no adquieren autoridad retroactiva sobre ninguna capa anterior.