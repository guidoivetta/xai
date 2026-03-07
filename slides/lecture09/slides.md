---
title: "\\emoji{wtf} XAI Lecture 09"
subtitle: "Adversarial Attacks on Explanations"
bibliography: references.bib

---

# Disclaimer

\input{../disclaimer.tex}

---

# Paper 1

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/paper1.png}
\end{center}

[@slack2020fooling]

---

# Motivation

- ML is increasingly used for **critical** decisions
  - Healthcare, criminal justice, finance
- Decision makers must **understand model behavior** to:
  - Diagnose errors and potential biases
  - Decide when and how much to trust these models
- This motivates the need for **explainable AI (XAI)** tools
  - e.g., LIME (Ribeiro et al., 2016) and SHAP (Lundberg & Lee, 2017)

---

# Motivation

- Trade-off between interpretability and accuracy
  - **Simple** models can be easily **interpreted** (e.g., linear regression)
  - **Complex** but also black-box model has much **better performance** (e.g., deep neural network)
- Can a ML method be both \textcolor{primarygreen}{\textbf{interpretable}} and \textcolor{red}{\textbf{accurate}}?
- *Post hoc* explanation can seemingly solve this problem:
  - First build \textcolor{primarygreen}{\textbf{complex and accurate}} ML models for good performance
  - Then use post hoc explanation for model \textcolor{primarygreen}{interpretation}
- The question is:
  - How robust and reliable is the *post hoc* explanation methods?

---

# Contribution: A Framework to 'Fool' Post Hoc Explanations

- A **scaffolding** framework that hides the biases of any black box classifier
  - Targets **perturbation-based** explanation methods (LIME & SHAP)
  - Lets an adversary craft arbitrary, innocuous-looking explanations
- Evaluated on real-world datasets with extremely biased classifiers
  - COMPAS, Communities & Crime, German Credit
- **Key takeaway:** LIME and SHAP are **not robust enough** to detect
  discriminatory behavior in adversarial settings

---

# Perturbation-based Post Hoc Explanation Method

\begin{center}
\includegraphics[width=0.25\columnwidth]{imgs/lime_perturbation.png}
\end{center}

\begin{center}
\textbf{Preliminaries \& Background}
\end{center}

:::: columns
::: column

$$\arg\min_{g \in \mathcal{G}} L(f, g, \pi_x) + \Omega(g)$$

:::
::: column

where the loss function $L$ is defined as:
$$L(f, g, \pi_x) = \sum_{x' \in X'} [f(x') - g(x')]^2 \pi_x(x')$$

:::
::::

\small
- $f$ is the original classifier and $x$ is the datapoint we want to explain
- $g$ is the explanation we want to learn, $\Omega(g)$ is the "complexity" of $g$
- $\pi$ is the proximity measure
- $X'$ is a **synthetic dataset**, consisting of perturbations of $x$

---

# Intuition

:::: columns
::: column

\includegraphics[width=\columnwidth]{imgs/compas_pca.png}

:::
::: column

- LIME and SHAP explain predictions by **perturbing** input instances
- These perturbations often fall **outside the real data distribution** (out-of-distribution, OOD)
- Key observation: OOD points are **easily distinguishable** from real data

\vspace{1em}

**If we can detect whether a point is a perturbation or real data,
we can make the model behave differently on each — and fool the explainer.**

:::
::::

---

# Approach: Set-up

\begin{center}
\large
\textbf{Adversary would like to deploy a biased classifier $f$!}
\end{center}

- **Background:** the biased model **f** uses sensitive attributes to make critical decisions
- **Requirement:** give access of black-box models to customers and regulators who use post-hoc explanations
- **Goal:** hide bias of the classifier **f**

\begin{flushright}
\includegraphics[width=.8\columnwidth]{imgs/burns.png}
\end{flushright}

---

# Approach: Set-up

**Goal:** build an adversarial classifier $\tilde{e}$ that wraps any biased model $f$

- **Input:** dataset $X$ sampled from the real-world distribution $\mathcal{X}_{dist}$
- **Output:** adversarial classifier $\tilde{e}$ defined as:

$$\tilde{e}(x) = \begin{cases} f(x) & \text{if } x \in \mathcal{X}_{dist} \quad \text{(real data → biased behavior)} \\ \psi(x) & \text{otherwise} \quad \text{(perturbations → innocuous behavior)} \end{cases}$$

where $f$ is the **biased** classifier and $\psi$ is an **unbiased** classifier

## It's a Trap

On real data, $\tilde{e}$ behaves like $f$. On OOD perturbations, it looks fair.

---

# Approach: OOD Detection

**Key question:** given input $x$, does it come from $\mathcal{X}_{dist}$ or is it a perturbation?

**Solution:** train a binary classifier `is_OOD(x)` using synthetic labels:

| Data | Label |
|------|-------|
| Original instances $X$ | `False` (real data) |
| Perturbed instances $X_p$ | `True` (OOD) — unless too close to $X$ |

- Perturbations are generated the same way LIME/SHAP would generate them
- Any off-the-shelf classifier works (authors use Random Forest)


## Simple explained

`is_OOD(x)` is the gatekeeper: it decides whether $\tilde{e}$ runs $f$ or $\psi$

---

# How hard can it be to implement this? \emoji{snake.png}

\fontsize{8pt}{6pt}
```python
# Step 1: Generate perturbations (same method as LIME/SHAP)
X_perturbed = perturb(X)

# Step 2: Remove perturbations too close to real data
X_ood = [x for x in X_perturbed if not too_close(x, X)]

# Step 3: Build labeled dataset
X_train = X        + X_ood
y_train = [False]  + [True]   # False = real, True = OOD

# Step 4: Train OOD detector
is_OOD = RandomForest().fit(X_train, y_train)

# Step 5: Build adversarial classifier
def e(x):
    if not is_OOD(x):   # real data → biased behavior
        return f(x)
    else:               # perturbation → innocuous behavior
        return psi(x)
```

---

# How hard can it be to implement this? \emoji{snake.png}

\fontsize{8pt}{6pt}
```python
# Step 1: Generate perturbations (same method as LIME/SHAP)
X_perturbed = perturb(X)

# Step 2: Remove perturbations too close to real data
X_ood = [x for x in X_perturbed if not too_close(x, X)]

# Step 3: Build labeled dataset
X_train = X        + X_ood
y_train = [False]  + [True]   # False = real, True = OOD

# Step 4: Train OOD detector
is_OOD = RandomForest().fit(X_train, y_train)

# Step 5: Build adversarial classifier
def e(x):
    if not is_OOD(x):   # real data → biased behavior
        return f(x)
    else:               # perturbation → innocuous behavior
        return psi(x)
```

## Now for real! \emoji{snake.png}

Let's ask an AI agent to code it properly — using the scikit-learn predictor interface

\emoji{link.png} [adversarial_scaffold.py \emoji{snake.png}](https://github.com/leliel12/xai/blob/2026/slides/lecture09/codes/adversarial_scaffold.py)

---

# Experiment: Set-up

![](imgs/datasets.png)

- Biased classifier **f** makes predictions purely based on sensitive attributes (race, gender)
- Unbiased classifier **$\psi$** uses only features uncorrelated with the sensitive attributes

## Social Biases

We are not looking for a flaw in the mechanics of the calculation, but for the persistence of historical patterns that arbitrarily prioritize or exclude certain groups

---

# Experiment: Results — COMPAS

:::: columns
::: column

- Each bar shows how often a feature appears at a given importance rank (1st, 2nd, 3rd) across test instances

- **LIME:** the attack is fully successful — race disappears from all explanations in 100% of instances
- **SHAP:** effective with 1 feature (84%), but less so with 2 — SHAP's local accuracy property
  distributes attribution across features, making it harder to concentrate on a single decoy

:::
::: column

\begin{center}
\includegraphics[width=\columnwidth]{imgs/compas_results.png}
\end{center}

:::
::::

---

# Experiment: Results — Communities and Crime

:::: columns
::: column

- Each bar shows how often a feature appears at a given importance rank (1st, 2nd, 3rd) across test instances
- **LIME:** the attack succeeds in both settings — race is effectively hidden in nearly 100% of instances
- **SHAP:** partially effective with 1 feature, but race re-emerges at lower ranks with 2 features —
  consistent with SHAP's local accuracy constraint distributing attribution more broadly

:::
::: column

\begin{center}
\includegraphics[width=\columnwidth]{imgs/communities_results.png}
\end{center}

:::
::::


---

# Experiment: Results — German Credit

\begin{center}
\includegraphics[width=0.65\columnwidth]{imgs/german_results.png}
\end{center}

- Here $\psi$ uses a **real feature** (Loan Rate % Income) instead of a synthetic uncorrelated one
- Both LIME and SHAP attacks succeed: gender disappears from the top-3 in ~91% and ~85% of instances respectively
- Using a real feature as a decoy produces the cleanest attack — it is more natural and harder to detect

---

# Takeaway from Experiments

1. Accuracy of the OOD classifier $\to$ success of the adversarial attack
2. Adversarial classifiers to LIME are ineffective against SHAP explanations
   a. Any sufficiently accurate OOD classifier is sufficient to fool LIME, while fooling SHAP requires more accurate classifiers
3. SHAP less successful when using two features $\leftarrow$ local accuracy property
   a. Distribute attributions among several features


---

# Related Works

- Issues with post-hoc explanations:
  - **Doshi-Velez and Kim** identify explainability of predictions as a potentially useful feature of interpretable models.
  - **Lipton** and **Rudin** argues post-hoc explanations can be misleading and are not trustworthy for sensitive applications.
  - **Ghorbani et al.** and **Mittelstadt et al.** identified further weaknesses of post-hoc explanations.
- Adversarial explanations
  - **Dombrowski et al.** and **Heo et al.** show how to change saliency maps in arbitrary ways by imperceptibly changing inputs.

---

# Q\&A

- Are the experimental results sufficient to justify the conclusions?
  - In particular, how can we explain the discrepancy in results for LIME vs. SHAP?
- What about fooling other classes of post-hoc explanation methods?
  - Past work: gradient-based methods
- Alternatively, can one design post-hoc explanations that are *adversarially robust*?

---

# Paper 2

\begin{center}
\includegraphics[width=0.75\textwidth]{imgs/paper2.png}
\end{center}

[@dombrowski2019explanations]


---

# Motivation

- Explanation methods aim to make ML models more **trustworthy** and **interpretable**
  - Understand and verify model behavior
  - Aid decision making in high-stakes scenarios (healthcare, criminal justice)
- This requires **reliable** explanations

## Can we always trust model explanations?

This paper shows **the answer is no** — explanations can be manipulated arbitrarily
with imperceptible input perturbations, while keeping the model's output unchanged.

---

# Summary / Contribution 1/2

::: columns
:::: column

- Manipulate explanations! \emoji{smiling-face-with-horns.png}
- Provide a theoretical understanding of such nonrobustness and derive a bound \emoji{thinking-face.png}
- Introduce smoothing to increase explanation robustness! \emoji{smiling-face-with-sunglasses.png}


::::
:::: column

![](imgs/dog_manipulation.png){width=95%}

::::
:::

## The key insight of the entire paper

The gradient is highly sensitive to small input changes — like a model that memorizes instead
of generalizing, it **overfits** to each point on the manifold and changes drastically between neighbors.

---

# Summary / Contribution 2/2


\begin{center}
\includegraphics[width=0.35\columnwidth]{imgs/dog_manipulation.png}
\end{center}

The bound makes this precise: the change in explanation is proportional to the **curvature** of the manifold:

$$\|h(p) - h(p_0)\| \leq |\lambda_{max}| \, d_g(p, p_0)$$

- $|\lambda_{max}|$ — curvature: how severely the gradient overfits locally
- $d_g(p, p_0)$ — geodesic distance: how far apart the two inputs truly are on the manifold

---

# Background + Related Work

- **Interpretation of Neural Networks is Fragile** — Ghorbani et al. (2019)
  - Small input perturbations cause unstructured, unpredictable changes in explanation maps

- **The (Un)reliability of Saliency Methods** — Kindermans et al.
  - Explanations should be invariant to constant input shifts — many methods fail this basic test

- **Sanity Checks for Saliency Maps** — Adebayo et al.
  - Randomizing network weights should destroy explanations — surprisingly, some methods are insensitive

- **Fairwashing with Off-Manifold Detergent** — Anders et al.
  - Biased models can hide their behavior by exploiting the gap between the true data manifold
    and the high-dimensional embedding space

---

# Methodology -  Notation

## Model

A neural network $g : \mathbb{R}^d \to \mathbb{R}^K$ with ReLU non-linearities

- Predicted class: $k = \arg\max_i \, g(x)_i$
- Explanation map: $h : \mathbb{R}^d \to \mathbb{R}^d$ — assigns a relevance score to each pixel

## Goal of the attack:

Given input $x$, find a manipulated image $x_{adv} = x + \delta x$ such that:

1. $h(x_{adv}) \approx h^t$ — explanation matches an arbitrary target map
2. $g(x_{adv}) \approx g(x)$ — network output stays unchanged
3. $\|\delta x\| \ll 1$ — perturbation is imperceptible

---

# Properties of Manipulated Image

The attack constructs $x_{adv} = x + \delta x$ satisfying three conditions simultaneously:

1. **Prediction unchanged:** $g(x_{adv}) \approx g(x)$ — the model still outputs the same class with the same confidence

2. **Explanation hijacked:** $h(x_{adv}) \approx h^t$ — the explanation now shows whatever the attacker wants, regardless of the true model behavior

3. **Perturbation imperceptible:** $\|\delta x\| \ll 1$ — the modified image looks identical to the original

---

# The Explanation Methods Under Attack

## Gradient-based

- **Vanilla Gradients:** $h(x) = \frac{\partial g}{\partial x}(x)$
  - Quantifies how infinitesimal perturbations in each pixel change the prediction
- **Gradient × Input:** $h(x) = x \odot \frac{\partial g}{\partial x}(x)$
  - For linear models, gives the exact contribution of each pixel to the prediction
- **Integrated Gradients:** $h(x) = (x - \bar{x}) \odot \int_0^1 \frac{\partial g(\bar{x} + t(x - \bar{x}))}{\partial x} \, dt$
  - Accumulates gradients along the path from a baseline $\bar{x}$ to the input $x$

## Propagation-based

- **Guided Backpropagation (GBP):** gradient explanation with negative components zeroed out during backprop
- **Layer-wise Relevance Propagation (LRP):** propagates relevance scores backwards through the network layers
- **Pattern Attribution (PA):** standard backpropagation with weights scaled by learned patterns

---

# Manipulation Method 1/3

\begin{center}
Obtain manipulated images by optimizing the loss function:
\end{center}

\textbf{
    $$\mathcal{L} = \|h(x_{adv}) - h^t\|^2 + \gamma \|g(x_{adv}) - g(x)\|^2$$}

\vspace{0.3cm}

with respect to $x_{adv}$ using gradient descent

\vspace{0.5cm}

\footnotesize
- $h(x_{adv})$: manipulated explanation map
- $h^t$: target map
- $\gamma$: weighting hyperparameter (free parameter)
- $g(x_{adv})$: network output (manipulated input)
- $g(x)$: network output (original input)

---

# Manipulation Method 2/3

\begin{center}
Obtain manipulated images by optimizing the loss function:
\end{center}

\textbf{
    $$\mathcal{L} = \|h(x_{adv}) - h^t\|^2 + \gamma \|g(x_{adv}) - g(x)\|^2$$}

\vspace{0.3cm}

- **First term:** penalizes deviation from the target map $h^t$ — the optimizer wants the explanation to match exactly what the attacker chose
- **Second term:** penalizes any change in the network output — the optimizer wants the prediction to stay identical
- **$\gamma$:** controls the trade-off
  - Large $\gamma$ → preserving the prediction takes priority
  - Small $\gamma$ → manipulating the explanation takes priority, even at the cost of slightly changing the output


---

# Manipulation Method 3/3

\begin{center}
Obtain manipulated images by optimizing the loss function:
\end{center}

:::: columns
::: column

\textbf{
    $$\mathcal{L} = \|h(x_{adv}) - h^t\|^2 + \gamma \|g(x_{adv}) - g(x)\|^2$$}

:::
::: column

\begin{center}
\includegraphics[width=.6\columnwidth]{imgs/dog_manipulation2.png}
\end{center}

:::
::::

\begin{center}
\large
\textbf{
Find an image that looks identical to the original, predicts the same class, but whose explanation says whatever the attacker wants.}
\end{center}


---

# Manipulation Method: Softplus Trick

\small
To minimize $\mathcal{L}$ with gradient descent, we need to compute the gradient of the loss with respect to $x_{adv}$.
But that gradient involves the second derivative of the network:

$$\partial_{x_{adv}} \|h(x_{adv}) - h^t\|^2 \propto \frac{\partial h}{\partial x_{adv}} = \frac{\partial^2 g}{\partial x^2_{adv}} \propto \text{relu}'' = 0$$

ReLU has second derivative exactly zero everywhere — there is no signal for the optimizer to follow.

**Solution:** replace ReLU with softplus during optimization:

$$\text{softplus}_\beta(x) = \frac{1}{\beta} \log(1 + e^{\beta x})$$

Softplus is a smoothed version of ReLU, nearly identical for large $\beta$, but with a well-defined second derivative. Once optimization is complete, $x_{adv}$ is tested on the original ReLU network.

---

# Experiments - Experimental Setup

- Apply algorithm to 100 randomly selected images for each explanation method
- Use VGG-16 network pre-trained on ImageNet
- For each run, randomly select two images from the test set:
  - One of the two images is used to generate a target explanation map
  - The other image is perturbed by the algorithm with the goal of replicating the target using a few thousand iterations of gradient descent

\vspace{0.5cm}

- Comparable results obtained for ResNet-18, AlexNet, and Densenet-121 + CIFAR-10 dataset

---

# Results: Visual Comparison

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/explanation_methods_visual.png}
\end{center}

---

# Results: Quantitative Metrics

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/similarities_boxplot.png}
\end{center}

---

# Theoretical Analysis

---

# Intuition

\textcolor{primarygreen}{Why} are explanations vulnerable and unreliable?

\textcolor{primarygreen}{Large curvature} of the NN output manifold!

\begin{center}
\includegraphics[width=0.65\columnwidth]{imgs/curvature_intuition.png}
\end{center}

[@ghorbani2019interpretation]

---

# Theoretical Bound

\begin{block}{Theorem 1}
Let $g : \mathbb{R}^d \to \mathbb{R}$ be a network with $\text{softplus}_\beta$ non-linearities and $\mathcal{U}_\epsilon(p) = \{x \in \mathbb{R}^d; \|x - p\| < \epsilon\}$ an environment of a point $p \in S$ such that $\mathcal{U}_\epsilon(p) \cap S$ is fully connected. Let $g$ have bounded derivatives $\|\nabla g(x)\| \geq c$ for all $x \in \mathcal{U}_\epsilon(p) \cap S$. It then follows for all $p_0 \in \mathcal{U}_\epsilon(p) \cap S$ that

$$\|h(p) - h(p_0)\| \leq |\lambda_{max}| \, d_g(p, p_0) \leq \beta C \, d_g(p, p_0)$$

where $\lambda_{max}$ is the principle curvature with the largest absolute value for any point in $\mathcal{U}_\epsilon(p) \cap S$ and the constant $C > 0$ depends on the weights of the neural network.
\end{block}

---

# Robustness via Smoothing

\begin{columns}
\begin{column}{0.5\textwidth}
\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/smoothing_illustration.png}
\end{center}
\end{column}
\begin{column}{0.48\textwidth}
$$\text{softplus}_\beta(x) = \frac{1}{\beta} \log(1 + e^{\beta x})$$

Replacing relu with softplus reduces the curvature $\to$ more robust explanations
\end{column}
\end{columns}

---

# Smoothing: Connections to SmoothGrad

\begin{block}{Theorem 2}
For a one-layer neural network $g(x) = \text{relu}(w^T x)$ and its $\beta$-smoothed counterpart $g_\beta(x) = \text{softplus}_\beta(w^T x)$, it holds that

$$\mathbb{E}_{\epsilon \sim p_\beta}[\nabla g(x - \epsilon)] = \nabla g_{\frac{\beta}{\|w\|}}(x)$$

where $p_\beta(\epsilon) = \frac{\beta}{(e^{\beta\epsilon/2} + e^{-\beta\epsilon/2})^2}$.
\end{block}

\vspace{0.5cm}

- \textbf{SmoothGrad} $\equiv$ **$\beta$-smoothing**
- $\epsilon_i \approx \mathcal{N}(0, \sigma)$ with variance $\sigma = \log(2) \frac{\sqrt{2\pi}}{\beta}$

---

# Robustness Experiments

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/robustness_exp1.png}
\end{center}

\footnotesize Figure 4. $\beta$-smoothing makes explanations more robust.

---

# Robustness Experiments

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/robustness_exp2.png}
\end{center}

\footnotesize Figure 5. $\beta$-smoothing 1) makes explanations more robust, 2) is comparable to SmoothGrad, 3) has a faster runtime than SmoothGrad.

---

# Conclusion

---

# Critique

## Strengths

- Thorough investigation: problem $\to$ reason $\to$ solution
- Extensive validation: various explanation methods, models, and datasets

## Limitations

- Analyses focused on relu/softplus activation function
- Evaluation of robustness based on Pearson correlation coefficient

---

# Future Directions \& Food for Thought

## Future directions

- Extend empirical analyses to other tasks and data modalities
- Generalize theoretical analyses to propagation-based methods
- Modify model training process to make NNs less vulnerable to explanation manipulation
  - Low-curvature models [Srinivas et al., NeurIPS 2022]

## Food for thought

- Might there be other reasons for explanations being sensitive to manipulation?
- What are other ways to evaluate robustness of explanations?
- Is it a good idea to trade-off faithfulness for better robustness?

---

\begin{center}
\Huge Thank You!
\end{center}

---

# References {.allowframebreaks}

\footnotesize
