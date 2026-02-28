# Images to extract from Lecture_8.pdf

| Archivo | Slide PDF | Contenido |
|---|---|---|
| `smoothgrad_paper.png` | Página 1 | Slide de título: "SmoothGrad: removing noise by adding noise", Authors: Daniel Smilkov et al., Presented by: Vignav Ramesh, Zelin Li, Paul Liu |
| `motivation_gazelle.png` | Página 2 | Columna derecha: foto de gacela con etiqueta "Image" arriba, y mapa de sensibilidad en escala de grises con etiqueta "Sensitivity map M_c" abajo |
| `lime_perturbation.png` | Página 4 | Diagrama LIME: región rosada y azul (decision boundary), línea punteada diagonal, puntos de muestras con pesos (cruces rojas y círculos azules de distintos tamaños) |
| `backprop_network.png` | Página 5 | Red neuronal: nodo verde (Output) arriba, capas de nodos azules con conexiones rojas, nodos amarillos (inputs) abajo con etiqueta "Yellow = inputs" |
| `noisy_gradients_plot.png` | Página 8 | Centro: plot con 3 líneas (rojo/verde/azul) mostrando ∂S_c/∂x_i(x + tε) vs t (0.0 a 1.0). A los lados: dos fotos de gacelas en sabana |
| `hyperparams_sigma.png` | Página 12 | Grid de mapas de sensibilidad: 3 filas (3 gacelas distintas) × 6 columnas (Noise level: 0%, 5%, 10%, 20%, 30%, 50%). Imagen original en la primera columna |
| `hyperparams_n.png` | Página 13 | Fila de mapas de sensibilidad: imagen de gacela original + 5 mapas a Sample size n: 2, 5, 20, 50, 100. Caption: "Figure 4. Effect of sample size on the estimated gradient for inception. 10% noise was applied to each image." |
| `visual_coherence_fig5.png` | Página 17 | Figure 5: Grid comparativo. Columnas: Vanilla / Integrated / Guided BackProp / SmoothGrad (con borde rojo), en dos grupos (Gradient y Gradient × Image). Filas: High Impact (drilling platform, great white shark, hognose snake) y Low Impact (night snake, lorikeet, coyote) |
| `discriminativity_fig6.png` | Página 18 | Figure 6: Grid discriminativity. Columnas: VanillaGrad / IntegGrad / GuidedBackProp / SmoothGrad (borde rojo). Filas: foto de perro+gato (EntlerBucher-tiger cat arriba, bull mastiff-tiger cat abajo). Mapa de colores azul-gris-rojo |
| `combining_methods.png` | Página 20 | Figure 7: Grid comparativo. Columnas: Integrated / Integrated+Smooth (borde rojo) / GuidedBackProp / GuidedBackProp+Smooth (borde rojo). Filas: desktop computer, knee pad, soap dispenser, lighter |
| `ig_paper.png` | Página 23 | Slide de título: "Axiomatic Attribution for Deep Networks", Presented by Alex Lin, Steve Li, Kevin Huang. Autores: Mukund Sundararajan, Ankur Taly, Qiqi Yan |
| `ig_mnist_attribution.png` | Página 24 | Grid superior derecho: 4 filas (dígitos 5, 9, 8, 6) × 5 columnas (imagen original + 4 variantes con overlay de attribution en azul/rojo), con barra de colores |
| `ig_break_sensitivity.png` | Página 28 | Izquierda: arquitectura DeConvNet (CNN + Deconvolution network en espejo). Derecha: matrices forward pass (f^l, f^{l+1} con ReLU) y backward pass guided backpropagation con anotación "The gradients for both the red and yellow neurons are not backpropagated." |
| `ig_break_invariance.png` | Página 29 | Izquierda: grid de atribuciones DeepLift para dígitos MNIST (grid negro con patches grises). Derecha: grafo LRP con nodos y flechas + 4 fórmulas del forward/backward pass (z_k, s_k, c_j, R_j) |
| `ig_path_methods.png` | Página 32 | Figure 1: Plot con dos puntos (r_1,r_2) abajo izquierda y (s_1,s_2) arriba derecha, con tres caminos P_1 (rojo), P_2 (verde, straight line), P_3 (azul/verde). Caption completo |
| `ig_object_recognition.png` | Página 35 | Grid de resultados CNN: 6 ejemplos (reflex camera, fireboat, school bus, mosque, viaduct, cabbage butterfly). Para cada uno: foto original + predicción + Integrated Grad. + Grad at Image |
| `ig_question_classification.png` | Página 36 | Texto con palabras coloreadas en rojo (positive attribution) / azul (negative) / gris (neutral). 9 preguntas con predicciones [NUMERIC, STRING, DATETIME, YESNO]. Leyenda al pie |
| `ig_machine_translation.png` | Página 37 | Izquierda: arquitectura RNN Encoder-Decoder "He loved to eat" → "Er liebte zu essen". Derecha: heatmap de attribution (matriz 10×7 con valores y colores rojo/azul, barra de colores -0.6 a 0.6) |
| `ig_ligand_screening.png` | Página 38 | Molécula CID1562745 (izquierda), Attribution summary box (centro), Atom attribution heatmap (arriba derecha), Bond and D2-pair attribution heatmap (abajo derecha) |
