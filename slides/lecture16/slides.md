---
title: "\\emoji{wtf} XAI: Interactive Explanations — XAL and TalkToModel"
bibliography: references.bib

---

# Disclaimer

\input{../disclaimer.tex}

---

# Paper 1: Explainable Active Learning (XAL)

\begin{center}
\Large\textbf{Explainable Active Learning (XAL): Toward AI Explanations as Interfaces for Machine Teachers}
\end{center}

\vspace{1em}

\begin{center}
Ghai, Moon, Kumar, Cheng, Zhang — CSCW 2021
\end{center}

[@ghai2021explainable]

---

# Motivation: Active Learning Bottleneck

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/xal_system_overview.png}
\end{center}

- Human annotators label data $\rightarrow$ model learns $\rightarrow$ model queries uncertain points
- But annotators get \textbf{no feedback} on why the model is uncertain

---

# The XAL Paradigm

\begin{columns}
\begin{column}{0.55\textwidth}
\begin{exampleblock}{Explainable Active Learning}
\begin{enumerate}
\item Model sends prediction \textbf{+ explanation} to annotator
\item Annotator confirms/rejects \textbf{+ provides feedback}
\item Model updates from annotation and feedback
\end{enumerate}
\end{exampleblock}
\end{column}
\begin{column}{0.42\textwidth}
\begin{center}
\includegraphics[width=\columnwidth]{imgs/xal_explanation_example.png}
\end{center}
\end{column}
\end{columns}

---

# Explanation Format

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/xal_explanation_example.png}
\end{center}

- Local feature importance bar chart (top 5 features)
- \textcolor{primarygreen}{Green} = positive influence, \textcolor{red}{red} = negative influence
- Orange baseline = model intercept (base chance)

---

# Task: Adult Income Classification

- Dataset: Adult Income (UCI)
- Task: Predict whether income $>$ \$80k (binary classification)
- Model: Logistic regression with L2 regularization
- Explanation method: local feature importance

---

# Study Design

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/xal_study_conditions.png}
\end{center}

\begin{columns}
\begin{column}{0.32\textwidth}
\begin{block}{AL}
Standard Active Learning (no explanation)
\end{block}
\end{column}
\begin{column}{0.32\textwidth}
\begin{block}{CL}
Crowdsourcing Learning (random queries, no explanation)
\end{block}
\end{column}
\begin{column}{0.32\textwidth}
\begin{exampleblock}{XAL}
Active Learning \textbf{with} explanations
\end{exampleblock}
\end{column}
\end{columns}

\vspace{0.5em}

36 AMT participants, 2 stages (early: 0 queries, late: 200 queries), 20 annotations each

---

# AL Simulation: Early vs. Late Stage

\begin{center}
\includegraphics[width=0.7\columnwidth]{imgs/xal_accuracy_curve.png}
\end{center}

- Model accuracy curve defines \textbf{early stage} (low accuracy) and \textbf{late stage} (high accuracy)
- Same model exposed at different points in AL curve

---

# Research Questions

\begin{columns}
\begin{column}{0.48\textwidth}
\textbf{RQ1:} How does human vs. model accuracy change across stages?

\vspace{0.5em}

\textbf{RQ2:} Does XAL affect user experience?
\begin{itemize}
\item H1: Trust calibration $\checkmark$
\item H2: Satisfaction $\times$
\item H3: Cognitive workload $\checkmark$
\end{itemize}
\end{column}
\begin{column}{0.48\textwidth}
\textbf{RQ3:} What moderates XAL effects?
\begin{itemize}
\item H4: Task knowledge $\times$
\item H5: AI experience $\checkmark$
\item H6: Need for cognition $\checkmark$
\end{itemize}

\vspace{0.5em}

\textbf{RQ4:} What determines explanation quality ratings?
\end{column}
\end{columns}

---

# Key Findings: Trust Calibration

\begin{center}
\includegraphics[width=0.65\columnwidth]{imgs/xal_trust_calibration.png}
\end{center}

- \textbf{H1 confirmed}: XAL users show \textbf{low trust early} (model is wrong), \textbf{increasing trust late} (model improves)
- AL/CL users trust blindly throughout
- Lower task knowledge $\rightarrow$ blind trust in XAL (lower sophistication users anchor on explanations)

---

# Key Findings: Explanation Ratings

- Explanation ratings are \textbf{higher} when the model is correct
- Explanation ratings are \textbf{higher} when annotators \textbf{wrongly disagree} with the model in the late stage
- Suggests users judge explanations by outcome, not reasoning quality

---

# Open Feedback Categories

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/xal_open_feedback.png}
\end{center}

Participants' suggestions for model improvement:
- \textbf{Tuning feature weights} (81 mentions)
- \textbf{Removing/changing/adding features} (28)
- \textbf{Ranking/ordering} (12)

---

# XAL Conclusions

\begin{columns}
\begin{column}{0.55\textwidth}
\begin{exampleblock}{Contributions}
\begin{itemize}
\item First study combining XAI with Active Learning
\item XAL improves \textbf{trust calibration} and reduces \textbf{cognitive overload}
\item Explanations enable annotators to act as "machine teachers"
\end{itemize}
\end{exampleblock}
\end{column}
\begin{column}{0.42\textwidth}
\begin{alertblock}{Limitations}
\begin{itemize}
\item Small N (36 AMT)
\item Only one explanation method
\item Interpretable model only (LR)
\end{itemize}
\end{alertblock}
\end{column}
\end{columns}

\vspace{0.5em}

Future: mitigate anchoring (Buçinca et al., CSCW'21), learn from explanation feedback

---

# XAL Discussion Questions

1. In which scenarios would XAL be most/least useful?
2. How can we prevent anchoring on incorrect explanations?
3. Would XAL work with less interpretable models?

---

# Paper 2: TalkToModel

\begin{center}
\Large\textbf{Explaining Machine Learning Models with Interactive Natural Language Conversations Using TalkToModel}
\end{center}

\vspace{1em}

\begin{center}
Slack, Krishna, Lakkaraju, Singh — Nature Machine Intelligence 2023
\end{center}

[@slack2023talktomodel]

---

# Motivation: The Explainability Bottleneck

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/ttm_system_overview.png}
\end{center}

- Post-hoc XAI methods (LIME, SHAP) are \textbf{hard for lay practitioners}
- Each method requires separate understanding and tooling
- Goal: \textbf{natural language dialogue} as a universal interface

---

# System Overview

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/ttm_system_overview.png}
\end{center}

TalkToModel: open-ended dialogue for understanding any \textbf{dataset + classifier} pair

---

# Component 1: Dialogue Engine

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/ttm_dialogue_engine.png}
\end{center}

\begin{columns}
\begin{column}{0.48\textwidth}
\textbf{Grammar-based} domain-specific language (DSL)

\vspace{0.5em}

Maps utterances $\rightarrow$ parse trees $\rightarrow$ operations
\end{column}
\begin{column}{0.48\textwidth}
\textbf{LLM fine-tuning} (seq2seq)
\begin{itemize}
\item T5 fine-tuned on generated data
\item GPT-J few-shot baseline
\end{itemize}
\end{column}
\end{columns}

---

# Fine-Tuning Data Generation

- Authors write \textbf{50 (utterance, parse) pairs} per domain
  - Every operation appears $\geq$ 2 times
- MTurk: paraphrase each utterance \textbf{8 ways} = 400 pairs
- MTurk: rate fidelity of paraphrase (keep $\geq$ 3/4 averaged over 5 raters)
- Manual filtering by authors
- Enumerate wildcards $\rightarrow$ \textbf{20k--40k training pairs} per domain

---

# The Grammar: DSL Operations

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/ttm_grammar_operations.png}
\end{center}

---

# Component 2: Execution Engine

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/ttm_execution_engine.png}
\end{center}

\begin{itemize}
\item \textbf{Counterfactual}: DiCE
\item \textbf{Post-hoc Feature Explanations}: LIME / KernelSHAP
\item \textbf{Data/Prediction Exploration}
\end{itemize}

Selects "best" explanation via \textbf{Faith score}

---

# Faith and Fudge Scores

\begin{center}
\includegraphics[width=0.7\columnwidth]{imgs/ttm_faith_fudge.png}
\end{center}

**Fudge score** (faithfulness of a mask $\mathbf{m}$ for instance $\mathbf{x}$):

$$\text{Fudge}(f,\mathbf{x},\mathbf{m}) = \frac{1}{N}\sum_{n=1}^N |f(\mathbf{x}) - f(\mathbf{x}+\epsilon_n \odot \mathbf{m})|$$

**Faith score** = sum of Fudge scores over top-$k$ features

Computed for LIME (kernels 0.25/0.5/0.75/1.0) and KernelSHAP $\rightarrow$ report highest

---

# Experiment 1: LLM Evaluation

\begin{columns}
\begin{column}{0.48\textwidth}
\textbf{Datasets:}
\begin{itemize}
\item Diabetes (Pima Indian): 768 women, 8 features, 400→190 questions
\item Credit (German): 1000 applicants, 20 features, 400→200 questions
\item Recidivism (COMPAS): 11757 defendants, 43 features, 400→146 questions
\end{itemize}
\end{column}
\begin{column}{0.48\textwidth}
\textbf{Splits:}
\begin{itemize}
\item \textbf{IID (Easy)}: operations seen in training, different arguments
\item \textbf{Compositional (Hard)}: new operation combinations not seen in training
\end{itemize}
\end{column}
\end{columns}

---

# LLM Results: Exact Match Accuracy

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/ttm_llm_results.png}
\end{center}

\begin{itemize}
\item \textbf{T5-Large best}: German 63.5\%, Compas 66.4\%, Diabetes 76.8\% overall
\item GPT-J (few-shot) $\ll$ T5 fine-tuning, especially on \textbf{compositional split}
\item All models: low accuracy on hard (compositional) split
\end{itemize}

---

# Experiment 2: Grammar Coverage

\textbf{Question:} Is the grammar expressive enough to capture all XAI questions?

\begin{exampleblock}{Method}
\begin{itemize}
\item Use a curated \textbf{XAI question bank} (31 questions, informed by expert interviews)
\item Manually review if grammar operations can answer each
\end{itemize}
\end{exampleblock}

\begin{block}{Result}
\textbf{30/31} questions can be answered by the grammar

Example: \texttt{topk(test\_data, all)}, \texttt{mistakes(test\_data)}, \texttt{cfe(filter(test\_data, id, A, =), 10, Q)}
\end{block}

---

# Experiment 3: User Study

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/ttm_user_experiment.png}
\end{center}

- Diabetes dataset + gradient-boosted tree
- 45 healthcare workers + 12 ML grad students
- 10 XAI multiple-choice questions each
- Compared vs. \textbf{explainerdashboard} (baseline)

---

# The Baseline: explainerdashboard

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/ttm_explainerdashboard.png}
\end{center}

---

# TalkToModel Interface

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/ttm_interface_screenshot.png}
\end{center}

---

# User Study Findings

\begin{exampleblock}{TalkToModel vs. explainerdashboard}
\begin{itemize}
\item \textbf{Over 90\% accurate} vs. $\sim$60\% with explainerdashboard
\item Answered questions in \textbf{half the time}
\item \textbf{Consistently preferred} on ease of use, confidence, speed, and likability
\end{itemize}
\end{exampleblock}

\begin{columns}
\begin{column}{0.48\textwidth}
\begin{center}
\textbf{\% Questions Completed}

Healthcare workers: 86.2\% vs. 74.7\%

ML grads: 93.9\% vs. 73.8\%
\end{center}
\end{column}
\begin{column}{0.48\textwidth}
\begin{center}
\textbf{\% Accuracy on Completed}

Healthcare workers: 91.8\% vs. 66.1\%

ML grads: 100\% vs. 62.5\%
\end{center}
\end{column}
\end{columns}

---

# TalkToModel Conclusions

- \textbf{Elegant UI}: natural language makes model interpretation accessible to laypeople and ML practitioners
- \textbf{Highly extensible}: handles a variety of XAI methods, problem domains
- \textbf{Reasonably accurate}: fine-tuned T5 interprets user intent well
- \textbf{Low barrier}: only need your own dataset to deploy

---

# TalkToModel Limitations

\begin{alertblock}{Limitations}
\begin{itemize}
\item Not tested in \textbf{real-world settings}
\item \textbf{No flexibility} in explanation method selection ("most feasible CFE", "most stable explanation")
\item \textbf{No guarantees on data quality} for fine-tuning; some manual labor required
\item \textbf{No domain knowledge} beyond the grammar
\item Accuracy on \textbf{compositional (hard) split} still very low
\end{itemize}
\end{alertblock}

---

# TalkToModel Discussion Questions

1. Are ML practitioners most responsible for the accessibility of XAI?
2. Is the TalkToModel LLM itself interpretable? When is it acceptable to improve XAI with more black-box AI?
3. How much control over explanations should we give users while remaining accessible to laypeople?
4. Does TalkToModel's existence excuse other XAI methods from being accessible?
5. Dashboard vs. Dialogue — which is better and when?

---

\begin{center}
\Huge Thank You!
\end{center}

---

# References {.allowframebreaks}

\footnotesize
