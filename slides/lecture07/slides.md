---
title: "\\emoji{wtf} XAI: LIME & SHAP"
bibliography: references.bib

---

# Disclaimer

\input{../disclaimer.tex}

---

# Paper 1

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/lime_paper.png}
\end{center}

[@ribeiro2016should]

---

# Define Trust - Two Notions

ML models are often used as black boxes — but humans need to understand them before acting on their outputs.

- **Trusting a prediction:** Does this specific output make sense?
  *E.g., should a doctor act on this diagnosis?*

- **Trusting a model:** Will this model behave reasonably when deployed?
  *E.g., does it generalize beyond the validation set?*

> Both depend on how much the user understands the model's behavior.

---

# Define Explanation for a Prediction

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/lime_explanation_flow.png}
\end{center}

An explanation identifies **which parts of the input** drove the model's prediction —
and in which direction.

- \emoji{green-circle.png} *sneeze*, *headache* → evidence **for** Flu
- \emoji{red-circle.png} *no fatigue* → evidence **against** Flu

## Formally:
A textual or visual artifact that describes the relationship between an instance's components and the model's output.

---

# Explanations as a Means to Select Model 1/2

\begin{center}
\includegraphics[width=0.750\columnwidth]{imgs/model_selection.png}

\textbf{Both models predict "Atheism" correctly — but for very different reasons.}

\end{center}

---

# Explanations as a Means to Select Model 2/2

\begin{center}

\textbf{Both models predict "Atheism" correctly — but for very different reasons.}

\end{center}

| | Algorithm 1 | Algorithm 2 |
|---|---|---|
| **Key words** | *GOD, mean, anyone* | *Posting, Host, Nntp* |
| **Reason** | Semantic content \emoji{check-mark-button.png} | Email header metadata \emoji{cross-mark.png} |
| **Will it generalize?** | Likely yes | Likely no |

- Accuracy alone cannot distinguish these models.
- Explanations expose *why* a prediction was made — and whether to trust it.

---

# Why Do We Need Trust and Interpretability?

A model can have **high accuracy** and still be wrong for the right reasons.

- **Data leakage:** the model learns features that are accidentally correlated
  with the label (e.g., patient ID predicts diagnosis). High accuracy, zero generalization.

- **Dataset shift / Concept drift:** training and real-world data differ — either
  the input distribution changes/shift, or the relationship between inputs and labels
  changes/drift over time. The model looks good on validation but fails in deployment.

- **Spurious features:** the model exploits features that *work* statistically
  but are undesirable (e.g., clickbait signals in a recommender system).

> In all three cases, validation accuracy is misleading.
> Interpretability lets us catch these failures before they cause harm.

---

# Desired Characteristics for Explainers

- **Interpretable:** explanations must be understandable to humans,
  not just technically correct (e.g., no thousands of non-zero weights)

- **Locally faithful:** must reflect how the model *actually behaves*
  near the instance being explained — global fidelity is often impossible

- **Model-agnostic:** must work as a black box, applicable to any classifier, including models that don't yet exist

- **Global perspective:** beyond single predictions, explanations should
  help users understand the model as a whole

## Local Interpretable Model-agnostic Explanations (LIME)

A framework designed to satisfy all four criteria simultaneously.

---

# LIME Step 1: Define LIME Framework

\begin{center}
\textbf{Goal:} Find the simplest explanation that still accurately describes
the model's behavior \textit{near} the instance $x$.
\end{center}

\textbf{
$$\xi(x) = \underset{g \in G}{\text{argmin}} \ \mathcal{L}(f, g, \pi_x) + \Omega(g)$$
}

- \textbf{$\xi(x)$} — explanation for instance $x$
- \textbf{$g \in G$} — interpretable model (e.g., linear model)
- \textbf{$f$} — black-box model to be explained
- \textbf{$\mathcal{L}(f, g, \pi_x)$} — unfaithfulness of $g$ approximating $f$ locally
- \textbf{$\pi_x$} — proximity measure that defines the local neighborhood
- \textbf{$\Omega(g)$} — complexity of $g$ (e.g., number of non-zero weights)

\begin{center}
\normalsize
This is a \textbf{fidelity-interpretability trade-off}:
minimize error locally,
while keeping the explanation simple enough for humans to understand.
\end{center}

---

# LIME Step 2: Interpretable Data Representation

- The black-box model operates on features that are often incomprehensible to humans
(e.g., embeddings, raw pixels).
- LIME maps these to an **interpretable representation**
that humans can reason about:

  - **Text:** binary vector indicating the presence or absence of a word
  - **Image:** binary vector indicating the presence or absence of a contiguous patch of similar pixels (superpixel)

\begin{center}
\textbf{$$x \in \mathbb{R}^d \xrightarrow{h_x} x' \in \{0,1\}^{d'}$$
}
\footnotesize Original Representation $\longrightarrow$ Interpretable Representation

\end{center}

where $x \in \mathbb{R}^d$ is the original instance with $d$ features, $x' \in \{0,1\}^{d'}$ is a binary vector of length $d'$ where each entry is $1$ if the corresponding interpretable component is \textbf{present} and $0$ if it is \textbf{absent}, and $h_x$ is the function that maps $x'$ back to the original representation.

---

# LIME Step 3: Sampling for Local Exploration 1/2

Since $f$ is a black box, LIME **interrogates** it: perturb, query, and fit $g$ locally.

1. Start from $x'$, the interpretable representation of the instance to explain
2. Generate perturbed samples $z'$ by randomly turning off components of $x'$
3. Map each $z'$ back to the original space: $z = h_x(z')$
4. Query the black-box model to get a label: $f(z)$
5. Weight each sample by its proximity to $x$: $\pi_x(z)$

$$x \xrightarrow{} x' \xrightarrow{\text{perturb}} z' \xrightarrow{h_x} z \xrightarrow{f} f(z)$$

\begin{center}

The dataset \textbf{$\mathcal{Z} = \{(z', f(z), \pi_x(z))\}$} is then used to fit the local model $g$.

\end{center}

---

# LIME Step 3: Sampling for Local Exploration 2/2

Since $f$ is a black box, LIME cannot minimize $\mathcal{L}(f, g, \pi_x)$ analytically.
Instead, it **interrogates** $f$: it generates perturbed samples near $x'$, queries
the model, and uses the responses to fit $g$ locally.

\small
1. **Start from the instance:** take the review *"The movie was great and funny"*
   → $x' = [1, 1, 1, 1, 1, 1]$

2. **Randomly turn off words:** generate a masked version
   → $z' = [0, 1, 0, 1, 0, 1]$ → *"movie great funny"*

3. **Map back to original space:** reconstruct the input the model understands
   → $z = h_x(z')$ (e.g., recompute embeddings for *"movie great funny"*)

4. **Ask the black box:** what does $f$ predict for this masked input?
   → $f(z) = 0.85$ (positive sentiment)

5. **Weight by proximity:** samples closer to $x$ matter more
   → $\pi_x(z)$ is high if few words were removed, low otherwise

$$x \xrightarrow{} x' \xrightarrow{\text{perturb}} z' \xrightarrow{h_x} z \xrightarrow{f} f(z)$$

\begin{center}

Repeat $N$ times → fit a sparse linear model $g$ on $\mathcal{Z} = \{(z', f(z), \pi_x(z))\}$.

\end{center}

---

# Sampling Procedure Intuition

\begin{center}
\includegraphics[width=0.65\columnwidth]{imgs/sampling_intuition.png}
\end{center}

\begin{center}
A complex decision boundary is approximated locally by a simple linear model (dashed line). Samples closer to the instance of interest (red cross) are weighted more.
\end{center}

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

# Example: Sparse Linear Explanation \emoji{snake.png}

:::: {.columns}

::: {.column width="40%"}

$$\xi(x) = \underset{g \in G}{\text{argmin}} \ \mathcal{L}(f, g, \pi_x) + \Omega(g)$$

$$g(z') = w_g \cdot z'$$

$$\pi_x(z) = \exp\!\left(-\frac{D(x,z)^2}{\sigma^2}\right)$$

$$\mathcal{L}(f,g,\pi_x) = \sum_{z,z' \in \mathcal{Z}} \pi_x(z)\bigl(f(z)-g(z')\bigr)^2$$

$$\Omega(g) = \infty \mathbb{1}[\|w_g\|_0 > K]$$

:::

::: {.column width="58%"}
\fontsize{7.5pt}{6pt}
!!include python: codes/sparse.py
:::

::::



---

# Some Results

\begin{center}
\includegraphics[width=0.90\columnwidth]{imgs/some_results.png}
\end{center}

----

# Global LIME: Intuition

If we could explain **every instance** in the dataset, we would have a complete
picture of how the model behaves globally.

But this is clearly infeasible — datasets can have thousands of instances,
and users have limited time and patience.

## Key question:

Which $B$ instances should we show the user to maximize
their understanding of the model?

---

# Gain Global Understanding of the Model

A single explanation gives local insight — but how do we understand the model **globally**?
The pick step selects $B$ instances to show the user, such that together they are
maximally informative about the model's overall behavior.

- **Budget $B$:** users have limited time — we can only show $B$ explanations
- **Explanation-aware selection:** instances are chosen based on their LIME explanations,
  not raw data alone — looking at raw predictions is not enough
- **Diverse and representative:** selected instances should cover as many different
  important features as possible, avoiding redundancy

> The goal: with just $B$ explanations, give the user a global picture of how the model works.

---

# Submodular Pick (SP) Algorithm 1/2

\begin{center}
\textbf{After running LIME on every $B$ instance, we organize the results into a matrix
$\mathcal{W}_{n \times d'}$ that summarizes how important each interpretable
feature is across all instances.}
\end{center}

:::: {.columns}

::: {.column width="48%"}

\begin{center}
\includegraphics[width=.8\columnwidth]{imgs/submodular_matrix.png}
\end{center}

:::

::: {.column width="50%"}

- Each **row** $i$ represents an instance $x_i$
- Each **column** $j$ represents an interpretable feature (e.g., a word)
- Each **cell** $\mathcal{W}_{ij} = |w_{g_j}|$ is the importance LIME assigned
  to feature $j$ for instance $i$ — $0$ if unused

From $\mathcal{W}$, the **global importance** of each feature is:

$$I_j = \sqrt{\sum_{i=1}^n |\mathcal{W}_{ij}|}$$

A high $I_j$ means feature $j$ is relevant across many instances.

:::

::::

---

# Submodular Pick (SP) Algorithm 2/2

:::: {.columns}

::: {.column width="48%"}

\begin{center}
\includegraphics[width=.99\columnwidth]{imgs/submodular_pick.png}
\end{center}

:::

::: {.column width="50%"}

We want to select a set $V$ of at most $B$ instances that **maximizes coverage**
of globally important features:

$$c(V, \mathcal{W}, I) = \sum_{j=1}^{d'} \mathbbm{1}_{[\exists i \in V: \mathcal{W}_{ij} > 0]} I_j$$

$$\text{Pick}(\mathcal{W}, I) = \underset{V, |V| \leq B}{\text{argmax}} \ c(V, \mathcal{W}, I)$$

$c$ is a **submodular function**: adding a new
instance to $V$ yields diminishing returns as $V$ grows.

Greedy solution: at each step, add the instance that maximally increases coverage:

:::

::::

---

# Simulated User Experiment - Experimental Setup

\small
**Goal:** evaluate explanation quality across different models and methods.

**Datasets:** two sentiment analysis datasets (books and DVDs, 2000 instances each)
— task is to classify product reviews as positive or negative.

**Models trained:** Decision Tree, Logistic Regression, Nearest Neighbors, SVM, Random Forest

## Explanation methods compared:
\small
- **Random:** selects $K$ features at random — minimal baseline
- **Greedy:** removes features one by one until the prediction changes
- **Parzen:** approximates $f$ globally with Parzen windows, explains via gradient
- **LIME:** proposed method — local sparse linear approximation

## Instance selection strategies:
\small
- **Random Pick (RP):** selects instances at random
- **Submodular Pick (SP):** selects instances to maximize feature coverage

\begin{center}
 \textbf{All methods produce explanations of size $K = 10$ features.}
\end{center}
---

# Simulated User Experiment - Are explanations faithful to the method?

\begin{columns}
\begin{column}{0.4\textwidth}

\textbf{Key idea:} use interpretable models (sparse LR, decision trees) where we
\textit{know} the true important features — the \textbf{gold set}. Then measure how many
gold features each method recovers (\textbf{recall}).

\begin{exampleblock}{}
LIME achieves the highest recall of truly important features on both Books and DVDs datasets.
\end{exampleblock}

\end{column}
\begin{column}{0.6\textwidth}

\begin{center}
\includegraphics[width=.75\columnwidth]{imgs/simulated_faithful.png}
\end{center}

\end{column}
\end{columns}

---

# Simulated User Experiment - Should I trust this prediction?
\small
- Randomly mark 25% of features as untrustworthy (simulating problematic
features such as data leakage or spurious correlations). A prediction is labeled
**untrustworthy** if it changes when those features are removed (the model
was relying on them).
- The prediction is then  untrustworthy if the problematic features appear in it with high weight.
- We measure **F1 of trustworthiness** to evaluate whether each explanation method
correctly identifies which predictions to trust and which to reject.

\begin{center}
\includegraphics[width=.45\columnwidth]{imgs/trust_prediction.png}
\end{center}

\begin{center}
\small
\textbf{LIME maintains both high precision and high recall —
it neither over-trusts nor over-distrusts predictions.}
\end{center}

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
