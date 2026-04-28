---
title: "\\emoji{wtf} XAI Lecture 11"
subtitle: "Counterfactual Explanations \\& Algorithmic Recourse"
bibliography: references.bib

---

# Disclaimer

\input{../disclaimer.tex}

---

# Paper 1

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/paper1_title.png}
\end{center}

[@wachter2017counterfactual]

---

# Introduction + Motivation

**EU General Data Protection Regulation (2018)**

:::: columns
::: {.column width="48%"}

- "the toughest privacy and security law in the world"
- Article 13-14, regarding automated decision-making: "meaningful information about the logic involved"
- Recital 71: "the right to obtain an explanation of the decision reached and to challenge the decision"

:::
::: {.column width="50%"}

\begin{alertblock}{4 Key Problems}
\begin{enumerate}
\item Not legally binding
\item Only applicable in limited cases
\item Explainability is technically very challenging
\item Competing interests of data controllers, subjects, etc.
\end{enumerate}
\end{alertblock}

:::
::::

---

# Unconditional Counterfactual Explanations

**Authors propose**

- **3 aims for explanations**
  - Inform and help the subject understand "why"
  - Provide grounds to contest decisions
  - Understand options for recourse
- **CFEs**
  - Fulfill the above goals
  - Overcome challenges w.r.t. current interpretability work
  - Can bridge the gap between interests of data subjects and data controllers

\vspace{1em}
\begin{center}
\huge
\textbf{Do you buy this?}
\end{center}



---

# Unconditional Counterfactual Explanations


- **Definition:**
  - A statement of how the world would have to be different for a desirable outcome to occur
  - **Because** of features $\{x_1, x_2\}$, $x$'s outcome was label $y_1$  
  **If** $x = \{x_1 + \delta_1, x_2 + \delta_2\}$, **then** $y_2$.
- **Example:**
  - "You were denied a loan **because** your annual income was \$30000.   
  **If** your income has been \$45000, **you would have been offered a loan**"


## Notes

- No one \textbf{unique} CF
- Need to consider \textbf{actionability} (mutability of variables)
- Providing \textbf{several diverse} CFEs may be more useful than simply the closest/shortest one

---

# Background + Related Work

- Historic context of knowledge
- Prior explainability work
- Adversarial examples/perturbations
- Causality/Fairness

---

# Background: Historic Context of Knowledge

- In order to know something, it is not enough to simply **believe** that it is true: rather, you must also have a good **reason** for believing it
- If $q$ were false, $S$ would not believe $p$


## Note

- This statement only describes $S$'s \textbf{beliefs}, which might not reflect reality
- This statement can be made without knowledge of the \textbf{causal relationship} between $p$ and $q$
- Q: who is $S$? The user? The model? Us?



---

# Background: Previous Explanations in AI/ML

- **Previously:** providing insight into the internal state of an algorithm, human-understandable approximations of the algorithm

- Three-way tradeoff between:
  1. quality of approximation
  2. ease of understanding the function
  3. size of the domain for which the approximation is valid

- **CFEs:**
  - Minimal amount of information
  - Require no understanding of internal logic of model
  - No approximation (although might not always be minimum length)
  - Con: May be overly restrictive

---

# Background: Adversarial Perturbations (not the same)

* **Shared Mechanism:** Both find the minimal change ($\delta$) to flip a prediction: $f(x + \delta) = y'$.
* **The Contrast:**
    * **Adversarial:** Invisible, targets pixels, intended to **deceive**.
    * **Counterfactual:** *Sparse*, targets features, intended to **inform**.
* **The "Manifold" Requirement:**
    * Mathematical changes must be **plausible** in the real world.
    * GDPR requires explanations to be "meaningful," not just possible.
* **Key Insight:** A CFE is an adversarial attack with a **human-centric purpose**.

---

# Background: Causality and Fairness

* **Bias Detection:** CFEs act as an audit tool; they reveal if a decision is based on protected attributes (e.g., race, gender, age).
* **Counterfactual Fairness:** If the "shortest path" to a loan approval requires changing your race or gender, the model is demonstrably discriminatory.
* **Evidence of Disparate Treatment:** CFEs provide a "smoking gun" for auditors without needing to inspect the model's internal weights.
* **The Converse Question:** If a model is biased, will the CFE *always* change a protected attribute? 
    * *Warning:* Bias often hides in "proxies" (e.g., ZIP code as a proxy for race).

---

# Summary of Contributions

**Core argument:** explaining automated decisions does not require opening the black box.

| Contribution | Key point |
|---|---|
| Complexity of ML explanations | Internal logic is too complex to convey to lay users |
| Counterfactual approach | Rooted in adversarial ML; no model internals required |
| GDPR alignment | CFEs satisfy transparency goals better than local approximations |

> **Bottom line:** CFEs shift the focus from *how the model works*
> to *what would need to change* --- actionable, model-agnostic, and legally compatible.

---

# Approach: Counterfactual Optimization

\begin{center}
\large
\textbf{$$\arg\min_{x'} \max_{\lambda} \; \lambda(f_w(x') - y')^2 + d(x_i, x')$$}
\end{center}

> **In plain terms:** find the closest point to $x_i$ that flips the prediction to $y'$.

| Symbol | Meaning |
|--------|---------|
| $x'$ | Counterfactual point (what we optimize) |
| $\lambda$ | Weight balancing target vs. proximity |
| $\lambda(f_w(x') - y')^2$ | Penalizes missing the target label |
| $d(x_i, x')$ | Penalizes distance from factual point |
| $\max_\lambda$ | Forces label flip to dominate over proximity |

**Procedure:** alternate --- optimize $x'$, then increase $\lambda$ until constraint is satisfied.

---

# Approach: Distance Metrics

$$d(x, x') = \sum_{k \in F} \frac{\|x_{i,k} - x'_k\|_p}{N_k}$$

\begin{center}
\textbf{In plain terms:} sum of per-feature differences, normalized so all features are comparable.
\end{center}

| Term | Meaning |
|------|---------|
| $x_{i,k} - x'_k$ | Change in feature $k$ |
| $\|\cdot\|_p$ | $\ell_1$ (sparse changes) or $\ell_2$ (smooth changes) |
| $N_k$ | Normalizing factor --- makes features comparable |

**Two normalizing choices:**

1. $N_k = \text{MAD}_k = \text{median}_{j}\bigl(|X_{j,k} - \text{median}_l(X_{l,k})|\bigr)$
2. $\qquad N_k = \text{std}_{j}(x_{j,k})$


---

# Experimental Results: LSAT 1/3

**Setup:** predict law school admission score from $\{$GPA, LSAT, Race$\}$ using a black-box model.
\vfill 

**Goal:** 

- For each below-average student, find the *minimal change* that brings their score to $y' = 0$ (population mean).  
- *population mean*The minimum score to be considered an average candidate.


\vfill

## Key question: 
Does the choice of distance metric produce
fair, realistic, and actionable counterfactuals?

---

# Experimental Results: LSAT

:::: {.columns}
::: {.column width="55%"}
![](imgs/lsat_l2.png)
:::
::: {.column width="45%"}
- Without normalization, the optimizer freely modifies Race ($-1.0$, $0.9$), producing impossible counterfactuals.
- MAD normalization makes changing Race relatively costly, keeping it fixed across all CFEs.
- Distance metric choice is not a technical detail --- it directly determines fairness and plausibility of recommendations.
:::
::::

---

# Experimental Results: Discussion

1. **Two practical design decisions for realistic CFEs:**

| Technique | Purpose |
|-----------|---------|
| Clipping | Truncate CFE values to observed data range |
| Clamping | Force categorical variables to valid values |

2. **We need reasobales counterfactual targets:**

| Dataset | Target $y'$ | Interpretation |
|---------|-------------|----------------|
| LSAT | $0$ | Reach population average score |
| PIMA | $0.5$ | Cross from high to low diabetes risk |

> **Note:** the choice of $y'$ is not neutral --- it encodes
> a normative judgment about what counts as a "desirable" outcome.

---

# Explanations and The GDPR

**GDPR Recital 71** requires that automated decisions include:
the right to obtain an explanation and to challenge the decision.

| Requirement | CFE response |
|-------------|-------------|
| Intelligible explanation | Simple "if-then" statements |
| No black-box exposure | CFEs depend only on external facts, not model internals |
| No trade secret violation | No algorithm details disclosed |
| Individual-level insight | Tailored to each data subject's situation |

> **Bottom line:** CFEs do not require opening the black box ---
> they satisfy GDPR goals while protecting data controllers' interests.

---

# Advantages of Counterfactual Explanations

- Bypass explaining the *internal workings* of complex machine learning system
- Simple to compute and convey
- Provide information that is both easily digestible and practically useful
  - Understanding the reasons for a decision
  - Contesting decisions
  - Altering future behaviour to receive a preferred outcome

\begin{alertblock}{}
\centering Possible mechanism to meet the explicit requirements and background aims of the GDPR
\end{alertblock}


---

# Legal Information Gaps on Contesting Decisions

**The GDPR leaves critical gaps for individuals seeking to contest automated decisions:**

- **Art. 16**
  - Data subject has the right to correct inaccurate data used to make a decision, but does not need to be informed of which data the decision depended
- **Art. 22**
  - Data subjects do not need to be informed of their right *not* to be subject to an automated decision

## CFEs close these gaps: 

By revealing which features were most influential,
they give individuals the information needed to meaningfully contest a decision.

---

# Explanations to Alter Future Decisions

**The third goal of explanations:** not just to understand or contest,
but to guide the individual toward a better outcome.

| Source | Position |
|--------|----------|
| GDPR | Silent --- does not explicitly require forward-looking explanations |
| Art. 29 Working Party | Recommends suggestions on how to improve outcomes |
| CFEs | Naturally satisfy this goal --- show *what to change* and *by how much* |

> **Key advantage:** CFEs can address the impact of changing
> multiple variables simultaneously, producing realistic and actionable recourse paths.

---

# Empirical Evidence: Yacoby et al. (2020)

\begin{center}
\includegraphics[width=0.6\columnwidth]{imgs/yacoby.png}
\end{center}

**Setup:** 8 U.S. state court judges evaluated criminal risk assessments
accompanied by CFEs.

**Example CFE shown to judges:** *"If this defendant had stable employment, the system would have classified them as low risk."*

**Finding:** CFEs did not change judicial decisions because:

1. Misinterpretation: Judges see it as a claim about the defendant, not the model.
2. Irrelevance: Once understood, judges find it irrelevant to the case.

**Implication:** CFEs can be legally compliant and mathematically correct
yet fail entirely in practice due to user misinterpretation.

---

# Discussion: Limitations of CFEs (Wachter et al.)

**Who do these explanations actually serve?**

- **Developers:** debugging and model improvement
- **Data subjects:** recourse and contestation
- **Lawmakers:** accountability and compliance

**Two sources of misinterpretation:**

- **Causality:** CFEs describe model behavior, not real-world causal effects
- **Sparsity bias:** mathematically minimal changes may be unrealistic or unachievable

> **Takeaway:** CFEs tell you *where to go*, not *how to get there* ---
> this gap motivates Karimi et al.'s causal recourse framework.

---

# Paper 2

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/paper2_title.png}
\end{center}

\vfill
\footnotesize By Kamiri, Schölkopf, and Valera

[@karimi2021algorithmic]

---

# Algorithmic Recourse

\begin{columns}
\begin{column}{0.52\textwidth}

- Increasingly algorithms are used to make consequential decisions for individuals
- Recourse: "*Systematic process of reversing unfavorable decisions made by algorithms and bureaucracies*"
  - Promoting **agency** and **trust**

\end{column}
\begin{column}{0.45\textwidth}

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/loan_approval.png}
\end{center}

\end{column}
\end{columns}

---

# Paper's Main Contributions

1. **Insufficiencies of previous problem formulations**
   - $\rightarrow$ Motivates causal approach to recourse
2. **Structural Causal Model approach to recourse**
3. **Discuss examples motivated by real-world problems and future directions**

---

# Nearest Counterfactual Explanations

\begin{columns}
\begin{column}{0.48\textwidth}

- For a person with features $\mathbf{x}^F$ who was denied a loan, find the "nearest neighbor" $\mathbf{x}$ who was granted a loan
- Difference between $\mathbf{x}^F$ and $\mathbf{x}$ is an "explanation" for the loan denial for $\mathbf{x}^F$

\end{column}
\begin{column}{0.48\textwidth}

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/nearest_cfe.png}
\end{center}

\end{column}
\end{columns}

---

# Nearest Counterfactual Explanation (CFE)

$$\mathbf{x}^{*\text{CFE}} \in \underset{\mathbf{x}}{\arg\min} \; \text{dist}(\mathbf{x}, \mathbf{x}^F) \quad \text{s.t.} \quad h(\mathbf{x}) \neq h(\mathbf{x}^F),\; \mathbf{x} \in \mathcal{P}$$

- **Finding nearest counterfactual explanation as an optimization problem**
  - $\mathbf{x}^{*\text{CFE}}$ is the Counter Factual Explanation
  - Function $h$ is the classifier
- **Distance metrics**
  - Lp norm; L1 norm divided by median absolute deviation; etc.

---

# Why Are CFEs Not Ideal for Recourse?

\begin{center}
\Large Counterfactual Explanations provide \textbf{understanding} but do not necessarily lead to optimal \textbf{action recommendations}
\end{center}

---

# Why Are CFEs Not Ideal for Recourse?

1. Don't account for person's difficulty or "cost" of changing dimensions of $\mathbf{x}^F$ (addressed by Ustun et al.)

2. Don't account for downstream "causal" impact of taking actions (addressed by this work)

---

# Accounting for the "Cost" of Actions (Ustun et al.)

$$\delta^* \in \underset{\delta}{\arg\min} \; \text{cost}(\delta; \mathbf{x}^F) \quad \text{s.t.} \quad h(\mathbf{x}^{\text{CFE}}) \neq h(\mathbf{x}^F),$$
$$\mathbf{x}^{\text{CFE}} = \mathbf{x}^F + \delta, \quad \mathbf{x}^{\text{CFE}} \in \mathcal{P}, \quad \delta \in \mathcal{F}$$

- $\delta^*$ restricted to the set of "feasible changes"
- Consider linear impact of changes $\delta$
- Non-trivial to choose costs that reflect people's true objective functions

[@ustun2019actionable]

---

# Insufficiencies of Ustun et al. Formulation

$$\delta^* \in \underset{\delta}{\arg\min} \; \text{cost}(\delta; \mathbf{x}^F) \quad \text{s.t.} \quad h(\mathbf{x}^{\text{CFE}}) \neq h(\mathbf{x}^F)$$

1. **Marginal cost of changing a feature is constant**
   - **Example:** Cost of going from salary \$0 to \$100k equals cost to go from salary \$800k to \$900k

2. **Doesn't consider downstream "causal" impact of actions**
   - **Example:** Loan decision for individual changed if "salary" reaches 100k (+33\%) or "bank balance" reaches 30k (+20\%). 20\% change seems easier.
   - However, best **action recommendation** is to increase salary by 14\% when 30\% of salary automatically saved to bank.

---

# Actions as Interventions: Structural Causal Model (SCM)

\begin{columns}
\begin{column}{0.48\textwidth}

**Setup**

- $M$ ($M \in \Pi$) = $\langle F, X, U \rangle$: SCM
- $X$: endogenous (observed) variables
- $U$: exogenous (unobserved) variables
- $F$: $U \rightarrow X$, structural equations
- $A$ ($\Pi \rightarrow \Pi$): structural interventions, i.e. transformations between SCMs
  - of the form $A := \text{do}(\{X_i := a_i\}_{i \in I})$

\end{column}
\begin{column}{0.48\textwidth}

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/scm_diagram.png}
\end{center}

- $M$: true world model
- observation: $M_1 \neq M_2 \neq M_3$

\end{column}
\end{columns}

---

# Actions as Interventions: Structural Counterfactuals

\begin{center}
\textit{What will individual $x^F$'s feature vector be after the individual performs action set $A$ in world $M$?}
\end{center}

\vspace{0.5cm}

**Assumptions:** (1) no hidden confounders (true SCM), (2) full access to invertible $F$

**Idea:** once we know $F$, $X$ (endogenous variables) can be uniquely determined given $U$ (exogenous variables)

Compute $F^{-1}(x^F)$

\begin{block}{}
\centering Takeaway: we can compute any structural counterfactual query for individual $x^F$:

$$x^{\text{SCF}} = F_A(F^{-1}(x^F))$$
\end{block}

---

# Limitations of CFE-Based Recourse: Formalism

**Setup:** $x^F$ (individual features), $\delta^*$ action recommendation (Ustun et al. solution),
$I$ (set of indices of acted-upon observed variables: $I = \{i \mid \delta^*_i \neq 0\}$)

\vspace{0.5cm}

**Definition** (CFE-Based Actions): a set of structural interventions $A^{\text{CFE}} := \text{do}(\{X_i := x^F_i + \delta^*\}_{i \in I})$

**Proposition:** $A^{\text{CFE}} \rightarrow x^{\text{SCF}} = x^{*\text{CFE}} := x^F + \delta^*$ (i.e. recourse is guaranteed) **if and only if** $I$'s descendants $= \{\}$.

**Corollary:** if the true world $M$ is independent—if all the observed features are root-nodes of $G$—then CFE-based actions always guarantee recourse.

---

# Algorithmic Recourse via Minimal Interventions: Setup

\begin{columns}
\begin{column}{0.48\textwidth}

\begin{block}{Formulation}
$$A^* \in \underset{A}{\arg\min} \; \text{cost}(A; \mathbf{x}^F)$$
$$\text{s.t.} \quad h(\mathbf{x}^{\text{SCF}}) \neq h(\mathbf{x}^F)$$
$$\mathbf{x}^{\text{SCF}} = \mathbb{F}_A(\mathbb{F}^{-1}(\mathbf{x}^F))$$
$$\mathbf{x}^{\text{SCF}} \in \mathcal{P}, \quad A \in \mathcal{F}$$
\end{block}

\end{column}
\begin{column}{0.48\textwidth}

**Remarks**

- ~~finding minimal shift of features~~ $\rightarrow$ finding minimal cost action set that yields favorable label
- $A^* \in \mathcal{F}$ = set of feasible actions with minimally costly recourse
- $\text{cost}(\square; x^F)$: $\mathcal{F} \times X \rightarrow \mathbb{R}_+$
- $\square^{\text{SCF}} \neq \square^{\text{CFE}}$ (from Ustun et al.)!

\end{column}
\end{columns}

---

# Algorithmic Recourse via Minimal Interventions: Formalism

$$A^* \in \underset{A}{\arg\min} \; \text{cost}(A; x^F) \quad \text{s.t.} \quad h(x^{\text{SCF}}) \neq h(x^F), \quad x^{\text{SCF}} = F_A(F^{-1}(x^F)), \quad x^{\text{SCF}} \in \mathcal{P}, \quad A \in \mathcal{F}$$

\begin{alertblock}{Proposition}
- $A^{\text{CFE}}$: Counter Factual Explanation-based action
- $A^*$: Minimal Intervention Solution

$$\text{cost}(A^*; x^F) \leq \text{cost}(A^{\text{CFE}}; x^F)$$
\end{alertblock}

---

# Algorithmic Recourse via Minimal Interventions: MINT

- **Recourse through Minimal Interventions (MINT) idea:**
  - Required: that we can compute structural counterfactual of an individual in the world given *any* feasible action
  - Focus on the case where the SCM is an additive noise model
  - $\Rightarrow$ Abduction-action-prediction technique (Pearl et al.) to compute $x^{\text{SCF}}$: $F_A(F^{-1}(x^F))$

---

# Abduction-Action-Prediction to Obtain $x^\text{SCF}$

\begin{columns}
\begin{column}{0.45\textwidth}

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/abduction_diagram.png}
\end{center}

$\{U_i\}^4_{i=1}$: mutually independent, exogenous

$\{f_i\}^4_{i=1}$: structural equations

$x = [x_1^F, x_2^F, x_3^F, x_4^F]^T$: observed factual features

\end{column}
\begin{column}{0.52\textwidth}

1. **Abduction:** compute exogenous variables
   - $u_1 = x_1^F$, $u_2 = x_2^F$, $u_3 = x_3^F - f_3(x_1^F, x_2^F)$, $u_4 = x_4^F - f_4(x_3^F)$

2. **Action:** modify SCM with interventions
   - $X_1 := [1 \in I] \cdot a_1 + [1 \notin I] \cdot U_1$
   - $X_2 := [2 \in I] \cdot a_2 + [2 \notin I] \cdot U_2$

3. **Prediction:** recursively compute endogenous variables
   - $x_1^{\text{SCF}} := [1 \in I] \cdot a_1 + [1 \notin I] \cdot u_1$
   - $x_3^{\text{SCF}} := [3 \in I] \cdot a_3 + [3 \notin I] \cdot (f_3(x_1^{\text{SCF}}, x_2^{\text{SCF}}) + u_3)$

\end{column}
\end{columns}

---

# General Formulation and Solving the Optimization Problem

\begin{columns}
\begin{column}{0.50\textwidth}

\begin{block}{General Formulation}
$$A^* \in \underset{A}{\arg\min} \; \text{cost}(A; \mathbf{x}^F)$$
$$\text{s.t.} \quad h(\mathbf{x}^{\text{SCF}}) \neq h(\mathbf{x}^F)$$
$$x_i^{\text{SCF}} = [i \in I] \cdot (x_i^F + \delta_i)$$
$$+ [i \notin I] \cdot (x_i^F + f_i(\mathbf{pa}_i^{\text{SCF}}) - f_i(\mathbf{pa}_i^F))$$
$$\mathbf{x}^{\text{SCF}} \in \mathcal{P}, \quad A \in \mathcal{F}$$
\end{block}

\end{column}
\begin{column}{0.47\textwidth}

**Remarks**

- $x_i^F + \delta_i$: intervention
- $f_i(\mathbf{pa}_i^F)$: factual values of $x_i$'s parents
- $f_i(\mathbf{pa}_i^{\text{SCF}})$: counterfactual values of $x_i$'s parents
- new closed-form expression for $F_{A^*}(F^{-1}(x^F))$ $\rightarrow$ use optimization methods

\end{column}
\end{columns}

---

# Experimental Setup

\begin{columns}
\begin{column}{0.48\textwidth}

\begin{center}
\textbf{Synthetic setting:}

Generate data following causal generative process
\end{center}

\end{column}
\begin{column}{0.48\textwidth}

\begin{center}
\textbf{Real-world setting:}

Use existing German credit dataset to learn structural causal model equations, by fitting a linear regression
\end{center}

\end{column}
\end{columns}

\vspace{0.5cm}
\begin{center}
Cost for both is $\ell_1$ norm over normalized feature change
\end{center}

---

# Experimental Setup: Synthetic Setting

\begin{columns}
\begin{column}{0.45\textwidth}

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/synthetic_scm.png}
\end{center}

\footnotesize \textbf{Causal Generative Process}

\end{column}
\begin{column}{0.52\textwidth}

$U_1 \sim \$10000 \cdot \text{Poisson}(10)$, $U_2 \sim \$2500 \cdot N(0,1)$

$$X_1 := U_1$$
$$X_2 := f_2(X_1) + U_2, \quad X_2 := \frac{3}{10} \cdot X_1 + U_2$$
$$\hat{Y} = h(X_1, X_2), \quad h = \text{sgn}(X_1 + 5 \cdot X_2 - \$225000)$$

\end{column}
\end{columns}

---

# Experimental Results: Synthetic Setting

\begin{center}
\small [annual salary, bank balance]
\end{center}

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/synthetic_results1.png}
\end{center}

---

# Experimental Results: Synthetic Setting (cont.)

\begin{center}
\includegraphics[width=0.55\columnwidth]{imgs/synthetic_results2.png}
\end{center}

\begin{columns}
\begin{column}{0.48\textwidth}
$\mathbf{x}^{*\text{SCF}}$ further dist from $\mathbf{x}^F$ than $\mathbf{x}^{*\text{CFE}}$
\end{column}
\begin{column}{0.48\textwidth}
\textbf{BUT}

$\text{cost}(\delta^*; x^F) \approx 2\, \text{cost}(A^*; x^F)$
\end{column}
\end{columns}

---

# Experimental Setup: Real-World Setting

\begin{columns}
\begin{column}{0.45\textwidth}

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/realworld_scm.png}
\end{center}

\footnotesize \textbf{Structural Causal Model}

\end{column}
\begin{column}{0.52\textwidth}

$$X_1 := U_1, \quad X_2 := U_2$$
$$X_3 := f_3(X_1, X_2) + U_3$$
$$X_4 := f_4(X_3) + U_4$$
$$\hat{Y} = h(\{X_i\}^4_{i=1})$$

\footnotesize $h$ can be logistic regression or decision tree

\end{column}
\end{columns}

---

# Experimental Results: Real-World Setting

\begin{center}
\small [gender, age, credit given, credit repayment duration]
\end{center}

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/realworld_results1.png}
\end{center}

---

# Experimental Results: Real-World Setting (cont.)

\begin{center}
\includegraphics[width=0.55\columnwidth]{imgs/realworld_results2.png}
\end{center}

\begin{center}
\textbf{42\% decrease in cost} using Karimi et al.'s formulation

Averaged over 50 test individuals, $39 \pm 24\%$ and $65 \pm 8\%$ decrease in cost, for $h$ as logistic regression and decision tree, respectively
\end{center}

---

# Future Work: Extended Kinds of Interventions

\begin{columns}
\begin{column}{0.45\textwidth}

**Forms**

- **Structural/hard** (actions in Karimi et al.): unconditionally sever all edges incident on intervened node
- **Additive/soft:** do not sever incident edges

$$x_i^{\text{SCF}} = [i \in I] \cdot \delta_i + (x_i^F + f_i(\mathbf{pa}_i^{\text{SCF}}) - f_i(\mathbf{pa}_i^F))$$

**Scopes**

- Karimi et al. assumes action = intervention on endogenous variable
- **Fat-hand/non-atomic:** confounded/correlated interventions

\end{column}
\begin{column}{0.52\textwidth}

**Feasibility**

Can encode as constraints to amend to $A \in \mathcal{F}$

- **Immutable:** closed under ancestral relationships
- **Mutable but non-actionable:** $[i \notin I] = 1$ is sufficient
- **Actionable and mutable:** contingent on (a) pre-intervention value of variable (b) pre-intervention value of other variables (c) post-intervention value of variable (d) post-intervention value of other variables

\end{column}
\end{columns}

---

# Future Work: Current Limitations

\begin{center}
\includegraphics[width=0.7\columnwidth]{imgs/limitations.png}
\end{center}

- **Reliance on true causal model of the world**
  - True for any approach suggesting actions to be performed in the real world
  - Study potential inefficiencies from partial/imperfect causal model

---

# Concluding Thoughts

- Overall an interesting work bridging counterfactual explanations (previous papers) and algorithmic recourse (next papers), clarifying their differences
- Tradeoff between generalizability of setting and hardness of optimization problem
  - Ustun et al. pursue algorithmic recourse in a specific linear setting
  - Karimi et al. pursue algorithmic recourse in general settings, require true causal model of world
  - Open question: where do we stand on this tradeoff? Consider the origins of counterfactual explanations in Wachter et al.

---

\begin{center}
\Huge Thank You!
\end{center}

---

# References {.allowframebreaks}

\footnotesize
