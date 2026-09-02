# Revisión de calibración documental del analista

## 0. Estatus y relación con las fases existentes

Este documento regula una **revisión de calibración** del analista documental ya construido.

No sustituye `analista/README.md`, `analista/FASES.md` ni `analista/config/clausura-descriptiva.yaml`. Los complementa para el trabajo posterior al cierre técnico alcanzado en la generación `analisis-textual-v0.1`.

Las fases históricas F0–F15 permanecen como la arquitectura y el historial de construcción del sistema. La revisión usa una numeración separada, `RC-0` a `RC-8`, para evitar confundir calibración con reconstrucción.

Baseline de referencia:

```text
rama:   analisis-textual-v0.1
commit: 817b05a9a2eaa2643a5a49ec90f881b85a5d572e
```

La revisión se desarrolla en una rama separada. El baseline no se reescribe ni se presenta retrospectivamente como si nunca hubiera cumplido sus contratos de construcción.

---

# 1. Propósito

El analista existe y realiza la cadena documental prevista: extrae, registra, verifica, audita, consolida y consulta evidencia. La revisión no parte de la premisa de que esa arquitectura deba destruirse.

El propósito es **calibrar la precisión documental de sus motores a partir de resultados reales de obras completas**, identificar inferencias o reglas automáticas que produzcan pérdida, truncamiento, clasificación indebida o cobertura insuficiente, y corregir únicamente las causas raíz demostradas.

La pregunta rectora es:

> **¿El registro producido por el motor está suficientemente sustentado por la evidencia documental exacta de la que declara proceder?**

La revisión no pregunta qué quiso decir el autor ni cuál sería la mejor reconstrucción doctrinal.

---

# 2. Qué esperamos obtener

Al cerrar la revisión se espera contar con:

1. motores calibrados sobre varias obras completas y estructuralmente diferentes;
2. evidencia reproducible de los errores encontrados y de las correcciones aplicadas;
3. pruebas de regresión permanentes para cada familia de error confirmada;
4. trazabilidad completa entre resultado, unidad y fuente;
5. separación efectiva entre detección candidata y clasificación fuerte;
6. segmentación que no confunda renglones físicos de conversión con unidades lingüísticas;
7. tratamiento explícito de corrupción de conversión, fórmulas incompletas y glifos no resueltos;
8. identidad conceptual respaldada por evidencia y no por mera recurrencia léxica;
9. estatus enunciativos defendibles documentalmente;
10. cobertura funcional medida mediante controles documentales y auditoría de resultados reales;
11. un maestro del corpus regenerado solo después de demostrar generalización;
12. un motor de consulta que distinga contrato de respuesta, cobertura funcional y estados de ausencia;
13. una interfaz para IA que entregue paquetes de evidencia controlados sin producir doctrina nueva.

El objetivo no es maximizar el número de registros. El objetivo es que cada registro conserve la fuerza probatoria que realmente permite su evidencia.

---

# 3. Principios vinculantes de la revisión

## 3.1. Conservación del sistema existente

Se conservará todo componente que ya satisfaga su contrato.

No se sustituirá un motor, esquema, auditor, verificador o producto por preferencia técnica. Toda modificación deberá responder a una causa demostrada, como mínimo una de las siguientes:

- error documental reproducible;
- pérdida de cobertura demostrable;
- inferencia automática no autorizada;
- clasificación incorrecta demostrable;
- problema de trazabilidad;
- corrupción o pérdida introducida por conversión;
- deficiencia operativa que impida cumplir el propósito del sistema.

La corrección mínima suficiente tendrá preferencia sobre la reescritura.

## 3.2. La autoridad sigue siendo el corpus

El corpus continúa siendo la autoridad.

La revisión humana no crea evidencia doctrinal suplementaria y no sustituye la fuente.

Una explicación posterior del autor no podrá utilizarse para elevar la fuerza de un registro cuya evidencia textual no alcance por sí misma.

## 3.3. El motor trabaja antes que el auditor humano

No se construirá previamente una interpretación manual que le indique al motor qué debe encontrar.

El orden obligatorio será:

```text
obra
→ ejecución del motor
→ productos reales
→ auditoría documental de esos productos
→ diagnóstico
→ calibración
→ nueva ejecución
```

## 3.4. Función humana permitida

La intervención humana se limita a **lectura y auditoría documental**.

Puede comprobar, mediante la fuente:

- si el texto citado corresponde a la localización declarada;
- si un fragmento comienza antes o continúa después;
- si dos fragmentos fueron unidos indebidamente;
- si una unidad pertenece a una pregunta, cita, discurso referido, condicional u otra función textual reconocible;
- si una entrada pertenece formalmente a un glosario;
- si una fórmula fue cortada;
- si un artefacto procede de la conversión;
- si una estructura textual está completa;
- si el criterio de detección invocado por el motor está realmente presente en la fuente.

No puede utilizarse para decidir:

- cuál definición es doctrinalmente preferible;
- qué quiso decir realmente un pasaje ambiguo;
- qué conceptos deberían ser equivalentes;
- qué formulaciones deberían armonizarse;
- qué tesis debería haber contenido la obra;
- cómo debería corregirse conceptualmente el texto.

Cuando la evidencia documental no permita decidir, la revisión conserva `no_determinado`.

## 3.5. Patrón humano de calibración

Cuando `README.md`, `FASES.md` o la clausura exijan un patrón humano para calibración, en esta revisión se entiende como un **patrón de auditoría documental construido a partir de resultados reales del motor y verificado contra la fuente**, no como un patrón doctrinal preparado por el autor antes de ejecutar el sistema.

El humano evalúa la correspondencia entre salida y evidencia. No aporta la respuesta doctrinal que el motor debería aprender.

## 3.6. Revisión obra por obra

La calibración se realizará sobre obras completas, una por una.

No se fija de antemano que deban revisarse las veinte obras. El conjunto de calibración crecerá únicamente mientras nuevas obras sigan revelando familias nuevas de errores relevantes.

Se espera que dos a cuatro obras estructuralmente diferentes sean suficientes para revelar la mayor parte de los errores sistemáticos; esta cifra es una expectativa operativa, no un criterio de cierre.

## 3.7. Cada corrección debe generalizar

El objetivo no es perfeccionar individualmente las obras seleccionadas.

Una corrección es preferible cuando:

- resuelve varios casos de la misma familia;
- funciona en más de una obra;
- no requiere una excepción por título;
- no codifica frases doctrinales concretas para aprobar la muestra;
- conserva los aciertos anteriores;
- no degrada cobertura o trazabilidad.

Las reglas específicas de una obra solo son admisibles cuando responden a una estructura documental exclusiva y demostrable de esa obra.

---

# 4. Expediente obligatorio de auditoría por registro

Todo resultado sometido a revisión deberá permitir mostrar, como mínimo:

```text
registro_id
tipo_registro
obra_id
fuente
archivo
unidad_id
localizacion
linea_inicio
linea_fin
texto_literal
criterio_deteccion
motor
version_motor
estado_extraccion
estado_verificacion
estado_auditoria
estatus_enunciativo, cuando corresponda
```

Para facilitar la lectura podrá añadirse `contexto_anterior` y `contexto_posterior`. Ese contexto es material de auditoría y no reemplaza el `texto_literal` ni altera la evidencia almacenada.

La finalidad es que cualquier observación pueda responder inmediatamente:

> ¿De dónde salió este registro y qué regla lo produjo?

---

# 5. Categorías de auditoría documental

La revisión utilizará categorías controladas. Como mínimo:

```text
correcto

truncado_inicio
truncado_final
fragmentacion_indebida
fusion_indebida

tipo_registro_incorrecto
estatus_enunciativo_incorrecto
concepto_no_establecido_por_la_evidencia

evidencia_insuficiente
referencia_incorrecta
trazabilidad_incorrecta

corrupcion_conversion
formula_incompleta

duplicado_indebido
otro_error_documental
no_determinado
```

Estas categorías describen la relación entre salida y evidencia; no corrigen doctrina.

Cada observación deberá conservar:

- registro revisado;
- categoría;
- fuente y localización usadas para comprobarlo;
- comentario documental mínimo cuando sea necesario;
- estado de resolución;
- causa raíz, cuando haya sido determinada.

---

# 6. Regla de causa raíz y regresión

No se corregirán manualmente los productos finales como solución permanente.

Cada error confirmado deberá investigarse hasta localizar, cuando sea posible, el mecanismo que lo produce.

Ejemplo:

```text
varias definiciones truncadas
→ mismo patrón
→ salto físico de línea tratado como frontera de oración
→ una causa raíz
→ una corrección del segmentador
→ prueba de regresión
```

Toda corrección del motor debe producir al menos una prueba que impida la reaparición del error confirmado.

Cuando una corrección introducida por una obra modifique el motor, deberán volver a ejecutarse las obras de calibración anteriores.

---

# 7. Inferencias automáticas que deben auditarse expresamente

La revisión prestará atención prioritaria a cualquier ascenso desde una señal textual hacia una categoría documental más fuerte.

Ejemplos:

```text
palabra → concepto
cópula → definición
oración → afirmación autoral
"no" → negación doctrinal
"solo" → restricción
proximidad textual → relación
semejanza léxica → identidad conceptual
```

Una señal de recuperación puede justificar un candidato sin justificar la categoría fuerte.

La fuerza máxima del registro deberá estar limitada por la evidencia disponible.

---

# 8. Tratamiento de conceptos y glosarios

Los glosarios constituyen evidencia documental privilegiada cuando la estructura de la obra los presenta como tales, pero no forman un universo conceptual cerrado.

La revisión deberá distinguir, al menos:

```text
concepto_declarado_en_glosario
concepto_establecido_en_cuerpo
candidato_de_recuperacion
```

El cuerpo puede establecer una designación conceptual mediante evidencia explícita suficiente.

Una palabra frecuente, un nombre de portada, un elemento de colofón o un término funcional no adquiere identidad conceptual por mera recurrencia.

---

# 9. Tratamiento de definiciones

Se conservará la distinción entre:

```text
definicion_explicita
definicion_candidata
```

Una definición candidata no se elevará para aumentar cobertura aparente.

Los glosarios deberán conservar, cuando exista, la entrada completa y su remisión documental.

La revisión deberá comprobar especialmente:

- inicio y final completos;
- pertenencia a una única unidad o tratamiento explícito de fragmentación;
- estatus enunciativo;
- concepto vinculado;
- criterio de detección;
- correspondencia exacta con la fuente.

---

# 10. Tratamiento de afirmaciones y predicaciones

La mera presencia de una proposición no la convierte en tesis autoral.

La revisión deberá comprobar que el estatus enunciativo intervenga antes de producir una clasificación fuerte cuando sea necesario.

Se auditarán particularmente:

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

Una pregunta, cita o condicional no deberá ascender automáticamente a predicación doctrinal positiva.

---

# 11. Negaciones, excepciones y restricciones

La presencia de un marcador léxico aislado no basta para establecer una categoría fuerte.

La revisión deberá intentar conservar documentalmente:

- proposición afectada;
- alcance del limitador;
- sujeto o concepto vinculado;
- texto exacto que introduce la limitación;
- estatus enunciativo.

Cuando el vínculo no pueda establecerse, el registro deberá permanecer candidato o no determinado.

---

# 12. Conversión documental y fórmulas

Los artefactos de PDF, Markdown u otras conversiones se consideran problemas documentales y se auditan separadamente de la doctrina.

Ejemplos:

```text
(cid:N)
saltos físicos de línea
folios
columnas fusionadas
tablas deformadas
fórmulas cortadas
caracteres perdidos
```

No se eliminará ni reconstruirá por conjetura un glifo desconocido.

La política es:

```text
resoluble contra fuente → corrección derivada documentada
no resoluble            → glifo_no_resuelto / no_determinado
```

Una fórmula no puede declararse íntegra si contiene pérdida documental no resuelta.

La fuente canónica de `corpus/fuentes/` permanece inmutable durante esta revisión. Cualquier vista normalizada deberá vivir fuera de ella y conservar correspondencia verificable con el original.

---

# 13. Mapa inicial de problemas a reproducir

La revisión parte de una auditoría externa del baseline que reportó, entre otros, los siguientes problemas. Estos hallazgos son **mapa de diagnóstico**, no nueva autoridad normativa; cada uno deberá reproducirse o verificarse dentro de la revisión antes de motivar cambios.

| Problema inicial | Tratamiento previsto |
|---|---|
| Cobertura funcional no ejercida por el gate F14 cuando un tipo carece de positivos | RC-7 |
| Fragmentos cortados a media oración | RC-1 / RC-2 |
| Palabras comunes o editoriales elevadas a conceptos | RC-1 / RC-2 |
| Definiciones generales presentes pero no consultables como categoría separada | RC-1 / RC-7 |
| Estatus enunciativo insuficientemente determinado | RC-1 / RC-2 |
| Artefactos `(cid:N)` y contaminación de conversión | RC-1 / RC-2 |
| Acumulación relacional y consumo de memoria en consulta | RC-7 |
| Barrido completo del maestro por lote de consultas | RC-7 |
| Respuestas masivas sin cursor o paginación | RC-7 |
| Restricciones o negaciones con cobertura anómala | RC-1 / RC-2 |
| Uso de `SystemExit` como contrato interno del motor de consulta | RC-7 |
| Colapso de estados distintos en recuperación relacional | RC-7 |

Las cifras concretas de la auditoría externa deberán considerarse mediciones de partida hasta que sean reproducidas por los productos de revisión.

---

# 14. Productos y estructura de trabajo esperada

Los productos de revisión deberán vivir fuera de `corpus/fuentes/` y fuera de los productos históricos del baseline.

Estructura recomendada:

```text
analista/revision-calibracion/
├── estado.json
├── incidencias-reproducidas.jsonl
├── regresiones/
└── obras/
    └── <obra_id>/
        ├── baseline/
        ├── expediente-revision.jsonl
        ├── auditoria-documental.jsonl
        ├── causas-raiz.json
        ├── calibrado/
        └── comparacion-antes-despues.json
```

Los nombres exactos de productos podrán versionarse mediante esquemas posteriores, pero deberán mantener separación entre baseline, auditoría y salida calibrada.

---

# 15. Fases de Revisión de Calibración

## RC-0 — Constitución de la revisión

### Objetivo

Fijar el contrato de calibración antes de tocar los motores.

### Entradas

- baseline `analisis-textual-v0.1` en commit `817b05a9a2eaa2643a5a49ec90f881b85a5d572e`;
- `analista/README.md`;
- `analista/FASES.md`;
- `analista/config/clausura-descriptiva.yaml`;
- este documento;
- auditoría externa utilizada como mapa inicial de problemas.

### Trabajo permitido

- registrar los hallazgos de partida;
- definir categorías de auditoría;
- definir productos de revisión;
- preparar herramientas para mostrar resultados y contexto;
- seleccionar la primera obra.

### Prohibido

- modificar todavía las reglas semánticas de los extractores;
- corregir manualmente doctrina;
- regenerar las veinte obras como nueva producción.

### Productos

- especificación RC vigente;
- configuración RC;
- baseline congelado;
- catálogo inicial de problemas por reproducir;
- selección de primera obra.

### Criterio de cierre

La revisión puede comenzar una obra sin ambigüedad sobre qué puede auditar el humano, qué se considera error y cómo se preserva el baseline.

---

## RC-1 — Auditoría documental de la primera obra

### Objetivo

Observar el comportamiento real del pipeline actual sobre una obra completa antes de modificarlo.

### Primera candidata

`corpus/fuentes/Caos_El_abismo_del_ego_y_la_doble_mediacion.md`.

La selección podrá cambiar solo por una razón operativa documentada.

### Trabajo

1. ejecutar el pipeline baseline aplicable a la obra;
2. conservar productos y hashes;
3. generar un expediente legible de revisión;
4. revisar conceptos, definiciones, afirmaciones/predicaciones, estatus, limitadores, fórmulas y trazabilidad;
5. registrar aciertos y errores;
6. agrupar casos por patrón;
7. identificar causas raíz probables sin modificar aún el motor durante la etapa de observación inicial.

### Criterio de cierre

Existe un catálogo reproducible de errores y aciertos de la obra, con evidencia exacta y causas raíz suficientemente identificadas para abrir calibración técnica.

---

## RC-2 — Calibración sobre la primera obra

### Objetivo

Corregir únicamente las causas raíz demostradas por RC-1.

### Trabajo

- aplicar la corrección mínima;
- añadir pruebas de regresión;
- reejecutar la obra completa;
- comparar baseline y salida calibrada;
- comprobar que los aciertos anteriores se conservan;
- repetir mientras existan errores sistémicos conocidos de la primera obra.

### Criterio de cierre

Los errores sistémicos confirmados en RC-1 están resueltos, explícitamente degradados a candidato/no determinado, o documentados como limitación no resoluble sin introducir doctrina.

---

## RC-3 — Prueba de generalización en una segunda obra

### Objetivo

Probar los motores calibrados sin adaptarlos previamente a una obra estructuralmente diferente.

### Selección

La segunda obra deberá añadir una dificultad distinta de la primera: por ejemplo fórmulas, fuerte contaminación de conversión, estructura de glosario diferente o prosa técnica.

### Trabajo

- ejecutar directamente la versión calibrada;
- auditar resultados con el mismo protocolo;
- distinguir errores ya conocidos de familias nuevas;
- comprobar si las correcciones de RC-2 generalizan.

### Criterio de cierre

Se conoce qué correcciones generalizan y qué nuevas familias de error aparecen en la segunda obra.

---

## RC-4 — Calibración multilibro

### Objetivo

Corregir las nuevas causas raíz encontradas en RC-3 sin degradar la primera obra.

### Trabajo

- ajustar motores solo por causas demostradas;
- añadir regresiones nuevas;
- ejecutar nuevamente obra 1 y obra 2;
- comparar métricas y casos auditados en ambas.

### Criterio de cierre

Las dos obras pasan conjuntamente las regresiones conocidas y no existe una mejora para una que deteriore silenciosamente la otra.

---

## RC-5 — Validación de generalización

### Objetivo

Determinar si el comportamiento calibrado generaliza suficientemente para dejar de incorporar obras a la revisión manual intensiva.

### Trabajo

- introducir una tercera obra sin adaptación previa;
- introducir una cuarta solo si la tercera revela familias nuevas relevantes o si se necesita cubrir otra estructura documental;
- reejecutar las obras anteriores cuando cambie el motor;
- medir la aparición de nuevas familias de error.

### Criterio de cierre

Las nuevas obras dejan de revelar errores sistémicos de clase nueva y las correcciones acumuladas permanecen estables en las obras anteriores.

El cierre no depende de alcanzar exactamente cuatro obras.

---

## RC-6 — Regeneración controlada del corpus

### Objetivo

Aplicar los motores calibrados a todas las obras previstas sin convertir la revisión humana en una corrección manual de veinte libros.

### Trabajo

- ejecutar el pipeline calibrado sobre todas las obras;
- ejecutar regresiones automáticas;
- producir métricas de anomalías y distribución;
- detectar desviaciones respecto del conjunto de calibración;
- investigar solo anomalías que indiquen posibles familias nuevas de error.

### Criterio de cierre

Todas las obras generan productos compatibles, trazables y libres de regresiones conocidas; cualquier anomalía nueva está resuelta o documentada antes de reconstruir los maestros globales.

---

## RC-7 — Revalidación de F9–F15

### Objetivo

Reconstruir y volver a validar los productos superiores a partir de los datos calibrados, conservando lo que siga cumpliendo sus contratos.

### Trabajo

Revisar, en orden:

1. ensamblado y maestro de obra;
2. comparación interobra;
3. auditoría del corpus;
4. maestro del corpus;
5. motor de consulta literal;
6. interfaz para sistemas de IA.

En F14 se separarán expresamente:

```text
gate de contrato de respuesta
gate de cobertura funcional
```

También se evaluarán, solo después de la calidad documental:

- índice de recuperación;
- memoria;
- paginación/cursor;
- tipos de consulta;
- distinción de estados relacionales;
- excepciones de dominio frente a `SystemExit`.

### Criterio de cierre

Los productos regenerados mantienen cadena de custodia, clausura descriptiva y capacidad de consulta, y los gates pueden detectar tanto respuestas inválidas como ausencia funcional de cobertura donde corresponda.

---

## RC-8 — Cierre de la revisión

### Objetivo

Demostrar qué cambió respecto del baseline y declarar el alcance real de la calibración.

### Comparación mínima

```text
baseline v0.1
vs.
revisión calibrada v0.2
```

La comparación deberá reportar, como mínimo:

- familias de error encontradas;
- regresiones creadas;
- errores resueltos;
- limitaciones no resueltas;
- distribución de conceptos;
- definiciones explícitas y candidatas;
- predicaciones;
- estatus enunciativos;
- negaciones, excepciones y restricciones;
- fórmulas completas/incompletas;
- trazabilidad;
- cobertura funcional;
- tamaño de productos;
- memoria y tiempo de consulta cuando proceda;
- hashes y versiones de los nuevos productos.

### Criterio de cierre

La calibración puede defenderse documentalmente en varias obras, generaliza al corpus completo sin regresiones conocidas y ningún nuevo registro contiene una afirmación más fuerte que la evidencia verificada de la que procede.

---

# 16. Regla de avance entre fases RC

No se adelanta una fase por conveniencia.

Antes de cerrar cada RC deben responderse afirmativamente estas preguntas:

1. ¿El producto de la fase existe y es reproducible?
2. ¿La evidencia utilizada es trazable hasta la fuente?
3. ¿La intervención humana se mantuvo documental y no doctrinal?
4. ¿Las correcciones realizadas responden a errores demostrados?
5. ¿Se preservaron los aciertos anteriores?
6. ¿Las nuevas reglas están cubiertas por regresiones cuando corresponde?
7. ¿La clausura descriptiva permanece intacta?

Si alguna respuesta es negativa, la fase permanece abierta.

---

# 17. Criterio de detención de la revisión manual intensiva

La revisión obra por obra no pretende convertirse en revisión manual de las veinte obras.

La incorporación de nuevas obras al conjunto intensivo se detiene cuando:

- una obra nueva no introduce familias importantes de error;
- las correcciones existentes generalizan sin reglas ad hoc;
- los motores mantienen sus regresiones en todas las obras ya calibradas;
- las anomalías restantes pueden detectarse automáticamente en RC-6.

Si una nueva obra introduce una familia estructural no contemplada, se reabre calibración únicamente para esa causa y luego se vuelven a ejecutar las obras anteriores pertinentes.

---

# 18. Regla final

Durante toda la revisión se aplicará la siguiente regla:

> **No corregimos lo que dice la obra. Corregimos únicamente la manera en que el motor observa, segmenta, recupera, clasifica y representa lo que la obra efectivamente contiene.**

Cuando la fuente no permita demostrar una clasificación:

> **NO DETERMINADO POR EL CORPUS.**
