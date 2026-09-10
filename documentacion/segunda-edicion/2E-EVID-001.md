# 2E-EVID-001 — Corrección editorial de E0–E8, `w` e incertidumbre

> **Producto editorial derivado para segunda edición.** Ejecuta `RES-EVID-001`. No modifica las fuentes canónicas de primera edición durante MANT ni introduce calibraciones numéricas no validadas.

- **ID:** `2E-EVID-001`
- **Estado:** **PREPARADO PARA SEGUNDA EDICIÓN / EJECUCIÓN DIFERIDA**
- **Prioridad:** alta
- **Resolución rectora:** `RES-EVID-001`
- **Auditoría relacionada:** `AUD-EVID-001`
- **Resoluciones relacionadas:** `RES-RSTAR-001`, `RES-SDO-PROM-001`, `RES-HISTOS-PROM-001`
- **Ámbito principal:** *Método Prometeo* Cap. 2 y Apéndice A; *Taxonomía General de Aplicaciones* U·2; referencias transversales a E0–E8, rangos `w`, análisis de sensibilidad y combinación de evidencia.

---

## 1. Principio editorial rector

La segunda edición debe separar explícitamente tres objetos:

1. **estado de la arista**;
2. **estimación de la magnitud causal**;
3. **incertidumbre epistémica de esa estimación**.

La regla central será:

> **la clase E informa fuerza epistémica e incertidumbre; no fija por sí sola la magnitud causal.**

La edición debe impedir que el lector interprete:

`E1 → w alto`

`E8 → w bajo`

como una ley del método.

---

## 2. Reescribir la arquitectura de Prometeo Paso 2

La secuencia actual debe desdoblarse.

No:

`tipo E → rango predeterminado de w`.

Sí:

`evidencia sustantiva`

`→ acreditación de existencia/mecanismo de la arista`

`→ estimación de magnitud causal ŵ`

`→ clasificación epistémica E1–E8`

`→ incertidumbre U(ŵ)`

`→ sensibilidad de Q_D / b_D / R*`.

La edición podrá adoptar otra notación definitiva, pero deberá conservar esta separación semántica.

---

## 3. Introducir notación diferenciada para estimación e incertidumbre

Usar provisionalmente o mediante equivalente editorial:

- `w_ij`: magnitud causal local;
- `ŵ_ij`: estimación de esa magnitud;
- `U(ŵ_ij)`: incertidumbre asociada.

`U(ŵ)` puede terminar representándose como:

- intervalo;
- radio;
- distribución;
- conjunto de sensibilidad;
- otra estructura metrológica.

La segunda edición no deberá elegir una forma matemática definitiva sin justificación suficiente.

---

## 4. Rehacer la tabla E1–E8

Las tablas actuales que asignan a cada clase E una banda fija de `w` no deben conservarse como definiciones de magnitud causal.

La nueva tabla debe separar, como mínimo:

- clase E;
- naturaleza/tipo de fuente;
- criterios de calidad;
- independencia;
- corroboración;
- ambigüedad;
- limitaciones;
- efecto esperado sobre la **precisión** de `ŵ`;
- factores que ensanchan o reducen `U(ŵ)`;
- reglas específicas de dominio, cuando existan.

No debe incluir una columna que pueda leerse como:

> «por ser E3, `w` debe encontrarse entre a y b».

---

## 5. E1–E8 como prior metodológico, no ley universal

La edición puede conservar una jerarquía ordinal general de fuerza epistémica, pero debe calificarla.

En igualdad de las demás condiciones:

- evidencia directa, independiente y corroborada debería sostener mayor precisión;
- evidencia indirecta, ambigua o no corroborada debería sostener menor precisión.

Pero el texto debe admitir excepciones por:

- ambigüedad documental;
- calidad metodológica del peritaje;
- independencia de testigos;
- tamaño/calidad de muestra;
- sesgos;
- contradicción;
- diferencias de dominio.

Por tanto no deberá decirse que E1 **siempre** implica un intervalo más estrecho que E2 o que cada paso ordinal tiene una anchura universal.

---

## 6. Separar E0 de la jerarquía E1–E8

La segunda edición debe decir expresamente:

> **E0 no es evidencia positiva más débil que E8.**

E0 representa:

`evidencia positiva de ausencia causal → arista nula documentada → w = 0`.

Por ello no debe representarse visualmente como el extremo inferior de una escala continua de fuerza epistémica.

Puede conservarse la etiqueta histórica `E0` por continuidad terminológica, pero debe marcarse como **estado especial**.

---

## 7. Eliminar «ausencia de evidencia = E0»

Taxonomía U·2 debe corregirse donde define E0 como «ausencia total de evidencia para la arista».

La segunda edición deberá distinguir:

### Nulidad documentada

Existe evidencia positiva de que la conexión no existe.

`E0 / w=0`.

### Hipótesis o arista no acreditada

No existe evidencia suficiente para incorporarla al grafo causal validado.

No recibe `w=0`.

### Arista acreditada

Existe evidencia suficiente de la conexión.

Recibe estimación `ŵ`, clase E1–E8 e incertidumbre `U(ŵ)`.

---

## 8. Definir el espacio de hipótesis

La segunda edición deberá decidir una convención explícita para conexiones plausibles pero no acreditadas.

Opciones editoriales admisibles:

- mantenerlas fuera de `G_D` en una lista de hipótesis;
- usar un grafo auxiliar de investigación;
- usar una marca específica no confundible con arista causal validada.

No debe usarse `w=0` para representar desconocimiento.

La decisión de notación queda abierta; la separación semántica es obligatoria.

---

## 9. Reconstruir cómo se estima la posición de `ŵ`

La segunda edición debe hacer explícito que la posición central o estimación sustantiva de `w` se deriva del mecanismo causal y de los hechos del caso.

Según el dominio, la justificación puede considerar:

- grado de formalización del comportamiento;
- margen de discrecionalidad;
- costos de apartarse;
- fungibilidad;
- secuencia de transmisión causal;
- capacidad material;
- habilitación;
- intensidad de la restricción;
- evidencia cuantitativa directamente relacionada con magnitud;
- otros factores causalmente pertinentes.

La edición debe distinguir entre:

> **«esta fuente demuestra que la arista existe»**

y

> **«esta fuente permite estimar que su magnitud es aproximadamente x»**.

No son la misma proposición.

---

## 10. Reconstruir cómo se determina `U(ŵ)`

La clase E debe migrar hacia la capa de incertidumbre.

Una futura regla operativa podrá usar factores como:

- clase E;
- número de fuentes;
- independencia;
- convergencia;
- contradicción;
- completitud;
- ambigüedad;
- calidad del método;
- dominio.

La segunda edición no deberá inventar coeficientes numéricos durante la reescritura.

Si se conservan números provisionales, deberán etiquetarse expresamente como **calibración provisional/versionada de incertidumbre**, no como definición de la magnitud causal.

---

## 11. Tratamiento de las tres tablas históricas

Las tres tablas existentes deberán conservarse como parte de la historia editorial del método, pero no competir como «la tabla verdadera».

La segunda edición debe explicar que fueron intentos de calibración que mezclaban:

- posición de `w`;
- amplitud de incertidumbre;
- clase de evidencia.

Ninguna se adopta automáticamente como canónica.

Si alguna información numérica se reutiliza, deberá pasar por una nueva justificación metrológica.

---

## 12. Reescribir la regla de intersección de Taxonomía U·2

La edición no debe intersectar automáticamente bandas E.

Antes de combinar intervalos debe documentarse:

1. qué proposición sostiene cada fuente;
2. si ambas estiman el mismo parámetro `w`;
3. qué semántica tiene cada `U(ŵ)`;
4. si las fuentes son independientes o dependientes;
5. qué regla de combinación es justificable.

La intersección puede conservarse únicamente si esas condiciones se satisfacen.

No debe presentarse como consecuencia automática de tener dos clases E distintas.

---

## 13. Reescribir la regla de prioridad

Cuando dos fuentes contradicen, la edición debe identificar primero **qué está en contradicción**:

- existencia de la arista;
- dirección;
- mecanismo;
- magnitud;
- hecho auxiliar;
- calidad/credibilidad de fuente.

La clase E superior puede constituir un prior metodológico, pero no autoriza por sí sola un desplazamiento numérico universal de `w`.

Cualquier regla futura de actualización debe declarar su semántica y supuestos.

---

## 14. Adaptar la Declaración D

Taxonomía puede conservar la Declaración D como salida de insuficiencia, pero sus disparadores deben expresarse en términos de incertidumbre efectiva y robustez del resultado, no de la supuesta magnitud implícita de E7/E8.

Ejemplo de criterio válido:

> una arista crítica tiene `U(ŵ)` tan amplio que el orden de `R*` cambia dentro del espacio plausible.

No:

> la arista es E8, por tanto su `w` es bajo.

---

## 15. Adaptar el análisis de sensibilidad

Bajo `RES-RSTAR-001`, la sensibilidad debe propagarse desde la incertidumbre de los pesos locales.

La segunda edición deberá reconstruir:

`ŵ ± U(ŵ)`

`→ Q_D / b_D variables`

`→ R*(D)`

`→ estabilidad o cambio de conclusiones`.

El cálculo no debe variar `w` dentro de una banda cuya posición proviene únicamente de E.

---

## 16. Hoja de calibración revisada

La hoja de trabajo de cada arista debería contener, como mínimo:

- identificador de arista;
- estado: nula / hipótesis / acreditada;
- mecanismo causal alegado;
- evidencia que acredita existencia;
- clase E de cada fuente;
- independencia/dependencia entre fuentes;
- hechos que sustentan magnitud;
- estimación `ŵ`;
- justificación de `ŵ`;
- representación `U(ŵ)`;
- justificación de incertidumbre;
- contradicciones;
- análisis de sensibilidad pertinente;
- trazabilidad a expediente.

Esto evita que «clasificar E» sea la única decisión sustantiva del analista.

---

## 17. Pruebas editoriales obligatorias

La reparación deberá superar al menos estas pruebas:

1. **E1 con magnitud baja:** un documento directo puede sostener `ŵ=0.15` si el mecanismo demuestra baja determinación.
2. **E6 con magnitud alta e incertidumbre alta:** evidencia estructural puede sostener una estimación central alta sin fingir precisión.
3. **E0 fuerte:** sólo evidencia positiva de ausencia produce `w=0`.
4. **desconocido ≠ cero:** falta de evidencia no introduce una arista nula.
5. **E0 fuera de la ordinalidad:** E0 no aparece como «menos fuerte» que E8.
6. **intersección condicionada:** no se combinan bandas sin semántica común de incertidumbre.
7. **contradicción tipada:** el protocolo identifica si el conflicto es sobre existencia, mecanismo, magnitud o fuente.
8. **sensibilidad real:** `R*` varía por `U(ŵ)`, no por posiciones prefijadas de E.

---

## 18. Búsqueda transversal antes de cerrar segunda edición

Debe auditarse toda ocurrencia que:

- afirme que E1 implica `w` alto;
- afirme que E8 implica `w` bajo;
- trate E0 como ausencia de evidencia;
- represente E0 como extremo inferior ordinal;
- asigne bandas de `w` únicamente desde clase E;
- intersecte rangos E automáticamente;
- aplique desplazamientos numéricos de prioridad sin semántica de incertidumbre;
- use E7/E8 como sustituto de una conclusión sobre magnitud;
- declare una arista nula por expediente incompleto;
- omita distinguir arista hipotética de arista nula.

Cada ocurrencia deberá clasificarse como:

- reescritura necesaria;
- aclaración de tipado;
- nota histórica;
- recalibración pendiente;
- sin cambio.

---

## 19. Qué permanece abierto

Esta nota **no resuelve numéricamente**:

- estimador definitivo de `ŵ`;
- forma matemática de `U(ŵ)`;
- radios o amplitudes por E;
- calibración por dominio;
- dependencia entre fuentes;
- regla óptima de combinación;
- actualización bayesiana u otro formalismo;
- validación empírica;
- recálculo de ejemplos históricos.

Estas cuestiones son deuda metrológica/empírica, no contradicción doctrinal restante sobre E0–E8.

---

## 20. Resultado editorial esperado

Tras ejecutar `2E-EVID-001`, el lector deberá poder reconstruir sin ambigüedad:

`estado de arista`

`+ mecanismo causal`

`+ evidencia sustantiva`

`→ ŵ`

mientras, por una ruta distinta:

`clase E + calidad/convergencia/contradicción/dominio`

`→ U(ŵ)`.

Después:

`ŵ + U(ŵ)`

`→ sensibilidad de Q_D,b_D`

`→ R*(D)`.

Y deberá ser imposible reducir el método a:

`E1–E8 → posición predeterminada de w`.

---

## 21. Condición de cierre

`2E-EVID-001` quedará ejecutada únicamente cuando:

- Prometeo Cap. 2 y Apéndice A hayan sido reescritos bajo la separación magnitud/incertidumbre;
- Taxonomía U·2 haya corregido E0 y sus reglas de combinación;
- E0 quede fuera de la ordinalidad E1–E8;
- exista tratamiento explícito de aristas no acreditadas;
- la hoja de calibración separe `ŵ` y `U(ŵ)`;
- toda tabla numérica restante declare su estatus de calibración;
- el análisis de sensibilidad use incertidumbre de pesos y no bandas de magnitud predeterminadas por E;
- se hayan auditado las referencias transversales;
- no se presente ninguna calibración provisional como teorema o validación empírica.