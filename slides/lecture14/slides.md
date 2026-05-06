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


:::: columns
::: {.column width="50%"}
\begin{center}
\includegraphics[width=\columnwidth]{imgs/jennifer_neuron.png}
\end{center}
:::
::: {.column width="50%"}
Neuroscientists have found that the brain uses sparse, localized representations: individual neurons (or small groups) respond selectively to specific concepts.
\begin{block}{Key Observation}
Some neurons fire strongly for one concept and weakly for almost everything else — a property called \textbf{selectivity}.
\end{block}
Question: Do deep neural networks learn similar structure?
:::
::::

---

# A Neuron That Only Fires for Jennifer Aniston
:::: columns
::: {.column width="55%"}
\begin{center}
\includegraphics[width=\columnwidth]{imgs/jennifer_firing.png}
\end{center}
:::
::: {.column width="45%"}
Quiroga et al. (2005) recorded neurons in the human medial temporal lobe and found neurons that fire exclusively for specific people or landmarks.

- One neuron fired for Jennifer Aniston — photos, drawings, even her name written in text
- Another neuron fired only for the Eiffel Tower

\begin{alertblock}{Why this matters}
This is a \textbf{disentangled} representation: one neuron = one concept. The paper asks whether CNNs learn something analogous.
\end{alertblock}
:::
::::

---

# Disentangled Representation in Visual Cortex

:::: columns
::: {.column width="55%"}
\begin{center}
\includegraphics[width=\columnwidth]{imgs/visual_cortex.png}
\end{center}
:::
::: {.column width="45%"}
The visual cortex processes information in a hierarchy of layers:

- V1: edges and orientations
- V2/V4: textures, colors, shapes
- IT (inferotemporal cortex): objects and faces

Each area builds on the previous one — low-level features combine into high-level concepts.
\begin{block}{Analogy}
This layered specialization is the biological inspiration for deep CNNs. Do CNNs also develop specialized detectors at each layer?
\end{block}
:::
::::

---

# Deep CNN for Computer Vision

:::: columns
::: {.column width="55%"}
\begin{center}
\includegraphics[width=\columnwidth]{imgs/imagenet_error.png}
\end{center}
:::
::: {.column width="45%"}
CNNs revolutionized computer vision, reaching superhuman performance on ImageNet — but they remain largely opaque.

- Units in early layers respond to edges and colors
- Units in later layers seem to respond to objects and scenes (Zhou et al., 2015)
- But this was observed qualitatively — no rigorous measurement existed

\begin{alertblock}{The gap}
We know CNNs \textit{work} extremely well. We don't know \textit{why}, or what exactly each unit has learned.
\end{alertblock}
:::
::::

---

# Proposed Questions

The paper frames the problem around three concrete research questions. Each has a direct answer by the end of the paper.

1. \textcolor{purple}{\textbf{What is a disentangled representation, and how can its factors be quantified and detected (in deep CNN)?}}
2. \textcolor{purple}{\textbf{Do interpretable hidden units reflect a special alignment of feature space, or are interpretations a chimera?}}

3. \textcolor{purple}{\textbf{What conditions in state-of-the-art training lead to representations with greater or lesser entanglement?}}

---

# Proposed Questions and Contributions

\textcolor{purple}{\textbf{What is a disentangled representation, and how can its factors be quantified and detected?}}

- Proposed a metric, intersection over union score (IoU), to quantify the interpretability of each unit
- The alignment level between unit activated area and human-interpretable concepts


\textcolor{purple}{\textbf{Do interpretable hidden units reflect a special alignment of feature space, or are interpretations a chimera?}}

- A semantic concept can be detected by many units
- A unit can detect many semantic concepts


\textcolor{purple}{\textbf{What conditions in state-of-the-art training lead to representations with greater or lesser entanglement?}}

- Number of unique detectors, layer depth, training iterations
- The angle of the images, input datasets
- Fine-tuning, supervised vs. unsupervised

# Related Works
 
Prior work tried to understand CNN internals through **visualization**, but all approaches share a fundamental limitation: they are qualitative and cannot be used to rigorously compare models.
 
1. \textcolor{purple}{\textbf{Generative Visualizations of Individual Units}}
   - Synthesize images that maximally activate a unit
   - Mahendran et al., CVPR 2015; Nguyen et al., NIPS 2016; Simonyan et al., ICML 2014
2. \textcolor{purple}{\textbf{Salience-based Visualizations of Individual Units}}
   - Highlight which pixels most contribute to a unit's activation
   - Deconvolution: Zeiler et al., ECCV 2014
3. \textcolor{purple}{\textbf{Visualizing Representations as a Whole}}
   - Project the full representation space into 2D for inspection
   - t-SNE: Maaten et al., JMLR, 2008; Yosinski et al., ICML, 2015
\vspace{0.3cm}
\begin{alertblock}{Common limitation}
All these methods produce images that \textbf{humans} must then interpret — subjective and impossible to compare across networks.
\end{alertblock}
 
---

# Related Works: The Need for Quantification

Prior work focused on **visualizing** internals, but these methods remain qualitative and subjective.

1. **Generative Visualizations**: Synthesizing images that maximize activation (e.g., Activation Maximization).
2. **Salience-based Methods**: Highlighting pixels that contribute most to a prediction (e.g., Deconvolution).
3. **Global Analysis**: Visualizing the representation space as a whole (e.g., t-SNE).

\begin{alertblock}{The Semantic Gap}
Visualizations still require a \textbf{human} to interpret the resulting images. Network Dissection aims to automate this by matching units with labeled concepts directly.
\end{alertblock}

---
 
# Method
 
---
 
# Broden: Broadly and Densely Labeled Dataset
 
To measure interpretability we need a **ground truth** of human concepts. Broden unifies five existing segmentation datasets into a single resource.
 
:::: columns
::: {.column width="55%"}
 
*broden dataset*
 
:::
::: {.column width="45%"}
 
| Category | \# Classes |
|---|---|
| Scene | 468 |
| Object | 584 |
| Part | 234 |
| Material | 32 |
| Texture | 47 |
| Color | 11 |
 
Multiple labels can apply to the **same pixel** (e.g., a black cat leg $\rightarrow$ "cat", "leg", "black")
 
\begin{block}{}
The range from colors to scenes allows testing interpretability at \textbf{all levels of abstraction}.
\end{block}
 
:::
::::


---

# Scoring Unit Interpretability: The Process

The method evaluates every convolutional unit $k$ as a solution to a **binary segmentation task** for every concept $c$.

1. **Activation Collection**: Extract the activation map $A_k(x)$ from the frozen network.
2. **Quantile Thresholding**: Define a threshold $T_k$ such that $P(a_k > T_k) = 0.005$ over the dataset. This identifies the "top" activations.
3. **Resolution Alignment**: Since $A_k(x)$ is lower resolution, use **bilinear interpolation** to upsample it to $S_k(x)$.
4. **Binary Mask**: Generate $M_k(x) \equiv S_k(x) \geq T_k$, selecting regions where the unit is "active".

\vfill
\begin{center}
\textit{This is a direct probe; no training or backpropagation is required.}
\end{center}

---
 
# Scoring Unit Interpretability
 
Each convolutional unit $k$ acts like a **filter** that fires on certain spatial regions of an image. The core idea: treat each unit as a candidate **segmentation model** for some concept.
 
:::: columns
::: {.column width="55%"}
 
*activation map*
 
:::
::: {.column width="45%"}
 
**Pipeline (no retraining needed):**
 
1. Feed images from Broden through the frozen CNN
2. Collect activation map $A_k(\mathbf{x})$ for every unit $k$
3. Upsample $A_k(\mathbf{x})$ to input resolution
4. Threshold to obtain a binary mask $M_k(\mathbf{x})$
5. Compare $M_k(\mathbf{x})$ against concept labels $L_c(\mathbf{x})$
:::
::::
 
---
 
# Scoring Unit Interpretability: Full Pipeline
 
*scoring pipeline*
 
For each unit, the method evaluates its activation mask against all **1,197 segmentation tasks** in Broden (one per concept). The unit is assigned the concept with the highest score.
 
---

# Scoring Unit Interpretability
 
*scoring threshold*
 
Threshold $T_k$: value $m$ such that $P(a^{ij}_k > m) = 0.005$
 
---
 
# Scoring Unit Interpretability
 
*scoring iou*
 
$$IoU_{k,c} = \frac{\sum |M_k(\mathbf{x}) \cap L_c(\mathbf{x})|}{\sum |M_k(\mathbf{x}) \cup L_c(\mathbf{x})|}$$

---

# Quantifying Alignment: The IoU Score

The interpretability of unit $k$ for concept $c$ is the **Intersection over Union (IoU)** across the dataset:

$$IoU_{k,c} = \frac{\sum |M_k(x) \cap L_c(x)|}{\sum |M_k(x) \cup L_c(x)|}$$

- **Detector Definition**: A unit $k$ is considered a detector for concept $c$ if $IoU_{k,c} > 0.04$.
- **Top Label**: If a unit matches multiple concepts, the top-ranked label is assigned.
- **Layer Score**: The interpretability of a layer is the number of **unique** semantic concepts aligned with its units.

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

The paper evaluates interpretability across diverse architectures and training regimes to identify which conditions favor disentangled representations.
 
| **Training** | **Network** | **Data set or task** |
|---|---|---|
| none | AlexNet | random |
| Supervised | AlexNet | ImageNet, Places205, Places365, Hybrid |
| Supervised | GoogLeNet | ImageNet, Places205, Places365 |
| Supervised | VGG-16 | ImageNet, Places205, Places365, Hybrid |
| Supervised | ResNet-152 | ImageNet, Places365 |
| Self | AlexNet | context, puzzle, egomotion, tracking, moving, videoorder, audio, crosschannel, colorization, objectcentric |
 
\footnotesize Places: scene-centric dataset with categories such as kitchen, living room, coast.

\begin{block}{Scene-centric vs. Object-centric}
Models trained on **Places** (scenes) generally develop more object detectors than those trained on **ImageNet** (objects).
\end{block}
 
---
 
# Experiment 1: Human Evaluation of Interpretations
 
1. **Identify Interpretable Units** — units that raters agreed with ground-truth interpretations
2. Raters shown 15 images with highlighted patches showing the most highly-activating regions for each unit in AlexNet trained on Places205, and asked to decide (yes/no) whether a given phrase describes most of the image patches
3. **Find Network Dissection** — portion of interpretations generated by method that were rated as descriptive
4. **Human Consistency** — portion of ground-truth labels found descriptive by a second group of raters
*exxp1_human_eval*

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


Is interpretability an "axis-aligned" property of the natural basis, or do concepts appear in every direction?

- **Method**: Apply a random orthogonal rotation $Q$ to the representation space.
- **Result**: Rotating the basis drastically reduces the number of unique detectors (up to 80% decrease).
- **Conclusion**: Interpretability is **not** an inevitable result of discriminative power. It is a special alignment learned by the network.

---
 
# Experiment 2: Axis-Aligned Interpretability
 
*exp2_rotation*
 
Number of unique detectors decreases as the basis is rotated — confirming hypothesis 2.


---
 
# Experiment 3: Concepts by Layer
 
*exp_3*
 
---
 
# Experiment 4: Network Architectures
 
*exp_4*
 
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
 
*exp_5*
 
---

# Experiment 6: Discrimination vs. Interpretability

Does being more "interpretable" make a model better at other tasks?

- **Task**: Use high-level activations to train a linear SVM for *action recognition* (Action40 dataset).
- **Finding**: There is a **positive correlation** between the number of unique object detectors and classification accuracy.
- **Implication**: Encouraging disentangled concept detection can improve the feature's ability to generalize to new tasks.

---

# Experiment 6: Discrimination
 
\textcolor{purple}{\textbf{Benchmark high-level activations on a new task:}}
 
- Across several Deep NNs, extract activations from high CNN layers
- Train a linear SVM on a new *action recognition* task
- Compute classification accuracy

---
 
# Experiment 6: Discrimination Results
 
*exp_6*
 
\textcolor{purple}{\textbf{Result:}} Positive correlation between object detectors and classification accuracy $\rightarrow$ encouraging **concept detection** can improve **discrimination**.
 
---
 
# Experiment 7: Width
 
\textcolor{purple}{\textbf{Effect of layer width (number of units in a layer):}}
 
Increased layer width retains similar accuracy, but many more **concept detectors**
 
- \# Detectors increased both at the increased layer and in the network generally
- Increase has a threshold

---

# Experiment 7: Layer Width

What happens if we make a layer "wider" (more units)?

- **Method**: Tripled the number of units in AlexNet's `conv5` (from 256 to 768).
- **Result**: Accuracy remains similar, but the number of **unique concept detectors** increases significantly.
- **Limit**: Increasing width beyond a certain point (e.g., 1024 units) yields diminishing returns in unique concepts.

\vfill
\begin{center}
\textit{Wider layers provide more "slots" for the network to separate explanatory factors.}
\end{center}

---
 
# Experiment 7: Width Results
 
*exp_7*
 
---
 
# Discussion Questions (Paper 1)
 
1. \textcolor{purple}{\textbf{Distribution Understanding:}} Concept detectors from a particular dataset betray something about the underlying distribution. How do you think this can be applied in the real world (e.g., bias detection)?
2. \textcolor{purple}{\textbf{Single unit to circuit:}} This method interprets single units; could it be extended to larger circuits and would this be useful?
3. \textcolor{purple}{\textbf{Beyond vision:}} This method is deeply tied to the vision domain. Could it be extended to other domains such as natural language?

---

\begin{center}
\Huge Thank You!
\end{center}

---

# References {.allowframebreaks}

\footnotesize
