---
title: "\\emoji{wtf} XAI: Understanding Black-Box Predictions via Influence Functions"
bibliography: references.bib

---

# Disclaimer

\input{../disclaimer.tex}

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

# Prior Work: Focus on Test Data

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/prior_work_diagram.png}
\end{center}

---

# Which Parts of the Test Input Matter?

## Saliency methods

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/saliency_example.png}
\end{center}

---

# Our Work: Link Model to Training Data

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/our_work_diagram.png}
\end{center}

---

# Example: Dataset Debugging

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/dataset_debugging.png}
\end{center}

---

# Finding Responsible Training Data

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/doctor_mislabeling.png}
\end{center}

---

# Leave-One-Out Approach

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/loo_approach.png}
\end{center}

[Quenouille, 1956; Tukey, 1958]

---

# LOO Results

\begin{center}
\includegraphics[width=0.7\columnwidth]{imgs/loo_results.png}
\end{center}

- Remove Tumor \#1 $\rightarrow$ \textcolor{red}{$-4\%$} (35\% $\to$ 31\% Normal)
- Remove Tumor \#2 $\rightarrow$ \textcolor{red}{$-2\%$} (35\% $\to$ 33\% Normal)
- Remove mislabeled Normal $\rightarrow$ \textcolor{primarygreen}{$+40\%$} (35\% $\to$ 75\% Normal) \emoji{fire}

---

# Problem and Solution

\begin{alertblock}{Problem}
Repeatedly removing training points and retraining is \textbf{too slow}
\end{alertblock}

\vspace{1em}

\begin{exampleblock}{Solution}
First-order Taylor approximation via \textbf{influence functions}
\end{exampleblock}

---

# Upweighting a Training Point

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/upweighting_diagram.png}
\end{center}

\begin{center}
Removing $z_\text{train}$ $\equiv$ upweighting by $\epsilon = -\frac{1}{n}$
\end{center}

---

# Taylor Approximation

\begin{center}
\includegraphics[width=0.65\columnwidth]{imgs/taylor_approx.png}
\end{center}

\begin{columns}
\begin{column}{0.48\textwidth}
\begin{center}
\textbf{Slow:} actual change (retrain without the point)
\end{center}
\end{column}
\begin{column}{0.48\textwidth}
\begin{center}
\textbf{Fast:} estimated change (first-order Taylor)
\end{center}
\end{column}
\end{columns}

---

# The Influence Function Approximation

Change in loss on $z_\text{test}$ after removing $z_\text{train}$:

\vspace{0.5em}

$$\ell(z_\text{test}, \hat\theta_{-z_\text{train}}) - \ell(z_\text{test}, \hat\theta) \approx \nabla_\theta \ell(z_\text{test}, \hat\theta)^T H_{\hat\theta}^{-1} \nabla_\theta \ell(z_\text{train}, \hat\theta)$$

\vspace{0.5em}

\begin{columns}
\begin{column}{0.32\textwidth}
\begin{center}
{\small Gradient of loss on $z_\text{test}$}
\end{center}
\end{column}
\begin{column}{0.32\textwidth}
\begin{center}
{\small Inverse Hessian}
\end{center}
\end{column}
\begin{column}{0.32\textwidth}
\begin{center}
{\small Gradient of loss on $z_\text{train}$}
\end{center}
\end{column}
\end{columns}

\vspace{1em}
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

# Technical Details

$$\hat\theta_{\epsilon,z} \stackrel{\text{def}}{=} \arg\min_{\theta\in\Theta} \frac{1}{n}\sum_{i=1}^n L(z_i,\theta) + \epsilon L(z,\theta)$$

\vspace{0.5em}

Differentiating at $\epsilon = 0$ using the chain rule:

$$\frac{dL(z_\text{test}, \hat\theta_{\epsilon,z})}{d\epsilon}\bigg|_{\epsilon=0} = \nabla_\theta L(z_\text{test}, \hat\theta)^\top \frac{d\hat\theta_{\epsilon,z}}{d\epsilon}\bigg|_{\epsilon=0}$$

Applying the implicit function theorem gives:

$$\frac{d\hat\theta_{\epsilon,z}}{d\epsilon}\bigg|_{\epsilon=0} = -H_{\hat\theta}^{-1} \nabla_\theta L(z, \hat\theta)$$

---

# From Classical to Modern Settings

\begin{columns}
\begin{column}{0.48\textwidth}
\textbf{Classical works (small \& low-dimensional):}
\begin{itemize}
\item Jaeckel, 1972 — The infinitesimal jackknife
\item Hampel, 1974 — The influence curve and its role in robust estimation
\item Cook, 1977 — Detection of influential observations in linear regression
\end{itemize}
\end{column}
\begin{column}{0.48\textwidth}
\textbf{Modern challenge (large \& high-dimensional):}

\vspace{0.5em}

$$\nabla_\theta \ell(z_\text{test}, \hat\theta)^T \underbrace{H_{\hat\theta}^{-1}}_{\text{difficult!}} \nabla_\theta \ell(z_\text{train}, \hat\theta)$$

\vspace{0.5em}

We use tools from 2nd-order optimization \& stochastic estimation

{\footnotesize [Pearlmutter, 1994; Martens, 2010; Agarwal et al., 2017]}
\end{column}
\end{columns}

---

# Removing Single Points: Validation

\begin{center}
\includegraphics[width=0.65\columnwidth]{imgs/removing_single_points.png}
\end{center}

Logistic regression (MNIST): each point = removing one training example. Influence function estimate tracks actual LOO change closely.

---

# Where Can You Apply Influence Functions?

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/where_to_apply.png}
\end{center}

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

\begin{columns}
\begin{column}{0.55\textwidth}
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
\end{column}
\begin{column}{0.42\textwidth}
\begin{center}
\includegraphics[width=\columnwidth]{imgs/our_work_diagram.png}
\end{center}
\end{column}
\end{columns}

---

\begin{center}
\Huge Thank You!
\end{center}

---

# References {.allowframebreaks}

\footnotesize
