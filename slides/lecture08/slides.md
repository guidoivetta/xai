---
title: "\\emoji{wtf} XAI: Post-hoc - SmoothGrad \\& Integrated Gradients"
bibliography: references.bib

---

# Disclaimer

\input{../disclaimer.tex}

---

# Paper 1

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/smoothgrad_paper.png}
\end{center}

[@smilkov2017smoothgrad]

---

# Motivation

:::: columns
::: {.column width="48%"}

We want **post-hoc explanations of image classifiers**

## *Solution*:

- **Sensitivity maps** (a.k.a. saliency maps, pixel attribution maps)
- Visual interpretation of gradient of class activation function w.r.t input image
  - Structured as grayscale image w/ dimension same as input image
  - Brightness of pixel $\propto$ importance to classification decision

:::
::: {.column width="50%"}

\begin{center}
\includegraphics[width=0.45\columnwidth]{imgs/motivation_gazelle.png}
\end{center}

:::
::::

---

# Background: Gradients as Sensitivity Maps

- $N$: network that classifies images into one class from set $C$
- Given input image $x$, $N$ typically computes class activation function $S_c$ for each $c \in C$
- Final classification $\text{class}(x) = \text{argmax}_{c \in C} \, S_c(x)$
- **Sensitivity map given by**

$$M_c(x) = \partial S_c(x)/\partial x$$

- ***Intuition***: $M_c$ represents \underline{how much difference} a \underline{tiny change} in each pixel of $x$ would make to the classification score for class $c$.
- In practice, this is done with **backpropagation** — same as during training, but instead of updating weights, we stop at the input pixels. The result is a gradient map with one value per pixel.

---

# Related Work: Perturbation Methods

- **Key idea:** generate a perturbed dataset to fit an explainable model
  - LIME
  - KernelSHAP

\begin{center}
\includegraphics[width=0.60\columnwidth]{imgs/lime_perturbation.png}
\end{center}

---

# Related Work: Backpropagation

Smothgrad lives in the family of backpropagation-based methods for explaining neural networks.

\small
All methods propagate a signal backwards from the output to the inputs to assign importance scores to pixels — just like training, but stopping at the input. They differ in **how** they modify that signal along the way:

:::: columns
::: {.column width="30%"}

\begin{center}
\includegraphics[width=0.60\columnwidth]{imgs/backprop_network.png}
\end{center}

:::
::: {.column width="70%"}
\small
- **Vanilla gradients** — raw gradient $\partial S_c / \partial x$, no modifications. Baseline for SmoothGrad.
- **Integrated Gradients** — averages gradients along a path from a reference image to $x$.
- **DeepLIFT** — propagates activation *differences* relative to a reference, instead of raw gradients.
- **LRP** — redistributes output relevance backwards layer by layer using conservation rules.
- **Guided Backprop / Deconvolution** — discards negative gradients through ReLUs to highlight only positive contributions.

:::
::::

\begin{center}
\textbf{SmoothGrad is complementary}, not a replacement — it can be applied on top of any of these to reduce visual noise.
\end{center}


---

# Limitations of Sensitivity Maps

\begin{center}
\large \textbf{Visually noisy}
\end{center}

- Often highlight pixels that–to a human eye–seem randomly selected
- *a priori*, we cannot know if this noise reflects an underlying truth about how networks perform classification, or is due to more superficial factors
- This is why saliency maps are typically visualized as a heatmap-like plot.

\begin{center}
\includegraphics[width=0.50\columnwidth]{imgs/motivation_gazelle2.png}
\end{center}

---

# Theory Behind SmoothGrad: Noisy Gradients

\begin{center}
\large \textbf{Key idea:} Noisy maps are due to noisy gradients
\end{center}

- The derivative of $S_c$ may fluctuate sharply at small scales — networks use **ReLUs, so $S_c$ is not even continuously differentiable**.
- *Two images that look identical to a human can have very different gradients — so the raw gradient at a single point is not a reliable importance signal.*
- The noise you see in the map is not necessarily telling you something meaningful
it may just be an accident of the mathematical landscape of $S_c$


\begin{center}
\includegraphics[width=0.62\columnwidth]{imgs/noisy_gradients_plot.png}
\end{center}

---

# SmoothGrad: Intuition

\begin{center}
\large \textbf{Simple solution}
\end{center}

- take an image of interest
- sample similar images by adding Gaussian noise to the image
- take the average of the resulting sensitivity maps for each sampled image
- This \underline{smoothes} the gradient

---

# SmoothGrad: Algorithm

1. Take random samples in a neighborhood of an input $x$ with added noise
2. Average the resulting sensitivity maps

\textbf{
$$\hat{M}_c(x) = \frac{1}{n} \sum_{1}^{n} M_c(x + \mathcal{N}(0, \sigma^2))$$
}

\vspace{1em}

- $n$ is the number of samples,
- $\mathcal{N}(0, \sigma^2)$ represents Gaussian noise with standard deviation $\sigma$.

---

# Experimental Setup

- Performed SmoothGrad on visualizations of two neural networks:
  - Inception v3 model by Google that was trained on the ILSVRC-2013 dataset
  - Convolutional MNIST model based on the TensorFlow tutorial

\begin{center}
\includegraphics[width=0.55\columnwidth]{imgs/bombardino.png}
\end{center}


---

# Choosing Hyperparameters (${\sigma}$: std. dev.)

\begin{center}
\includegraphics[width=.75\columnwidth]{imgs/hyperparams_sigma.png}
\end{center}

:::: columns
::: {.column width="50%"}
\textbf{$\quad \hat{M}_c(x) = \frac{1}{n} \sum_{1}^{n} M_c(x + \mathcal{N}(0, \sigma^2))$}
:::
::: {.column width="50%"}
\textbf{${\sigma}$}: the standard deviation of the Gaussian noise
:::
::::

---

# Choosing Hyperparameters ($n$: sample size)

\textbf{
$$\hat{M}_c(x) = \frac{1}{n} \sum_{1}^{n} M_c(x + \mathcal{N}(0, \sigma^2))$$
}

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/hyperparams_n.png}
\end{center}


---

# Qualitative Results: Visualization Techniques

- **Absolute Value of Gradients**
  - depends on the characteristics of dataset

  \begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/abs.png}
\end{center}

- **Capping outlying values**
  - presence of few pixels that have much higher gradients than the average
  - capping to 99 percentile
- **Multiplying maps with images**
  - produce simpler \& sharper images (Shrikumar et al., 2017; Sundararajan et al., 2017)
  - Downside: Pixels with values of 0 will never show up on the sensitivity map.
  - Upside: when viewing the importance of the feature as contribution to the image

---

# Qualitative Results: Visual Coherence 1/2

\begin{definition}{\textbf{Visual Coherence}}
Highlights are only on the object of interest, not the background
\end{definition}

Comparison with three gradient-based methods

- Vanilla gradient
- Integrated Gradients
- Guided BackProp

---

# Qualitative Results: Visual Coherence 2/2

\begin{center}
\includegraphics[width=.88\columnwidth]{imgs/visual_coherence_fig5.png}
\end{center}

---

# Qualitative Results: Discriminativity

:::: columns

::: {.column width="40%"}

\begin{definition}{\textbf{Discriminativity}}
the ability to explain / distinguish separate objects without confusion
\end{definition}

\vspace{0.5em}

**Open Problem**

Which properties affect the discriminativity of a given methods?

- Why did GBP show the worst performance?

:::

::: {.column width="58%"}

![](imgs/discriminativity_fig6.png)

:::

::::

---

# Combining with Other Methods

\begin{columns}
\begin{column}{0.40\textwidth}

The same smoothing procedure can be used to augment any gradient-based method.

\end{column}
\begin{column}{0.58\textwidth}

\begin{center}
\includegraphics[width=\columnwidth]{imgs/combining_methods.png}
\end{center}

\end{column}
\end{columns}

---

# Limitations / Discussion

- Completely qualitative results, can we get **quantitative metrics**?
- Noisy sensitivity maps are **due to noisy gradients**
  - Is this true?
  - \underline{Future work}: look for further evidence and theoretical arguments
- Does SmoothGrad **generalize** to other networks \& tasks?
- How do we tradeoff between making picture pretty and being faithful to the model? Do you think SmoothGrad handled this tradeoff well?

---

# Paper 2

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/ig_paper.png}
\end{center}

[@sundararajan2017axiomatic]

---

# Intuition 1/2

\begin{center}
\textbf{How much happier would an extra \$1 make you... if you already have a billion dollars?}
\end{center}

\begin{center}
\includegraphics[width=0.3\columnwidth]{imgs/mrcrab.png}
\end{center}

- The answer is "almost nothing" — but that doesn't mean money is unimportant.
- This is **exactly the problem** with vanilla gradients:

\begin{center}
If the model is \textbf{already very confident}, the score function is flat at that point, and the gradient is near zero for all pixels — even the obviously important ones.
\end{center}

- The gradient is a local measure — it tells you how the function is changing right there. But if you've already reached a flat region, that local information is misleading.

---

# Intuition 2/2

**Integrated Gradients** solves this with the same intuition you'd use in optimization to escape flat-regions:

\begin{center}
\includegraphics[width=0.30\columnwidth]{imgs/yoda.png}
\end{center}

 This way you capture the global contribution of each feature, not just its local behavior.

---

# Motivation and Problem Statement 1/2

\begin{columns}
\begin{column}{0.60\textwidth}

\begin{definition}{\textbf{Feature Attribution}}
\small
\begin{itemize}
\item $F: \mathbb{R}^n \to [0,1]$ — deep network with $n$ input features
\item $x'$ — baseline input representing "absence of signal"
\item $A_F(x, x') = (a_1, \ldots, a_n)$ — attribution vector, same size as input
\item $a_i$ — contribution of feature $x_i$ to the prediction $F(x)$ relative to $x'$
\end{itemize}
\end{definition}

\end{column}
\begin{column}{0.35\textwidth}

\begin{center}
\includegraphics[width=\columnwidth]{imgs/ig_mnist_attribution.png}
\end{center}

\end{column}
\end{columns}

\small
- $F$ takes an image $x$ with $n$ pixels and returns a score between 0 and 1
- An **attribution** is a vector of the same size as $x$
- Each $a_i$ tells you how much pixel $x_i$ contributed to the final prediction
- Everything is measured relative to a reference image $x'$ — the **baseline**
- In other words: you distribute the output score among the input pixels, giving each one its "share of the blame"

------

# Motivation and Problem Statement 2/2

- **Feature attribution** is a vector of the same size as the input — each $a_i$ tells you how much feature $x_i$ contributed to the prediction $F(x)$
  - Ex. in a CNN, it reveals which pixels were responsible for a certain label being picked
  - LIME and SHAP are the same idea.

- **Problem:** attribution techniques are hard to evaluate empirically — hard to separate errors from the model vs errors from the attribution method
  - **Solution: axiomatic approach** — define mathematical properties that every attribution method *should* satisfy
  - Ex. Vanilla gradients *seem* reasonable but violate one of these axioms (Sensitivity) — provably, without needing experiments

- **Baseline** $x'$: a design choice — a reference input representing "absence of signal"
  - Attributions are always measured *relative* to it
  - Ex. black image for vision, zero embedding vector for text
  - A bad baseline leads to misleading attributions, even if the method is correct

---

# Summary of Contributions

The paper proposes an **axiomatic approach**: instead of evaluating attribution methods empirically, define mathematical properties they *must* satisfy.

- **Sensitivity:** if a feature clearly changes the prediction, its attribution cannot be zero — otherwise the method is lying. Most methods (including vanilla gradients) violate this.

- **Implementation Invariance:** two networks that compute the same function should give the same attributions — attributions should not depend on irrelevant implementation details. Methods like DeepLIFT and LRP violate this.

These 2 axioms guide the design of **Integrated Gradients**: average the gradients along the entire path from the baseline $x'$ to the input $x$ — satisfies both axioms, no network modification needed.

---

# Why Vanilla Gradients Fail: Violating Sensitivity 1/2

**Key idea:** use $\partial F / \partial x$ as a proxy for feature importance.

**Problem — breaks Sensitivity:** the prediction function can flatten at the input, giving zero gradient even when the feature clearly matters.

**Example:** single ReLU network $f(x) = 1 - \text{ReLU}(1-x)$, baseline $x=0$, input $x=2$:

---

# Why Vanilla Gradients Fail: Violating Sensitivity 1/1

**Example:** $f(x) = 1 - \text{ReLU}(1-x)$, baseline $x=0$, input $x=2$

**Step 1: ReLU recap**
$\text{ReLU}(z) = \max(0, z)$ — returns $z$ if positive, 0 if negative.

**Step 2: Evaluate at baseline $x=0$**
- $1 - x = 1 - 0 = 1$, $\text{ReLU}(1) = 1$, $f(0) = 1 - 1 = 0$

**Step 3: Evaluate at input $x=2$**
- $1 - x = 1 - 2 = -1$, $\text{ReLU}(-1) = 0$, $f(2) = 1 - 0 = 1$

**Step 4: Gradient at $x=2$**
- For any $x > 1$: $\text{ReLU}(1-x) = 0$ always — $f(x) = 1$, flat, derivative $= 0$


## Sensitivity violated
The prediction changed from 0 to 1, but the gradient says $x$ is irrelevant


---

# DeConvNets, Guided back-propagation (GBP) Also Break Sensitivity

\begin{center}
\includegraphics[width=0.70\columnwidth]{imgs/ig_break_sensitivity.png}
\end{center}

\fontsize{8pt}{6pt}
- **GBP Rule:** only backpropagate through a ReLU if it was **on** at the input.
- **Forward pass:** ReLU zeros out negative activations — red/yellow cells in $f^l$ become 0 in $f^{l+1}$.
- **Backward pass:** gradients are only propagated through ReLUs that were active at the input. Neurons zeroed out in the forward pass receive attribution 0 — even if their gradients in $f^{l+1}$ are non-zero.

## Same root cause as vanilla gradients
- The method only looks at the current input, not the full path from $x'$ to $x$.
- A feature that was off at the input gets attribution 0 — even if it clearly mattered for the prediction.

---

# Other Attribution Methods: Methods that Break Implementation Invariance

- DeepLift and Layer-wise relevance propagation (LRP)

\begin{center}
\includegraphics[width=0.60\columnwidth]{imgs/ig_break_invariance.png}
\end{center}

- Both methods **replace gradients with discrete gradients**, use a modified form of backpropagation.
- Chain rule doesn't hold for discrete gradients (calculating gradients would be different) $\to$ breaks implementation invariance.
- So attributions depend on internal implementation details — two functionally equivalent networks can give different attributions.

---

# The Method: Integrated Gradients

:::: columns
::: {.column width="48%"}

\begin{center}
\textbf{Definition}
\end{center}

The **path integral** of the gradients along the **straight-line path** from the baseline $x'$ to the input $x$.

\begin{center}
\textbf{
$$\text{IntegratedGrads}_i(x) :=$$
$$(x_i - x'_i) \times \int_{\alpha=0}^{1} \frac{\partial F(x' + \alpha \times (x-x'))}{\partial x_i} \, d\alpha$$}
\end{center}

:::
::: {.column width="48%"}

\begin{center}
\textbf{New Axiom}
\end{center}

**Completeness:** The sum of the attributions is equal to the difference of the outputs.

\vspace{0.5em}

\small
*Proposition 1.* If $F : \mathbb{R}^n \to \mathbb{R}$ is differentiable almost everywhere$^1$ then

$$\sum_{i=1}^{n} \text{IntegratedGrads}_i(x) = F(x) - F(x')$$

:::
::::

\vspace{1.5em}


\fontsize{8pt}{6pt}
> **"Differentiable almost everywhere"** means F can have a few points where the derivative doesn't exist (like the corners of a ReLU), but there are so few of them that they don't affect the integral. Typical neural networks satisfy this.

---

# The Method:  Paths Methods and Uniqueness of Integrated Gradients

\small
- **Paths:** Images interpolated between the baseline and the input. For example, if the baseline is a black image and the input is a photo of an elephant, the path is a sequence of images that gradually 'fade in' from black to the full image.
- Integrated Gradients is the canonical method among **all possible** path-based attribution methods.

:::: columns
::: {.column width="50%"}

\begin{center}
\includegraphics[width=.8\columnwidth]{imgs/ig_path_methods.png}
\end{center}

:::
::: {.column width="50%"}

\begin{center}
\textbf{
$$\text{PathIntegratedGrads}_i^\gamma(x) :=$$
$$\int_{\alpha=0}^{1} \frac{\partial F(\gamma(\alpha))}{\partial \gamma_i(\alpha)} \frac{\partial \gamma_i(\alpha)}{\partial \alpha} \, d\alpha$$
}
\end{center}

:::
::::

---

# The Method:  Paths and why $P_2$

\small
\begin{center}
\textbf{Axioms}
\end{center}

- **Sensitivity (b):** If the function does not depend (mathematically) on some input, then the attribution for that input is always zero.
- **Linearity:** Attributions preserve any linearity within the network.
$$a \times f_1 + b \times f_2$$
- **Symmetry-Preserving:** For symmetric variables, if they have identical values in the input and identical values in the baseline, they then receive identical attributions.
$$\text{Si} \ F(x, y) = F(y, x)$$


## Why $P_2$
\textbf{$P_2$ (straight line) is the only path that satisfies all three axioms simultaneously} — it is the simplest, most canonical choice. 

---

# The Method: Using Integrated Gradients

:::: columns
::: {.column width="48%"}

\begin{center}
\textbf{Selecting a Baseline}
\end{center}
\vspace{1em}

The baseline $x'$ must satisfy two conditions:

- **Zero-Score:** $F(x') \approx 0$ — so attributions sum directly to the final prediction
- **Absence of Signal:** must not contain information that could contaminate attributions

**Examples:**

- Object Recognition: all-black image
- Text: all-zero input embedding vector

:::
::: {.column width="50%"}

\begin{center}
\textbf{Computing IGs}
\end{center}
\vspace{1em}

The integral is approximated with a Riemann sum over $m$ evenly-spaced points along the path:

\begin{center}
$$\text{IntegratedGrads}_i^{\text{approx}}(x) :=$$
$$(x_i - x'_i) \times \sum_{k=1}^{m} \frac{\partial F\!\left(x' + \frac{k}{m} \times (x-x')\right)}{\partial x_i} \times \frac{1}{m}$$
\end{center}

$m \in [20, 300]$ steps is sufficient in practice. **Sanity check:** attributions should sum to $F(x) - F(x')$.

:::
::::

---

# Experimental Results: Object Recognition CNN


**Task:** Given image, predict the category of the object

\begin{center}
\includegraphics[width=0.88\columnwidth]{imgs/ig_object_recognition.png}
\end{center}

- Fireboat: shows watter
- Butterfly: Leaf


---

# Question Classification CNN

**Task:** Given question, predict what **type** of answer it is looking for.

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/ig_question_classification.png}
\end{center}

---

# Machine Translation RNN

**Task:** Given English sentence, predict German translation

\begin{center}
\includegraphics[width=0.88\columnwidth]{imgs/ig_machine_translation.png}
\end{center}

---

# Conclusion and Discussion

\textbf{Summary}

- Formalizes two axioms for attribution: **sensitivity, implementation invariance**
- Propose **integrated gradients** and argue that it is theoretically superior to other gradient-based methods (e.g. DeepLift, LRP, guided backprop, etc.)
- Perform experiments across several domains to showcase method

\textbf{Discussion Questions}

- Are you convinced that these axioms are desirable?
- Do you see any strengths or weaknesses in the idea of producing explanations through an integrated path?
- Have the experiments convinced you of the superiority of their method?

---

\begin{center}
\Huge Thank You!
\end{center}

---

# References {.allowframebreaks}

\footnotesize
