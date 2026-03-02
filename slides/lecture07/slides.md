---
title: "\\emoji{wtf} XAI: Post-hoc - LIME & SHAP"
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

# Simulated User Experiment -  Can I trust this model?

- 10 noisy features added: correlated with the label in train/validation, but not in test
- Two random forests with similar validation accuracy ($< 0.1\%$ apart) but very different test accuracy ($> 5\%$ apart)
- **Task:** can a simulated user pick the better model by inspecting $B$ explanations?
- **SP-LIME** dominates, especially for small $B$

\begin{center}
\includegraphics[width=.7\columnwidth]{imgs/simulated_model.png}
\end{center}



---

# Evaluating with Human Subjects - Experimental Setup

Previous experiments were simulated — now we test with **real users** on Amazon Mechanical Turk.

- **Dataset:** 20 Newsgroups (Christianity vs. Atheism) — known to contain spurious features
  (headers, author names) that do not generalize
- To measure real-world generalization, a **new religion dataset** is created:
  - 819 web pages per class scraped from Atheism and Christianity websites
- Model: SVM with RBF kernel, hyperparameters tuned via cross-validation

---

# Evaluating with Human Subjects - Can users select the best classifier?

:::: {.columns}
::: {.column width="48%"}

- Train two SVMs:
  - one on problematic dataset
  - one on "cleaned" dataset
- Recruit humans to select which algorithm will perform best
-  The problematic model has *higher* validation accuracy (94.0% vs 88.6%), so accuracy alone would lead to the wrong choice.

:::
::: {.column width="48%"}

\begin{center}
\includegraphics[width=\columnwidth]{imgs/human_classifier.png}
\end{center}

:::
::::

> SP-LIME (89%) outperforms RP-LIME (75%), and both outperform greedy variants.

---

# Evaluating with Human Subjects - Can non-experts improve a classifier?

Each round: user sees $B=10$ instances with $K=10$ words per explanation
and marks words to remove. Model is retrained without those words.

:::: {.columns}

::: {.column width="50%"}

- Round 0: 10 subjects → 10 classifiers
- Round 1: 5 new users per classifier → 50 classifiers
- Round 2: 5 more users → 250 classifiers
- Real-world accuracy measured at each round on the religion dataset

:::

::: {.column width="50%"}

\begin{center}
\includegraphics[width=.75\columnwidth]{imgs/human_improve.png}\end{center}

:::

::::

## Result
Non-experts using LIME explanations can meaningfully improve a classifier without ever seeing the test data.

---

# Evaluating with Human Subjects - Do explanations lead to insights?

**Setup:** a deliberately bad classifier is trained to predict "wolf" when there
is snow in the background, and "husky" otherwise — ignoring the actual animal.

:::: columns
::: column

1. Find pictures such that classifier predicts "wolf" if there is snow, and "husky" otherwise
2. Ask subjects (grad students):
   - Do they trust model to work well in real world?
   - Why?
   - How do they think the model distinguishes?
3. Showed explanations and asked again

:::
::: column

\begin{center}
\includegraphics[width=.75\columnwidth]{imgs/husky_wolf.png}
\end{center}

:::
::::

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

# Paper 2

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/paper2.png}
\end{center}

[@lundberg2017unified]

---

# Additive Feature Attribution Methods (AFAMs)

This paper unifies **6 previous methods** for local interpretability under a single framework.
An AFAM explains a prediction $f(x)$ by assigning an importance $\phi_i$ to each feature $i$:

\textbf{$$g(z') = \phi_0 + \sum_{i=1}^{M} \phi_i z'_i, \quad z' \in \{0,1\}^M$$}

where $g$ is a linear explanation model over the interpretable representation $z'$.

---

# Additive Feature Attribution Methods (AFAMs)

**Example: LIME for image classification**

\small
- Features of $x$ are its **superpixels**
- Removing a feature = replacing its superpixel with grey pixels
- $y$ = the all-grey image (input with no features)
- LIME fits $g(z') \approx f(x)$ and $g(y') \approx f(y)$ locally
- The weights $\phi_i$ indicate how important each superpixel was for $f(x)$

## The key insight:
many existing methods already fit this form —
often without realizing they share the same underlying structure.


---

# DeepLIFT as an Additive Feature Attribution Method

Instead of perturbing features randomly, DeepLIFT compares the current prediction
against a **reference input** $r$ (e.g., a blank or average image).

- Features of $x$ are its **pixels**
- Removing a feature = replacing pixel $x_i$ with its value in $r$
- $\phi_0 = f(r)$ — base prediction on the reference input
- Each $\phi_i = C_{\Delta x_i \Delta o}$ measures how much pixel $i$ contributed
  *relative to its reference value*

DeepLIFT satisfies the **summation-to-delta** property exactly:

\textbf{
$$\sum_{i=1}^{n} C_{\Delta x_i \Delta o} = f(x) - f(r)$$}

**Human mode:** The attributions sum exactly to the difference between the current prediction and the reference prediction —
every unit of "change" (pixel) in the output is fully accounted for by the input features.

---

# LIME vs DeepLIFT

- Unlike LIME, DeepLIFT is not model-agnostic — it exploits the internal
structure of neural networks to back-propagate attribution values in a single pass,
without any sampling.

## DeepLIFT is an AFAM:

Setting $$\phi_0 = f(r)$$ and $$\phi_i = C_{\Delta x_i \Delta o}$$
makes it fit exactly the linear form $$g(z') = \phi_0 + \sum_i \phi_i z'_i$$

---

# Desiderata for Additive Feature Attribution Methods

\begin{center}
\textbf{Three desirable properties for an AFAM:}
\end{center}

**Local Accuracy:** the attributions must fully account for the prediction —
summing all $\phi_i$ plus the base value $\phi_0$ must recover $f(x)$ exactly.
No part of the prediction should be left unexplained.

**Consistency:** if feature $i$ always contributes more in model $f$ than in model $f'$
— regardless of what other features are present — then $\phi_i(f) \geq \phi_i(f')$.
Intuitively: if a feature becomes more important, its attribution should not decrease.
LIME can violate this depending on the sampling.

**Missingness:** if a feature was not present in the original input ($x'_i = 0$),
its attribution must be zero — you cannot credit or blame something that never existed.

## Key result:
These three properties together determine a *unique* solution — **SHAP values**.

---

# The Shapley Value Problem 1/3

Three workers collaborate to earn a reward: **carpenter (C), painter (P), salesperson (S)**.

| **Coalition **| **Reward** |
|---|---|
| {C} | $10 |
| {P} | $15 |
| {S} | $5 |
| {C, P} | $40 |
| {C, S} | $30 |
| {P, S} | $35 |
| {C, P, S} | $100 |

**Problem:** how much did each worker actually contribute to the $100 reward?

---

# The Shapley Value Problem 2/3
\small
| **Coalition **| **Reward** |
|---|---|
| {C} | $10 |
| {P} | $15 |
| {S} | $5 |
| {C, P} | $40 |
| {C, S} | $30 |
| {P, S} | $35 |
| {C, P, S} | $100 |

**Problem:** how much did each worker actually contribute to the $100 reward?

- The contribution of each worker depends on who else is cooperating —
the salesperson adds $60 when both C and P are present, but only $20 when only C is present.

## Shapley answer

Average each player's marginal contribution over all possible coalitions.

---

# The Shapley Value Problem 3/3

The value of player $i$ is:

$$\phi_i = \sum_{S \subseteq [d] \setminus \{i\}} \frac{|S|!(d - |S| - 1)!}{d!} \left[ g(S \cup \{i\}) - g(S) \right]$$

For the **salesperson (S)** whit $d = 3$:

| Coalition $S$ | $g(S \cup \{S\}) - g(S)$ | Weight $\frac{\|S\|!(d-\|S\|-1)!}{d!}$ | Contribution |
|---|---|---|---|
| $\emptyset$ | $5 - 0 = 5$ | $\frac{0! \cdot 2!}{3!} = \frac{2}{6}$ | $1.67$ |
| {C} | $30 - 10 = 20$ | $\frac{1! \cdot 1!}{3!} = \frac{1}{6}$ | $3.33$ |
| {P} | $35 - 15 = 20$ | $\frac{1! \cdot 1!}{3!} = \frac{1}{6}$ | $3.33$ |
| {C, P} | $100 - 40 = 60$ | $\frac{2! \cdot 0!}{3!} = \frac{2}{6}$ | $20$ |

$$\phi_S = 1.67 + 3.33 + 3.33 + 20 = \mathbf{28.33}$$

The weight favors large and small coalitions because there are few ways to reach them — there is only one way for $S$ to enter $\emptyset$ or $\{C,P\}$, but also only one way to enter $\{C\}$ or $\{P\}$.

---

# From Games to Local Interpretability

**Idea:** treat features as players and the model prediction $f(x)$ as the reward.
Shapley values would then tell us how much each feature contributed to the prediction.

**Problem:** to compute marginal contributions, we need to evaluate the model
on every possible subset of features $S$ — but the model was trained on all features at once.

> *What would the model have predicted if it only had access to features $S$?*

For example, if $x = [\text{age}=30, \text{income}=50k, \text{debt}=10k]$ and we want
to evaluate using only $\{\text{age}, \text{income}\}$ — what value do we give to $\text{debt}$?

\textcolor{red}{
$$g(S) = f(x_S) \quad \text{is not well-defined}$$}

The model cannot handle arbitrary patterns of missing inputs.

\begin{center}
\large
\textbf{This is the key challenge SHAP must solve.}
\end{center}

---

# Previously Proposed: Separate Models

- In **"Shapley regression values"**, for every subset of features $S \subseteq [d]$, we can train a model $f_S$ that tries to predict the labels
- The resulting Shapley values are a good metric for how important each feature is for good prediction of the labels
- However, they do **not** provide interpretability for the specific model $f$ we were working with
  - What $f$ might do without any information about the features in $[d] \setminus S$ might be very different than optimal prediction

## Human mode

Shapley regression values measure which features are important for predicting the target well, not which features your specific model relies on. They are useful for global feature selection, but not for explaining why $f$ made a particular prediction.

---

# Feature Ablation

We want to capture what our **particular** model $f$ would do if it had no access
to features $[d] \setminus S$.

This notion is captured by the **expectation of the model output given features $S$**:

$$E[f(x) \mid x_S] \tag{3}$$

We do not remove the missing features — instead we **neutralize** them by averaging
$f$'s predictions over different possible values, sampled from their real distribution.
The model still receives all its inputs, but the missing features no longer carry information.

We can approximate this by sampling over the conditional distribution:

$$\frac{1}{N} \sum_{i=1}^{N} f(x^{(i)}), \quad x^{(i)} \sim x \mid x_S \tag{4}$$

---

# Feature Ablation Example 1/2

Suppose $x = [\text{age}=30, \text{income}=50k, \text{debt}=10k]$ and $S = \{\text{age, income}\}$.
We want to estimate what $f$ predicts when it has no access to `debt`.

Instead of removing `debt`, we sample $N$ values from its conditional distribution
— i.e., examples in the dataset with age=30 and income=50k — and evaluate $f$ for each:

- $f([30, 50k, 10k])$
- $f([30, 50k, 5k])$
- $f([30, 50k, 20k])$
- $\ldots$

Then we average the results. This gives us what $f$ predicts on average when it only
knows age and income, without privileging any particular value of `debt`.

---

# Feature Ablation Example 2/2
\small
With $N = 3$ samples and $S = \{\text{age, income}\}$:

\textbf{$$E[f(x) \mid x_S] \approx \frac{1}{3} \left[ f([30, 50k, 10k]) + f([30, 50k, 5k]) + f([30, 50k, 20k]) \right]$$}
\small
Suppose the model predicts:

- $f([30, 50k, 10k]) = 0.8$
- $f([30, 50k, 5k]) = 0.7$
- $f([30, 50k, 20k]) = 0.6$

Then:

\textbf{$$E[f(x) \mid x_S] \approx \frac{0.8 + 0.7 + 0.6}{3} = \frac{2.1}{3} = 0.7$$}
\small
This is our estimate of what $f$ predicts when it only has access to age=30 and income=50k,
neutralizing the effect of `debt`.

---

# Model Agnostic: Feature Independence

- Computing SHAP values requires calculating $2^d$ differences $g(S \cup \{i\}) - g(S)$
    - With $d = 20$ features, that amounts to over one million model evaluations — infeasible in practice.
- One way to improve: assume **features are independent**, $\forall S$:

$$E[f(x) \mid x_S] = E_{x_S | x_S}[f(x)] \approx E_{x_S}[f(x)] \tag{5}$$

- We can then estimate SHAP values via sampling approximations (**the Shapley sampling values method**) which require fewer than $2^d$ difference calculations
    - Following the previous example, we simply sample values of `debt` from the entire dataset, regardless of age or income.
- But still requires lots of computations

---

# Kernel SHAP: LIME with the Right Parameters 1/2

- LIME's parameters **($\pi_x$, $L$, $\Omega$)** were chosen heuristically — they work well
in practice but **do not guarantee** local accuracy or consistency.
- **Key insight:** there exists a unique choice of these parameters such that
the solution to LIME's regression is exactly the SHAP values:

$$\Omega(g) = 0 \qquad \pi_x(z') = \frac{(M-1)}{\binom{M}{|z'|} |z'| (M - |z'|)} \qquad L(f, g, \pi_x) = \sum_{z' \in \mathcal{Z}} \left[ f_h(z') - g(z') \right]^2 \pi_x(z')$$

- **$\Omega(g) = 0$** — no regularization: SHAP values do not penalize complexity
- **$\pi_x(z')$** — upweights very small and very large coalitions, downweights intermediate ones
- **$L$** — standard weighted squared loss, same as LIME

---

# Kernel SHAP: LIME with the Right Parameters 1/2

$$\Omega(g) = 0 \qquad \pi_x(z') = \frac{(M-1)}{\binom{M}{|z'|} |z'| (M - |z'|)} \qquad L(f, g, \pi_x) = \sum_{z' \in \mathcal{Z}} \left[ f_h(z') - g(z') \right]^2 \pi_x(z')$$

\begin{center}
\large
\textbf{Why this kernel?}
\end{center}

Coalitions of 1 or $M-1$ features are the most informative —
we know exactly which feature is being added or removed. Intermediate coalitions
are more ambiguous because many features change at once.

\begin{center}
\large
\textbf{Kernel SHAP = LIME + Shapley kernel \\ Satisfies local accuracy and consistency by construction.}
\end{center}

---

# Kernel SHAP: Sample Weight Comparison

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/kernel_shap_plot.png}
\end{center}

\begin{exampleblock}{}
The Shapley kernel assigns more weight to very small and very large subsets compared to LIME kernels (cosine or L2 distance).
\end{exampleblock}

---

# Kernel SHAP: Linear Approximation

\small
Instead of sampling missing features, we can assume $f$ is linear and simply
replace each missing feature with its expected value $E[x_i]$:

$$x_i^* = \begin{cases} x_i & \text{if } i \in S \\ E[x_i] & \text{otherwise} \end{cases}$$

**Example:** $x = [\text{age}=30, \text{income}=50k, \text{debt}=10k]$, $S = \{\text{age, income}\}$

Instead of sampling `debt`, we substitute $E[\text{debt}] = 15k$ directly:
$$E[f(x) \mid x_S] \approx f([30, 50k, 15k]) = 0.75$$

Since $g$ is linear and $L$ is a squared loss, all $\phi_i$ can be solved **jointly**
via weighted linear regression — more efficient than estimating each separately.

\begin{center}
\large
\textbf{Kernel SHAP = LIME's regression framework + Shapley kernel + mean imputation}
\end{center}

---

# Model-Specific Approximations: Linear SHAP 1/2


For **linear (affine) models**, SHAP values can be computed analytically —
no sampling or regression needed.

$$\text{\textbf{If}} \quad f(x) = \sum_{j=1}^{M} w_j x_j + b \qquad \text{\textbf{Then}} \qquad \phi_0(f, x) = b \qquad \phi_i(f, x) = w_i(x_i - E[x_i])$$


**Intuition:** feature $i$'s contribution is how far its value deviates from
the average, scaled by how much the model cares about it ($w_i$).

- If $x_i = E[x_i]$ → feature $i$ contributes nothing: $\phi_i = 0$
- If $x_i > E[x_i]$ and $w_i > 0$ → positive contribution
- If $x_i < E[x_i]$ and $w_i > 0$ → negative contribution

---

# Model-Specific Approximations: Linear SHAP 2/2 (Example)

$f(x) = 2 \cdot \text{age} + 3 \cdot \text{income} + 5$,

with:

- $E[\text{age}] = 40$,
- $E[\text{income}] = 50k$, and
- $x = [\text{age}=30, \text{income}=60k]$:

$$\phi_0 = 5, \quad \phi_{\text{age}} = 2 \cdot (30 - 40) = -20, \quad \phi_{\text{income}} = 3 \cdot (60k - 50k) = 30k$$

## Local accuracy check:
$\phi_0 + \phi_{\text{age}} + \phi_{\text{income}} = 5 - 20 + 30 = 15 = f(x)$

---

# Model-Specific Approximations: Deep SHAP

DeepLIFT approximates SHAP values under two assumptions:
**feature independence** and **model linearity** (via linearization of non-linear components).

Specifically, DeepLIFT:

1. **Linearizes** non-linear components of the network — but the linearization rules
   were chosen heuristically, without theoretical justification
2. **Replaces missing features** with a reference value, which we interpret as $E[x]$

This means DeepLIFT satisfies **local accuracy** and **missingness**,
but **not consistency** — its heuristic linearizations can violate it.

**Deep SHAP** fixes this by choosing linearizations that are consistent with
Shapley values, turning DeepLIFT into a theoretically grounded approximation of SHAP.

\begin{center}
\large
\textbf{Deep SHAP = DeepLIFT + Shapley-consistent linearizations}
\end{center}


---

# User Experiments

Participants were told a story about a cooperative game and asked to assign
credit among players. **Human assignments aligned more closely with SHAP values
than with LIME or DeepLIFT.**


## Caveat {.alert}
This experiment uses a cooperative game setting — very different
from real neural network attribution. It seems selected to favor SHAP,
since SHAP values are derived directly from cooperative game theory.
This is weak evidence that SHAP aligns with human intuition for NN predictions.

---

# Class Difference Experiments

:::: {.columns}
::: {.column width="48%"}

- Using an image of an "8" and an MNIST classifier, the authors identified which pixels (according to SHAP, LIME, and DeepLIFT) are most important for the model's log-odds (i.e. logit difference) of 8 versus 3
- **Removing the pixels identified by SHAP** produced larger changes in log-odds from 8 to 3 than the other methods

:::
::: {.column width="48%"}

\begin{center}
\includegraphics[width=.8\columnwidth]{imgs/class_diff.png}
\end{center}

:::
::::

---

# Extensions: Shapley Values for the Whole Model 1/2

So far SHAP values explain a **single prediction** $f(x)$.
Can we explain the **model's behavior globally**?

**Naive approach:** average SHAP values over all inputs:
$$g(S) = E[E[f(x) \mid x_S]] = E[f(x)]$$
This collapses to a constant by the law of total expectation — it tells us nothing about feature importance.

---

# Extensions: Shapley Values for the Whole Model 1/2

**Better approach:** measure how much of the model's variance features in $S$ can explain:

\textbf{$$g(S) = \text{Var}(E[f(x) \mid x_S])$$}

- If $S$ contains **important features** → knowing $x_S$ makes predictions vary a lot → high variance
- If $S$ contains **irrelevant features** → knowing $x_S$ barely changes predictions → variance $\approx 0$

We can then apply Shapley values to $g(S)$ to fairly attribute
**how much each feature contributes to the model's overall variance**.

## Implementations

**SAGE** (Covert et al., 2020) and **Shapley Effects** (Owen, 2014).

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
