---
title: "\\emoji{wtf} XAI: Practitioner Interpretability Needs"
bibliography: references.bib

---

# Disclaimer

\input{../disclaimer.tex}

---

# Overview

## The Gap in Interpretable ML Research

- **Current Focus: (of 2023)** 
   - Developing new interpretable models and explanation methods
- **Much Less Explored:**
   - How useful are these tools actually to users?
   - Do practitioners effectively use interpretability tools?

---

# Papers

1. **Human Factors in Model Interpretability** by Hong et al.
   - Industry practitioners' needs and uses for interpretability

2. **Interpreting Interpretability: Understanding Data Scientists' Use of Interpretability Tools for Machine Learning** by Kaur et al.
   - How practitioners actually use interpretability tools

## These papers explore:

- How do ML practitioners use interpretability tools?
- What are their unmet needs?
- Do interpretability tools actually help practitioners understand models?

---

# Paper 1

\begin{center}
\includegraphics[width=.8\columnwidth]{imgs/paper1.png}
\end{center}

[@hong2020human]

## Key Contributions:

1. Conducts interview study to understand industry practitioners' existing needs and uses for interpretability
2. Presents findings on roles, stages, and goals related to interpretability
3. Identifies aspects of interpretability under-supported by existing technical solutions

---

# Research Motivation

\begin{center}
\includegraphics[width=1.0\columnwidth]{imgs/researcher_practitioner_gap.png}
\end{center}


---

# Methodology: Qualitative Study

- Useful for exploratory research
- Can generate hypotheses to test quantitatively

\vspace{2em}

## Study Design:

- **Type:** Semi-structured interviews
- **Participants:** 22 from convenience and snowball sampling
- **Analysis:** Qualitative coding
   - Iteratively build up a set of codes
   - Look at data and compare notes with other annotators

---

# Results: Three Dimensions

\begin{columns}
\begin{column}{0.5\textwidth}

\begin{itemize}
\item \textbf{Interpretability Roles:} Who needs interpretability?

\item \textbf{Interpretability Stages:}
   When is interpretability needed?

\item \textbf{Interpretability Goals:}
   Why is interpretability needed?
\end{itemize}

\end{column}
\begin{column}{0.5\textwidth}
\begin{center}
\includegraphics[width=.65\columnwidth]{imgs/dimensions.png}
\end{center}
\end{column}
\end{columns}

---

# Results Dimension: Interpretability Roles

\begin{center}
   \large
   \textbf{What methods are designed for different roles?}
\end{center}

\vspace{20pt}

\begin{columns}
\begin{column}{0.5\textwidth}

\textbf{Three Primary Roles:}
\vspace{10pt}
\begin{enumerate}
    \item \textbf{Model Builders} -- Create and develop ML models
    \item \textbf{Model Breakers} -- Test and validate models
    \item \textbf{Model Consumers} -- Use model outputs for decision-making
\end{enumerate}

\end{column}
\begin{column}{0.5\textwidth}
\begin{center}
\includegraphics[width=.65\columnwidth]{imgs/roles.png}
\end{center}
\end{column}
\end{columns}


---

# Results Dimension: Interpretability Roles


\begin{columns}
\begin{column}{0.5\textwidth}
\begin{itemize}
    \item \textbf{Model Builders}
    \begin{itemize}
        \item Debug models, identify edge cases, and compare model versions
        \item Communicate how models work to gain organizational trust
    \end{itemize}
    \item \textbf{Model Breakers}
    \begin{itemize}
        \item Verify legal compliance and validate predictions against domain knowledge
        \item Identify spurious correlations and provide improvement feedback
    \end{itemize}
    \item \textbf{Model Consumers}
    \begin{itemize}
        \item Need actionable explanations for decisions
        \item Require justifications when models contradict expertise and evidence for high-stakes choices
    \end{itemize}
\end{itemize}
\end{column}
\begin{column}{0.5\textwidth}
\begin{center}
\includegraphics[width=.65\columnwidth]{imgs/roles.png}
\end{center}
\end{column}
\end{columns}


---

# Results Dimension: Interpretability Stages

\begin{center}
   \large
   \textbf{What methods are designed for different stages?}
\end{center}

\vspace{20pt}

\begin{columns}
\begin{column}{0.5\textwidth}

\textbf{Three Stages in ML Pipeline:}
\vspace{10pt}
\begin{enumerate}
    \item Ideation and conceptualization stage
    \item Building and validation stage
    \item Deployment, maintenance, and use stage
\end{enumerate}

\end{column}
\begin{column}{0.5\textwidth}
\begin{center}
\includegraphics[width=.75\columnwidth]{imgs/stages.png}
\end{center}
\end{column}
\end{columns}

---

# Results Dimension: Interpretability Stages

\begin{columns}
\begin{column}{0.65\textwidth}

\begin{enumerate}
    \item \textbf{Ideation and Conceptualization Stage}
    \begin{itemize}
        \item Feature engineering with interpretability in mind and collaboration with domain experts
        \item Working with auditors to ensure compliance and write model white papers
    \end{itemize}
    \item \textbf{Building and Validation Stage}
    \begin{itemize}
        \item Testing edge cases, examining feature importance, and comparing model versions
        \item Communicating model behavior to stakeholders to gain trust
    \end{itemize}
    \item \textbf{Deployment, Maintenance, and Use Stage}
    \begin{itemize}
        \item Monitoring models and performing root cause analysis when issues arise
        \item Providing explanations to end-users for high-stakes decisions and knowledge discovery
    \end{itemize}
\end{enumerate}

\end{column}
\begin{column}{.35\textwidth}
\begin{center}
\includegraphics[width=\columnwidth]{imgs/stages.png}
\end{center}
\end{column}
\end{columns}

---

# Results Dimension: Interpretability Goals


\begin{center}
   \large
   \textbf{What methods are designed for different goals?}
\end{center}

\vspace{20pt}

\begin{columns}
\begin{column}{0.5\textwidth}

\textbf{Three Primary Goals:}
\vspace{10pt}
\begin{enumerate}
    \item \textbf{Model Validation and Improvement} --- Debugging and enhancing model performance
    \item \textbf{Decision Making and Knowledge Discovery} --- Using models to gain insights
    \item \textbf{Gaining Confidence and Obtaining Trust} --- Building confidence in model predictions
\end{enumerate}

\end{column}
\begin{column}{0.5\textwidth}
\begin{center}
\includegraphics[width=.65\columnwidth]{imgs/goals.png}
\end{center}
\end{column}
\end{columns}


---

# Results Dimension: 27 combinations

\begin{center}
\includegraphics[width=.75\columnwidth]{imgs/full_dims.png}
\end{center}

---

# Three Key Themes: 1 Interpretability is Cooperative

**Communication is Central:**

   - Important for communicating with domain experts and stakeholders
   - Facilitates trust, sometimes just by virtue of including an explanation

\begin{center}
\includegraphics[width=0.45\columnwidth]{imgs/team_collaboration.png}
\end{center}

\begin{center}
   \large
   \textbf{Better tools vs. better data science training for communication?}
\end{center}

---

# Three Key Themes: 1 Interpretability is Cooperative

\vspace{1em}
\begin{center}
   \large
   \textbf{Better tools vs. better data science training for communication?}
\end{center}
    
:::: {.columns}
::: {.column width="48%"}
### Better Tools

- Advanced visualization systems
- Automated explanation methods
- Interactive debugging interfaces
:::

::: {.column width="48%"}
### Better Training

- Communication skills development
- Stakeholder empathy building
- Cross-functional collaboration
:::
::::

::: {.block}
### Key Finding
Interpretability are often **communication problems between people**, not just technical person-model alignment issues.
:::

\begin{center}
\includegraphics[width=0.20\columnwidth]{imgs/vs.png}
\end{center}


---

# Three Key Themes: 2 Interpretability is a Process

**Continuous Engagement:**

- Important across many different stages of the ML pipeline
- Dialogue with the model for continued use
- Not a one-time activity


---

# Three Key Themes: 3 Mental Model Comparison

\vspace{1em}
**Understanding User Needs:**

- Understanding what end-users need is important
- Translating human hypotheses into ML models

\begin{center}
\includegraphics[width=0.55\columnwidth]{imgs/mental_model_comparison.png}
\end{center}

---

# Three Key Themes: 4 Context-Dependent 

**Tailored Explanations:**

- Good explanations depend on the user
- How detailed should it be?
- What skepticism will they bring to it?

\begin{center}
\includegraphics[width=0.87\columnwidth]{imgs/context_dependent.png}
\end{center}



---

# Three Key Themes: 4 Context-Dependent 

\vspace{1em}
\begin{center}
   \large
   \textbf{Effective explanations must be tailored to the specific user and context:}
\end{center}

:::: {.columns}
::: {.column width="48%"}
### Key Considerations

- **User expertise level** --- Technical depth varies by role
- **Actionability** --- What can users actually change?
- **Domain context** --- Healthcare ≠ Finance ≠ Manufacturing
:::

::: {.column width="48%"}
### Critical Questions

- How detailed should explanations be?
- What skepticism will users bring?
- Which features are meaningful to them?
:::
::::

::: {.block}
### Example
Doctors need explanations tied to **actionable treatments**, not just top features. 

A feature ranking without clinical context provides no value.
:::

---

# Design Opportunities Identified

**Four Key Areas for Improvement:**

1. **Integrating Human Expectations**
   - Better incorporate domain knowledge

2. **Communicating and Summarizing Behavior**
   - Clearer communication of model behavior

3. **Scalable and Integratable Tools**
   - Tools that work at scale in production

4. **Post-Deployment Support**
   - Ongoing interpretability after deployment


---

# In other words


\begin{center}
\includegraphics[width=0.6\columnwidth]{imgs/bsotwbresc.png}

\textbf{
\href{https://www.software.ac.uk/}{Software Sustainability Institute\\https://www.software.ac.uk/}}
\end{center}


---

# Let's try to understand other people mental models

\begin{center}
\includegraphics[width=.95\columnwidth]{imgs/paper1end.png}
\end{center}

---

# Paper 2

\vspace{1em}
\begin{center}
\includegraphics[width=.65\columnwidth]{imgs/paper2.png}
\end{center}

[@kaur2020interpreting]

## Key Contributions:

1. Evaluates whether interpretability tools help ML practitioners understand models

2. Contextual inquiry and survey of how practitioners use ML tools

3. Finds that data scientists **over-trust** and **misuse** interpretability tools

---

# Research Question

\includegraphics[width=.9\columnwidth]{imgs/paper2_research_question.png}

---

# Methodology Overview: Three-Phase Study

\begin{enumerate}
\item \textbf{\textit{Stage 1} -- Pilot Interviews} (N = 6)
   \begin{itemize}
   \item Identified issues to test in contextual inquiry
   \end{itemize}

\item \textbf{\textit{Stage 2} -- Contextual Inquiry} (N = 11)
   \begin{itemize}
   \item Can users find issues when given standard tools?
   \end{itemize}

\item \textbf{\textit{Stage 3} -- Survey} (N = 197)
   \begin{itemize}
   \item Validate and quantify findings in large sample
   \end{itemize}
\end{enumerate}

---

# Stage 1: Pilot Interviews

\vspace{1em}
\begin{center}
   \large
   \textbf{Objective:} Identify common issues faced by data scientists in their day-to-day ML work
\end{center}


## Method

- **N = 6** data scientists from large tech company
- **Semi-structured interviews** (~40 minutes each)
- **Analysis:** Inductive thematic analysis (open coding + affinity diagramming)


---

# Stage 1: Pilot Interviews - Common Issues

\begin{center}
\includegraphics[width=0.99\columnwidth]{imgs/common_issues_table.png}
\vspace{1em}
\textbf{These 6 issues were synthetically injected into the dataset for Stages 2 \& 3}
\end{center}

---

# Stage 2: Contextual Inquiry

**Objective:** Observe whether data scientists can use interpretability tools to **uncover** the injected issues


## Participants & Setup
- **N = 11** participants (ML researchers, data scientists, interns)
- **Dataset:** Adult Income (1994 census) - synthetically manipulated
- **Tools:** GAMs (n=6) or SHAP (n=5) - randomly assigned
- **Format:** Jupyter notebooks with tutorials

---

# Stage 2: Contextual Inquiry -- Tools Used

**Two Popular Interpretability Tools:**

## GAMs (Generalized Additive Models)
**Glassbox model** that decomposes predictions into additive components—one per feature—that can each be visualized as a non-linear function. Inherently interpretable by design; no post-hoc explanation needed.

## SHAP (SHapley Additive exPlanations)
**Post-hoc explanation technique** for blackbox models that assigns importance scores to features based on Shapley values from game theory. Explains any model's predictions by computing each feature's contribution to moving the prediction from a baseline.

---

# Stage 2: Contextual Inquiry -- Tools Used

\begin{center}
\includegraphics[width=1.0\columnwidth]{imgs/gam_shap_visualizations.png}
\end{center}

---

# Stage 2: Contextual Inquiry -- Results

- **Misuse:** Over-trusted tools due to visualizations
  - *"Age 38... the explanation clearly shows it... makes sense"* (P9)
- **Rationalization:** Used tools to justify suspicious observations
  - *"Test of means says same as SHAP about Age. All's good!"* (P8)
- **Social context:** Trusted because tools are public/popular
- **Misleading visualizations:** Different axis scales caused errors


---


# Stage 3: Large Scale Survey

**Objective:** Observe whether data scientists can use interpretability tools to **uncover** the injected issues


## Study Design

\vspace{2pt}

- **Type:** Survey based on example queries from previous tools
- **Participants:** 197 from mailing list of large tech company
- **Analysis:**
  - Coded open-ended responses
  - Statistical tests to compare outcomes by condition


---

# Stage 3: Large Scale Survey -- Experimental Conditions

\vspace{0.5cm}

\begin{columns}
\begin{column}{0.5\textwidth}
\textbf{Explanation Type}
\begin{itemize}
\item GAM
\item SHAP
\end{itemize}
\end{column}

\begin{column}{0.5\textwidth}
\textbf{Visualization Type}
\begin{itemize}
\item Normal (correct)
\item Manipulated (obviously wrong)
\end{itemize}
\end{column}
\end{columns}

\vspace{5pt}

\begin{alertblock}{Key Question}
\begin{center}
\large
\textbf{Do people trust obviously wrong explanations less?}
\includegraphics[width=0.5\columnwidth]{imgs/godzilla.png}
\end{center}
\end{alertblock}

---

# Stage 3: Large Scale Survey -- # Result 1:

\begin{center}
\textbf{Performance with Explanations}
\end{center}

**Key Findings:**

- **GAM >> SHAP**
  - GAM users performed significantly better

- **Better results with good explanations than manipulated**
  - But effect was smaller than expected

\vspace{0.5cm}

\begin{alertblock}{Implication}
\begin{center}
\large
\textbf{People don't always detect obviously flawed explanations}
\end{center}
\end{alertblock}

---

# Stage 3: Large Scale Survey -- Result 2:

\begin{center}
\textbf{How Practitioners Make Deployment Decisions}
\end{center}

1. **Intuition-Based Decisions**
   - Made decisions based on gut feeling

2. **Superficial Justification**
   - Used explanations to justify pre-existing beliefs

3. **Critical Examination (Some)**
   - Small group used tools as intended

\vspace{0.5cm}

\begin{alertblock}{Design Challenge}
\begin{center}
\large
\textbf{How to push people towards deliberative reasoning?}
\end{center}
\end{alertblock}

---

# Stage 3: Large Scale Survey -- # Result 3:

\begin{center}
\textbf{Mental Models of Tools} \\
\textbf{Understanding vs. Confidence}
\end{center}


- Participants largely **did not understand tools well**
- Despite that, they **believed tools effective** for many uses

\vspace{0.5cm}

\begin{alertblock}{Critical Question}
\begin{center}
\large
\textbf{Is it bad for explanations to persuade people without understanding?}
\end{center}
\end{alertblock}


---

# Stage 3: Large Scale Survey -- Result 4:

\begin{center}
\textbf{Experience Paradox} \\
\textbf{The Experience-Confidence Trade-off}
\end{center}

- More ML background → Better understanding of explanations
- More ML experience → Less confidence in explanations
- Less confidence → Lower willingness to deploy

\vspace{0.5cm}

\begin{alertblock}{Challenge}
\begin{center}
\large
How do we make ML explanations more accessible without sacrificing quality?
\end{center}
\end{alertblock}

---

# Discussion and Implications 1/3

## Key Takeaways from Both Papers

\begin{columns}
\begin{column}{0.5\textwidth}
\textbf{Paper 1: What Users Need}
\begin{itemize}
\item Cooperative interpretability
\item Process-oriented tools
\item Context-dependent explanations
\item Post-deployment support
\end{itemize}
\end{column}

\begin{column}{0.5\textwidth}
\textbf{Paper 2: How Tools Perform}
\begin{itemize}
\item Over-trust is common
\item Misuse is frequent
\item Better tools needed
\item Training is essential
\end{itemize}
\end{column}
\end{columns}

---

# Discussion and Implications 2/3

## Critical Questions for Discussion

1. **Better tools vs. better training?**
   - Should we focus on improving tools or educating users?

2. **Persuasion without understanding?**
   - Is it problematic if explanations convince without comprehension?

3. **Accessibility vs. sophistication?**
   - How to make tools accessible without oversimplifying?

4. **Role-specific design?**
   - Should we design different tools for different roles?

---

# Discussion and Implications 3/3

## Implications for Interpretability Research

**Research Directions:**

- Design tools with specific user roles and stages in mind
- Account for social and organizational context
- Provide safeguards against misuse
- Balance complexity with accessibility
- Support continuous engagement throughout ML lifecycle

---

# Open Research Questions

1. How can we design interpretability tools that are both powerful and accessible?

2. What interventions can reduce over-trust in explanations?

3. How should interpretability tools adapt to different user expertise levels?

4. What role should organizational culture play in interpretability tool design?

5. How can we better evaluate whether tools actually help users?

---

# Conclusion

**Main Messages:**

- Interpretability tools are widely used but often misused
- Gap exists between what researchers build and what practitioners need
- Context, role, and stage matter significantly
- User training is as important as tool design
- Much work remains to bridge research and practice

---

\begin{center}
\Huge Thank You!

\vspace{1cm}

\Large Questions and Discussion
\end{center}

---

# References {.allowframebreaks}

\footnotesize