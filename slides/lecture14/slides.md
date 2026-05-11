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


# How Is Semantic Visual Concept Represented in the Brain?


:::: columns
::: {.column width="50%"}
\begin{center}
\includegraphics[width=\columnwidth]{imgs/jennifer_neuron.png}
\end{center}
:::
::: {.column width="50%"}
Neuroscientists have found that individual neurons can respond 
selectively to specific concepts — a property called **selectivity**.

\begin{block}{The debate}
Does the brain use \textbf{local} representations (one neuron = one concept) or \textbf{distributed} ones (concepts spread across many neurons)?
\end{block}

Question: Do deep neural networks learn similar structure?
:::
::::


---

# A Neuron That Only Fires for Jennifer Aniston
:::: columns
::: {.column width="50%"}
\begin{center}
\includegraphics[width=\columnwidth]{imgs/jennifer_firing.png}
\end{center}


:::
::: {.column width="50%"}
Quiroga et al. (2005) recorded neurons in the human medial temporal lobe and found neurons that fire exclusively for specific people or landmarks.

- One neuron fired for Jennifer Aniston — photos, drawings, even her name written in text
- Another neuron fired only for the Eiffel Tower

\begin{block}{Why this matters}
This is a \textbf{disentangled} representation: one neuron = one concept. The paper asks whether CNNs learn something analogous.
\end{block}
:::
::::

---

# Disentangled Representation in Visual Cortex

:::: columns
::: {.column width="50%"}
\begin{center}
\includegraphics[width=\columnwidth]{imgs/jennifer_neuron.png}
\end{center}
:::
::: {.column width="50%"}
The visual cortex processes information in a **hierarchy** — the 
**ventral stream** ("what pathway"):

- **V1**: edges, orientations (small receptive fields)

- **V2/V4**: textures, shapes, color patterns

- **IT** (inferotemporal): objects, faces — where the "Jennifer Aniston neuron" lives

Along this hierarchy: **selectivity** increases and **invariance** increases.

\begin{block}{Bridge to CNNs}
This layered specialization is the biological inspiration for deep CNNs. Network Dissection tests whether CNNs develop analogous detectors at each layer.
\end{block}

\begin{block}{Analogy}
This layered specialization is the biological inspiration for deep CNNs. Do CNNs also develop specialized detectors at each layer?
\end{block}
:::
::::

---

# Disentangled Representation in Visual Cortex

:::: columns
::: {.column width="60%"}
The visual cortex processes information in a **hierarchy** — the **ventral stream** ("what pathway"):

- **V1**: edges, orientations (small receptive fields)

- **V2/V4**: textures, shapes, color patterns

- **IT** (inferotemporal): objects, faces — where the "Jennifer Aniston neuron" lives

Along this hierarchy: **selectivity** increases and **invariance** increases.

\begin{block}{Bridge to CNNs}
This layered specialization is the biological inspiration for deep CNNs. Network Dissection tests whether CNNs develop analogous detectors at each layer.
\end{block}
:::
::: {.column width="30%"}
\begin{center}
\includegraphics[width=\columnwidth]{imgs/visual_cortex.png}
\end{center}


:::
::::


---

# Deep CNN for Computer Vision

:::: columns
::: {.column width="50%"}
\begin{center}
\includegraphics[width=\columnwidth]{imgs/imagenet_error.png}
\end{center}
:::
::: {.column width="50%"}
CNNs revolutionized computer vision, reaching superhuman performance on ImageNet — but they remain largely opaque.

- Units in early layers respond to edges and colors
- Units in later layers seem to respond to objects and scenes (Zhou et al., 2015)
- But this was observed qualitatively — no rigorous measurement existed

:::
::::
\begin{block}{The gap}
We know CNNs \textit{work} extremely well. We don't know 
\textit{how}, or what each unit has learned. Network Dissection provides the first quantitative answer.
\end{block}

---


# Proposed Questions

The paper frames the problem around three concrete research questions. Each has a direct answer by the end of the paper.

1. \textcolor{purple}{\textbf{What is a disentangled representation, and how can its factors be quantified and detected (in deep CNN)?}}
2. \textcolor{purple}{\textbf{Do interpretable hidden units reflect a special alignment of feature space, or are interpretations a chimera?}}

3. \textcolor{purple}{\textbf{What conditions in state-of-the-art training lead to representations with greater or lesser entanglement?}}

---

# Proposed Questions and Contributions

\textcolor{red}{\textbf{Q1: How to quantify disentangled 
representations?}}

- Proposed a metric, intersection over union score (IoU), to quantify the interpretability of each unit
- The alignment level between unit activated area and human-interpretable concepts


\textcolor{red}{\textbf{Q2: Are interpretable units real or a 
chimera?}}

- A semantic concept can be detected by many units
- A unit can detect many semantic concepts
- But the natural basis is **special**: rotating it destroys interpretability

\textcolor{red}{\textbf{Q3: What training conditions affect 
entanglement?}}

- Factors tested: layer depth, training iterations, the angle of the images, input datasets, dropout, batch normalization, supervised vs. self-supervised, layer width

---

# Related Works

Prior work tried to understand CNN internals through **visualization**, but all approaches share a fundamental limitation: they are qualitative and cannot be used to rigorously compare models.
 
\vspace{0.3cm}

- \textcolor{red}{\textbf{Generative Visualizations}}: Synthesize images that maximally activate a unit (Mahendran et al., 2015; Nguyen et al., 2016; Simonyan et al., 2014)

- \textcolor{red}{\textbf{Salience-based Visualizations}}: Highlight which pixels most contribute to a unit's activation (Zeiler et al., 2014)

- \textcolor{red}{\textbf{Global Analysis}}: Project the full representation space into 2D for inspection (t-SNE: van der Maaten et al., 2008; Yosinski et al., 2015)

\vspace{0.3cm}

\begin{block}{Common limitation}
All these methods produce images that a \textbf{human} must then interpret — subjective and impossible to compare across networks.
Network Dissection replaces the human with a \textbf{metric}.
\end{block}

---
 
# Broden: Broadly and Densely Labeled Dataset
 
To measure interpretability we need a **ground truth** of human concepts. Broden unifies five existing segmentation datasets into a single resource.
 
:::: columns
::: {.column width="50%"}
 
\begin{center}
\includegraphics[width=\columnwidth]{imgs/broden_dataset.png}
\end{center}
 
:::
::: {.column width="50%"}
 
| Category | \# Classes |
|---|---|
| Scene | 468 |
| Object | 584 |
| Part | 234 |
| Material | 32 |
| Texture | 47 |
| Color | 11 |

:::
::::

Multiple labels can apply to the **same pixel** (e.g., a black cat leg $\rightarrow$ "cat", "leg", "black")

The range from colors to scenes allows testing nterpretability 
at \textbf{every level of abstraction}.

<!---

# Scoring Unit Interpretability: The Process

Each convolutional unit is evaluated as a **binary segmentation 
task** for every conceptc c in Broden.


1. **Activation Collection**: Feed Broden images through the frozen CNN, extract activation map $A_k(x)$ for unit $k$

2. **Quantile Thresholding**: Find threshold $T_k$ such that $P(a_{ij}^k > T_k) = 0.005$ over the dataset

3. **Resolution Alignment**: Upsample $A_k(x)$ to input resolution via **bilinear interpolation** → $S_k(x)$

4. **Binary Mask**: Generate $M_k(x) = S_k(x) \geq T_k$, selecting regions where the unit is "active"

5. **Compare**: Compute IoU between $M_k(x)$ and concept label $L_c$


\begin{exampleblock}{Key insight}
This is a \textbf{direct probe}: the network is frozen, no 
backpropagation or fine-tuning is involved.
\end{exampleblock}
--->

---

# Scoring Unit Interpretability

:::: columns
::: {.column width="45%"}
**Pipeline:**

- Feed images from Broden through the frozen CNN

- Collect activation map $A_k(x)$ for every unit $k$

- Upsample to input resolution → $S_k(x)$

- Threshold to obtain a binary mask $M_k(x)$

- Compare against concept labels $L_c$

:::
::: {.column width="50%"}
Each convolutional unit $k$ acts like a **filter** that fires on certain spatial regions of an image. The core idea: treat each unit as a candidate **segmentation model** for some concept.

For each unit, the method evaluates its activation mask against all **1,197 segmentation tasks** in Broden (one per concept). The unit is assigned the concept with the highest score.

:::
::::
\begin{center}
\includegraphics[width=0.6\columnwidth]{imgs/scoring_pipeline.png}
\end{center}
*scoring pipeline*

---

# Scoring Unit Interpretability: Threshold

:::: columns
::: {.column width="60%"}
\begin{center}
\includegraphics[width=\columnwidth]{imgs/scoring_threshold.png}
\end{center}
*threshold*
:::
::: {.column width="40%"}
Threshold $T_k$: value such that $P(a_{ij}^k > T_k) = 0.005$

This means: only the **top 0.5\%** of activations for unit $k$ 
across the entire dataset are considered "active."

\begin{alertblock}{Why a quantile?}
Each unit has a different activation range. A fixed threshold 
would favor high-magnitude units. The quantile normalizes this.
\end{alertblock}
:::
::::

---



# Scoring Unit Interpretability: IoU

:::: columns
::: {.column width="60%"}
\begin{center}
\includegraphics[width=\columnwidth]{imgs/scoring_iou.png}
\end{center}
:::
::: {.column width="40%"}
$$IoU_{k,c} = \frac{\sum_x |M_k(x) \cap L_c(x)|}
{\sum_x |M_k(x) \cup L_c(x)|}$$

## In plain English
"Of all the pixels where **either** the unit fires **or** the 
concept is present, what fraction has **both**?"

\begin{alertblock}{Detector definition}
Unit $k$ is a detector for concept $c$ if $IoU_{k,c} > 0.04$
\end{alertblock}
:::
::::

---

# Quantifying Alignment: Summary

The interpretability of unit $k$ for concept $c$ is the **IoU** 
across the dataset:

- **Detector**: Unit $k$ is a detector for concept $c$ if $IoU_{k,c} > 0.04$

- **Top Label**: If a unit matches multiple concepts, the one with the highest $IoU$ is assigned

- **Layer Score**: The interpretability of a layer is the number of **unique** semantic concepts aligned with its units

\begin{alertblock}{Why "unique"?}
If 50 units all detect "dog", the layer score counts "dog" only 
once. This measures \textbf{diversity} of concepts, not just 
quantity of detectors.
\end{alertblock}

---

# Experiments: Tested CNN Models

The paper evaluates interpretability across diverse architectures and training regimes to identify which conditions favor disentangled representations.

| **Training** | **Network** | **Dataset / Task** |
|---|---|---|
| None | AlexNet | Random weights |
| Supervised | AlexNet, GoogLeNet, VGG-16, ResNet-152 | ImageNet, Places205, Places365, Hybrid |
| Self-supervised | AlexNet | 10 proxy tasks (context, puzzle, colorization, etc.) |

\footnotesize Places: scene-centric dataset with categories such as kitchen, living room, coast.

\begin{alertblock}{Surprising finding (preview)}
Models trained on \textbf{Places} (scenes) develop more 
\textit{object} detectors than those trained on \textbf{ImageNet} 
(objects). Why? Because recognizing a scene \textit{requires} 
identifying the objects in it.
\end{alertblock}


<!--
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
 
-->

---

# Experiment 1: Human Evaluation of Interpretations

- Does Network Dissection agree with **human judgment**?
  - Raters shown 15 images with highlighted patches for each unit in AlexNet (Places205)
  - Asked: "Does this phrase describe most of the patches?" (yes/no)
  - **Network Dissection accuracy**: portion of method's labels rated as descriptive
  - **Human consistency**: portion of ground-truth labels found descriptive by a second group of raters

| | conv1 | conv2 | conv3 | conv4 | conv5 |
|---|---|---|---|---|---|
| Interpretable units | 57/96 | 126/256 | 247/384 | 258/384 | 194/256 |
| Human consistency | 82% | 76% | 83% | 82% | 91% |
| Network Dissection | 37% | 56% | 54% | 59% | 71% |

\begin{block}{Two takeaways}
1. Network Dissection agreement \textbf{increases} in higher layers (37\% → 71\%)\\
2. Human consistency remains high throughout (76--91\%), setting an upper bound
\end{block}

---
 

# Experiment 2: Axis-Aligned Interpretability

Is interpretability a property of the **natural basis** learned by the network, or does it appear in **every direction**?

\vspace{0.3cm}

\textcolor{red}{\textbf{Hypothesis 1: Concepts appear in every 
direction}}

- Single units are not more interpretable than random combinations
- Interpretability would be an artifact, not a real property

\textcolor{green}{\textbf{Hypothesis 2: The natural basis is special}}

- The model converges to a semantically rich, axis-aligned basis
- Interpretability is a learned property of the representation

\vspace{0.3cm}

**Test**: Apply a random orthogonal rotation $R$ to the representation space. If H2 is correct, rotating the basis should **destroy** interpretability.

---



# Experiment 2: Rotation Results

:::: columns
::: {.column width="55%"}
\begin{center}
\includegraphics[width=\columnwidth]{imgs/exp2_rotation.png}
\end{center}

:::
::: {.column width="45%"}
Number of unique detectors **decreases up to 80%** as the basis is rotated away from the natural one.

\begin{block}{Conclusion}
Interpretability is \textbf{not} an inevitable byproduct of 
discriminative power. It is a \textbf{special alignment} learned by the network — \textbf{Hypothesis 2 confirmed}.
\end{block}
:::
::::

---

# Experiment 3: Concepts by Layer

\begin{center}
\includegraphics[width=0.7\columnwidth]{imgs/exp3_concepts_layer.png}
\end{center}

The type of concept detected changes with **layer depth**:
**Early layers**: colors, textures → **Middle layers**: materials, 
parts → **Late layers**: objects, scenes.

This mirrors the visual cortex hierarchy: V1 (edges) $\rightarrow$ 
V4 (textures) $\rightarrow$ IT (objects). The analogy holds 
quantitatively.

---


# Experiment 4: Network Architectures

:::: columns
::: {.column width="40%"}
\begin{center}
\includegraphics[width=\columnwidth]{imgs/exp4_architectures.png}
\end{center}
:::
::: {.column width="40%"}
Comparing the number of unique detectors across architectures 
trained on the **same dataset**:

- Deeper and more complex architectures tend to develop **more unique concept detectors**

- **ResNet-152** and **VGG-16** consistently outperform AlexNet and GoogLeNet

\begin{block}{Key nuance}
More detectors does not always mean better accuracy — the relationship is architecture-dependent.
\end{block}
:::
::::

---
 

# Experiment 5: Training Conditions

What training choices affect interpretability?

\vspace{0.3cm}

- \textcolor{green}{\textbf{Weight initializations}}: **Minimal effect** — models converge to similar levels of interpretability regardless of random seed

- \textcolor{orange}{\textbf{Dropout}}: **Some effect** — removing dropout leads to more "texture" detectors and fewer "object" detectors

- \textcolor{red}{\textbf{Batch Normalization}}: **Significant  effect** — interpretability decreased substantially

\begin{block}{Surprising result}
Batch Normalization improves accuracy but \textbf{hurts} interpretability. There may be a trade-off between optimization 
convenience and semantic disentanglement.
\end{block}

---

# Experiment 5: Training Conditions Results


\begin{center}
\includegraphics[width=0.5\columnwidth]{imgs/exp5_training.png}
\end{center}

The figure confirms:

- Different random seeds → nearly identical interpretability

- Dropout removal → shift from objects to textures

- Batch Norm → large drop in unique detectors across all categories

---


# Experiment 6: Discrimination vs. Interpretability

Does being more "interpretable" make a model **better at new tasks**?

\vspace{0.3cm}

\textcolor{red}{\textbf{Benchmark:}}

- Across several CNNs, extract activations from high layers

- Train a **linear SVM** on a new task: **action recognition** (Action40 dataset)

- Compare classification accuracy vs. number of unique object detectors

\vspace{0.3cm}

\begin{exampleblock}{Why a linear SVM?}
A linear classifier can only succeed if the features are already well-organized. If interpretable representations also produce linearly separable features, that's strong evidence they generalize.
\end{exampleblock}

---

# Experiment 6: Discrimination Results


\begin{center}
\includegraphics[width=0.5\columnwidth]{imgs/exp6_scatter.png}
\end{center}

\textcolor{red}{\textbf{Result:}} Positive correlation between 
object detectors and classification accuracy.

\begin{block}{Implication}
Encouraging \textbf{concept detection} can improve \textbf{discrimination}. Interpretability and performance are \textbf{not} at odds — they can reinforce each other.
\end{block}



---
 
# Experiment 7: Layer Width

What happens if we make a layer **wider** (more units)?

\vspace{0.3cm}

- **Method**: Tripled the number of units in AlexNet's conv5 (from 256 to 768)

- **Result**: Accuracy remains similar, but the number of **unique concept detectors** increases significantly

- **Limit**: Beyond ~1024 units, diminishing returns in unique concepts

\begin{exampleblock}{Intuition}
Wider layers provide more "slots" for the network to separate 
explanatory factors — like having a bigger bookshelf with room 
for more categories.
\end{exampleblock}

---
 

# Experiment 7: Width Results


\begin{center}
\includegraphics[width=0.5\columnwidth]{imgs/exp7_width.png}
\end{center}

Increased width:

- More unique detectors both at the widened layer **and** in the network generally

- Accuracy remains stable

- Effect saturates beyond a threshold

If interpretability is a goal, \textbf{wider layers} are a cheap way to get more disentangled representations without sacrificing accuracy.

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

# From Network Dissection to TCAV - ver si lo dejo

:::: columns
::: {.column width="50%"}
**Network Dissection** (Bau et al., 2017)

- Interprets **individual units**
- Concepts come from a **fixed dataset** (Broden)
- Measures: does unit $k$ detect concept $c$?
- Spatial alignment (IoU)
- Limited to CNNs with spatial activations
:::
::: {.column width="50%"}
**TCAV** (Kim et al., 2018)

- Interprets **entire classes**
- Concepts defined by the **user** (any set of examples)
- Measures: is concept $c$ important for class $k$?
- Directional sensitivity in activation space
- Works on any differentiable model
:::
::::

\begin{block}{The shift}
Network Dissection asks: "what does this unit detect?" \\
TCAV asks: "how important is this concept for this prediction?"
\end{block}

---


# Motivation + Problem Statement


- Interpreting deep learning models is crucial to understanding 
  their behavior and ensuring accurate predictions

- But remains a big challenge due to size, complexity, and opacity 
  of ML models

- Many systems operate on **low-level features** (e.g., pixel 
  values) rather than \textcolor{red}{\textbf{high-level concepts}} 
  (e.g., face) that are human-interpretable

\begin{block}{The mismatch}
Models explain in \textbf{pixels}. Humans understand in 
\textbf{concepts}. TCAV bridges this gap.
\end{block}


\begin{center}
\includegraphics[width=0.6\columnwidth]{imgs/tcav_features_levels.png}
\end{center}

---

# Motivation + Problem Statement

**Problem:**

- We can't express these concepts as pixels

- And they weren't our input features

- Existing methods (saliency maps, LIME) explain in terms of input features — not the concepts humans care about

:::: columns
::: {.column width="55%"}
\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/tcav_cash_machine.png}
\end{center}

:::
::: {.column width="40%"}

\begin{exampleblock}{What we want to ask}
"Did the model use the concept of \textit{person}? Of \textit{money}? Of \textit{machine}?" — not "which pixels mattered?"
\end{exampleblock}
:::
::::


---

# Summary of Contributions

:::: columns
::: {.column width="55%"}
- Introduce \textcolor{orange}{\textbf{Concept Activation Vectors 
  (CAVs)}}: way to interpret a neural network's internal state in 
  terms of human-friendly concepts

- Key idea: use the high-dimensional internal state of a neural net 
  as an **aid**, not an obstacle

- Main contribution: \textcolor{orange}{\textbf{Testing with CAV 
  (TCAV)}}, that quantifies model sensitivity to a high-level 
  concept learned by a CAV for a particular class

\begin{exampleblock}{Example}
"How sensitive is the class \textit{zebra} to the concept 
\textit{striped}?" → TCAV returns a single number.
\end{exampleblock}
:::
::: {.column width="45%"}
\begin{center}
\includegraphics[width=\columnwidth]{imgs/tcav_contributions.png}
\end{center}

:::
::::

<!---

# Summary of Contributions

- Introduce \textcolor{orange}{\textbf{Concept Activation Vectors (CAVs)}}: way to interpret a neural network's internal state in terms of human-friendly concepts
- Key idea is to use the high-dimensional internal state of a neural net as an aid, not an obstacle
- Main contribution: \textcolor{orange}{\textbf{Testing with CAV (TCAV)}}, that quantifies model sensitivity to a high-level concept learned by a CAV for a particular class

\begin{center}
\includegraphics[width=0.7\columnwidth]{imgs/tcav_contributions.png}
\end{center}

--->

---

# Goals of TCAV

- \textcolor{blue}{\textbf{Accessibility:}} requires little to no 
  ML expertise

- \textcolor{red}{\textbf{Customization:}} adaptable to any concept, 
  even outside of training

- \textcolor{orange}{\textbf{Plug-in readiness:}} works without 
  retraining/modifying ML models

- \textcolor{olive}{\textbf{Global quantification:}} can interpret 
  entire classes with a single quantitative measure

\vspace{0.5cm}

\begin{center}
$\downarrow$

\textbf{Assessed with experiments + human evaluation}
\end{center}

\begin{block}{Compare with Network Dissection}
ND is not accessible (requires understanding IoU), not customizable 
(fixed Broden concepts), and not global (per-unit, not per-class). 
TCAV addresses all three.
\end{block}

---


# Related Work: Limitations of Current Methods

\textcolor{red}{\textbf{Perturbation-based}} (LIME, SHAP):

- Explain individual predictions (**local**), not entire classes
- Operate at the input feature level, not at the concept level

\vspace{0.2cm}

\textcolor{red}{\textbf{Saliency methods}} (Gradient, CAM, etc.):

- **Local**: one image at a time
- **Lack customization**: cannot test user-defined concepts
- **Vulnerable** to adversarial attacks (Ghorbani et al., 2017)
- **Insensitive** to model randomization (Adebayo et al., 2018)

\begin{block}{Core limitation shared by all}
These methods explain in terms of \textbf{input features}. 
Saliency maps tell you \textit{where} the model looks, not 
\textit{what} it sees. TCAV explains in terms of 
\textbf{human-defined concepts}.
\end{block}

---

# Related Work: Linearity + Latent Dimensions

A key observation across deep learning: **concepts tend to be 
linear directions** in representation spaces.

- **word2vec** (Mikolov et al., 2013): 
  $\vec{king} - \vec{man} + \vec{woman} \approx \vec{queen}$
  → "gender" is a linear direction

- **Probing classifiers** (Alain \& Bengio, 2016): linear 
  classifiers on hidden layers extract semantic information

- **Network Dissection** (Bau et al., 2017): individual units 
  align with concepts — the axes themselves are meaningful

\begin{block}{TCAV builds on this}
If concepts are \textbf{linear directions} in activation space, we 
can find them with a simple linear classifier and measure their 
influence via \textbf{directional derivatives}.
\end{block}

---

# Approach: Defining the CAV

:::: columns
::: {.column width="55%"}
<!---Consider the fully connected layer $f_l : \mathbb{R}^n \rightarrow \mathbb{R}^m$  --->
The user wants to test concept $C$ (e.g., "stripes"). How do we 
represent it inside the network?

1. Collect a set of examples $P_C$ of the that concept and a negative set $N$ of examples that don't

2. Feed both through the network, extract activations at layer $l$

3. Train a **linear classifier** to separate them

4. The **CAV** $\mathbf{v}_C^l$ is the vector **orthogonal** to the decision boundary between activations — it points in the "direction of the concept"

\begin{block}{Key insight}
A CAV is a \textbf{direction} in activation space that represents 
a human-defined concept. No retraining of the original model needed.
\end{block}
:::
::: {.column width="45%"}
\begin{center}
\includegraphics[width=0.7\columnwidth]{imgs/tcav_cav_definition.png}
\end{center}
:::
::::
![alt text](image.png)

---

# Approach: Visualizing the CAV

:::: columns
::: {.column width="60%"}
\begin{center}
\includegraphics[width=\columnwidth]{imgs/tcav_cav_visualization.png}
\end{center}

:::
::: {.column width="35%"}
The CAV $\mathbf{v}_C^l$ is the normal to the linear decision boundary:

- One side → "has concept $C$"

- Other side → "does not have concept $C$"

Moving along the CAV direction = "adding more of concept $C$" to 
the representation.

:::
::::


---


# Approach: Concept Sensitivity

Saliency maps gauge sensitivity with respect to per-pixel perturbations. With CAV, we gauge sensitivity 
**towards a concept** at an entire layer:

$$S_{C,k,l}(\mathbf{x}) = \nabla h_{l,k}(f_l(\mathbf{x})) \cdot \mathbf{v}_C^l$$

## In plain English

"If we nudge the activations in the direction of concept $C$, how much does the prediction for class $k$ change?"

\vspace{0.3cm}

- $f_l(\mathbf{x})$: activations at layer $l$ for input $\mathbf{x}$

- $\nabla h_{l,k}(f_l(\mathbf{x}))$: gradient of class $k$ output w.r.t. those activations

- $\mathbf{v}_C^l$: the CAV (concept direction)

- The **dot product** measures alignment between the gradient and the concept direction


---


# Approach: The TCAV Score

The sensitivity $S_{C,k,l}(\mathbf{x})$ is **per-image**. To get a 
**global** measure for the entire class:

$$\text{TCAV}_{Q_{C,k,l}} = \frac{|\{\mathbf{x} \in X_k : S_{C,k,l}(\mathbf{x}) > 0\}|}{|X_k|}$$

## In plain English

"Of all images of class $k$, what fraction has activations that are 
**positively influenced** by concept $C$?"

\vspace{0.3cm}

- $\text{TCAV} = 1.0$ → every image of class $k$ is sensitive to $C$

- $\text{TCAV} = 0.5$ → no more influence than random (meaningless)

- $\text{TCAV} = 0.0$ → concept $C$ pushes **away** from class $k$

\begin{block}{Statistical safeguard} 
A $t$-test across multiple random negative sets filters spurious 
CAVs. Only statistically significant results are reported.
\end{block}

---

# Approach Summary

\begin{center}
\includegraphics[width=\columnwidth]{imgs/tcav_approach_summary.png}
\end{center}

\begin{exampleblock}{The full pipeline in one sentence}
User provides concept examples → linear classifier on activations → 
CAV direction → directional derivative → TCAV score → $t$-test. 
\textbf{The original model is never modified.}
\end{exampleblock}


---



# Results: Sorting Images with CAVs

Images sorted by their projection onto a CAV direction, a qualitative validation that the CAV captures the intended concept.

- Class "stripes" sorted by concept "CEO": confirms CAV reflects the concept correctly

- Class "necktie" sorted by concept "model woman": reveals a gender bias in the learned representation

\begin{center}
\includegraphics[width=0.7\columnwidth]{imgs/tcav_sorting_images.png}
\end{center}

Sorting by unexpected concepts can reveal biases invisible to standard evaluation metrics.
\begin{block}{Why this matters}
Sorting by unexpected concepts can reveal biases invisible to standard evaluation metrics.
\end{block}

---



# Results: Gaining Insights with TCAV

:::: columns
::: {.column width="50%"}
\begin{center}
\includegraphics[width=\columnwidth]{imgs/tcav_insights.png}
\end{center}
:::
::: {.column width="50%"}
Each bar = TCAV score at a different layer. Only statistically 
significant CAVs shown.

- "Red" $\rightarrow$ "fire engine": high TCAV

- "Striped" $\rightarrow$ "zebra": high TCAV

- "Dotted" $\rightarrow$ "zebra": filtered out by $t$-test

- "Caucasian" $\rightarrow$ "rugby ball": high TCAV

- - TCAV enables **ranking concepts by importance** for a class —
  not just "is it relevant?" but "how much more relevant than 
  others?"

Layers closer to the output have greater influence on the 
prediction.

\begin{block}{Key result}
TCAV confirms intuitive associations \textbf{and} reveals hidden 
biases — with statistical rigor.
\end{block}
:::
::::

---

# Results: TCAV for Where Concepts Are Learned

:::: columns
::: {.column width="45%"}
CAV accuracy at different layers reveals *where* each concept is learned:

- Simple concepts (colors, patterns) reach high accuracy at low layers.

- Complex concepts (age, sex, objects) don't reach high accuracy until higher layers.

:::
::: {.column width="55%"}
\begin{center}
\includegraphics[width=\columnwidth]{imgs/tcav_where_learned.png}
\end{center}
:::
::::

\begin{block}{Convergence with Network Dissection}
Both methods confirm the same hierarchy using completely different approaches: early layers = low-level features, late layers = high-level concepts.
\end{block}

---

# Results: Controlled Experiment with Ground Truth

:::: columns
::: {.column width="55%"}
\begin{center}
\includegraphics[width=\columnwidth]{imgs/tcav_controlled.png}
\end{center}
:::
::: {.column width="45%"}
A model trained on images with **embedded captions** to create 
known ground truth:

- **"Cab"**: image concept dominates $\rightarrow$ TCAV correctly shows high image sensitivity, low caption sensitivity

- **"Cucumber"**: caption concept dominates when present $\rightarrow$ TCAV correctly reflects this

\begin{block}{Validation}
TCAV scores faithfully reflect the \textbf{true} importance of 
each concept — confirmed against known ground truth.
\end{block}
:::
::::

---

# Results: Evaluation of Saliency Maps

\begin{center}
\includegraphics[width=0.6\columnwidth]{imgs/tcav_saliency_eval.png}
\end{center}

We know that for "cab" the image concept is most important. But saliency maps highlight the caption text (high contrast) instead — across all four methods.


---

# Results: Saliency Maps Are Misleading

:::: columns
::: {.column width="55%"}
\begin{center}
\includegraphics[width=\columnwidth]{imgs/tcav_human_eval.png}
\end{center}
:::
::: {.column width="45%"}
Using the same controlled experiment:

- **Saliency maps** led human subjects to **incorrect conclusions** about which concept was more important

- Subjects thought the caption was more important than the image for "cab" — **wrong**

- **TCAV scores** correctly identified the dominant concept in every case
:::
::::

Saliency maps are not just imprecise — they are actively \textbf{misleading}. They highlight visually salient pixels (high contrast text), not causally important ones.


---


# Results: TCAV for Medical Diagnosis

:::: columns
::: {.column width="45%"}
\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/tcav_medical.png}
\end{center}
:::
::: {.column width="55%"}
TCAV applied to a diabetic retinopathy diagnosis model:

- \textcolor{green}{Green} = medically relevant concepts

- \textcolor{red}{Red} = irrelevant concepts

- **Level 4**: model correctly uses relevant concepts

- **Level 1**: model gives too much importance to HMA (relevant for Level 2, not Level 1)

\begin{block}{Debugging with TCAV}
A doctor (no ML expertise) can verify whether the model uses the \textbf{right medical concepts} — not just whether it gets the right answer.
\end{block}


- TCAV score shows model successfully distinguishes relevant and irrelevant concepts for level 4 DR diagnosis
- TCAV score reveals model gives too much importance to HMA concept for level 1 diagnosis → use this to debug the model


:::
::::

---


# Conclusions


\textcolor{red}{\textbf{Roadmap:}} Gradient $\rightarrow$ 
Attention $\rightarrow$ Concept-based 
(\textcolor{orange}{\textbf{TCAV!}})

\vspace{0.3cm}

\textcolor{red}{\textbf{Limitations:}}

- Evaluated only on computer vision tasks

- Assumes concepts are **linear** directions in activation space

- Statistical significance testing — is a $t$-test rigorous 
  enough?

- Depends on quality of user-provided concept examples
<!--- es la misma del metodo
:::
::: {.column width="50%"}
\begin{center}
\includegraphics[width=\columnwidth]{imgs/tcav_conclusions.png}
\end{center}
:::
::::
--->

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
