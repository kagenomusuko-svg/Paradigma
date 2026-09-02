# Mapa maestro

Esta carpeta contiene la capa semántica de Paradigma.

## Función

El mapa maestro debe orientar desde una pregunta hacia los pasajes correctos del corpus. No sustituye a `corpus/fuentes/` ni debe convertirse en una reescritura de los libros.

Ejemplo de comportamiento esperado:

**consulta:** «¿Cuál es la fórmula del ego?»

**mapa:** identifica la formulación de `Caos`, la reformulación de `La transformación formal` y la formalización correspondiente; entrega los localizadores y el orden de lectura.

**lectura:** el asistente abre esos pasajes y responde desde el texto real.

## Principios de diseño

- concept-centric, no sentence-centric;
- proveniencia obligatoria;
- múltiples formulaciones pueden coexistir;
- explícito, inferido y editorial se distinguen;
- fórmulas y objetos matemáticos son entidades de primera clase;
- las rutas de lectura dependen del propósito de la consulta;
- el archivo maestro será una representación derivada y regenerable;
- los datos fuente del mapa deben poder migrarse sin volver a extraer manualmente todo el corpus.

## Estado de construcción

La versión 1 del esquema no debe congelarse en abstracto. Primero se validará con tres casos representativos:

1. fórmula del ego;
2. R*;
3. Aego.

Después de superar las pruebas descritas en `documentacion/protocolo-mapa-maestro.md`, el esquema se congela y comienza la extracción sistemática del corpus.

## Regla de uso

**Mapa → localizador → texto real → respuesta o producto.**

Nunca:

**Mapa → respuesta como si el mapa fuera el libro.**