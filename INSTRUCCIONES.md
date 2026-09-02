# Instrucciones operativas de Paradigma

> **FUENTE NORMATIVA ÚNICA DEL REPOSITORIO**
>
> Si una persona, asistente o agente va a trabajar con Paradigma, este es el único archivo de instrucciones que necesita leer antes de comenzar.
>
> Los README y los documentos de `documentacion/` pueden explicar estructura, antecedentes o detalles técnicos, pero **no añaden reglas operativas nuevas**. Si alguna redacción secundaria parece entrar en conflicto con este archivo, prevalece `INSTRUCCIONES.md`.

## 1. Propósito del repositorio

Paradigma conserva el corpus filosófico de Miguel Hilario Olvera Aguilar y construye representaciones derivadas que permiten localizar el contexto correcto para:

- responder preguntas sobre el corpus;
- preparar diplomados y materiales docentes;
- revisar estilo, coherencia y evolución doctrinal;
- desarrollar motores de cálculo causal y otras herramientas tecnológicas;
- relacionar ontología, formalización matemática, métodos e instrumentos.

El objetivo del repositorio **no** es convertir los libros en JSON ni sustituir su lectura.

El objetivo del mapa maestro es conducir desde una pregunta o tarea hacia los pasajes correctos del corpus.

Flujo obligatorio:

**pregunta o tarea → mapa maestro → localizadores → lectura del texto real → respuesta o producto**

Nunca:

**pregunta → mapa maestro → respuesta como si el mapa fuera el libro**

---

## 2. Orden de autoridad

### 2.1 Fuente canónica

Ruta: `corpus/fuentes/`

Es la máxima autoridad para establecer qué dice una obra.

- Los Markdown se conservan íntegros.
- `SHA256SUMS.txt` registra su integridad.
- No se modifican para normalizar estilo, facilitar búsquedas, adaptar el texto a una IA ni resolver una discrepancia doctrinal.
- Una corrección directa solo procede cuando se verifica que el Markdown no reproduce fielmente la edición fuente.

### 2.2 Estructura documental derivada

Rutas:

- `corpus/libros/`
- `corpus/catalogo-generado.json`

Sirven para localizar y leer unidades manejables.

- Los segmentos son derivados y regenerables.
- Cada `estructura.json` enlaza segmentos con la fuente canónica y sus rangos.
- Ante cualquier discrepancia, prevalece `corpus/fuentes/`.
- `corpus/catalogo-generado.json` es el único catálogo estructural global vigente.
- El catálogo global se genera; no se edita manualmente.

### 2.3 Mapa semántico

Ruta: `mapa/`

Es una capa analítica derivada.

Su función es responder:

**¿qué debe leerse para comprender correctamente esta pregunta o realizar esta tarea?**

No adquiere autoridad doctrinal sobre los libros.

### 2.4 Productos de uso

Diplomados, revisiones editoriales, motores de cálculo, interfaces, informes y demás productos aplican el corpus. No redefinen retrospectivamente ninguna de las capas anteriores.

---

## 3. Modelo mental del repositorio

No usar el árbol completo de `corpus/libros/` como menú humano.

Para orientarse:

1. leer `INSTRUCCIONES.md`;
2. consultar `mapa/` si la tarea depende del contenido filosófico;
3. usar `corpus/catalogo-generado.json` para localizar obras y segmentos;
4. abrir el segmento o la fuente necesarios;
5. ejecutar la tarea desde el texto real.

`corpus/libros/` puede ser visualmente grande porque funciona como caché estructural regenerable. Su tamaño no implica que deba reorganizarse.

---

## 4. Reglas generales para cualquier asistente o agente

1. No responder desde memoria si la consulta depende del corpus y el repositorio está disponible.
2. Consultar el mapa maestro para determinar qué textos leer cuando exista una ruta semántica pertinente.
3. Leer después los segmentos o fuentes indicados.
4. Distinguir siempre entre lo que el texto afirma, lo que se infiere y lo que se propone editorialmente.
5. No rellenar huecos con filosofía general sin declararlo.
6. No tratar una formulación anterior como error solo porque exista una formulación posterior.
7. No atribuir al autor del corpus una tesis expuesta de Hume, Kant, Aristóteles, Arendt u otro interlocutor sin evidencia de apropiación, reformulación o adhesión.
8. Para correcciones editoriales o doctrinales, leer contexto continuo; no decidir desde un snippet aislado.
9. Para implementación tecnológica, cargar definiciones, fórmulas, dependencias, supuestos y estatus epistémico antes de programar.
10. Si el mapa no resuelve una consulta, registrar el fallo como caso de prueba antes de proponer un cambio de esquema.
11. No pedir al autor que haga extracción mecánica que puede realizarse directamente desde el corpus.
12. La intervención humana se reserva principalmente para ambigüedades filosóficas reales, decisiones editoriales y validación de interpretaciones difíciles.

---

## 5. Reglas del mapa maestro

### 5.1 Unidad semántica

La unidad ordinaria del mapa no es la frase, la página ni necesariamente el capítulo.

Se registra una **unidad semántica relevante**, por ejemplo:

- concepto;
- distinción;
- definición;
- formulación;
- fórmula;
- variable u objeto formal;
- axioma;
- teorema o lema;
- método;
- categoría diagnóstica;
- relación explícita entre conceptos;
- correspondencia terminológica entre obras;
- ruta de lectura.

Una mera mención no se registra salvo que sea necesaria para navegación, evolución doctrinal o uso técnico.

No se construye una tabla exhaustiva frase por frase del corpus.

### 5.2 Evidencia

Cada entrada semántica debe indicar su carácter:

- `explicit`: el corpus lo afirma, define, formula o relaciona identificablemente;
- `inferred`: relación analítica razonada pero no expresada de ese modo por el corpus;
- `editorial`: decisión organizativa del mapa sin pretensión doctrinal.

Estas categorías nunca se confunden.

Toda entrada doctrinal o formal relevante debe permitir regresar a su evidencia mediante, según disponibilidad:

- ID de obra;
- fuente canónica;
- hash de la fuente;
- segmento;
- rango de líneas;
- encabezado o sección;
- fragmento de evidencia cuando sea útil y permitido.

### 5.3 Evolución conceptual

Un concepto puede tener varias formulaciones.

No reducir automáticamente:

`concepto → una definición definitiva`

cuando el corpus muestre:

`génesis → formulación → refinamiento → formalización → aplicación`.

Las formulaciones antiguas se conservan y se relacionan con las posteriores mediante relaciones explícitas o inferidas debidamente marcadas.

### 5.4 Relaciones preferidas

Cuando correspondan, usar relaciones estables como:

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

No marcar una relación como explícita si el texto no la sostiene identificablemente.

### 5.5 Interlocutores

Cuando el corpus exponga a otros autores:

- registrar la posición del interlocutor por separado;
- registrar la interpretación o crítica del autor del corpus por separado;
- atribuir una tesis al sistema solo cuando exista evidencia de apropiación o reformulación.

### 5.6 Objetos formales

Fórmulas, variables, funciones, espacios, coeficientes, axiomas, teoremas, lemas, modelos y calibraciones son entidades de primera clase.

Cuando corresponda, registrar:

- símbolo;
- nombre;
- tipo matemático;
- dominio y codominio;
- definición;
- dependencias;
- supuestos;
- estatus epistémico;
- proveniencia;
- correspondencia con lenguaje ontológico.

No tratar:

- calibración empírica como teorema;
- modelo estadístico como axioma;
- analogía o metáfora como identidad formal;
- inferencia editorial como afirmación doctrinal.

---

## 6. Construcción del mapa: orden obligatorio

### Fase 1 — Prueba de arquitectura

Modelar primero tres casos deliberadamente distintos:

1. **Fórmula del ego** — evolución conceptual y correspondencia entre obras.
2. **R\*** — objeto formal, definición matemática, dependencias y aplicaciones.
3. **Aego** — categoría ontológica/diagnóstica, distinciones y uso instrumental.

El mismo esquema debe resolver los tres.

No extender el esquema al corpus completo antes de superar esta fase.

### Fase 2 — Núcleo ontológico

Integrar:

- `Caos`;
- los cinco volúmenes de `Afrodita Areia`;
- `El dilema de Aquiles`;
- `El juego de las máscaras`;
- `El telar de las Moiras`.

Objetivo: representar el vocabulario y las relaciones que las obras posteriores presuponen, no agotar cada frase.

### Fase 3 — Formalización y metrología

Integrar:

- `La transformación formal`;
- `Axiomatización del sistema de la doble mediación`;
- `Metrología Causal` I y II;
- `El cálculo de la responsabilidad`.

Objetivo: conectar con precisión lenguaje ontológico y lenguaje matemático.

### Fase 4 — Métodos, instrumentos y aplicaciones

Integrar:

- SDO;
- ECO;
- HISTOS;
- Método Prometeo;
- Arquitectura ontológica de sistemas artificiales;
- Taxonomía General de Aplicaciones.

Las aplicaciones enlazan al núcleo; no lo duplican.

### Fase 5 — Rutas de lectura y validación

Crear rutas orientadas a tareas reales y ejecutar la batería de aceptación.

---

## 7. Pruebas mínimas de aceptación

La versión 1 debe permitir localizar el contexto necesario, sin barrer indiscriminadamente el corpus, para responder correctamente al menos:

1. ¿Cuál es la fórmula del ego y cómo cambia entre obras?
2. ¿Cuál es la diferencia entre primera y segunda mediación?
3. ¿Cómo se relacionan mediación neutral, Fanes y Bis con la terminología de `Caos`?
4. ¿Qué es Aego y cómo se distingue de evasión o bloqueo de φ₂?
5. ¿Qué es R\*, cómo se calcula y qué presupuestos necesita?
6. ¿Qué mide S y cómo cambia su interpretación entre ontología y aplicación?
7. ¿Qué significan α y Δ y cuál es su estatus formal?
8. ¿Qué es IIC y dónde entra en el cálculo colectivo?
9. ¿Cómo se traduce una observación del SDO a entradas del modelo causal?
10. ¿Qué partes del corpus deben leerse para implementar un motor de cálculo sin mezclar metáfora, definición y calibración?
11. ¿Qué pasajes deben revisarse si se corrige una formulación doctrinal concreta?
12. ¿Qué capítulos son prerrequisitos para diseñar un módulo de diplomado sobre un concepto determinado?

La prueba se considera superada cuando el sistema puede devolver primero localizadores adecuados y, tras leerlos, producir una respuesta o producto consistente con el corpus.

---

## 8. Congelación del esquema

Después de que los tres casos de la Fase 1 funcionen, el esquema semántico v1 queda congelado.

Un cambio estructural posterior solo procede si existe un caso de uso concreto que el esquema vigente no pueda resolver correctamente.

Toda propuesta de cambio debe indicar:

1. qué consulta o tarea falla;
2. por qué falla por estructura y no por falta de datos;
3. cuál es la modificación mínima necesaria;
4. cómo se migran reproduciblemente los datos existentes;
5. qué prueba demuestra que el cambio resolvió el fallo sin romper los casos anteriores.

No se reinicia manualmente la extracción por un cambio de criterio.

No se rediseña el esquema porque otra estructura parezca más elegante.

---

## 9. Infraestructura estable y límites de refactorización

Los scripts y workflows existentes de ingestión, segmentación, integridad y catálogo se consideran infraestructura estable mientras cumplan sus invariantes.

La división histórica en varios segmentadores puede ser poco elegante, pero no se refactoriza por estética.

Solo se modifica esa infraestructura si ocurre al menos una de estas condiciones:

- una fuente nueva no puede registrarse sin duplicación peligrosa;
- un cambio de formato rompe la segmentación;
- aparece una inconsistencia comprobable entre derivados y fuentes;
- el mantenimiento actual impide una operación necesaria del mapa maestro.

Toda refactorización debe preservar reconstrucción exacta de las fuentes y tener una prueba concreta de necesidad.

---

## 10. Incorporación de nuevas obras o versiones

Cuando se incorpore una nueva fuente:

1. preservar el Markdown íntegro en `corpus/fuentes/`;
2. registrar o recalcular su hash;
3. generar la estructura derivada mediante el pipeline existente;
4. reconstruir el catálogo global;
5. identificar qué nodos y rutas semánticas podrían verse afectados;
6. actualizar únicamente esos elementos del mapa;
7. volver a ejecutar las pruebas pertinentes.

Una nueva obra no obliga a reconstruir el mapa completo.

Una nueva versión de una obra no autoriza a sobrescribir silenciosamente formulaciones anteriores del mapa sin verificar qué cambió.

---

## 11. Correcciones de estilo y doctrina

### Corrección de estilo

- Se trabaja sobre una copia o producto editorial, no directamente sobre la fuente canónica.
- Se lee contexto continuo.
- El mapa sirve para localizar usos conceptualmente relacionados que podrían requerir consistencia terminológica.

### Corrección doctrinal

- Se identifican todas las formulaciones relevantes y sus relaciones históricas.
- Se compara la formulación que se desea modificar con desarrollos posteriores.
- Se distingue entre error, evolución, refinamiento y traducción entre lenguajes.
- Ningún cambio se incorpora silenciosamente a la fuente canónica.

---

## 12. Uso para diplomados

Para preparar un módulo o diplomado:

1. identificar el concepto o problema central;
2. consultar su ruta de lectura y prerrequisitos;
3. abrir los pasajes reales;
4. construir la secuencia pedagógica desde dependencias conceptuales, no desde el orden accidental de archivos;
5. distinguir material nuclear, formalización, aplicaciones e interlocutores;
6. mantener trazabilidad hacia las obras utilizadas.

El mapa no sustituye el estudio de los capítulos utilizados en la clase.

---

## 13. Uso para motores de cálculo y software

Antes de implementar una fórmula o parámetro:

1. localizar su definición formal vigente;
2. cargar dependencias y supuestos;
3. verificar su estatus: axioma, teorema, modelo, calibración, heurística u otro;
4. identificar correspondencias con conceptos ontológicos cuando sean relevantes;
5. distinguir parámetros derivados de parámetros calibrados;
6. revisar los límites declarados por el corpus;
7. implementar pruebas que reproduzcan ejemplos o propiedades documentadas cuando existan.

Nunca programar una fórmula solo desde una paráfrasis del mapa.

---

## 14. Acciones prohibidas

No se debe:

- convertir el mapa en sustituto del corpus;
- crear un JSON frase por frase sin necesidad de recuperación demostrada;
- mantener manualmente datos que pueden derivarse de `estructura.json`;
- crear un segundo catálogo global competidor;
- modificar fuentes canónicas por comodidad;
- mezclar afirmaciones del autor con posiciones de interlocutores;
- borrar formulaciones históricas porque existe una posterior;
- tratar inferencias como explícitas;
- refactorizar infraestructura estable solo por limpieza estética;
- crear nuevas carpetas o herramientas cuya única finalidad sea preparar otra capa futura sin un caso de uso actual;
- exigir al autor extracción mecánica que el sistema puede realizar;
- reiniciar desde cero trabajo ya validado cuando pueda migrarse.

---

## 15. Definición de terminado para el mapa maestro v1

El mapa maestro v1 está terminado cuando:

- los conceptos nucleares necesarios para comprender las obras posteriores tienen localizadores verificables;
- las formulaciones históricas y posteriores están conectadas sin borrarse entre sí;
- los objetos formales relevantes poseen dependencias y estatus epistémico;
- métodos e instrumentos enlazan al núcleo en vez de duplicarlo;
- las doce pruebas mínimas de aceptación funcionan;
- puede localizarse contexto para docencia, edición y programación;
- un cambio de fuente permite identificar qué elementos semánticos requieren revisión mediante proveniencia y hash;
- añadir nuevas obras pasa a ser mantenimiento, no reconstrucción arquitectónica.

---

## 16. Estado actual del proyecto

La infraestructura documental ya está construida y no es el trabajo principal pendiente.

El siguiente hito es **Fase 1 del mapa maestro**:

**fórmula del ego + R\* + Aego**.

Hasta que esos tres casos no validen el esquema, no se realiza extracción sistemática de todo el corpus.

---

## 17. Regla final

**No volver a cimentar una base que ya funciona.**

Cuando algo falle, corregir el fallo observable con el cambio mínimo verificable. Cuando algo funcione, usarlo para avanzar al siguiente producto.