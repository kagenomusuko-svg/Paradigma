# Análisis textual auditable

Esta carpeta contiene una capa **derivada** del corpus. Las fuentes canónicas permanecen en `corpus/fuentes/` y no se modifican.

## Regla epistemológica

El sistema separa estrictamente:

1. **evidencia textual**: unidades y citas localizables;
2. **extracción automática**: conceptos del glosario, definiciones explícitas y candidatos;
3. **revisión**: aprobación, rechazo o reclasificación;
4. **reconstrucción**: relaciones o tesis obtenidas de varias evidencias;
5. **inferencia**: conclusión que exige premisas y una regla declarada.

La extracción automática **no puede** crear por sí sola equivalencias, contradicciones, dependencias conceptuales ni puentes inferenciales.

## Invariantes

- No hay definición explícita → no se crea una definición explícita.
- No hay texto literal equivalente → se registra `null`.
- No sabemos si A = B → A y B permanecen separados.
- Una inferencia conserva siempre sus premisas y su regla.
- Una inferencia nunca se convierte retroactivamente en evidencia primaria.
- Una contradicción requiere revisión de referente, sentido, nivel de análisis, escala temporal y contexto.
- La explicación del autor orienta la búsqueda; no sustituye la evidencia del corpus.
- Si el corpus no resuelve una cuestión → `no_determinado`.
- Todo registro sustantivo debe poder retroceder a una unidad textual o declarar que es reconstruido/inferido.

## Piloto v0.1

El primer piloto usa `Afrodita Areia: Sobre la pasión - Volumen I`.

El extractor determinista:

- divide los Markdown derivados en unidades textuales con líneas;
- obtiene conceptos y definiciones **solo** del glosario explícito;
- marca afirmaciones candidatas mediante patrones lingüísticos de alta precisión;
- extrae fórmulas candidatas literalmente;
- construye apariciones por concepto;
- no interpreta relaciones ni resuelve tensiones.

Los resultados se escriben en `analisis/generado/sobre-la-pasion/` y se validan con `scripts/auditar_analisis.py`.

La carpeta `generado/` es evidencia de trabajo, **no doctrina aprobada**.
