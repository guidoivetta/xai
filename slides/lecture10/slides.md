---
title: "\\emoji{wtf} XAI Lecture 10"
subtitle: "Sanity Checks for Saliency Maps \\& OpenXAI"
bibliography: references.bib

---

# Disclaimer

\input{../disclaimer.tex}

---

# Paper 1

\begin{center}
\Large \textbf{Sanity Checks for Saliency Maps}
\end{center}

\vspace{0.5cm}

**Authors:** Julius Adebayo, Justin Gilmer, Michael Muelly, Ian Goodfellow, Moritz Hardt, Been Kim

[@adebayo2018sanity]

---

# Overview

- Feature Attribution / Saliency Maps Setup
- Overview of Sanity Checks for Saliency Maps
- Follow-up work
- Parting thoughts / Q\&A

---

# Feature Attributions / Saliency Maps

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/bird_saliency.png}
\end{center}

\begin{center}
\textbf{What parts of the input are 'most important' for the model prediction?}
\end{center}

---

# Identifying Shortcuts

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/husky_shortcut.png}
\end{center}

\begin{center}
\small Model relying on snow to identify Huskies $\Rightarrow$ Collect additional data to fix the bug.
\end{center}

---

# Feature Attribution / Saliency Maps

**Feature attribution method:** assigns an output 'relevance' score to each dimension of the input.

$$F : \mathbb{R}^d \to \mathbb{R}^c \quad \text{Model}$$
$$\rule{6cm}{0.4pt}$$
$$F_i : \mathbb{R}^d \to \mathbb{R} \quad \textcolor{red}{\text{class specific logit}}$$

---

# Input-Gradient / Saliency / Gradient

\textcolor{red}{\textbf{Input-Gradient:}}

$$\nabla_x F_i(x) \in \mathbb{R}^d$$

- Same dimension as the input
- Gradient w.r.t. **Input** for class **Logit** $i$

[@baehrens2010explain; @simonyan2014deep]

---

# Integrated Gradients

$$(x - \tilde{x}) \times \int_{\alpha=0}^{1} \frac{\partial F(\tilde{x} + \alpha \times (x - \tilde{x}))}{\partial x}$$

Path integral: 'sum' of interpolated gradients from \textcolor{red}{\textbf{Baseline input}} $\tilde{x}$ to $x$.

[@sundararajan2017axiomatic]

---

# SmoothGrad

$$\frac{1}{N} \sum_{i}^{N} \nabla_{(x+\epsilon)} F_i(x + \epsilon)$$

Average of gradients computed on input $x$ perturbed with \textcolor{red}{\textbf{Gaussian noise}} $\epsilon$.

[@smilkov2017smoothgrad]

---

# Guided Backprop: "Modified Backprop"

\begin{columns}
\begin{column}{0.55\textwidth}
activation:
$$f_i^{l+1} = \text{relu}(f_i^l) = \max(f_i^l, 0)$$

backpropagation:
$$R_i^l = (f_i^l > 0) \cdot R_i^{l+1}, \quad R_i^{l+1} = \frac{\partial f^{out}}{\partial f_i^{l+1}}$$

guided backpropagation:
$$R_i^l = (f_i^l > 0) \cdot \boxed{(R_i^{l+1} > 0)} \cdot R_i^{l+1}$$
\end{column}
\begin{column}{0.43\textwidth}
\small Additional gate: only backpropagate \textbf{positive} relevance signals
\end{column}
\end{columns}

---

# Recap: Many Saliency Methods

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/methods_overview.png}
\end{center}

---

# Recap: Additional Methods

- **Class Activation Mapping** (Zhou et al. 2016)
- **Meaningful Perturbation** (Fong et al. 2017)
- **RISE** (Petsuik et al. 2018)
- **Extremal Perturbations** (Fong \& Patrick 2019)
- **DeepLift** (Shrikumar et al. 2018)
- **Expected Gradients** (Erion et al. 2019)
- **GradCAM** / **Guided GradCAM** (Selvaraju et al. 2016)
- **Occlusion** (Zeiler et al. 2014)
- **Prediction Difference Analysis** (Gu et al. 2019)
- **Internal Influence** (Leino et al. 2018)

\vspace{0.3cm}
\textcolor{red}{\textbf{See for additional methods: Samek \& Montavon et al. 2020}}

---

# Recap: Which Method Should You Use?

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/methods_overview.png}
\end{center}

---

# 'Sanity Checks'

Intuitive 'principles' that an attribution method should satisfy.

- **'Model' Faithfulness**: is the 'explanation' sensitive to model parameters?
  - Test: change the model weights and measure corresponding change in explanation.
  - Operationalize by reinitialization of model weights.
- **Data Faithfulness**: is the attribution sensitive to training data?
  - Test: change training label and measure corresponding change in explanation.
  - Operationalize by randomization labelling in training data.

---

# Sensitivity to Model Parameters

If the parameter settings change of model changes, the saliency map should change.

\begin{columns}
\begin{column}{0.48\textwidth}
- \textbf{Model 1}: trained normally
- \textbf{Model 2}: randomly initialized (or randomized top layers)
- Saliency maps should \textbf{differ} between models
\end{column}
\begin{column}{0.48\textwidth}
\begin{alertblock}{Key Question}
Does the explanation actually depend on the learned model weights?
\end{alertblock}
\end{column}
\end{columns}

---

# Sensitivity to Model Parameters: Cascading Randomization

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/cascading_randomization.png}
\end{center}

---

# Sensitivity to Model Parameters: SSIM Results

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/ssim_plot.png}
\end{center}

---

# Modified BackProp Approaches

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/modified_backprop.png}
\end{center}

\begin{alertblock}{Key Finding}
These modified backprop methods \textbf{converge to a rank-1 matrix}! The product of a sequence of non-negative matrices (non-orthogonal columns) converges to a rank-1 matrix (Theorem 1 in Sixt et al. 2020 [@sixt2020explanations]).
\end{alertblock}

---

# Recap: Which Method Should You Use?

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/which_method.png}
\end{center}

---

# Some Takeaways

- Identified certain classes of feature attribution methods that are **invariant to higher layer weights**
- 'Sanity Checks' are actually 'weak' requirements, i.e., does **not** tell you whether a method is effective

---

# Some Objections

Causal reframing suggests that sanity checks results might be **task specific**.

\begin{block}{Revisiting Sanity Checks for Saliency Maps}
Gal Yona, Daniel Greenfeld — Weizmann Institute of Science / Jether Energy Research
\end{block}

\begin{block}{On the Relationship Between Explanation and Prediction: A Causal View}
Amir-Hossein Karimi, Krikamol Muandet, Simon Kornblith, Bernhard Schölkopf, Been Kim
\end{block}

Where you choose to perform randomization matters, and perhaps the **weight randomization is not the best approach**.

\begin{block}{Shortcomings of Top-Down Randomization-Based Sanity Checks for Evaluations of Deep Neural Network Explanations}
Alexander Binder, Leander Weber, Sebastian Lapuschkin, Grégoire Montavon, Klaus-Robert Müller, Wojciech Samek
\end{block}

---

# More Recent Observations: Spurious Features

Beyond faithfulness, it is unclear whether these feature attribution methods are effective for **model debugging**.

\begin{block}{Do Feature Attribution Methods Correctly Attribute Features?}
Yilun Zhou, Serena Booth, Marco Tulio Ribeiro, Julie Shah — MIT CSAIL / Microsoft Research
\end{block}

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/modified_backprop.png}
\end{center}

---

# More Recent Observations

\begin{columns}
\begin{column}{0.48\textwidth}
\textbf{Do Input Gradients Highlight Discriminative Features?}

Harshay Shah, Prateek Jain, Praneeth Netrapalli — Microsoft Research India

- BlockMNIST: label determined by top block
- Standard gradients highlight non-discriminative features
\end{column}
\begin{column}{0.48\textwidth}
\textbf{Rethinking the Role of Gradient-based Attribution Methods for Model Interpretability}

Suraj Srinivas, François Fleuret — Idiap Research Institute / University of Geneva

- $\ell_2$ Robust training $\to$ more discriminative gradient maps
\end{column}
\end{columns}

---

# Parting Thoughts

\begin{exampleblock}{}
Feature attribution is still important for applications, however, additional work is needed to characterize the properties of DNN model training that will result in 'gradients' that capture discriminative signals.
\end{exampleblock}

---

# Exploring the Explanation Landscape

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/explanation_landscape.png}
\end{center}

\begin{center}
\Large How do we \textbf{\underline{evaluate}} the \textcolor{red}{\textbf{reliability}} of state-of-the-art explanation methods?
\end{center}

---

# Paper 2

\begin{center}
\Large \textbf{OpenXAI: Towards a Transparent Evaluation of Model Explanations}
\end{center}

\vspace{0.5cm}

**Authors:** Chirag Agarwal et al.

[@agarwal2022openxai]

---

# Overview

- Reliability pillars
- OpenXAI
- Is OpenXAI all you need?
- New directions

---

# Applications of Saliency Methods

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/applications_collage.png}
\end{center}

\small Natural images, MRI brain scans, Text, Videos, Audio, Chest X-rays, Detecting biases

---

# Reliability Pillars

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/reliability_pillars.png}
\end{center}

\begin{center}
\footnotesize C. Agarwal, M. Zitnik, H. Lakkaraju, Probing GNN Explainers: A Rigorous Theoretical and Empirical Analysis of GNN Explanation Methods, AISTAT
\end{center}

---

# Pillar 1: Faithfulness

\begin{definition}{}
An explanation is faithful if it accurately captures which features the model uses to make its prediction.

$$\text{faithfulness}(e, f, x) = \text{corr}\left(e_i(x),\; \Delta f_i(x)\right)$$

where $\Delta f_i(x)$ measures the change in model output when feature $i$ is masked.
\end{definition}

---

# Pillar 2: Stability

\begin{definition}{}
An explanation is stable (robust) if similar inputs receive similar explanations — small perturbations to $x$ should not drastically change $e(x)$.
\end{definition}

\begin{center}
\includegraphics[width=0.5\columnwidth]{imgs/pillar2_stability.png}
\end{center}

\footnotesize C. Agarwal et al., Rethinking Stability for Attribution-based Explanations, Oral presentation @ ICLR 2022 PAIR\^{}2Struct workshop.

---

# Pillar 3: Counterfactual Fairness

\begin{definition}{}
An explanation is counterfactually fair if members of different demographic groups receive explanations of comparable quality.

$$\text{PGU} = \mathbb{E}_{x \sim \text{majority}}[\Delta f(x, e)] - \mathbb{E}_{x \sim \text{minority}}[\Delta f(x, e)]$$
\end{definition}

\footnotesize J. Dai et al., Fairness via Explanation Quality: Evaluating Disparities in the Quality of Post hoc Explanations, AIES 2022.

---

# How Do We Pick an Explanation Method?

\begin{center}
\Huge How do we \textbf{\underline{pick}} an explanation method from the XAI landscape?
\end{center}

---

# OpenXAI

- OpenXAI provides an **automated end-to-end pipeline** that simplifies and standardizes the evaluation of post hoc explanation methods
- OpenXAI promotes **transparency and reproducibility** in benchmarking explanation methods

\vspace{0.5cm}

\footnotesize C. Agarwal et al., OpenXAI: Towards a Transparent Evaluation of Model Explanations, NeurIPS Datasets and Benchmark Track'2022

\url{https://github.com/AI4LIFE-GROUP/OpenXAI}

---

# OpenXAI's Key Components

- A flexible **synthetic data generator** and a collection of 7 real-world datasets, **16 pre-trained models**, and **6 state-of-the-art explanation methods**

- Open-source implementations of **22 quantitative metrics** for evaluating faithfulness, stability (robustness), and fairness of explanation methods

- **First-ever public XAI leaderboards** to benchmark explanation methods

---

# XAI Ready Dataloaders and Models

```python
from openxai import Dataloader
loader_train, loader_test = Dataloader.return_loaders(
    data_name='german', download=True)
inputs, labels = iter(loader_test).next()
```

\vspace{0.5cm}

OpenXAI provides pre-trained models for readily benchmarking explanation methods.

```python
from openxai import LoadModel
model = LoadModel(data_name='german', ml_model='ann')
```

---

# OpenXAI Explainers

OpenXAI provides ready-to-use implementations of six state-of-the-art feature attribution methods.

```python
from openxai import Explainer
exp_method = Explainer(method='LIME')
explanations = exp_method.get_explanations(
    model, X=inputs, y=labels)
```

\vspace{0.5cm}

```python
@abstractmethod
def get_explanations(self, model, X: torch.Tensor,
                     y: torch.Tensor):
    """
    Generate explanations for given input/s.
    Parameters: model, X (m x n tensor), y (labels)
    Returns: torch.Tensor (explanation vector/matrix)
    """
    pass
```

---

# OpenXAI's Evaluation

OpenXAI provides implementations and ready-to-use APIs for a set of **22 quantitative metrics** proposed by prior research to evaluate the faithfulness, stability, and fairness of explanation methods.

```python
from openxai import Evaluator
metric_evaluator = Evaluator(inputs, labels, model,
                             explanations)
score = metric_evaluator.eval(metric='RIS')
```

---

# OpenXAI's Leaderboard

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/openxai_leaderboard.png}
\end{center}

---

# Exploring the Landscape Using OpenXAI

- LIME produces more faithful (+24.9%) explanations
- Across all real-world datasets, SmoothGrad achieves **63.2% higher RRS** values

\begin{center}
\includegraphics[width=0.7\columnwidth]{imgs/openxai_landscape.png}
\end{center}

\small PGU metric for Majority vs. Minority groups — SmoothGrad shows largest fairness gap.

---

# Is OpenXAI All You Need?

- How to benchmark different **non-perturbation-based** explanation methods?

- Benchmarking explanations on **other modalities**:
  - Vision (Quantus)
  - NLP (e-ViL)
  - Graphs (GraphXAI)

\footnotesize C. Agarwal et al., Evaluating Explainability for Graph Neural Networks, Nature Scientific Data'2023

\footnotesize M. Kayser et al., e-ViL: A Dataset and Benchmark for Natural Language Explanations in Vision-Language Tasks, ICCV'2021

---

# New Directions

- Training models using **Explanation Feedbacks**
- **Differentiable Explainable Curricula** for RL Agents
- Learning **Hierarchical and Multi-modal Explanations**

---

\begin{center}
\Huge Thank You!
\end{center}

---

# References {.allowframebreaks}

\footnotesize
