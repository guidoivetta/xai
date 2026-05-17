---
title: "\\emoji{balance-scale} XAI: Explainability for Fairness \\& the Right to be Forgotten"
bibliography: references.bib

---

# Disclaimer

\input{../disclaimer.tex}

---

# Paper 1: Explainability for Fair Machine Learning

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/fairml_title.png}
\end{center}

[@begley2020explainability]

---

# Fair Machine Learning

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/fairml_history.png}
\end{center}

- Rapid growth of fairness research since 2015 — now a major concern
- Yet: many competing, often **incompatible** definitions
- And: fairness guarantees can be **gamed** by explanation manipulation

---

# Challenges: Defining Fairness

**Defining fairness is hard:**

- Many competing definitions — statistics-based, causal-reasoning-based, etc.
- Group outcomes vs.\ individual outcomes
- Requires contextual understanding

\begin{center}
\includegraphics[width=0.65\columnwidth]{imgs/fairml_challenges_table.png}
\end{center}

\begin{alertblock}{No universal definition}
Definitions often incompatible — satisfying one can violate another
\end{alertblock}

---

# Fairness Definition: Demographic Parity

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/fairml_demographic_parity.png}
\end{center}

\begin{definition}{}
\textbf{Demographic parity:} $f(x)$ must be unconditionally independent of sensitive attribute $a$
\end{definition}

**Example:** if 100 female and 100 male students apply to Harvard, demographic parity requires the **same admission percentage** for both groups — regardless of average qualification.

---

# Fairness Definition: Equalized Odds

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/fairml_equalized_odds.png}
\end{center}

\begin{definition}{}
\textbf{Equalized odds:} $f(x)$ must be independent of sensitive attribute $a$ \textbf{given} $y$
\end{definition}

Qualified and unqualified applicants have the same acceptance/rejection rates across groups — regardless of base rates.

---

# Challenge: Explanation Methods Can Be Manipulated

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/fairml_manipulation.png}
\end{center}

\begin{alertblock}{Problem (Dimanov, ECAI 2020)}
An explanation attack can mask a model's discriminatory use of a sensitive feature \textbf{without hurting accuracy} — fooling Gradients, SHAP, LIME, and other methods simultaneously
\end{alertblock}

---

# Proposed Solution

\begin{exampleblock}{Unified approach via Fairness Shapley Values}
A single framework covering many group-fairness criteria:
\begin{itemize}
\item demographic parity, equalised odds, conditional demographic parity
\item for each fairness definition, define a Shapley value function that attributes overall unfairness to individual features
\end{itemize}
\end{exampleblock}

- **Cannot hide unfairness** by manipulating explanations
  - Fairness Shapley values must collectively sum to the chosen fairness metric
- **Meta Algorithm**: learn a corrective perturbation $\delta_\theta$ to the original model — no full retraining needed

[@begley2020explainability]

---

# Methodology

---

# Explaining Model Accuracy

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/fairml_accuracy_shapley.png}
\end{center}

- Shapley value $\phi_v(i)$ attributes the total value $v(N)$ to feature $i$
- Value function marginalises over out-of-coalition features: $v_{f_y(x)}(S) = \mathbb{E}_{p(x')}[f_y(x_S \sqcup x'_{N\setminus S})]$
- Global Shapley: $\Phi_f(i) = \mathbb{E}_{p(x,y)}[\phi_{f_{y(x)}}(i)]$
- Sum: $\sum_i \Phi_f(i) = \mathbb{E}_{p(x,y)}[f_y(x)] - \mathbb{E}_{p(x')p(y)}[f_y(x')]$

---

# Explaining Model Fairness

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/fairml_fairness_shapley.png}
\end{center}

New value function capturing fairness (for **demographic parity**):

$$g_a(x) = f(x) \cdot \frac{(-1)^a}{p(a)} \qquad a: \text{sensitive attribute}$$

$$\sum_i \Phi_g(i) = \int dx\, p(x|a{=}0)\, f(x) - \int dx\, p(x|a{=}1)\, f(x)$$

Each feature's Fairness Shapley value = its marginal contribution to overall demographic disparity

---

# Learning Corrective Perturbations

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/fairml_perturbation.png}
\end{center}

By the **linearity axiom** of Shapley values, the fairness Shapley values of $f_\theta = f + \delta_\theta$ are the linear combination of Shapley values of $f$ and $\delta_\theta$.

$$f_\theta = f + \delta_\theta \qquad \delta_\theta(f(x), x, a) = \sigma\!\left(\sigma^{-1}(f(x)) + \tilde{\delta}_\theta(f(x), x, a)\right) - f(x)$$

- $\tilde{\delta}_\theta$: any training-time fairness algorithm (e.g., Agarwal et al. 2018)
- Only the perturbation is retrained — the original model stays fixed

---

# Experiments \& Results

---

# Datasets

\begin{columns}
\begin{column}{0.48\textwidth}
**Adult Dataset** (UCI)

*Task:* predict whether an individual earns more than \$50K/year based on demographics

**Sensitive attribute:** sex
\end{column}
\begin{column}{0.48\textwidth}
**COMPAS Recidivism Dataset** (Larson et al., 2016)

*Task:* predict recidivism risk based on demographics

**Sensitive attribute:** race
\end{column}
\end{columns}

---

# Explainability Results

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/fairml_explainability_plots.png}
\end{center}

- **Top row:** accuracy Shapley values; **Bottom row:** fairness Shapley values
- Key contributors to unfairness: **marital status**, **sex**, **relationship**
- After correction: fairness Shapley values near zero while accuracy is maintained

---

# Robustness of Fairness Explanation

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/fairml_robustness.png}
\end{center}

\begin{block}{Experiment: Suppress sex feature importance}
Suppressing sex in accuracy Shapley values: Demographic Parity Difference $0.193 \to 0.184$
\end{block}

Fairness Shapley values reveal the true sources of unfairness — manipulation of accuracy explanations cannot hide the fairness impact.

---

# Learnt Perturbations: Performance

\begin{columns}
\begin{column}{0.48\textwidth}
\begin{center}
\includegraphics[width=\columnwidth]{imgs/fairml_perf_dp.png}
\end{center}
\textbf{Demographic Parity:} No significant accuracy reduction while imposing fairness constraint
\end{column}
\begin{column}{0.48\textwidth}
\begin{center}
\includegraphics[width=\columnwidth]{imgs/fairml_perf_eo.png}
\end{center}
\textbf{Equalised Odds:} Same result — perturbative approach competitive with full retraining
\end{column}
\end{columns}

---

# Learnt Perturbations: Stability

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/fairml_stability.png}
\end{center}

\begin{exampleblock}{Advantage of perturbative approach}
Less variance and higher mean accuracy compared to Zhang et al. and Adel et al. across all fairness levels
\end{exampleblock}

Model-agnostic: structure/access requirements apply only to the perturbation, not the original model.

---

# Discussion Questions: Fair ML

1. What are the advantages and disadvantages of the perturbation method vs.\ other training-time fairness algorithms?
2. If a feature contributes greatly to unfairness (e.g., marital status in demographic parity), is it always correct to remove it from the model?
3. After reading this paper, what is your opinion on using interpretability methods to **validate** the fairness of ML models?

[@begley2020explainability]

---

# Paper 2: Towards Bridging the Gaps between the Right to Explanation and the Right to be Forgotten

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/rocerf_title.png}
\end{center}

[@krishna2022rocerf]

---

# Two Competing Rights

\begin{columns}
\begin{column}{0.48\textwidth}
\textbf{Right to an Explanation}

Given a model prediction, provide a reason — via Algorithmic Recourse (counterfactuals)

\vspace{0.5em}
Prior work: Multi-Objective CFE (Dandel et al. 2020), MACE (Karimi et al. 2020)
\end{column}
\begin{column}{0.48\textwidth}
\textbf{Right to be Forgotten}

User can ask to have personal data removed from databases and models

\vspace{0.5em}
Prior work: Descent-to-delete (Neel et al. 2021), Approximate deletion (Izzo et al. 2021)
\end{column}
\end{columns}

\begin{alertblock}{The Conflict}
Forgetting $\Rightarrow$ Model changes $\Rightarrow$ Counterfactual explanation becomes invalid $\Rightarrow$ Right to explanation not met
\end{alertblock}

---

# Previous Work \& Motivation

- **Pawelczyk et al.\ 2022**: identified the tradeoff between right to explanation and right to be forgotten
  - Trade-off stems from the fact that current explanation methods ignore underlying model changes
- **ROAR** (Upadhyay et al.\ 2021): methods that assume certain model changes
  - But: we can't know *exactly* how a model changes as a result of forgetting
- Pawelczyk et al.\ highlighted the problem — there is a need for a **solution**

\begin{exampleblock}{This Paper}
ROCERF: first algorithmic framework to address this tradeoff, with theoretical guarantees
\end{exampleblock}

---

# Contributions

\begin{exampleblock}{ROCERF: \textbf{RO}bust \textbf{C}ounterfactual \textbf{E}xplanations under the \textbf{R}ight to be \textbf{F}orgotten}
\end{exampleblock}

1. First framework to formally address the right-to-explanation vs.\ right-to-be-forgotten tradeoff
2. Efficient approximation via first-order Taylor expansion (avoids $\binom{n}{k}$ retraining)
3. Theoretical bounds on cost and validity for linear and nonlinear models
4. ROCERF **outperforms** existing counterfactual explanation methods (SCFE, C-CHVAE, ROAR)

[@krishna2022rocerf]

---

# ROCERF Framework

---

# Notation

\begin{center}
\includegraphics[width=0.82\columnwidth]{imgs/rocerf_notation.png}
\end{center}

- Training data $D = \{(x_i, y_i)\}_{i=1}^n$, $y_i \in \{-1, +1\}$
- **Data weight vector** $w \in \{0,1\}^n$: $w_i = 1$ (in training), $w_i = 0$ (forgotten)
- $w = \mathbf{1}$: no data removed; $f_{\theta_1}$: model trained on all data; $f_{\theta_w}$: model on $D_w$

---

# Counterfactual Explanation as Optimization

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/rocerf_cfe_opt.png}
\end{center}

Standard CFE: find the closest valid counterfactual under the **current** model

$$\min_{x \in \mathcal{X}} \|x - x_0\|_2 \quad \text{subject to} \quad f_{\hat{\theta}_1}(x) \geq 0$$

**Problem:** after data deletion, $f_{\theta_w} \neq f_{\theta_1}$ — the CFE may no longer be valid.

---

# $k$-Removal Robust CFE

\begin{center}
\includegraphics[width=0.82\columnwidth]{imgs/rocerf_k_removal.png}
\end{center}

\begin{definition}{}
\textbf{$k$-RR CFE:} a counterfactual that remains valid upon removal of \textbf{any} $k$ data points
\end{definition}

$$\mathcal{W}^{(k)} = \{w \in \{0,1\}^n : \|w\|_1 = n - k\}$$

$$\min_{x \in \mathcal{X}} \|x - x_0\|_2 \quad \text{s.t.} \quad f_{\hat{\theta}_w}(x) \geq 0,\ \forall w \in \mathcal{W}^{(k)}$$

Naive approach: train $\binom{n}{k}$ classifiers with $\binom{n}{k}$ constraints — \textbf{computationally impractical!}

---

# Efficient Approximation

Fix $x$ and approximate $f_{\hat{\theta}_w}(x)$ via **first-order Taylor expansion** in $w$:

$$\tilde{f}_{\hat{\theta}_w}(x) = f_{\hat{\theta}_1}(x) + \frac{\partial f_{\hat{\theta}_w}(x)}{\partial w}\bigg|_{w=\mathbf{1}} (w - \mathbf{1})$$

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/rocerf_approx_formula.png}
\end{center}

Key result (via infinitesimal jackknife, Giordano et al. 2019):

$$\tilde{f}_{\hat{\theta}_w}(x) = f_{\hat{\theta}_1}(x) + \frac{1}{n} \sum_{i:\, w_i=0} \beta(x)^T H^{-1} g_i(\hat{\theta}_1)$$

where $\beta(x) = \left(\frac{\partial f_\theta(x)}{\partial \theta}\big|_{\theta=\hat{\theta}_1}\right)^T$ and $H = \frac{1}{n}\sum_i h_i(\hat{\theta}_1)$

---

# From $\binom{n}{k}$ to a Single Constraint

\begin{center}
\includegraphics[width=0.82\columnwidth]{imgs/rocerf_final_opt.png}
\end{center}

Define $\mathcal{A}(x) := \{\beta(x)^T H^{-1} g_i(\hat{\theta}_1)\}$ — independent of weight vector $w$

The worst-case constraint reduces to picking the **$k$ smallest** elements of $\mathcal{A}(x)$:

$$f_\mathcal{A}^{(k)}(x) := f_{\hat{\theta}_1}(x) + \frac{1}{n} \min_{\mathcal{B} \subseteq \mathcal{A}(x),\, |\mathcal{B}|=k} \sum_{b \in \mathcal{B}} b$$

Final optimization: $\min_{x \in \mathcal{X}} \|x - x_0\|_2 \quad \text{s.t.} \quad f_\mathcal{A}^{(k)}(x) \geq \delta$

Solved via **penalty method**: $\min_x J_t(x) = \lambda_t \phi(\delta - f_\mathcal{A}^{(k)}(x)) + \|x - x_0\|_2$

---

# Practical Considerations

- **Computational cost:** $O(n)$ — only requires computing $\beta(x)^T H^{-1} g_i(\hat{\theta}_1)$ for each sample
- **Hyperparameters:** $k$ (number of removals), $\delta$ (approximation error margin)
- **Linear models:** can avoid the backward pass entirely

$$\tilde{f}_{\hat{\theta}_w}(x) = \hat{\theta}_1^T x + \frac{1}{n} \sum_{i:\, w_i=0} x^T H^{-1} g_i(\hat{\theta}_1)$$

---

# Theoretical Analysis: Validity \& Cost

\begin{center}
\includegraphics[width=0.78\columnwidth]{imgs/rocerf_validity_cost.png}
\end{center}

**Validity:** fraction of weight vectors $w \in \mathcal{V}$ for which the CFE $c(x)$ remains valid under $f_{\hat{\theta}_w}$

**Cost:** average $\ell_2$ distance from original $x$ to counterfactual $c(x)$

\begin{block}{Linear Model Bound}
Additional cost to achieve robust validity has upper bound $O(k/n)$:
$$\|\tilde{x}_0^{(k)} - x_0\|_2 \leq \|\tilde{x}_0 - x_0\|_2 + \frac{kC}{n\|\hat{\theta}_1\|_2}$$
\end{block}

For nonlinear (Mu-strongly convex) models: bound is $O(k/n\mu)$ under regularity conditions.

---

# Experiments \& Results

---

# Experimental Setup

\begin{columns}
\begin{column}{0.48\textwidth}
**Datasets:** 3 real-world binary classification datasets from high-stakes decision making

- German Credit
- COMPAS
- Adult

**Models:** regularized logistic regression + 3-layer feedforward NN
\end{column}
\begin{column}{0.48\textwidth}
**Baselines:** SCFE, C-CHVAE, ROAR

**Evaluation:**
- Validity: randomly remove fraction $\alpha \in [0.5\%, 5\%]$
- Repeat $M = 100$ times
- $k = 0.5\%$ of training set, $\delta = 0$
\end{column}
\end{columns}

---

# Results: Average Validity (Logistic Regression)

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/rocerf_results_lr.png}
\end{center}

\begin{exampleblock}{ROCERF achieves near-perfect validity}
While SCFE, C-CHVAE, and ROAR degrade significantly as more data is removed, ROCERF (red) maintains validity $\approx 1.0$ across all datasets
\end{exampleblock}

---

# Results: Average Validity (Neural Networks)

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/rocerf_results_nn.png}
\end{center}

\begin{alertblock}{Non-linear models: more complex behavior}
Some baselines improve validity as more data is forgotten (non-intuitive). ROCERF still competitive — though linear approximation assumptions are more strained for complex NNs.
\end{alertblock}

---

# Results: Average Cost

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/rocerf_costs_tables.png}
\end{center}

- ROCERF achieves **comparable or lower cost** than baselines (except SCFE on some datasets)
- C-CHVAE has very high cost — pays dearly for its robustness approach
- Cost overhead of ROCERF over standard CFE is bounded by $O(k/n)$

---

# Sensitivity to Hyperparameter $k$

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/rocerf_sensitivity.png}
\end{center}

\begin{exampleblock}{Robust to $k$}
ROCERF validity remains near 1.0 across all tested values of $k$ (0.005n to 0.05n) on COMPAS and Adult. Results insensitive to choice of $k$ in practice.
\end{exampleblock}

---

# Conclusions: ROCERF

- **ROCERF** is the first framework to formally bridge the gap between the right to explanation and the right to be forgotten
- Provably robust to model updates triggered by data deletion requests
- Efficient: reduces exponential constraints to $O(n)$ computation via first-order approximation
- Theoretical guarantees on validity and cost for linear models; empirically strong for NNs

---

# Limitations \& Future Work

- **Non-linear models:** linear approximation may not capture complex NN behavior — validity can improve as more data is forgotten (non-intuitive)
- **ROAR vs.\ ROCERF:** results track closely in some settings — is ROAR sufficient?
- **Sensitivity to $k$:** why doesn't performance vary more with $k$? — higher $\alpha$ regimes needed
- **Open question:** why has recourse literature focused on linear approximations when non-linear models exhibit non-intuitive behavior?

---

# Discussion Questions: ROCERF

1. This paper bridges the right-to-explanation vs.\ right-to-be-forgotten gap (unlike the privacy vs.\ explanation tradeoff, which seems more opposed). What other XAI tradeoffs do you think can be bridged?
2. Given that ROAR exists, do we really need ROCERF? Could deletion of data parameters be viewed as a perturbation of model parameters?
3. Why has recourse literature focused on linear approximations when results show non-linear models exhibit non-intuitive behavior?

[@krishna2022rocerf]

---

\begin{center}
\Huge Thank You!
\end{center}

---

# References {.allowframebreaks}

\footnotesize
