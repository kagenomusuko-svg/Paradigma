# AUD-EVID-001 — Auditoría MANT de la escala de evidencia E0–E8

> **Documento derivado de auditoría.** No modifica fuentes canónicas ni adjudica todavía una tabla numérica canónica para segunda edición.

- **ID:** `AUD-EVID-001`
- **Estado:** TENSIÓN METODOLÓGICA Y DE CALIBRACIÓN CONFIRMADA
- **Familia:** `E0–E8`, rangos `w`, jerarquía de evidencia, ausencia de evidencia / evidencia de ausencia
- **Obras contrastadas:** *Método Prometeo* (Cap. 2 y Apéndice A), *Taxonomía General de Aplicaciones* (U·2)
- **Revisión principal:** `review.prometeo.evidence_scale_versions`

## 1. Función estable de la escala

A través de las obras, E0–E8 pretende cumplir una función estable:

- clasificar la calidad/tipo de evidencia que sustenta una arista causal;
- traducir esa clasificación a un rango admisible de peso `w`;
- alimentar el análisis de sensibilidad en lugar de fingir un peso puntual cierto.

El núcleo metodológico es reconocible y estable:

`tipo de evidencia → rango de incertidumbre sobre w`.

La tensión aparece en la **semántica de los niveles y en sus rangos numéricos**.

## 2. Método Prometeo — tabla del cuerpo (Cap. 2)

La tabla usada en el protocolo y reproducida en los casos aplica aproximadamente:

| Tipo | Rango w |
|---|---|
| E1 | `[0.75,0.95]` |
| E2 | `[0.70,0.90]` |
| E3 | `[0.55,0.75]` |
| E4 | `[0.50,0.70]` |
| E5 | `[0.35,0.55]` |
| E6 | `[0.25,0.45]` |
| E7 | `[0.10,0.30]` |
| E8 | `[0.05,0.20]` |
| E0 | `0.00` |

En esta formulación se insiste en una distinción epistemológica central:

> “no hay evidencia de la arista” no equivale a “hay evidencia de que la arista no existe”.

E0 requiere **evidencia positiva de ausencia**.

## 3. Método Prometeo — Apéndice A

El Apéndice A se presenta como “referencia de calibración central del método”, pero contiene otra tabla:

| Tipo | Rango w |
|---|---|
| E1 | `[0.75,0.95]` |
| E2 | `[0.55,0.75]` |
| E3 | `[0.40,0.60]` |
| E4 | `[0.30,0.55]` |
| E5 | `[0.20,0.45]` |
| E6 | `[0.15,0.35]` |
| E7 | `[0.05,0.20]` |
| E8 | `[0.02,0.10]` |
| E0 | `0.00` |

Las diferencias son sustanciales, no redondeos.

Ejemplos:

- E2 cambia de `[0.70,0.90]` a `[0.55,0.75]`;
- E3 cambia de `[0.55,0.75]` a `[0.40,0.60]`;
- E4 cambia de `[0.50,0.70]` a `[0.30,0.55]`;
- E8 cambia de `[0.05,0.20]` a `[0.02,0.10]`.

Por tanto una misma evidencia puede producir pesos y resultados de sensibilidad materialmente distintos según qué tabla del mismo libro se use.

## 4. Taxonomía General — U·2

La Taxonomía vuelve a declarar que la tabla E0–E8 es la “referencia de calibración central”, pero usa una tercera versión:

| Tipo | Rango w |
|---|---|
| E1 | `[0.75,0.95]` |
| E2 | `[0.55,0.75]` |
| E3 | `[0.40,0.60]` |
| E4 | `[0.35,0.55]` |
| E5 | `[0.30,0.50]` |
| E6 | `[0.25,0.45]` |
| E7 | `[0.15,0.35]` |
| E8 | `[0.05,0.20]` |
| E0 | `[0.00]` |

Esta tabla coincide parcialmente con el Apéndice A, pero no completamente.

No existe, por tanto, una única calibración transversal publicada.

## 5. Incompatibilidad fuerte en E0

La diferencia más importante no es numérica sino semántica.

### Prometeo — cuerpo y Apéndice A

E0 significa **arista nula documentada**:

- existe prueba de que el nodo no tuvo acceso, conocimiento, capacidad o participación;
- `w=0` se sostiene con evidencia positiva;
- la ausencia de evidencia no basta.

### Taxonomía U·2

E0 se define como:

> “Ausencia total de evidencia para la arista. La arista se excluye del análisis”.

Estas dos reglas son incompatibles.

Si “no encontré evidencia” basta para asignar `w=0`, entonces el método convierte una limitación epistemológica en una afirmación causal negativa.

Eso contradice directamente la distinción que Prometeo formula como fundamental:

`ausencia de evidencia ≠ evidencia de ausencia`.

Clasificación:

- tensión de redacción menor: no;
- diferencia de calibración: sí;
- incompatibilidad metodológica real: sí.

## 6. Riesgo causal de la versión E0 = ausencia de evidencia

Excluir una arista por falta de evidencia puede:

- eliminar nodos invisibles precisamente porque el expediente es incompleto;
- favorecer sistemáticamente a nodos de diseño o arquitectos con baja trazabilidad documental;
- sobrecargar nodos visibles;
- reducir artificialmente la incertidumbre;
- transformar “desconocido” en “cero”.

En términos metrológicos, un dato faltante/no identificado no debe convertirse automáticamente en medición cero.

La segunda edición deberá distinguir al menos:

- **arista nula demostrada**;
- **arista no acreditada / evidencia insuficiente**;
- **arista hipotética/inferida**, si el protocolo la admite.

## 7. Las bandas numéricas son calibraciones, no teoremas

Ninguna de las tres tablas deriva matemáticamente los extremos concretos de sus intervalos desde axiomas del sistema.

Afirmaciones como:

- E2 empieza en `0.55`;
- E4 termina en `0.70`;
- E8 empieza en `0.02`;

son decisiones de calibración/modelado salvo que exista evidencia empírica externa que las estime.

La jerarquía ordinal puede ser defendida metodológicamente:

`evidencia más directa/robusta → intervalo esperado más alto/estrecho`,

pero los números concretos requieren calibración y validación.

Por tanto, frases como “límites derivados de la estructura epistémica del tipo de evidencia” no bastan para demostrar los valores numéricos.

## 8. La jerarquía tampoco está totalmente limpia

La Taxonomía afirma una jerarquía general resumida como:

`documento directo > testimonio > correlación > indicio`.

Pero E2 es peritaje/análisis documental, E3 testimonio convergente y E4 correlación. La relación puede ser razonable como orden operativo, pero no es universalmente válida por el mero nombre del tipo.

Un peritaje débil puede ser menos fiable que múltiples documentos/testimonios convergentes; una correlación estadística extremadamente robusta puede aportar más información que un testimonio aislado.

Por tanto la “jerarquía” debe entenderse como **prior estructural del método**, no como ley epistémica universal, salvo validación.

## 9. Regla de intersección y contradicción

La Taxonomía trata cada tipo como si generara directamente un intervalo de `w` y permite intersectar rangos de fuentes distintas.

Eso presupone que los intervalos tienen el mismo significado metrológico y están calibrados sobre una escala común.

Mientras existan tres tablas incompatibles, esa operación no tiene base estable.

Además, una contradicción entre un documento y un testimonio no es necesariamente contradicción entre “rangos de peso causal”: primero puede ser contradicción sobre el **hecho** que sustenta la arista.

La segunda edición deberá separar:

1. adjudicación/valoración de evidencia sobre existencia y mecanismo de la arista;
2. estimación de magnitud causal `w` una vez establecida la arista;
3. incertidumbre del peso.

## 10. E0 y la incertidumbre

Una normalización futura debería impedir que tres estados diferentes colapsen en el mismo número:

- `w=0` porque se demostró ausencia de conexión;
- `w` desconocido porque no hay evidencia suficiente;
- `w≈0` porque hay conexión documentada pero de magnitud mínima.

Son objetos epistemológicamente distintos.

La escala actual no siempre los separa.

## 11. Impacto sobre R* y análisis de sensibilidad

E0–E8 alimenta directamente los rangos de `w`.

Por tanto cualquier cambio de calibración afecta:

- construcción del operador causal;
- R*;
- orden de nodos;
- Declaraciones A/B/C/D;
- análisis de sensibilidad;
- scores aplicados de S;
- cualquier ejemplo numérico construido desde esos rangos.

Tras `RES-RSTAR-001`, la escala de evidencia debe normalizarse en coordinación con el aparato causal vigente y no como tabla aislada.

## 12. Clasificación final

- **Función conceptual de E0–E8:** estable.
- **Una única tabla publicada:** no.
- **Tres calibraciones incompatibles:** sí.
- **E0 con semántica estable:** no.
- **Ausencia de evidencia = evidencia de ausencia:** incompatible con Prometeo.
- **Rangos numéricos demostrados:** no.
- **Jerarquía ordinal como prior metodológico:** sí, provisionalmente.
- **Calibración empírica transversal:** no demostrada.
- **Normalización de segunda edición:** obligatoria.
- **Adjudicación autoral requerida:** sí, especialmente para E0 y para escoger/reconstruir los rangos.

## 13. Preguntas que quedan para adjudicación/segunda edición

1. ¿Debe E0 reservarse exclusivamente para **evidencia positiva de ausencia**?
2. ¿Qué estado/notación debe representar “no hay evidencia suficiente para estimar la arista”?
3. ¿Debe existir una única tabla universal o bandas calibradas por dominio?
4. ¿Qué datos o criterio justifican los extremos numéricos?
5. ¿La clase E mide fuerza epistémica, tipo de fuente, o ambas?
6. ¿Cómo se combinan fuentes heterogéneas sin confundir existencia de la arista con magnitud del peso?
7. ¿Cómo se recalibran los ejemplos después de `RES-RSTAR-001`?
