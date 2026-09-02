# Protocolo de construcción del mapa maestro

## 1. Objetivo

Construir un índice semántico verificable que permita localizar con precisión qué partes del corpus deben leerse para responder una pregunta, enseñar un tema, revisar una formulación o implementar una herramienta.

El mapa maestro **no responde en lugar de los libros**. Reduce el espacio de búsqueda y preserva la evolución conceptual del corpus.

## 2. Unidad de trabajo

La unidad ordinaria del mapa no es la frase ni la página. Es una **unidad semántica relevante**, por ejemplo:

- concepto;
- distinción;
- definición;
- formulación;
- fórmula;
- variable u objeto formal;
- axioma;
- teorema;
- método;
- categoría diagnóstica;
- relación explícita entre conceptos;
- correspondencia terminológica entre obras;
- ruta de lectura.

Una simple mención no se registra salvo que cumpla una función de navegación o de evolución doctrinal.

## 3. Regla fundamental de evidencia

Todo dato semántico debe distinguir entre:

- **explícito**: el texto lo afirma, define, formula o relaciona;
- **inferido**: la relación es una lectura analítica razonada pero no está declarada de ese modo por el texto;
- **editorial**: decisión de organización del mapa sin pretensión doctrinal.

Las tres categorías pueden existir, pero nunca se confunden.

Toda formulación explícita o inferida debe poseer localizador suficiente para volver a la fuente: obra, segmento, fuente canónica, hash y rango de líneas cuando esté disponible.

## 4. Instrucciones de extracción

### 4.1 Antes de extraer

1. Consultar el catálogo estructural vigente.
2. Identificar las obras y segmentos probablemente relevantes.
3. Priorizar señales escritas por el propio corpus: índices temáticos, glosarios, mapas del sistema, tablas de correspondencia, fórmulas, axiomas, teoremas, definiciones y encabezados.
4. Leer un bloque contextual continuo antes de registrar una formulación.

### 4.2 Al registrar conceptos

- Asignar un ID estable que no dependa de la redacción visible.
- Registrar aliases solo cuando sean usados por el corpus o necesarios para recuperación.
- Conservar varias formulaciones del mismo concepto cuando existan.
- No elegir una sola "definición verdadera" si la obra muestra desarrollo histórico o traducciones entre lenguajes.
- Distinguir génesis, definición, refinamiento, formalización, aplicación y delimitación negativa.

### 4.3 Al registrar relaciones

Relaciones preferidas:

- `requires`
- `produces`
- `condition_of`
- `distinguished_from`
- `refines`
- `formalizes`
- `translates`
- `presupposes`
- `applies`
- `criticizes`
- `case_of`
- `measures`
- `operationalizes`

Una relación no se registra como explícita si el texto no la sostiene de forma identificable.

### 4.4 Autores e interlocutores

Cuando una obra explica a Aristóteles, Hume, Kant, Arendt u otro interlocutor:

- la posición del interlocutor se registra como tal;
- la interpretación del autor del corpus se registra por separado;
- solo se atribuye una proposición al sistema cuando existe apropiación, reformulación o adhesión explícita.

### 4.5 Objetos formales

Fórmulas, variables, funciones, espacios, coeficientes, axiomas, teoremas, lemas, modelos y calibraciones se registran como objetos propios.

Cada objeto formal debe indicar, cuando corresponda:

- símbolo;
- nombre;
- tipo matemático;
- dominio/codominio;
- definición;
- dependencias;
- supuestos;
- estatus epistémico;
- localizadores de fuente;
- relación con su lenguaje ontológico.

No se trata una calibración empírica como teorema ni un modelo estadístico como axioma.

## 5. Orden de construcción

### Fase 1 — Prueba de arquitectura

Se modelan tres casos deliberadamente distintos:

1. **Fórmula del ego** — evolución conceptual y correspondencia entre obras.
2. **R\*** — objeto formal, definición matemática, dependencias y aplicaciones.
3. **Aego** — categoría ontológica/diagnóstica, distinciones y uso en instrumentos.

Objetivo: demostrar que el mismo esquema resuelve evolución doctrinal, formalización matemática y aplicación diagnóstica.

No se congela el esquema por elegancia abstracta. Se congela cuando estos tres casos y las pruebas de consulta funcionan.

### Fase 2 — Núcleo ontológico

Construir los conceptos y relaciones fundacionales de:

- `Caos`;
- los cinco volúmenes de `Afrodita Areia`;
- `El dilema de Aquiles`;
- `El juego de las máscaras`;
- `El telar de las Moiras`.

El objetivo no es agotar cada frase, sino representar el vocabulario que otras obras presuponen.

### Fase 3 — Formalización y metrología

Integrar:

- `La transformación formal`;
- `Axiomatización del sistema de la doble mediación`;
- `Metrología Causal` I y II;
- `El cálculo de la responsabilidad`.

Aquí deben quedar formalizadas las correspondencias entre lenguaje ontológico y matemático.

### Fase 4 — Métodos e instrumentos

Integrar:

- SDO;
- ECO;
- HISTOS;
- Método Prometeo;
- Arquitectura ontológica de sistemas artificiales;
- Taxonomía General de Aplicaciones.

La capa de aplicaciones debe enlazar al núcleo; no duplicarlo.

### Fase 5 — Rutas de lectura y validación

Crear rutas orientadas a tareas reales y ejecutar la batería de aceptación.

## 6. Batería mínima de aceptación

El mapa se considera útil solo si permite, sin barrido indiscriminado del corpus, localizar el contexto necesario para responder correctamente al menos estas consultas:

1. ¿Cuál es la fórmula del ego y cómo cambia su formulación entre obras?
2. ¿Cuál es la diferencia entre primera y segunda mediación?
3. ¿Cómo se relacionan mediación neutral, Fanes y Bis con la terminología de `Caos`?
4. ¿Qué es Aego y cómo se distingue de evasión o bloqueo de φ₂?
5. ¿Qué es R\*, cómo se calcula y qué presupuestos necesita?
6. ¿Qué mide S y cómo cambia su interpretación entre ontología y aplicación?
7. ¿Qué significan α y Δ y cuál es su estatus formal?
8. ¿Qué es IIC y dónde entra en el cálculo colectivo?
9. ¿Cómo se traduce una observación del SDO a entradas del modelo causal?
10. ¿Qué parte del corpus debe leerse para implementar un motor de cálculo sin mezclar metáfora, definición y calibración?
11. ¿Qué pasajes deben revisarse si se corrige una formulación doctrinal concreta?
12. ¿Qué capítulos son prerequisitos para diseñar un módulo de diplomado sobre un concepto determinado?

Cada prueba debe devolver primero localizadores y después permitir lectura del texto real.

## 7. Política de cambios del esquema

Una vez superada la Fase 1, la versión 1 del esquema queda congelada.

Un cambio posterior exige una prueba de aceptación fallida que no pueda resolverse añadiendo datos al modelo vigente.

Si el cambio es necesario:

1. se incrementa la versión del esquema;
2. se escribe una migración reproducible;
3. se conservan los IDs estables siempre que sea posible;
4. se ejecutan nuevamente todas las pruebas de aceptación;
5. no se vuelve a extraer manualmente el corpus desde cero.

## 8. Instrucciones para asistentes o agentes

Cuando se trabaje con Paradigma:

1. No responder desde memoria cuando la pregunta dependa del corpus y el repositorio esté disponible.
2. Consultar primero el mapa para decidir qué leer.
3. Leer después los segmentos o fuentes indicados.
4. Distinguir claramente lo textual, lo inferido y lo propuesto.
5. No completar silenciosamente huecos con filosofía general.
6. No tratar una formulación anterior como error solo porque exista una posterior.
7. No atribuir al autor una tesis de un interlocutor sin evidencia de apropiación.
8. Para tareas editoriales, revisar contexto continuo, no solo snippets.
9. Para tareas técnicas, cargar definiciones, dependencias, supuestos y estatus epistémico de los objetos formales involucrados.
10. Si una consulta no puede resolverse con el mapa, registrar el fallo como prueba antes de proponer ampliar el esquema.

## 9. Definición de terminado

El mapa maestro está terminado en su versión 1 cuando:

- todos los conceptos nucleares necesarios para comprender las obras posteriores poseen localizadores verificables;
- las formulaciones históricas y posteriores están conectadas sin borrarse entre sí;
- los objetos formales relevantes poseen dependencias y estatus epistémico;
- las obras de métodos y aplicaciones enlazan al núcleo en lugar de duplicarlo;
- las doce pruebas mínimas de aceptación funcionan;
- el mapa permite localizar textos para docencia, edición y programación;
- cambiar el corpus fuente no obliga a rehacer manualmente todo el mapa: los elementos afectados pueden identificarse por proveniencia y hash.

A partir de ese punto, añadir nuevas obras o conceptos es mantenimiento del sistema, no reconstrucción de su arquitectura.