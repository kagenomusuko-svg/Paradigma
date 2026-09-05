# 2E-RSC-IT-001 — Reparación formal de RSC, I(t) e irreversibilidad

> **Entrada editorial derivada para segunda edición.** Implementa la distinción conceptual de `RES-RSC-IT-001` sin fijar todavía la representación matemática definitiva.

- **Estado:** PREPARADO PARA NORMALIZACIÓN FORMAL DE SEGUNDA EDICIÓN
- **Prioridad:** ALTA
- **Resolución de referencia:** `RES-RSC-IT-001`
- **Auditoría de referencia:** `AUD-RSC-IT-001`
- **Revisiones principales:** `review.axiom.rsc_type`, `review.axiom.irreversibility`, `review.axiom.phi2_integration`
- **Obra principal afectada:** *Axiomatización del sistema de la doble mediación*

## 1. Distinción que debe regir toda la corrección

La segunda edición deberá separar de manera explícita:

`RSC = registro histórico de eventos/colapsos producidos`

de:

`I(t) = estado agregado o proyección derivada de la historia integrada hasta t`.

La irreversibilidad factual del acto pertenece primariamente al historial: un evento ocurrido no deja de haber ocurrido aunque una representación agregada pueda compensar sus efectos o retornar a un valor anterior.

## 2. Qué debe corregirse en la definición de RSC

La definición histórica:

`RSC(t)={c(τ):τ∈[0,t]}`

no es suficiente para funcionar como registro porque la imagen de una función:

- elimina multiplicidades;
- no conserva por sí misma la identidad de cada ocurrencia;
- no conserva el orden temporal como estructura;
- no adjunta aceptación/rechazo;
- no adjunta profundidad, alcance o peso de integración.

La segunda edición deberá reemplazarla por una estructura indexada por evento o temporalmente marcada.

Son candidatas conceptuales posibles:

- secuencia de eventos;
- multiconjunto indexado;
- medida de eventos;
- medida marcada;
- ledger/registro inmutable con atributos.

Esta entrada no adjudica cuál será la estructura matemática definitiva.

## 3. Datos mínimos por evento

La representación elegida deberá poder conservar, cuando el dominio lo requiera:

- identificador del evento;
- tiempo/orden;
- colapso o acto producido;
- actor/nodo relevante;
- marca de integración/aceptación/rechazo;
- profundidad/alcance de integración si se conserva ese aparato;
- peso temporal o evidencia asociada;
- dominio o clase de evento cuando sea necesario.

## 4. Qué debe corregirse en I(t)

`I(t)` debe definirse como una operación sobre el historial relevante, no como el historial mismo.

La segunda edición deberá especificar una ruta equivalente a:

`RSC(t) → selección/marca de eventos integrados → operador de agregación → I(t)`.

Debe quedar explícito:

- qué eventos entran;
- bajo qué regla;
- qué información retiene I(t);
- qué información descarta;
- qué tipo matemático tiene;
- qué propiedades son demostrables.

## 5. Teorema de irreversibilidad

El Teorema 2.1 histórico no puede mantenerse con la demostración actual.

No es válido inferir:

`g≠0` en un conjunto de medida positiva `⇒ ||∫g||>0`.

Una futura formulación debe distinguir dos propiedades:

### Irreversibilidad histórica

El historial de eventos crece en el sentido de que un evento ocurrido permanece registrado.

### Evolución del estado agregado

`I(t)` puede cambiar, permanecer constante o incluso retornar a un valor anterior según su operador de agregación.

No debe llamarse a esta segunda propiedad irreversibilidad salvo que se añadan hipótesis matemáticas específicas que realmente la garanticen.

## 6. φ₂

La segunda edición debe reformular φ₂ para distinguir entre:

1. producción del evento;
2. decisión de integración;
3. marca de integración/rechazo;
4. actualización del estado agregado.

La notación deberá impedir expresiones mal tipadas como:

- `RSC(t) \ I(t)`;
- `c(τ) ∈ I(t)`;
- `A_D ∩ I(t)`.

Si se necesita hablar del conjunto/registro de integrados, debe existir un objeto de ese tipo, por ejemplo una subcolección marcada del historial, y no usarse el vector `I(t)` como si fuera un conjunto.

## 7. Caso continuo y caso discreto

La segunda edición deberá revisar la relación entre:

- función de peso continua `w:T→R_+` medible/acotada;
- sumas discretas de eventos;
- deltas de Dirac.

La delta de Dirac no es una función ordinaria medible y acotada del tipo declarado históricamente.

Hay dos rutas posibles de reparación:

1. separar formalmente caso continuo y caso discreto;
2. formular ambos mediante integración respecto de una medida adecuada.

La elección queda para la normalización matemática.

## 8. α

La corrección de RSC/I(t) debe actualizar únicamente la representación formal que α utiliza para identificar eventos integrados.

No modifica:

- `RES-ALPHA-001`;
- la independencia de α respecto del dolo;
- la posibilidad de asunción voluntaria, forzada o impuesta;
- la definición aplicada vigente de asunción efectiva.

La segunda edición deberá sustituir los indicadores basados en pertenencia a `I(t)` por marcas/funciones definidas sobre eventos identificables.

## 9. Pruebas mínimas obligatorias

La nueva formalización deberá superar al menos estos casos:

### Caso A — eventos opuestos

Dos eventos producen aportes agregados opuestos y `I(t₂)=I(t₀)`.

Resultado esperado:

- ambos eventos siguen en RSC;
- la irreversibilidad histórica se conserva;
- no se concluye que no ocurrió nada.

### Caso B — eventos repetidos

Dos eventos con el mismo valor ocurren en tiempos distintos.

Resultado esperado:

- RSC conserva dos ocurrencias;
- la multiplicidad no se pierde.

### Caso C — evento rechazado

Un evento ocurre pero no se integra.

Resultado esperado:

- aparece en RSC;
- su marca de integración es negativa;
- no se confunde con ausencia del evento.

### Caso D — recontextualización

Un evento posterior modifica el estado agregado respecto de un evento anterior.

Resultado esperado:

- I(t) cambia según el operador;
- ninguno de los eventos desaparece del historial.

## 10. Criterio de cierre

La entrada podrá considerarse incorporada cuando un lector pueda distinguir formalmente, sin ambigüedad de tipos:

`qué ocurrió` → RSC,

`qué fue integrado y cómo` → marcas/operador,

`qué estado agregado resulta` → I(t),

sin usar la repetición o cancelación de I(t) como negación retrospectiva de los actos ocurridos.
