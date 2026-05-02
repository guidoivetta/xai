# Images to replace

| Archivo | Slide PDF (página) | Contenido |
|---|---|---|
| `xal_system_overview.png` | 2 | Diagrama XAL: Teacher → (prediction + explanation) → Learner → (confirm/reject + feedback) → Teacher. Loop de active learning con flecha azul de explicación |
| `xal_explanation_example.png` | 5 | Barra horizontal de feature importance local: top 5 features, verde=positivo, rojo=negativo, naranja=base chance (intercepto del modelo). Ejemplo Adult Income dataset |
| `xal_study_conditions.png` | 10 | Tres condiciones de estudio: AL (standard active learning), CL (crowdsourcing, random queries), XAL (active learning + explanations). 36 participantes AMT, 2 stages, 20 anotaciones cada uno |
| `xal_accuracy_curve.png` | 12 | Curva de accuracy del modelo AL: eje x = número de queries, eje y = accuracy. Marca "early stage" (izquierda, baja accuracy) y "late stage" (derecha, alta accuracy) |
| `xal_trust_calibration.png` | 17 | Gráfico de trust calibration por condición (AL/CL/XAL) en early vs late stage. XAL: trust bajo en early (modelo incorrecto), trust alto en late (modelo mejorado) |
| `xal_open_feedback.png` | 20 | Categorías de feedback abierto de participantes: Tuning weights (81), Removing/changing/adding features (28), Ranking (12). Gráfico de barras o tabla |
| `xal_related_work.png` | 22 | Slide de Related Work: Active Learning, Interactive ML, Explainable AI references |
| `ttm_system_overview.png` | 36 | Diagrama TalkToModel: User → Natural Language → Dialogue Engine → DSL parse → Execution Engine → Explanation → Text Interface → User. Tres componentes conectados |
| `ttm_dialogue_engine.png` | 42 | Diagrama del Dialogue Engine: utterance → grammar-based parser / LLM (T5 fine-tuned, GPT-J few-shot) → parse tree → DSL operation |
| `ttm_execution_engine.png` | 48 | Diagrama del Execution Engine: parse → DiCE (counterfactual) / LIME / KernelSHAP / Data exploration → Faith score selection → templated response |
| `ttm_faith_fudge.png` | 50 | Fórmula del Fudge score: Fudge(f,x,m) = (1/N)Σ|f(x) - f(x + ε_n ⊙ m)|. Explicación visual de máscaras sobre features |
| `ttm_llm_results.png` | 88-90 | Tabla de Exact Match Accuracy: filas = modelos (Nearest Neighbors, GPT-Neo 1.3B/2.7B, GPT-J 6B, T5 small/base/large), columnas = German/Compas/Diabetes × IID/Comp/Overall. T5-Large mejor (highlighted verde), GPT-Neo peor (highlighted rojo) |
| `ttm_grammar_operations.png` | 93 | Tabla completa de operaciones DSL: Data (filter, change, show, statistic, count, and, or), Explainability (explain, cfe, topk, important, interaction, mistakes), ML (predict, likelihood, incorrect, score), Conversational (prev_filter, prev_operation, followup), Description (function, data, model, define) |
| `ttm_user_experiment.png` | 94 | Resultados User Study: tabla % Agree TalkToModel Better (healthcare workers vs ML grads) en Easiness/Confidence/Speed/Likability. Tabla % Questions Completed y % Accuracy por grupo |
| `ttm_explainerdashboard.png` | 95 | Screenshot explainerdashboard: "Model Explainer" UI con tabs (Feature Importances, Classification Stats, Individual Predictions, What if..., Feature Dependence, Feature Interactions, Decision Trees). Gráfico SHAP values del Titanic dataset |
| `ttm_interface_screenshot.png` | 96 | Screenshot TalkToModel: interfaz de chat con usuario preguntando "how likely are patients older than forty to have diabetes?" y respuesta del sistema mostrando estadísticas y feature importances |
