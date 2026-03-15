---
title: "\\emoji{wtf} XAI Lecture 12"
subtitle: "Robust \\& Probabilistically Robust Algorithmic Recourse"
bibliography: references.bib

---

# Disclaimer

\input{../disclaimer.tex}

---

# Paper 1

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/paper1_title.png}
\end{center}

\vfill
\footnotesize Sohini Upadhyay, Shalmali Joshi, Himabindu Lakkaraju

[@upadhyay2021robust]

---

# Motivation

\begin{columns}
\begin{column}{0.48\textwidth}

**Algorithmic Recourse**

- ML models are deployed in high stakes scenarios
- If you receive an unfavorable outcome as a result of a prediction, how can you reverse it?
- Ex: A bank might tell you to increase your salary by \$10,000

\end{column}
\begin{column}{0.48\textwidth}

**Model Updates**

- In practice, data collectors are (hopefully) frequently updating their datasets
- Models are updated to reflect dataset changes
- Current algorithms to generate counterfactuals **assume models are static**

\end{column}
\end{columns}

---

# Motivation: An Example

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/motivation_example.png}
\end{center}

\begin{alertblock}{}
Original suggested recourse for the datapoint no longer crosses the decision boundary when the model is updated/retrained
\end{alertblock}

---

# Summary of Contributions

- **Outline model + data shifts** that people should consider
  - Temporal shift
  - Geospatial shift
  - Data correction shift
- **Propose ROAR** — RObust Algorithmic Recourse
  - Introduces a novel minimax objective that can be used to construct robust actionable recourses while minimizing the recourse costs
- **Theoretical analysis**
  - How bad are regular counterfactuals under model shifts?
  - How much does the proposed method increase the cost of recourses when compared to normal CFs?
- **Experimental analysis**

---

# Related Work

\begin{columns}
\begin{column}{0.52\textwidth}

**Algorithmic recourse**

- "Can I still trust you?": Understanding the impact of model updates on recourse from different kinds of dataset shifts

\begin{center}
\includegraphics[width=0.7\columnwidth]{imgs/adversarial_pig.png}
\end{center}

\end{column}
\begin{column}{0.45\textwidth}

**Adversarial Training**

- Optimizes a **minimax objective** that captures the worst-case loss over a given set of perturbations to the input data
- At each gradient step, **computes the gradient at worst-case perturbation**
- Recent work explores robust feature attribution and rule-based explanations robust to *dataset* shifts

\end{column}
\end{columns}

---

# Background: Recourse/Counterfactuals

\begin{columns}
\begin{column}{0.52\textwidth}

**Optimal CF:**

$$x' = \underset{x' \in \mathcal{A}}{\arg\min}\; c(x, x') \quad \text{s.t.} \quad \mathcal{M}(x') = 1$$

**Unconstrained and differentiable relaxation:**

$$x' = \underset{x' \in \mathcal{A}}{\arg\min}\; \ell(\mathcal{M}(x'), 1) + \lambda\, c(x, x')$$

\end{column}
\begin{column}{0.45\textwidth}

\begin{block}{Notation Notes}
- $x$: specific data point
- $x'$: counterfactual
- $\mathcal{M}$: model (or linear approximation of model around point $x$)
- $C$: cost function (how hard is it to achieve the counterfactual)
- $\mathcal{A}$: actionable/possible counterfactuals
\end{block}

\end{column}
\end{columns}

---

# A Primer: Comparing Models Under Shifts

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/primer_models.png}
\end{center}

\begin{exampleblock}{}
\centering How to compare these models? (especially if they are nonlinear and high-dimensional)
\end{exampleblock}

---

# Approach (Intuition)

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/approach_intuition.png}
\end{center}

- **Adversarial Training:** perturb inputs slightly (maximize training loss) $\rightarrow$ gradient descent step on perturbed inputs (minimize training loss)
- **ROAR:** perturb model slightly (maximize recourse loss) $\rightarrow$ gradient descent step on perturbed model (minimize recourse loss)

---

# Approach (Intuition): Diagram

\begin{center}
\includegraphics[width=0.7\columnwidth]{imgs/approach_diagram.png}
\end{center}

\begin{center}
The goal: find $x''$ that remains valid under all model perturbations $\delta \in \Delta$
\end{center}

---

# Approach (Details)

$$x'' = \underset{x'' \in \mathcal{A}}{\arg\min} \; \underset{\delta \in \Delta}{\max} \; \ell(f_{w+\delta}(x''), 1) + \lambda\, c(x, x'')$$

\begin{columns}
\begin{column}{0.52\textwidth}

\begin{block}{Algorithm 1: Optimization Procedure}
\footnotesize
\textbf{Input:} $x$ s.t. $f_w(x) = 0$, $f_w$, $\lambda > 0$, $\Delta$, learning rate $\alpha > 0$.

\textbf{Initialize} $x'' = x$, $g = 0$

\textbf{repeat}

\quad $\hat{\delta} = \arg\max_{\delta \in \Delta} \ell(f_{w+\delta}(x''), 1)$

\quad $g = \nabla[\ell(f_{w+\hat{\delta}}(x''), 1) + \lambda c(x'', x)]$

\quad $x'' -= \alpha g$

\textbf{until} convergence; \textbf{Return} $x''$
\end{block}

\end{column}
\begin{column}{0.45\textwidth}

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/approach_details_diagram.png}
\end{center}

\end{column}
\end{columns}

---

# Proofs: Theorem 1

\begin{columns}
\begin{column}{0.48\textwidth}

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/theorem1_diagram.png}
\end{center}

\end{column}
\begin{column}{0.48\textwidth}

$\Omega = \{x' : w^T x' > 0 \cap (w+\delta)^T x' \leq 0\}$

... integrating over $\Omega$

$$P(x' \text{ is invalidated}) \geq$$
$$\frac{1}{2}\sqrt{\frac{2e}{\pi}} \frac{\sqrt{\beta-1}}{\beta} \exp\left(-\beta \frac{(w^T\mu)^2}{2\|\sqrt{D}Uw\|^2}\right)$$

\textbf{Assumptions:} $x \sim \mathcal{N}(\mu, \Sigma)$, $x' \sim \mathcal{N}(\mu, \Sigma)$, $\Sigma = UDU^T$, $\beta \geq 1$

\end{column}
\end{columns}

---

# Proofs: Theorem 2

\begin{columns}
\begin{column}{0.48\textwidth}

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/theorem2_diagram.png}
\end{center}

\end{column}
\begin{column}{0.48\textwidth}

w.h.p. $(1 - \eta')$:

$$c(x'', x) \leq c(x', x) +$$
$$\frac{1}{\lambda\|w+\delta\|}\alpha(w+\delta)^T\mu + \sqrt{\frac{D^2}{2}\log\frac{1}{\eta'}}$$

\textbf{Assumptions:}
- Log-loss + simple model
- Optimal solution for $x''$
- $D$ is a bound for the "diameter" of dataset (l2)

\end{column}
\end{columns}

---

# Experimental Results

\begin{columns}
\begin{column}{0.48\textwidth}

**Real World Datasets**
- German Credit → Data Correction Shift
- Small Business Administration → Temporal Shifts
- Portuguese Student Performance → Geospatial Shift

**Synthetic Datasets**
- 2 Gaussians: Mean Shift, Variance Shift, Mean \& Variance Shift

\end{column}
\begin{column}{0.48\textwidth}

**Models:** LR, SVM, 3 Layer Deep NN

**Cost Functions:**
- L1
- Pairwise Feature Comparison (PFC): Bradley Terry Comparison to parametrize $p(i,j)$ = probability that feature $i$ is less actionable than feature $j$

**Metrics:**
- **Cost:** How close is our counterfactual?
- **Validity:** When undertaking recourse (after a model shift) does it actually work?

\end{column}
\end{columns}

---

# Experimental Results: Logistic Regression

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/results_lr.png}
\end{center}

\footnotesize
$$\arg\min_{x'' \in \mathcal{A}} \max_{\delta \in \Delta} \ell(\mathcal{M}_\delta(x''), 1) + \lambda c(x, x'') \qquad \arg\min_{x'} \max_{\lambda} \lambda(f_w(x')-y')^2 + d(x_i, x')$$

---

# Experimental Results: Deep NN

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/results_nn.png}
\end{center}

---

# Takeaways

- Cost increases with robust recourse in general
  - The authors bound this!
- Linear approximations to complex models harms $\mathcal{M}_1$ validity
  - Robustness can actually help!
- We can optimize for $\mathcal{M}_1$ validity by making our loss function more complex:

$$\arg\min_{x''} \max_{\delta} \max_{\lambda} \; \lambda\ell(M(x''), 1) + c(x, x'')$$

---

# Experimental Results: Shift and Validity

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/shift_validity.png}
\end{center}

---

# Conclusions (Paper 1)

- Novel minimax objective and optimization strategy
- Bounds on error for non-robust counterfactuals under data shifts
- Bounds on cost of robust optimization
- Empirical results in both real world and synthetic scenarios validating method

---

# Questions/Discussion

1. Do you think this problem should be worked on more from the CS/ML side or more from the policy side?
2. Do you think other types of explanations (that are not recourse motivated) need to be similarly robust?
3. What happens if model architecture/training dynamics change?
4. What incentive is there for companies/data controllers to implement this?

---

# Paper 2

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/paper2_title.png}
\end{center}

\vfill
\footnotesize Martin Pawelczyk, Teresa Datta, Johannes van-den-Heuvel, Gjergji Kasneci, Himabindu Lakkaraju (2022)

[@pawelczyk2022probabilistically]

---

# Motivation (Paper 2)

- Algorithmic recourse aims to provide users with actionable changes to move from a negative to a positive prediction in a ML model
- Typically, the minimum cost change is computed
- In the real-world, these changes are often **implemented noisily**
  - E.g. an individual who was asked to increase their salary by \$500 may get a promotion which comes with a raise of \$505 or even \$499.95
  - Or, changing certain factors may cause others to change

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/motivation_robustness.png}
\end{center}

---

# Related Work (Paper 2)

- **Counterfactual Explanations and Recourse**
  - A plethora of papers including Wachter et al. (2018) [@wachter2017counterfactual]
  - Summarised in Verma et al. (2020) [@verma2020counterfactual]:
    - Type of the underlying predictive model
    - Whether they encourage sparsity in counterfactuals
    - Whether counterfactuals should lie on the data manifold
    - Whether causal relationships should be accounted for
- **Robustness to model/data shift:**
  - ROAR — Robust Algorithmic Recourse, Upadhyay et al. (2021) [@upadhyay2021robust]
- **Robustness to input perturbations:**
  - Causal Algorithmic Recourse, Dominguez-Olmedo et al. (2022) [@dominguez2022adversarial]
- All approaches generate recourses **assuming that prescribed recourses will be correctly implemented** by users

---

# Solution: PROBE

\begin{columns}
\begin{column}{0.48\textwidth}

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/probe_diagram.png}
\end{center}

\end{column}
\begin{column}{0.48\textwidth}

- **PROBE** — Probabilistically Robust Recourse
- Allows users to manage the **recourse cost vs. robustness tradeoffs**
- Users can choose the **recourse invalidation rate**
  - Probability with which a recourse could get invalidated
- PROBE recourses are, compared to baselines:
  - Less costly than previous methods
  - More robust to noisy implementations
  - Able to provide recourses at various invalidation rates

\end{column}
\end{columns}

---

# Notation

\begin{columns}
\begin{column}{0.48\textwidth}

$\mathbf{x} \in \mathcal{X} \subseteq \mathbb{R}^d$ \quad input space

$\mathcal{Y} = \{0, 1\}$ \quad output space
- 0: unfavourable outcome
- 1: favourable outcome

$h : \mathcal{X} \rightarrow \mathcal{Y}$ \quad classifier

$h(\mathbf{x}) = g(f(\mathbf{x}))$

\end{column}
\begin{column}{0.48\textwidth}

$f : \mathcal{X} \rightarrow \mathbb{R}$ \quad inputs $\rightarrow$ logits

$g : \mathbb{R} \rightarrow \mathcal{Y}$ \quad logits $\rightarrow$ binary labels

\end{column}
\end{columns}

---

# General Formulation of Algorithmic Recourse

$$\check{\mathbf{x}} = \underset{\mathbf{x}' \in \mathcal{A}}{\arg\min} \; \underbrace{\ell(h(\mathbf{x}'), 1)}_{\text{make CF have favourable outcome}} + \lambda \cdot \underbrace{d_c(\mathbf{x}, \mathbf{x}')}_{\text{low cost}}$$

- Accounts for CF having favourable outcome and low cost
- **Does not account** for potential noise in the implemented counterfactual
  - Addressed by this paper

---

# Recourse Invalidation Rate

$$\Delta(\check{\mathbf{x}}_E) = \mathbb{E}_{\varepsilon}\Big[\underbrace{h(\check{\mathbf{x}}_E)}_{\text{CF class}} - \underbrace{h(\check{\mathbf{x}}_E + \varepsilon)}_{\text{class after response}}\Big]$$

where $\varepsilon \sim p_\varepsilon$ $\rightarrow$ probability distribution that captures noise in response

e.g. $\varepsilon \sim \mathcal{N}(\mathbf{0}, \sigma^2 \mathbf{I})$

---

# Recourse Invalidation Rate Aware Objective

$$\mathcal{L} = \underbrace{R(\mathbf{x}'; r, \sigma^2\mathbf{I})}_{\substack{\text{make IR of CF close} \\ \text{to target IR (new term)}}} + \underbrace{\ell(f(\mathbf{x}'), s)}_{\substack{\text{make CF have} \\ \text{favourable outcome}}} + \underbrace{\lambda d_c(\mathbf{x}', \mathbf{x})}_{\text{low cost}}$$

where $R(\mathbf{x}'; r, \sigma^2\mathbf{I}) = \max(0, \underbrace{\Delta(\mathbf{x}'; \sigma^2\mathbf{I})}_{\text{CF's IR}} - \underbrace{r}_{\text{target IR}})$

---

# Approximation of Recourse Invalidation Rate (Theorem 1)

**Problem:** $\Delta(\mathbf{x}')$ is not differentiable (used in objective function)

**Solution:** use a first order approximation of $\Delta(\mathbf{x}')$

$$\tilde{\Delta}(\check{\mathbf{x}}_E; \sigma^2\mathbf{I}) = 1 - \Phi\!\left(\frac{f(\check{\mathbf{x}}_E)}{\sqrt{\nabla f(\check{\mathbf{x}}_E)^\top \sigma^2\mathbf{I}\, \nabla f(\check{\mathbf{x}}_E)}}\right)$$

where $\check{x}_E$: counterfactual, $f(\check{x}_E)$: logit at counterfactual

**Proof sketch:**
1. Solve $\mathbb{P}(f(\check{x}_E + \varepsilon) > 0)$
2. Use first order Taylor series to approximate logit
3. Calculate probability that normal r.v. is less than a value $\rightarrow$ CDF

---

# Theorem 1: Further Analyses

- **Proposition 1** — Wachter et al. (2018) method for logistic regression
  - Derive closed form solution for IR of CF
  - Show how to make CF more robust
- **Proposition 2** — PROBE recourse incurs an additional cost (linear regression)
- **Proposition 3** — Upperbound on IR

---

# Experimental Evaluation: Datasets

- **Adult Dataset:** Predict whether an individual has an income greater than 50,000 USD/year
- **Give Me Some Credit:** Predict whether an individual will experience financial distress within the next two years or not
- **COMPAS:** Predict if criminal is high or low risk of re-offending

---

# Experimental Evaluations: Baselines

**Baseline Methods**
- **Growing Spheres (GS):** Random search algorithm — generate observations until decision boundary is crossed then move greedily toward decision boundary
- **AR (-LIME):** Actionable Recourse in Linear Models → use integer programming
- **DICE:** Diverse Counterfactual Explanations — promote diversity of counterfactual explanations
- **Gradient:** General formulation of algorithmic recourse

**Adversarial Minmax Objectives Methods**
- **ROAR:** Recourse robust to model changes by generating CFs that minimize worst-case loss over plausible model shifts
- **ARAR:** Adversarial Robustness of Causal Algorithmic Recourse — recourse robust to features of individual

---

# Experimental Evaluation: Measures Used

- **Average Cost (AC):** Average cost for all prescribed recourses for the test set (implemented as l1-norm)
- **Recourse Accuracy (RA):** For all prescribed recourses what fraction results in the desired prediction
- **Average IR (AIR):** Average recourse invalidation rate for all prescribed recourses in test set

---

# Experimental Evaluation: Results

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/probe_results_table.png}
\end{center}

---

# Experimental Evaluation: Results (Cost vs. IR)

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/probe_results_plot.png}
\end{center}

---

# Conclusions \& Future Work (Paper 2)

- First work to navigate tradeoff between recourse cost and robustness, give control to the user
- Experimental evidence demonstrates usefulness of framework and the existence of tradeoff
- Future work: generate recourse that is simultaneously robust to noise in inputs and shifts in model parameters

---

# Discussions/Limitations

- "Generate recourse that is simultaneously robust to noise in inputs and shifts in model parameters"
  - Is there not a tradeoff still? Would the user have to provide different robustness thresholds for the different aspects the method is robust with respect to? Or is there one threshold to rule them all?
- Would users be okay with this risk of defining $r\%$ invalidation? Bias? How does recourse relate to bias?
- In general this idea of cost being described as l1 distance across methods seems to be a major limitation. Not all features incur similar contributions to cost (i.e. getting a degree versus putting more money into your savings account, one is harder than the other). Cost is a difficult concept to quantify.

---

\begin{center}
\Huge Thank You!
\end{center}

---

# References {.allowframebreaks}

\footnotesize
