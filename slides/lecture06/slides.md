---
title: "\\emoji{wtf} XAI: Generalized Additive Models \\& Prototype-Based Approaches"
bibliography: references.bib

---

# Disclaimer

\input{../disclaimer.tex}

---

# Intelligible Models for HealthCare - GAMS

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/healthcare_title.png}
\end{center}

\begin{center}
- Generalized Additive Models -
\end{center}

[@caruana2015intelligible]

---

# Contributions

Two healthcare case studies are presented:
- **Pneumonia risk prediction** — small dataset (14K patients, 46 features)
- **30-day hospital readmission** — large dataset (196K patients, 3,956 features)

\vspace{0.5cm}

## Main Claim
GA²Ms achieve **state-of-the-art accuracy** while remaining **intelligible, modular, and editable** — challenging the assumption that accuracy and interpretability must be traded off..

## Roadmap

1. Motivation
2. Intelligible Models
3. Case study: Pneumonia risk
4. Case study: 30-day readmission

---

# Motivation

- A large project to evaluate application of ML to healthcare problems
- Predicting \textbf{probability of death (POD)} for pneumonia patients

    - **Most accurate model:** Neural nets ($0.86$ AUC)
    - **Actually Deployed:** Logistic Regression: ($0.77$ AUC)

\begin{center}
\Large
\textbf{Why was logistic regression used instead?}
\end{center}

---

# Motivation: The Asthma Paradox

- 1990s study: neural nets were the **most accurate** models for pneumonia mortality
- A rule-based system discovered: \texttt{HasAsthma(x) $\Rightarrow$ LowerRisk(x)}
  - Asthmatic patients were sent directly to the ICU $\rightarrow$ aggressive care $\rightarrow$ lower observed mortality
  - The model learned the **effect of treatment**, not the true underlying risk

\vspace{0.3cm}

\begin{alertblock}{The Core Problem: {\bf The NN almost certainly learned the same pattern}}
But because it was \textbf{opaque}, there was no way to detect or fix it. Deploying it could have sent high-risk asthmatic patients home.
\end{alertblock}

\vspace{0.3cm}

## The Lesson
- A dangerous rule in an intelligible model can be **recognized and removed**.
- A dangerous pattern in a black-box model may never be found.

---

# Motivation: The problem persists

\begin{center}
\Large
\textbf{SVMs, random forests, boosted trees, deep nets — all unintelligible}
\end{center}

\vspace{0.5cm}

## Why GA²Ms

Accurate as black-box models — but **intelligible**, **modular**, and **editable** by domain experts.


---

# Generalized Additive Models (GAMs)

**Intuition:** Instead of one global equation, the model learns a separate function for each feature — then adds them up.

\vspace{0.3cm}

$$g(\mathbb{E}[y]) = \beta_0 + \sum_j f_j(x_j)$$

\vspace{0.3cm}

where $g$ is a link function and each $f_j$ is a **shape function** learned from data, with $\mathbb{E}[f_j] = 0$.

\vspace{0.3cm}

\begin{block}{Key Properties}
\begin{itemize}
  \item Each $f_j$ can be \textbf{non-linear} — no need to manually discretize features
  \item Contributions are \textbf{additive and independent} — each $f_j$ can be visualized separately
  \item Logistic regression is a special case where $f_j(x_j) = w_j x_j$
\end{itemize}
\end{block}

---

# GAMs: Notation

$$g(\mathbb{E}[y]) = \beta_0 + \sum_j f_j(x_j)$$

\vspace{0.3cm}

- $g$ — **link function**: maps the expected output to the linear predictor. For binary classification: $g(p) = \log\frac{p}{1-p}$ (logit)
- $f_j$ — **shape function**: learned from data, centered so that $\mathbb{E}[f_j] = 0$, ensuring each term has a unique, identifiable contribution.
    - $\mathbb{E}[f_j] = 0$ The average of the shape function over the training data is zero:
- $\beta_0$ — **baseline**: the only constant term; calibrated so that the average predicted probability equals the observed baseline rate in the training data

---

# GAMs — Shape Functions (Bike Sharing)

\begin{center}
\includegraphics[width=0.6\columnwidth]{imgs/gams_bikeshare.png}

\textbf{Shape functions learned by a GAM on a bike-sharing dataset.}

Each plot shows the contribution of one feature to predicted demand (y-axis: additive score relative to baseline)
\end{center}

---

# GAMs — Shape Functions (Bike Sharing)

\begin{center}
\includegraphics[width=0.5\columnwidth]{imgs/gams_bikeshare.png}
\end{center}

Features shown:

\fontsize{7.5pt}{6pt}
- **Hour** (top-left) — demand peaks at 8am and 5-6pm, reflecting commute patterns;
- **Temperature** (top-right) — demand rises with warmth, drops above ~35°C;
- **Year** (bottom-left) — demand grew from 2011 to 2012;
- **Working Day** (bottom-center) — slight increase on working days;
- **Season** (bottom-right) — winter highest, spring lowest.

---

# GAMs — Shape Functions (Concrete/Other)

$$g(\mathbb{E}[y]) = \beta_0 + f_1(x_1) + f_2(x_2) + \cdots + f_p(x_p)$$

\vspace{0.3cm}

\begin{center}
Each $f_j$ is learned freely from data — no linearity assumption required.
\end{center}

\begin{columns}
  \begin{column}{0.48\textwidth}
    \begin{figure}
      \includegraphics[width=.75\textwidth]{imgs/generic_shapes.png}
      \caption{Shape functions can take any form: linear, concave, oscillating.}
    \end{figure}
  \end{column}
  \begin{column}{0.48\textwidth}
    \begin{figure}
      \includegraphics[width=\textwidth]{imgs/sement_shapes.png}
      \caption{\textbf{Cement:} monotonically increasing — more cement, higher strength. \textbf{Water:} non-monotone — there is an optimal range; too much or too little reduces strength. \textbf{Age:} rapid early growth (curing process), stabilizes with a second soft peak at later ages.}
    \end{figure}
  \end{column}
\end{columns}


---

# From GAM to GA$^2$M

## GAMS

$$g(\mathbb{E}[y]) = \beta_0 + \sum_j f_j(x_j)$$

A GAM models each feature independently — the contribution of $x_j$ to the output
never depends on the value of any other feature.

## GA$^2$M

$$g(\mathbb{E}[y]) = \beta_0 + \sum_j f_j(x_j) + \sum_{i \neq j} f_{ij}(x_i, x_j)$$

Adds pairwise interaction terms $f_{ij}(x_i, x_j)$,
capturing cases where the effect of one feature depends on another.
- First fits the best GAM, then detects and ranks all pairwise interactions in the residuals.
- The top $k$ pairs are added.

---

# Intelligibility and Accuracy

\small
| **Model** | **Form** | **Intelligibility** | **Accuracy** |
|---|---|---|---|
| **Linear Model** | $y = \beta_0 + \beta_1 x_1 + \ldots + \beta_n x_n$ | +++ | + |
| **Generalized Linear Model** | $g(y) = \beta_0 + \beta_1 x_1 + \ldots + \beta_n x_n$ | +++ | + |
| **Additive Model** | $y = f_1(x_1) + \ldots + f_n(x_n)$ | ++ | ++ |
| **Generalized Additive Model** | \textbf{$g(y) = f_1(x_1) + \ldots + f_n(x_n)$} | **++** | **++** |
| **Full Complexity Model** | $y = f(x_1, \ldots, x_n)$ | + | +++ |

[@lou2012intelligible]

---

# Learning Shape Functions

Shape functions $f_j$ can be represented as **splines** or **regression trees**.
The paper uses gradient boosting with bagging of shallow trees — empirically the most accurate choice.

\vspace{0.3cm}

## Training GA$^2$M

1. Fit the best GAM using gradient boosting on individual features
2. Compute residuals and detect all possible pairwise interactions
3. Rank interactions by their ability to explain the residuals
4. Add the top $k$ pairs to the model ($k$ chosen by cross-validation)

\vspace{0.3cm}

Bagging (100 rounds for pneumonia) reduces overfitting and provides
pseudo-confidence intervals for the shape plots.

---

# Case Study: Pneumonia Risk

\begin{columns}
\begin{column}{0.48\textwidth}
\begin{block}{Dataset}
\begin{itemize}
  \item 14,199 pneumonia patients
  \item Train: 9,847
  \item Test: 4,352
  \item 46 features
\end{itemize}
\end{block}
\end{column}
\begin{column}{0.48\textwidth}
\begin{alertblock}{Task}
Predict \textbf{probability of death (POD)} \\
\vspace{0.2cm}
10.86\% of patients died (1,542)
\end{alertblock}
\end{column}
\end{columns}

---

# Pneumonia Risk: Features

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/pneumonia_features.png}
\end{center}

- **C (continuous):** numeric feature — the GAM learns a full shape function $f_j(x_j)$ that can be non-linear
- **— (binary/categorical):** takes values 0/1 — the shape function reduces to two points; presented as a bar plot for visual consistency with continuous features

---

# Pneumonia Risk: AUC Results

| **Model** | **Pneumonia (AUC)** |
|---|---|
| **Logistic Regression** | 0.8432 |
| **GAM** | 0.8542 |
| **GA²M** | 0.8576 |
| **Random Forests** | 0.8460 |
| **LogitBoost** | 0.8493 |

- GA²M achieves the highest AUC while remaining fully intelligible.
- The gap between models is small (<0.02).
- **Note** that the dataset is highly imbalanced
(only **10.86%** of patients died), which can bias AUC as an evaluation metric.


---

# Understanding Outputs of GA$^2$M (1/2)

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/ga2m_outputs_1.png}
\end{center}

Shape functions learned by GA²M on the pneumonia dataset (y-axis: risk score contribution relative to baseline).

- **Age:** low and flat below 50, rises sharply after 65.
- **Asthma:** having asthma *decreases* predicted risk — a known data artifact (ICU effect).
- **BUN (Blood Urea Nitrogen) level:** missing/low values indicate low risk; elevated levels (>30) signal kidney or cardiac complications.
- **Cancer:** strong positive risk contribution — nearly doubles the predicted odds of death.

---

# Understanding Outputs of GA$^2$M (2/2)

\begin{center}
\includegraphics[width=0.3\columnwidth]{imgs/ga2m_age_cancer.png}
\end{center}

The interaction term $f_{ij}(\text{age}, \text{cancer})$ reveals a pattern
invisible to individual shape functions:

\vspace{0.3cm}

- **Cancer = 1, young patients:** highest risk (yellow) — childhood cancers are associated with high risk of death
- **Cancer = 1, older patients:** moderate risk (orange/red) — adult cancers are serious but less acutely lethal
- **Cancer = 0:** uniformly low risk (purple) regardless of age

---

# Case Study: 30-Day Readmission

\begin{columns}
\begin{column}{0.48\textwidth}
\begin{block}{Dataset}
\begin{itemize}
  \item 195K patients (train)
  \item 100K patients (test)
  \item \textbf{3,956 features}
\end{itemize}
\end{block}
\end{column}
\begin{column}{0.48\textwidth}
\begin{alertblock}{Context}
Hospitals with high readmission rates are \textbf{penalized financially} (inadequate earlier care). \\
\vspace{0.2cm}
8.91\% of patients readmitted within 30 days.
\end{alertblock}
\end{column}
\end{columns}

---

# 30-Day Readmission: AUC Results

| **Model** | **Readmission (AUC)** |
|---|---|
| **Logistic Regression** | 0.7523 |
| **GAM** | 0.7795 |
| **GA²M** | 0.7833 |
| **Random Forests** | 0.7671 |
| **LogitBoost** | 0.7835 |

- GA²M matches LogitBoost (0.7833 vs 0.7835) while remaining fully intelligible —
on a dataset with 196K patients and 3,956 features.
- Again, the dataset is imbalanced (**8.91%** readmission rate),
so AUC should be interpreted with caution as it may overestimate model performance.


---

# Case Study: High Risk Patient


\begin{center}
Top 6 shape functions sorted by risk contribution for a High Risk Patient ($p = 0.9326$)

  \includegraphics[width=.70\textwidth]{imgs/patient1.png}
\end{center}

\small
- The blue line marks the patient's feature value; the number is its risk score contribution.
- High readmission risk is driven by a history of frequent hospitalizations (40 total, 19 in the last 12 months)
- and large doses of amoxicillin — suggesting an ongoing infection not responding to antibiotics.

---

# Case Study: Low Risk Patient

\begin{center}
Top 6 shape functions sorted by risk contribution for a Low Risk Patient ($p = 0.0873$)

\includegraphics[width=0.70\columnwidth]{imgs/patient_insights_2.png}
\end{center}

\small
- Post menopausal.
- Moderate risk is driven by treatable cancers (endometrial carcinoma, non-invasive breast lesion)
and a benign abdominal tumor — conditions that respond well to outpatient treatment.
- Notably, inpatient and ER visit counts are low, suggesting the patient is being managed
effectively without repeated hospitalization.


---

# Modularity of GAMs

\begin{block}{Model Decomposition}
$$\text{prediction} = \underbrace{\beta_0}_{\text{bias}} + \underbrace{\sum_j f_j(x_j)}_{\text{individual features}} + \underbrace{\sum_{i \neq j} f_{ij}(x_i, x_j)}_{\text{pairwise interactions}}$$
\end{block}

\vspace{0.5cm}

This structure helps us **clearly understand the model**: for each patient, we can compute which term is resulting in what risk score and rank terms based on their contribution.

---

# Sorting Terms by Importance

- For each patient, we can compute which term contributes what risk score
- Terms are ranked by their individual risk score contribution for that patient
- This ranking identifies which features are driving the risk prediction for each specific patient

Although the readmission model has over 4,000 terms, in practice only a small number
are relevant per patient — **making even large models locally interpretable**.

---

# Feature Shaping vs. Expert Discretization

\begin{columns}
\begin{column}{0.48\textwidth}
\begin{block}{Expert Discretization}
Experts manually convert continuous features into binary ranges
(e.g., age 18--39, 40--54, \ldots). Used in the original logistic regression model.
\end{block}
\end{column}
\begin{column}{0.48\textwidth}
\begin{exampleblock}{GAM Feature Shaping}
GAMs \textbf{learn} the function shape directly from data — no manual binning required.
GAM with continuous features outperformed expert-discretized LR by $\sim$0.01 AUC.
\end{exampleblock}
\end{column}
\end{columns}

\vspace{0.5cm}

\begin{alertblock}{Conclusion}
Expert discretization introduces unnecessary rigidity — GAMs can discover finer structure
(e.g., a jump in pneumonia risk at age 67) that experts would not define by hand.
\end{alertblock}

---

# Correlation $\neq$ Causation

\begin{alertblock}{\emoji{warning} Important Warning}
GAMs and GA$^2$Ms are intelligible — \textbf{but they are not causal!}
\end{alertblock}

\vspace{0.5cm}

- What we see in plots are \textbf{associations} captured from data, not causal implications
- It is often easy to confuse intelligibility of predictive models with causality

\vfill

\begin{center}
\Large \textbf{Please don't make that mistake!}
\end{center}

---

# Deep Learning for Case-Based Reasoning through Prototypes

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/prototypes_title.png}

\Large \textbf{Prototype-Based Approaches}
\end{center}

[@li20172017]

---

# Contributions (Prototypes)

\begin{exampleblock}{Novel Architecture}
Proposed and developed a novel network architecture for deep learning that:
\end{exampleblock}

\vspace{0.3cm}

- Explains its own reasoning for each prediction
- \textbf{Not} post-hoc explanations
- Prototypes are learned \textbf{during training}
- Explanations are \textbf{faithful} to what the network computes

---

# Motivation (Prototypes)

- ML models are increasingly deployed to answer societal questions $\Rightarrow$ \textbf{interpretability/transparency}
- \textbf{Radiology:} lack of transparency poses challenges to FDA approval for deep learning models
- Neural nets are particularly difficult to understand because of the high degree of non-linearity

---

# Related Work: Post-hoc Explanations

\begin{alertblock}{Problem with Post-hoc Approach}
Past neural nets were designed mainly for accuracy, with post-hoc explanations added after.
\end{alertblock}

\vspace{0.5cm}

- Build neural net first, then interpret!
- Post-hoc explanations \textbf{may not be faithful} to the model
- Easy to create \textbf{multiple conflicting yet convincing} explanations, none of which is correct

---

# Background: Autoencoder (1/3)

\begin{center}
\includegraphics[width=0.65\columnwidth]{imgs/autoencoder_1.png}
\end{center}

\begin{center}
\textbf{Non-linear Dimensionality Reduction and Reconstruction}
\end{center}

---

# Background: Autoencoder (2/3)

\begin{center}
\includegraphics[width=0.65\columnwidth]{imgs/autoencoder_2.png}
\end{center}

---

# Background: Constructing an Autoencoder

- Constrain the number of nodes present in the hidden layer(s) of the network
  - Limiting the amount of information that can flow through the network
- By penalizing the network according to the \textbf{reconstruction error}, the model can learn the most important attributes of the input data

\vspace{0.3cm}

\begin{exampleblock}{Key Insight}
The encoding will learn and describe \textbf{latent attributes} of the input data.
\end{exampleblock}

---

# Proposed Network Architecture

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/network_architecture.png}
\end{center}

\begin{center}
\small \textit{Autoencoding}
\end{center}

---

# Autoencoder — Latent Space

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/autoencoder_latent.png}
\end{center}

\footnotesize Input $\mathbf{x} \in \mathbb{R}^p$, encoded representation $f(\mathbf{x}) \in \mathbb{R}^q$ with $q < p$

---

# Prototype Layer

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/prototype_layer.png}
\end{center}

\begin{block}{Prototype Layer Computation}
$$\mathbf{z} = f(\mathbf{x}) \qquad p(\mathbf{z}) = \left[\|\mathbf{z} - \mathbf{p}_1\|_2^2, \quad \|\mathbf{z} - \mathbf{p}_2\|_2^2, \quad \ldots \quad \|\mathbf{z} - \mathbf{p}_m\|_2^2\right]^\top$$
\end{block}

\footnotesize Each node in layer $p$ computes one of the above elements.

---

# Fully Connected Layer

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/fully_connected.png}
\end{center}

- The fully connected layer computes weighted sums of the distances: $Wp(\mathbf{z})$
- $W$ is a $k \times m$ matrix

---

# Softmax Layer

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/softmax_layer.png}
\end{center}

\begin{block}{}
The weighted sums $Wp(\mathbf{z})$ are normalized by the softmax layer to output a \textbf{probability distribution over $K$ classes}.
\end{block}

---

# Advantages of the Proposed Architecture

\begin{exampleblock}{Key Advantages}
\begin{itemize}
  \item \textbf{Automatically learns} useful features (non-linear dimensional reduction)
  \item Suitable for \textbf{high-dimensional data} such as images
  \item Prototype vectors can be \textbf{decoded and visualized} (same latent space as encoded inputs)
  \item Ability to interpret \textbf{without post-hoc analysis}
\end{itemize}
\end{exampleblock}

---

# Cost Function

\begin{block}{Cross-Entropy Loss}
$$E(h \circ f, D) = \frac{1}{n} \sum_{i=1}^{n} \sum_{k=1}^{K} -\mathbb{1}[y_i = k] \log((h \circ f)_k(\mathbf{x}_i))$$
\end{block}

\vspace{0.5cm}

\begin{block}{Reconstruction Error}
$$R(g \circ f, D) = \frac{1}{n} \sum_{i=1}^{n} \|(g \circ f)(\mathbf{x}_i) - \mathbf{x}_i\|_2^2$$
\end{block}

---

# Cost Function: Interpretability Regularizers

\begin{block}{$R_1$: Prototypes close to training data}
$$R_1(\mathbf{p}_1, \ldots, \mathbf{p}_m, D) = \frac{1}{m} \sum_{j=1}^{m} \min_{i \in [1,n]} \|\mathbf{p}_j - f(\mathbf{x}_i)\|_2^2$$
\end{block}

\begin{block}{$R_2$: Training data close to prototypes}
$$R_2(\mathbf{p}_1, \ldots, \mathbf{p}_m, D) = \frac{1}{n} \sum_{i=1}^{n} \min_{j \in [1,m]} \|f(\mathbf{x}_i) - \mathbf{p}_j\|_2^2$$
\end{block}

\footnotesize
- $R_1$: Each prototype vector should be as close as possible to \textbf{at least one training example}
- $R_2$: Each training example should be as close as possible to \textbf{one prototype}

---

# Full Cost Function

$$L((f, g, h), D) = E(h \circ f, D) + \lambda R(g \circ f, D) + \lambda_1 R_1(\mathbf{p}_1, \ldots, \mathbf{p}_m, D) + \lambda_2 R_2(\mathbf{p}_1, \ldots, \mathbf{p}_m, D)$$

---

# Training: Neural Network Steps

1. **Define architecture**
2. **Outline cost function**
3. **Forward pass, compute derivatives, backpropagate, update parameters — repeat!**

\vspace{0.5cm}

\begin{block}{Note on min functions}
Min functions are not technically differentiable — but in practice, packages allow it. This is essentially \textbf{gradient descent}.
\end{block}

---

# Backpropagation: Intuition (1/4)

\begin{center}
\includegraphics[width=0.6\columnwidth]{imgs/backprop_1.png}
\end{center}

---

# Backpropagation: Intuition (2/4)

\begin{center}
\includegraphics[width=0.6\columnwidth]{imgs/backprop_2.png}
\end{center}

---

# Backpropagation: Intuition (3/4)

\begin{center}
\includegraphics[width=0.6\columnwidth]{imgs/backprop_3.png}
\end{center}

---

# Backpropagation: Intuition (4/4)

\begin{center}
\includegraphics[width=0.6\columnwidth]{imgs/backprop_4.png}
\end{center}

\begin{center}
\textcolor{red}{Local gradient $\times$ upstream gradient}
\end{center}

---

# Results: MNIST Data

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/mnist_results.png}
\end{center}

\begin{exampleblock}{Performance}
Test accuracy \textbf{above 99\%} and on par with SOTA. Reconstruction Error: 4.22
\end{exampleblock}

---

# Learned Weight Matrix

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/weight_matrix.png}
\end{center}

---

# Ablation Study on Cars Data (1/2)

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/ablation_1.png}
\end{center}

\begin{columns}
\begin{column}{0.48\textwidth}
\begin{exampleblock}{Learned Prototypes (with $R_1, R_2$)}
Clear, recognizable car images.
\end{exampleblock}
\end{column}
\begin{column}{0.48\textwidth}
\begin{alertblock}{Without $R_1$ and $R_2$}
Noisy, uninterpretable prototypes.
\end{alertblock}
\end{column}
\end{columns}

---

# Ablation Study on Cars Data (2/2)

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/ablation_2.png}
\end{center}

\begin{columns}
\begin{column}{0.48\textwidth}
\begin{alertblock}{Without $R_1$}
Noisy, unrecognizable prototypes.
\end{alertblock}
\end{column}
\begin{column}{0.48\textwidth}
\begin{block}{Without $R_2$}
Redundant prototypes (lack of diversity).
\end{block}
\end{column}
\end{columns}

---

\begin{center}
\Huge Thank You!
\end{center}

---

# References {.allowframebreaks}

\footnotesize
