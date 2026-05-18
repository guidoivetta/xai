# Are SHAP Explanations Reliable for Operational Decision Support?
## A Stability and Faithfulness Audit in Electrical Distribution Incident Management

**Integrantes:** Martin Hunziker

---

## Objetivo

**Pregunta de investigación:** ¿Las explicaciones SHAP generadas para un modelo de predicción
de despachos técnicos improcedentes son estables, fieles al modelo, y consistentes entre
incidentes similares? ¿Estas propiedades varían según características del incidente?

**Hipótesis central:** En dominios operacionales críticos, las explicaciones post-hoc basadas 
en SHAP pueden poner en evidencia inestabilidad y baja faithfulness en en subgrupos específicos 
de instancias y también de forma despareja en subgrupos definidos por características usadas de 
forma discriminatoria, como por ejemplo el barrio en el que se encuentran subgrupos específicos 
de instancias,comprometiendo su utilidad real para operadores que deben tomar decisiones bajo 
presión de tiempo.

---

## Propuesta experimental

El experimento utiliza un dataset de incidentes históricos de una distribuidora eléctrica
brasileña, donde un modelo XGBoost predice si el desplazamiento de una cuadrilla técnica va 
a resultar improcedente en el momento en que llegue a realizarse.

Se evaluarán tres propiedades formales de las explicaciones SHAP sobre el modelo entrenado:

**Experimento 1 — Estabilidad:** Para cada instancia, se computa SHAP con múltiples seeds y
tamaños de background. Se mide la varianza del ranking top-k de features entre corridas.
Un operador no puede confiar en una explicación que cambia cada vez que se recalcula.

**Experimento 2 — Faithfulness:** Se aplica input perturbation: si se zeroa la feature más
importante según SHAP, ¿la predicción cambia más que si se zeroa una feature aleatoria?
Se computa un faithfulness score por instancia siguiendo la metodología de Covert et al. (2021).

**Experimento 3 — Consistencia local:** Para pares de incidentes similares (vecinos en el
espacio de features), se mide si sus explicaciones SHAP son también similares. Alta similitud
de input con baja similitud de explicación indica inestabilidad operacionalmente problemática.

**Análisis complementario — Disparidad por subgrupo:** Se evalúa si el faithfulness score
varía significativamente según zona geográfica, tipo de cliente o franja horaria, conectando
con el eje de fairness en la calidad de explicaciones (Dai et al., 2022).

---

## Plan de actividades

| Semana | Actividad |
|---|---|
| **Semana 1** | Revisión bibliográfica; preprocesamiento del dataset; entrenamiento y evaluación del modelo XGBoost (accuracy, F1, AUC-ROC); análisis exploratorio de features |
| **Semana 2** | Cómputo de SHAP values globales y locales; implementación de Experimento 1 (estabilidad: varianza del ranking top-k entre seeds y tamaños de background); implementación de Experimento 2 (faithfulness via input perturbation) |
| **Semana 3** | Implementación de Experimento 3 (consistencia local entre incidentes similares); análisis de disparidad por subgrupo (zona, tipo de cliente, franja horaria); análisis estadístico integrado y visualizaciones |
| **Semana 4** | Redacción del paper en inglés (template ACM, hasta 12 páginas); revisión y corrección; preparación de la presentación oral |

---

## Relación con los temas del curso

- **Semana 4** — Feature attributions: SHAP como método central del experimento
- **Semana 5** — Pitfalls y evaluación de explicaciones: núcleo metodológico (Slack et al. 2020,
  Adebayo et al. 2018, Agarwal et al. 2023)
- **Semana 9** — Teoría de explicabilidad: faithfulness score basado en Covert et al. (2021)
- **Semana 10** — Fairness y XAI: análisis de disparidad en calidad de explicaciones
  (Begley et al. 2020, Dai et al. 2022)
- **Semana 2** — Human factors: motivación desde la perspectiva del operador

---

## Referencias iniciales

- Lundberg & Lee, 2017 — SHAP
- Slack et al., 2020 — Fooling LIME and SHAP
- Adebayo et al., 2018 — Sanity Checks for Saliency Maps
- Covert et al., 2021 — Explaining by Removing
- Agarwal et al., 2023 — OpenXAI
- Begley et al., 2020 — Explainability for Fair Machine Learning
- Dai et al., 2022 — Fairness via Explanation Quality
- Hunziker et al., 2025 — Improper dispatch prediction (dataset base)
