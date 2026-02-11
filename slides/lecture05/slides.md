---
title: "\\emoji{wtf} XAI: Rule Based Approaches"
bibliography: references.bib
---

# Disclaimer

\input{../disclaimer.tex}

---

# Paper 1

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/paper1_title.png}
\end{center}

[@letham2015interpretable]

---

# Contributions

- Introducing a generative model called \textbf{Bayesian Rule Lists (BRL)}
  - Goal is to output a decision list (\texttt{if then else-lif})

- Novel prior structure to \textbf{encourage sparsity}

  - "Sparse" means the model has few active elements
  - Instead of using all possible rules, BRL keeps only a few that are sufficiently expressive.
  - Truncated Poisson priors over list length (λ) and rule complexity (η) encourage \textit{sparse}, \textit{interpretable} decision lists.

- Predictive accuracy \textbf{on par} with top classic algorithms (RF, SVM, CHADS$_2$)

---

# Decision List: Titanic Example

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/decision_list_example.png}
\end{center}

- This **is one of many** accurate and interpretable decision lists that can be learned from the data — BRL captures this uncertainty by maintaining a posterior distribution over all of them.
- **Each rule fires in order** — the first matching rule determines the prediction. 
- A male adult in 1st class gets **21%**, not **96%**, because the first rule takes priority.
- The values in parentheses are **95% credible intervals** — the narrower, the more data behind that rule.

---

# Implementing a Decision List in Python

```python
>>> def predict_survival(male, adult, passenger_class):
...     if male and adult:
...         return 0.21, (0.19, 0.23)
...     elif passenger_class == 3:
...         return 0.44, (0.38, 0.51)
...     elif passenger_class == 1:
...         return 0.96, (0.92, 0.99)
...     return 0.88, (0.82 , 0.94)
...     
>>> survival, confidence = predict_survival(True, False, 3)
>>> survival
0.44
>>> confidence
(0.38, 0.51)
```

---
# Introduction: BRL

- Produces \textbf{a posterior distribution over permutations of \textit{if.. then.. Else-if...} rules} from a large set of \textbf{pre-mined rules} with FP-Growth (*Frequent Pattern Growth*, is an algorithm for mining frequent itemsets from data.).

- Decision lists with \textbf{high posterior probability tend to be both accurate and interpretable}
  - \textbf{Prior} favors concise lists with small number of rules and fewer terms in left hand side

---

# Introduction: BRL

- New type of \textbf{balance} between accuracy, interpretability, and computation

- \textbf{What about using other similar models}?
  - Decision trees (CART)
  - They employ greedy construction methods
  - Not particularly computationally demanding but affects quality of solution -- both accuracy and interpretability

---

# Pre-mined Rules

- A major source of practical feasibility: \textbf{pre-mined rules}
  - Reduces model space
  - Complexity of problem depends on number of pre-mined rules

- As long as pre-mined set is expressive, \textbf{accurate decision list can be found} + smaller model space means \textbf{better generalization} (Vapnik, 1995)

---

# Pre-mined Rules: Intuition

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/premined_rules_intuition.png}
\end{center}

- So the final candidate antecedents passed to BRL would be: \{2\}, \{3\}, \{4\}, \{2,3\}, \{2,4\}, \{3,4\}.

- This is Apriori algorithm. FP-growth is a single pass algorithm (more efficient).

---

# Preliminaries: Notation

- Training data $\{(x_i, y_i)\}_{i=1}^{n}$, $x_i \in \mathbb{R}^d$, $y_i \in \{1, \ldots, L\}$

$$\mathbf{x} = (x_1, \ldots, x_n) \quad \mathbf{y} = (y_1, \ldots, y_n)$$

## Two labels: 

1. stroke
2. no stroke

---

# Warning

\begin{center}
\Large
\emoji{desktop-computer.png}
\emoji{warning.png}
\textcolor{red}{Warning}
\textcolor{lightgreen}{
for students with a background in computer science}
\normalsize
\end{center}
\vspace{1em}

- **Intuition:** Bayesians use probability distributions like programmers use libraries (`numpy`, `sklearn`). Instead of building new theory from scratch, they pick standard distributions that fit their problem and update them with data.

- **Formally:** You encode prior beliefs using these distributions *before* seeing data, then combine them with observations via Bayes' theorem to get the posterior. The 'library' gives you the mathematical machinery, but you still need to choose the right prior and let the data update it.


---

# Bayesian Decision Lists

\begin{center}
\includegraphics[width=0.6\columnwidth]{imgs/bayesian_decision_lists.png}
\end{center}

\small
## Where:
\begin{itemize}
    \item $a_j$: Antecedent (the "if" condition) for rule $j$
    \item $y \sim \text{Multinomial}(\boldsymbol{\theta}_j)$: The predicted label follows a multinomial distribution with probabilities $\boldsymbol{\theta}_j$
    \item $\boldsymbol{\theta}_j \sim \text{Dirichlet}(\boldsymbol{\alpha} + \mathbf{N}_j)$: The parameters $\boldsymbol{\theta}_j$ themselves have a posterior distribution (Dirichlet) that combines the prior pseudocounts $\boldsymbol{\alpha}$ with the observed data counts $\mathbf{N}_j$
    \item $\boldsymbol{\alpha}$: Prior pseudocounts (hyperparameter). Setting $\boldsymbol{\alpha} = (1,1,\ldots,1)$ gives a uniform prior with no class preference
    \item $\mathbf{N}_j = (N_{j,1}, \ldots, N_{j,L})$: Counts of observations captured by rule $j$ for each of the $L$ classes
\end{itemize}
\normalsize

---

# Preliminaries: Sampling from a multinomial

The code simulates throwing a 6-sided die 20 times, where each face has equal probability 1/6.

```python
>>> import numpy as np
>>> np.random.multinomial(20, [1/6]*6, size=1) 
array([[4, 1, 7, 5, 2, 1]])
```

- `[1/6] * 6` = `[1/6, 1/6, 1/6, 1/6, 1/6, 1/6]`
- returns how many times each face appeared:  means face 1 appeared 4 times, face 2 once, face 3 seven times, etc.

## Parameters are probability values

- $\theta_j$, in BRL, is  a vector of probabilities, one per class. For example, $\theta_j = [0.6, 0.3, 0.1]$ for a 3-class problem.
- When you sample a label y from Multinomial($\theta_j$), you're drawing one outcome according to those probabilities.

---

# Preliminaries: Dirichlet Distribution

- **Dirichlet samples from this simplex:** Drawing from $Dirichlet(\alpha_1, \alpha_2$ gives probability vectors like (0.6, 0.4) or (0.3, 0.7)

- **Probability simplex:** The space of all valid probability vectors (sum to 1, non-negative)
  - Example: (0.6, 0.4) is valid; (0.6, 0.5) is not (sums to 1.1)

- **K-dimensional Dirichlet has k parameters $(\alpha_1, \alpha_2, ..., \alpha_m)$**
  - Each $\alpha_k$ controls expected probability mass for dimension $k$
  - Higher $\alpha_k$ → more weight on that dimension
  - All $\alpha_k = 1$ → uniform distribution over the simplex

\begin{columns}
\begin{column}{0.48\textwidth}
\begin{center}
 $$\Theta \sim \text{Dirichlet}(\alpha_1, \alpha_2, \ldots, \alpha_m)$$
 \end{center}
\end{column}
\begin{column}{0.48\textwidth}
\begin{center}
$$P(\theta_1, \theta_2, \ldots, \theta_m) = \frac{\Gamma(\sum_k \alpha_k)}{\prod_k \Gamma(\alpha_k)} \prod_{k=1}^{m} \theta_k^{\alpha_k - 1}$$
\end{center}
\end{column}
\end{columns}


---

# Preliminaries: Dirichlet Prior

- Conjugate prior for multinomial distribution

- Conjugate prior: posterior in the same family as prior

- Prior:

$$(p_1, \ldots, p_k) \sim \text{Dirichlet}(\alpha_1, \ldots, \alpha_k)$$

- Posterior:

$$(p_1, \ldots, p_k) | (x_1, \ldots, x_k) \sim \text{Dirichlet}(\alpha_1 + x_1, \ldots, \alpha_k + x_k)$$

Conjugado (conjugate):
Un prior es "conjugado" cuando el posterior tiene la misma forma matemática que el prior. Esto hace que los cálculos bayesianos sean simples — no necesitás integrales complicadas.

Verosimilitud (likelihood):
Es la probabilidad de observar tus datos dado un modelo. Por ejemplo: si tenés un dado y observás 100 tiros, la verosimilitud te dice qué tan probable es ver esos resultados si el dado tiene ciertos parámetros.

Para datos multinomiales:

Prior: Las probabilidades (p₁, ..., pₖ) siguen Dirichlet(α₁, ..., αₖ)
Datos observados: Contás cuántas veces apareció cada categoría: (x₁, ..., xₖ)
Posterior: Sigue siendo Dirichlet, pero con parámetros actualizados: Dirichlet(α₁ + x₁, ..., αₖ + xₖ)


Por qué importa para BRL:
Literalmente sumás las observaciones a los pseudoconteos del prior. Si tenías α = (1,1,1) y observaste (5,2,3) datos, tu posterior es Dirichlet(6,3,4). Esta actualización limpia permite que BRL calcule posteriors eficientemente para cada regla.

---

# Bayesian Association Rules

$$a \to y \sim \text{Multinomial}(\boldsymbol{\theta}). \qquad \boldsymbol{\theta} | \boldsymbol{\alpha} \sim \text{Dirichlet}(\boldsymbol{\alpha}).$$

$$\boldsymbol{\theta} | \mathbf{x}, \mathbf{y}, \boldsymbol{\alpha} \sim \text{Dirichlet}(\boldsymbol{\alpha} + N)$$

$$N = (N_{\cdot,1}, \ldots, N_{\cdot,L})$$

---

# Generative Model

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/generative_model.png}
\end{center}

Our goal is to sample from the posterior distribution over antecedent lists:

$$p(d|\mathbf{x}, \mathbf{y}, \mathcal{A}, \boldsymbol{\alpha}, \lambda, \eta) \propto p(\mathbf{y}|\mathbf{x}, d, \boldsymbol{\alpha}) p(d|\mathcal{A}, \lambda, \eta).$$

$\mathcal{A}$ is complete collection of pre-mined antecedents

---

# Prior Probabilities

$$p(d|\mathcal{A}, \lambda, \eta) = p(m|\mathcal{A}, \lambda) \prod_{j=1}^{m} p(c_j|c_{<j}, \mathcal{A}, \eta) p(a_j|a_{<j}, c_j, \mathcal{A}).$$

Truncated Poisson:

$$p(m|\mathcal{A}, \lambda) = \frac{(\lambda^m / m!)}{\sum_{j=0}^{|\mathcal{A}|}(\lambda^j / j!)}, \qquad m = 0, \ldots, |\mathcal{A}|.$$

Ensures that sampled values are within bounds!

Also, ensures expected value is close to $\lambda$ when there are a large number of pre-mined rules

---

# Prior Probabilities

Another Truncated Poisson,

$$p(c_j|c_{<j}, \mathcal{A}, \eta) = \frac{(\eta^{c_j} / c_j!)}{\sum_{k \in R_{j-1}(c_{<j}, \mathcal{A})}(\eta^k / k!)}, \qquad c_j \in R_{j-1}(c_{<j}, \mathcal{A}).$$

$p(a_j|a_{<j}, c_j, \mathcal{A})$ is sampled uniformly from available antecedents with appropriate cardinality.

---

# Likelihood

- Likelihood is the product of multinomial probability mass functions for the observed label counts at each rule

$$p(\mathbf{y}|\mathbf{x}, d, \boldsymbol{\theta}) = \prod_{j: \sum_l N_{j,l} > 0} \text{Multinomial}(\mathbf{N}_j | \theta_j),$$

$$\theta_j \sim \text{Dirichlet}(\boldsymbol{\alpha}).$$

Marginalize over $\theta_j$, integrate out the intermediate parameter $\theta_j$

---

# Markov Chain Monte Carlo

- Generate a chain of random samples until convergence

- Each random sample is a stepping stone for the next one (chain)

- New samples do not depend on any samples before the previous one (Markov)

---

# Markov Chain Monte Carlo

- How to go to (optimal) $d^*$ from current $d^t$

- Move an antecedent to a different position in the list

- Add an antecedent that is not currently in the list

- Remove an antecedent from the list

---

# Metropolis Hastings

- Start with a random decision list

- Choose a move based on "proposal distribution" Q

- After you choose your move, you compute an acceptance probability A

- Generate a random number u

- If $u \leq A$, then accept; otherwise reject

---

# Metropolis Hastings

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/metropolis_hastings_algorithm.png}
\end{center}

---

# Proposal Probabilities

- Move chosen uniformly

- Which antecedents and their new position is also chosen uniformly

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/proposal_probabilities.png}
\end{center}

---

# Estimating label of a new observation

$$p(\tilde{y} = l | \tilde{x}, d, \mathbf{x}, \mathbf{y}, \alpha) = \frac{\alpha_l + N_{j(d,\tilde{x}),l}}{\sum_{k=1}^{L}(\alpha_k + N_{j(d,\tilde{x}),k})}.$$

Match the antecedent by looking at feature values of new observation

---

# Experiments

---

# Tic-Tac-Toe

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/tictactoe_results.png}
\end{center}

5 fold cross validation; accuracy computed across 5 folds

---

# Stroke Prediction

- N = 12,586, 14% had stroke
- 6000 times larger than data for CHADS2 score
- Pre-mining: support 10% and max cardinality 2
- 5 fold evaluation

---

# Stroke Prediction

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/stroke_prediction_rules.png}
\end{center}

---

# Stroke Prediction

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/stroke_prediction_more.png}
\end{center}

---

# Stroke Prediction - AUC

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/stroke_prediction_auc.png}
\end{center}

---

# Paper 2

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/paper2_title.png}
\end{center}

[@lakkaraju2016interpretable]

---

# Contributions

- A framework called \textbf{Interpretable Decision Sets} (IDS) for classification

- \textbf{Novel objective function} + proof of \textbf{submodularity}

- Optimization procedure with optimality guarantees

- \textbf{Detailed metrics for evaluating interpretability} + user studies

---

# Motivation

- Traditional classification models optimize for predictive accuracy

- Very little understanding of the model itself and its predictions

- Model being "readable" is not enough

- \textbf{Humans should be able to reason about predictions and readily explain the functionality of the model}

---

# Decision Lists vs Decision Sets

## Decision Lists

- Ordered sequence of if-then-else rules
- Order matters: first matching rule applies
- Like a chain of if/else-if statements

## Decision Sets

- Unordered collection of if-then rules
- Each rule independently assigns a class
- Rules can overlap (multiple rules may fire)

---

# Decision Sets

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/decision_sets_example.png}
\end{center}

---

# Criteria for Interpretability

- \textbf{Parsimony}: Fewer rules with fewer conditions
  - Cognitive limits of human understanding

- \textbf{Distinctness}: Minimal overlap of rules w.r.t the data points they cover
  - No redundant and contradicting explanations of data points

- \textbf{Class Coverage}: Explain all the classes in the data
  - Rules explaining minority classes are important

---

# Problem Formulation

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/problem_formulation.png}
\end{center}

---

# Desiderata

- We need to optimize for the following criteria
  - Recall
  - Precision
  - Distinctness
  - Parsimony
  - Class Coverage

- Recall and Precision $\Rightarrow$ Accurate predictions

- Distinctness, Parsimony, and Class Coverage $\Rightarrow$ Interpretability

---

# Objective Function

## Parsimony

- Fewer rules: $f_1(\mathcal{R}) = |\mathcal{S}| - \text{size}(\mathcal{R})$

- Fewer predicates: $f_2(\mathcal{R}) = L_{\max} \cdot |\mathcal{S}| - \sum_{r \in \mathcal{R}} \text{length}(r)$

---

# Objective Function

## Distinctness

- Intra-class overlap:

$$f_3(\mathcal{R}) = N \cdot |S|^2 - \sum_{\substack{r_i, r_j \in \mathcal{R} \\ i \leq j \\ c_i = c_j}} \text{overlap}(r_i, r_j)$$

- Inter-class overlap:

$$f_4(\mathcal{R}) = N \cdot |S|^2 - \sum_{\substack{r_i, r_j \in \mathcal{R} \\ i \leq j \\ c_i \neq c_j}} \text{overlap}(r_i, r_j)$$

---

# Objective Function

## Class Coverage

$$f_5(\mathcal{R}) = \sum_{c' \in \mathcal{C}} \mathbf{1}\left(\exists r = (s, c) \in \mathcal{R} \text{ such that } c = c'\right)$$

Check if there exists some rule corresponding to a given class $c$

---

# Objective Function

## Precision

- Minimize "incorrect" covers:

$$f_6(\mathcal{R}) = N \cdot |\mathcal{S}| - \sum_{r \in \mathcal{R}} |\text{incorrect-cover}(r)|$$

Given a rule $r = (s, c)$, the number of data points which satisfy $s$ but do not belong to class $c$.

---

# Objective Function

## Recall

- Encourage at least one "correct" cover per data point:

$$f_7(\mathcal{R}) = \sum_{(\mathbf{x}, y) \in \mathcal{D}} \mathbf{1}\left(|\{r | (\mathbf{x}, y) \in \text{correct-cover}(r)\}| \geq 1\right)$$

Given a rule $r = (s, c)$, the number of data points which satisfy $s$ and belong to class $c$.

---

# Objective Function

- Complete objective is

$$\underset{\mathcal{R} \subseteq \mathcal{S} \times \mathcal{C}}{\text{argmax}} \sum_{i=1}^{7} \lambda_i f_i(\mathcal{R})$$

- The intra-class and inter-class overlap terms are non-monotone
- The parsimony, overlap, and precision terms are non-normal
- All the component terms are submodular

---

# Submodularity

\textbf{\textcolor{red}{Diminishing returns} characterization}

$$F(A \cup d) - F(A) \geq F(B \cup d) - F(B)$$

\begin{columns}
\begin{column}{0.48\textwidth}
Gain of adding $d$ to a small set
\end{column}
\begin{column}{0.48\textwidth}
Gain of adding $d$ to a large set
\end{column}
\end{columns}

\vspace{1em}

\begin{alertblock}{Key Property}
A non-negative linear combination of submodular functions is submodular
\end{alertblock}

---

# Objective Function

- Complete objective is

$$\underset{\mathcal{R} \subseteq \mathcal{S} \times \mathcal{C}}{\text{argmax}} \sum_{i=1}^{7} \lambda_i f_i(\mathcal{R})$$

\begin{alertblock}{Result}
The complete objective is non-negative, non-normal, non-monotone, submodular
\end{alertblock}

---

# Optimizing the Objective

- Maximizing a non-monotone submodular function is \textbf{NP-hard}

- \textbf{Smooth local search} [SLS] algorithm provides a 2/5 approximation [Feige, Mirrokni, Vondrak FOCS 07; SIAM Comp. J. 11]
  - Will be at least 2/5 of the optimal solution

---

# Submodular Maximization: Local Search

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/local_search_1.png}
\end{center}

S and S' correspond to the intermediate solution sets

---

# Submodular Maximization: Local Search

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/local_search_2.png}
\end{center}

S and S' correspond to the intermediate solution sets

---

# Submodular Maximization: Local Search

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/local_search_3.png}
\end{center}

S and S' correspond to the intermediate solution sets

---

# Submodular Maximization: Local Search

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/local_search_4.png}
\end{center}

S and S' correspond to the intermediate solution sets

---

# Submodular Maximization: Local Search

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/local_search_5.png}
\end{center}

S and S' correspond to the intermediate solution sets

---

# Submodular Maximization: Local Search

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/local_search_6.png}
\end{center}

S and S' correspond to the intermediate solution sets

---

# Submodular Maximization: Local Search

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/local_search_7.png}
\end{center}

S and S' correspond to the intermediate solution sets

---

# Local Search

- ~1/3 approximation
  - At least 1/3 of optimal solution

- we use a slightly different version of this algorithm
  - Smooth local search
  - 2/5 approximation

---

# Smooth Local Search

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/smooth_local_search_algorithm.png}
\end{center}

---

# Evaluation: Datasets

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/evaluation_datasets.png}
\end{center}

---

# Evaluating Predictive Performance

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/predictive_performance.png}
\end{center}

---

# Evaluating Goodness of Rules

- Results on Medical Diagnosis Data

\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/goodness_of_rules.png}
\end{center}

---

# Ablation Study

- Results on Medical Diagnosis Data

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/ablation_study.png}
\end{center}

---

\begin{center}
\Huge Thank You!
\end{center}

---

# References {.allowframebreaks}

\footnotesize
