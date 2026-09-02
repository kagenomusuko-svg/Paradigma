# Paradigma

Repositorio documental y semántico del corpus filosófico de Miguel Hilario Olvera Aguilar.

La finalidad del repositorio no es convertir los libros a JSON ni sustituir su lectura. Su finalidad es conservar las fuentes, generar representaciones estructurales verificables y construir un mapa maestro que permita localizar el contexto correcto para análisis, docencia, revisión editorial y desarrollo de herramientas de cálculo causal.

## Empieza aquí

La arquitectura se entiende en cuatro capas:

1. **Fuente canónica** — `corpus/fuentes/`
2. **Representación estructural derivada** — `corpus/libros/` y `corpus/catalogo-generado.json`
3. **Mapa semántico** — `mapa/`
4. **Uso** — lectura contextual, diplomados, revisión de obra y desarrollo tecnológico

Flujo general:

**fuente canónica → segmentación → catálogo estructural → mapa semántico → lectura del pasaje real → tarea**

El JSON semántico debe orientar la lectura; nunca reemplazarla.

## Qué contiene cada zona

### `corpus/fuentes/`

Contiene las fuentes Markdown íntegramente recibidas y sus sumas SHA-256. Son la autoridad documental del repositorio. No se corrigen por estilo, doctrina ni conveniencia analítica.

### `corpus/libros/`

Contiene copias segmentadas para consulta y análisis. Son archivos derivados y regenerables. Cada obra o volumen incluye un `estructura.json` que enlaza sus segmentos con la fuente canónica y sus rangos de líneas.

No debe recorrerse esta carpeta manualmente como índice general del proyecto: para eso existe el catálogo.

### `corpus/catalogo-generado.json`

Es el índice estructural global vigente. Se reconstruye a partir de todos los `estructura.json`. No contiene interpretación filosófica.

### `mapa/`

Es la capa semántica. Debe contener conceptos, formulaciones, objetos formales, relaciones entre obras, proveniencia y rutas de lectura. Su función es responder **qué debe leerse y por qué**, no responder por sí sola en lugar del corpus.

### `documentacion/`

Contiene las reglas operativas y las decisiones que no deben rediscutirse en cada sesión.

### `scripts/` y `.github/workflows/`

Mantienen la ingestión, segmentación, verificación de integridad y reconstrucción del catálogo. Son infraestructura estable. No se refactorizan por razones estéticas mientras cumplan sus invariantes.

## Reglas no negociables

- `corpus/fuentes/` es canónico.
- Toda interpretación debe poder regresar a una fuente y a un localizador verificable.
- Ningún resumen, embedding, índice o JSON adquiere autoridad sobre el texto fuente.
- El mapa semántico no se construye frase por frase: registra unidades conceptualmente relevantes.
- Una formulación posterior no borra automáticamente una anterior; se registra la relación entre ambas.
- Las posiciones de autores citados no se atribuyen al autor del corpus salvo apropiación explícita.
- Una modificación del esquema semántico debe estar motivada por una prueba de uso que el esquema vigente no pueda resolver; si ya existen datos, el cambio exige migración, no reinicio manual.

## Documentos de trabajo

- `documentacion/convenciones-del-corpus.md` — integridad y segmentación.
- `documentacion/arquitectura-operativa.md` — arquitectura congelada y límites de cada capa.
- `documentacion/protocolo-mapa-maestro.md` — instrucciones para construir y validar el mapa semántico.
- `mapa/README.md` — función y reglas de la capa semántica.

## Principio rector

**No volver a construir una base nueva cuando la base existente funciona.**

Los cambios de infraestructura deben justificarse porque resuelven un fallo observable del flujo final, no porque otra estructura parezca más elegante.