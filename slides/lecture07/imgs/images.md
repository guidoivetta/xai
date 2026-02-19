# Images to extract from Lecture_7.pdf

| Archivo | Slide PDF | Contenido |
|---|---|---|
| `lime_explanation_flow.png` | Página 3 | Diagrama de flujo: Model → Data and Prediction → Explainer (LIME) → Explanation (magnifying glass con sneeze/headache/no fatigue) → Human makes decision |
| `model_selection.png` | Página 4 | UI comparando Algorithm 1 vs Algorithm 2, mostrando palabras importantes y predicciones para clase Atheism |
| `lime_formula.png` | Página 7 | Fórmula LIME con anotaciones: ξ(x) = argmin L(f,g,πx) + Ω(g) con flechas indicando cada componente |
| `sampling_intuition.png` | Página 10 | Diagrama de boundary complejo con muestras ponderadas alrededor del punto de interés (cruz roja grande), línea punteada como aproximación lineal local |
| `sparse_linear.png` | Página 11 | Algorithm 1 box: Sparse Linear Explanations using LIME con pseudocódigo |
| `some_results.png` | Página 12 | Izquierda: Algorithm 2 word importance bar chart (Atheism). Derecha: Figure 4 - Inception explications para Electric guitar / Acoustic guitar / Labrador con imagen del perro/guitarra |
| `submodular_pick.png` | Página 14 | Izquierda: matriz de explicación W con filas (documentos) y columnas (features f1-f5). Derecha: Algorithm 2 pseudocódigo SP algorithm. Abajo: fórmula c(V,W,I) y Pick(W,I) en recuadro rojo |
| `simulated_faithful.png` | Páginas 16 | Figure 6 y Figure 7: gráficas de barras Recall (%) para random/parzen/greedy/LIME en Sparse LR y Decision Tree para Books y DVDs datasets |
| `simulated_trust.png` | Página 17 | Table 1: Average F1 of trustworthiness for Random/Parzen/Greedy/LIME sobre Books y DVDs para LR/NN/RF/SVM |
| `simulated_model.png` | Página 18 | Dos plots de líneas: % correct choice vs # of instances seen by user, con SP-LIME/RP-LIME/SP-greedy/RP-greedy para (a) Books y (b) DVDs |
| `human_classifier.png` | Página 20 | Gráfica de barras: % correct choice para greedy y LIME con Random Pick (azul) y Submodular Pick (naranja). Valores: greedy 68/80, LIME 75/89 |
| `human_improve.png` | Página 21 | Gráfica de líneas: Real world accuracy vs Rounds of interaction para SP-LIME (rojo), RP-LIME (azul), No cleaning (negro) |
| `husky_wolf.png` | Página 22 | (a) Husky classified as wolf (foto de husky), (b) Explanation (imagen gris con nieve visible). Table: Before/After para "Trusted the bad model" y "Snow as a potential feature" |
| `kernel_shap_plot.png` | Página 38 | Plot (A): Sample weight vs Subsets ordered by cardinality, comparando Shapley kernel (azul), LIME kernel cosine dist (verde oscuro), LIME kernel L2 dist (verde claro) en escala log |
| `class_diff.png` | Página 44 | (A) Grid de imágenes: Orig/DeepLift/New DeepLift/SHAP/LIME para Input/Explain 8/Explain 3/Masked. (B) Boxplot de Changes in log-odds |
