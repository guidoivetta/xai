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

**Three Primary Roles:**

1. **Model Builders**
   - Create and develop ML models

2. **Model Breakers**
   - Test and validate models

3. **Model Consumers**
   - Use model outputs for decision-making

---

\begin{alertblock}{Design Question}
What methods are designed for different roles?
\end{alertblock}

## Interpretability Stages

**Three Stages in ML Pipeline:**

```
\begin{center}
\begin{tikzpicture}[node distance=2.5cm]
\node (fe) [rectangle, draw, minimum width=2.5cm, minimum height=1cm] {Feature Engineering};
\node (mb) [rectangle, draw, minimum width=2.5cm, minimum height=1cm, right of=fe] {Model Building};
\node (dep) [rectangle, draw, minimum width=2.5cm, minimum height=1cm, right of=mb] {Deployment};
\draw [->] (fe) -- (mb);
\draw [->] (mb) -- (dep);
\end{tikzpicture}
\end{center}
```

**Detailed Stages:**
- Ideation and conceptualization stage
- Building and validation stage
- Deployment, maintenance, and use stage

\begin{alertblock}{Design Question}
What methods are designed for different stages?
\end{alertblock}

## Interpretability Goals

**Three Primary Goals:**

1. **Model Validation and Improvement**
   - Debugging and enhancing model performance

2. **Decision Making and Knowledge Discovery**
   - Using models to gain insights

3. **Gaining Confidence and Obtaining Trust**
   - Building confidence in model predictions

\begin{alertblock}{Design Question}
What methods are designed for different goals?
\end{alertblock}

# Key Themes

## Theme 1: Interpretability is Cooperative

**Communication is Central:**
- Important for communicating with domain experts and stakeholders
- Facilitates trust, sometimes just by virtue of including an explanation

\includegraphics[width=0.6\columnwidth]{imgs/team_collaboration.png}

\vspace{1cm}

\begin{exampleblock}{Open Question}
Better tools vs. better data science training for communication?
\end{exampleblock}

## Theme 2: Interpretability is a Process

**Continuous Engagement:**
- Important across many different stages of the ML pipeline
- Dialogue with the model for continued use
- Not a one-time activity

## Theme 3: Mental Model Comparison

**Understanding User Needs:**
- Understanding what end-users need is important
- Translating human hypotheses into ML models

\includegraphics[width=0.7\columnwidth]{imgs/mental_model_comparison.png}

\vspace{0.5cm}

\begin{center}
Human Mental Model $\stackrel{?}{=}$ Model Logic
\end{center}

## Theme 4: Context-Dependent Interpretability

**Tailored Explanations:**
- Good explanations depend on the user
- How detailed should it be?
- What skepticism will they bring to it?

\includegraphics[width=0.7\columnwidth]{imgs/context_dependent.png}

\vspace{0.5cm}

**Different audiences require different approaches:**
- Technical vs. non-technical stakeholders
- Domain experts vs. general users

## Design Opportunities Identified

**Four Key Areas for Improvement:**

1. **Integrating Human Expectations**
   - Better incorporate domain knowledge

2. **Communicating and Summarizing Behavior**
   - Clearer communication of model behavior

3. **Scalable and Integratable Tools**
   - Tools that work at scale in production

4. **Post-Deployment Support**
   - Ongoing interpretability after deployment

# Paper 2: Interpreting Interpretability

## Interpreting Interpretability

**Understanding Data Scientists' Use of Interpretability Tools for Machine Learning**

**Authors:**
- Harmanpreet Kaur, Harsha Nori, Samuel Jenkins (University of Michigan)
- Rich Caruana, Hanna Wallach, Jennifer Wortman Vaughan (Microsoft Research)

## Research Question

\includegraphics[width=1.0\columnwidth]{imgs/paper2_research_question.png}

\begin{columns}
\begin{column}{0.45\textwidth}
\textbf{Interpretability Researchers}
\begin{itemize}
\item Create interpretability tools
\end{itemize}
\end{column}

\begin{column}{0.1\textwidth}
\begin{center}
\Large $\rightarrow$
\end{center}
\end{column}

\begin{column}{0.45\textwidth}
\textbf{ML Practitioners}
\begin{itemize}
\item Use interpretability tools
\end{itemize}
\end{column}
\end{columns}

\vspace{1cm}

\begin{alertblock}{Critical Question}
But do they actually work?
\end{alertblock}

## Study Contributions

**Key Findings:**

1. Evaluates whether interpretability tools help ML practitioners understand models

2. Contextual inquiry and survey of how practitioners use ML tools

3. Finds that data scientists **over-trust** and **misuse** interpretability tools

## Methodology Overview

**Three-Phase Study:**

\begin{enumerate}
\item \textbf{Pilot Interviews} (N = 6)
   \begin{itemize}
   \item Identified issues to test in contextual inquiry
   \end{itemize}

\item \textbf{Contextual Inquiry} (N = 11)
   \begin{itemize}
   \item Can users find issues when given standard tools?
   \end{itemize}

\item \textbf{Survey} (N = 197)
   \begin{itemize}
   \item Validate and quantify findings in large sample
   \end{itemize}
\end{enumerate}

## Pilot Study: Common Issues

\includegraphics[width=1.0\columnwidth]{imgs/common_issues_table.png}

\small

| **Theme** | **Description** |
|-----------|----------------|
| **Missing values** | Methods for dealing with missing values can cause biases or leakage |
| **Changes in data** | Data can change over time (e.g., new categories) |
| **Duplicate data** | Unclear naming conventions can lead to accidental duplication |
| **Redundant features** | Same feature in several ways distributes importance |
| **Ad-hoc categorization** | Arbitrary bins when converting continuous to categorical |
| **Debugging difficulties** | Identifying model improvements from small samples is difficult |

## Contextual Inquiry: Tools Used

**Two Popular Interpretability Tools:**

\includegraphics[width=1.0\columnwidth]{imgs/gam_shap_visualizations.png}

\begin{columns}
\begin{column}{0.5\textwidth}
\textbf{GAM (Generalized Additive Models)}
\begin{itemize}
\item Inherently interpretable model
\item Shows feature importance
\item Shape functions for each feature
\end{itemize}
\end{column}

\begin{column}{0.5\textwidth}
\textbf{SHAP (SHapley Additive exPlanations)}
\begin{itemize}
\item Post-hoc explanation method
\item Feature importance plots
\item Local and global explanations
\end{itemize}
\end{column}
\end{columns}

## Contextual Inquiry Results

**Key Findings:**

1. **Misuse and Disuse**
   - Participants struggled to use tools correctly

2. **Social Context is Important**
   - Organizational factors affect interpretability use

3. **Visualizations Can Be Misleading**
   - Participants misinterpreted visualizations

# Large Scale Survey

## Survey Methodology

**Study Design:**

- **Type:** Survey based on example queries from previous tools
- **Participants:** 197 from mailing list of large tech company
- **Analysis:**
  - Coded open-ended responses
  - Statistical tests to compare outcomes by condition

## Experimental Conditions

**Two Factors:**

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

\vspace{1cm}

\begin{alertblock}{Key Question}
Do people trust obviously wrong explanations less?
\end{alertblock}

## Result 1: Performance with Explanations

**Key Findings:**

- **GAM >> SHAP**
  - GAM users performed significantly better

- **Better results with good explanations than manipulated**
  - But effect was smaller than expected

\vspace{0.5cm}

\begin{block}{Implication}
People don't always detect obviously flawed explanations
\end{block}

## Result 2: Deployment Decisions

**How Practitioners Make Deployment Decisions:**

1. **Intuition-Based Decisions**
   - Made decisions based on gut feeling

2. **Superficial Justification**
   - Used explanations to justify pre-existing beliefs

3. **Critical Examination (Some)**
   - Small group used tools as intended

\vspace{0.5cm}

\begin{exampleblock}{Design Challenge}
How to push people towards deliberative reasoning?
\end{exampleblock}

## Result 3: Mental Models of Tools

**Understanding vs. Confidence:**

\includegraphics[width=0.6\columnwidth]{imgs/mental_models_results.png}

- Participants largely **did not understand tools well**
- Despite that, they **believed tools effective** for many uses

\vspace{1cm}

\begin{alertblock}{Critical Question}
Is it bad for explanations to persuade people without understanding?
\end{alertblock}

## Result 4: Experience Paradox

**The Experience-Confidence Trade-off:**

- More ML background → Better understanding of explanations
- More ML experience → Less confidence in explanations
- Less confidence → Lower willingness to deploy

\vspace{1cm}

\begin{exampleblock}{Challenge}
How do we make ML explanations more accessible without sacrificing quality?
\end{exampleblock}

# Discussion and Implications

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

## Critical Questions for Discussion

1. **Better tools vs. better training?**
   - Should we focus on improving tools or educating users?

2. **Persuasion without understanding?**
   - Is it problematic if explanations convince without comprehension?

3. **Accessibility vs. sophistication?**
   - How to make tools accessible without oversimplifying?

4. **Role-specific design?**
   - Should we design different tools for different roles?

## Implications for Interpretability Research

**Research Directions:**

- Design tools with specific user roles and stages in mind
- Account for social and organizational context
- Provide safeguards against misuse
- Balance complexity with accessibility
- Support continuous engagement throughout ML lifecycle

## Open Research Questions

1. How can we design interpretability tools that are both powerful and accessible?

2. What interventions can reduce over-trust in explanations?

3. How should interpretability tools adapt to different user expertise levels?

4. What role should organizational culture play in interpretability tool design?

5. How can we better evaluate whether tools actually help users?

## Conclusion

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