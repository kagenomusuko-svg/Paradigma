# 2E-HISTOS-PROM-001 — Corrección editorial de la interfaz HISTOS → Prometeo

> **Producto editorial derivado para segunda edición.** Ejecuta `RES-HISTOS-PROM-001` cuando se prepare una nueva edición. No modifica las fuentes canónicas de primera edición.

- **ID:** `2E-HISTOS-PROM-001`
- **Estado:** **PREPARADO PARA SEGUNDA EDICIÓN / EJECUCIÓN DIFERIDA**
- **Prioridad:** alta
- **Resolución rectora:** `RES-HISTOS-PROM-001`
- **Resoluciones relacionadas:** `RES-ALPHA-001`, `RES-DELTA-001`, `AUD-S-001` / `2E-S-001`, `RES-RSTAR-001`, `RES-PHI2-OBS-001`, `RES-SDO-PROM-001`
- **Ámbito principal:** HISTOS P·1, P·2, V·3, VI·2 y toda referencia interna que use `α`, `S`, `Δ`, `P(Hijos)` o «convergencia» para describir la interfaz con Prometeo; referencias cruzadas en Prometeo/Taxonomía sólo cuando atribuyan transferencia directa desde HISTOS.

---

## 1. Principio editorial rector

La segunda edición deberá organizar toda la interfaz bajo esta regla:

> **referente compartido ≠ estimando compartido ≠ evidencia compartida.**

HISTOS y Prometeo pueden presentarse como instrumentos complementarios sobre una familia ontológica común, pero no como instrumentos que producen automáticamente las mismas magnitudes con evidencia intercambiable.

La redacción debe distinguir siempre:

1. qué fenómeno general comparten;
2. qué estima cada instrumento;
3. con qué evidencia lo estima;
4. en qué momento temporal se obtuvo el dato;
5. qué uso puede hacer el otro instrumento de ese dato.

---

## 2. Reescribir la arquitectura de VI·2

La tabla actual de VI·2 contiene una columna de «limitaciones del aporte». Esa estructura es insuficiente porque deja la cautela como advertencia posterior a una transferencia que el resto de la tabla parece autorizar.

La segunda edición deberá convertir esas limitaciones en **condiciones previas de procesabilidad**.

La nueva tabla debe contener, como mínimo, estas columnas:

- salida de HISTOS;
- estimando local;
- fuente de evidencia;
- período/fecha;
- dominio/acto;
- estado pre/post intervención;
- certeza/incertidumbre;
- uso permitido en Prometeo;
- inferencia prohibida;
- evidencia independiente requerida;
- consentimiento/finalidad de transferencia.

No basta con decir después que el aporte es limitado: la tabla debe impedir desde su diseño una lectura de transferencia directa.

---

## 3. Renotar α por dominio instrumental

La segunda edición no debe usar una única columna `α` para HISTOS y Prometeo.

Usar, provisionalmente o mediante una notación editorial equivalente:

- `α_H`: estimación cualitativa de integración/asunción interna durante HISTOS;
- `α_P`: asunción efectiva aplicada de Prometeo, sustentada por acciones o consecuencias verificables.

La notación definitiva puede cambiar, pero la distinción debe ser visible.

### Regla de redacción

No escribir:

`α de HISTOS → α de Prometeo`

como identidad.

Escribir:

`α_H → contexto/hipótesis sobre asunción → evidencia independiente → α_P`

cuando la transferencia sea metodológicamente pertinente.

---

## 4. Separar las escalas numéricas de α

Las bandas numéricas de HISTOS que coinciden superficialmente con rangos usados en Prometeo deben dejar de sugerir conmensurabilidad automática.

La segunda edición deberá escoger una de estas dos soluciones editoriales:

### Opción preferente

Conservar los niveles de HISTOS como categorías/intervalos **locales del proceso**, identificados expresamente como `α_H`, sin afirmar que un valor o rango corresponde numéricamente a `α_P`.

### Opción futura condicionada

Si se desea una función de traducción cuantitativa entre `α_H` y `α_P`, deberá definirse como un objeto nuevo con:

- dominio y codominio;
- observables de entrada;
- regla de transformación;
- incertidumbre;
- condiciones de validez;
- calibración;
- validación independiente.

Mientras esa función no exista y no esté validada, **no hay traducción numérica**.

---

## 5. Contraejemplos obligatorios para α

La nueva edición debe incluir o superar conceptualmente dos pruebas de consistencia.

### Caso A — integración interna alta, asunción aplicada baja

Un sujeto reconoce e integra causalmente el acto en HISTOS, pero todavía no ha reparado, pagado ni modificado externamente el sistema.

Resultado esperado:

`α_H alto` puede coexistir con `α_P bajo`.

### Caso B — asunción aplicada alta, integración interna baja

Un actor recibe una sanción, embargo, despido o consecuencia impuesta que Prometeo registra como asunción efectiva, pero no reconoce ni integra subjetivamente el acto.

Resultado esperado:

`α_P alto` puede coexistir con `α_H bajo`.

Cualquier redacción que haga imposibles estos dos casos confunde estimandos.

---

## 6. Renotar Δ y retirar la identidad automática

La segunda edición debe distinguir:

- `Δ_H`: déficit cualitativo de asunción/integración dentro del proceso HISTOS;
- `Δ_P = R* − α_P`: brecha formal aplicada de Prometeo.

No presentar `Δ_H` como si fuera el resultado de la resta formal cuando HISTOS no ha calculado `R*` ni ha construido `α_P`.

El momento del arco, la historia de bloqueos o `α_H` pueden contextualizar la investigación de `Δ_P`, pero no producirlo.

### Redacción que debe evitarse

> «HISTOS mide el mismo Δ que Prometeo.»

### Redacción correcta

> «HISTOS sigue cualitativamente una brecha de asunción interna análoga en genealogía conceptual a la brecha aplicada que Prometeo calcula como `R* − α_P`; las dos no son el mismo estimando ni comparten automáticamente escala.»

---

## 7. Renotar S y cortar la inferencia P(Hijos) → S_P

La segunda edición deberá distinguir:

- `S_H`: indicador cualitativo de dependencia del campo/idiosincrasia usado durante HISTOS;
- `S_P`: sustituibilidad estructural contrafáctica de Prometeo.

`P(Hijos)` puede orientar una hipótesis de investigación, pero no asigna `S_P`.

Eliminar o reformular expresiones equivalentes a:

> «Fobos dominante permite estimar S alta en Prometeo.»

La relación correcta es:

`P(Hijos) → hipótesis sobre patrones de actuación → investigación de estructura del rol/sistema → S_P`.

Prometeo debe conservar sus propios criterios estructurales y evidenciales.

---

## 8. Prueba obligatoria para S

La edición debe admitir el siguiente caso:

Dos actores con el mismo Hijo dominante pueden tener `S_P` radicalmente distinto si sus posiciones estructurales difieren.

Ejemplo abstracto:

- actor A: rol altamente formalizado, alto costo de desobediencia, reemplazabilidad amplia;
- actor B: rol discrecional, baja fungibilidad, decisiones no prescritas por el sistema.

Aunque ambos compartan un patrón Fobos, `S_P(A)` puede ser alto y `S_P(B)` bajo.

Si el texto deriva el mismo S de la coincidencia del Hijo, la interfaz sigue mal tipada.

---

## 9. Reescribir el lenguaje de «convergencia»

La convergencia entre HISTOS y Prometeo no debe llamarse sin calificación:

- validación cruzada;
- prueba independiente;
- confirmación de precisión;
- demostración de solidez externa.

Puede describirse como:

- consistencia interna;
- corroboración contextual;
- convergencia de perspectivas;
- reducción de incertidumbre bajo supuestos explícitos;
- señal para análisis de sensibilidad;
- razón para buscar evidencia adicional.

La segunda edición debe advertir que instrumentos que comparten teoría, categorías, datos o juicios de operador no son independientes por mera pluralidad de nombres.

---

## 10. Arquitectura de evidencia: segundo nivel, no sustitución

La frase de VI·2 según la cual las salidas de HISTOS son «estimaciones cualitativas de segundo nivel que reducen incertidumbre sin reemplazar el análisis documental» debe convertirse en regla rectora y no permanecer sólo como síntesis o advertencia.

Toda transferencia debe obedecer:

`dato HISTOS`

`→ contexto / hipótesis / reducción de incertidumbre`

`→ evidencia independiente del caso`

`→ reconstrucción causal Prometeo`

`→ parámetro aplicado`.

Queda prohibida editorialmente la secuencia implícita:

`dato HISTOS → parámetro Prometeo`.

---

## 11. Añadir procedencia temporal obligatoria

HISTOS modifica deliberadamente el sistema observado a lo largo del tiempo. Por ello, todo dato transferible debe indicar:

- `t0`: tiempo del hecho/estado que Prometeo reconstruye;
- fecha o intervalo real de observación HISTOS;
- número o fase de sesión cuando corresponda;
- si la observación antecede o sigue a una intervención relevante;
- dominio del acto;
- estado del arco.

### Regla de no retroproyección

Una observación obtenida después de intervención no puede describirse como evidencia contemporánea de `t0` salvo que exista una inferencia explícita sustentada por evidencia independiente.

La redacción debe distinguir:

- «el sujeto presenta X en `t2`»;
- «X es compatible con la hipótesis de que… en `t0`»;
- «la evidencia contemporánea de `t0` demuestra…».

Son proposiciones de distinto estatus.

---

## 12. Separar tres operaciones del handoff

La segunda edición debe abandonar «operación paralela» como etiqueta única y separar tres flujos.

### A. Ejecución Prometeo

El analista puede ejecutar una reconstrucción documental independiente sin introducirla al acompañamiento.

### B. Transferencia HISTOS → Prometeo

Requiere consentimiento, finalidad definida, resumen tipado, procedencia temporal, dominio, certeza y carácter de segundo nivel.

### C. Retroalimentación Prometeo → HISTOS / sujeto

Puede modificar el proceso de `φ₂` y por ello requiere una regla distinta.

El umbral `M·3+` debe asociarse explícitamente a esta retroalimentación en el dominio pertinente.

---

## 13. Precisar M·1/M·2 frente a M·3+

La nueva edición debe decir expresamente:

- estar en `M·1` o `M·2` no vuelve inválido por sí mismo un análisis documental independiente ejecutado fuera del proceso;
- lo que debe restringirse es la introducción de conclusiones o atribuciones externas que puedan forzar el arco antes de que el sujeto pueda trabajarlas;
- `M·3+` es condición de retroalimentación al acompañamiento para el dominio de los actos analizados, además de las demás condiciones de consentimiento y seguridad del protocolo.

No usar el momento global del sujeto si el estado difiere por dominio.

---

## 14. Implementar firewall informacional

La segunda edición debe convertir el principio de no-contaminación en un protocolo operativo.

### Hacia el analista

El mediador prepara un **resumen mínimo necesario**, no una apertura indiscriminada del expediente.

El resumen debe excluir contenido irrelevante para la finalidad autorizada.

### Hacia el mediador

Mientras no proceda retroalimentación, el analista no comunica información que pueda sesgar el acompañamiento, incluyendo:

- actos específicos seleccionados para imputación si su revelación orientaría sesiones;
- hipótesis causales sobre responsabilidad;
- ranking de nodos;
- `R*`, `S_P`, `α_P`, `Δ_P`;
- Declaraciones A–D;
- conclusiones sobre qué debería asumir el sujeto.

### Consentimiento

El consentimiento es:

- específico;
- informado respecto de finalidad;
- revocable;
- registrable;
- no equivalente a renuncia general a confidencialidad.

---

## 15. Separación funcional de roles

La edición debe indicar que el protocolo concurrente ordinario presupone dos funciones separadas:

- mediador HISTOS;
- analista Prometeo.

Una misma persona no puede desconocer activamente información que ya posee. Por ello, la dualidad de roles sobre el mismo dominio/caso no puede presentarse como equivalente al protocolo ordinario con firewall.

Si una futura edición desea autorizar un régimen excepcional de doble rol, deberá definirlo por separado con reglas de segregación, registro, uso de información y límites. Mientras no exista ese protocolo, la operación concurrente estándar debe mantener separación funcional.

---

## 16. Formato mínimo del resumen HISTOS → Prometeo

La segunda edición deberá incorporar una plantilla o especificación equivalente con al menos:

- identificador del caso;
- finalidad autorizada;
- período cubierto;
- dominio/actos a los que se refiere;
- estado del proceso por período;
- `P(Hijos)` con incertidumbre declarada;
- `α_H` cualitativo por período y dominio;
- `S_H` cualitativo por período y dominio;
- `Δ_H` cualitativo por período y dominio;
- historia de bloqueos pertinente;
- fuente de cada dato;
- marca pre/post intervención;
- limitaciones de inferencia;
- consentimiento y fecha;
- responsable de preparación;
- advertencia explícita: **no sustituye evidencia documental ni produce parámetros Prometeo**.

---

## 17. Registro de transferencias

La interfaz debe conservar un log mínimo de:

- fecha;
- emisor;
- receptor;
- contenido transferido;
- finalidad;
- consentimiento vigente;
- restricciones;
- uso posterior;
- eventual devolución de resultados;
- momento del arco al realizar la devolución.

Esto permite auditar contaminación, procedencia y uso secundario de información.

---

## 18. No convertir el firewall en validación causal

La existencia de un firewall protege independencia operativa, pero no prueba validez de los instrumentos.

La segunda edición debe mantener abiertas por separado:

- calibración de `α_H`;
- calibración de `S_H`;
- eventual formalización de `Δ_H`;
- reproducibilidad inter-mediador;
- fiabilidad longitudinal;
- atribución causal del cambio a HISTOS;
- eficacia del acompañamiento;
- equivalencia empírica entre resultados HISTOS y Prometeo.

La arquitectura correcta evita circularidad; no convierte por ello los parámetros en validados empíricamente.

---

## 19. Pruebas editoriales obligatorias

Antes de incorporar esta reparación a una segunda edición, la redacción debe superar al menos estas seis pruebas:

1. **α divergente:** permite `α_H` alto con `α_P` bajo y viceversa.
2. **S estructural:** permite dos sujetos con el mismo Hijo dominante y `S_P` distinto por estructura del rol/sistema.
3. **Δ tipado:** nunca calcula `Δ_P` desde un `Δ_H` cualitativo sin `R*` y `α_P` propios.
4. **tiempo:** un dato observado post-intervención no aparece como evidencia contemporánea de `t0`.
5. **M·1/M·2:** Prometeo puede ejecutarse documentalmente en paralelo, pero sus resultados no ingresan al acompañamiento antes del umbral válido del dominio.
6. **firewall:** una operación concurrente con una sola persona desempeñando ambos roles no puede declararse equivalente al protocolo ordinario de separación informacional.

---

## 20. Búsqueda transversal antes de edición

Antes de cerrar la segunda edición debe ejecutarse búsqueda textual sobre HISTOS y referencias cruzadas para localizar expresiones que:

- llamen «el mismo α/S/Δ» a objetos de ambos instrumentos;
- presenten la convergencia como validación independiente;
- deriven `S_P` desde `P(Hijos)`;
- usen bandas `α_H` como valores directamente transferibles a `α_P`;
- describan datos longitudinales post-intervención como evidencia del estado previo;
- presenten `M·3+` como prohibición de toda ejecución externa de Prometeo, en vez de condición de retroalimentación al acompañamiento;
- permitan al analista orientar al mediador hacia actos concretos del análisis;
- omitan consentimiento, finalidad o procedencia temporal en la transferencia.

Cada ocurrencia debe clasificarse como:

- reescritura necesaria;
- nota de tipado;
- aclaración histórica;
- sin cambio.

---

## 21. Qué no debe cambiar

La reparación no debe eliminar:

- la tesis de complementariedad entre perspectiva interna y externa;
- la utilidad de `P(Hijos)` para formular hipótesis;
- el uso cualitativo de indicadores durante HISTOS;
- la posibilidad de operación concurrente;
- el consentimiento revocable;
- la regla de no orientar HISTOS hacia el resultado que Prometeo pretende analizar;
- la posibilidad de que divergencias entre instrumentos sean informativas.

Debe cambiar únicamente la pretensión de identidad automática entre constructos, escalas y evidencias.

---

## 22. Estado de revisiones tras la reparación

### Cierre editorial preparado

- `review.histos.prometeo_independence`: arquitectura de independencia y firewall definida.
- `review.histos.delta_semantics`: separación `Δ_H/Δ_P` definida.
- `review.histos.system_coherence`: lenguaje de validación independiente corregible.
- `review.histos.alpha_scale`: equivalencia numérica rechazada; queda sólo calibración/validez local.
- `review.histos.s_qualitative`: inferencia directa a `S_P` rechazada; queda sólo validez/calibración local.

### Permanecen fuera de esta corrección

- `review.histos.change_attribution`;
- eficacia y seguridad;
- calibración empírica;
- fiabilidad y reproducibilidad;
- funciones de traducción cuantitativa futuras;
- cualquier revisión jurídica específica de confidencialidad que requiera estándares externos.

---

## 23. Resultado editorial esperado

Tras ejecutar `2E-HISTOS-PROM-001`, el lector debe poder reconstruir sin ambigüedad esta cadena:

`HISTOS`

`→ observación longitudinal y acompañamiento`

`→ α_H / S_H / Δ_H / P(Hijos) / arco / bloqueos`

`→ resumen consentido, fechado y tipado como segundo nivel`

`→ hipótesis y contexto`

`→ evidencia independiente`

`→ Prometeo: G_D → w → R* → S_P / α_P / Δ_P`

`→ resultado externo`

`→ retroalimentación sólo bajo consentimiento + umbral M·3+ del dominio + firewall`.

La edición no deberá permitir que el lector reduzca esa arquitectura a:

`HISTOS → α/S/Δ → Prometeo`.

---

## 24. Condición de cierre de esta nota

`2E-HISTOS-PROM-001` quedará ejecutada únicamente cuando:

- VI·2 haya sido reestructurado;
- las ocurrencias transversales hayan sido auditadas;
- la notación distinga los estimandos;
- la tabla de transferencia contenga las condiciones de procesabilidad;
- la procedencia temporal sea obligatoria;
- el firewall esté operacionalizado;
- las seis pruebas editoriales anteriores sean satisfechas;
- ninguna corrección presente calibración, fiabilidad o eficacia como validadas sin evidencia adicional.

Hasta entonces, esta nota permanece **PREPARADA PARA SEGUNDA EDICIÓN / EJECUCIÓN DIFERIDA**.