# Analista documental del corpus Paradigma

## 1. Propósito

Este directorio contiene la especificación conceptual, metodológica y técnica del sistema de extracción y auditoría documental del corpus **Paradigma**.

El objetivo final no es construir una inteligencia artificial que «interprete» los libros, ni un asistente que produzca explicaciones plausibles. El objetivo es producir un **reporte auditado, trazable y reproducible de los conceptos y afirmaciones que efectivamente contiene el corpus**.

El sistema debe poder responder, para cualquier registro que presente:

- qué afirma;
- dónde lo afirma;
- en qué unidad textual aparece;
- qué concepto o conceptos intervienen;
- cómo fue clasificado;
- qué herramienta lo extrajo;
- qué auditoría superó;
- y cuál es el texto fuente que permite verificarlo.

Si una afirmación no puede retroceder hasta evidencia textual suficiente, no pertenece al análisis doctrinal literal.

---

## 2. Principio rector

> **El corpus es la autoridad. El programa no completa, armoniza, corrige ni interpreta lo que el corpus no afirma.**

Reglas derivadas:

1. No hay definición explícita → no se inventa definición.
2. No hay tesis → no se fabrica tesis.
3. No hay relación textual suficiente → no se establece relación doctrinal.
4. No hay contradicción demostrable → no se busca una a fuerza.
5. No hay continuidad conceptual establecida → no se presupone.
6. No sabemos si dos expresiones son equivalentes → permanecen separadas.
7. Si el autor no resolvió algo en los textos → queda sin resolver.
8. Una inferencia posible no se convierte en doctrina literal.
9. Una semejanza semántica no constituye identidad conceptual.
10. La explicación posterior del autor puede señalar dónde buscar, pero no sustituye la evidencia del corpus.

El sistema está diseñado para preferir **«NO DETERMINADO POR EL CORPUS»** antes que una respuesta plausible pero no textual.

### 2.1. Clausura descriptiva

El analista permanece en la descripción del estado documental del corpus. Puede registrar que el corpus contiene lenguaje normativo, modal o prescriptivo sin convertirse por ello en prescriptivo.

La presencia de un significante como `debe` no determina por sí sola su función semántica. El contexto puede mostrar obligación normativa, condición funcional, necesidad definida por un modelo, expectativa, consecuencia lógica u otra función. Si la función no está suficientemente determinada, se conserva como **no determinada**.

El analista nunca produce por sí mismo una prescripción sobre cómo debería formularse, corregirse o armonizarse el corpus.

---

## 3. Resultado esperado

El producto final será un **expediente auditado del corpus**, construido en dos escalas.

### 3.1. Expediente maestro de cada obra

Cada libro tendrá un JSON maestro auditado que conserve, al menos:

- fuente y metadatos;
- unidades textuales;
- conceptos y apariciones;
- definiciones explícitas;
- afirmaciones o tesis explícitas;
- fórmulas;
- relaciones explícitas;
- distinciones;
- negaciones;
- excepciones;
- restricciones de alcance;
- predicaciones de cada sujeto o concepto;
- estatus enunciativo de las afirmaciones;
- hallazgos de auditoría intraobra;
- trazabilidad de cada registro hasta la fuente;
- cobertura de cada motor sobre las unidades de la obra;
- versión de los extractores y esquemas que produjeron el expediente.

El JSON maestro **no es una síntesis interpretativa del libro**. Es su expediente documental auditado.

### 3.2. Expediente maestro del corpus

Solo después de terminar y auditar todas las obras se realizará una segunda etapa que compare los JSON maestros.

El análisis del corpus podrá mostrar, por ejemplo:

- todas las definiciones de `primera mediación` por obra;
- todas sus predicaciones;
- todas sus fórmulas;
- variaciones terminológicas;
- formulaciones repetidas;
- formulaciones diferentes;
- negaciones y excepciones;
- referencias exactas de cada caso.

El auditor del corpus reportará los datos y sus multiplicidades. **No resolverá por sí mismo si dos formulaciones son compatibles, equivalentes, evolutivas o contradictorias.**

---

## 4. Arquitectura general

El sistema se construirá como una cadena de herramientas pequeñas y especializadas. Ningún programa debe intentar hacerlo todo.

```text
CORPUS CANÓNICO
      │
      ▼
EXTRACTORES ESPECIALIZADOS
      │
      ├── fuentes
      ├── unidades
      ├── conceptos
      ├── definiciones
      ├── afirmaciones
      ├── fórmulas
      ├── relaciones explícitas
      ├── distinciones
      ├── negaciones
      ├── excepciones
      └── otros módulos que se justifiquen
      │
      ▼
JSON INTERMEDIOS
      │
      ▼
VERIFICACIÓN DE EVIDENCIA
      │
      ▼
ENSAMBLADO DEL LIBRO
      │
      ▼
AUDITOR INTRAOBRA
      │
      ▼
JSON MAESTRO DEL LIBRO
```

Cuando existan todos los maestros:

```text
MAESTROS DE LAS OBRAS
      │
      ▼
MOTORES DE COMPARACIÓN DEL CORPUS
      │
      ▼
JSON INTERMEDIO DEL CORPUS
      │
      ▼
AUDITOR DEL CORPUS
      │
      ▼
JSON MAESTRO DEL CORPUS
```

---

## 5. Especialización de los extractores

Cada extractor tendrá **una sola responsabilidad principal**.

Ejemplos:

- el extractor de fuentes solo identifica y describe fuentes;
- el extractor de unidades solo segmenta y referencia unidades textuales;
- el extractor de conceptos solo identifica apariciones conceptuales bajo reglas controladas;
- el extractor de definiciones solo busca estructuras definicionales;
- el extractor de afirmaciones solo produce afirmaciones candidatas;
- el extractor de fórmulas solo conserva y estructura fórmulas y su contexto.

Si un extractor falla, debe poder sustituirse o mejorarse sin modificar los demás.

Los extractores producen **candidatos o registros documentales**, no doctrina consolidada.

---

## 6. JSON intermedio

Todo resultado automático previo a auditoría es un **JSON intermedio**.

Un JSON intermedio puede contener:

- candidatos;
- coincidencias;
- texto literal;
- referencias;
- motivos de detección;
- confianza de extracción;
- normalizaciones tipográficas permitidas;
- estatus enunciativo candidato;
- cobertura del motor que lo produjo.

No tiene autoridad doctrinal.

La confianza numérica, cuando exista, expresa confianza en la **detección o clasificación automática**, nunca probabilidad de que una tesis sea verdadera.

---

## 7. Verificación de evidencia

Antes de que un registro pueda llegar al auditor, una herramienta de verificación deberá comprobar de manera mecánica:

- que la fuente existe;
- que la unidad existe;
- que las líneas o rango declarados existen;
- que el texto literal coincide con la fuente;
- que el hash o identificador de la fuente corresponde a la versión analizada;
- que las referencias internas no están rotas.

El verificador no interpreta filosofía. Solo garantiza cadena de custodia documental.

---

## 8. Auditor intraobra

El auditor de cada libro es un **auditor**, no un editor y no un intérprete.

No lee el libro para reconstruirlo nuevamente: trabaja sobre registros previamente extraídos y cuya evidencia ya fue verificada.

Sus funciones incluyen dos niveles.

### 8.1. Auditoría estructural y epistemológica

Debe comprobar, entre otras cosas:

- que una definición explícita tenga evidencia textual;
- que las unidades y conceptos referenciados existan;
- que una afirmación explícita conserve su texto fuente;
- que una fórmula preserve su bloque completo;
- que no haya IDs rotos o duplicados indebidos;
- que las relaciones apunten a registros existentes;
- que un candidato no haya ascendido de categoría sin la evidencia exigida;
- que las afirmaciones conserven su estatus enunciativo o permanezcan como no determinadas.

### 8.2. Auditoría descriptiva intraobra

Debe agrupar y reportar **qué se predica del mismo sujeto o concepto dentro del libro**.

Ejemplo:

```text
A-001: φ₁ orienta la voluntad.
A-028: φ₁ produce el colapso.
A-071: φ₁ condiciona el acto.
```

El auditor debe registrar una **multiplicidad predicativa** y conservar las tres afirmaciones con sus referencias.

No debe sintetizarlas como una nueva definición.

No debe resolver si son equivalentes, complementarias, jerárquicas o incompatibles.

El mismo principio aplica a:

- definiciones múltiples;
- variaciones de predicado;
- variaciones de objeto;
- formulaciones múltiples;
- negaciones;
- excepciones;
- restricciones de alcance;
- usos singulares;
- relaciones repetidas.

Los resultados se registrarán como **hallazgos de auditoría**, no necesariamente como problemas.

Categorías descriptivas posibles:

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

El auditor **no usa por defecto** categorías interpretativas como:

```text
contradiccion
error
incoherencia
confusion
evolucion_conceptual
```

Estas requieren análisis posterior o declaración textual explícita.

---

## 9. Normalización lingüística y niveles de literalidad

La normalización sirve para **recuperar evidencia**, no para fabricar identidad doctrinal.

Se distinguen cuatro niveles:

### 9.1. Texto literal

La secuencia efectivamente conservada en la fuente. Es la base de toda trazabilidad.

### 9.2. Normalización formal

Ejemplo:

```text
φ1
φ₁
```

Puede normalizarse automáticamente cuando la identidad del signo sea inequívoca.

### 9.3. Normalización léxica para recuperación

Ejemplo:

```text
bosque
floresta
```

Puede utilizarse para ampliar búsquedas o generar candidatos de revisión.

No autoriza a fusionar conceptos.

### 9.4. Identidad conceptual

Solo se registra cuando existe evidencia textual suficiente de que dos términos designan el mismo concepto en el contexto correspondiente.

Compartir un predicado no produce identidad de sujeto:

```text
bosque verde
cielo verde
```

no son equivalentes por compartir `verde`.

La regla es: **normalizar significantes para encontrar evidencia; nunca convertir semejanza lingüística en doctrina.**

---

## 10. Análisis doctrinal literal

El análisis doctrinal literal es una etapa posterior y especialmente restringida.

Una proposición pertenece a esta capa **si y solo si existe evidencia textual suficiente de que el corpus la afirma**.

Puede incluir:

- definiciones explícitas;
- tesis explícitas;
- relaciones explícitas;
- equivalencias explícitas;
- distinciones explícitas;
- excepciones explícitas;
- argumentos efectivamente formulados por los textos.

No incluye automáticamente:

- consecuencias lógicas posibles;
- inferencias reconstruidas;
- armonizaciones;
- equivalencias por semejanza;
- soluciones a tensiones;
- interpretaciones plausibles.

Si en el futuro se desea una capa de reconstrucción analítica, deberá mantenerse separada y cada inferencia conservará sus premisas, regla aplicada y ausencia o presencia de texto literal equivalente.

---

## 11. Separación respecto de la edición

El analista **no modifica el corpus**.

Los problemas editoriales descubiertos incidentalmente durante el análisis podrán registrarse en el área correspondiente de edición, pero su corrección pertenece a otro proceso.

Un futuro corrector editorial automático tendrá expresamente prohibido modificar contenido conceptual bajo cualquier circunstancia. Podrá corregir únicamente aspectos formales previamente autorizados, como ortografía, puntuación, tipografía o normalización formal de fórmulas.

Los cambios doctrinales o conceptuales serán decisiones autorales realizadas fuera del analista y en ramas o ediciones destinadas expresamente a ello.

La auditoría ortográfica y tipográfica general del corpus **no forma parte de la fase actual**.

---

## 12. Orden de trabajo obligatorio

El proyecto seguirá este orden:

1. definir esquemas y reglas;
2. construir extractores especializados;
3. analizar una obra de forma intraobra;
4. verificar evidencia;
5. auditar la obra;
6. producir su JSON maestro;
7. repetir exactamente el proceso para todas las obras;
8. no comparar doctrinalmente el corpus hasta contar con los maestros de todas las obras previstas;
9. construir entonces los motores de comparación interobra;
10. producir y auditar el JSON maestro del corpus;
11. solo después construir consultas o análisis doctrinales sobre ese maestro.

No se adelantará una fase para obtener respuestas más rápidas.

La planificación detallada y los criterios de cierre de cada fase se mantienen en `analista/FASES.md`.

---

## 13. Trazabilidad y reproducibilidad

Todo registro maestro debe conservar como mínimo:

- ID estable;
- fuente;
- unidad textual;
- texto literal pertinente;
- rango o localización;
- extractor que lo produjo;
- versión del extractor;
- versión del esquema;
- hash o versión de la fuente;
- estado de verificación;
- estado de auditoría;
- historial de reclasificaciones cuando proceda.

Una modificación posterior de un extractor debe permitir regenerar su salida y comparar qué cambió.

---

## 14. Criterio de éxito

El proyecto no se considerará terminado porque el programa «entienda» los libros ni porque produzca explicaciones convincentes.

Se considerará exitoso cuando pueda entregar, para cada concepto del corpus, un reporte como este:

```text
CONCEPTO: X

Obra A
├── definición explícita → referencia
├── predicación 1 → referencia
├── predicación 2 → referencia
└── excepción → referencia

Obra B
├── definición explícita → referencia
└── formulación diferente → referencia

Obra C
└── uso singular → referencia

Hallazgos auditados:
- n definiciones explícitas
- n predicaciones
- n relaciones explícitas
- n excepciones
- n variaciones registradas

Resolución doctrinal adicional:
NO REALIZADA salvo evidencia textual suficiente.
```

El resultado puede parecer deliberadamente aburrido. Esa es una virtud: debe ser legible por humanos, recorrible por programas y especialmente útil para sistemas de IA que necesiten consultar el paradigma sin inventarlo.

---

## 15. Pregunta de control

Antes de añadir cualquier función al analista, debe responderse:

> **¿Esta función mejora la capacidad de recuperar, verificar, auditar o relacionar evidencia textual sin introducir contenido que el corpus no contiene?**

Si la respuesta es no, la función pertenece a otro proyecto o a otra capa.

---

## 16. Fórmula del proyecto

```text
recuperar
→ registrar
→ verificar
→ auditar
→ conservar multiplicidades
→ producir maestro de obra
→ repetir para todo el corpus
→ comparar maestros
→ auditar corpus
→ consultar literalmente
```

Nunca:

```text
leer
→ suponer qué quiso decir
→ armonizar
→ presentar la reconstrucción como texto
```

**La función del sistema no es pensar por el corpus. Es hacer que el corpus pueda rendir cuentas de lo que dice.**

---

## 17. Salvaguardas adicionales de implementación

### 17.1. Estatus enunciativo

La mera presencia de una oración en un libro no significa que sea una tesis del autor. Una afirmación deberá conservar, cuando pueda determinarse por evidencia textual, su función enunciativa.

Categorías mínimas:

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

Ejemplo:

```text
«Algunos sostienen que X. Esta posición es insostenible.»
```

no autoriza a registrar `X` como tesis autoral positiva.

Cuando el estatus no pueda establecerse con suficiente evidencia, debe conservarse como `no_determinado`.

### 17.2. Ausencia de hallazgo y cobertura

`No encontrado` no significa automáticamente `no existe`.

Cada motor deberá registrar:

- número total de unidades elegibles;
- unidades efectivamente procesadas;
- unidades omitidas y motivo;
- errores de procesamiento;
- versión del motor.

Se distinguen:

```text
NO ENCONTRADO POR ESTE MOTOR
NO PRESENTE EN LOS REGISTROS AUDITADOS
NO DETERMINADO POR EL CORPUS
```

Una consulta negativa deberá preferir expresiones como:

> **No se encontró evidencia auditada en el expediente disponible.**

antes que afirmar sin más que el corpus carece de ella.

### 17.3. Agregación no equivale a síntesis

El auditor puede reunir bajo un mismo sujeto todas sus definiciones, predicaciones, negaciones, relaciones y excepciones.

No puede convertir esa agregación en una tesis nueva.

```text
A-001: X es A.
A-002: X produce B.
A-003: X no es C.
```

puede presentarse como expediente conjunto de `X`, pero no sintetizarse automáticamente como:

```text
X = A + productor de B - C
```

### 17.4. Precisión y cobertura son métricas distintas

El sistema medirá por separado:

**Precisión:** de lo extraído, cuánto fue extraído y clasificado correctamente.

**Cobertura:** de los elementos que debían ser recuperados, cuánto encontró el motor.

La trazabilidad perfecta no demuestra cobertura perfecta.

Para calibrar motores semánticos se mantendrá un **patrón de oro humano** sobre una muestra representativa del corpus. Las métricas de confianza automática se referirán a detección o clasificación, nunca a verdad doctrinal.

### 17.5. Regla de fuerza probatoria

Ninguna salida puede ser más fuerte que su evidencia.

Ejemplos:

```text
Evidencia: posible definición
→ salida máxima: definición candidata

Evidencia: equivalencia léxica para búsqueda
→ salida máxima: candidato de vinculación

Evidencia: tesis explícita verificada
→ salida máxima: tesis explícita auditada
```

El sistema nunca asciende de categoría únicamente porque una formulación sea plausible, frecuente o coherente con otras.
