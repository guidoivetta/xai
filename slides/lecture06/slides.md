---
title: "\\emoji{brain} XAI: Generalized Additive Models \\& Prototype-Based Approaches"
bibliography: references.bib

---

# Disclaimer

\input{../disclaimer.tex}

---

# Paper Presentations

\begin{alertblock}{Reminder}
If you are presenting next week, please come and see us in office hours this week. Ideally, we would like to walk through your slides with you.
\end{alertblock}

\vspace{0.5cm}

- Each paper: **25 mins** of Paper Presentation + **5 mins** Q\&A

---

# Guidelines for Paper Presentation

1. Motivation
2. Problem Statement
3. Summary of Contributions
4. Related Work
5. Preliminaries + Background \textit{(Intuition First!)}
6. Approach \textit{(Intuition First!)}
7. Key Experimental Results
8. Conclusions
9. Your Perspective on the Weaknesses of Paper
10. What would you do differently?

---

# Generalized Additive Models

\begin{center}
\Huge Generalized Additive Models
\end{center}

---

# Intelligible Models for HealthCare

\begin{center}
\includegraphics[width=0.5\columnwidth]{imgs/healthcare_title.png}
\end{center}

\begin{center}
\Large \textcolor{red}{Intelligible Models for HealthCare}

\vspace{0.3cm}
Caruana et al.
\end{center}

---

# Contributions

\begin{exampleblock}{Main Contributions}
Two case studies where Generalized Additive Models (intelligible) yield state-of-the-art accuracy:
\begin{itemize}
  \item Pneumonia risk prediction
  \item 30-day hospital readmission
\end{itemize}
\end{exampleblock}

\vspace{0.5cm}

\begin{block}{Claim}
GAMs is a class of models that can handle the \textbf{interpretability/accuracy trade-off} quite well.
\end{block}

---

# Roadmap

1. Motivation
2. Intelligible Models
3. Case study: Pneumonia risk
4. Case study: 30-day readmission

---

# Motivation (1/3)

- A large project to evaluate application of ML to healthcare problems
- Predicting \textbf{probability of death (POD)} for pneumonia patients

\vspace{0.5cm}

\begin{columns}
\begin{column}{0.48\textwidth}
\begin{exampleblock}{Most Accurate}
Neural nets: \textbf{0.86 AUC}
\end{exampleblock}
\end{column}
\begin{column}{0.48\textwidth}
\begin{alertblock}{Actually Deployed}
Logistic Regression: \textbf{0.77 AUC}
\end{alertblock}
\end{column}
\end{columns}

\vspace{0.5cm}

\begin{center}
\textbf{Why was logistic regression used instead?}
\end{center}

---

# Motivation (2/3)

- Rule-based learning method was also used
- Insight: \texttt{HasAsthma(x) $\Rightarrow$ LowerRisk(x)}
  - \textit{Counterintuitive?}

\vspace{0.5cm}

\begin{alertblock}{Key Problem}
Rule-based system was intelligible, making it easy to \textbf{recognize and remove dangerous rules}. \\
Lack of intelligibility made it harder to deploy neural nets because it was difficult to know other problems with the model.
\end{alertblock}

---

# Motivation (3/3)

- Many more models today are equally unintelligible: SVMs, random forests, boosted trees

\vspace{0.5cm}

\begin{exampleblock}{Why GAMs?}
\begin{itemize}
  \item GAMs are both \textbf{intelligible and accurate!}
  \item \textbf{Editable} by domain experts
\end{itemize}
\end{exampleblock}

---

# GAMs — Shape Functions (Bike Sharing)

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/gams_bikeshare.png}
\end{center}

---

# GAMs — Shape Functions (Concrete/Other)

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/gams_shapes.png}
\end{center}

---

# GAMs and GA$^2$Ms — Formulas

\begin{block}{GAM}
$$g(E[y]) = \beta_0 + \sum_j f_j(x_j)$$
\end{block}

\vspace{0.5cm}

\begin{block}{GA$^2$M (with pairwise interactions)}
$$g(E[y]) = \beta_0 + \sum_j f_j(x_j) + \sum_{i \neq j} f_{ij}(x_i, x_j)$$
\end{block}

\vspace{0.5cm}

\footnotesize
- $g$: link function — identity (regression) or $\log(E[y] / 1-E[y])$ (classification)
- $f_j$: shape function

---

# Intelligibility and Accuracy

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/intelligibility_accuracy_table.png}
\end{center}

[@lou2012intelligible]

---

# Shape Functions — Learning

- **Regression Splines**
- **Trees**
- **Ensembles of Trees**

\vspace{0.5cm}

\begin{block}{Learning GA$^2$Ms}
\begin{enumerate}
  \item Represent each component as a spline or regression tree on a single/pair of features
  \item Gradient boosting with bagging of shallow trees
  \item Build GAM first, then detect and rank all possible pairs of interactions in the residual
  \item Choose top $k$ pairs (determined by CV)
\end{enumerate}
\end{block}

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
\includegraphics[width=0.75\columnwidth]{imgs/pneumonia_features.png}
\end{center}

---

# Pneumonia Risk: AUC Results

\begin{center}
\includegraphics[width=0.6\columnwidth]{imgs/pneumonia_auc_table.png}
\end{center}

\begin{exampleblock}{Result}
GAM (0.8542) and GA$^2$M (0.8576) \textbf{outperform Random Forests (0.8460) and LogitBoost (0.8493)}, while remaining intelligible.
\end{exampleblock}

---

# Understanding Outputs of GA$^2$M (1/2)

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/ga2m_outputs_1.png}
\end{center}

\footnotesize
\textbf{Blood Urea Nitrogen (BUN):} Normal value: 10–20. \quad 0 means not ordered.

---

# Understanding Outputs of GA$^2$M (2/2)

\begin{center}
\includegraphics[width=0.55\columnwidth]{imgs/ga2m_age_cancer.png}
\end{center}

\begin{alertblock}{Insight}
Childhood cancers are associated with \textbf{high risk of death} from pneumonia.
\end{alertblock}

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

\begin{center}
\includegraphics[width=0.6\columnwidth]{imgs/readmission_auc_table.png}
\end{center}

\begin{exampleblock}{Result}
GA$^2$M (0.7833) matches LogitBoost (0.7835) and outperforms Random Forests (0.7671), while remaining fully interpretable.
\end{exampleblock}

---

# Patient Level Insights (1/2)

\begin{center}
\includegraphics[width=0.55\columnwidth]{imgs/patient_insights_1.png}
\end{center}

\begin{alertblock}{High Risk Patient — $p(\text{risk}) = 0.9326$}
Lots of admissions $\cdot$ Received lot of Amoxicillin (strep/pneumonia) $\cdot$ Verapamil (hypertension)
\end{alertblock}

---

# Patient Level Insights (2/2)

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/patient_insights_2.png}
\end{center}

\begin{columns}
\begin{column}{0.48\textwidth}
\begin{alertblock}{$p(\text{risk}) = 0.9326$}
Lots of admissions, Amoxicillin, Verapamil
\end{alertblock}
\end{column}
\begin{column}{0.48\textwidth}
\begin{exampleblock}{$p(\text{risk}) = 0.0873$}
Post-menopausal $\cdot$ Cancers responding well to treatment $\cdot$ Not hospitalized much
\end{exampleblock}
\end{column}
\end{columns}

---

# Modularity of GAMs

\begin{block}{Model Decomposition}
$$\text{prediction} = \underbrace{\beta_0}_{\text{bias}} + \underbrace{\sum_j f_j(x_j)}_{\text{individual features}} + \underbrace{\sum_{i \neq j} f_{ij}(x_i, x_j)}_{\text{pairwise interactions}}$$
\end{block}

\vspace{0.5cm}

This structure helps us **clearly understand the model**: for each patient, we can compute which term is resulting in what risk score and rank terms based on their contribution.

---

# Feature Shaping vs. Expert Discretization

\begin{columns}
\begin{column}{0.48\textwidth}
\begin{block}{Expert Discretization}
Experts provide inputs by manually discretizing features, used in logistic regression.
\end{block}
\end{column}
\begin{column}{0.48\textwidth}
\begin{exampleblock}{GAM Feature Shaping}
GAMs \textbf{learn} the function shapes automatically — and outperformed expert-discretized LR.
\end{exampleblock}
\end{column}
\end{columns}

\vspace{0.5cm}

\begin{alertblock}{Conclusion}
Feature shaping is \textbf{valuable} — GAMs captured non-linearities that experts missed.
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

# Prototype-Based Approaches

\begin{center}
\Huge Prototype-Based Approaches
\end{center}

---

# Deep Learning for Case-Based Reasoning through Prototypes

\begin{center}
\includegraphics[width=0.45\columnwidth]{imgs/prototypes_title.png}
\end{center}

\begin{center}
\large \textcolor{red}{Deep Learning for Case-Based Reasoning through Prototypes}

\vspace{0.3cm}
\normalsize Oscar Li, Hao Liu, Chaofan Chen, Cynthia Rudin
\end{center}

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
