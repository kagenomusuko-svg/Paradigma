# 2E-SDO-PROM-001 — Corrección editorial de la interfaz SDO → Prometeo

> **Producto editorial derivado para segunda edición.** Ejecuta `RES-SDO-PROM-001` cuando se prepare una nueva edición. No modifica las fuentes canónicas de primera edición.

- **ID:** `2E-SDO-PROM-001`
- **Estado:** **PREPARADO PARA SEGUNDA EDICIÓN / EJECUCIÓN DIFERIDA**
- **Prioridad:** alta
- **Resolución rectora:** `RES-SDO-PROM-001`
- **Resoluciones relacionadas:** `RES-RSTAR-001`, `RES-ALPHA-001`, `RES-DELTA-001`, `RES-PHI2-OBS-001`, `RES-RSC-IT-001`
- **Ámbito principal:** SDO VI·3, VII·1–VII·4, VIII·1; Taxonomía U·3; referencias cruzadas a Prometeo.

---

## 1. Cambio estructural de redacción

La segunda edición no debe decir sin calificación:

> «SDO produce el grafo causal que Prometeo calcula».

Debe distinguir:

`observaciones → localización SDO → grafo/configuración candidata → pregunta causal D → evidencia → grafo causal G_D → w → R*`.

La localización orienta **qué investigar** y **qué pregunta hacer**. La reconstrucción causal determina qué entra realmente al cálculo.

---

## 2. Introducir dos objetos distintos

### `G_SDO`

Grafo de configuración o hipótesis:

- códigos;
- Otros relevantes;
- eventos narrados;
- roles/máscaras/campos;
- relaciones cualitativas propuestas;
- certeza de la inferencia.

### `G_D`

Grafo causal relativo a un resultado `D`:

- ancestros causales pertinentes;
- mecanismos documentados;
- aristas primitivas;
- pesos locales `w`;
- resultado explícito.

No presentar ambos como el mismo objeto.

---

## 3. Corregir la ficha extendida

La sección «Parámetros por nodo/arista: R*, α, Δ» debe ser reconstruida.

Bajo `RES-RSTAR-001`:

- **arista:** `w_ij`;
- **nodo respecto de D:** `R*_i(D)`.

Si se desea medir una contribución de arista o de ruta, debe definirse otro objeto con nombre, símbolo y fórmula propios.

La ficha deberá añadir un campo obligatorio:

**Resultado D respecto del cual se calcula R***.

Sin `D`, no ejecutar el módulo R*.

---

## 4. Corregir las traducciones automáticas desde códigos

Redacciones del tipo:

- «E-4 produce arista de alta R* desde el Otro»;
- «V-2 produce determinada asimetría de pesos»;
- «M-3 tiene R* sobre todos los nodos»;

se deben reformular como **hipótesis de investigación causal**.

Ejemplo editorial:

> «Una localización E-4 hace pertinente investigar qué Otro(s) y qué mecanismos contribuyen a la persistencia de la configuración. El peso causal no se deriva del código: se reconstruye respecto del resultado definido y de la evidencia disponible.»

---

## 5. Series 1, 2 y 3

Las «tres series de Prometeo» de SDO deben identificarse editorialmente como **series de la interfaz SDO-Prometeo**.

### Serie 1

Antes de calcular debe definir un `D` operacional para el estado estudiado, por ejemplo persistencia de una configuración o bloqueo observable.

### Serie 2

Debe distinguir distribución composicional de estados/Hijos de atribución causal `R*`.

### Serie 3

Puede conservarse como la serie más directamente alineada con el Prometeo causal, siempre que use el aparato R* vigente.

---

## 6. Separar nodo, estado, evento y resultado

Toda tabla de grafo deberá tipar cada entrada como una de estas clases:

- actor/agente;
- factor estructural o instrumental;
- evento;
- estado/variable mediadora;
- resultado `D`.

No poner en una misma columna como objetos homogéneos a una persona, `φ₂`, una máscara, un evento y un código SDO sin declarar qué función causal representa cada uno.

---

## 7. R* no debe usarse como efecto de intervención

Eliminar o calificar formulaciones como:

> «el factor con mayor R* es el que, si cambia, produce mayor efecto».

La segunda edición debe decir:

> `R*` distribuye atribución causal respecto de `D`. La selección de un punto de intervención requiere además un modelo de modificabilidad/respuesta a intervención.

No derivar de `R*` por sí solo:

- punto de entrada óptimo;
- magnitud futura de cambio;
- rapidez del proceso;
- número esperado de sesiones.

---

## 8. `R* × α`

Si se conserva el producto usado como «potencial de movimiento», debe presentarse como:

- heurística propuesta;
- objeto distinto de R*;
- pendiente de validación intervencional.

No atribuirlo al aparato canónico de Prometeo como resultado ya demostrado.

El nombre y símbolo definitivos pueden fijarse en la revisión editorial, pero no debe conservarse una notación que sugiera una propiedad derivada de R* sin demostración.

---

## 9. α de integración SDO

La segunda edición debe distinguir:

- α interno/instrumental de integración;
- α aplicado de `RES-ALPHA-001`.

No usar una sola columna `α` para ambos.

Cuando SDO hable de «capacidad de integración», la notación deberá hacer visible que es un proxy/estimador local y no asunción efectiva aplicada.

---

## 10. α_T

`α_T = ΔI(t)_genuina_asumida / exposición_a_la_pérdida`

puede conservarse únicamente con estatus explícito:

**índice propuesto / operacionalización pendiente**.

Antes de convertirlo en magnitud aplicada deberán definirse:

- numerador observable;
- denominador observable;
- unidades o escala;
- estimador;
- tratamiento de incertidumbre;
- calibración;
- dependencia respecto de la reconstrucción de `I(t)`.

Los valores `0.05`, `0.38` y similares deben presentarse como ilustrativos si no provienen de una medición reproducible.

---

## 11. Renotar Δ temporal/prospectiva

La segunda edición no debe usar el mismo `Δ` para:

- `R*−α`;
- cambio de localización;
- cambio temporal de nodo;
- cambio proyectado tras intervención.

`Δ` queda reservado por `RES-DELTA-001` para:

`Δ=R*−α`.

Los cambios temporales/prospectivos deben recibir una notación diferenciada.

No seleccionar por reemplazo ciego: revisar cada ocurrencia de SDO VII·1 y VII·4.

---

## 12. Pesos de Hijos

El vector normalizado de Hijos debe llamarse distribución composicional estimada, no peso causal.

Debe distinguirse:

`H = distribución estimada de Hijos`

frente a:

`w_ij = peso causal local`

y:

`R*_i(D) = atribución causal estable`.

La segunda edición debe declarar pendiente la calibración del algoritmo que convierte señales/intensidades/factores contextuales en scores numéricos.

---

## 13. Taxonomía U·3 — feedback

Reformular «el output de Prometeo prueba la coherencia de los inputs» como:

> «el output puede funcionar como control interno de consistencia y sensibilidad; no valida causalmente los inputs si se contrasta con la misma evidencia utilizada para construirlos.»

El protocolo debe permitir tres salidas distintas:

1. error de entrada verificable → corregir;
2. evidencia adicional independiente → actualizar;
3. incompatibilidad persistente → declarar incertidumbre/no identificabilidad.

No permitir:

`output no esperado → ajustar inputs hasta obtener output esperado`.

---

## 14. Retirar la presunción diseñador > ejecutor

Taxonomía U·3 usa como alarma que el ejecutor supere al diseñador.

Bajo `RES-RSTAR-001` esa presunción no es universal.

La segunda edición debe sustituirla por controles que no preseleccionen al ganador del cálculo, por ejemplo:

- trazabilidad de cada arista;
- ausencia de doble conteo;
- sensibilidad a rangos;
- consistencia de orientación;
- cumplimiento del dominio `ρ(Q_D)<1`;
- explicación documental de mecanismos.

---

## 15. Pronóstico y trayectoria

Las afirmaciones de:

- `x–y` sesiones;
- velocidad de amortiguación;
- trayectoria esperada;
- «mayor potencial de movimiento»;
- Δ proyectada de una intervención;

no deben presentarse como outputs disponibles del cálculo R* vigente.

Pueden conservarse como programa de desarrollo si se añade un módulo temporal/intervencional explícito y se valida posteriormente.

---

## 16. Búsqueda transversal obligatoria

Antes de cerrar la segunda edición buscar:

- `grafo de entrada`;
- `grafo causal`;
- `R* de la arista`;
- `R* sobre φ₂`;
- `R* sobre V-3`;
- `R*_α` / `R* α`;
- `potencial de movimiento`;
- `punto de entrada óptimo`;
- `sesiones` asociadas a R*/α;
- `Δ proyectada`;
- `magnitud del cambio`;
- `α_T`;
- `pesos de Hijos`;
- `Prometeo calcula`;
- `Serie 1`, `Serie 2`, `Serie 3`;
- `output inconsistente`;
- `revisar inputs`;
- `nodo de diseño` / `nodo de ejecución`.

Cada ocurrencia debe clasificarse como:

1. observación;
2. inferencia SDO;
3. hipótesis causal;
4. arista documentada;
5. calibración;
6. cálculo R*;
7. heurística intervencional;
8. afirmación empírica/pronóstica.

---

## 17. Pruebas obligatorias de consistencia

### Caso A — E-4 sin evidencia del mecanismo

Localización: `E-4` con un Otro identificado.

Resultado esperado:

- SDO puede proponer al Otro como candidato;
- no asignar `w` ni `R*` hasta documentar mecanismo respecto de `D`.

### Caso B — arista y nodo

Existe `A→B` con `w_AB=0.8`.

Resultado esperado:

- no escribir `R*(A→B)=0.8`;
- calcular `R*_A(D)` sólo tras reconstruir rutas completas hacia `D`.

### Caso C — nodo traumático

SDO identifica evento fundante.

Resultado esperado:

- evento puede entrar como candidato causal;
- «bloqueo de φ₂» debe tiparse como resultado/estado;
- R* requiere mecanismo y evidencia, no el código traumático por sí solo.

### Caso D — máximo R* e intervención

Un nodo tiene `R*=0.60` pero es inmodificable; otro tiene `R*=0.20` y es altamente modificable.

Resultado esperado:

- R* no decide por sí solo el punto de intervención.

### Caso E — feedback

El resultado contradice la intuición del analista pero no existe nueva evidencia.

Resultado esperado:

- no recalibrar hasta obtener la intuición;
- revisar errores objetivos o declarar incertidumbre.

### Caso F — α/Δ

SDO registra capacidad de integración y cambio de localización.

Resultado esperado:

- no introducirlos en columnas de α aplicado o `Δ=R*−α` sin crosswalk explícito.

---

## 18. Pendientes que esta nota no resuelve

- calibración E0–E8 y `w`;
- calibración de pesos de Hijos;
- fiabilidad interobservador de SDO;
- validez de α_T;
- validez de escalas de integración;
- modelo de intervención;
- pronóstico temporal;
- número de sesiones;
- validez clínica o predictiva;
- portabilidad entre dominios;
- nueva notación final de los objetos locales de cambio/intervención.

Estas cuestiones permanecen abiertas; la corrección editorial evita presentarlas como ya resueltas.
