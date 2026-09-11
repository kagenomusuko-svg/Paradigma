# PROVENIENCIA-MANT-001 — Matriz de proveniencia para notas 2E de la sesión transversal

> **Documento de saneamiento de proveniencia.** No añade doctrina, no modifica fuentes canónicas y no convierte propuestas editoriales en decisiones autorales. Su única función es impedir que desarrollos operativos redactados durante la auditoría transversal de 2026-09-10 sean leídos como si hubieran sido adjudicados por el autor.

- **ID:** `PROVENIENCIA-MANT-001`
- **Estado:** VIGENTE COMO ACLARACIÓN DE PROVENIENCIA
- **Fecha de saneamiento:** 2026-09-10
- **Alcance:** notas 2E y precisiones producidas durante la sesión HISTOS→Prometeo / E0–E8 / IIC / REC
- **No altera:** `corpus/`, mapa maestro, resoluciones previas ajenas a esta sesión ni adjudicaciones autorales ya registradas

## 1. Regla de lectura

Las notas de segunda edición mezclan necesariamente dos capas:

1. **núcleo adjudicado o hallazgo demostrado**, que puede gobernar la corrección de una formulación;
2. **diseño editorial/operativo derivado**, que propone cómo ejecutar esa corrección.

La segunda capa no adquiere autoridad autoral por estar escrita con verbos como «deberá», «obligatorio», «regla» o «prueba». Cuando no exista una adjudicación autoral identificable, esas expresiones se leen como:

> **propuesta editorial pendiente de adopción durante la ejecución de segunda edición.**

Este documento no degrada los hallazgos matemáticos o textuales demostrados; sólo corrige su proveniencia.

## 2. HISTOS → Prometeo

### 2.1 Núcleo respaldado

En `RES-HISTOS-PROM-001`, `RES-HISTOS-PROM-001-P1`, `2E-HISTOS-PROM-001` y `2E-HISTOS-PROM-001-P1` se conserva como adjudicado:

- referente compartido ≠ estimando compartido ≠ evidencia compartida;
- `α_H` no es automáticamente `α_P`;
- `S_H`/`P(Hijos)` no determinan `S_P`;
- `Δ_H` no sustituye `Δ_P = R* − α_P`;
- HISTOS no produce `D`, aristas causales, `w`, `Q_D`, `b_D` ni `R*`;
- una observación post-intervención no se retroproyecta automáticamente a `t0`;
- ejecutar Prometeo, transferir información HISTOS→Prometeo y retroalimentar resultados Prometeo→HISTOS son operaciones distintas;
- `M·3+` se vincula a la retroalimentación al acompañamiento en el dominio pertinente, no a una prohibición absoluta de ejecutar externamente un análisis documental independiente.

### 2.2 Desarrollo editorial derivado, no adjudicación autoral automática

Permanecen como propuestas de implementación hasta adopción expresa:

- estructura exacta de tablas nuevas;
- campos mínimos de un resumen HISTOS→Prometeo;
- formato de logs o registros de transferencia;
- segregación concreta de funciones y régimen de doble rol;
- listas exhaustivas de información que debe ocultarse o compartirse;
- diseño detallado del firewall;
- baterías de «pruebas editoriales obligatorias»;
- notación definitiva `α_H/α_P`, `S_H/S_P`, `Δ_H/Δ_P` si una edición posterior decide otra convención equivalente.

El firewall como problema y necesidad de separación informacional está respaldado por la adjudicación; **su implementación concreta no estaba adjudicada en todos sus detalles**.

## 3. E0–E8 / `w`

### 3.1 Núcleo respaldado

En `RES-EVID-001` y `2E-EVID-001` se conserva como adjudicado:

- fuerza epistémica y magnitud causal son dimensiones distintas;
- E1–E8 no fijan por sí solas la posición de `w`;
- la clase E informa la incertidumbre/precisión defendible de la estimación;
- E0 significa evidencia positiva de ausencia causal, no ausencia de evidencia;
- deben distinguirse arista nula documentada, arista hipotética/no acreditada y arista acreditada;
- las bandas históricas E→`w` no pueden conservarse sin más como definición intrínseca de magnitud causal;
- cualquier nueva calibración numérica requiere trabajo metrológico/empírico propio.

### 3.2 Desarrollo editorial/metrológico derivado

Permanecen como propuestas o trabajo pendiente:

- forma matemática definitiva de `U(ŵ)`;
- hojas de calibración y campos obligatorios;
- diseño de grafos auxiliares para hipótesis;
- reglas concretas de combinación o prioridad entre fuentes;
- adaptación detallada de Declaraciones A/B/C/D;
- baterías de pruebas editoriales;
- formatos específicos de análisis de sensibilidad;
- cualquier coeficiente, radio, distribución o perfil numérico de incertidumbre.

## 4. IIC

### 4.1 Núcleo respaldado

En `RES-IIC-001` y `2E-IIC-001` se conserva como adjudicado:

- el objeto doctrinal es la congruencia/brecha entre campo declarado y campo producido respecto de `D`;
- IIC canónico se trabaja como índice no direccional en `[0,1]`;
- `IIC=0` significa congruencia nula/brecha total dentro del índice, no «campo opuesto»;
- correlación estadística real y divergencia direccional son objetos distintos;
- una estimación cualitativa no debe llamarse correlación si no existe un estimador estadístico real;
- media uniforme, `k`, forma multiplicativa y umbral de fraude annona siguen siendo decisiones de modelo/calibración revisables;
- la doble aparición de IIC puede corresponder a funciones distintas, sin que ello demuestre que la segunda modulación sea necesaria o esté validada.

### 4.2 Desarrollo editorial/metrológico derivado

No queda adjudicado como fórmula canónica:

`IIC = Σ λ_k g_k`.

Esa expresión sólo ilustra una familia posible de ponderaciones por materialidad. También permanecen como propuestas:

- símbolo definitivo para divergencia direccional;
- regla de ponderación por protocolo;
- transformación entre correlación y congruencia;
- baterías de pruebas editoriales;
- protocolo concreto de recalibración de fraude annona.

## 5. REC

### 5.1 Núcleo respaldado y/o formalmente demostrado

En `RES-REC-001` y `2E-REC-001` se conserva:

- `n(ΔI·Δh) ≥ 4τ₀²` no se sigue de la cadena publicada;
- el factor `4` surge de un Paso 2 formalmente inválido;
- bajo la parametrización realmente demostrada, la cota conservable es `ΔI·Δh ≥ τ₀/n`;
- la demostración corresponde a una logística Bernoulli one-vs-rest, no a un softmax multinomial general;
- `τ_eff` no transforma algebraicamente la cota lineal en la cuadrática;
- el caso binario hace imposible `max_k h_k < 1/2`;
- `η(τ)` permanece heurística/orientativa.

Estos puntos no dependen de la taxonomía transversal retirada; son correcciones formales independientes.

### 5.2 Desarrollo editorial derivado

Permanecen como propuestas de edición:

- ubicación gráfica de `η(τ)`;
- formato exacto de la comparación con Heisenberg;
- batería enumerada de pruebas editoriales;
- decisión final sobre conservar la cota como teorema condicionado, resultado auxiliar o modelo ilustrativo;
- cualquier nueva derivación multinomial o fórmula sustitutiva.

## 6. Referencia obsoleta a `RES-S-001`

`RES-S-001` fue creado de manera redundante y retirado en `318ae81cd414915d0796f91bf848c2fecb8cd945`.

Por tanto, cualquier referencia residual a `RES-S-001` dentro de documentos de esta sesión se considera **referencia histórica obsoleta**, no una autoridad vigente.

La proveniencia correcta para `S` es:

`AUD-S-001 + 2E-S-001 + adjudicación autoral registrada en 1a532f07e31eb8e65662088e159a6a7ea999c100`.

No debe recrearse `RES-S-001` para reparar esas referencias.

## 7. Taxonomías retiradas

No forman parte del vocabulario vigente del proyecto:

- `SD` — sustitución directa;
- `RO` — redemostración obligatoria;
- `RC` — recálculo;
- `IR` — interfaz a retipar;
- esquema `Eje A / Eje B` de `2E-RSTAR-INVENTARIO-001`.

`2E-RSTAR-INVENTARIO-001` fue eliminado en `b8cb5b08fc117d4404725d30ff856025873d9f07`.

Las categorías descriptivas utilizadas en `AUD-MANT-TRANS-001` tampoco se atribuyen al autor como taxonomía propia.

## 8. Efecto práctico

Después de este saneamiento:

- las adjudicaciones sustantivas de la sesión se conservan;
- los errores matemáticos demostrados siguen corregidos;
- las propuestas útiles no se borran, pero dejan de aparentar autoridad autoral;
- una futura edición puede adoptar, modificar o descartar los desarrollos operativos derivados;
- ninguna nota 2E de esta sesión puede citarse por sí sola como prueba de que el autor aprobó todos sus detalles de implementación.

La ejecución editorial deberá volver siempre a la resolución específica, a su proveniencia y, cuando corresponda, a la fuente canónica.
