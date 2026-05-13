---
title: "\\emoji{wtf} XAI: What is Your Data Worth? Equitable Valuation of Data"
bibliography: references.bib

---

# Disclaimer

\input{../disclaimer.tex}

---

\begin{center}
\Large\textbf{What is Your Data Worth? Equitable Valuation of Data}
\end{center}

\vspace{1em}

\begin{center}
Amirata Ghorbani, James Zou — ICML 2019
\end{center}

[@ghorbani2019data]

---

# The Data Valuation Problem

If data is fuel, we need a principled way to measure its value. Stakeholders have different priorities:

* **ML Engineers:** Assess heterogeneous sources and data quality.
* **Data Vendors:** Determine fair pricing for buying and selling data.
* **Individuals/Data Producers:** Understand compensation or credit for contributed data.


---

# Ingredients of Data Value

\begin{center}
\includegraphics[width=0.6\columnwidth]{imgs/ingredients.png}
\end{center}

---

# Leave One Out Method

\begin{center}
\includegraphics[width=0.4\columnwidth]{imgs/LOO1.png}
\end{center}

---

# Desirable Properties of Valuation

A fair valuation method must satisfy three fundamental axioms from cooperative game theory:

1.  **Null Element:** If adding a point to *any* subset of training data never changes the model's performance, its value is exactly 0.
2.  **Symmetry:** If adding point $A$ or point $B$ to any subset always results in the exact same performance change, they must receive the same value ($Value(A) = Value(B)$).
3.  **Linearity:** If the performance metric is a sum of performances on individual tasks, the data value must reflect the sum of values for those individual tasks.

---

# The Data Shapley Value

The only data value mathematically guaranteed to satisfy these three properties is based on marginal contributions across all possible subset sizes.

$$Value(data~k) = \sum_{S \subseteq D \setminus \{k\}} \frac{performance(S \cup \{k\}) - performance(S)}{\binom{n-1}{|S|}}$$

\begin{itemize}
\item Evaluates the expected contribution to all possible sizes of train data samples.
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

**Insights from Shapley:**

* For Colon Cancer, a massive center received a *negative* Shapley value.

* Investigation revealed the model heavily relied on *Age* as a predictive feature, but the specific anomalous center exhibited colon cancer rates entirely independent of age.

\begin{center}
\includegraphics[width=0.5\columnwidth]{imgs/UK.png}
\end{center}

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

Training on noisy Google Image Search data to test on the clean, clinical HAM10000 dataset. Applying Shapley weights improved classification by $\approx 25\%$.

\begin{center}
\includegraphics[width=0.6\columnwidth]{imgs/skin_data.png}
\end{center}

---

# Domain Adaptation Results (Skin Lesion)

\begin{center}
\includegraphics[width=0.5\columnwidth]{imgs/skin_training.png}
\end{center}

---

# Domain Adaptation Results (Gender Detection)

Models trained on LFW+A (heavily biased toward white males) fail on balanced datasets like PPB. Shapley values easily identify out-of-distribution elements; adaptation increases accuracy on underrepresented minorities by $\approx 7\%$.

\begin{center}
\includegraphics[width=0.6\columnwidth]{imgs/gender_data.png}
\end{center}

---

# Domain Adaptation Results (Gender Detection)

\begin{center}
\includegraphics[width=0.5\columnwidth]{imgs/gender_training.png}
\end{center}

---

# Summary

\begin{itemize}
\item Data Shapley provides an equitable, axiom-backed framework to quantify the value of individual ML data points.
\item It moves beyond LOO limitations by measuring expected contributions over all possible subsets.
\item Applications span data cleaning, debugging, valuation pricing, and addressing distributional shifts.
\end{itemize}

---

# Understanding Models via Their Training Data

\begin{center}
\Large\textbf{Understanding black-box predictions via influence functions}
\end{center}

\vspace{1em}

\begin{center}
Pang Wei Koh, Percy Liang — ICML 2017
\end{center}

[@koh2017understanding]

---

# Dataset Debugging

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/db1.png}
\end{center}

---

# Dataset Debugging

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/db2.png}
\end{center}

---

# Dataset Debugging

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/db3.png}
\end{center}

---

# Dataset Debugging

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/db4.png}
\end{center}

---

# Dataset Debugging

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/db5.png}
\end{center}

---

# Dataset Debugging

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/db6.png}
\end{center}

---

# Dataset Debugging

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/db7.png}
\end{center}

---

# Dataset Debugging

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/db8.png}
\end{center}

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
$\nabla_\theta \ell(z_\text{test}, \hat\theta)$ encodes how the model "sees" $z_\text{test}$
\end{exampleblock}
\end{column}
\begin{column}{0.48\textwidth}
\begin{block}{$H_{\hat\theta}^{-1}$ = effect of other training points}
Accounts for the curvature induced by the full training set
\end{block}
\end{column}
\end{columns}

\vspace{0.5em}

High influence $\Rightarrow$ test and train have **similar model representations**

---

# Removing Single Points: Validation

\begin{center}
\includegraphics[width=0.65\columnwidth]{imgs/mnist.png}
\end{center}

Logistic regression (MNIST): each point = removing one training example. Influence function estimate tracks actual LOO change closely.

---

# Impact

\begin{columns}
\begin{column}{0.32\textwidth}
\begin{block}{Robustness}
{\small
\begin{itemize}
\item Training set biases [Ren et al., 2018]
\item Inference reliability [Broderick et al., 2021]
\item Cross-validation [Stephenson et al., 2020]
\item Memorization [Feldman, 2019]
\end{itemize}
}
\end{block}
\end{column}
\begin{column}{0.32\textwidth}
\begin{block}{Applications}
{\small
\begin{itemize}
\item Data distillation [Wang et al., 2020]
\item Data valuation [Jia et al., 2019]
\item Active learning [Gudovskiy et al., 2020]
\item Data debugging [Guo et al., 2021]
\end{itemize}
}
\end{block}
\end{column}
\begin{column}{0.32\textwidth}
\begin{block}{Fairness \& Security}
{\small
\begin{itemize}
\item Algorithmic bias [Verma et al., 2021]
\item Data labor [Arrieta-Ibarra, 2018]
\item Privacy [Shokri et al., 2021]
\item Data poisoning [Chen et al., 2017]
\end{itemize}
}
\end{block}
\end{column}
\end{columns}

---

# Limitations

\begin{alertblock}{Key assumptions required}
\begin{itemize}
\item What assumptions on models are needed to calculate influence functions?
\item Can you calculate influence functions for a neural network?
\end{itemize}
\end{alertblock}

$$\hat\theta_{\epsilon,z} \stackrel{\text{def}}{=} \arg\min_{\theta\in\Theta} \frac{1}{n}\sum_{i=1}^n L(z_i,\theta) + \epsilon L(z,\theta)$$

- **Non-convexity:** derivation assumes a convex loss landscape
- **Non-convergence:** derivation assumes the optimizer has converged

\vspace{0.5em}

\begin{center}
\textit{"If Influence Functions are the Answer, Then What is the Question?"}

{\footnotesize Bae, Ng, Lo, Ghassemi \& Grosse}
\end{center}

---

# Summary

\begin{itemize}
\item \textbf{Link} model behavior to training data
\item \textbf{Efficient} to calculate — no retraining needed
\item \textbf{Many applications:} debugging, fairness, security, privacy
\item \textbf{Limitations} when applying to complex models
  \begin{itemize}
  \item Non-convexity
  \item Non-convergence
  \end{itemize}
\end{itemize}

---

\begin{center}
\Huge Thank You!
\end{center}

---

# References {.allowframebreaks}

\footnotesize
