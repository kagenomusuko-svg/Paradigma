# AUD-MANT-TRANS-001 — Inventario transversal de estado MANT

> **Documento derivado de verificación, sin autoridad doctrinal ni adjudicatoria autónoma.** Su función es resumir el estado de resoluciones, auditorías y entradas de segunda edición ya existentes. No modifica `corpus/fuentes/`, no sustituye una adjudicación autoral, no convierte una inferencia editorial en doctrina y no habilita ni cierra por sí mismo ninguna fase del proyecto.

- **ID:** `AUD-MANT-TRANS-001`
- **Estado:** **INVENTARIO TRANSVERSAL DERIVADO / PROVENIENCIA DEPURADA**
- **Fecha original:** 2026-09-10
- **Fase:** MANT — mantenimiento posterior a mapa maestro v1
- **Alcance:** resoluciones MANT, auditorías derivadas y registro de segunda edición existentes en `documentacion/`
- **Autoridad:** `INSTRUCCIONES.md` y las fuentes/decisiones específicas a las que remite cada entrada

## 1. Regla de proveniencia

Este documento no puede crear una decisión por agregación.

Para cada familia debe distinguirse entre:

1. **adjudicación autoral registrada:** existe una decisión expresa del autor incorporada al historial del repositorio;
2. **hallazgo formal o textual:** se verifica una inconsistencia, dependencia, error o relación mediante lectura del corpus o demostración;
3. **inferencia transversal:** organización analítica derivada de varias fuentes o resoluciones;
4. **propuesta editorial:** forma posible de incorporar una adjudicación en segunda edición.

Las etiquetas anteriores son únicamente una convención de proveniencia para este inventario. **No constituyen una taxonomía doctrinal del Paradigma ni se atribuyen al autor como clasificación propia.**

Del mismo modo, las expresiones históricas «deuda formal/metrológica», «deuda empírica/calibración» y «deuda editorial/interfaz» pueden seguir utilizándose descriptivamente cuando resulten útiles, pero no se consideran categorías autorales ni estados normativos del proyecto.

## 2. Corrección de la atribución transversal

La versión anterior de este documento afirmó que el autor había confirmado expresamente:

- una clasificación global en cuatro estados;
- dos carriles generales de dependencia;
- el cierre del checkpoint MANT como consecuencia de esa clasificación;
- un inventario transversal de `R*` con categorías propias como prerrequisito del proyecto.

Esa atribución fue demasiado amplia.

El contraste autoral disponible sí respalda adjudicaciones sustantivas concretas —entre ellas HISTOS→Prometeo, E0–E8/`w`, IIC y REC—, pero **no convierte automáticamente el andamiaje organizativo usado por esta auditoría en una decisión del autor**.

Por tanto:

> **este documento registra estado; no adjudica por sustitución, no habla en nombre del autor y no transforma una herramienta de análisis en vocabulario del proyecto.**

## 3. Matriz de estado con proveniencia

| Familia | Fuente vigente | Qué puede darse por fijado | Qué permanece abierto | Proveniencia principal |
| --- | --- | --- | --- | --- |
| Aego / afasia volitiva | `RES-AEGO-001` | relación doctrinal ya adjudicada | incorporación/crosswalk 2E | resolución específica previa |
| `R*` / operador causal | `RES-RSTAR-001` | operador vigente y separación respecto de formulaciones históricas | estimación de `w`, equivalencia contrafáctica, feedback, recálculos | resolución específica previa |
| α / asunción | `RES-ALPHA-001` | separación de capas y estatus conceptual | observabilidad, calibración, escalas por dominio | resolución específica previa |
| Δ | `RES-DELTA-001` | `Δ = R* − α` y semántica de signo | conmensurabilidad, agregados, recálculos | resolución específica previa |
| `Δ_B` | `RES-DELTAB-001` | objeto/tipo/fórmula adjudicados | `G_B`, `R*_B`, beneficio total, doble conteo | resolución específica previa |
| φ₂ / observabilidad | `RES-PHI2-OBS-001` | separación entre operación interna, atribución exterior y proxy | fiabilidad e identificabilidad | resolución específica previa |
| `RSC` / `I(t)` | `RES-RSC-IT-001` | distinción conceptual | representación matemática y operador de integración | resolución específica previa |
| `S` | `AUD-S-001` + `2E-S-001` (`1a532f07`) | constructo de sustituibilidad conservado | contrafactual exacto, estimador, proxies, calibración | adjudicación autoral previa; no requiere `RES-S-001` |
| SDO → Prometeo | `RES-SDO-PROM-001` | separación entre localización SDO y reconstrucción causal Prometeo | calibración y validación instrumental | resolución específica previa |
| HISTOS → Prometeo | `RES-HISTOS-PROM-001` + precisión | referente compartido no implica identidad de estimando/evidencia; HISTOS no produce `R*`; separación temporal y de handoff | calibración, fiabilidad, change attribution y detalles operativos no adjudicados | núcleo con adjudicación autoral; desarrollos operativos pueden ser propuesta editorial |
| E0–E8 / `w` | `RES-EVID-001` | E informa fuerza epistémica/incertidumbre y no fija por sí sola la posición de `w`; E0 = nulidad causal documentada | estimador `ŵ`, forma de `U(ŵ)`, calibración y combinación | núcleo con adjudicación autoral |
| IIC | `RES-IIC-001` | IIC canónico como congruencia `[0,1]`; correlación y divergencia direccional separadas | estimador, ponderación, `k`, ajuste de `W`, fraude annona | núcleo con adjudicación autoral; arquitecturas de ponderación son propuestas salvo adopción posterior |
| REC | `RES-REC-001` | error del factor 4; cota condicionada `ΔI·Δh ≥ τ₀/n`; alcance logístico-Bernoulli | multinomial, Fisher matricial, `τ`, predictibilidad y eventual nueva derivación | hallazgo formal + adjudicación autoral de corrección |

La existencia de una entrada `2E-...` no prueba por sí sola que una cuestión esté doctrinal, matemática o empíricamente resuelta.

## 4. Corrección específica de `S`

`S` ya estaba adjudicada antes de esta verificación:

- `AUD-S-001` estableció que el constructo de sustituibilidad no presentaba una contradicción doctrinal nuclear;
- `2E-S-001` y el commit `1a532f07e31eb8e65662088e159a6a7ea999c100` registraron la decisión autoral de conservar el constructo y reconstruir su estimador/operacionalización.

La creación posterior de `RES-S-001` fue redundante y fue retirada en `318ae81cd414915d0796f91bf848c2fecb8cd945`.

La autoridad vigente es, por tanto:

`AUD-S-001 + 2E-S-001 / adjudicación autoral`

no un archivo adicional de resolución.

## 5. Dependencias técnicas observadas

Existen dependencias reales entre trabajos pendientes. Registrarlas no implica convertirlas en una taxonomía autoral ni en un plan único obligatorio.

Entre las más claras:

- los recálculos de `R*` dependen de una estimación operativa defendible de `w` y su incertidumbre;
- una reconstrucción formal de `S` que use `R*` debe respetar el operador vigente;
- cualquier interpretación cuantitativa de `Δ = R* − α` requiere atender la conmensurabilidad de las escalas;
- la formalización de `I(t)` condiciona cualquier desarrollo matemático que pretenda usarla como entrada de α;
- los ejemplos y tablas dependientes de fórmulas corregidas no deben conservar resultados numéricos por mera sustitución textual.

Estas dependencias deben verificarse **caso por caso mediante el mapa maestro y la lectura de las fuentes**, conforme a `INSTRUCCIONES.md`. Este documento no establece «dos carriles» como vocabulario obligatorio del proyecto.

## 6. Estado de las adjudicaciones surgidas durante la sesión

### 6.1 HISTOS → Prometeo

Se conserva el núcleo adjudicado:

- identidad de referente ≠ identidad de estimando ≠ identidad de evidencia;
- `α_H` no es automáticamente `α_P`;
- `S_H`/`P(Hijos)` no determinan `S_P`;
- `Δ_H` no sustituye `Δ_P = R* − α_P`;
- HISTOS no produce `D`, aristas, `w`, `Q_D`, `b_D` ni `R*`;
- los datos post-intervención no se retroproyectan automáticamente a `t0`;
- ejecutar Prometeo, transferir información HISTOS→Prometeo y retroalimentar resultados Prometeo→HISTOS son operaciones distintas.

Los protocolos concretos de firewall, plantillas, campos obligatorios, segregación de roles o formatos de transferencia son **desarrollo editorial/operativo derivado** salvo que exista adopción autoral específica posterior.

### 6.2 E0–E8 / `w`

Se conserva el núcleo adjudicado:

- magnitud causal y fuerza epistémica son dimensiones distintas;
- la clase E informa incertidumbre/precisión defendible, no la posición automática de `w`;
- E0 significa evidencia positiva de ausencia causal, no ausencia de evidencia;
- deben distinguirse arista nula documentada, hipótesis no acreditada y arista acreditada.

Las hojas de calibración, formatos de trabajo, baterías de pruebas y futuras representaciones matemáticas de `U(ŵ)` son **propuestas o trabajo metrológico pendiente**, no doctrina ya fijada.

### 6.3 IIC

Se conserva el núcleo adjudicado:

- IIC como índice de congruencia no direccional en `[0,1]`;
- correlación estadística real y divergencia direccional son objetos distintos;
- `IIC = 0` significa congruencia nula dentro del índice, no oposición direccional;
- media uniforme, `k`, forma multiplicativa y umbral de fraude annona siguen siendo decisiones de modelo/calibración revisables.

Formas generales de ponderación, símbolos nuevos y protocolos concretos de agregación son **propuestas metrológicas/editoriales**, no fórmulas canónicas adjudicadas.

### 6.4 REC

Se conserva la corrección formal adjudicada:

- el factor `4` no se sigue de la cadena publicada;
- la consecuencia demostrada bajo el modelo efectivamente usado es `ΔI·Δh ≥ τ₀/n`;
- el Lema 7.1 debe restringirse a la parametrización que realmente demuestra;
- `τ_eff` no rescata algebraicamente la forma cuadrática;
- predictibilidad y `η(τ)` no adquieren estatus de teorema por proximidad editorial.

Las decisiones de maquetación, baterías de pruebas editoriales y una eventual nueva derivación pertenecen a segunda edición y no son doctrina ya fijada.

## 7. Sobre la campaña de segunda edición

`AUD-MANT-TRANS-001` **no es la autoridad que abre, cierra o habilita la campaña 2E**.

La segunda edición puede continuar cuando el estado vigente del repositorio, las entradas `2E-*`, las resoluciones específicas y las decisiones autorales aplicables así lo permitan. Esta auditoría sólo ayuda a no confundir:

- una adjudicación con una propuesta;
- un error demostrado con una preferencia editorial;
- una deuda de calibración con una contradicción doctrinal;
- una herramienta de organización con vocabulario del Paradigma.

La regla `PREPARADO ≠ INCORPORADO`, cuando aparezca en las entradas de segunda edición, describe el estado editorial de esas entradas; no se usa aquí como prueba de ratificación autoral de este documento.

## 8. Contaminación ya retirada

Queda registrado para evitar recurrencia:

- `RES-S-001` fue retirado por redundar una adjudicación autoral previa;
- `2E-RSTAR-INVENTARIO-001` fue retirado en `b8cb5b08fc117d4404725d30ff856025873d9f07`;
- no se mantienen `SD/RO/RC/IR` ni el esquema `Eje A/Eje B` como vocabulario del proyecto;
- la localización de dependencias de `R*` debe volver al mapa maestro, a las entradas 2E ya existentes y a la lectura de las fuentes.

## 9. Regla para futuras auditorías MANT

Ningún documento derivado debe atribuir al autor una clasificación, arquitectura, cierre o prioridad global salvo que exista una adjudicación autoral identificable.

Cuando no exista, debe rotularse como una de estas cosas:

- hallazgo textual/formal;
- inferencia analítica;
- propuesta editorial;
- cuestión abierta.

Una propuesta puede ser útil y conservarse. Lo que no puede hacer es adquirir autoridad por haber sido escrita en `documentacion/`.

## 10. Siguiente operativo

Se conserva el estado operativo fijado tras retirar el inventario paralelo:

> **MANT — reanudar la campaña 2E desde el mapa maestro, `2E-RSTAR-001` y `2E-RSTAR-RECALCULO-001`; no crear inventarios paralelos ni nuevas taxonomías de tratamiento sin necesidad demostrada y, cuando sean meramente editoriales, marcarlas como tales.**
