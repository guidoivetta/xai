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
\includegraphics[width=0.9\columnwidth]{imgs/paper1.png}
\end{center}

[@adebayo2018sanity]

---

# Feature Attributions / Saliency Maps

\begin{center}
\textbf{What parts of the input are 'most important' for the model prediction?}
\end{center}


\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/bird_saliency.png}
\end{center}

---

# Identifying Shortcuts

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/husky_shortcut.png}
\end{center}

A **shortcut** is a specific type of bias — the model learns a spurious correlation that works well on training data but fails to generalize. Instead of learning the relevant feature (the dog), it learns an easier, correlated signal (the snow).

---

# Feature Attribution / Saliency Maps

**Feature attribution method:** assigns an output 'relevance' score to each dimension of the input.

$$F : \mathbb{R}^d \to \mathbb{R}^c \quad \text{Model}$$
$$\rule{6cm}{0.4pt}$$
$$F_i : \mathbb{R}^d \to \mathbb{R} \quad \textbf{\text{class specific logit}}$$

An attribution method produces a map $E: \mathbb{R}^d \to \mathbb{R}^d$ of the same shape as the input, where each value $E_j(x)$ indicates how much dimension $j$ contributed to the prediction of class $i$.

---

# Input-Gradient / Saliency / Gradient

\textcolor{red}{\textbf{Input-Gradient:}}

$$\nabla_x F_i(x) \in \mathbb{R}^d$$

- Same dimension as the input
- Gradient w.r.t. **Input** for class **Logit** $i$

**Intuitively**, $\nabla_x F_i(x)$ answers:

\begin{center}
\textit{"if I perturb input dimension $j$ slightly, how much does the predicted score for class $i$ change?}
\end{center}

Large values indicate dimensions the model is most sensitive to near $x$.


[@baehrens2010explain; @simonyan2014deep]

---

# Input-Gradient / Saliency / Gradient - Demo

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/imputgrad.png}
\end{center}

**Intuitively**, $\nabla_x F_i(x)$ answers:

\begin{center}
\textit{"if I perturb input dimension $j$ slightly, how much does the predicted score for class $i$ change?}
\end{center}

Large values indicate dimensions the model is most sensitive to near $x$.


[@baehrens2010explain; @simonyan2014deep]

---

# Integrated Gradients

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/intgrad.png}
\end{center}

$$(x - \tilde{x}) \times \int_{\alpha=0}^{1} \frac{\partial F(\tilde{x} + \alpha \times (x - \tilde{x}))}{\partial x}$$

**Path integral:** 'sum' of interpolated gradients from \textcolor{red}{\textbf{Baseline input}} $\tilde{x}$ to $x$.

[@sundararajan2017axiomatic]

---

# SmoothGrad

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/smothgrad.png}
\end{center}

$$\frac{1}{N} \sum_{i}^{N} \nabla_{(x+\epsilon)} F_i(x + \epsilon)$$

Average of gradients computed on input $x$ perturbed with \textcolor{red}{\textbf{Gaussian noise}} $\epsilon$.

[@smilkov2017smoothgrad]

---

# Guided Backprop: "Modified Backprop"

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/guidedgrad.png}
\end{center}

\vspace{1em}

\begin{columns}
\begin{column}{0.32\textwidth}
\small activation:
$$f_i^{l+1} = \text{relu}(f_i^l) = \max(f_i^l, 0)$$
\end{column}
\begin{column}{0.32\textwidth}
\small backpropagation:
$$R_i^l = (f_i^l > 0) \cdot R_i^{l+1}, \quad R_i^{l+1} = \frac{\partial f^{out}}{\partial f_i^{l+1}}$$
\end{column}
\begin{column}{0.32\textwidth}
\small guided backpropagation:
$$R_i^l = (f_i^l > 0) \cdot \boxed{(R_i^{l+1} > 0)} \cdot R_i^{l+1}$$

\end{column}
\end{columns}

\vspace{0.5em}
Additional gate: only backpropagate \textbf{positive} relevance signals

---

# Are Saliency Maps Reliable?


\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/trustsalienci.png}
\end{center}

Both maps are produced by the **same method** on the **same input** — but one comes
from a trained model and the other from a **randomly initialized** network.

- **Top:** explanation from a **trained** model.
- **Bottom:** explanation from a **randomly initialized** model.

Can you tell which is which?

> Visual inspection alone is not a reliable criterion for evaluating saliency methods.



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

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/sensehp.png}
\end{center}

If the parameter settings of the model change, the saliency map should change.

- **Model 1**: trained normally
- **Model 2**: randomly initialized (or randomized top layers)
- Saliency maps should **differ** between models


---

# Sensitivity: Cascading Randomization

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/cascading_randomization.png}
\end{center}

\begin{center}
\textbf{
A method that looks the same regardless of the model's parameters
cannot be explaining what the model learned.}
\end{center}

---

# Sensitivity to Model Parameters: SSIM Results

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/ssim_plot.png}
\end{center}

---

# Modified BackProp Approaches

:::: {.columns}
::: {.column width="55%"}

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/modified_backprop.png}
\end{center}

:::
::: {.column width="43%"}

Backprop-based methods that modify gradients at each layer collapse to a
**rank-1 matrix** — their output is dominated by the **input structure**,
not by the model's learned weights.

**This is why these methods still produce recognizable maps even when the
model is completely random: they are recovering the input, not explaining the model.**

*(Sixt et al. 2020, Theorem 1)*
:::
::::

---

# Recap: Which Method Should You Use?

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/which_method.png}
\end{center}

---

# Some Takeaways

- Identified certain classes of feature attribution methods that are **invariant to higher layer weights**
- 'Sanity Checks' are actually **weak** requirements, i.e., does **not** tell you whether a method is effective

---

# Some Objections 1/2

\begin{center}
\large
Causal reframing suggests that sanity checks results might be \textbf{task specific}.
\end{center}

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/objection1.png}
\end{center}

---

# Some Objections 2/2

\begin{center}
\large
Where you choose to perform randomization matters, and perhaps the \textbf{weight randomization is not the best approach}.
\end{center}

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/objection2.png}
\end{center}

---

# More Recent Observations: Spurious Features

Beyond faithfulness, it is unclear whether these feature attribution methods are effective for **model debugging**.

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/objection3.png}
\end{center}

---

# More Recent Observations

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/objection4.png}
\end{center}

\small
- **BlockMNIST:** each image has two blocks — the discriminative one is fixed by class position. A good saliency method should focus on the correct block.
- **Key finding:** saliency quality depends not only on the attribution method, but also on **how the model was trained** — robustly trained models produce cleaner, more discriminative gradients.

---

# Parting Thoughts

\begin{exampleblock}{}
\Large
Feature attribution is still important for applications, however, additional work is needed to characterize the properties of DeepNN model training that will result in 'gradients' that capture discriminative signals.
\end{exampleblock}

---

# Paper 2

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/paper2.png}
\end{center}

[@agarwal2022openxai]

---

# Overview

- Reliability pillars
- OpenXAI
- Is OpenXAI all you need?
- New directions

---

# Applications of Saliency Methods 1/2

:::: columns
::: {.column width="60%"}

\begin{center}
\includegraphics[width=.9\columnwidth]{imgs/applications_collage.png}
\end{center}

:::
::: {.column width="40%"}

\small
Saliency methods are used across a wide range of data modalities —
the question of how to evaluate them is relevant in all of these settings.

- **Natural images** — highlighting relevant regions in a scene
- **MRI / medical imaging** — localizing diagnostically relevant areas
- **Text** — identifying influential words or tokens
- **Video** — attributing predictions to specific frames or regions
- **Audio** — localizing relevant time-frequency patterns in spectrograms

:::
::::

---

# Applications of Saliency Methods 2/2

:::: columns
::: {.column width="60%"}

\begin{center}
\includegraphics[width=.9\columnwidth]{imgs/applications_collage2.png}
\end{center}

:::
::: {.column width="40%"}

\small
In high-stakes domains, unreliable explanations can have serious consequences.

- **Medical diagnosis** — a model predicts Pneumonia (85%), but is it
  looking at the right region of the X-ray?
- **Detecting biases** — a horse classifier was found to rely on a
  **photographer's watermark** rather than the animal itself.

> A visually compelling explanation is not necessarily a correct one —
> this is precisely what makes evaluation frameworks like OpenXAI necessary.

:::
::::

---

# How Do We Evaluate the Reliability of Explanation Methods?

A reliable explanation method should satisfy three key properties (pillars):

- **Faithful** — the explanation accurately reflects the model's true behavior.
- **Stable** — similar inputs should produce similar explanations.
- **Fair** — explanation quality should not vary across demographic groups.

---

# Pillar 1: Faithfulness

\begin{center}
\textbf{An explanation is faithful if it accurately reflects the model's true behavior.}
\end{center}

- **Intuitively:** if we hide the features the explanation marks as unimportant,
the model's prediction should not change much.

- **Definition.** Given an input $x$ and its explanation $E_x$:

  \textbf{$$\frac{1}{N} \sum_N \| f(x) - f(t(E_x, x)) \|_2$$}

  where \textbf{$t(E_x, x)$} masks the features deemed unimportant by \textbf{$E_x$}.

  A **lower value** indicates higher faithfulness.


---

# Pillar 2: Stability

\begin{center}
\textbf{An explanation is \textbf{stable} if similar inputs produce similar explanations.}
\end{center}

:::::::::::::: {.columns}
::: {.column width="50%"}


- **Intuitively:** a small perturbation to the input $x$ should not drastically
change what the explanation highlights.

- **Definition.** Given an input $x$ and a perturbed counterpart $x'$,
the explanation $E_x$ is stable if:

  \textbf{$$D(E_x, E_{x'}) \leq \delta$$}

  where \textbf{$D$} measures the distance between the two explanations and
  \textbf{$\delta$} is a small tolerance threshold.

:::
::: {.column width="50%"}

\begin{center}
\includegraphics[width=.95\columnwidth]{imgs/pillar2_stability.png}
\end{center}

:::
::::::::::::::

---

# Pillar 3: Counterfactual Fairness

\begin{center}
\textbf{An explanation is fair if changing a protected attribute only affects the explanation to the extent that it affects the model's prediction.}
\end{center}

- **Intuitively:** if the model treats two individuals the same regardless of their protected attribute, their explanations should also be the same.

- **Definition.** Given a feature vector $x$ and its protected attribute
perturbation $x^S$, an explanation $E_x$ preserves counterfactual fairness if:

  \textbf{$$D(E_x, E_{x^S}) \propto f(x) - f(x^S)$$}

  The difference between explanations should be **proportional** to the difference in predictions. If the model's output didn't change,the explanation shouldn't change either.

---

# How Do We Pick an Explanation Method?

\begin{center}
\Huge How do we \textbf{\underline{pick}} an explanation method from the XAI landscape?
\end{center}

. . .

**Short answer:** it depends. **Longer answer:** it really depends.

**The XAI landscape offers dozens of methods** — but there is no universal
winner. The best method depends on your model, your data, and what
"reliable" means in your specific context.

---

# OpenXAI

**This is exactly what OpenXAI is for:**

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

# XAI-Ready Dataloaders and Models

OpenXAI includes 7 real-world datasets (finance, healthcare, criminal justice)
and a synthetic data generator — all preprocessed and ready to use out of the box.
```python
from openxai import Dataloader
loader_train, loader_test = Dataloader.return_loaders(
    data_name='german',
    download=True,
)
inputs, labels = iter(loader_test).next()
```

Pre-trained models (ANNs and logistic regression) are also available,
so you can start benchmarking explanation methods without training anything yourself.

```python
from openxai import LoadModel
model = LoadModel(data_name='german', ml_model='ann')
```


---

# OpenXAI Explainers

OpenXAI provides ready-to-use implementations of six state-of-the-art
feature attribution methods: LIME, SHAP, Vanilla Gradients,
Gradient $\times$ Input, SmoothGrad, and Integrated Gradients.

```python
from openxai import Explainer
exp_method = Explainer(method='LIME')
explanations = exp_method.get_explanations(model, X=inputs, y=labels)
```

This makes it easy to swap methods and compare their outputs
under identical conditions.

---

# OpenXAI Explainers - API

Any custom method can be integrated by extending the `Explainer` class
and implementing a single method:

```python
@abstractmethod
def get_explanations(self, model, X: torch.Tensor, y: torch.Tensor):
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
metric_evaluator = Evaluator(inputs, labels, model, explanations)
score = metric_evaluator.eval(metric='RIS')
```

---

# OpenXAI's Leaderboard 1/2

OpenXAI provides a public leaderboard to compare explanation methods
across datasets, models, and evaluation metrics — making it easy to
identify which method works best for a given setting.

\begin{center}
\includegraphics[width=0.99\columnwidth]{imgs/openxai_leaderboard.png}
\end{center}

---

# OpenXAI's Leaderboard 2/2

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/openxai_leaderboard.png}
\end{center}

\fontsize{10pt}{9pt}
The table shows **faithfulness metrics** for six methods on the **German Credit** dataset:

- **FA, RA, SA, SRA, PRA, RC** — agreement between explanation and ground truth.
- **PGI / PGU** — prediction gap when masking important / unimportant features.

**Key observation:** gradient-based methods consistently outperform SHAP —
but this may not hold across all settings.

---

# Exploring the Landscape Using OpenXAI

\begin{center}
\includegraphics[width=0.7\columnwidth]{imgs/openxai_landscape.png}
\end{center}

\small
No single method wins on all dimensions:

- **LIME** produces more faithful explanations (+24.9%).
- **SmoothGrad** achieves 63.2% higher stability (RRS) — but shows the
  **largest fairness gap** between majority and minority groups.

The chart shows PGU scores by demographic group. A gap between majority (red)
and minority (purple) indicates unequal explanation quality across groups.

\begin{center}
\textbf{A method that is faithful and stable may still be unfair}
\end{center}

---

# Is OpenXAI All You Need?

- How to benchmark different **non-perturbation-based** explanation methods?

- Benchmarking explanations on **other modalities**:
  - Vision (Quantus): [https://quantus.readthedocs.io/en/latest/](https://quantus.readthedocs.io/en/latest/)
  - NLP (e-ViL): [https://github.com/maximek3/e-ViL](https://github.com/maximek3/e-ViL)
  - Graphs (GraphXAI): [https://github.com/mims-harvard/GraphXAI](https://github.com/mims-harvard/GraphXAI)

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
