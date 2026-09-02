# Arquitectura operativa de Paradigma

## 1. Propósito

Paradigma debe conservar un corpus filosófico verificable y permitir que una persona o sistema artificial encuentre el pasaje correcto antes de explicar, enseñar, corregir o programar a partir de la obra.

El repositorio no debe convertirse en una copia del corpus fragmentada en metadatos. La lectura del Markdown sigue siendo la operación interpretativa principal.

## 2. Capas y autoridad

### Capa 0 — Fuente canónica

Ruta: `corpus/fuentes/`

Contiene los Markdown íntegros recibidos y `SHA256SUMS.txt`.

Autoridad: máxima.

Regla: no se modifica para normalizar estilo, reparar doctrina, facilitar búsquedas ni adaptar el texto a herramientas.

### Capa 1 — Estructura documental

Rutas: `corpus/libros/` y `corpus/catalogo-generado.json`.

Contiene copias segmentadas, `estructura.json`, localizadores y catálogo global.

Autoridad: derivada. Si existe discrepancia, prevalece la fuente canónica.

Función: responder **dónde está** un contenido.

### Capa 2 — Mapa semántico

Ruta: `mapa/`.

Contendrá conceptos, formulaciones, relaciones, objetos formales, proveniencia y rutas de lectura.

Autoridad: analítica y derivada. Nunca sustituye a la fuente.

Función: responder **qué debe leerse para comprender correctamente una pregunta**.

### Capa 3 — Productos de uso

Incluye, cuando existan, materiales de diplomado, revisiones editoriales, motores de cálculo, interfaces y otros productos.

Función: aplicar el corpus. Estos productos no redefinen retrospectivamente el corpus ni el mapa.

## 3. Modelo mental del repositorio

La carpeta visualmente más grande es `corpus/libros/`, pero no es el centro intelectual del proyecto. Es una caché estructural regenerable.

Para orientarse se sigue este orden:

1. `README.md` para saber qué capa usar.
2. `corpus/catalogo-generado.json` para localizar obras y segmentos.
3. `mapa/` para navegar conceptos y relaciones.
4. `corpus/fuentes/` o el segmento derivado indicado para leer contexto real.

No se usa el árbol completo de `corpus/libros/` como menú humano.

## 4. Qué se conserva aunque parezca voluminoso

Se conservan las copias segmentadas porque permiten lectura parcial, indexación y validación exacta contra la fuente.

Se conservan los scripts de segmentación especializados existentes. Su división histórica en lotes no es elegante, pero actualmente es estable y verifica reconstrucción byte a byte. Consolidarlos ahora produciría riesgo sin mejorar el objetivo semántico inmediato.

Regla: no refactorizar estos scripts salvo que ocurra una de estas condiciones:

- una fuente nueva no pueda registrarse sin duplicación peligrosa;
- un cambio de formato rompa la segmentación;
- aparezca una inconsistencia comprobable entre derivados y fuentes;
- el mantenimiento de los lotes impida una operación necesaria del mapa maestro.

La incomodidad estética no es criterio suficiente.

## 5. Qué se elimina o evita

- Catálogos estructurales antiguos que compitan con el catálogo generado vigente.
- Resúmenes presentados como sustitutos del texto.
- Tablas frase por frase sin una necesidad de recuperación demostrable.
- Clasificaciones semánticas sin proveniencia.
- Duplicados manuales de datos que ya pueden derivarse de `estructura.json`.
- Embeddings, similitud vectorial o inferencias automáticas tratados como verdad doctrinal.
- Nuevas carpetas o herramientas cuya única justificación sea preparar una futura preparación.

## 6. Invariantes

Toda evolución del repositorio debe preservar estos invariantes:

1. Una fuente canónica puede reconstruirse y verificarse por hash.
2. Cada segmento derivado conserva un vínculo inequívoco con su fuente.
3. El catálogo global se genera; no se mantiene manualmente.
4. Todo nodo semántico relevante posee proveniencia verificable.
5. Las inferencias del sistema se distinguen de las afirmaciones explícitas del corpus.
6. Las formulaciones históricas pueden coexistir con formulaciones posteriores.
7. Ninguna capa derivada corrige silenciosamente a otra.
8. Un cambio de esquema con datos existentes requiere una migración reproducible.

## 7. Regla de congelación arquitectónica

A partir del inicio del mapa maestro, la arquitectura básica queda congelada.

Un cambio estructural solo se aprueba cuando existe un caso de uso concreto que no puede resolverse correctamente con el diseño vigente. La propuesta de cambio debe indicar:

- qué consulta o tarea falla;
- por qué falla por estructura y no por falta de datos;
- qué modificación mínima lo resuelve;
- cómo se migran los datos existentes;
- qué prueba demuestra que el cambio solucionó el problema sin romper los casos anteriores.

No se reinicia manualmente el trabajo semántico por un cambio de criterio.