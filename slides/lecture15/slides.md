---
title: "\\emoji{wtf} XAI: Quantifying Data Value and Influence in Machine Learning"
bibliography: references.bib
---

# Disclaimer

\input{../disclaimer.tex}

---

\begin{center}
\Large\textbf{Quantifying Data Value and Influence in Machine Learning}
\end{center}

\vspace{1em}

\begin{center}
Combining insights from:\\
\textit{What is Your Data Worth? Equitable Valuation of Data} (Ghorbani \& Zou, ICML 2019)\\
\textit{Understanding black-box predictions via influence functions} (Koh \& Liang, ICML 2017)
\end{center}

---

# Ingredients of Data Value

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/ingredients.png}
\end{center}

- How can we **split** the $0.8$ Performance Value into the Train Data?

---

# Ingredients of Data Value

\begin{center}
\includegraphics[width=0.7\columnwidth]{imgs/ingredients2.png}
\end{center}

---

# The Data Valuation & Influence Problem

We need a principled way to measure its value and its effect on our models. 

Stakeholders have different priorities:

* **ML Engineers:** Assess heterogeneous sources, debug model behavior, ensure data quality, curate mislabeled data, etc.
* **Data Vendors:** Determine fair pricing for buying and selling data.
* **Individuals/Data Producers:** Understand compensation or credit for contributed data.
* **Regulators & Auditors:** Ensure compliance, fairness, and accountability in data usage.
* **Researchers:** Benchmark datasets, study data efficiency, and advance reproducibility.

---

# The Baseline: Leave One Out Method

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/db1.png}
\end{center}

---

# The Baseline: Leave One Out Method

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/db2.png}
\end{center}

---

# The Baseline: Leave One Out Method

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/db3.png}
\end{center}

---

# The Baseline: Leave One Out Method

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/db4.png}
\end{center}

---

# The Baseline: Leave One Out Method

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/db5.png}
\end{center}

---

# The Baseline: Leave One Out Method

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/db6.png}
\end{center}

---

# The Baseline: Leave One Out Method

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/db7.png}
\end{center}

---

# The Baseline: Leave One Out Method

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/db8.png}
\end{center}

---

# The Bottleneck

Leave-One-Out (LOO) is conceptually simple but practically flawed:

1. **Computationally intractable:** Retraining the model for every single data point is impossible for large datasets.

2. **Ignores interactions:** It doesn't account for how data points interact with one another in subsets.

Two frameworks address these issues: **Data Shapley** and **Influence Functions**.

---

\begin{center}
\Large\textbf{Approach 1: Data Shapley}
\end{center}

\vspace{1em}

\begin{center}
Equitable Valuation of Data
\end{center}

[@ghorbani2019data]


---

# Desirable Properties of Valuation

A fair valuation method must satisfy three fundamental axioms from cooperative game theory:

1.  **Null Element:** If adding a point to *any* subset of training data never changes the model's performance, its value is exactly 0.
2.  **Symmetry:** If adding point $A$ or point $B$ to any subset always results in the exact same performance change, they must receive the same value ($Value(A) = Value(B)$).
3.  **Linearity:** If the performance metric is a sum of performances on individual tasks, the data value must reflect the sum of values for those individual tasks. Add or remove a task should add or remove value for that task.

These are the Shapley axioms.

---

# The Data Shapley Value

The only data value mathematically guaranteed to satisfy these three properties is based on marginal contributions across all possible subset sizes.

$$Value(data~k) = \sum_{S \subseteq Dataset \backslash \{k\}} \frac{performance(S \cup \{k\}) - performance(S)}{\binom{n-1}{|S|}}$$

\begin{itemize}
\item Evaluates the expected marginal contribution to all possible sizes of train data samples.
\item Directly applies Lloyd Shapley’s cooperative game theory to individual ML data points.
\end{itemize}

---

# The Data Shapley Value Example

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/algorithm_example.png}
\end{center}

---

# Efficient Approximation: TMC-Shapley

Exact calculation is computationally infeasible for realistic datasets because it grows exponentially.

**Truncated Monte-Carlo (TMC) Approximation:**
\begin{enumerate}
\item Sample a random permutation of the training data.
\item Add one point at a time based on the sampled permutation.
\item Re-train the model to capture the marginal increase in performance.
\item \textbf{Truncate} the calculation when performance saturates to save computational resources.
\end{enumerate}

---

# Application 1: Identifying Low-Quality Data

**Result:** Ordering points from most negative Shapley value to positive allows for rapid dataset cleaning. Examining just ~30\% of the data uncovers nearly all mislabeled examples.

\begin{center}
\includegraphics[width=0.4\columnwidth]{imgs/bad_data.png}
\end{center}

---

# Application 2: Identifying Essential Data

**Case Study: UK Biobank**

* Dataset spanning 500,000 individuals across 22 centers in the UK.

* Centers were evaluated as singular "data sources" for predicting Breast and Colon Cancer.

---

# Application 2: Identifying Essential Data

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/UK.png}
\end{center}

---

# Application 2: Identifying Essential Data

**Insights from Shapley:**

* For most centers, its value is related to the number of patients. This is consistent for Breast Cancer.

* For Colon Cancer, a massive center received a *negative* Shapley value.

* Why this specific center? We don't know for sure.

* A hypothesis is that the model heavily relies on *Age* as a predictive feature, but the specific anomalous center exhibited colon cancer rates entirely independent of age. We detected out-of-distribution data.

---

# Application 2: Identifying Essential Data

\begin{columns}
\begin{column}{0.4\textwidth}
\begin{center}
\includegraphics[width=\columnwidth]{imgs/good_data.png}
\end{center}
\end{column}
\begin{column}{0.4\textwidth}
\begin{center}
\vspace{2em}
\includegraphics[width=\columnwidth]{imgs/good_data_2.png}
\end{center}
\end{column}
\end{columns}

---

# Application 3: Domain Adaptation

What if the training data differs in quality, distribution, or class balance from the test environment?

**Shapley Adaptation Strategy:**

1.  Compute Shapley values relative to the target test distribution.

2.  Remove data with negative values.

3.  Reweight the remaining training data based on relative positive weights.

---

# Domain Adaptation Results (Skin Lesion)

Training on noisy Google Image Search data to test on the clean, clinical HAM10000 dataset.

\begin{center}
\includegraphics[width=0.6\columnwidth]{imgs/skin_data.png}
\end{center}

---

# Domain Adaptation Results (Skin Lesion)

Applying Shapley weights improved classification by $\approx 25\%$.

\begin{center}
\includegraphics[width=0.4\columnwidth]{imgs/skin_training.png}
\end{center}

---

# Domain Adaptation Results (Gender Detection)

Models trained on LFW+A (heavily biased toward white males) fail on balanced datasets like PPB.

\begin{center}
\includegraphics[width=0.6\columnwidth]{imgs/gender_data.png}
\end{center}

---

# Domain Adaptation Results (Gender Detection)

Shapley values identify out-of-distribution elements; adaptation increases accuracy on underrepresented minorities by $\approx 7\%$. Top $20\%$ of high-value datapoints are all female.

\begin{center}
\includegraphics[width=0.4\columnwidth]{imgs/gender_training.png}
\end{center}

---

\begin{center}
\Large\textbf{Extra: Distributional Shapley}
\end{center}

\vspace{1em}

\begin{center}
A More Intrinsic Measure of Value
\end{center}

[@ghorbani2020distributional]

---

# Extra! (Distributional Shapley)

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/val1.png}
\end{center}

---

# Extra! (Distributional Shapley)

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/val2.png}
\end{center}

---

# Extra! (Distributional Shapley)

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/val3.png}
\end{center}

---

# Extra! (Distributional Shapley)

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/val4.png}
\end{center}

---

# Extra! (Distributional Shapley)

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/val5.png}
\end{center}

---

# Extra! (Distributional Shapley)

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/val6.png}
\end{center}

---

\begin{center}
\Large\textbf{Approach 2: Influence Functions}
\end{center}

\vspace{1em}

\begin{center}
Understanding black-box predictions via influence functions
\end{center}

[@koh2017understanding]

---

# The Influence Function Approximation

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/influence_function.png}
\end{center}

\begin{center}
\textbf{Doesn't require retraining!}
\end{center}

---

# Interpretation: Model Representations

$$\ell(z_\text{test}, \hat\theta_{-z_\text{train}}) - \ell(z_\text{test}, \hat\theta) \approx \nabla_\theta \ell(z_\text{test}, \hat\theta)^T H_{\hat\theta}^{-1} \nabla_\theta \ell(z_\text{train}, \hat\theta)$$

\vspace{0.5em}

\begin{columns}
\begin{column}{0.48\textwidth}
\begin{exampleblock}{Gradient = model's representation}
$\nabla_\theta \ell(z_\text{test}, \hat\theta)$\\
How "loudly" the training point wants to pull the model parameters to reduce its own error.
\end{exampleblock}
\end{column}
\begin{column}{0.48\textwidth}
\begin{block}{$H_{\hat\theta}^{-1}$ = curvature of overall loss}
A measure of the curvature of the loss function across all training data. It essentially calculates how strongly the rest of the training dataset resists the parameter changes pushed by point $z$.
\end{block}
\end{column}
\end{columns}

---

# Implementation Output

\begin{center}
\includegraphics[width=0.5\columnwidth]{imgs/influence_code_results.png}
\end{center}

---

# Limitations

\begin{alertblock}{Key assumptions required}

\begin{itemize}
\item \textbf{Convexity:} derivation assumes a convex loss landscape
\item \textbf{Convergence:} derivation assumes the optimizer has converged
\end{itemize}

\end{alertblock}

\textbf{Can you calculate influence functions for a neural network?}

\begin{itemize}
\item Neural networks are inherently \textbf{non-convex}.
\item Frequently feature \textbf{non-differentiable} components.
\item Parameters are typically obtained via \textbf{SGD with early stopping}, rather than converging to a true global minimum.
\end{itemize}

$\Rightarrow$ To adapt influence functions to neural networks, the paper introduces several \textbf{practical approximations}.

---

# Summary

Both approaches aim to link model behavior back to the training data.

\textbf{Data Shapley:}
\begin{itemize}
\item Axiom-backed framework moving beyond LOO by measuring expected contributions over all subsets.
\item Excellent for data valuation, pricing, cleaning, and domain adaptation.
\item Computationally intensive (requires Monte Carlo approximation).
\end{itemize}

\textbf{Influence Functions:}
\begin{itemize}
\item Efficient gradient-based calculation—no retraining needed.
\item Excellent for fast debugging, fairness analysis, and understanding specific predictions.
\item Limited by strict mathematical assumptions (convexity, convergence) in complex models.
\end{itemize}

---

\begin{center}
\Huge Thank You!
\end{center}

---

# References {.allowframebreaks}

\footnotesize