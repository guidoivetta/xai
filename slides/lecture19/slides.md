---
title: "\\emoji{magnifying-glass-tilted-left} XAI: Input Gradients \\& Privacy Risks"
bibliography: references.bib

---

# Disclaimer

\input{../disclaimer.tex}

---

# Paper 1: Do Input Gradients Highlight Discriminative Features?

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/diffroar_title.png}
\end{center}

[@shah2021gradients]

---

# Do Attribution Methods Work?

\begin{alertblock}{Central Question}
Do input gradient attribution methods actually highlight features that drive model predictions?
\end{alertblock}

- Attribution methods assign **importance scores** to input features
- Common assumption: higher gradient magnitude $\Rightarrow$ higher feature contribution
- But... how do we *rigorously evaluate* this?

\vspace{0.5em}

\begin{block}{Challenge}
Existing evaluations are often qualitative or rely on synthetic benchmarks — lacking a principled framework
\end{block}

---

# Assumption (A)

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/diffroar_assumption.png}
\end{center}

\begin{definition}{}
\textbf{Assumption (A):} For model $f$ and input $x$, feature $i$ is more important than $j$ if $|\nabla_{x_i} f(x)| > |\nabla_{x_j} f(x)|$
\end{definition}

This assumption underlies most gradient-based XAI methods.

---

# Key Contributions

\begin{exampleblock}{DiffROAR: a new evaluation framework}
Systematically evaluate whether attribution methods highlight truly discriminative features via retrain-and-compare
\end{exampleblock}

- **Multiple benchmarks**: SVHN, FashionMNIST, CIFAR-10, ImageNet-10
- **BlockMNIST**: controlled dataset isolating discriminative vs.\ spurious features
- **Feature Leakage Hypothesis**: theoretical explanation for when attribution *appears* to work
- **Theorem**: formal characterization of feature leakage conditions

[@shah2021gradients]

---

# Related Work

\begin{columns}
\begin{column}{0.48\textwidth}
**Sanity Checks** (Adebayo et al.)

- Randomize model weights or labels
- Attribution must change accordingly

**Fidelity-based Evaluation**

- Mask top features, measure accuracy drop
- Single-pass (no retraining)
\end{column}
\begin{column}{0.48\textwidth}
**Adversarial Robustness**

- Attribution fragility under adversarial perturbations

\vspace{0.5em}

\begin{alertblock}{Limitation of Prior Work}
No evaluation establishes whether top-attributed features are truly \textit{discriminative} for model predictions
\end{alertblock}
\end{column}
\end{columns}

---

# DiffROAR Framework

---

# Setting

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/diffroar_framework.png}
\end{center}

**Pipeline:** train $f$ on $D$ $\to$ compute attribution $A(f,x)$ $\to$ mask top-$k$ or bot-$k$ features $\to$ **retrain** $\to$ measure accuracy

\begin{alertblock}{Key: Retraining}
Retraining (not just masking) avoids distribution shift artefacts in the evaluation
\end{alertblock}

---

# Unmasking Schemes

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/diffroar_unmasking.png}
\end{center}

Three strategies for replacing masked features:

- **Random**: replace with random noise
- **Meaningful**: replace with in-distribution values (e.g., blurred pixel)
- **Constant**: replace with a fixed value (e.g., zero)

---

# Predictive Power \& DiffROAR Metric

**Predictive Power** ($\text{PredPower}_k$): test accuracy of a model retrained with only the top-$k$ (or bot-$k$) features preserved

\begin{definition}{}
$$\text{DiffROAR} = \text{PredPower}(\text{top-}k) - \text{PredPower}(\text{bot-}k)$$
\end{definition}

\begin{center}
\includegraphics[width=0.65\columnwidth]{imgs/diffroar_metric.png}
\end{center}

\begin{exampleblock}{Interpretation}
DiffROAR $\gg 0$: top-$k$ features are more discriminative than bot-$k$ (attribution works) \\
DiffROAR $\approx 0$: attribution performs at random level
\end{exampleblock}

---

# Experiment 1: Image Classification

---

# Experimental Setup

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/diffroar_procedure.png}
\end{center}

**Datasets:** SVHN, FashionMNIST, CIFAR-10, ImageNet-10

**Attribution methods:** Integrated Gradients, Gradient $\times$ Input, SmoothGrad, GradCAM, Random Baseline

**5-step procedure:** train $\to$ attribute $\to$ mask top/bot-$k$ $\to$ retrain $\to$ compute DiffROAR

---

# Results: Benchmark Datasets

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/diffroar_results.png}
\end{center}

\begin{alertblock}{Surprising Finding}
Most attribution methods yield DiffROAR $\approx 0$ on standard benchmarks — they perform no better than a \textbf{random feature selector}
\end{alertblock}

---

# Experiment 2: BlockMNIST

---

# BlockMNIST Dataset

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/diffroar_blockmnist.png}
\end{center}

- Two MNIST digits placed **side by side**
- **Relevant digit**: correlated with class label
- **Spurious digit**: uncorrelated with label
- A good attribution method should highlight the **relevant** digit

---

# "Not Always!"

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/diffroar_not_always.png}
\end{center}

\begin{exampleblock}{On BlockMNIST}
Attribution methods \textit{can} achieve positive DiffROAR — they appear to correctly identify the relevant digit
\end{exampleblock}

But... **why** do they work here and not on natural images?

---

# Feature Leakage Hypothesis

\begin{center}
\includegraphics[width=0.78\columnwidth]{imgs/diffroar_feature_leakage.png}
\end{center}

\begin{alertblock}{Feature Leakage}
In BlockMNIST, relevant and spurious features are \textbf{spatially separated}. Gradients highlight the relevant region simply because the model "looks there" — not because they understand semantics.
\end{alertblock}

- Success on BlockMNIST reflects **dataset structure**, not method quality
- This leakage structure can be formalized theoretically

---

# Theoretical Analysis: Feature Leakage

---

# Theorem 1: Feature Leakage

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/diffroar_theorem1.png}
\end{center}

\begin{block}{Theorem 1 (Informal)}
If a dataset has a feature leakage structure (relevant and spurious features are linearly separable in input space), then any model trained on it will produce input gradients that concentrate on the relevant features — regardless of whether those features are used for prediction.
\end{block}

---

# Empirical Validation

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/diffroar_empirical.png}
\end{center}

- DiffROAR on BlockMNIST **correlates with degree of feature leakage**
- As relevant/spurious features overlap more (leakage decreases), DiffROAR drops
- Confirms the theoretical prediction

[@shah2021gradients]

---

# Conclusions: DiffROAR

\begin{columns}
\begin{column}{0.48\textwidth}
\begin{alertblock}{Negative Result}
Input gradient methods do \textbf{not} reliably highlight discriminative features on standard image benchmarks
\end{alertblock}

DiffROAR $\approx 0$ for most methods on SVHN, FashionMNIST, CIFAR-10, ImageNet-10
\end{column}
\begin{column}{0.48\textwidth}
\begin{exampleblock}{Key Nuance}
Feature leakage explains apparent successes:
\begin{itemize}
\item BlockMNIST works due to spatial separation
\item Not evidence of general semantic understanding
\end{itemize}
\end{exampleblock}
\end{column}
\end{columns}

---

# Discussion Questions: DiffROAR

1. DiffROAR requires **retraining** — is this a realistic evaluation paradigm in practice?
2. Does the feature leakage hypothesis generalize beyond synthetic datasets?
3. Can attribution methods be designed to be provably robust to feature leakage?
4. If attribution methods don't highlight discriminative features, what are they actually highlighting?

---

# Paper 2: On the Privacy Risks of Algorithmic Recourse

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/privacy_title.png}
\end{center}

[@pawelczyk2022privacy]

---

# Privacy Risks in XAI

\begin{alertblock}{Central Question}
Can XAI mechanisms — specifically \textbf{algorithmic recourse} — leak private information about training data?
\end{alertblock}

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/privacy_motivation.png}
\end{center}

---

# Algorithmic Recourse

**Context:** a rejected loan applicant receives actionable steps to get approved

$$x' = \arg\min_{x' \in \mathcal{A}^p} \ell(f_\theta(x'), 1) + \lambda \cdot c(x, x')$$

- $x'$: counterfactual (the recourse)
- $c(x, x')$: cost/distance from $x$ to $x'$
- $\mathcal{A}^p$: set of actionable features

\begin{definition}{}
\textbf{CFD (Counterfactual Distance):} $c(x, x')$ — distance from input $x$ to its recourse $x'$
\end{definition}

\begin{block}{Key Observation}
The CFD output by recourse algorithms may reveal whether $x$ was in the training set
\end{block}

---

# Previous Works

\begin{center}
\includegraphics[width=0.72\columnwidth]{imgs/privacy_mi_attribution.png}
\end{center}

\begin{columns}
\begin{column}{0.48\textwidth}
**MI via Feature Attribution**
- Shokri et al.: attribute $\to$ infer membership
- Requires **multiple queries**
\end{column}
\begin{column}{0.48\textwidth}
**Model Extraction via Counterfactuals**
- Repeated counterfactual queries
- Also requires **many queries**

\begin{alertblock}{Limitation}
Prior attacks assume multiple queries — impractical for real recourse systems
\end{alertblock}
\end{column}
\end{columns}

---

# Contributions

\begin{exampleblock}{Novel Contribution}
First \textbf{single-query} membership inference (MI) attack using counterfactual distances
\end{exampleblock}

1. **CFD Thresholding Attack**: simple threshold on counterfactual distance
2. **CFD LRT Attack**: likelihood ratio test using shadow models (more powerful)
3. **Theoretical bounds**: DP-based upper bounds on adversary success
4. **Empirical evaluation**: diverse datasets (Adult, HELOC, Diabetes) and recourse methods (SCFE, GS, CCHVAE)

[@pawelczyk2022privacy]

---

# MI Attacks: Background

**Classic Membership Inference:**

- $M_\text{Loss}$: MEMBER if $\ell(f(x), y) < \tau$ \quad (training samples have lower loss)
- **Loss LRT** (Carlini et al.): likelihood ratio test using shadow models — more powerful

\begin{center}
\includegraphics[width=0.72\columnwidth]{imgs/privacy_mi_game.png}
\end{center}

---

# Recourse-based MI Game

**Owner $O$** (model provider):

1. Trains $f_\theta$ on training set $S$
2. Provides recourse $\mathcal{R}(x) \to x'$ when queried

**Adversary $\mathcal{A}$** (attacker):

1. Queries $\mathcal{R}(x)$ for target sample $x$
2. Receives CFD $= c(x, x')$
3. Predicts: is $x \in S$?

\begin{alertblock}{Single-Query Constraint}
The adversary can only query the recourse system \textbf{once} per sample — making this a realistic threat model
\end{alertblock}

---

# Intuition: Why CFD Works

\begin{center}
\includegraphics[width=0.78\columnwidth]{imgs/privacy_intuition.png}
\end{center}

\begin{block}{Intuition}
Training samples tend to be \textbf{further from the decision boundary} (the model fits them well). Their counterfactuals require a larger shift $\Rightarrow$ larger CFD.
\end{block}

\begin{columns}
\begin{column}{0.48\textwidth}
MEMBER $\to$ large CFD (far from boundary)
\end{column}
\begin{column}{0.48\textwidth}
NON-MEMBER $\to$ small CFD (closer to boundary)
\end{column}
\end{columns}

---

# Attack 1: CFD Thresholding

\begin{center}
\includegraphics[width=0.7\columnwidth]{imgs/privacy_attack1.png}
\end{center}

$$M_\text{Distance}(x) = \begin{cases} \text{MEMBER} & \text{if } c(x, x') \geq \tau_D \\ \text{NON-MEMBER} & \text{otherwise} \end{cases}$$

- Simple and practical: only requires the recourse output $c(x, x')$
- $\tau_D$ chosen to maximize balanced accuracy at a given FPR

---

# Attack 2: CFD Likelihood Ratio Test

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/privacy_cfd_lrt.png}
\end{center}

**Algorithm (CFD LRT):**

1. Train $k$ **shadow models** on random subsets of a reference dataset
2. Estimate $\hat{\mu}_\text{in}, \hat{\sigma}^2_\text{in}$ (member CFD distribution) via MLE
3. Estimate $\hat{\mu}_\text{out}, \hat{\sigma}^2_\text{out}$ (non-member CFD distribution) via MLE
4. Compute LRT statistic; threshold at $z_{1-\alpha}$

\begin{exampleblock}{Advantage}
Leverages distributional information from shadow models — more powerful than simple thresholding
\end{exampleblock}

---

# Privacy Bounds via Differential Privacy

\begin{center}
\includegraphics[width=0.78\columnwidth]{imgs/privacy_dp_theorem.png}
\end{center}

\begin{block}{Theorem 1}
If the model training mechanism is $\varepsilon$-DP, then for any MI adversary $\mathcal{A}$:
$$\text{BA}_\mathcal{A} \leq \frac{1}{2} + \frac{1 - e^{-\varepsilon}}{2}$$
\end{block}

\begin{alertblock}{DP is Not a Silver Bullet}
Small $\varepsilon$ bounds adversary success — but significantly degrades recourse quality (utility-privacy tradeoff)
\end{alertblock}

---

# Experimental Setup

\begin{columns}
\begin{column}{0.48\textwidth}
**Datasets:**

- Adult (income prediction)
- HELOC (credit risk)
- Diabetes
- Synthetic (controlled)
\end{column}
\begin{column}{0.48\textwidth}
**Recourse Methods:**

- SCFE
- GS (Growing Spheres)
- CCHVAE

**Baselines:** $M_\text{Loss}$ threshold, Loss LRT
\end{column}
\end{columns}

---

# Attack Efficiency: ROC Curves

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/privacy_roc.png}
\end{center}

\begin{exampleblock}{Key Takeaway}
CFD LRT consistently outperforms CFD Thresholding and $M_\text{Loss}$ baseline — counterfactual distances carry \textbf{strong membership signal}
\end{exampleblock}

---

# Effect of Feature Dimensionality

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/privacy_num_features.png}
\end{center}

\begin{alertblock}{Finding}
Higher-dimensional feature spaces $\Rightarrow$ greater MI attack success
\end{alertblock}

More features $\to$ richer counterfactual signal $\to$ more distinguishable CFD distributions

---

# Effect of Model Architecture

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/privacy_model_arch.png}
\end{center}

\begin{alertblock}{Finding}
More complex model architectures $\Rightarrow$ greater MI attack success
\end{alertblock}

Complex models memorize training data more strongly $\to$ larger margin for training samples $\to$ larger CFD gap

---

# Conclusion: Privacy Risks

\begin{columns}
\begin{column}{0.48\textwidth}
**Novel Attacks**

- Leverage recourses to infer training data membership
- MI attacks using counterfactual distances (**CFD**)
- \textbf{Single-query} — practical threat model
\end{column}
\begin{column}{0.48\textwidth}
**Evidence of Privacy Leakage**

- Recourse algorithms carry membership signal
- \textbf{Explainability-privacy tradeoff} is real
- Attacks effective across diverse domains (lending, healthcare, law)
\end{column}
\end{columns}

---

# Limitations

- CFD is only a **heuristic** — an approximation of distance to the decision boundary
- Single-query assumption (adversary can only query once per sample)
- Must assume adversary knows the optimal threshold maximizing TPR at fixed FPR
- Paper highlights the **problem**, not yet a **solution**
- Evaluated on binary classification tasks only

---

# Future Work

- **Generalization**: can recourse lead to reconstruction attacks or attacks on training data statistics?
- **Other XAI mechanisms**: which other explanation methods involve privacy violations?
- **Solutions to protect privacy**: train models that provide recourse while mitigating privacy risks
  - How to construct faithful explanations that don't leak training data?
  - What is the privacy-utility trade-off?

[@pawelczyk2022privacy]

---

# Discussion Questions: Privacy Risks

1. Given the explainability-privacy tradeoff, what is the role of **ML practitioners** vs.\ **end users** in setting explainability and privacy benchmarks?
2. Both privacy and explainability cultivate user *trust* in ML models. In what situations would you prioritize one pillar over the other?
3. Besides recourse, what other XAI mechanisms might lead to privacy violations?
4. Is it even possible to have **private explanations**? Is this worth pursuing?

---

\begin{center}
\Huge Thank You!
\end{center}

---

# References {.allowframebreaks}

\footnotesize
