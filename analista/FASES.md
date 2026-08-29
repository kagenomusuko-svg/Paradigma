# Fases de construcción del analista documental

Este documento convierte los principios de `analista/README.md` en una hoja de ruta ejecutable.

Su función es impedir que el proyecto avance por entusiasmo técnico hacia funciones que todavía no corresponden. **Cada fase tiene entradas, trabajo permitido, productos y criterio de cierre. No se pasa a la siguiente fase mientras el criterio de cierre no se cumpla.**

---

# Fase 0 — Constitución y gobierno del sistema

## Objetivo

Fijar las reglas epistemológicas y operativas que ningún motor posterior podrá violar.

## Entradas

- corpus canónico existente;
- `analista/README.md`;
- `analista/config/clausura-descriptiva.yaml`.

## Trabajo

1. Definir la clausura descriptiva.
2. Definir qué constituye evidencia.
3. Definir qué significa `explícito`, `candidato`, `auditado` y `no determinado`.
4. Definir niveles de literalidad.
5. Definir estatus enunciativos mínimos.
6. Definir prohibiciones de síntesis, inferencia doctrinal, armonización y edición conceptual.
7. Definir política de IDs, versiones, hashes y trazabilidad.

## Productos

- README constitucional;
- YAML de restricciones;
- convenciones de nombres e IDs;
- catálogo de estados permitidos.

## Criterio de cierre

La especificación permite responder inequívocamente si una función propuesta pertenece o no al analista.

**Estado actual: sustancialmente cumplida.**

---

# Fase 1 — Esquemas de datos y contratos entre motores

## Objetivo

Definir antes de programar qué recibe y qué entrega cada herramienta.

## Trabajo

Crear esquemas versionados para, al menos:

- fuente;
- unidad textual;
- aparición conceptual;
- concepto;
- definición;
- afirmación;
- fórmula;
- relación explícita;
- distinción;
- negación;
- excepción;
- restricción de alcance;
- hallazgo de auditoría;
- reporte de cobertura;
- expediente maestro de obra.

Cada esquema deberá distinguir:

```text
texto_literal
normalizacion_formal
normalizacion_lexica
estatus_enunciativo
estado_extraccion
estado_verificacion
estado_auditoria
```

## Instrucciones

- Ningún esquema incluirá campos prescriptivos o editoriales.
- Ningún JSON intermedio podrá declararse doctrinalmente definitivo.
- Las referencias entre objetos se realizarán mediante IDs estables.
- Las versiones de esquema deberán conservarse en cada salida.

## Productos

`analista/esquema/`

## Criterio de cierre

Todos los motores previstos en la primera obra pueden intercambiar datos sin depender de estructuras ad hoc.

---

# Fase 2 — Motor de fuentes

## Objetivo

Construir la cadena de custodia de la obra antes de analizar su contenido.

## Responsabilidad única

Identificar y describir fuentes.

## Debe producir

- ID de fuente;
- título;
- ruta canónica;
- rutas derivadas;
- hash;
- versión;
- metadatos documentales;
- relación fuente íntegra ↔ segmentación.

## No puede

- interpretar contenido;
- corregir texto;
- decidir conceptos.

## Criterio de cierre

Toda unidad posterior puede remontarse inequívocamente a una fuente versionada.

---

# Fase 3 — Motor de unidades textuales

## Objetivo

Crear unidades estables sobre las cuales trabajarán todos los extractores posteriores.

## Responsabilidad única

Segmentar y localizar.

## Debe conservar

- ID estable;
- fuente;
- archivo;
- capítulo/sección;
- rango de líneas o posición;
- texto literal;
- orden textual;
- tipo estructural cuando sea formalmente reconocible.

## Debe medir

```text
unidades_totales
unidades_procesadas
unidades_omitidas
errores
```

## Criterio de cierre

La totalidad de la obra elegible está cubierta por unidades trazables y reproducibles.

---

# Fase 4 — Motores de extracción documental especializados

Esta fase se construye **motor por motor**. Un motor terminado no autoriza a fusionarlo con otro.

## 4A — Conceptos y apariciones

### Función

Localizar significantes y apariciones conceptuales candidatas.

### Debe distinguir

- forma literal;
- variante formal;
- variante léxica de búsqueda;
- concepto confirmado solo cuando exista evidencia suficiente.

### No puede

Fusionar conceptos por similitud semántica.

---

## 4B — Definiciones

### Función

Detectar estructuras definicionales candidatas y definiciones explícitas inequívocas.

### Regla

Si la evidencia solo permite `definición candidata`, la salida no puede ascender a `definición explícita`.

---

## 4C — Afirmaciones y tesis

### Función

Recuperar proposiciones potencialmente relevantes.

### Requisito crítico

Toda afirmación deberá conservar o proponer un `estatus_enunciativo`:

```text
afirmacion_autoral
negacion_autoral
cita
discurso_referido
objecion
hipotesis
ejemplo
pregunta
definicion
formulacion_condicional
caso_contrafactico
no_determinado
```

Una oración citada, objetada o presentada como hipótesis no puede convertirse automáticamente en tesis autoral.

---

## 4D — Fórmulas

### Función

Extraer fórmulas completas y su contexto suficiente.

### Debe evitar

- cortar fórmulas multilínea;
- perder índices, subíndices o símbolos;
- separar una fórmula de la unidad que explica sus variables.

---

## 4E — Relaciones explícitas

### Función

Registrar relaciones que el texto establezca de manera suficiente.

### No puede

- aplicar transitividad para fabricar relaciones;
- deducir equivalencias;
- convertir proximidad textual en relación doctrinal.

---

## 4F — Distinciones, negaciones, excepciones y restricciones

### Función

Recuperar elementos que limitan o modulan lo afirmado.

Esta información es obligatoria para impedir que una definición o tesis se vuelva más fuerte al ser extraída de su contexto.

## Criterio de cierre de Fase 4

Cada motor tiene pruebas propias, reporte de cobertura y salida intermedia independiente.

---

# Fase 5 — Normalización para recuperación

## Objetivo

Mejorar la recuperación sin crear doctrina.

## Niveles permitidos

```text
Nivel 0: texto literal
Nivel 1: normalización formal
Nivel 2: normalización léxica para búsqueda
Nivel 3: identidad conceptual solo con evidencia
```

## Herramientas posibles

- normalización Unicode;
- variantes tipográficas;
- flexión morfológica;
- lematización;
- diccionarios de sinónimos para búsqueda;
- similitud semántica solo para generar candidatos.

## Regla central

**Los niveles 1 y 2 amplían recuperación; no autorizan fusión conceptual.**

## Criterio de cierre

El sistema recupera variantes relevantes sin modificar los IDs conceptuales auditados.

---

# Fase 6 — Verificador mecánico de evidencia

## Objetivo

Sellar cada registro contra su fuente antes de auditarlo.

## Debe comprobar

- existencia de fuente;
- hash correcto;
- existencia de unidad;
- rango válido;
- coincidencia del texto citado;
- integridad de referencias;
- versión de extractor y esquema.

## No puede

- reclasificar filosofía;
- decidir qué quiso decir el autor;
- crear nuevas relaciones.

## Producto

JSON intermedio con estado de evidencia verificable.

## Criterio de cierre

Ningún registro llega al auditor sin evidencia verificable o sin una marca expresa de fallo.

---

# Fase 7 — Auditor intraobra

## Objetivo

Convertir registros verificados en un expediente auditado del libro.

## 7A — Auditoría estructural

Comprobar:

- IDs;
- referencias;
- duplicados;
- estados;
- fuerza probatoria;
- fórmulas completas;
- consistencia de esquemas.

## 7B — Auditoría descriptiva

Agrupar sin sintetizar:

- todas las predicaciones del mismo sujeto;
- definiciones múltiples;
- predicados diferentes;
- objetos diferentes;
- negaciones;
- excepciones;
- restricciones;
- usos singulares;
- variaciones terminológicas registradas.

## Hallazgos permitidos

```text
multiplicidad_predicativa
variacion_terminologica
variacion_de_predicado
variacion_de_objeto
definiciones_multiples
formulaciones_multiples
relacion_repetida
negacion_explicita
excepcion_explicita
restriccion_de_alcance
uso_singular
```

## Prohibido

```text
resolver
armonizar
sintetizar
corregir
inferir evolución
inferir contradicción
```

salvo que el propio texto establezca explícitamente la relación correspondiente.

## Criterio de cierre

El auditor puede mostrar todo lo que una obra predica de un concepto sin producir una definición sintética nueva.

---

# Fase 8 — Patrón de oro y calibración

## Objetivo

Medir por separado precisión y cobertura.

## Trabajo

Seleccionar una muestra representativa de unidades y construir manualmente un patrón de oro que indique qué debería recuperar cada motor.

## Métricas mínimas

```text
precision
cobertura
falsos_positivos
falsos_negativos
unidades_procesadas
```

## Regla

Una salida perfectamente trazable puede seguir siendo incompleta. La trazabilidad no sustituye la medición de cobertura.

## Criterio de cierre

Cada motor alcanza el umbral que se defina posteriormente para la producción de maestros.

---

# Fase 9 — Ensamblador y JSON maestro de una obra piloto

## Objetivo

Producir el primer expediente maestro completo.

## Obra piloto

**Afrodita Areia: Sobre la pasión**.

## El maestro debe contener

- metadatos de la obra;
- fuentes;
- unidades;
- conceptos y apariciones;
- definiciones;
- afirmaciones y estatus enunciativos;
- fórmulas;
- relaciones explícitas;
- distinciones;
- negaciones;
- excepciones;
- restricciones;
- hallazgos intraobra;
- cobertura de cada motor;
- métricas de calibración;
- historial de versiones;
- hashes y trazabilidad.

## Criterio de cierre

Una consulta sobre cualquier registro del maestro puede remontarse hasta el texto fuente y puede saberse qué motor lo produjo y qué auditoría superó.

---

# Fase 10 — Repetición controlada para todas las obras

## Objetivo

Producir un maestro auditado independiente por cada obra prevista.

## Regla esencial

**Durante esta fase no se realiza comparación doctrinal interobra.**

Cada libro habla primero por sí mismo.

## Trabajo por obra

```text
fuentes
→ unidades
→ extractores
→ normalización de recuperación
→ verificación
→ auditoría intraobra
→ maestro
```

## Criterio de cierre

Todas las obras previstas poseen JSON maestro compatible con la misma familia de esquemas y reglas.

---

# Fase 11 — Motores de comparación del corpus

## Objetivo

Trabajar exclusivamente sobre los JSON maestros de las obras.

## Motores especializados previstos

- conceptos del corpus;
- definiciones del corpus;
- afirmaciones del corpus;
- fórmulas del corpus;
- relaciones explícitas del corpus;
- negaciones y excepciones;
- variantes terminológicas;
- distribución por obra;
- orden y recurrencia.

## Ejemplo de salida

```text
CONCEPTO: primera mediación

Obra A
- predicación X → referencia
- predicación Y → referencia

Obra B
- predicación Z → referencia
```

## Prohibido

Decidir automáticamente que X, Y y Z son equivalentes, complementarios o contradictorios.

## Criterio de cierre

El sistema puede reunir exhaustivamente los registros relacionados sin añadir relaciones no documentadas.

---

# Fase 12 — Auditor del corpus

## Objetivo

Auditar los productos comparativos exactamente como el auditor intraobra, pero a escala interobra.

## Debe reportar

- multiplicidades por concepto;
- definiciones por obra;
- predicaciones por obra;
- variaciones terminológicas;
- negaciones;
- excepciones;
- relaciones explícitas;
- ausencia de resolución cuando corresponda.

## No debe

- reconciliar libros;
- declarar evolución doctrinal por mera secuencia;
- resolver aparentes contradicciones;
- escoger una definición como verdadera o definitiva.

## Criterio de cierre

Puede producir un expediente transversal de cualquier concepto sin sobrepasar los maestros de origen.

---

# Fase 13 — JSON maestro del corpus

## Objetivo

Consolidar todos los expedientes auditados en una estructura consultable.

## Producto esperado

Para cada concepto deberá ser posible obtener:

```text
obras donde aparece
formas literales
variantes de recuperación
definiciones explícitas
predicaciones
relaciones explícitas
fórmulas
negaciones
excepciones
restricciones
hallazgos de auditoría
referencias completas
```

## Criterio de cierre

Cada afirmación del maestro del corpus puede seguir una cadena completa:

```text
maestro_corpus
→ maestro_obra
→ registro_auditado
→ unidad
→ fuente
```

---

# Fase 14 — Motor de búsqueda y consulta literal

## Objetivo

Construir la interfaz que permita consultar el maestro del corpus.

## Consultas esperadas

- ¿Qué definiciones explícitas existen de X?
- ¿Qué se predica de X?
- ¿Qué se niega de X?
- ¿Dónde aparece X?
- ¿Qué fórmulas contienen X?
- ¿Existe evidencia explícita de que X = Y?
- ¿Qué variaciones terminológicas están documentadas?
- ¿Qué excepciones limitan una tesis?

## Respuestas negativas

Preferir:

> **No se encontró evidencia auditada en el expediente disponible.**

Y cuando la pregunta exija una relación que el corpus no establece:

> **NO DETERMINADO POR EL CORPUS.**

## Criterio de cierre

El buscador responde mediante registros auditados y referencias, no generando doctrina nueva.

---

# Fase 15 — Interfaz para sistemas de IA

## Objetivo

Permitir que una IA utilice el expediente sin tener que reconstruir el corpus desde cero.

## La IA recibirá

- registros pertinentes;
- texto literal;
- IDs;
- estatus;
- hallazgos;
- referencias;
- restricciones de respuesta.

## La IA no recibirá autoridad para

- completar lagunas;
- reconciliar formulaciones;
- convertir semejanzas en equivalencias;
- presentar inferencias como corpus.

## Criterio de cierre

Una respuesta generada puede mostrar exactamente qué registros utilizó y puede abstenerse cuando no existe evidencia suficiente.

---

# Fase futura separada — Auditoría y corrección editorial

Esta fase **no pertenece al analista documental actual**.

Podrá existir posteriormente un corrector formal destinado a:

- ortografía;
- puntuación;
- tipografía;
- Unicode;
- normalización visual de fórmulas;
- formato editorial.

Tendrá prohibido bajo cualquier circunstancia modificar contenido conceptual.

Los cambios conceptuales pertenecerán exclusivamente a trabajo autoral en ramas o ediciones creadas expresamente para ello.

---

# Regla global de avance

Antes de cerrar cualquier fase deben responderse cuatro preguntas:

1. **¿La salida es reproducible?**
2. **¿Cada registro es trazable?**
3. **¿La herramienta permaneció descriptiva?**
4. **¿La salida afirma únicamente lo que su evidencia permite?**

Si alguna respuesta es no, la fase no está cerrada.

---

# Secuencia completa

```text
0. Constitución
1. Esquemas
2. Fuentes
3. Unidades
4. Extractores especializados
5. Normalización para recuperación
6. Verificación de evidencia
7. Auditoría intraobra
8. Patrón de oro y calibración
9. Maestro de obra piloto
10. Maestros de todas las obras
11. Comparación del corpus
12. Auditoría del corpus
13. Maestro del corpus
14. Búsqueda y consulta literal
15. Interfaz para IA
```

La prioridad no es terminar rápido. La prioridad es que **cada capa reduzca la libertad interpretativa de la siguiente sin perder la evidencia original**.
