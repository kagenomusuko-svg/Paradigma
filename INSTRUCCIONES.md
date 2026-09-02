# Instrucciones operativas de Paradigma

> **FUENTE NORMATIVA ÚNICA DEL REPOSITORIO**
>
> Si una persona, asistente o agente va a trabajar con Paradigma, este es el único archivo de instrucciones que necesita leer antes de comenzar.
>
> Los README y los documentos de `documentacion/` pueden explicar estructura o detalles técnicos, pero **no añaden reglas operativas nuevas**. Si alguna redacción secundaria parece entrar en conflicto con este archivo, prevalece `INSTRUCCIONES.md`.

## 1. Propósito

Paradigma conserva el corpus filosófico de Miguel Hilario Olvera Aguilar y construye representaciones derivadas que permitan localizar el contexto correcto para:

- responder preguntas sobre el corpus;
- preparar diplomados y materiales docentes;
- revisar estilo, coherencia y evolución doctrinal;
- desarrollar motores de cálculo causal y otras herramientas tecnológicas;
- relacionar ontología, formalización matemática, métodos e instrumentos.

El objetivo del repositorio **no** es convertir los libros en JSON ni sustituir su lectura.

El objetivo del mapa maestro es conducir desde una pregunta o tarea hacia los pasajes correctos del corpus.

Paradigma y su mapa maestro **no están organizados alrededor de un único concepto, obra o familia doctrinal**. Deben representar el corpus completo en la pluralidad de problemas, conceptos, distinciones, argumentos, formalizaciones, métodos y aplicaciones que las propias obras desarrollen. Que un concepto se utilice como caso de prueba, ejemplo o puerta de entrada no le concede centralidad automática sobre los demás.

Flujo obligatorio:

**pregunta o tarea → mapa maestro → localizadores → lectura del texto real → respuesta o producto**

Nunca:

**pregunta → mapa maestro → respuesta como si el mapa fuera el libro**

---

## 2. Orden de autoridad y capas

### 2.1 Fuente canónica

Ruta: `corpus/fuentes/`

Es la máxima autoridad para establecer qué dice una obra.

- Los Markdown se conservan íntegros.
- `SHA256SUMS.txt` registra su integridad.
- No se modifican para normalizar estilo, facilitar búsquedas, adaptar el texto a una IA ni resolver discrepancias doctrinales.
- Una corrección directa solo procede cuando se verifica que el Markdown no reproduce fielmente la edición fuente.

### 2.2 Estructura documental derivada

Rutas:

- `corpus/libros/`
- `corpus/catalogo-generado.json`

Función: responder **dónde está** un contenido.

- Los segmentos son derivados y regenerables.
- Cada `estructura.json` enlaza segmentos con la fuente canónica y sus rangos.
- Ante discrepancia, prevalece `corpus/fuentes/`.
- `corpus/catalogo-generado.json` es el único catálogo estructural global vigente.
- El catálogo global se genera; no se mantiene manualmente.

### 2.3 Mapa semántico

Ruta: `mapa/`

Es una capa analítica derivada.

Función: responder **qué debe leerse para comprender correctamente una pregunta o realizar una tarea**.

No adquiere autoridad doctrinal sobre los libros.

### 2.4 Productos de uso

Diplomados, revisiones editoriales, motores de cálculo, interfaces, informes y demás productos aplican el corpus. No redefinen retrospectivamente ninguna capa anterior.

---

## 3. Cómo reanudar el proyecto

Para reanudar Paradigma en una conversación nueva o después de una pausa:

1. leer `INSTRUCCIONES.md`;
2. leer el **commit más reciente de trabajo en `main`**;
3. tomar de ese commit la fase, subsistema, estado, trabajo validado y siguiente paso;
4. continuar desde ese punto sin reconstruir decisiones históricas desde conversaciones anteriores.

No debe ser necesario leer una cadena de documentos, chats o commits antiguos para saber qué sigue.

Los commits automáticos se rigen por la regla especial de la sección 17 para que tampoco destruyan esta continuidad.

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
11. No pedir al autor extracción mecánica que pueda realizarse directamente desde el corpus.
12. La intervención humana se reserva principalmente para ambigüedades filosóficas reales, decisiones editoriales y validación de interpretaciones difíciles.
13. No inferir la jerarquía temática del corpus a partir de los conceptos elegidos para probar, explicar o implementar el mapa.

---

## 5. Reglas del mapa maestro

### 5.0 Alcance integral

El mapa es **corpus-céntrico, no ego-céntrico ni concepto-céntrico en sentido jerárquico**.

Debe poder navegar cualquier núcleo doctrinal o técnico relevante que aparezca en las obras: ontología, voluntad, pasión, posibilidad, colapso, mediación, identidad, alteridad, responsabilidad, metrología, diagnóstico, métodos, aplicaciones y cualquier otro dominio que el corpus desarrolle con función sustantiva.

Esta enumeración es ilustrativa, no una taxonomía cerrada. La centralidad de un concepto se establece por su función y dependencias dentro del corpus, no por haber sido seleccionado antes como ejemplo.

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

### 5.2 Evidencia y proveniencia

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

## 6. Construcción del mapa: fases obligatorias

### Fase 1 — Prueba de arquitectura

Modelar primero tres casos deliberadamente distintos:

1. **Fórmula del ego** — evolución conceptual y correspondencia entre obras.
2. **R\*** — objeto formal, definición matemática, dependencias y aplicaciones.
3. **Aego** — categoría ontológica/diagnóstica, distinciones y uso instrumental.

Estos tres casos son **pruebas de estrés del esquema**, no una selección de los conceptos más importantes del paradigma ni una delimitación del contenido futuro. Se eligen porque obligan al mismo modelo a resolver tres problemas estructurales distintos: evolución doctrinal, objeto matemático y categoría aplicada.

El mismo esquema debe resolver los tres.

No extender el esquema al corpus completo antes de superar esta fase.

### Fase 2 — Núcleo conceptual y ontológico del corpus

Integrar:

- `Caos`;
- los cinco volúmenes de `Afrodita Areia`;
- `El dilema de Aquiles`;
- `El juego de las máscaras`;
- `El telar de las Moiras`.

Objetivo: representar **el conjunto de conceptos, problemas, distinciones y relaciones nucleares que estas obras desarrollan y que otras partes del corpus presuponen**, no únicamente ego, mediación o sus derivados y no agotar cada frase.

La extracción debe dejar que la estructura conceptual emerja de las obras. No debe forzar todos los contenidos a organizarse como subtemas de un concepto elegido previamente.

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

Estas pruebas verifican capacidades de navegación y representación, no definen por sí solas el inventario temático completo del corpus.

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

### 11.1 Corrección de estilo

- Se trabaja sobre una copia o producto editorial, no directamente sobre la fuente canónica.
- Se lee contexto continuo.
- El mapa sirve para localizar usos conceptualmente relacionados que podrían requerir consistencia terminológica.

### 11.2 Corrección doctrinal

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
- reiniciar desde cero trabajo ya validado cuando pueda migrarse;
- reducir el mapa del corpus a un eje temático único porque ese eje haya sido usado como ejemplo o caso de prueba.

---

## 15. Definición de terminado para el mapa maestro v1

El mapa maestro v1 está terminado cuando:

- los conceptos nucleares necesarios para comprender las obras posteriores tienen localizadores verificables;
- la cobertura conceptual refleja los distintos núcleos sustantivos del corpus y no solo una familia temática preseleccionada;
- las formulaciones históricas y posteriores están conectadas sin borrarse entre sí;
- los objetos formales relevantes poseen dependencias y estatus epistémico;
- métodos e instrumentos enlazan al núcleo en vez de duplicarlo;
- las doce pruebas mínimas de aceptación funcionan;
- puede localizarse contexto para docencia, edición y programación;
- un cambio de fuente permite identificar qué elementos semánticos requieren revisión mediante proveniencia y hash;
- añadir nuevas obras pasa a ser mantenimiento, no reconstrucción arquitectónica.

---

## 16. Estado actual y siguiente hito

La infraestructura documental ya está construida y no es el trabajo principal pendiente.

Estado vigente al fijar estas instrucciones:

- **fase:** F0 cerrada — arquitectura e instrucciones;
- **siguiente fase:** F1 — prueba de arquitectura del mapa maestro;
- **casos de F1:** fórmula del ego + R\* + Aego;
- **sentido de los casos:** validar capacidades estructurales distintas del esquema, no definir la jerarquía temática del corpus;
- **restricción:** no realizar extracción sistemática del corpus antes de validar esos tres casos.

Este apartado describe el hito de partida, pero el **estado operativo más reciente siempre se obtiene del último commit de trabajo**, conforme a la sección 17.

---

## 17. Protocolo obligatorio de commits y continuidad

### 17.1 Principio

Cada commit de trabajo debe funcionar como **punto de reanudación autosuficiente**.

Una persona o agente que lea `INSTRUCCIONES.md` y el commit de trabajo más reciente debe poder saber:

- en qué fase está el proyecto;
- qué subsistema se modificó;
- si el trabajo quedó terminado, parcial o bloqueado;
- qué se hizo;
- qué quedó validado;
- cuál es el siguiente paso concreto.

No asumir que el lector revisará el commit anterior ni una conversación previa.

### 17.2 Formato del asunto

Todo commit de trabajo usa:

`[F<fase>][<SISTEMA>][<ESTADO>] descripción breve de lo completado`

Fases:

- `F0` — arquitectura, instrucciones e infraestructura de base;
- `F1` — prueba de arquitectura del mapa;
- `F2` — núcleo conceptual y ontológico del corpus;
- `F3` — formalización y metrología;
- `F4` — métodos, instrumentos y aplicaciones;
- `F5` — rutas de lectura y validación final;
- `MANT` — mantenimiento posterior a v1.

Subsistemas preferidos:

- `DOCS` — instrucciones y documentación normativa;
- `FUENTES` — fuentes canónicas e integridad;
- `ESTRUCTURA` — segmentación, estructuras y catálogo;
- `MAPA` — datos o esquema semántico;
- `VALIDACION` — pruebas de aceptación y consistencia;
- `EDITORIAL` — revisiones de estilo o doctrina;
- `DOCENCIA` — diplomados y materiales formativos;
- `SOFTWARE` — motores, calculadoras e interfaces;
- `INFRA` — scripts, workflows y automatización.

Estados:

- `HECHO` — el hito descrito quedó completado y validado;
- `PARCIAL` — avance utilizable, pero el hito continúa;
- `BLOQUEADO` — existe un impedimento concreto que debe quedar descrito;
- `DERIVADO` — commit automático o regenerado que no modifica por sí mismo el hito intelectual del proyecto.

### 17.3 Cuerpo obligatorio del commit de trabajo

Todo commit de trabajo debe incluir estas líneas:

```text
FASE: <fase y nombre>
SISTEMA: <subsistema>
ESTADO: <HECHO | PARCIAL | BLOQUEADO>
HECHO: <qué cambió o quedó construido>
VALIDADO: <qué prueba, criterio o verificación ya pasó>
SIGUIENTE: <una acción concreta que continúa el proyecto>
```

Cuando proceda puede añadirse:

```text
BLOQUEO: <impedimento verificable>
DECISION: <decisión arquitectónica/doctrinal que no debe rediscutirse sin una prueba fallida>
```

### 17.4 Granularidad

- Un commit debe representar un hito lógico reconocible, no una mezcla arbitraria de subsistemas.
- No crear commits vacíos únicamente para actualizar el estado.
- El mensaje describe el estado después del commit, no el plan previo.
- Si un trabajo queda parcial por cierre de sesión, debe poder retomarse desde `SIGUIENTE` sin reconstruir el razonamiento histórico.

### 17.5 Commits automáticos

Los workflows que generen commits deben usar `DERIVADO` y preservar el contexto del commit que los disparó.

Formato mínimo:

```text
[F<fase>][<SISTEMA>][DERIVADO] <regeneración automática>

ORIGEN: <mensaje del commit que disparó el workflow>
CAMBIO_DE_HITO: no
```

Un commit `DERIVADO` no sustituye el estado intelectual del commit de origen: debe permitir recuperarlo directamente desde su propio mensaje mediante `ORIGEN`.

Si un workflow no puede preservar ese contexto, debe modificarse antes de considerarlo compatible con esta estrategia de continuidad.

### 17.6 Pull requests y merges

Cuando se use un pull request:

- el título y el merge deben conservar la fase y el subsistema;
- el mensaje final en `main` debe seguir siendo suficiente para reanudar el trabajo;
- no usar un merge genérico que borre el significado de los commits de trabajo.

### 17.7 Regla de cierre de cada sesión de trabajo

Antes de considerar terminada una sesión que haya modificado el repositorio:

1. verificar que el último commit cumple este protocolo;
2. comprobar que `SIGUIENTE` apunta al próximo trabajo real y no a otra ronda abstracta de preparación;
3. si cambió una fase, reflejarlo explícitamente en el mensaje;
4. no crear otro documento de estado paralelo.

---

## 18. Regla final

**No volver a cimentar una base que ya funciona.**

Cuando algo falle, corregir el fallo observable con el cambio mínimo verificable. Cuando algo funcione, usarlo para avanzar al siguiente producto.