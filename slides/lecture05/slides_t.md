---
title: "\\emoji{wtf} XAI Lecture 05 (Tamed) \\emoji{rainbow} "
subtitle: "Rule Based Approaches"
bibliography: references.bib
---

# Disclaimer

\input{../disclaimer.tex}

---

# Paper 1

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/paper1_title.png}
\end{center}

[@letham2015interpretable]

---

# Contributions

- **Bayesian Rule Lists (BRL):** a generative model that outputs an ordered `if-then-else` decision list

- **Novel sparsity-inducing prior:** truncated Poisson priors over list length and rule complexity encourage short lists with simple conditions

- **Predictive accuracy on par** with Random Forests, SVMs, and CHADS$_2$ — while remaining fully interpretable

---

# Decision List: Titanic Example

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/decision_list_example.png}
\end{center}

- **Rules fire in order** — the first matching rule determines the prediction
- Values in parentheses are **95% credible intervals** — the narrower, the more data behind that rule
- BRL doesn't output a single list — it maintains a **posterior distribution over many possible lists**

---

# How Does BRL Work?

\begin{center}
\large
\textbf{Mine candidate rules} $\xrightarrow{\text{FP-Growth}}$ \textbf{Define prior} $\xrightarrow{}$ \textbf{Compute likelihood} $\xrightarrow{\text{MCMC}}$ \textbf{Posterior over lists}
\end{center}

\vspace{1em}

- **Step 1 — Mine:** extract frequent `if` conditions from data using FP-Growth
- **Step 2 — Prior:** favor short lists with simple rules (truncated Poisson)
- **Step 3 — Likelihood:** measure how well a list explains the observed labels
- **Step 4 — MCMC:** sample decision lists proportionally to their posterior probability

---

# Pre-mined Rules

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/premined_rules_intuition.png}
\end{center}

- FP-Growth extracts all frequent conditions (antecedents) from the data — e.g., `{diabetes}`, `{age > 60}`, `{diabetes, age > 60}`
- BRL only searches over this **pre-mined set** — this keeps the problem tractable and improves generalization

---

# Bayesian Association Rules

A **Bayesian association rule** predicts a probability distribution over classes, not a single label:

$$a \rightarrow y \sim \text{Multinomial}(\boldsymbol{\theta}_j), \qquad \boldsymbol{\theta}_j \sim \text{Dirichlet}(\boldsymbol{\alpha} + \mathbf{N}_j)$$

**In plain English:** for each rule $a$, we estimate the probability of each class by combining prior belief ($\boldsymbol{\alpha}$) with observed counts ($\mathbf{N}_j$) — the more data, the more the prior is washed out.

**Example:** rule `age > 60 AND diabetes` captures 10 patients: 7 stroke, 3 no stroke. With $\boldsymbol{\alpha} = (1,1)$, posterior $= \text{Dirichlet}(8, 4)$ → stroke probability $\approx 67\%$.

---

# Dirichlet-Multinomial: The Key Idea

The **Dirichlet** distribution is a prior over probability vectors — it represents our belief about class probabilities *before* seeing data.

$$\boldsymbol{\theta} \mid \mathbf{N}_j, \boldsymbol{\alpha} \sim \text{Dirichlet}(\boldsymbol{\alpha} + \mathbf{N}_j)$$

**In plain English:** start with a prior guess ($\boldsymbol{\alpha}$), then add observed counts ($\mathbf{N}_j$) — the posterior is just the sum. No complex integrals needed.

| | Prior | Observed | Posterior |
|---|---|---|---|
| Stroke | $\alpha_1 = 1$ | $N_1 = 7$ | $8$ |
| No Stroke | $\alpha_2 = 1$ | $N_2 = 3$ | $4$ |

Estimated stroke probability: $8 / (8+4) \approx 67\%$

---

# Generative Model

\begin{center}
\includegraphics[width=0.65\columnwidth]{imgs/generative_model.png}
\end{center}

$$p(d \mid \mathbf{x}, \mathbf{y}, \mathcal{A}, \boldsymbol{\alpha}, \lambda, \eta) \propto \underbrace{p(\mathbf{y} \mid \mathbf{x}, d, \boldsymbol{\alpha})}_{\text{likelihood}} \cdot \underbrace{p(d \mid \mathcal{A}, \lambda, \eta)}_{\text{prior}}$$

**In plain English:** a list $d$ is good if it both explains the data well *and* was a plausible list to begin with. Bayes combines both signals.

---

# Prior: Encouraging Sparsity

$$p(d \mid \mathcal{A}, \lambda, \eta) = p(m \mid \mathcal{A}, \lambda) \prod_{j=1}^{m} p(c_j \mid c_{<j}, \mathcal{A}, \eta)\, p(a_j \mid a_{<j}, c_j, \mathcal{A})$$

**In plain English:** the prior penalizes long lists ($\lambda$) and rules with many conditions ($\eta$) — it's a built-in preference for simplicity.

- $\lambda$: expected number of rules — lower $\lambda$ → shorter lists preferred
- $\eta$: expected number of conditions per rule — lower $\eta$ → simpler rules preferred
- Both use **truncated Poisson** so the list length can never exceed the number of available rules

---

# Likelihood

$$p(\mathbf{y} \mid \mathbf{x}, d, \boldsymbol{\alpha}) = \prod_{j} \int \text{Multinomial}(\mathbf{N}_j \mid \boldsymbol{\theta}_j)\, \text{Dirichlet}(\boldsymbol{\theta}_j \mid \boldsymbol{\alpha})\, d\boldsymbol{\theta}_j$$

**In plain English:** for each rule in the list, count how many observations of each class it captures — then ask how probable those counts are. Multiply across all rules to get the total likelihood.

- Thanks to Dirichlet-Multinomial conjugacy, $\boldsymbol{\theta}_j$ can be integrated out analytically — no numerical approximation needed
- A list scores high when each rule captures observations that are mostly from the same class

---

# MCMC: Searching Over Decision Lists

BRL uses **Markov Chain Monte Carlo** to sample lists from the posterior — instead of finding one optimal list, it explores many.

At each iteration, propose a new list $d^*$ from the current $d^t$ via one of three moves:

- **Add:** insert a new rule from $\mathcal{A}$
- **Remove:** delete a rule from $d^t$
- **Move:** relocate an existing rule to a different position

**In plain English:** think of it as randomly editing the current list and deciding whether the new version is better — good edits are usually accepted, bad ones are accepted with small probability to avoid getting stuck.

---

# MCMC: Metropolis-Hastings

$$A = \min\left(1,\ \frac{p(d^* \mid \mathbf{x}, \mathbf{y}, \mathcal{A}) \cdot Q(d^t \mid d^*)}{p(d^t \mid \mathbf{x}, \mathbf{y}, \mathcal{A}) \cdot Q(d^* \mid d^t)}\right)$$

**In plain English:** compare how good the proposed list $d^*$ is versus the current list $d^t$. If $d^*$ is better, always accept it. If it's worse, accept it anyway with some probability — this prevents getting trapped in local optima.

- **Posterior ratio:** is $d^*$ a better explanation of the data?
- **Proposal ratio:** corrects for asymmetric moves (some edits are easier to propose than others)

---

# Implementing BRL in Python

\fontsize{7.5pt}{6pt}
!!include python: codes/brl_pseudo.py
\normalsize

---

# Prediction

Once MCMC converges to a point estimate $\hat{d}$, predicting a new observation $\tilde{x}$ is straightforward:

$$p(\tilde{y} = l \mid \tilde{x}, \hat{d}, \mathbf{x}, \mathbf{y}, \boldsymbol{\alpha}) = \frac{\alpha_l + N_{j(\hat{d},\tilde{x}),l}}{\sum_{k=1}^{L}(\alpha_k + N_{j(\hat{d},\tilde{x}),k})}$$

**In plain English:** find the first rule in $\hat{d}$ that matches $\tilde{x}$, then report the class probabilities estimated from that rule's data — prior counts plus observed counts, normalized to sum to 1.

```python
def predict(x, d, N, alpha):
    j = first_matching_rule(x, d)
    counts = alpha + N[j]
    return counts / counts.sum()
```

---

# Experiment: Stroke Prediction

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/stroke_prediction_auc.png}
\end{center}

- Dataset: $N = 12{,}586$ patients, 14% stroke — **6000× larger** than the data used to build CHADS$_2$
- BRL matches or exceeds CHADS$_2$ AUC while producing a **human-readable list**
- Note: AUC may be misleading given class imbalance — AUPRC would be more appropriate here

---

# Paper 2

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/paper2_title.png}
\end{center}

[@lakkaraju2016interpretable]

---

# Contributions

- A framework called \textbf{Interpretable Decision Sets (IDS)} for multi-class classification

- \textbf{Joint objective function} that simultaneously optimizes accuracy and interpretability — with a proof of \textbf{submodularity}

- Optimization via **Smooth Local Search** with a formal $2/5$ approximation guarantee

- \textbf{Quantitative interpretability metrics} + user study validation

---

# Decision Lists vs Decision Sets

:::: columns
::: column
**Decision Lists (BRL)**

- Ordered `if-then-else` rules
- Order matters: first match wins
- Zero overlap by construction
- Harder for humans to reason about: understanding one rule requires knowing all preceding rules
:::
::: column
**Decision Sets (IDS)**

- Unordered `if-then` rules
- Each rule is independent
- Overlap is minimized but allowed
- Easier to reason about: each rule stands on its own

:::
::::

---

# Problem Setup

**Input:**

- Data $\mathcal{D} = \{(\mathbf{x}_i, y_i)\}_{i=1}^{N}$, class labels $\mathcal{C}$
- Frequent itemsets $\mathcal{S}$ mined via Apriori — e.g., `Gender = Female AND Age > 35`

**Output:** a decision set $\mathcal{R} \subseteq \mathcal{S} \times \mathcal{C}$

**In plain English:** pick a subset of (condition, class) pairs from all possible combinations — the result is your rule set.

$$\underset{\mathcal{R} \subseteq \mathcal{S} \times \mathcal{C}}{\text{argmax}} \sum_{i=1}^{7} \lambda_i f_i(\mathcal{R})$$

**In plain English:** find the rule set $\mathcal{R}$ that maximizes a weighted sum of seven desirable properties.

---

# Desiderata: What Makes a Good Rule Set?

| Property | What it means |
|---|---|
| **Parsimony** | Few rules, short conditions |
| **Distinctness** | Rules don't cover the same data points |
| **Class Coverage** | At least one rule per class |
| **Precision** | Rules don't misclassify the points they cover |
| **Recall** | Rules collectively cover all data points |

Each property is captured by one or more terms $f_i$ in the objective — and the $\lambda_i$ weights let you trade them off.

---

# Objective: Parsimony & Distinctness

## Fewer rules ($f_1$) and shorter rules ($f_2$)

$$f_1(\mathcal{R}) = |\mathcal{S}| - \text{size}(\mathcal{R}), \qquad f_2(\mathcal{R}) = L_{\max} \cdot |\mathcal{S}| - \sum_{r \in \mathcal{R}} \text{length}(r)$$

**In plain English:** prefer 12 rules over 30, and prefer `Age > 60` over `Age > 60 AND Diabetes AND Hypertension AND Smoker`.

## Low overlap ($f_3$, $f_4$)

- $f_3$: two rules predicting the **same** class shouldn't cover the same patients
- $f_4$: two rules predicting **different** classes shouldn't cover the same patients — otherwise a tie-breaking rule decides, which hurts interpretability

---

# Objective: Coverage, Precision & Recall

## Class coverage ($f_5$)

**In plain English:** every class must have at least one rule — this is critical for rare but important classes like rare diseases.

## Precision ($f_6$) and Recall ($f_7$)

$$f_6(\mathcal{R}) = N \cdot |\mathcal{S}| - \sum_{r \in \mathcal{R}} |\text{incorrect-cover}(r)|$$

**In plain English ($f_6$):** each rule should cover mostly patients of the right class — not a mix.

**In plain English ($f_7$):** the rule set should correctly classify as many patients as possible — leaving few uncovered.

---

# Submodularity: Why It Matters

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/dreturns.png}
\end{center}

\small
**In plain English:** adding a rule to a small set helps a lot; adding the same rule to a large set helps less — this is **diminishing returns**, and it's exactly what submodularity captures for set functions.

\begin{alertblock}{Key Property}
\small
A non-negative linear combination of submodular functions is submodular — so the full IDS objective inherits this property.
\end{alertblock}

---

# Optimization: Smooth Local Search

Maximizing the IDS objective is **NP-hard** — the space of possible rule sets is exponential in $|\mathcal{S}|$.

**Smooth Local Search (SLS)** provides a $2/5$ approximation guarantee:

1. Start with $\mathcal{R} = \emptyset$
2. Estimate marginal contribution of each candidate rule
3. Add rules that improve the objective enough
4. Remove rules that hurt the objective enough
5. Repeat until convergence; return a random subset (the "smoothing" step)

**In plain English:** instead of checking all $2^{|\mathcal{S}|}$ possible sets, SLS makes smart local edits — and guarantees the result is worth at least $2/5$ of the theoretical optimum.

---

# Evaluation: Datasets

\fontsize{7.5pt}{6pt}
| **Dataset** | **# Datapoints** | **Features** | **Classes** |
|---|---|---|---|
| **Bail Outcomes** | 86K | Gender, age, offense details, criminal record | No Risk, Failure to Appear, New Criminal Activity |
| **Student Performance** | 21K | Gender, age, grades, absence rates, suspension history | Graduated on Time, Delayed Graduation, Dropped Out |
| **Medical Diagnosis** | 150K | Ailments, age, BMI, gender, smoking, medical history | Asthma, Diabetes, Depression, Lung Cancer, Rare Blood Cancer |

\normalsize

All three datasets involve **high-stakes decisions** — justice, education, and medicine — where interpretability is not optional.

---

# Results: Predictive Performance

\fontsize{7.5pt}{6pt}
| **Method** | **Bail** | **Student** | **Medical** |
|---|---|---|---|
| **IDS** | **69.78** | **75.12** | **61.19** |
| Bayesian Decision Lists | 67.18 | 72.54 | 59.18 |
| Decision Trees | 70.08 | 75.31 | 63.28 |
| Gradient Boosted Trees | 71.23 | 77.18 | 64.21 |
| Random Forests | 70.87 | 77.12 | 63.92 |
\normalsize

IDS trades a small accuracy gap against black-box models for **full interpretability**. Note: class imbalance is likely in all three datasets — AUC results should be interpreted with caution.

---

# Results: Interpretability Metrics

| **Method** | **Frac. Overlap** | **Frac. Uncovered** | **Avg. Rule Length** | **Num. Rules** | **Frac. Classes** |
|---|---|---|---|---|---|
| **IDS** | **0.09** | **0.13** | **3.17** | **12** | **1.00** |
| BDL | 0.00 | 0.18 | 8.46 | 11 | 0.67 |
| CBA | 0.00 | 0.14 | 8.60 | 32 | 1.00 |
| CN2 | 0.12 | 0.14 | 9.78 | 38 | 1.00 |

IDS rules are **3× shorter** than baselines, cover **all classes** (BDL misses 2 rare diseases), and use far fewer rules than CBA and CN2.

---

# Results: User Study

47 Stanford students assigned to either IDS or BDL — never both. Each answered 10 objective + 2 descriptive questions about a medical diagnosis rule set.

| **Task** | **Metric** | **IDS** | **BDL** |
|---|---|---|---|
| **Descriptive** | Accuracy | 0.81 | 0.17 |
| | Avg. Time (secs.) | 113 | 397 |
| **Objective** | Accuracy | 0.97 | 0.82 |
| | Avg. Time (secs.) | 28 | 36 |

IDS users were **4.7× more accurate** on descriptive tasks and **3.5× faster** — confirming that unordered rules are fundamentally easier for humans to reason about.

---

# BRL vs IDS — When to Use Each?

| | **BRL** | **IDS** |
|---|---|---|
| **Structure** | Ordered if-then-else list | Unordered if-then rules |
| **Prediction** | Probabilistic (credible intervals) | Deterministic (precision-based) |
| **Best for** | Binary classification, medical risk scoring | Multi-class problems with rare classes |
| **Uncertainty** | Built-in via Dirichlet-Multinomial | Not provided |
| **Optimization** | MCMC sampling | Submodular optimization ($2/5$ guarantee) |
| **Rule overlap** | Zero by construction | Minimized but allowed |
| **Use when** | You need calibrated probabilities | You need equally good rules for all classes |

---

# Key Takeaways

- Interpretability is **multifaceted** — sparsity, overlap, coverage, and rule length all matter independently

- **Ordered vs. unordered rules** is not just a structural choice — it fundamentally affects how humans understand models (user study: 4.7× accuracy gap)

- Both papers show interpretability and accuracy are **not mutually exclusive**

- Evaluating interpretability requires **both quantitative metrics and user studies**

- The right model depends on the task: BRL excels at **uncertainty quantification**, IDS at **multi-class clarity**

---

\begin{center}
\Huge Thank You!
\end{center}

---

# References {.allowframebreaks}

