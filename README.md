# Paradigma

Repositorio documental y semántico del corpus filosófico de Miguel Hilario Olvera Aguilar.

## Antes de trabajar

**Leer únicamente `INSTRUCCIONES.md` como fuente normativa del repositorio.**

Ese archivo define de forma completa:

- propósito y límites del proyecto;
- autoridad de cada capa;
- reglas para asistentes y agentes;
- construcción y uso del mapa maestro;
- proveniencia y tratamiento de inferencias;
- objetos formales y evolución doctrinal;
- correcciones editoriales;
- uso para diplomados y software;
- límites de refactorización;
- pruebas de aceptación;
- criterio de congelación del esquema;
- definición de terminado.

Los demás README y archivos de `documentacion/` son explicativos o técnicos. **No añaden instrucciones operativas y no es necesario leerlos para comenzar.** Ante cualquier duda de precedencia, prevalece `INSTRUCCIONES.md`.

## Estructura

- `corpus/fuentes/` — fuentes canónicas.
- `corpus/libros/` — segmentación derivada y regenerable.
- `corpus/catalogo-generado.json` — catálogo estructural global vigente.
- `mapa/` — capa semántica y mapa maestro.
- `documentacion/` — notas y especificaciones técnicas no normativas.
- `scripts/` — infraestructura de ingestión, segmentación e integridad.
- `.github/workflows/` — automatización del pipeline documental.

## Flujo

**pregunta o tarea → mapa maestro → localizadores → texto real → respuesta o producto**

El mapa orienta la lectura; no sustituye al corpus.