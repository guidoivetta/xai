# Images to replace

| Archivo | Slide PDF (página) | Contenido |
|---|---|---|
| `xal_prediction_task.png` | 2 | Customer profile del dataset Adult Income + esquema del modelo de regresión logística. Perfil de persona con atributos (age, occupation, education, etc.) |
| `xal_active_learning_task.png` | 4 | Participante juzgando nivel de ingreso de un customer profile dentro del loop de AL. Similar a xal_prediction_task pero en contexto de Active Learning con query del modelo |
| `xal_system_overview.png` | 8 | Diagrama XAL: Teacher → (prediction + explanation) → Learner → (confirm/reject + feedback) → Teacher. Loop de active learning con flecha azul de explicación |
| `xal_explanation_example.png` | 9 | Barra horizontal de feature importance local: top 5 features, verde=positivo, rojo=negativo, naranja=base chance (intercepto del modelo). Ejemplo Adult Income dataset |
| `xal_study_conditions.png` | 13 | Tres condiciones de estudio: AL (standard active learning), CL (crowdsourcing, random queries), XAL (active learning + explanations). 36 participantes AMT, 2 stages, 20 anotaciones cada uno |
| `xal_accuracy_curve.png` | 12 | Curva de accuracy del modelo AL: eje x = número de queries, eje y = accuracy. Marca "early stage" (izquierda, baja accuracy) y "late stage" (derecha, alta accuracy) |
| `xal_results_rq1.png` | 15 | Gráficos de annotation + learning outcomes para RQ1: human accuracy y % agreement decreases in later stage; model accuracy increases. Barras o líneas por condición (AL/CL/XAL) |
| `xal_trust_calibration.png` | 18 | Gráfico de trust calibration por condición (AL/CL/XAL) en early vs late stage. XAL: trust bajo en early (modelo incorrecto), trust alto en late (modelo mejorado) |
| `xal_results_h4.png` | 21-22 | Resultados H4: comparación de accuracy y blind trust en XAL por nivel de task knowledge (high vs low). Scatter o barras mostrando que los de menor conocimiento tienen menor accuracy y mayor blind trust |
| `xal_results_h5.png` | 23 | Resultados H5: trust calibration en XAL para participantes con vs. sin experiencia en AI. Los sin experiencia se benefician más de las explicaciones |
| `xal_results_h2h6.png` | 24 | Resultados H2 y H6: satisfaction en XAL según need for cognition. Efecto negativo significativo para quienes tienen bajo need for cognition |
| `xal_results_h3.png` | 25 | Resultados H3: cognitive workload en XAL para participantes con vs. sin experiencia en AI. XAL induce mayor workload para quienes tienen experiencia en AI |
| `xal_explanation_ratings.png` | 27 | Ratings de explicaciones en condición XAL: más altos cuando el modelo es correcto y cuando los anotadores incorrectamente discrepan con el modelo en la etapa tardía |
| `xal_open_feedback.png` | 28 | Categorías de feedback abierto de participantes: Tuning weights (81), Removing/changing/adding features (28), Ranking (12). Gráfico de barras o tabla |
| `xal_related_work.png` | 30 | Slide de Related Work: Active Learning, Interactive ML, Explainable AI references |
| `ttm_system_overview.png` | 36 | Diagrama TalkToModel: User → Natural Language → Dialogue Engine → DSL parse → Execution Engine → Explanation → Text Interface → User. Tres componentes conectados |
| `ttm_background_methods.png` | 40 | Los tres métodos XAI ilustrados: SHAP (Shapley values bar chart), LIME (local linear approximation), Counterfactual (minimal changes to flip prediction). Tres columnas con ilustraciones |
| `ttm_method_pipeline.png` | 44-47 | Pipeline completo de TalkToModel: Human Query → Dialogue Engine (LLM) → Structured Instructions → Execution Engine → Structured Result → Natural Language Response. Diagrama de flujo con los tres componentes principales |
| `ttm_dialogue_engine.png` | 42 | Diagrama del Dialogue Engine: utterance → grammar-based parser / LLM (T5 fine-tuned, GPT-J few-shot) → parse tree → DSL operation |
| `ttm_data_collection.png` | 56-59 | Pipeline de data collection: Authors (50 pairs) → MTurk paraphrase (×8 = 400) → MTurk fidelity rating (keep ≥3/4) → Manual filtering → Wildcard enumeration → 20k-40k pairs |
| `ttm_execution_engine.png` | 48 | Diagrama del Execution Engine: parse → DiCE (counterfactual) / LIME / KernelSHAP / Data exploration → Faith score selection → templated response |
| `ttm_faith_fudge.png` | 50 | Fórmula del Fudge score: Fudge(f,x,m) = (1/N)Σ|f(x) - f(x + ε_n ⊙ m)|. Explicación visual de máscaras sobre features |
| `ttm_grammar_operations.png` | 75 | Tabla completa de operaciones DSL: Data (filter, change, show, statistic, count, and, or), Explainability (explain, cfe, topk, important, interaction, mistakes), ML (predict, likelihood, incorrect, score), Conversational (prev_filter, prev_operation, followup), Description (function, data, model, define) |
| `ttm_results_summary.png` | 76 | Diagrama resumen de los 3 experimentos: (1) LLM Experiment → Dialogue Engine, (2) Grammar Experiment, (3) User Experiment → Dialogue+Execution Engine |
| `ttm_llm_results.png` | 88-90 | Tabla de Exact Match Accuracy: filas = modelos (Nearest Neighbors, GPT-Neo 1.3B/2.7B, GPT-J 6B, T5 small/base/large), columnas = German/Compas/Diabetes × IID/Comp/Overall. T5-Large mejor (highlighted verde), GPT-Neo peor (highlighted rojo) |
| `ttm_user_experiment.png` | 94 | Resultados User Study: tabla % Agree TalkToModel Better (healthcare workers vs ML grads) en Easiness/Confidence/Speed/Likability. Tabla % Questions Completed y % Accuracy por grupo |
| `ttm_explainerdashboard.png` | 95 | Screenshot explainerdashboard: "Model Explainer" UI con tabs (Feature Importances, Classification Stats, Individual Predictions, What if..., Feature Dependence, Feature Interactions, Decision Trees). Gráfico SHAP values del Titanic dataset |
| `ttm_interface_screenshot.png` | 96 | Screenshot TalkToModel: interfaz de chat con usuario preguntando "how likely are patients older than forty to have diabetes?" y respuesta del sistema mostrando estadísticas y feature importances |
