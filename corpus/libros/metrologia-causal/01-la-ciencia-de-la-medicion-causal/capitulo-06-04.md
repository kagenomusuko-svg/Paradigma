PARTE VI · Los documentos del análisis: producción e interpretación

### Capítulo VI·4

### El vector R*: producción y estructura

Del eigenvector del grafo a la tabla de distribución con todos los

parámetros

### I.  El cálculo del vector R* desde la hoja de calibración

El vector R* se calcula en tres pasos a partir de la hoja de calibración. Primer paso: construir la matriz de adyacencia ponderada W desde la hoja de calibración, usando el punto central de cada rango [a_ij, b_ij] como w_ij. Segundo paso: verificar que W satisface las condiciones de Perron-Frobenius (irreducibilidad y aperiodicidad). Si no las satisface, aplicar los protocolos del capítulo V·2. Tercer paso: calcular el eigenvector principal de W usando el método de potencias, normalizar para que la suma sea 1.00, y redondear a cuatro decimales.

El cálculo del eigenvector con el punto central de los rangos produce el R* de punto central — el que aparece en la columna principal de la tabla del vector. El R* de punto central es el valor más probable de la distribución de responsabilidad dado el estado central del conocimiento sobre la evidencia. No es el valor correcto ni el valor único: es el punto de referencia

Metrología Causal

alrededor del cual el análisis de sensibilidad explora el espacio de parámetros.

R*_neta_i = R*_i × (1 − S_i) se calcula para cada nodo después de determinar S_i desde la distribución P(Hijos) del nodo (tabla de S por Hijo, II·10, modulada por los códigos de eje del SDO, III·8). La tabla del vector presenta ambas columnas — R* y R*_neta — para que el lector pueda ver simultáneamente la centralidad causal total y la centralidad idiosincrática.

### II.  La estructura de la tabla del vector R*

α Δ = R*

Nod

Descrip

R* (midp

R*_n

S (midp

o

ción

eta

oint)

oint)

× (1−

α)

ECP Agente del MP — acto detonant e

### 0.308 0.283 0.08 0. 11 0.2 74

PSM Agente del MP — encubri miento

### 0.118 0.031 0.74 0. 06 0.1 11

Metrología Causal

FRO Fiscalía — nodo de diseño del campo

### 0.381 0.362 0.05 0. 03 0.3 70

BM Banco Meridion al — daño estructur al

### 0.193 0.095 0.51 0. 24 0.1 47

— 1.000 0.771 — — 0.9 02

TOT AL

La tabla del caso Altamirano ilustra la estructura estándar del vector R*. Cada fila es un nodo; las columnas son los parámetros del sistema. La columna TOTAL verifica que Σ R* = 1.000 (la suma de las responsabilidades causales es el 100% del daño). Σ R*_neta = 0.771 < 1.000 porque la diferencia (0.229) es la responsabilidad sistémica — la fracción del daño que corresponde al campo c en lugar de a los actores individuales. Σ Δ = 0.902 es el déficit total de asunción del sistema: el 90.2% del daño causado no ha sido reconocido por ningún nodo.

### III.  El formato estándar para cada tipo de foro

Metrología Causal

El formato de la tabla varía con el foro. Ante el tribunal: la tabla completa con todas las columnas, acompañada de una nota al pie que define cada parámetro en lenguaje no técnico. La columna Δ es especialmente relevante para el juez porque muestra la brecha entre lo causado y lo reconocido — la información que el sistema de Prometeo añade al sistema de imputación ordinario. Ante el consejo de administración: la tabla simplificada con R*, R*_neta y Δ, sin α y sin S, con una columna adicional de «implicaciones para el plan de acción». Ante el regulador: la tabla completa con el IIC añadido como columna adicional para los nodos institucionales, porque el regulador necesita la brecha de integridad para diseñar las medidas.

Metrología Causal

