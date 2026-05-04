---
title: "\\emoji{wtf} XAI Lecture 17"
subtitle: "Unified Frameworks for Model Explanation"
bibliography: references.bib

---

# Disclaimer

\input{../disclaimer.tex}

---

# Paper 1

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/paper1_title.png}
\end{center}

**Authors:** Ian C. Covert, Scott Lundberg, Su-In Lee

[@covert2021explaining]

---

# Motivation

\begin{exampleblock}{}
\centering There is a need for a unifying framework
\end{exampleblock}

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/motivation_diagram.png}
\end{center}

LIME, SHAP, RISE, INVASE, REAL-X, FIDO-CA, Extremal Perturbations, ...

---

# Contributions

1. A unified framework that characterizes **26** existing explanation methods $\rightarrow$ **removal-based explanations**

2. **Mathematical tools** to represent different approaches for **removing features** from ML models

3. Removal-based explanations are implicitly tied to **cooperative game theory** $\rightarrow$ advantages of the **Shapley value** over alternative allocation strategies

4. Feature removal is a simple application of **subtractive counterfactual reasoning**

---

# Previous Unifying Efforts

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/previous_unifying_efforts.png}
\end{center}

- LIME, DeepLIFT, LRP, QII $\rightarrow$ **SHAP**
- Grad $\times$ Input, DeepLIFT, LRP, Integrated Gradients $\rightarrow$ **modified gradient back propagations**
- permutation tests, Shapley Net Effects, feature ablation, SAGE $\rightarrow$ **additive importance measures**

---

# The Removal-based Explanations Framework

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/framework_overview.png}
\end{center}

:::: columns
::: {.column width="30%"}
**1. Feature removal**

$F: \mathcal{X} \times \mathcal{P}(D) \mapsto \mathcal{Y}$
:::
::: {.column width="35%"}
**2. Model behavior**

$u: \mathcal{P}(D) \mapsto \mathbb{R}$
:::
::: {.column width="33%"}
**3. Summary technique**

$E: U \mapsto \mathbb{R}^d$ or $E: U \mapsto \mathcal{P}(D)$
:::
::::

---

# Methods Survey

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/methods_survey_table.png}
\end{center}

**Key insights:**
1. Common: marginalize out removed features with their conditional distribution + Shapley values
2. Relatively unique and spatially isolated: RISE; LIME for tabular data; INVASE
3. Many combinations left unexplored!

---

# Mathematical Formulation

---

# Overview

:::: columns
::: {.column width="30%"}
**1. Feature removal**

$$F: \mathcal{X} \times \mathcal{P}(D) \mapsto \mathcal{Y}$$
:::
::: {.column width="35%"}
**2. Model behavior**

$$u: \mathcal{P}(D) \mapsto \mathbb{R}$$
:::
::: {.column width="33%"}
**3. Summary technique**

$$E: U \mapsto \mathbb{R}^d$$
$$\text{or}$$
$$E: U \mapsto \mathcal{P}(D)$$
:::
::::

---

# Defining Feature Removal

$$F(x) = f(\text{features\_to\_keep},\ \text{features\_to\_remove})$$

- **Zero ablation** $\quad F(x_S) = f(x_S, 0)$
- **Default values** $\quad F(x_S) = f(x_S, r_{\bar{S}})$
- **Generative model** $\quad F(x_S) = f(x_S, \tilde{x}_{\bar{S}})$
- **Train separate models**
  - Train surrogate models
- **"Missingness" during training**

---

# Defining Feature Removal (cont)

**Marginalization**

- **Marginalize with conditional** $\quad F(x_S) = \mathbb{E}[f(X) \mid X_S = x_S]$
  - Tree distribution
- **Marginalize with marginal** $\quad F(x_S) = \mathbb{E}[f(x_S, X_{\bar{S}})]$
- **Marginalize with product of marginals** $\quad F(x_S) = \mathbb{E}_{\prod_{i \in D} p(X_i)}[f(x_S, X_{\bar{S}})]$
- **Marginalize with uniform** $\quad F(x_S) = \mathbb{E}_{\prod_{i \in D} u_i(X_i)}[f(x_S, X_{\bar{S}})]$
- **Marginalize with replacement distribution** $\quad F(x, S) = \mathbb{E}_{\prod_{i \in D} q_{x_i}(X_i)}[f(x_S, X_{\bar{S}})]$

---

# Explaining Model Behaviors

Given the newly defined model $F(x_S)$, we need a metric to assess how important the $x_S$ features are.

**Options:**

| Behavior | Formula |
|----------|---------|
| Prediction | $F(x_S)$ |
| Prediction loss | $-\ell(F(x_S), y)$ |
| Prediction mean loss | $-\mathbb{E}_{p(Y \mid X=x)}\left[\ell(F(x_S), Y)\right]$ |
| Dataset loss | $-\mathbb{E}_{XY}\left[\ell(F(X_S), Y)\right]$ |
| Prediction loss w.r.t. output | $-\ell(F(x_S), F(x))$ |
| Dataset loss w.r.t. output | $-\mathbb{E}_X\left[\ell(F(X_S), F(X))\right]$ |

---

# Summarizing Feature Influence

Two related approaches:

- **Map feature to real number value (feature attribution)** $\quad E: \mathcal{U} \rightarrow \mathbb{R}^d$
- **Map dataset to a set of important features (feature selection)** $\quad E: \mathcal{U} \rightarrow \mathcal{P}(D)$

Both are related; often the second is just a threshold applied to the first.

\begin{center}
\includegraphics[width=0.5\columnwidth]{imgs/summarizing_influence.png}
\end{center}

---

# Computational Complexity

**How to isolate features?**

- Consider every subset including the feature in question
  - Exact solutions are $O(2^d / d)$ in the worst case
  - SHAP, RISE summarization, LIME additive model, etc.
- Only consider the subset where you remove the feature
  - Polynomial in $d$
  - Occlusion, PRedDiff, CXPlain, permutation tests, etc.

**Approximations?** (much faster, but lose worst-case guarantees)

- Sampling
- TreeSHAP (dynamic programming solution for tree models)
- Solve a continuous relaxation of the subset problem (i.e. learn a mask)
- Greedy search (MIR)
- Learn a model to do the explanation task

\begin{center}
\includegraphics[width=0.45\columnwidth]{imgs/computational_complexity.png}
\end{center}

---

# Connections to Other Theoretical Frameworks

---

# Game Theory

Same setup as what the SHAP people said:

- Cooperative games where we solve for allocations
- Makes SHAP unique; however, other methods can be viewed as fitting (linear, additive) models to cooperative games
- Proofs in appendix, not critical

| Summarization | Methods | Related To |
|---|---|---|
| Shapley value | SHAP, TreeSHAP, KernelSHAP, LossSHAP, IME, QII, Shapley Net Effects, SAGE, SPVIM | Shapley value, probabilistic values, modeling cooperative games |
| Mean value when included | RISE | Banzhaf value, probabilistic values, modeling cooperative games |
| Remove/include individual players | Occlusion, PredDiff, CXPlain, permutation tests, univariate predictors, feature ablation (LOCO) | Probabilistic values, modeling cooperative games |
| Fit additive model | LIME | Shapley value, Banzhaf value, modeling cooperative games |
| High/low value coalitions | MP, EP, MIR, MM, L2X, INVASE, REAL-X, FIDO-CA | Maximum/minimum excess |

---

# Information Theory

- $f$ approximates response variable's conditional distribution
  - Classification: $f(x) \approx p(Y \mid X = x)$
  - Regression: $f(x) \approx \mathbb{E}[Y \mid X = x]$
- $F$ can also approximate conditional distribution (over subsets!)
  - Set of conditional distributions: $\{q(Y \mid X_S) : S \subseteq D\}$
- Want this to be probabilistically valid (called **consistent**)
  - Countable Additivity
  - Bayes' Rule
  - Occurs only when average over conditional distribution

---

# Information Theory Quantities

| Model Behavior | Set Function | Methods | Related To |
|---|---|---|---|
| Prediction | $u_x$ | Occlusion, MIR, MM, IME, QII, LIME, MP, EP, FIDO-CA, RISE, SHAP, KernelSHAP, TreeSHAP | Conditional probability, conditional expectation |
| Prediction loss | $v_{xy}$ | LossSHAP, CXPlain | Pointwise mutual information |
| Prediction mean loss | $v_x$ | INVASE | KL divergence with conditional distribution |
| Dataset loss | $v$ | Permutation tests, univariate predictors, feature ablation (LOCO), Shapley Net Effects, SAGE, SPVIM | Mutual information (with label) |
| Prediction loss (output) | $w_x$ | L2X, REAL-X | KL divergence with full model output |
| Dataset loss (output) | $w$ | Shapley Effects | Mutual information (with output) |

---

# Cognition Theory

- Subtractive Counterfactual (Epstude and Roese, 2008) and Method of Difference (Mill, 1884)
- Norm Theory and the downhill rule
- Trade-off between simplicity and completeness

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/cognition_theory.png}
\end{center}

**Simplicity** $\longleftrightarrow$ **Completeness**

- Global feature selection $\rightarrow$ Global feature attribution $\rightarrow$ Local feature selection $\rightarrow$ Local feature attribution

---

# Approximations of SHAP

**Conditional Distribution is Intractable**

$$\mathbb{E}[f(X) \mid X_S = x_S] = \mathbb{E}_{p(X_{\bar{S}} \mid X_S = x_S)}[f(x_S, X_{\bar{S}})]$$

- **Assume feature independence** $\approx \mathbb{E}_{p(X_{\bar{S}})}[f(x_S, X_{\bar{S}})]$
- **Assume model linearity** $\approx f(x_S, \mathbb{E}[X_{\bar{S}}])$

Or:

- **Assume normality** (but "one does not simply use the normal distribution")

---

# Approximations of SHAP (cont)

:::: columns
::: {.column width="55%"}

- **Generative Model**
  - Draw samples from cGAN
  - Single-Sample Monte Carlo Approximation

- **Surrogate Model**
  - Train a model to match model predictions
  - Objective: $\min_F \mathbb{E}_X \mathbb{E}_S\left[\ell(F(X_S), f(X))\right]$

- **Training with Missing**
  - Train your original model with missing features
  - Objective: $\min_F \mathbb{E}_{XY} \mathbb{E}_S\left[\ell(F(X_S), Y)\right]$

- **Separate Model**
  - Train separate model for each possible subset

:::
::: {.column width="42%"}

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/approximations_shap_generative.png}
\end{center}

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/approximations_shap_surrogate.png}
\end{center}

:::
::::

---

# Experiments

---

# Methods Survey (Full)

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/methods_survey_full.png}
\end{center}

> **So many unexplored combinations!!!**

---

# Experimental Goals

1. Fill in the gaps of removal-based method combinations (hint: **SHAP!**)
2. Verify that the information-theoretic model works best
3. Verify other theorized relationships between existing methods

---

# Removal-Based Model Combinations

:::: columns
::: {.column width="30%"}
**Feature Removal**

- Default Values
- Marginalization
  - Uniform
  - Product
  - Joint
:::
::: {.column width="35%"}
**Model Behavior**

- Prediction
- Prediction Loss
- Dataset Loss
:::
::: {.column width="32%"}
**Summary Technique**

- Removing
- Including
- Mean when Included
- Banzhaf
- Shapley

> **Over 80 combinations tested!**
:::
::::

---

# Experimental Domains

:::: columns
::: {.column width="55%"}

- **Census Income**
  - 48,842 individuals
  - 14 socioeconomic features, >\$50k income or not
  - Light-GBM (gradient boosted tree)
- **MNIST**
  - 70,000 handwritten digits
  - 32×32 grayscale pixels
  - CNN (14 layers)
- **Breast Cancer Subtypes**
  - 510 patients
  - Random subset of 100/17,814 genes
  - Logistic regression

:::
::: {.column width="42%"}

\begin{center}
\includegraphics[width=0.7\columnwidth]{imgs/experimental_domains.png}
\end{center}

:::
::::

---

# 1. Census Income: Qualitative

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/census_income_results_1.png}
\end{center}

- Bottom four the same $\rightarrow$ Approximate conditional distribution
- Include and Banzhaf/Shapley the same $\rightarrow$ Similar formulations
- Mean When Included is different

---

# 1. Census Income: Quantitative

How good is the conditional distribution approximation?

- Intractable, so treat separate models as ground truth
- **Surrogate Removal Method does best**

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/census_income_correlation.png}
\end{center}

---

# 2. MNIST: Qualitative

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/mnist_qualitative_1.png}
\end{center}

- **Default Values** gives zero attribution to zero-valued features
- **Shapley "looks" the best**

---

# 2. MNIST: Quantitative

- **Insertion:** Remove the bottom-$k$ important features
- **Deletion:** Remove the top-$k$ important features
- Removing with surrogate is better!

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/mnist_quantitative.png}
\end{center}

---

# 3. Breast Cancer Subtypes: Qualitative

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/breast_cancer_qualitative.png}
\end{center}

- ESR1 gene is most important
- Hard to compare qualitatively
- Verify that "mean when included" is much different from the rest

---

# 3. Breast Cancer Subtypes: Quantitative

- Select only 20 most important genes
- **Surrogate + Shapley best!**

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/breast_cancer_quantitative.png}
\end{center}

---

# Conclusion (Paper 1)

- **SHAP + Surrogate Model is the best** $\rightarrow$ in line with information-theoretic connection
- The authors' unified framework helps us reason abstractly about these techniques
  - Able to identify and fill so many gaps in the combination of removal-based models

---

# Limitations (Paper 1)

- No limitations section
- No comparisons across model behavior
- Quantifying approximation quality with an approximation
- Evaluation metrics can be aligned with explanation method
  - Doesn't bode well for a universal unbiased metric
- Slightly suspect analysis for Breast Cancer dataset

---

# Discussion (Paper 1)

- Are removal-based the right framework to go in XAI?
- How do we reconcile with the fact that removing features may result in out-of-distribution behavior?
- What other unifying frameworks can you think of?
- Do you agree with the assessment that SHAP provides the best explanation?
- What methods do not fall under removal-based methods?

---

# Paper 2

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/paper2_title.png}
\end{center}

**Authors:** Tessa Han, Suraj Srinivas, Himabindu Lakkaraju

[@han2022explanation]

---

# Interpretability

- Machine Learning models make decisions in high stake settings (healthcare, law, finance)
- Growing emphasis on understanding how models make predictions

\begin{center}
\includegraphics[width=0.6\columnwidth]{imgs/interpretability.png}
\end{center}

---

# Explainability

- Dealing with complicated models requires explainability through post hoc explanations

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/explainability.png}
\end{center}

---

# Post Hoc Explanation Methods

- LIME
- C-LIME
- SHAP
- Occlusion
- Vanilla Gradients
- Gradient $\times$ Input
- SmoothGrad
- Integrated Gradients

---

# Different Methods, Different Explanations

- Inconsistency in their goals
- What is an explanation?
- Lack of mathematical framework resulting in misunderstanding of their goals and properties

---

# Summary of Key Contributions (Paper 2)

1. Formalize the **local function approximation (LFA)** framework
2. Demonstrate that **eight popular explanation methods** can be characterized as instances of the LFA framework
3. **No Free Lunch Theorem:** no single LFA method can perform optimally across all noise neighbourhoods
4. Provide a **guiding principle** for choosing among LFA explanation methods based on the input domain

---

# Related Work (Paper 2)

- C-LIME and SmoothGrad connections
- Gradient-based explanation methods and when they produce similar explanations
- Faithfulness to the black-box model, robustness to adversarial attack, and fairness across subgroups

---

# Local Function Approximation Framework

**Definition 1.** *Local function approximation (LFA) of a black-box model $f$ on a neighbourhood distribution $\mathcal{Z}$ around $\mathbf{x}_0$ by an interpretable model class $\mathcal{G}$ and a loss function $\ell$ is given by*

$$g^* = \underset{g \in \mathcal{G}}{\arg\min}\ \underset{\xi \sim \mathcal{Z}}{\mathbb{E}}\ \ell(f, g, \mathbf{x}_0, \xi) \tag{1}$$

*where a valid loss $\ell$ is such that $\mathbb{E}_{\xi \sim \mathcal{Z}}\ \ell(f, g, \mathbf{x}_0, \xi) = 0 \iff f(\mathbf{x}_\xi) = g(\mathbf{x}_\xi)\ \forall \xi \sim \mathcal{Z}$*

---

# Distinction with LIME

- The LFA framework requires that $f$ and $g$ share the same input domain $X$ and output domain $Y$, suggesting LIME does not fall in LFA
- LFA framework ensures model recovery if $f \in G$ and $\text{domain}(x) = X$
- Optimization is done through splitting the perturbation data into train/validation/test sets. LIME does not, making it possible to overfit a small number of perturbations

---

# Designing Explanations with LFA

LFA guides creation of explanations. LFA requires you define:

1. interpretable model class $\mathbf{G}$
2. neighbourhood distribution $\mathbf{Z}$
3. loss function $\mathbf{l}$
4. binary operator $\oplus$ to combine the input and the noise

---

# Correspondence with Explanation Methods

| Explanation Method | Local Neighbourhood $\mathcal{Z}$ around $\mathbf{x}_0$ | Loss Function $\ell$ |
|---|---|---|
| ~~C-LIME~~ | $\mathbf{x}_0 + \xi;\ \xi(\in \mathbb{R}^d) \sim \text{Normal}(0, \sigma^2)$ | Squared Error |
| SmoothGrad | $\mathbf{x}_0 + \xi;\ \xi(\in \mathbb{R}^d) \sim \text{Normal}(0, \sigma^2)$ | Gradient Matching |
| Vanilla Gradients | $\mathbf{x}_0 + \xi;\ \xi(\in \mathbb{R}^d) \sim \text{Normal}(0, \sigma^2),\ \sigma \rightarrow 0$ | Gradient Matching |
| Integrated Gradients | $\xi \mathbf{x}_0;\ \xi(\in \mathbb{R}) \sim \text{Uniform}(0, 1)$ | Gradient Matching |
| Gradients $\times$ Input | $\xi \mathbf{x}_0;\ \xi(\in \mathbb{R}) \sim \text{Uniform}(a, 1),\ a \rightarrow 1$ | Gradient Matching |
| LIME | $\mathbf{x}_0 \odot \xi;\ \xi(\in \{0,1\}^d) \sim \text{Exponential kernel}$ | Squared Error |
| KernelSHAP | $\mathbf{x}_0 \odot \xi;\ \xi(\in \{0,1\}^d) \sim \text{Shapley kernel}$ | Squared Error |
| Occlusion | $\mathbf{x}_0 \odot \xi;\ \xi(\in \{0,1\}^d) \sim \text{Random one-hot vectors}$ | Squared Error |

---

# LFA with Continuous Noises: Gradient-Based Methods

**Gradient Matching Loss:**

$$\ell_{gm}(f, g, \mathbf{x}_0, \xi) = \|\nabla_\xi f(\mathbf{x}_0 \oplus \xi) - \nabla_\xi g(\mathbf{x}_0 \oplus \xi)\|_2^2$$

---

# No Free Lunch Theorem for Explanation Methods

**Theorem 3** *(No Free Lunch for Explanation Methods). Consider explaining a black-box model $f$ around point $\mathbf{x}_0$ using an interpretable model $g$ from model class $\mathcal{G}$ and a valid loss function $\ell$ where the distance between $f$ and $\mathcal{G}$ is given by $d(f, \mathcal{G}) = \min_{g \in \mathcal{G}} \max_{\mathbf{x} \in \mathcal{X}} \ell(f, g, 0, \mathbf{x})$.*

*Then, for any explanation $g^*$ over a neighbourhood distribution $\xi_1 \sim \mathcal{Z}_1$ such that $\max_{\xi_1} \ell(f, g^*, \mathbf{x}_0, \xi_1) \leq \epsilon$, there always exists another neighbourhood $\xi_2 \sim \mathcal{Z}_2$ such that $\max_{\xi_2} \ell(f, g^*, \mathbf{x}_0, \xi_2) \geq d(f, \mathcal{G})$.*

When $g$ is less expressive than $f$, **no single explanation $g^*$ can perform optimally across all neighborhoods**

- Example: $f$ is non-linear and $g^*$ is linear

---

# Characterizing Explanation Methods via Model Recovery

**Definition 2** *(Model Recovery: Guiding Principle). Given an instance of the LFA framework with a black-box model $f$ such that $f \in \mathcal{G}$ and a specific noise type (e.g., Gaussian, Uniform), an explanation method performs model recovery if there exists some noise distribution $\mathcal{Z}$ such that LFA returns $g^* = f$.*

How can you evaluate whether an explanation $g$ works for $f$?

If $f$ and $g^*$ are the same model class, it should be possible for $g$ to approximate ("recover") $f$

---

# Characterizing Explanation Methods via Model Recovery (cont)

Let's explore which of the 8 explanation methods work for various input domains $\mathbf{X}$. Three cases:

1. continuous $\mathbf{X}$
2. binary $\mathbf{X}$
3. discrete $\mathbf{X}$

---

# 1. Which Explanation for continuous *X*? (1/2)

Assume $f$ and $g$ are linear ($f(\mathbf{x}) = \mathbf{w}_f^\top \mathbf{x}$ and $g(\mathbf{x}) = \mathbf{w}_g^\top \mathbf{x}$)

**A)** ✅ Additive continuous noise (SmoothGrad, Vanilla Gradients, C-LIME). Why? $w_g = w_f$

$$\ell(f, g, \mathbf{x}_0, \xi) = \|\nabla_\xi f(\mathbf{x}_\xi) - \nabla_\xi g(\mathbf{x}_\xi)\|_2^2$$

**B)** ❌ Multiplicative continuous noise (Integrated Gradients and Gradient $\times$ Input). Why? loss function parameterization

$$\ell(\tilde{f}, g, \mathbf{x}_0, \xi) = \|\nabla_\xi f(\mathbf{x}_\xi) - \nabla_\xi g(\xi)\|_2^2$$

---

# 1. Which Explanation for continuous *X*? (2/2)

**C)** ❌ Multiplicative binary noise (LIME, KernelSHAP, and Occlusion). Why? Consider sinusoidal example

**Remark 2.** *For $\mathcal{X} = \mathbb{R}^d$, periodic functions $f$ and $g$ where $f(\mathbf{x}) = \sum_{i=1}^d \sin(\mathbf{w}_{f_i} \odot \mathbf{x}_i)$ and $g(\mathbf{x}) = \sum_{i=1}^d \sin(\mathbf{w}_{g_i} \odot \mathbf{x}_i)$, and an integer $n$, binary noise methods do not perform model recovery for $|w_{f_i}| \geq \frac{n\pi}{\mathbf{x}_{0_i}}$.*

$\sin(\mathbf{w}_{f_i} \mathbf{x}_{0_i}) = \sin(\pm n\pi) = \sin(0) = 0$

$\sin(\mathbf{w}_{f_i} \mathbf{x}_{0_i})$ outputs zero for all binary perturbations $\rightarrow$ discrete nature of noise makes model recovery impossible

---

# 2. Which Explanation for binary *X*?

Consider binary noise methods (continuous noise invalid)

Only **Multiplicative binary perturbations methods (LIME, KernelSHAP, and Occlusion)** enable $g$ to recover $f$ in the binary domain

---

# 3. Which Explanation for discrete *X*?

- ❌ continuous noise methods invalid
- ❌ binary noise methods — same sinusoidal logic
- All 8 explanations fail
- Use LFA to design new explanation with a discrete noise type

---

# Summary of Properties of Existing Explanation Methods

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/lfa_properties_table.png}
\end{center}

- For **continuous data**: C-LIME, SmoothGrad, Vanilla Gradients perform model recovery
- For **binary data**: LIME, KernelSHAP, Occlusion perform model recovery
- Integrated Gradients and Gradient $\times$ Input: no model recovery in either domain

---

# Empirical Evaluation — Datasets & Models

1. **Common Experimental Goal:** Examine different XAI methods' explanations of models' predictions on sample datasets to validate theoretical claims

2. **Two Datasets:**
   - World Health Organization Life Expectancy dataset (20 features)
   - Home Equity Line of Credit (HELOC) dataset from FICO (24 features)

3. **4 Models:**
   - 1 Simple Model (generalized linear regression)
   - 3 Neural Network Models of varying complexity

---

# Empirical Evaluation — Experiment #1

**Goal:** Show each explanation method fits within the LFA framework by comparing the original method with a LFA re-implementation

**Methodology:**
- For each XAI method (e.g. LIME), randomly select 100 test set points
- Use the LFA and original (Meta) implementations to explain the predictions of black-box models
- Evaluate the similarity of the two implementations' explanations (L1)

**Results:**
- All 7 methods tested (excl. C-LIME) display near-zero L1 distances
- Implies each method fits within the LFA framework

---

# Empirical Evaluation — Experiment #1 Results

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/eval_exp1_results.png}
\end{center}

---

# Empirical Evaluation — Experiment #2

**Goal:** Confirm that all XAI methods within the LFA achieve "model recovery"

**Methodology:**
- Set $f$ to be the trained linear regression model on each dataset
- Generate LFA explanations ($g^*$), where model class $G$ is linear models
- Compare weights of $g^*$ with $f$

**Results:**
- All 7 models satisfy the LFA guiding principle of "model recovery"
- Weights of $g^* =$ (gradient of $f$) or (gradient of $f$) $\times$ (input) for each method

---

# Empirical Evaluation — Experiment #2 Results

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/eval_exp2_results.png}
\end{center}

---

# Empirical Evaluation — Experiment #3

**Goal:** Illustrate the LFA No Free Lunch Theorem for common XAI methods

**Methodology:**
- For each method, generate explanations for 100 random test points
- For $k = (1, 12)$, evaluate each explanation by:
  - Replace the top/bottom-$k$ features with 0 (binary perturbation)
  - Adding Gaussian noise to the top/bottom-$k$ features (continuous perturbation)
- Calculate the absolute change in model prediction after perturbation

**Results:**
- SmoothGrad & Vanilla Gradients perform less well for binary perturbations
- 5 other methods perform less well for continuous perturbations

---

# Empirical Evaluation — Experiment #3: Bottom-K Features

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/eval_exp3_results_bottomk.png}
\end{center}

---

# Empirical Evaluation — Experiment #3: Top-K Features

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/eval_exp3_results_topk.png}
\end{center}

---

# Summary of Key Contributions (Paper 2)

1. Formalized the **local function approximation (LFA)** framework
2. Demonstrated that **eight popular explanation methods** can be characterized as instances of the LFA framework
3. **No Free Lunch Theorem:** no single LFA method can perform optimally across all noise neighbourhoods
4. Provided a **guiding principle** for choosing among LFA explanation methods based on the input domain

---

# Future Work (Paper 2)

1. Extend LFA analysis to additional post-hoc explanation methods

2. Develop a similar unifying conceptual framework for the *interpretability* of different model explanations
   - This work develops a unifying framework for evaluating *faithfulness* of explanations
   - May require more than a theoretical examination
     - Human-Computer Interaction research such as user studies

---

# Discussion Questions (Paper 2)

1. Do you agree that the Local Function Approximation framework is a useful conceptual tool for understanding & comparing explanation methods?

2. If no explainability method can perform optimally across all perturbation distributions, as implied by the No Free Lunch Theorem, does that mean explainability should be defined relative to a perturbation neighborhood?
   - How does that complicate interpretability, especially for practitioners without ML expertise?

3. More broadly, what do you think about papers that attempt to create conceptual coherence & clarity across the field of explainability? Should this be a higher priority area of research?

---

\begin{center}
\Huge Thank You!
\end{center}

---

# References {.allowframebreaks}

\footnotesize
