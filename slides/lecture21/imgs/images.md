# Images to extract from Lecture_21.pdf

| Archivo | Slide PDF (página) | Contenido |
|---|---|---|
| mech_title.png | 1 | Título: "Open Problems in Mechanistic Interpretability: A Whirlwind Tour" — Neel Nanda |
| mech_motivation.png | 2 | Motivation slide con dibujo de neurociencia/cerebro y gráfico de fase |
| mech_captcha.png | 3 | Ejemplo ARC: modelo mensajea TaskRabbit worker para resolver CAPTCHA — razona "I should not reveal that I am a robot" |
| mech_transformer.png | 5 | Diagrama de Transformer: tokens → embed → residual stream → attention heads h0,h1 → MLP m → unembed → logits |
| mech_car_detector.png | 7 | Circuito car detector: Windows/Car Body/Wheels → car detector (Olah et al) |
| mech_growing_area1.png | 8 | Mosaico de 6 papers de mech. interp.: Mathematical Framework, Key-Value Memories, Localization Editing, Gender Bias, Toy Models of Superposition, ROME |
| mech_growing_area2.png | 9 | Mosaico de 6 papers más: Multimodal Neurons, Compositional Explanations, Causal Abstractions, SGD Learns Parities, Curve Circuits, Quantization Model |
| mech_multimodal_neurons.png | 11 | Grid de neuronas multimodales: Region, Person, Emotion, Religion, Person Trait, Art Style (Goh et al) |
| mech_number_feature.png | 12 | Dataset examples con "NUMBER (implicitly of people)" resaltado: 150, six, 70, 40 (Softmax Linear Units, Elhage et al) |
| mech_neuroscope.png | 13 | Tool Neuroscope: ejemplos de dataset para el token "in the" |
| mech_induction_heads.png | 14 | Diagrama de Induction Head: "Category 40 ids node struction ... node" — prefix matching + copy |
| mech_induction_illustrated.png | 15 | Induction Heads Illustrated: diagrama Layer 0 + Layer 1 con key/query/value/output (Callum McDougall) |
| mech_in_context_learning.png | 16 | Gráficos de in-context learning: modelos 1L/2L/3L — mejora abrupta + induction heads en phase change (Olsson et al) |
| mech_grokking.png | 18 | Plot grokking: Modular Division — train accuracy sube rápido, val accuracy mucho después (Power et al) |
| mech_modular_addition.png | 19 | Circuito Modular Addition: diagrama con fórmulas trig, Logit(c) ∝ cos(w(a+b-c)), círculos Fourier (Nanda et al) |
| mech_polysemanticity.png | 21 | Neurona "game" de Multimodal Neurons: responde a juegos/dados, poesía/libros, ficción (polysemanticity) |
| mech_superposition.png | 22 | Hipótesis superposición: 0% sparsity (ortogonal), 80% (antipodal pairs), 90% (pentágono) (Elhage et al) |
| mech_geometry_superposition.png | 23 | Feature Geometry Graph: Dedicated Dimension → Tetrahedron → Triangle → Digon → Pentagon → Square Antiprism |
| mech_ioi_circuit.png | 24 | Circuito IOI (Indirect Object Identification): IO/S1/S2/END → Previous Token Heads → Duplicate → Induction → S-Inhibition → Name Movers (Wang et al) |
| mech_ablations.png | 25 | Scatter plot: Original vs Post-Ablation Direct Logit Attribution — Backup Head y Negative Backup Head |
| mech_activation_patching.png | 26 | Activation Patching: diagrama clean/corrupted runs, patch one activation (ROME, Meng et al) |
| mech_linear_representation.png | 28 | Linear Representation Hypothesis: word2vec king/queen (Male-Female) y walking/walked (Verb tense) |
| mech_othello_gpt.png | 29 | Emergent World Representations in Othello-GPT: board state pre/post intervention (Li et al) |
| mech_othello_linear.png | 30 | Othello-GPT's Linear Model of Board State: "My colour vs their's" — Probe Output visualization (Nanda) |
