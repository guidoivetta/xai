# Images to extract from Lecture_20.pdf

| Archivo | Slide PDF (página) | Contenido |
|---|---|---|
| fairml_title.png | 1 | Título del Paper 1: "Explainability for Fair Machine Learning" con autores |
| fairml_history.png | 2 | Gráfico "Brief History of Fairness in ML" (LOL FAIRNESS!! / OH, CRAP.) |
| fairml_challenges_table.png | 3 | Tabla de definiciones de fairness (Statistical parity, Equal opportunity, etc.) |
| fairml_demographic_parity.png | 4 | Definición demographic parity: "f(x) unconditionally independent of sensitive attr. a" |
| fairml_equalized_odds.png | 5 | Definición equalized odds con tablas Female/Male students Qualified/Unqualified |
| fairml_manipulation.png | 6 | Explanation methods can be manipulated: histogramas de importancia género (original vs modified) |
| fairml_accuracy_shapley.png | 9 | Fórmulas Shapley para accuracy: ecuaciones (1)–(5) |
| fairml_fairness_shapley.png | 11 | Fórmulas Shapley para fairness: ecuaciones (6)–(9) |
| fairml_perturbation.png | 12 | Learning corrective perturbations: f_θ = f + δ_θ, ecuaciones (10)–(11) |
| fairml_explainability_plots.png | 15 | 6 plots: Unfair model f / Perturbation δ_θ / Corrected model f_θ (accuracy + dem. parity) |
| fairml_robustness.png | 16 | Robustness: Accuracy y Fairness Shapley values (original vs suppressed sex feature) |
| fairml_perf_dp.png | 17 | Table 1: Accuracy associated with decreasing demographic parity thresholds |
| fairml_perf_eo.png | 18 | Table 2: Accuracy associated with decreasing equalised odds thresholds |
| fairml_stability.png | 20 | Violin plots: Perturbed vs Zhang et al. vs Adel et al. — Figure 3 |
| rocerf_title.png | 23 | Título del Paper 2: "Towards Bridging the Gaps between Right to Explanation and Right to be Forgotten" |
| rocerf_notation.png | 28 | Notación ROCERF: D, f_θ, data weight vector w |
| rocerf_cfe_opt.png | 30 | CFE como optimización: min ||x-x0||_2 s.t. f_{θ1}(x) ≥ 0 |
| rocerf_k_removal.png | 31 | K-Removal Robust CFE: W^(k), optimización con binom(n,k) restricciones |
| rocerf_approx_formula.png | 33 | Fórmula eficiente aproximada (caja roja): f̃_{θ_w}(x) = f_{θ1}(x) + (1/n)Σ β(x)^T H^{-1} g_i(θ1) |
| rocerf_final_opt.png | 35 | Optimización final: f_A^{(k)}(x) y problema min ||x-x0||_2 s.t. f_A^{(k)}(x) ≥ δ |
| rocerf_validity_cost.png | 38 | Definiciones de validity y cost: fórmulas de evaluación |
| rocerf_results_lr.png | 44 | Figure 1: Average validity (logistic regression) vs fraction of removal α — German Credit, COMPAS, Adult |
| rocerf_results_nn.png | 45 | Figure 2: Average validity (neural networks) vs fraction of removal α — German Credit, COMPAS, Adult |
| rocerf_costs_tables.png | 46 | Table 1 (logistic regression) + Table 2 (neural networks): average cost L2 norm |
| rocerf_sensitivity.png | 47 | Figure 3: Sensitivity analysis con hyperparameter k (k=0.005n a 0.05n) |
