---
title: "\\emoji{wtf} XAI: LIME \\& SHAP"
bibliography: references.bib

---

# Disclaimer

\input{../disclaimer.tex}

---

# "Why Should I Trust You?" Explaining the Predictions of Any Classifier

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/lime_explanation_flow.png}
\end{center}

\begin{center}
\footnotesize Ribeiro, Singh, Guestrin (2016) — Presented by Robin Na, Paul Liu, Zelin (James) Li
\end{center}

[@ribeiro2016should]

---

# Define Trust

- **Trusting a prediction:** whether a user trusts sufficiently to take some action based on it

\vspace{1em}

- **Trusting a model:** whether a user trusts a model to behave in reasonable ways if deployed

---

# Define Explanation for a Prediction

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/lime_explanation_flow.png}
\end{center}

\begin{block}{}
Textual or visual artifacts to provide qualitative understanding of the relationship between instance's components and the model's prediction.
\end{block}

---

# Explanations as a Means to Select Model

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/model_selection.png}
\end{center}

---

# Why Do We Need Trust and Interpretability?

- Sometimes models can go wrong (in a way that's obvious to humans)!

\vspace{0.5em}

- **Data leakage:** patient ID being correlated with the target class

\vspace{0.5em}

- **Dataset shift:** training data is different than the test data

\vspace{0.5em}

- **Exploiting features:** users may favor recommender systems that don't exploit on "clickbaits"

---

# Desired Characteristics for Explainers

- **Interpretable**
- **Local fidelity:** at least locally faithful
- **Model-agnostic:** the ability to explain any model
- **Global perspective:** ability to explain the model not just single prediction

\vspace{1em}

## LIME as Interpretable Framework

**Local Interpretable Model-agnostic Explanation**

---

# LIME as Interpretable Framework

## Step 1: Define LIME Framework
*(Ensure both local fidelity and interpretability)*

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/lime_formula.png}
\end{center}

$$\xi(x) = \underset{g \in G}{\text{argmin}} \ \mathcal{L}(f, g, \pi_x) + \Omega(g)$$

- $\xi(x)$: an instance
- $f$: model to be explained
- $g \in G$: interpretable model
- $\pi_x$: proximity measure to define locality
- $\mathcal{L}$: measure of unfaithfulness
- $\Omega(g)$: complexity measure

---

# LIME as Interpretable Framework

## Step 2: Interpretable Data Representation

- **Text:** binary vector indicating the presence or absence of a word
- **Image:** binary vector indicating the presence or absence of a contiguous patch of similar pixels

$$x \in \mathbb{R}^d \rightarrow x' \in \{0,1\}^{d'}$$

\begin{center}
\footnotesize Original Representation $\longrightarrow$ Interpretable Representation
\end{center}

---

# LIME as Interpretable Framework

## Step 3: Approximate Locality-Aware $\min_g \ \mathcal{L}(f, g, \pi_x)$

**Perturbed Sample ($z'$) Sampling Procedure:**

- Sample around $x'$ by drawing nonzero elements of $x'$ uniformly at random
- The number of draws is also uniformly sampled
- $z'$ basically has a fraction of nonzero elements of $x'$
- Samples are weighted by $\pi_x$

$$x \rightarrow x' \rightarrow z' \rightarrow z \rightarrow f(z)$$

\begin{center}
\footnotesize interpretable repr. $\to$ sampling local area $\to$ inverse (interpr. repr.) $\to$ obtain label
\end{center}

---

# Sampling Procedure Intuition

\begin{center}
\includegraphics[width=0.65\columnwidth]{imgs/sampling_intuition.png}
\end{center}

\begin{exampleblock}{}
A complex decision boundary is approximated locally by a simple linear model (dashed line). Samples closer to the instance of interest (red cross) are weighted more.
\end{exampleblock}

---

# Example: Sparse Linear Explanation

\begin{columns}
\begin{column}{0.48\textwidth}

$$\xi(x) = \underset{g \in G}{\text{argmin}} \ \mathcal{L}(f, g, \pi_x) + \Omega(g)$$

$$g(z') = w_g \cdot z'$$

$$\pi_x(z) = \exp\!\left(-\frac{D(x,z)^2}{\sigma^2}\right)$$

$$\mathcal{L}(f,g,\pi_x) = \sum_{z,z' \in \mathcal{Z}} \pi_x(z)\bigl(f(z)-g(z')\bigr)^2$$

$$\Omega(g) = \infty \mathbb{1}[\|w_g\|_0 > K]$$

\end{column}
\begin{column}{0.48\textwidth}

\begin{center}
\includegraphics[width=\columnwidth]{imgs/sparse_linear.png}
\end{center}

\end{column}
\end{columns}

---

# Some Results

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/some_results.png}
\end{center}

---

# Gain Global Understanding of the Model

## Proposal: Explain a set of individual instances

- The number of instances should be small (denoted by budget $B$)
- The pick step should account for the explanations that accompany each prediction
- Should pick a **diverse, representative set**

---

# Submodular Pick (SP) Algorithm

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/submodular_pick.png}
\end{center}

$$c(V, \mathcal{W}, I) = \sum_{j=1}^{d'} \mathbb{1}_{[\exists i \in V: \mathcal{W}_{ij} > 0]} I_j \qquad \text{(submodular)}$$

$$\text{Pick}(\mathcal{W}, I) = \underset{V, |V| \leq B}{\text{argmax}} \ c(V, \mathcal{W}, I)$$

\begin{alertblock}{}
Submodularity has the property of diminishing returns — greedy optimization yields a near-optimal solution.
\end{alertblock}

---

# Simulated User Experiment

## Experimental Setup

- Models: Decision Tree, Logistic Regression, Nearest Neighbors, SVM, RandomForest
- Compare with **parzen**, **greedy**, and **random** procedures:
  - *Greedy:* greedily remove features that contribute the most until prediction changes
  - *Random:* randomly select $K$ features
- Pick procedures: **Submodular Pick (SP)** and **Random Pick (RP)**

---

# Simulated User Experiment

## Are explanations faithful to the method?

\begin{columns}
\begin{column}{0.48\textwidth}

- Train sparse logistic regression and decision trees (interpretable $\Rightarrow$ know gold set features)
- Compute average fractions of gold features covered by the explanations (over all instances)

\end{column}
\begin{column}{0.48\textwidth}

\begin{center}
\includegraphics[width=\columnwidth]{imgs/simulated_faithful.png}
\end{center}

\end{column}
\end{columns}

\begin{exampleblock}{}
LIME achieves the highest recall of truly important features on both Books and DVDs datasets.
\end{exampleblock}

---

# Simulated User Experiment

## Should I trust this prediction?

1. Randomly select 25% of features to be untrustworthy
2. Label predictions as untrustworthy if prediction changes when all untrustworthy features are removed
   - For greedy and random: untrustworthy if untrustworthy features present

\begin{center}
\includegraphics[width=0.65\columnwidth]{imgs/simulated_trust.png}
\end{center}

\begin{exampleblock}{}
LIME achieves the highest average F1 of trustworthiness across all classifiers and datasets.
\end{exampleblock}

---

# Simulated User Experiment

## Can I trust this model?

\begin{columns}
\begin{column}{0.48\textwidth}

1. Add noisy features to create spurious correlations
2. Train two random forests:
   - Validation accuracy within 0.1% of each other
   - Test accuracy differs by at least 5%
3. Mark noisy features as untrustworthy and follow a similar procedure

\end{column}
\begin{column}{0.48\textwidth}

\begin{center}
\includegraphics[width=\columnwidth]{imgs/simulated_model.png}
\end{center}

\end{column}
\end{columns}

---

# Evaluating with Human Subjects

## Experimental Setup

- Previous 20 newsgroups dataset (Problematic!) — contains features that do not generalize
- Create a **new religion dataset:** 819 web pages in each of "Christianity" and "Atheism"
- Use SVM with RBF Kernel with hyperparameters chosen by cross-validation

---

# Evaluating with Human Subjects

## Can users select the best classifier?

\begin{columns}
\begin{column}{0.48\textwidth}

- Train two SVMs:
  - one on problematic dataset
  - one on "cleaned" dataset
- Recruit humans to select which algorithm will perform best

\end{column}
\begin{column}{0.48\textwidth}

\begin{center}
\includegraphics[width=\columnwidth]{imgs/human_classifier.png}
\end{center}

\end{column}
\end{columns}

\begin{exampleblock}{}
SP-LIME (89\%) outperforms RP-LIME (75\%), and both outperform greedy variants.
\end{exampleblock}

---

# Evaluating with Human Subjects

## Can non-experts improve a classifier?

\begin{columns}
\begin{column}{0.48\textwidth}

Human marks which words to remove after seeing $B=10$ instances and $K=10$ words in explanation.

\vspace{0.5em}
- 10 subjects $\to$ train 10 classifiers
- 5 more users $\to$ 50 classifiers
- 5 more users $\to$ 250 classifiers

\end{column}
\begin{column}{0.48\textwidth}

\begin{center}
\includegraphics[width=\columnwidth]{imgs/human_improve.png}
\end{center}

\end{column}
\end{columns}

\begin{exampleblock}{}
SP-LIME outperforms RP-LIME in real-world accuracy across rounds of interaction.
\end{exampleblock}

---

# Evaluating with Human Subjects

## Do explanations lead to insights?

\begin{columns}
\begin{column}{0.5\textwidth}

1. Find pictures such that classifier predicts "wolf" if there is snow, and "husky" otherwise
2. Ask subjects (grad students):
   - Do they trust model to work well in real world?
   - Why?
   - How do they think the model distinguishes?
3. Showed explanations and asked again

\end{column}
\begin{column}{0.45\textwidth}

\begin{center}
\includegraphics[width=\columnwidth]{imgs/husky_wolf.png}
\end{center}

\end{column}
\end{columns}

\begin{alertblock}{}
After seeing explanations: trusted the bad model dropped from 10/27 to 3/27; snow identified as feature rose from 12/27 to 25/27.
\end{alertblock}

---

# Related Work

\begin{columns}
\begin{column}{0.55\textwidth}

\textbf{Inherently Interpretable Models}

\begin{itemize}
\item Trees, lists, sets, (generalized) linear models, and additive models
\item \emph{Interpretable Decision Sets} (Lakkaraju et al.) — joint framework for description and prediction
\end{itemize}

\end{column}
\begin{column}{0.42\textwidth}

\textbf{Post-hoc, Model-agnostic}

\begin{itemize}
\item LIME: one of the \textbf{first significant papers} for post-hoc, model-agnostic analysis
\item \emph{Extracting Faithful and Descriptive Representations} — approximating globally through gradient is a challenge $\Rightarrow$ Local fidelity
\end{itemize}

\end{column}
\end{columns}

\vspace{0.5em}

\begin{block}{Show, Attend and Tell (Xu et al.)}
Interpretable description of images via visual attention — LIME aims for a more model-agnostic approach.
\end{block}

---

# Limitations and Future Work

- **Feature space complexity:** expected to work on feature spaces that are not too complex
  - Can similar ideas be applied to sequential decision making (e.g., RL)?

\vspace{0.5em}

- **User experiment:** results could depend on how the study notified the definition of "trustworthiness" to participants

\vspace{0.5em}

- **Automation:** a principled way for the algorithm to automatically improve based on its explanation (without humans having to modify the data or algorithm manually)

---

# A Unified Approach to Interpreting Model Predictions

\begin{center}
\Large Scott Lundberg and Su-In Lee
\end{center}

\vspace{1em}

\begin{center}
\textit{Presented by Max Nadeau, Max Li, and Xander Davies}
\end{center}

[@lundberg2017unified]

---

# Outline

1. **Additive Explanations**
   - Overview and relation to LIME
   - LIME Desiderata
2. **Shapley Values**
   - Introduction to Shapley values
   - Removing features
3. **Approximations**
4. **Experiments**
5. **Extensions**
   - Global interpretability
   - Inner interpretability

---

# Introduction to Additive Feature Attribution Methods

This paper unifies **6 previous methods** for local interpretability as **additive feature attribution methods (AFAMs)**.

An AFAM consists of:

- An enumeration of the **features present** in $x$
- A protocol for **"removing some features"** from $x$, defining $y$ (the "input with no features")
- An approximation $g(x')$ of $f(x)$ and $g(y')$ of $f(y)$
- A partition of $g(x') - g(y')$ among the features of $x$, indicating **how important each feature was** for the model's output

The importance of feature $i$ is denoted $\phi_i$

---

# LIME as an Additive Feature Attribution Method

- LIME (for explaining a classification of some image $x$) is an AFAM
- The **set of superpixels** is the set of features of $x$
- We **remove a superpixel** (feature) by replacing its pixels with grey
  - The image with no features is all grey
- LIME outputs a function $g$ that approximates $f(x)$ and $f(y)$ as $g(x')$ and $g(y')$
- $g$ provides a weighting $g_i$ for the importance of each superpixel in determining $f(x)$ — these serve as the $\phi_i$

---

# DeepLIFT as an Additive Feature Attribution Method

- DeepLIFT is another local interpretability method (Shrikumar et al., 2019)
- The **set of pixels** is the set of features of $x$
- Removing a feature consists of setting a pixel to the value of that pixel in a **reference image** (serves as $y$)
- DeepLIFT uses $g(x') = f(x)$ and $g(y') = f(y)$ directly (no approximation)
- DeepLIFT calculates a value $C_{\Delta x_i \Delta o}$ for each pixel $x_i$ such that $C_{\Delta x_i \Delta o} = f(x) - f(y)$
  - Each $C_{\Delta x_i \Delta o}$ represents importance of $x_i$ to classification $f(x)$

---

# Desiderata for Additive Feature Attribution Methods

Three desirable properties proposed for an AFAM:

\begin{block}{Local Accuracy}
$g(x') = f(x)$. DeepLIFT meets this; LIME does not necessarily.
\end{block}

\begin{block}{Consistency}
For input $x$, let $x \setminus i$ denote "removing feature $i$ from $x'$". If including feature $i$ in the input always makes a bigger difference in model $f$ than in model $f'$, then the AFAM should give higher importance $\phi_i$ for model $f$ than for $f'$.
\end{block}

\begin{alertblock}{Missingness}
Described as "really just a minor book-keeping property" — we'll ignore it.
\end{alertblock}

---

# Cooperative Games

- Suppose we have a game with $d$ players, where each can choose whether or not to cooperate
- Assume a **reward function** $g: \mathcal{P}([d]) \to \mathbb{R}$. If $S \subseteq [d]$ is the set of cooperating players, the group receives reward $g(S)$
- We want to determine how much each player **"contributes"** to the reward
  - The marginal contribution of player $i$ may depend on which other players have also chosen to cooperate
  - $g$ does not need to be monotonic!

---

# Shapley Values

The **Banzhaf power index** averages player $i$'s marginal contribution over all subsets:

$$\frac{1}{2^{d-1}} \sum_{S \subseteq [d] \setminus \{i\}} \bigl(g(S \cup \{i\}) - g(S)\bigr) \tag{1}$$

The **Shapley value** reweights marginal contributions based on the size of subset $S$:

$$\frac{1}{d} \sum_{j=0}^{d-1} \binom{d-1}{j}^{-1} \sum_{S \subseteq [d] \setminus \{i\},\, |S|=j} \bigl(g(S \cup \{i\}) - g(S)\bigr) \tag{2}$$

Or equivalently: $\sum_{\sigma \in S_d} g(\sigma(\sigma(i))) - g(\sigma(\sigma(i)-1))$

---

# From Games to Local Interpretability

- Suppose for some input $x$, a model produces prediction $f(x)$, and we want to measure how "important" each feature was
- We can treat the **features as players** in a cooperative game, and ask how much each contributed to the output
- However, to prompt the model, we need to provide all input features $S$. How do we measure what the model would have predicted **if it only had access to a subset of features**?

\begin{alertblock}{}
In other words, the function $g: \mathcal{P}([d]) \to \mathbb{R}$ is not well-defined.
\end{alertblock}

---

# Previously Proposed: Separate Models

- In **"Shapley regression values"**, for every subset of features $S \subseteq [d]$, we can train a model $f_S$ that tries to predict the labels
- The resulting Shapley values are a good metric for how important each feature is for good prediction of the labels
- However, they do **not** provide interpretability for the specific model $f$ we were working with
  - What $f$ might do without any information about the features in $[d] \setminus S$ might be very different than optimal prediction

---

# Feature Ablation

We want to capture what our **particular** model $f$ would do if it had no access to features $[d] \setminus S$.

This notion is captured by the **expectation of the model output given features $S$**:

$$E[f(x) \mid x_S] \tag{3}$$

We can approximate this by sampling over the conditional distribution:

$$\frac{1}{N} \sum_{i=1}^{N} f(x^{(i)}), \quad x^{(i)} \sim x \mid x_S \tag{4}$$

---

# Model Agnostic: Feature Independence

- Computing SHAP values requires calculating $2^d$ differences $g(S \cup \{i\}) - g(S)$
- One way to improve: assume **features are independent**, $\forall S$:

$$E[f(x) \mid x_S] = E_{x_S | x_S}[f(x)] \approx E_{x_S}[f(x)] \tag{5}$$

- We can then estimate SHAP values via sampling approximations (**the Shapley sampling values method**) which require fewer than $2^d$ difference calculations
- But still requires lots of computations

---

# Model Agnostic: Kernel SHAP via LIME

The kernel weights ($\pi_x$), loss function ($L$), and simplicity function ($\Omega$) in LIME aren't consistent with desired properties (local accuracy \& consistency). We adjust these to form the **Shapley kernel**:

$$\Omega(g) = 0 \tag{6}$$

$$\pi_x(z') = \frac{(M-1)}{\binom{M}{|z'|} |z'| (M - |z'|)} \tag{7}$$

$$L(f, g, \pi_x) = \sum_{z' \in \mathcal{Z}} \left[ f_h(z') - g(z') \right]^2 \pi_x(z') \tag{8}$$

where $|z'|$ is the number of non-zero elements in $z'$.

---

# Kernel SHAP: Sample Weight Comparison

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/kernel_shap_plot.png}
\end{center}

\begin{exampleblock}{}
The Shapley kernel assigns more weight to very small and very large subsets compared to LIME kernels (cosine or L2 distance).
\end{exampleblock}

---

# Model Agnostic: Kernel SHAP (cont.) {.fragile}

We can consider LIME's feature removing protocol an **approximation of SHAP values** that assumes $f$ is linear, so that $E[f(x) \mid x_S] = f(x^*)$, where:

$$x_i^* = \begin{cases} x_i & \text{if } i \in S \\ E[x_i] & \text{otherwise} \end{cases} \tag{9}$$

- Since we can solve for $g$ in (8) as a **weighted linear regression problem**, we have a regression-based, model-agnostic estimation of SHAP values!
- This is **more efficient** than previously, since we jointly solve for SHAP values

---

# Model-Specific Approximations: Linear SHAP

We can do better by looking for **model-specific approximations**.

If the model is **affine** and we assume **feature independence**, feature $i$'s importance for $x$ is its difference from the mean multiplied by its weight:

If $f(x) = \sum_{j=1}^{M} w_j x_j + b$, then:

$$\phi_0(f, x) = b$$

$$\phi_i(f, x) = w_i (x_i - E[x_i])$$

---

# Model-Specific Approximations: Deep SHAP

DeepLIFT approximates SHAP values assuming **feature independence** and the deep model is **linear**, since it:

1. **Linearizes** the non-linear components of a network ("heuristically chosen")
2. **Replaces values** with a reference value, which we can consider $E[x]$ (like LIME)

- Currently satisfies **local accuracy** (and missingness), but **not consistency**
- We can choose **new linearizations** which satisfy consistency

\begin{exampleblock}{}
$\Rightarrow$ \textbf{Deep SHAP!}
\end{exampleblock}

---

# User Experiments

- The authors run an experiment in which they tell a story about people playing a **cooperative game**, and find that **human assignments of credit align better with SHAP's assignment** than with LIME's or DeepLIFT's

\vspace{1em}

\begin{alertblock}{Caveat}
This is a very different setting from attribution in neural networks, seemingly selected to make SHAP look good, so this experiment is unimpressive evidence that SHAP aligns with human intuition for NN credit assignment.
\end{alertblock}

---

# Class Difference Experiments

\begin{columns}
\begin{column}{0.5\textwidth}

- Using an image of an "8" and an MNIST classifier, the authors identified which pixels (according to SHAP, LIME, and DeepLIFT) are most important for the model's log-odds (i.e. logit difference) of 8 versus 3
- **Removing the pixels identified by SHAP** produced larger changes in log-odds from 8 to 3 than the other methods

\end{column}
\begin{column}{0.45\textwidth}

\begin{center}
\includegraphics[width=\columnwidth]{imgs/class_diff.png}
\end{center}

\end{column}
\end{columns}

---

# Extensions: Shapley Values for the Whole Model

Rather than attributing Shapley values for a particular input $x$, we can instead attribute Shapley values for the **model's prediction over the entire input distribution**.

- Naively: $g(S) = E[E[f(x) \mid x_S]]$, which reduces to $E[f(x)]$ by Adam's law
- Instead, to capture the amount of model behavior we can explain with only a subset of features, use a **symmetric loss function**:

$$g(S) = \text{Var}(E[f(x) \mid x_S])$$

Methods that do this include **SAGE** (Covert et al., 2020) and **Shapley Effects** (Owen, 2014).

---

# Extensions: Neuron Shapley

- We can **treat neurons as features** (Ghorbani and Zou, 2020)
- This paper uses **zero ablation**
- We can also use **multi-armed bandit sampling algorithms** to estimate Shapley values

\vfill

\begin{block}{}
Neuron Shapley extends SHAP concepts to understand the contribution of individual neurons in neural networks.
\end{block}

---

\begin{center}
\Huge Thank You!
\end{center}

---

# References {.allowframebreaks}

\footnotesize
