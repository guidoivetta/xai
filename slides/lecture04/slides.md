---
title: "\\emoji{wtf} XAI: Evaluating Interpretability"
bibliography: references.bib
---

# Disclaimer

\input{../disclaimer.tex}

---

# Evaluating Interpretability

**CS 282 BR Topics in Machine Learning:**  
**Interpretability and Explainability**

Ike Lage  
02/01/2023

---

# Overview

- Evaluating interpretability in the interpretable ML community:
  - Interpretability depends on human experience of the model
  - Disagreement about the best way to measure it
- These papers:
  - Evaluating factors related to interpretability through user studies

---

# Other Relevant Fields

- **Human-Computer Interaction (HCI):**
  - Theories for how people interact with technology
- **Psychology:**
  - Theories for how people process information
- **Both** have thought carefully about experimental design

---

# Outline

- Research paper: "Human Evaluation of Models Built for Interpretability" by Lage et al.
- Research paper: "Manipulating and Measuring Model Interpretability" by Poursabzi-Sangdeh et al.
- Discussion

---

# Paper 1

---

# Human Evaluation of Models Built for Interpretability

**Isaac Lage, Emily Chen, Jeffrey He, Menaka Narayanan,**  
**Been Kim, Samuel J. Gershman, Finale Doshi-Velez**

<!-- \includegraphics[width=0.8\columnwidth]{imgs/paper1_title.png} -->

---

# Contributions

## Research Questions:

- Which types of decision set complexity most affect human-simulatability?
- Is relationship between complexity and human-simulatability context dependent?

## Approach:

- Large scale, carefully controlled user studies

---

# Decision Sets

- Logic-based models are often considered interpretable
- Many approaches for learning them from data

<!-- \includegraphics[width=0.9\columnwidth]{imgs/decision_sets_example.png} -->

---

# Regularizers

- There are many ways to regularize decision sets that make them **less complex**
- What kinds of complexity is it **most urgent to regularize** to learn interpretable models?

\vspace{1cm}

\begin{columns}
\begin{column}{0.3\textwidth}
**Choose a regularizer for interpretability**
\end{column}
\begin{column}{0.3\textwidth}
**Optimize With regularizer**
\end{column}
\begin{column}{0.3\textwidth}
**Interpretable Model?**
\end{column}
\end{columns}

---

# Types of Complexity

- **Model size**: Number of rules/lines in the decision set
- **Variable repetitions**: Same variable appearing multiple times
- **Cognitive chunks**: Number of distinct logical conditions

<!-- \includegraphics[width=0.85\columnwidth]{imgs/complexity_types.png} -->

\vspace{0.5cm}

What if we optimized the models with data?

---

# Context: Domains

\begin{columns}
\begin{column}{0.48\textwidth}
<!-- \includegraphics[width=\columnwidth]{imgs/alien_food.png} -->

**Low Risk:** Alien meal recommendation
\end{column}
\begin{column}{0.48\textwidth}
<!-- \includegraphics[width=\columnwidth]{imgs/alien_medical.png} -->

**High Risk:** Alien medical prescription
\end{column}
\end{columns}

\vspace{1cm}

\begin{alertblock}{Design Question}
What if we used 2 different real domains?
\end{alertblock}

---

# Context: Tasks

\begin{columns}
\begin{column}{0.48\textwidth}
<!-- \includegraphics[width=\columnwidth]{imgs/decision_set_tasks.png} -->
\end{column}
\begin{column}{0.48\textwidth}
- **Simulation:**
  - What would the model recommend the alien?
- **Verification:**
  - Is *milk and guava* a correct recommendation?
- **Counterfactual:**
  - If *patient* were replaced with *sleepy*, would the correctness of the *milk and guava* recommendation change?
\end{column}
\end{columns}

\vspace{0.5cm}

What if we used more realistic tasks?

---

# Tradeoff Between Control and Generalizability

- Tradeoff between the ability to tightly control the experiment and running it under realistic conditions (generalizability)

\vspace{1cm}

\begin{center}
\textbf{Tightly controlled} $\longleftrightarrow$ \textbf{Realistic}

\vspace{0.5cm}

\textcolor{blue}{\textbf{This paper}}
\end{center}

---

# Procedure

- Experiment posted on Mturk
- Takes around 20 minutes
- Participants paid 3 USD
- Excluded participants who could not complete practice questions
- Total: 50-70 participants out of 150

\vspace{1cm}

\begin{center}
Instructions $\rightarrow$ 3-6 practice questions $\rightarrow$ 15-18 test questions $\rightarrow$ Payment code
\end{center}

---

# Statistical Analysis: Linear Model

We use a linear model for each metric in each experiment:

- Response time
- Accuracy
- Satisfaction

## Example – Model Size, Response Time:

- **Step 1:** Fit linear regression to predict response time from number of lines and number of output terms
- **Step 2:** Interpret coefficients as effects of number of lines and number of output terms on response time

---

# Statistical Analysis: Multiple Hypothesis Testing

<!-- \includegraphics[width=0.9\columnwidth]{imgs/xkcd_hypothesis.png} -->

## We use a Bonferroni correction

- Instead of p < 0.05, use:  
  **p < (0.05 / # comparisons)**

---

# Results: Complexity Increases Response Time

**Recipe Domain**

<!-- \includegraphics[width=0.7\columnwidth]{imgs/complexity_response_time.png} -->

\vspace{1cm}

\begin{exampleblock}{Key Finding}
Greater complexity results in longer response time for all kinds of complexity
\end{exampleblock}

---

# Results: Type of Complexity Matters

\begin{center}
\textbf{Response time for: cognitive chunks > model size > repeated terms}
\end{center}

<!-- \includegraphics[width=0.85\columnwidth]{imgs/complexity_comparison_table.png} -->

- **Model size:** Significant in one domain
- **Cognitive chunks:** Significant in all domains
- **Variable repetitions:** Significant in neither domain

---

# Results: Consistency - Domains, Tasks, Metrics

Results consistent across domains, tasks and the response time and subjective difficulty metrics

<!-- \includegraphics[width=0.7\columnwidth]{imgs/consistency_results.png} -->

\begin{exampleblock}{Example}
Similar effect sizes, both statistically significant across different experimental conditions
\end{exampleblock}

---

# Results: Counterfactuals Are Hard

The counterfactual task is much more challenging than simulation!

<!-- \includegraphics[width=0.75\columnwidth]{imgs/counterfactual_difficulty.png} -->

\vspace{0.5cm}

\begin{alertblock}{Key Finding}
In all experiments, counterfactual tasks require longer response time than simulation tasks
\end{alertblock}

---

# Discussion: Paper 1

- Consistent guidelines for interpretability
- Simplified tasks to measure interpretability
- Using Mturk workers as a proxy for domain experts

\vspace{1cm}

\begin{center}
\textbf{Key Takeaway:} Different types of complexity affect human-simulatability differently, with cognitive chunks having the strongest effect
\end{center}

---

# Paper 2

---

# Manipulating and Measuring Model Interpretability

**Forough Poursabzi-Sangdeh, Daniel G. Goldstein, Jake M. Hofman**  
**Jennifer Wortman Vaughan, Hanna Wallach**

Microsoft Research

<!-- \includegraphics[width=0.8\columnwidth]{imgs/paper2_title.png} -->

---

# Motivation

- Interpretability as a latent property that can be manipulated or measured indirectly
- What are the factors through which it can be manipulated effectively?
- Bring HCI methods to interpretable ML since interpretability is defined by user experience

---

# Contributions

## Research Questions:

- How well can people estimate what a model will predict?
- How much do people trust a model's predictions?
- How well can people detect when a model has made a sizable mistake?

## Approach:

- Large-scale, pre-registered user studies to answer these questions in the context of linear regression models

---

# Comparison to Paper 1

- Studies **linear regression models** instead of decision sets
- Measures people's ability to make their **own predictions** in addition to forward simulation
- Uses **real-world housing dataset** and models optimized with data

---

# Ways to Manipulate Interpretability

\begin{columns}
\begin{column}{0.48\textwidth}
<!-- \includegraphics[width=\columnwidth]{imgs/clear_2_features.png} -->

\textbf{CLEAR-2:} 2 features, transparent
\end{column}
\begin{column}{0.48\textwidth}
<!-- \includegraphics[width=\columnwidth]{imgs/blackbox_2_features.png} -->

\textbf{BB-2:} 2 features, black-box
\end{column}
\end{columns}

\vspace{0.5cm}

\begin{columns}
\begin{column}{0.48\textwidth}
<!-- \includegraphics[width=\columnwidth]{imgs/clear_8_features.png} -->

\textbf{CLEAR-8:} 8 features, transparent
\end{column}
\begin{column}{0.48\textwidth}
<!-- \includegraphics[width=\columnwidth]{imgs/blackbox_8_features.png} -->

\textbf{BB-8:} 8 features, black-box
\end{column}
\end{columns}

\vspace{0.5cm}

**Two manipulations:** Number of Features & Transparency

---

# Procedure

- Participants shown:
  - **Training:** 10 apartments
  - **Testing:** 12 apartments (this is the data they use)
- Participants paid 2.5 USD
- 750-1,250 participants per experiment

\vspace{1cm}

\begin{center}
\textbf{Each Trial:}

Forward simulate model's prediction $\rightarrow$ View model's true prediction $\rightarrow$ Make own prediction
\end{center}

---

# Statistical Analysis: Participant Specific Effects

## A repeated measures experimental design

- Each participant makes many predictions
- Use a **mixed-effects model** to control for correlations between a participant's responses
- Assumes a random, participant-specific effect

---

# Statistical Analysis: Multiple Hypothesis Testing

- **Pre-registering hypotheses** corresponds to deciding and publishing which analyses you will run **before collecting data**
- Reduces the probability that effects were discovered by chance

\vspace{1cm}

\begin{exampleblock}{Example}
\texttt{https://aspredicted.org/xy5s6.pdf}

"We will use 2-by-2 ANOVA for statistical analysis of the effect of number of features and model clarity on final deviation from model's prediction and simulation error."
\end{exampleblock}

---

# Design Choices

- Randomized the order of the first 10 (normal) apartments and fixed the order of the last 2 (unusual)
- All participants are shown an identical set of apartments
- Each participant completed a single condition (between subjects design)

\vspace{1cm}

\begin{center}
\begin{tabular}{cc}
\textbf{Fix sources of randomness} & \textbf{Randomize as much as possible} \\
Can introduce bias & Increases variance \\
\end{tabular}
\end{center}

---

# Results: Simulating Small, Transparent Models

**Experiment 1: New York City prices**

<!-- \includegraphics[width=0.7\columnwidth]{imgs/simulation_error_nyc.png} -->

\vspace{1cm}

\begin{exampleblock}{Key Finding}
Best simulation accuracy with small, transparent models (CLEAR-2)
\end{exampleblock}

---

# Results: No Difference in Trust or Prediction

**Experiment 1: New York City prices**

\begin{columns}
\begin{column}{0.48\textwidth}
<!-- \includegraphics[width=\columnwidth]{imgs/deviation_results.png} -->

\textbf{Trust (Deviation)}
\end{column}
\begin{column}{0.48\textwidth}
<!-- \includegraphics[width=\columnwidth]{imgs/prediction_error.png} -->

\textbf{Prediction Error}
\end{column}
\end{columns}

\vspace{1cm}

\begin{alertblock}{Key Finding}
None of the conditions are statistically different for trust or prediction error
\end{alertblock}

---

# Results: Clear Models Make Mistakes Worse

**Experiment 1: New York City prices - Apartment 12 (1 bed, 3 bath)**

<!-- \includegraphics[width=0.7\columnwidth]{imgs/deviation_unusual.png} -->

\vspace{0.5cm}

\begin{alertblock}{Surprising Finding}
Participants deviate \textit{less} from the bad prediction with clear models (CLEAR-2, CLEAR-8)

Higher deviation is better - means people are catching the error!
\end{alertblock}

---

# Additional Experiments

## Experiment 2: Scaled Prices

- Scaled down prices to better reflect national average
- **Same results** for simulation accuracy

---

# Additional Experiments (cont.)

## Experiment 3: Better Trust Metrics

- Scaled down prices to better reflect national average
- Better trust metrics
- **No significant difference in trust between models**

---

# Additional Experiments (cont.)

## Experiment 4: Attention Check

- Attention check for unusual features
- **People catch more errors** when explicitly asked to look for unusual inputs

---

# Discussion: Paper 2

Key findings from the experiments:

- Highlighting weird inputs helps catch errors
- Having people predict before seeing the model helped catch errors
- **Transparency actually makes people worse at catching errors**

\vspace{1cm}

\begin{alertblock}{Counterintuitive Result}
More interpretable models (transparent, fewer features) led to worse error detection on unusual cases
\end{alertblock}

---

# General Discussion

## Comparing Both Papers:

- **Paper 1:** Decision sets, controlled synthetic domains, cognitive complexity matters
- **Paper 2:** Linear models, real-world data, transparency can backfire

\vspace{1cm}

## Key Lessons:

- Interpretability is multifaceted and context-dependent
- User studies are essential for evaluating interpretability
- Simplified models ≠ always better decision-making
- Different tasks require different evaluation metrics

---

\begin{center}
\Huge Thank You!
\end{center}