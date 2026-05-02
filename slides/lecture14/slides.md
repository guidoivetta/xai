---
title: "\\emoji{wtf} XAI Lecture 14"
subtitle: "Network Dissection \\& TCAV"
bibliography: references.bib

---

# Disclaimer

\input{../disclaimer.tex}

---

# Paper 1

\begin{center}
\Large \textbf{Network Dissection: Quantifying Interpretability of Deep Visual Representations}
\end{center}

\vspace{0.5cm}

\begin{center}
\textbf{Authors}: David Bau, Bolei Zhou, Aditya Khosla, Aude Oliva, Antonio Torralba (CSAIL, MIT)

\textbf{Presented by}: Anat Kleiman, Gustaf Ahdritz, Xin Tang, Luke Bailey
\end{center}

\vfill
[@bau2017network]

---

# Presentation Roadmap

- \textcolor{purple}{\textbf{Introduction}}
  - Motivation
  - Questions the paper aims to answer
  - Related works
- **Method**
- **Experiments**
  - Training Conditions
  - Discrimination
  - Layer Width

---

# How Is Semantic Visual Concept Represented in the Brain?

\begin{center}
\includegraphics[width=0.7\columnwidth]{imgs/jennifer_neuron.png}
\end{center}

---

# A Neuron That Only Fires for Jennifer Aniston

\begin{center}
\includegraphics[width=\columnwidth]{imgs/jennifer_firing.png}
\end{center}

---

# Disentangled Representation in Visual Cortex

\begin{center}
\includegraphics[width=\columnwidth]{imgs/visual_cortex.png}
\end{center}

---

# Deep CNN for Computer Vision

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/imagenet_error.png}
\end{center}

- Deeper and better — but what has been learned inside deep CNNs?
- Will CNNs exhibit a similar phenomenon to what we saw in the human brain?

---

# Proposed Questions

1. \textcolor{purple}{\textbf{What is a disentangled representation, and how can its factors be quantified and detected (in deep CNN)?}}

2. \textcolor{purple}{\textbf{Do interpretable hidden units reflect a special alignment of feature space, or are interpretations a chimera?}}

3. \textcolor{purple}{\textbf{What conditions in state-of-the-art training lead to representations with greater or lesser entanglement?}}

---

# Proposed Questions and Contributions

1. \textcolor{purple}{\textbf{What is a disentangled representation, and how can its factors be quantified and detected?}}
   - Proposed a metric, intersection over union score (IoU), to quantify the interpretability of each unit
   - The alignment level between unit activated area and human-interpretable concepts

2. \textcolor{purple}{\textbf{Do interpretable hidden units reflect a special alignment of feature space, or are interpretations a chimera?}}
   - A semantic concept can be detected by many units
   - A unit can detect many semantic concepts

3. \textcolor{purple}{\textbf{What conditions in state-of-the-art training lead to representations with greater or lesser entanglement?}}
   - Number of unique detectors, layer depth, training iterations
   - The angle of the images, input datasets
   - Fine-tuning, supervised vs. unsupervised

---

# Related Works

1. \textcolor{purple}{\textbf{Generative Visualizations of Individual Units}}
   - Mahendran et al., CVPR 2015
   - Nguyen et al., NIPS 2016
   - Simonyan et al., ICML 2014

2. \textcolor{purple}{\textbf{Salience-based Visualizations of Individual Units}}
   - Deconvolution: Zeiler et al., ECCV 2014

3. \textcolor{purple}{\textbf{Visualizing Representations as a Whole}}
   - t-SNE: Maaten et al., JMLR, 2008
   - prototype autoencoder: Li et al., AAAI, 2018
   - Yosinski et al., ICML, 2015

\vspace{0.3cm}
\footnotesize Limitation: qualitative analyses, cannot be used for comparison between models.

---

# Method

---

# Broden: Broadly and Densely Labeled Dataset

- Combination of multiple datasets with segmentation and image-wide labels

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/broden_dataset.png}
\end{center}

- Multiple labels can apply to the same pixel (e.g., "cat, leg, black")

---

# Scoring Unit Interpretability

Unit is a convolutional filter

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/activation_map.png}
\end{center}

---

# Scoring Unit Interpretability

\begin{center}
\includegraphics[width=\columnwidth]{imgs/scoring_pipeline.png}
\end{center}

---

# Scoring Unit Interpretability

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/scoring_threshold.png}
\end{center}

Threshold $T_k$: value $m$ such that $P(a^{ij}_k > m) = 0.005$

---

# Scoring Unit Interpretability

\begin{center}
\includegraphics[width=\columnwidth]{imgs/scoring_iou.png}
\end{center}

$$IoU_{k,c} = \frac{\sum |M_k(\mathbf{x}) \cap L_c(\mathbf{x})|}{\sum |M_k(\mathbf{x}) \cup L_c(\mathbf{x})|}$$

---

# Scoring Unit Interpretability

$$IoU_{k,c} = \frac{\sum |M_k(\mathbf{x}) \cap L_c(\mathbf{x})|}{\sum |M_k(\mathbf{x}) \cup L_c(\mathbf{x})|}$$

- Changing $IoU$ threshold changes number of concept detectors but not orderings between networks
- One unit might be a detector for multiple concepts; they choose the top-ranked concept for an individual unit
- Interpretability of a layer = number of unique concepts aligned with units

---

# Experiments

---

# Experiments: Tested CNN Models

| **Training** | **Network** | **Data set or task** |
|---|---|---|
| none | AlexNet | random |
| Supervised | AlexNet | ImageNet, Places205, Places365, Hybrid |
| Supervised | GoogLeNet | ImageNet, Places205, Places365 |
| Supervised | VGG-16 | ImageNet, Places205, Places365, Hybrid |
| Supervised | ResNet-152 | ImageNet, Places365 |
| Self | AlexNet | context, puzzle, egomotion, tracking, moving, videoorder, audio, crosschannel, colorization, objectcentric |

\footnotesize Places: scene-centric dataset with categories such as kitchen, living room, coast.

---

# Experiment 1: Human Evaluation of Interpretations

1. **Identify Interpretable Units** — units that raters agreed with ground-truth interpretations
2. Raters shown 15 images with highlighted patches showing the most highly-activating regions for each unit in AlexNet trained on Places205, and asked to decide (yes/no) whether a given phrase describes most of the image patches
3. **Find Network Dissection** — portion of interpretations generated by method that were rated as descriptive
4. **Human Consistency** — portion of ground-truth labels found descriptive by a second group of raters

\begin{center}
\includegraphics[width=0.7\columnwidth]{imgs/exp1_human_eval.png}
\end{center}

---

# Experiment 1: Human Evaluation Results

\vspace{0.3cm}

| | conv1 | conv2 | conv3 | conv4 | conv5 |
|---|---|---|---|---|---|
| Interpretable units | 57/96 | 126/256 | 247/384 | 258/384 | 194/256 |
| Human consistency | 82% | 76% | 83% | 82% | 91% |
| Network Dissection | 37% | 56% | 54% | 59% | 71% |

\vspace{0.3cm}
\begin{exampleblock}{}
Network Dissection agreement increases in higher layers; Human consistency remains high throughout.
\end{exampleblock}

---

# Experiment 2: Axis-Aligned Interpretability

Two hypotheses:

1. \textcolor{purple}{\textbf{Concepts appear in every direction}}
   - **Default hypothesis:** single units not much more interpretable than combinations of units

2. \textcolor{purple}{\textbf{Concepts are rare + the model converges to a special, semantically rich basis}}
   - The model's natural basis is a meaningful decomposition

---

# Experiment 2: Axis-Aligned Interpretability

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/exp2_rotation.png}
\end{center}

Number of unique detectors decreases as the basis is rotated — confirming hypothesis 2.

---

# Experiment 3: Concepts by Layer

\begin{center}
\includegraphics[width=\columnwidth]{imgs/exp3_concepts_layer.png}
\end{center}

---

# Experiment 4: Network Architectures

\begin{center}
\includegraphics[width=\columnwidth]{imgs/exp4_architectures.png}
\end{center}

---

# Experiment 5: Training Conditions

Varied training conditions:

1. \textcolor{purple}{\textbf{Weight Initializations}}
   - **Minimal Effect:** Models converge to similar levels of interpretability

2. \textcolor{purple}{\textbf{Dropout}}
   - **Some Effect:** Lack of dropout leads to more "texture" and less "object" detectors

3. \textcolor{purple}{\textbf{Batch Normalization}}
   - **Significant Effect:** Interpretability decreased significantly

---

# Experiment 5: Training Conditions

\begin{center}
\includegraphics[width=\columnwidth]{imgs/exp5_training.png}
\end{center}

---

# Experiment 6: Discrimination

\textcolor{purple}{\textbf{Benchmark high-level activations on a new task:}}

- Across several Deep NNs, extract activations from high CNN layers
- Train a linear SVM on a new *action recognition* task
- Compute classification accuracy

---

# Experiment 6: Discrimination Results

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/exp6_scatter.png}
\end{center}

\textcolor{purple}{\textbf{Result:}} Positive correlation between object detectors and classification accuracy $\rightarrow$ encouraging **concept detection** can improve **discrimination**.

---

# Experiment 7: Width

\textcolor{purple}{\textbf{Effect of layer width (number of units in a layer):}}

Increased layer width retains similar accuracy, but many more **concept detectors**

- \# Detectors increased both at the increased layer and in the network generally
- Increase has a threshold

---

# Experiment 7: Width Results

\begin{center}
\includegraphics[width=\columnwidth]{imgs/exp7_width.png}
\end{center}

---

# Discussion Questions (Paper 1)

1. \textcolor{purple}{\textbf{Distribution Understanding:}} Concept detectors from a particular dataset betray something about the underlying distribution. How do you think this can be applied in the real world (e.g., bias detection)?

2. \textcolor{purple}{\textbf{Single unit to circuit:}} This method interprets single units; could it be extended to larger circuits and would this be useful?

3. \textcolor{purple}{\textbf{Beyond vision:}} This method is deeply tied to the vision domain. Could it be extended to other domains such as natural language?

---

# Paper 2

\begin{center}
\Large \textbf{Interpretability Beyond Feature Attribution: Quantitative Testing with Concept Activation Vectors (TCAV)}
\end{center}

\vspace{0.5cm}

\begin{center}
\textbf{Authors}: Kim et al. (2018)

\textbf{Presented by}: Lucia Gordon, Matthew Nazari, Catherine Yeh
\end{center}

\vfill
[@kim2018interpretability]

---

# Thoughts on Concept-Based Explanations So Far?

\begin{center}
\vspace{2cm}
\Large Thoughts on \textcolor{orange}{\textbf{Concept-Based}} Explanations So Far?
\end{center}

---

# Motivation + Problem Statement

- Interpreting deep learning models is crucial to understanding their behavior, ensuring accurate predictions, and reflecting our values
- But remains a big challenge due to size, complexity, and opacity of ML models
- Many systems operate on **low-level features** (e.g., pixel values) rather than \textcolor{red}{\textbf{high-level concepts}} (e.g., face) that are human-interpretable

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/tcav_features_levels.png}
\end{center}

---

# Motivation + Problem Statement

\begin{columns}
\begin{column}{0.55\textwidth}

\begin{center}
\includegraphics[width=\columnwidth]{imgs/tcav_cash_machine.png}
\end{center}

\end{column}
\begin{column}{0.45\textwidth}

**Problem:**
- We can't express these concepts as pixels
- And they weren't our input features

\end{column}
\end{columns}

---

# Summary of Contributions

- Introduce \textcolor{orange}{\textbf{Concept Activation Vectors (CAVs)}}: way to interpret a neural network's internal state in terms of human-friendly concepts
- Key idea is to use the high-dimensional internal state of a neural net as an aid, not an obstacle
- Main contribution: \textcolor{orange}{\textbf{Testing with CAV (TCAV)}}, that quantifies model sensitivity to a high-level concept learned by a CAV for a particular class

\begin{center}
\includegraphics[width=0.7\columnwidth]{imgs/tcav_contributions.png}
\end{center}

---

# Goals of TCAV

- \textcolor{blue}{\textbf{Accessibility:}} requires little to no ML expertise
- \textcolor{red}{\textbf{Customization:}} adaptable to any concept, even outside of training
- \textcolor{orange}{\textbf{Plug-in readiness:}} works without retraining/modifying ML models
- \textcolor{olive}{\textbf{Global quantification:}} can interpret entire classes with a single quantitative measure

\vspace{0.5cm}

\begin{center}
$\downarrow$

\textbf{Assessed with experiments + human evaluation}
\end{center}

---

# Related Work: Interpretability Methods

\textbf{Interpretability methods:}

- *Inherently interpretable* models vs. *post-hoc* explanations (Kim et al., 2014; Doshi-Velez et al., 2015; Goodman \& Flaxman, 2016)
- \textcolor{red}{\textbf{Perturbation-based methods:}} e.g., LIME/SHAP (Ribeiro et al., 2016; Lundberg \& Lee, 2017)
  - *local* vs. *global*

\begin{center}
\includegraphics[width=0.6\columnwidth]{imgs/tcav_related_local_global.png}
\end{center}

---

# Related Work: Saliency Limitations

**Interpretability methods in neural networks**

- Limitations of **saliency methods**:
  - Local explanation (Erhan et al., 2009; Smilkov et al., 2017)
  - Lack customization
  - Vulnerable to adversarial attacks (Ghorbani et al., 2017)
  - Insensitivity to randomization (Adebayo et al., 2018)

\begin{center}
\includegraphics[width=0.7\columnwidth]{imgs/tcav_related_saliency.png}
\end{center}

---

# Related Work: Linearity + Latent Dimensions

**Linearity in neural network + latent dimensions**

- Meaningful information can be learned from simple *linear* classifiers (Bau et al., 2017; Alain \& Bengio, 2016)
- Mapping *latent* dimensions to human *concepts* (Mikolov et al., 2013; Zhu et al., 2017)

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/tcav_related_linearity.png}
\end{center}

---

# Approach: Defining the CAV

\begin{columns}
\begin{column}{0.55\textwidth}

Consider the fully connected layer $f_l : \mathbb{R}^n \rightarrow \mathbb{R}^m$ and the concept of interest $C$

- Collect a set of examples $P_C$ of that concept and a negative set $N$ of examples that don't

- Define the CAV to be a vector orthogonal to a decision boundary between activations $\{f_l(\mathbf{x}) : \mathbf{x} \in P_C\}$ and $\{f_l(\mathbf{x}) : \mathbf{x} \in N\}$

\end{column}
\begin{column}{0.45\textwidth}

\begin{center}
\includegraphics[width=\columnwidth]{imgs/tcav_cav_definition.png}
\end{center}

\end{column}
\end{columns}

---

# Approach: Visualizing the CAV

\begin{columns}
\begin{column}{0.55\textwidth}

\begin{center}
\includegraphics[width=\columnwidth]{imgs/tcav_cav_visualization.png}
\end{center}

\end{column}
\begin{column}{0.45\textwidth}

The CAV $\mathbf{v}_C^l$ is the normal to the linear decision boundary separating:

- $\in \{f_l(x) : x \in P_C\}$ (concept examples)
- $\in \{f_l(x) : x \in N\}$ (non-examples)

\end{column}
\end{columns}

---

# Approach: Gauging "Concept Sensitivity"

Saliency maps gauge sensitivity of $h_k(\mathbf{x})$ with respect to per-pixel perturbations:

$$S_{C,k,l}(\mathbf{x}) = \nabla h_{l,k}(f_l(\mathbf{x})) \cdot \mathbf{v}_C^l$$

With CAV, we can gauge sensitivity of $h_{l,k}(f_l(\mathbf{x}))$ \textcolor{red}{\textbf{towards a concept}} at an entire layer.

---

# Approach: Testing with CAV (TCAV)

$$\text{TCAV}_{Q_{C,k,l}} = \frac{|\{\mathbf{x} \in X_k : S_{C,k,l}(\mathbf{x}) > 0\}|}{|X_k|}$$

- $\text{TCAV}_{Q_{C,k,l}}$ measures the fraction of inputs whose activations were influenced by a concept
- This provides interpretation global to a particular class
- A $t$-test can safeguard against meaningless CAVs

---

# Approach Summary

\begin{center}
\includegraphics[width=\columnwidth]{imgs/tcav_approach_summary.png}
\end{center}

---

# Results: Sorting Images with CAVs

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/tcav_sorting_images.png}
\end{center}

- Confirmation that the CAVs correctly reflect the concept of interest
- Sorting procedure can reveal biases used to learn the CAV

---

# Results: Gaining Insights with TCAV

\begin{columns}
\begin{column}{0.5\textwidth}

\begin{center}
\includegraphics[width=\columnwidth]{imgs/tcav_insights.png}
\end{center}

\end{column}
\begin{column}{0.5\textwidth}

- Matches intuition: "Red" important for "fire engine"; "Striped" important for "zebra"
- **Biases:** "Caucasian" important for "rugby ball"
- Statistical significance test successfully removed spurious CAVs ("Dotted" not important for "zebra")

\end{column}
\end{columns}

---

# Results: TCAV for Where Concepts Are Learned

\begin{columns}
\begin{column}{0.45\textwidth}

- Simple concepts (colors, patterns) reach high accuracy at **low layers**
- Complex concepts (age, sex, objects) don't reach high accuracy until **higher layers**
- Confirming past findings: lower layers = feature detectors, higher layers = classifiers

\end{column}
\begin{column}{0.55\textwidth}

\begin{center}
\includegraphics[width=\columnwidth]{imgs/tcav_where_learned.png}
\end{center}

\end{column}
\end{columns}

---

# Results: Controlled Experiment with Ground Truth

\begin{center}
\includegraphics[width=\columnwidth]{imgs/tcav_controlled.png}
\end{center}

- **Cab:** image concept more important than caption regardless of noise
- **Cucumber:** caption concept more important when caption is likely to appear
- TCAV reflects ground truth: only image important → high accuracy; only caption important → low accuracy

---

# Results: Evaluation of Saliency Maps

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/tcav_saliency_eval.png}
\end{center}

\textcolor{orange}{For "cab" the "image" concept is most important, but this is \textbf{not} reflected in saliency maps $\rightarrow$ superiority of TCAV.}

---

# Results: Saliency Maps vs. Human Subjects

\begin{center}
\includegraphics[width=\columnwidth]{imgs/tcav_human_eval.png}
\end{center}

- Subjects incorrectly thought the caption was more important than the image
- Subjects could not discern a difference in importance between image and caption
- TCAV score correctly reflects which concept is most important
- \textbf{Saliency maps are misleading!}

---

# Results: TCAV for a Medical Application

\begin{center}
\includegraphics[width=\columnwidth]{imgs/tcav_medical.png}
\end{center}

- TCAV score shows model successfully distinguishes relevant and irrelevant concepts for level 4 DR diagnosis
- TCAV score reveals model gives too much importance to HMA concept for level 1 diagnosis → use this to **debug the model**

---

# Conclusions

\begin{columns}
\begin{column}{0.5\textwidth}

- \textcolor{red}{\textbf{Roadmap:}} Gradient $\rightarrow$ Attention $\rightarrow$ Concept based approaches (\textcolor{orange}{\textbf{TCAV!}})
- \textcolor{red}{\textbf{Limitations:}}
  - Evaluated only on computer vision tasks
  - Statistical significance testing — is this rigorous?

\end{column}
\begin{column}{0.5\textwidth}

\begin{center}
\includegraphics[width=\columnwidth]{imgs/tcav_conclusions.png}
\end{center}

\end{column}
\end{columns}

---

# Discussion Questions (Paper 2)

- How does this method compare to e.g., saliency maps?
- How would you adapt TCAV for other types of data (e.g., audio/video) and what would that look like?
- Thoughts on TCAV for adversarial example identification (Appendix A)?
- Do you think there could be adversarial images that allow meaningless CAVs to pass the statistical significance test?

---

\begin{center}
\Huge Thank You!
\end{center}

---

# References {.allowframebreaks}

\footnotesize
