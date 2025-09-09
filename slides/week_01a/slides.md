---
title: "\\emoji{wtf} XAI: Understanding Course Foundations and Motivations"
author: "FAMAF - UNC"
date: \today
fontsize: 13pt
theme: "Boadilla"
colortheme: "dolphin"
aspectratio: 169
bibliography: references.bib
header-includes:
  - \definecolor{primarygreen}{HTML}{2E7D32}
  - \definecolor{lightgreen}{HTML}{558B2F}
  - \definecolor{darkgreen}{HTML}{1B5E20}
  - \setbeamercolor{frametitle}{fg=primarygreen}
  - \setbeamercolor{framesubtitle}{fg=primarygreen}
  - \setbeamercolor{title}{fg=primarygreen}
  - \setbeamercolor{structure}{fg=primarygreen}
  - \setbeamercolor{item}{fg=darkgreen}
  - \setbeamercolor{block title}{bg=lightgreen,fg=white}
  - \setbeamercolor{block body}{bg=lightgreen!20}
  - \setbeamerfont{bibliography item}{size=\footnotesize}
  - \setbeamerfont{bibliography entry author}{size=\footnotesize}
  - \setbeamerfont{bibliography entry title}{size=\footnotesize}
  - \setbeamerfont{bibliography entry location}{size=\footnotesize}
  - \setbeamerfont{bibliography entry note}{size=\footnotesize}
  - \usepackage{graphicx}
  - \titlegraphic{\includegraphics[width=4cm]{../../assets/logo.jpeg}}
  - \newcommand{\emoji}[1]{\raisebox{-0.1ex}{\includegraphics[height=0.8em]{../emojis/#1}}}
  - \newcommand{\here}{\textbf{\textcolor{red}{\Huge HASTA ACÁ LLEGUE!}}}
  - \newcommand{\wtf}[1]{"\textbf{#1} \emoji{wtf}"}
  - \renewcommand{\textbf}[1]{\textcolor{darkgreen}{\bf#1}}
  - \let\oldframetitle\frametitle
  - \renewcommand{\frametitle}[1]{\oldframetitle{\emoji{mate}~\texttt{#1~------}}}
---

# Disclaimer

## This course is based on

**Explainable Artificial Intelligence **

From Simple Predictors to Complex Generative Models
Spring 2023, Harvard University

https://interpretable-ml-class.github.io/

---

# Agenda

- Course Goals & Logistics
- Model Understanding: Use Cases
- Inherently Interpretable Models vs. Post-hoc Explanations
- Defining and Understanding Interpretability

---

# Goals of this Course

Learn and improve upon the state-of-the-art literature on ML interpretability and explainability:

- Understand where, when, and why is interpretability/explainability needed
- Read, present, and discuss research papers
- Formulate, optimize, and evaluate algorithms
- Implement state-of-the-art algorithms; Do research!
- Understand, critique, and redefine literature

**EMERGING FIELD!!**

---

# Course Overview

1. **Foundations and Human Factors** - definitions, taxonomies, and cognitive aspects
2. **Interpretability and Explainability Methods** - inherently interpretable models and post-hoc explanations
3. **Advanced Techniques and Evaluation** - attention-based explanations and quality metrics
4. **Interpretability of Large Models** - mechanistic interpretability and LLM understanding
5. **Emerging Frontiers of XAI** - automated circuit discovery and multimodal techniques

---

# Who should take this course?

- Course particularly tailored to students interested in **research** \emoji{test-tube} on interpretability/explainability

  - **Not a surface level course! \emoji{fire}**
  - **Not just applications! \emoji{fire}**

- Goal is to push you to question existing work and make new contributions to the field

---

# Class Format

- Course comprises of lectures, guests, and student presentations
- Each lecture will cover: at least 2 papers \emoji{page-facing-up} \emoji{page-facing-up}
- Students are **expected** to "at least" skim through the papers beforehand \emoji{yawning-face}
- Students will divide into groups

**Each breakout group is expected to come up with:**

- A list of 2 to 3 weaknesses of each of the works discussed
- Strategies for addressing those weaknesses

---

# Research Projects - AKA Final Exam

## Requirements

- Short research paper (max 4 pages)
- Teams of 2 students
- Target: Local conference submission

## Assessment

- Ongoing feedback from entire course
- Course approved when paper is submitted

---

# Background

**Understanding:**

- Linear algebra
- Probability
- Algorithms
- Machine learning
- Programming in Python, Numpy, Sklearn

**Familiarity with:**

- Statistics
- Optimization

---

# Motivation

**Machine Learning is EVERYWHERE!!**

\begin{center}
\includegraphics[width=.75\columnwidth]{imgs/motivation.png}
\end{center}


[@lipton2016mythos]

---

# Motivation: Why Model Understanding?


\begin{center}
\textbf{Example:} Image classification model
\includegraphics[width=.85\columnwidth]{imgs/husky0.png}
\end{center}

---

# Motivation: Why Model Understanding?


\begin{center}
\textbf{Example:} Image classification model
\includegraphics[width=.85\columnwidth]{imgs/husky1.png} \\
\textbf{\large Model understanding facilitates debugging}
\end{center}

---

# Motivation: Why Model Understanding?


\begin{center}
\textbf{Example:} Criminal justice risk assessment
\includegraphics[width=.90\columnwidth]{imgs/judge0.png}
\end{center}

[@lipton2016mythos]

---

# Motivation: Why Model Understanding?


\begin{center}
\textbf{Example:} Criminal justice risk assessment
\includegraphics[width=.90\columnwidth]{imgs/judge1.png} \\
\textbf{\large Model understanding facilitates bias detection}
\end{center}

[@lipton2016mythos]

---

# Motivation: Why Model Understanding?

\begin{center}
\textbf{Example:} Loan application system
\includegraphics[width=.70\columnwidth]{imgs/loan0.png}
\end{center}

---

# Motivation: Why Model Understanding?

\begin{center}
\textbf{Example:} Loan application system
\includegraphics[width=.70\columnwidth]{imgs/loan1.png} \\
\textbf{Model understanding helps provide recourse to individuals who are adversely affected by model predictions}
\end{center}


---


# Motivation: Why Model Understanding?

\begin{center}
\textbf{Example:} Medical diagnosis system
\includegraphics[width=.75\columnwidth]{imgs/trust0.png}
\end{center}

---

# Motivation: Why Model Understanding?

\begin{center}
\textbf{Example:} Medical diagnosis system
\includegraphics[width=.75\columnwidth]{imgs/trust1.png} \\
\textbf{Model understanding helps assess when to trust predictions}
\end{center}

---

# Motivation: Why Model Understanding?

\begin{center}
\textbf{Summary of Use Cases}\\
\includegraphics[width=.75\columnwidth]{imgs/sumarywhy0.png}
\end{center}

---

# Motivation: Why Model Understanding?

\begin{center}
\textbf{Summary of Use Cases}\\
\includegraphics[width=.75\columnwidth]{imgs/sumarywhy1.png}
\end{center}

---

# Achieving Model Understanding

\begin{center}
\textbf{Take 1:} Build inherently interpretable predictive models\\
\includegraphics[width=.95\columnwidth]{imgs/inherent.png}
\end{center}

[@letham2015interpretable; @lakkaraju2016interpretable]

---

# Achieving Model Understanding

\begin{center}
\textbf{Take 2:} Explain pre-built models in a post-hoc manner\\
\includegraphics[width=.90\columnwidth]{imgs/bbox.png}
\end{center}

[@ribeiro2016should; @lakkaraju2019interpretability; @ribeiro2018anchors]

---

# Inherently Interpretable Models vs. Post hoc Explanations


\begin{center}
\textbf{Accuracy-Interpretability Trade-offs}\\
\includegraphics[width=.90\columnwidth]{imgs/intvsacc.png}\\
\vspace{0.5cm}
{\large In certain settings, accuracy-interpretability trade offs may exist.}
\end{center}

(Cireşan et. al. 2012, Caruana et. al. 2006, Frosst et. al.  2017, Stewart 2020)

---

# Inherently Interpretable Models vs. Post hoc Explanations

\begin{center}
\textbf{Example scenarios:} Simple vs complex boundaries\\
\includegraphics[width=.85\columnwidth]{imgs/boundaries.png}\\
\vspace{0.5cm}
{\Large In certain settings, accuracy-interpretability trade offs may exist.}
\end{center}



---

# Inherently Interpretable Models vs. Post hoc Explanations

\begin{center}
\Large
\textbf{Sometimes, you don't have enough data to build your model from scratch.}
\vspace{0.5cm}
\textbf{And, all you have is a (proprietary) black box!}
\end{center}
\vspace{1cm}

[@ribeiro2016should]

---

# Inherently Interpretable Models vs. Post hoc Explanations

## Recommendation

\begin{center}
\textit{If you can build an interpretable model which is also adequately accurate for your setting,} \\
\vspace{0.5cm}
\textbf{\Large DO IT!} \\
\vspace{0.5cm}
\textit{Otherwise, \textbf{post hoc explanations} come to the rescue!}
\vspace{1cm}
\end{center}

---

# Inherently Interpretable Models vs. Post hoc Explanations

## Recommendation

\begin{center}
\textit{If you can build an interpretable model which is also adequately accurate for your setting,} \\
\vspace{0.5cm}
\textbf{\Large DO IT!} \\
\vspace{0.5cm}
\textit{Otherwise, \textbf{post hoc explanations} come to the rescue!} \\
\vspace{1cm}
{\Huge \textcolor{primarygreen}{Let’s get into some details!}}
\end{center}

---

# Next Up!

- Define and evaluate interpretability somewhat! \emoji{wtf}
- Taxonomy of interpretability evaluation
- Taxonomy of interpretability based on applications/tasks
- Taxonomy of interpretability based on methods

---

# Defining and Understanding Interpretability: Motivation for Interpretability

- ML systems are being deployed in complex **high-stakes settings**
- Accuracy alone is no longer enough
- **Auxiliary criteria are important:**
  - Safety
  - Nondiscrimination
  - Right to explanation

---

# Motivation for Interpretability (cont.)

- Auxiliary criteria are often **hard to quantify** (completely):
  - E.g.: Impossible to enumerate all scenarios violating safety of an autonomous car

\vspace{1cm}

## Fallback option: *Interpretability*

\begin{center}
If the system can explain its reasoning, we can verify if that reasoning is sound w.r.t. auxiliary criteria
\end{center}

---

# Prior Work: Defining and Measuring Interpretability

\begin{alertblock}{Bad News}
Little consensus on what interpretability is and how to evaluate it.
\end{alertblock}

**Interpretability evaluation typically falls into:**

1. **Evaluate in the context of an application**

   - If a system is useful in a practical application or a simplified version, it must be interpretable

2. **Evaluate via a quantifiable proxy**
   - Claim some model class is interpretable and present algorithms to optimize within that class
   - E.g. rule lists

\begin{center}
\Large
\textbf{"You will know it when you see it!"}
\end{center}

---

# Lack of Rigor?

\begin{block}{Yes and No}
Previous notions are reasonable
\end{block}

- **However:**
  - Are all models in all "interpretable" model classes equally interpretable?
    - Model sparsity allows for comparison
  - How to compare a linear model with a decision tree?
  - Do all applications have same interpretability needs?

\begin{center}
\Large
\textbf{Important to formalize these notions!!!}
\end{center}

---

# What is Interpretability?

\begin{definition}{} 
\begin{center}
\Large Ability to explain or to present in understandable terms to a human
\end{center}
\end{definition}

**No clear answers in psychology to:**

- What constitutes an explanation?
- What makes some explanations better than the others?
- When are explanations sought?

---

# When and Why Interpretability?

\begin{center}
\Large \textbf{Not all ML systems require interpretability}
\end{center}

- E.g., ad servers, postal code sorting
- No human intervention
- **No explanation needed because:**
  - No consequences for unacceptable results
  - Problem is well studied and validated well in real-world applications → trust system's decision

\begin{center}
\Large \textbf{When do we need explanation then?}
\end{center}

---

# When and Why Interpretability?

- **Incompleteness in problem formalization**
  - Hinders optimization and evaluation

\vspace{1cm}

- **Incompleteness $\neq$ Uncertainty**
  - Uncertainty can be quantified
  - E.g., trying to learn from a small dataset (uncertainty)

---

# Incompleteness: Illustrative Examples

**Scientific Knowledge**

- E.g., understanding the characteristics of a large dataset
- Goal is abstract

**Safety**

- End to end system is never completely testable
- Not possible to check all possible inputs

**Ethics**

- Guard against certain kinds of discrimination which are too abstract to be encoded
- No idea about the nature of discrimination beforehand

---

# Taxonomy of Interpretability Evaluation

\begin{center}
\includegraphics[width=.90\columnwidth]{imgs/taxonomy.png}\\
\vspace{0.5cm}
{\large \textbf{Claim of the research should match the type of the evaluation!}}
\end{center}


---

# Application-grounded evaluation

- Real humans (domain experts), real tasks
- Domain experts experiment with **exact application task**
- Domain experts experiment with a **simpler or partial task**
  - Shorten experiment time
  - Increases number of potential subjects
- Typical in *Human-Computer Interaction* (HCI) and visualization communities

---

# Human-grounded evaluation

**Real humans, simplified tasks**

- Can be completed with lay humans
- Larger pool, less expensive

**Potential experiments:**

- Pairwise comparisons
- Simulate the model output
- What changes should be made to input to change the output?

---

# Functionally-grounded evaluation

**No humans, just proxies**

- Appropriate for a class of models already validated (E.g., decision trees)
- A method is not yet mature
- Human subject experiments are unethical
- What proxies to use?

**Potential experiments:**

- Complexity (of a decision tree) compared to other models of the same (similar) class
  - How many levels? How many rules?

---

# Open Problems: Design Issues

- What proxies are best for what real world applications? \emoji{wtf}

\vspace{1cm}

- What factors to consider when designing simpler tasks in place of real world tasks? \emoji{wtf}

---

# Taxonomy based on applications/tasks

**Global vs. Local**

- High level patterns vs. specific decisions

**Degree of Incompleteness**

- What part of the problem is incomplete? How incomplete is it?
- Incomplete inputs or constraints or costs?

**Time Constraints**

- How much time can the user spend to understand explanation?

---

# Taxonomy based on applications/tasks (cont.)

**Nature of User Expertise**

- How experienced is end user?
- Experience affects how users process information
- E.g., domain experts can handle detailed, complex explanations compared to opaque, smaller ones

\vfill

## Note:

These taxonomies are constructed based on intuition and are not data or evidence driven. They must be treated as hypotheses.

---

# Taxonomy based on methods

**Basic units of explanation:**

- Raw features? E.g., pixel values
- Semantically meaningful? E.g., objects in an image
- Prototypes?

**Number of basic units of explanation:**

- How many does the explanation contain?
- How do various types of basic units interact?
- E.g., prototype vs. feature

---

# Taxonomy based on methods (cont.)

**Level of compositionality:**

- Are the basic units organized in a structured way?
- How do the basic units compose to form higher order units?

**Interactions between basic units:**

- Combined in linear or non-linear ways?
- Are some combinations easier to understand?

**Uncertainty:**

- What kind of uncertainty is captured by the methods?
- How easy is it for humans to process uncertainty?

---

# Relevant Conferences to Explore

**ML/AI Venues:**

- ICML, NeurIPS, ICLR
- UAI, AISTATS, KDD, AAAI

**Ethics/HCI Venues:**

- FAccT, AIES
- CHI, CSCW, HCOMP

---

# Closing

- Say hi to your neighbors! Introduce yourselves!
- What topics are you most excited about learning as part of this course? 
- Are you convinced that model interpretability/explainability is important? 
- Do you think we can really interpret/explain models (correctly)?
- What is your take on inherently interpretable models vs. post hoc explanations? Would you favor one over the other? Why?

# References {.allowframebreaks}

\footnotesize