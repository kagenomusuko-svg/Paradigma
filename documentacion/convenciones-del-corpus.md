# Convenciones del corpus

> **Documento técnico no normativo.** Las instrucciones operativas completas y vigentes están en `/INSTRUCCIONES.md`. Este archivo describe decisiones de implementación documental y no añade reglas nuevas.

## 1. Fuente canónica

Cada archivo de `corpus/fuentes/` conserva el Markdown recibido sin modificaciones. Su suma SHA-256 queda registrada en `corpus/fuentes/SHA256SUMS.txt`.

## 2. Segmentación

La segmentación sirve para lectura, indexación y análisis automatizado. No sustituye a la fuente. Los cortes se realizan únicamente en encabezados estructurales identificados de forma conservadora. No se corta por cualquier cadena que contenga la palabra «Capítulo», porque la conversión de origen contiene encabezados espurios dentro de referencias y del cuerpo del texto.

## 3. Unidad documental

La unidad ordinaria de segmentación es el capítulo. Prefacios, prólogos, epílogos, apéndices y glosarios se conservan como unidades independientes cuando la estructura de la obra los distingue. Las subsecciones internas permanecen dentro del capítulo.

La unidad semántica del mapa puede ser distinta y conserva proveniencia hacia esta estructura documental.

## 4. Correcciones de conversión

Cuando se detecta un error de conversión, la comparación se realiza contra la edición fuente y el cambio debe quedar documentado.

Las revisiones estilísticas o doctrinales pertenecen a productos editoriales separados.

## 5. Capas derivadas

Glosarios normalizados, mapas conceptuales, índices semánticos, axiomas, relaciones entre obras, notas analíticas y resultados de herramientas viven fuera de `corpus/fuentes/`.

## 6. Precedencia documental

Para determinar qué dice el texto, la fuente canónica es la referencia. `estructura.json` y el catálogo localizan; el mapa semántico relaciona y orienta; los productos derivados aplican.