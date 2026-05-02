# Images to replace

| Archivo | Slide PDF (página) | Contenido |
|---|---|---|
| `jennifer_neuron.png` | 4 | Imagen de neurona con cara de Jennifer Aniston superpuesta |
| `jennifer_firing.png` | 5 | Grid de fotos y raster plots mostrando neurona que solo dispara para Jennifer Aniston |
| `visual_cortex.png` | 6 | Hubel/Wiesel (foto) + experimento con gato + jerarquía pixels→edges→parts→objects |
| `imagenet_error.png` | 7 | Bar chart ImageNet Top-5 Error (%) vs. año (AlexNet, VGG, GoogleNet, ResNet-152) |
| `broden_dataset.png` | 12 | 6 pares de imágenes del Broden dataset: street (scene), flower (object), headboard (part), swirly (texture), pink (color), metal (material) |
| `activation_map.png` | 13 | Diagrama: Input→Kernel→Output (activation map) + 32x32x3 → Convolution Layer → activation maps 28x28x6 |
| `scoring_pipeline.png` | 14 | Diagrama completo: imagen de entrada → CNN (congelado) → unit activation → A_k(x_1) → a_k (1D distribution) |
| `scoring_threshold.png` | 15 | Diagrama: a_k + T_k (m s.t. P(a_ij > m)=0.005) → A_k(x_1) bilinear upscaling → S_k(x_1) + T_k |
| `scoring_iou.png` | 16 | Diagrama: S_k(x_1) ≥ T_k → M_k(x_1) + L_c binary concept maps (Colors/Textures/Materials/Scenes/Parts/Objects) → IoU formula |
| `exp1_human_eval.png` | 20 | AMT interface: Task1 (write word), Task2 (mark images that don't correspond), Task3 (pick category) |
| `exp2_rotation.png` | 23 | Line chart: Number of unique detectors vs rotation (baseline, 0.2, 0.4, 0.6, 0.8, 1) por categoría (object, part, scene, material, texture, color) |
| `exp3_concepts_layer.png` | 24 | Izquierda: line charts AlexNet on Places205 e ImageNet por capa. Derecha: grid de ejemplos visuales por conv1-conv5 |
| `exp4_architectures.png` | 25 | Figura 7: stacked bars por arquitectura (ResNet152-Places365, ..., AlexNet-random) + Figura 8: stacked bars supervised vs self-supervised |
| `exp5_training.png` | 27 | Dos stacked bar charts: Number of unique detectors y Number of detectors para baseline/repeat1/2/3/NoDropout/BatchNorm |
| `exp6_scatter.png` | 29 | Scatter plot: Accuracy on action40 (x) vs Number of unique object detectors (y), puntos rojos (supervised) y verdes (self-supervised) |
| `exp7_width.png` | 31 | Dos stacked bar charts: unique detectors y detectors totales comparando AlexNet vs AlexNet-GAP-Wide por capa |
| `tcav_features_levels.png` | 35 | Tres grillas de imágenes: Low level features (bordes), Mid level features (partes de cara), High level features (caras completas) |
| `tcav_cash_machine.png` | 36 | Imagen de cash machine + saliency map + preguntas en amarillo (pixels, human, wheels, etc.) |
| `tcav_contributions.png` | 37 | (a) ejemplos de "striped" concept + (b) ejemplos de zebras en distintos estilos |
| `tcav_related_local_global.png` | 39 | Diagrama: boundary global (todo el espacio) → flecha → boundary local (zoom al punto de interés) |
| `tcav_related_saliency.png` | 40 | Tabla: Original Image + Gradient + SmoothGrad + Guided BackProp + Guided GradCAM + Integrated Gradients + ... para Junco Bird, Corn, Wheaten Terrier |
| `tcav_related_linearity.png` | 41 | Izquierda: PCA de word2vec (country/capital vectors). Derecha: cycleGAN Monet↔Photos, Zebras↔Horses, Summer↔Winter |
| `tcav_cav_definition.png` | 42 | Columna izquierda: 6 imágenes "Stripes" (P_C). Columna derecha: 6 imágenes "Not stripes" (N) — corgi, pepino, etc. |
| `tcav_cav_visualization.png` | 43 | Diagrama con X verdes y X rojas separadas por línea punteada, con flecha v_C^l perpendicular. Derecha: mismas imágenes de stripes/not-stripes |
| `tcav_approach_summary.png` | 46 | Diagrama completo del pipeline: (a) striped examples, (b) zebra examples, (c) NN con f_l y h_{l,k}, (d) activations + v_C^l, (e) S formula |
| `tcav_sorting_images.png` | 47 | Izquierda: "CEO concept" most/least similar striped images. Derecha: "Model Women concept" most/least similar necktie images |
| `tcav_insights.png` | 48 | 4 bar charts de TCAV scores en GoogleNet: Fire engine (red/yellow/blue/green), Zebra (zigzagged/striped/dotted), Rugby ball (latino/eastasian/african/caucasian), School bus (male_lfw/female_lfw/baby) |
| `tcav_where_learned.png` | 49 | Line chart: accuracies of linear classifiers (y) vs layer (mixed3a...logit) para grupos de conceptos (arms/lampshade, red/blue/green, striped/dotted, etc.) |
| `tcav_controlled.png` | 50 | Arriba: imágenes cab image / cab w caption / cucumber image / cucumber w caption. Abajo: 2 line charts (cab y cucumber): Accuracy + TCAV img + TCAV caption vs noise level |
| `tcav_saliency_eval.png` | 51 | Grid: rows = Models trained on (no captions / 0%/30%/100% noisy), cols = Vanilla gradient / Guided backprop / Integrated gradient / Smoothgrad |
| `tcav_human_eval.png` | 52 | Izquierda: SmoothGrad results (subject's perceived importance image vs caption). Centro: TCAV results (TCAV score image vs caption). Abajo: % questions subject rated very confident |
| `tcav_medical.png` | 53 | Arriba: Retina DR level 4 + TCAV bar chart (PRP/PRH-VH/NV-FP/VB). Abajo: Retina DR level 1 + TCAV bar chart (MA/HMA) + HMA distribution on predicted DR |
| `tcav_conclusions.png` | 54 | Diagrama TCAV approach summary repetido (a)(b)(c)(d)(e) — misma figura que approach summary |
