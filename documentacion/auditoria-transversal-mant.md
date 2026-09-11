# AUD-MANT-TRANS-001 — Verificación transversal previa a la campaña de segunda edición

> **Documento derivado de auditoría transversal.** No modifica fuentes canónicas, no ejecuta correcciones de segunda edición y no convierte deudas formales o empíricas en resultados validados. Su función es comprobar si las tensiones MANT registradas cuentan ya con una adjudicación suficiente para iniciar la campaña editorial y clasificar con precisión lo que todavía permanece abierto.

- **ID:** `AUD-MANT-TRANS-001`
- **Estado:** **CHECKPOINT MANT CERRADO / DEUDAS 2E CLASIFICADAS / CAMPAÑA 2E HABILITADA**
- **Fecha:** 2026-09-10
- **Fase:** MANT — mantenimiento posterior a mapa maestro v1
- **Alcance:** resoluciones MANT, auditorías derivadas y registro de segunda edición existentes en `documentacion/`
- **Límite:** esta verificación no sustituye una nueva auditoría línea por línea de todo el corpus ni declara validación científica externa de los modelos.

## 1. Pregunta de cierre

La verificación responde:

> **¿queda alguna tensión doctrinal, semántica o formal prioritaria ya identificada por MANT que todavía carezca de adjudicación suficiente para pasar a trabajo de segunda edición?**

La respuesta, sobre el conjunto actualmente registrado, es:

> **no se detecta una contradicción doctrinal prioritaria sin adjudicación; sí permanecen deudas formales, metrológicas, empíricas y editoriales sustantivas que constituyen precisamente el trabajo de segunda edición.**

Esta distinción es necesaria. Una deuda de calibración no equivale a una contradicción doctrinal; una fórmula histórica inválida ya adjudicada no sigue siendo una decisión autoral abierta; y una interfaz que requiere reparación editorial no debe reabrirse como si el referente ontológico estuviera nuevamente en disputa.

## 2. Criterios de clasificación

Esta auditoría usa cuatro estados distintos.

### 2.1 Tensión adjudicada

Existe una adjudicación que fija qué lectura o arquitectura gobierna hacia adelante, aunque la primera edición conserve la formulación histórica.

### 2.2 Deuda formal/metrológica

El objeto conceptual está fijado, pero falta un estimador, operador, demostración, tipado o regla de combinación matemáticamente válida.

### 2.3 Deuda empírica/calibración

La arquitectura puede estar bien tipada, pero faltan datos, validación externa, parámetros, perfiles por dominio o evidencia para sostener números concretos.

### 2.4 Deuda editorial/interfaz

La adjudicación ya existe, pero debe incorporarse en segunda edición mediante crosswalks, renotación, separación de capas, aclaraciones de alcance, corrección de tablas, ejemplos o protocolos.

Sólo el primer estado bloquea por sí mismo el cierre de una tensión MANT. Los otros tres son trabajo legítimo de segunda edición y no deben disfrazarse de doctrina resuelta ni de contradicción pendiente.

## 3. Matriz de tensiones prioritarias

| Familia | Adjudicación vigente | Estado transversal | Trabajo pendiente |
| --- | --- | --- | --- |
| Aego / afasia volitiva | `RES-AEGO-001` | cerrada doctrinalmente | crosswalk histórico en 2E |
| `R*` / operador causal | `RES-RSTAR-001` | núcleo formal adjudicado | `w`, equivalencia contrafáctica, feedback y recálculos |
| α / asunción | `RES-ALPHA-001` | núcleo doctrinal adjudicado | observabilidad, calibración, escalas por dominio |
| Δ | `RES-DELTA-001` | fórmula y signo adjudicados | conmensurabilidad, agregados, recálculos |
| `Δ_B` | `RES-DELTAB-001` | objeto/tipo/fórmula adjudicados | `G_B`, `R*_B`, beneficio total, doble conteo |
| φ₂ / observabilidad | `RES-PHI2-OBS-001` | frontera ontológica/metrológica adjudicada | fiabilidad e identificabilidad de proxies |
| `RSC` / `I(t)` | `RES-RSC-IT-001` | distinción conceptual adjudicada | representación matemática y operador de integración |
| `S` | `AUD-S-001` + adjudicación autoral de `2E-S-001` (`1a532f07`) | constructo adjudicado | contrafactual exacto, estimador, proxies y calibración |
| SDO → Prometeo | `RES-SDO-PROM-001` | interfaz conceptual adjudicada | reparación editorial y validación instrumental |
| HISTOS → Prometeo | `RES-HISTOS-PROM-001` + precisión | interfaz/temporalidad adjudicadas | implementación editorial, trazabilidad y validación |
| E0–E8 / `w` | `RES-EVID-001` | arquitectura epistémica adjudicada | estimador `ŵ`, `U(ŵ)`, perfiles y combinación |
| IIC | `RES-IIC-001` | escala/semántica adjudicadas | estimador, materialidad, `k`, ajuste de `W`, fraude annona |
| REC | `RES-REC-001` | error formal y alcance adjudicados | multinomial, Fisher matricial, `τ`, predictibilidad |

La existencia de una entrada `2E-...` no se usa por sí sola como prueba de que un problema esté matemáticamente resuelto. En `S`, sin embargo, el propio commit `1a532f07e31eb8e65662088e159a6a7ea999c100` registra expresamente una **adjudicación autoral** del constructo; por ello no hacía falta crear una resolución adicional para volver a decidir lo ya decidido.

## 4. Comprobación de `S`: ya estaba resuelta

La revisión del historial anterior a esta auditoría muestra una secuencia suficiente y explícita:

- `d5bde166600171908aee4e0cdccb0200739bb625` añadió `AUD-S-001` y decidió que **no existe tensión doctrinal nuclear en S**: el concepto de sustituibilidad es estable, mientras los problemas pertenecen al tipado, la formalización y la calibración;
- `1a532f07e31eb8e65662088e159a6a7ea999c100` añadió `2E-S-001` y registró expresamente la **adjudicación autoral**: el concepto de sustituibilidad se mantiene y la segunda edición debe normalizar su fórmula y aparato de medición sobre el `R*` vigente, separando constructo, estimador y operacionalización.

Por tanto, la afirmación de que faltaba una adjudicación autónoma de `S` fue incorrecta. La ausencia de un archivo llamado `resolucion-s.md` no significaba ausencia de decisión: la decisión ya estaba fijada materialmente por el commit autoral de `2E-S-001`.

La creación posterior de `RES-S-001` en `4d8ce7263d81dae78360bd37f859222b57c05075` fue redundante y fue retirada en `318ae81cd414915d0796f91bf848c2fecb8cd945`. No añade una nueva doctrina ni constituye una segunda adjudicación del mismo objeto.

La lectura vigente de `S` continúa siendo la ya fijada antes de esta verificación:

`constructo S estable ≠ S_prob ≠ S_op ≠ S_est ≠ S_app`.

El estimador formal sigue pendiente; la doctrina del objeto no.

## 5. Deudas formales de alta dependencia

### 5.1 Entrada causal `w` y evidencia

`RES-RSTAR-001` fija el operador de atribución, pero el operador recibe pesos locales `w` cuya estimación todavía debe reconstruirse bajo `RES-EVID-001`.

Por ello no conviene iniciar una campaña masiva de recálculo de `R*` usando las antiguas bandas E→`w`.

Dependencia correcta:

`evidencia → existencia/mecanismo de arista → ŵ + U(ŵ) → Q_D,b_D → R*`.

Antes de recalcular ejemplos debe existir una semántica operacional mínima para `ŵ` y `U(ŵ)`. Los valores numéricos de calibración pueden permanecer provisionales o ausentes; lo que no puede permanecer es la confusión entre calidad epistémica y posición de `w`.

### 5.2 `review.calc.rstar_equivalence`

`RES-RSTAR-001` conserva abierta la relación entre:

- necesidad contrafáctica;
- pesos escalares locales;
- proporción estable `R*`;
- eventual fracción material de daño.

Esto no reabre qué algoritmo calcula `R*`. Sí exige que segunda edición no pase automáticamente de una proporción causal normalizada a una afirmación de fracción física, monetaria o jurídica del daño sin un puente adicional.

Se clasifica como **deuda de interpretación/metrología de alta dependencia**, no como segunda definición rival de `R*`.

### 5.3 `RSC` e `I(t)`

La doctrina ya distingue:

`RSC = registro histórico`

`I(t) = estado agregado derivado`.

Pero falta decidir la estructura matemática que preserve identidad, multiplicidad, temporalidad y marcas de integración, y el operador que proyecta esa historia hacia `I(t)`.

Esta deuda es upstream para cualquier formalización interna de α que dependa de pertenencia/integración de eventos.

### 5.4 `S`

El constructo está adjudicado, pero `S_est` histórico no puede sobrevivir y `S_op` no es idéntico al constructo.

La reconstrucción debe ocurrir después de fijar el operador vigente de `R*` —ya hecho— y antes de recalcular sistemáticamente `R*_neta` o scores dependientes de sustituibilidad.

### 5.5 Δ y conmensurabilidad

La operación correcta es:

`Δ=R*−α`.

Sin embargo, una resta formalmente correcta sólo es metrológicamente interpretable si `R*` y α están en escalas comparables para la aplicación concreta.

Las revisiones de magnitud, apéndice y comparabilidad no deben cerrarse por arrastre desde `RES-DELTA-001`.

### 5.6 IIC

La escala `[0,1]` y la separación frente a correlación/dirección están adjudicadas. No lo están:

- el estimador universal de congruencia;
- la ponderación de protocolos;
- la calibración de `k`;
- la validez causal del ajuste de `W`;
- la forma multiplicativa y umbral de fraude annona.

Se trata de decisiones/modelos que requieren demostración o validación, no de contradicciones semánticas ya abiertas.

### 5.7 REC

La cota condicional `ΔI·Δh≥τ/n` puede conservarse dentro del modelo logístico-Bernoulli realmente demostrado.

La extensión a softmax multinomial, Fisher matricial, estimación real de `τ` y relación con predictibilidad permanecen trabajo formal/empírico. La forma histórica con factor `4` no debe reaparecer como deuda por resolver: ya fue adjudicada como no demostrada.

## 6. Deudas empíricas y de calibración

Permanecen abiertas, entre otras:

- estimación y validación de `w`;
- perfiles de incertidumbre `U(ŵ)` por dominio;
- calibración de scores de `S` y rangos por Hijos;
- calibración/validez de escalas internas y aplicadas de α;
- validez de ECO, SDO e HISTOS como proxies de integración o contexto;
- atribución de cambio durante HISTOS;
- calibración de `k` y del umbral `0.20` de fraude annona;
- calibración de `τ`, `η(τ)` y predictibilidad;
- construcción y validación de `G_B`/`R*_B`;
- traducción de magnitudes causales a daño, beneficio u otras unidades materiales.

Estas deudas no impiden comenzar la campaña editorial. Sí impiden presentar números no validados como propiedades necesarias del paradigma.

## 7. Deudas editoriales e interfaces ya tipadas

Las resoluciones existentes ya permiten corregir sin nueva doctrina:

- Aego temprano ↔ afasia volitiva madura;
- `R*` separado de φ₂ y del eigenvector de `W` cruda;
- α interno/clínico ↔ α aplicado, sin identidad automática de escala;
- `Δ=R*−α`, con posibilidad de signo negativo;
- `RSC` como historia e `I(t)` como proyección;
- SDO/HISTOS como fuentes de señal/contexto y no como sustitutos del grafo causal;
- ejecución de Prometeo separada de transferencia de datos y retroalimentación al acompañamiento;
- firewall funcional HISTOS/Prometeo;
- E0 como nulidad documentada, no ausencia de evidencia;
- E1–E8 como fuerza epistémica y no posición de `w`;
- IIC no direccional separado de correlación/oposición;
- REC histórica con factor `4` separada del resultado realmente demostrado.

Aquí el trabajo pendiente es de incorporación y pruebas editoriales, no de inventar una tercera solución.

## 8. Familias heredadas que no constituyen por sí solas bloqueadores de campaña

El registro general de segunda edición conserva familias que todavía no han sido elevadas a una tensión prioritaria adjudicada individualmente, entre ellas:

- Shapley y causalidad acumulativa;
- Itô y extensiones estocásticas;
- daño, tiempo de vida y reglas de conversión;
- criterios de cierre y seguimiento HISTOS;
- crosswalk ECO/HISTOS/Prometeo más amplio;
- portabilidad de Taxonomía entre dominios;
- correspondencias funcionales en sistemas artificiales sin promoverlas a subjetividad o conciencia.

Esta auditoría no las declara resueltas. Las clasifica como **backlog de investigación/formalización/editorial no bloqueante** mientras ninguna corrección concreta de segunda edición dependa de ellas.

Si durante una edición concreta una de estas familias se vuelve necesaria para sostener una afirmación, debe recibir su propia auditoría antes de incorporarse.

## 9. Orden de dependencias para la campaña formal

No toda segunda edición necesita ser estrictamente serial. Conviene separar al menos dos carriles upstream.

### Carril causal

`EVID / estimación de w e incertidumbre`

`→ R* y recálculos`

`→ S formal`

`→ Δ / Δ_B y magnitudes dependientes`

`→ IIC y ajustes estructurales`

`→ ejemplos, tablas y aplicaciones`.

### Carril de integración

`RSC / registro de eventos`

`→ operador de integración e I(t)`

`→ formalización interna/observacional de α`

`→ comparabilidad con α aplicado`

`→ Δ y crosswalks instrumentales`.

Las reparaciones puramente textuales que ya tienen adjudicación —por ejemplo, Aego, terminología de φ₂ o advertencias de alcance— pueden avanzar en paralelo, siempre que no congelen una fórmula dependiente de un carril aún abierto.

## 10. Criterio de preparación para segunda edición

La campaña puede comenzar porque:

1. las principales tensiones de significado cuentan con resolución;
2. los errores formales conocidos están tipados y no deben conservarse por inercia;
3. las interfaces SDO/HISTOS/Prometeo tienen reglas de independencia suficientes para editarse;
4. existe un inventario de entradas `2E-...` preparado;
5. las deudas restantes pueden tratarse como trabajo formal, empírico o editorial con proveniencia explícita.

Pero **PREPARADO no significa INCORPORADO**.

Ninguna entrada deberá marcarse incorporada si depende de:

- una fórmula todavía no reconstruida;
- una calibración inventada;
- una escala no comparable;
- una validación empírica inexistente;
- un recálculo no ejecutado;
- una nueva decisión autoral genuina todavía abierta.

## 11. Resultado de la verificación

Dentro del conjunto de tensiones MANT registradas y revisadas transversalmente:

- no queda una segunda definición doctrinal rival sin adjudicación para Aego, R*, α, Δ, Δ_B, φ₂, RSC/I(t), S, E0–E8, IIC o REC;
- SDO→Prometeo e HISTOS→Prometeo tienen ya arquitectura de interfaz suficiente para distinguir señal/contexto de medición causal;
- los problemas restantes se localizan en formalización, calibración, validación, recálculo o incorporación editorial;
- no se detecta una razón para reiniciar la auditoría prioritaria antes de abrir segunda edición.

Esta conclusión es **suficiente para el checkpoint MANT** y no pretende afirmar que el corpus carece de toda posible tensión futura. Una auditoría independiente que identifique una contradicción nueva reabre únicamente la familia afectada.

## 12. Contraste con la auditoría paralela del autor — completado

El autor completó una auditoría independiente y confirmó que su resultado coincide sustantivamente con `AUD-MANT-TRANS-001`.

Quedan expresamente confirmados:

- la separación entre tensión adjudicada, deuda formal/metrológica, deuda empírica/calibración y deuda editorial/interfaz;
- los dos carriles de dependencia del §9;
- la ausencia de contradicciones doctrinales prioritarias sin adjudicación;
- que las diferencias surgidas durante la sesión fueron de inventario/estado documental y no doctrinales;
- la regla **PREPARADO ≠ INCORPORADO**;
- que el inventario exhaustivo de apariciones de `R*` es el prerequisito técnico real antes de ejecutar correcciones dependientes.

Por tanto:

> **el checkpoint MANT queda cerrado y la campaña de segunda edición queda habilitada.**

La habilitación no autoriza a inventar calibraciones ni a tratar como demostradas las formalizaciones que permanecen abiertas.

## 13. Primer prerequisito de campaña 2E

Antes de modificar una fuente canónica dependiente de `R*`, debe completarse un inventario transversal de todas sus apariciones y clasificarlas al menos como:

1. definición directa;
2. axioma, lema, teorema o prueba;
3. fórmula dependiente;
4. vector o valor numérico publicado;
5. ejemplo o caso calculado;
6. código/pseudocódigo;
7. interfaz con otro objeto (`S`, `Δ`, `Δ_B`, IIC u otros).

La razón es de dependencia: una sustitución local de la definición de `R*` puede dejar intacta una prueba, un ejemplo o una fórmula aguas abajo que ya no sea válida bajo el operador vigente.

El inventario precede a la incorporación editorial. Ningún recálculo se ejecutará usando las antiguas bandas `E→w` como si siguieran siendo una calibración canónica después de `RES-EVID-001`.
