---
title: "\\emoji{wtf} XAI: Interactive Explanations — XAL and TalkToModel"
bibliography: references.bib
---

# Disclaimer

\input{../disclaimer.tex}

---

# Paper 1: Explainable Active Learning (XAL)

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/xal_paper.png}
\end{center}

[@ghai2021explainable]

---

# Motivation: Machine Learning Bottleneck

Current ML development processes are bottlenecked by:

- \textbf{Machine learning is used} in a wide variety of fields
- \textbf{Resources and expertise} — labeling is costly
- \textbf{Asynchronous interaction} between Subject Matter Expert (SME), developer and the model
- Many AL paradigms have been developed; very little attention given to \textbf{improving human interaction} with AL algorithms

\vspace{1em}
Efforts are underway to make machine learning more accessible.

---

# Related Work: Active Learning

\begin{definition}{}
Active Learning (AL): a paradigm in which the model \textbf{queries} a human annotator for labels on the data points where it is most uncertain.
\end{definition}

\vspace{0.5em}

\includegraphics[width=0.9\columnwidth]{imgs/xal_active_learning_task.png}

- Human annotators label data $\rightarrow$ model learns $\rightarrow$ model queries uncertain points
- AL tries to maximize model performance while minimizing annotation effort via \textbf{uncertainty sampling}.

---

# Related Work: Interactive ML

- AL is sometimes considered within \textbf{interactive machine learning (iML)}
- iML approaches \textbf{value transparency over performance}
- Empirical studies demonstrate iML techniques lower need for data — but little else
- iML approaches are esoteric; \textbf{explanations as interfaces} could help non-ML experts

---

# Problem Statement

\begin{alertblock}{Active Learning interfaces remain minimal and opaque}
\begin{itemize}
\item But annotators get \textbf{no feedback} on why the model is uncertain
\item Annotator cannot monitor \textbf{training progress}
\item Annotator is unaware of the \textbf{effectiveness} of their teaching
\end{itemize}
\end{alertblock}

\vspace{1em}

Explanations show potential for better active learning.

\vspace{1em}

\begin{center}
\Large\textbf{Big Question:} Can explanations improve the active learning process?
\end{center}

---

# Summary of Contributions

1. Propose a novel paradigm: \textbf{Explainable Active Learning (XAL)}
2. Conduct an \textbf{empirical study} to investigate the impact of explanations on annotation experience

---

# Contribution #1: The XAL Paradigm

\begin{columns}
\begin{column}{0.55\textwidth}
\begin{exampleblock}{Explainable Active Learning}
\begin{enumerate}
\item Model sends prediction \textbf{+ local explanation} to annotator
\item Annotator confirms or rejects the prediction
\item Annotator \textbf{provides feedback} on the explanation
\item Model updates from annotation \textbf{and} feedback
\end{enumerate}
\end{exampleblock}

\vspace{0.5em}

Mimics how humans teach and learn — explanations make it easier to \textbf{reject incorrect predictions}.
\end{column}
\begin{column}{0.42\textwidth}
\begin{center}
\includegraphics[width=\columnwidth]{imgs/xal_system_overview.png}
\end{center}
\end{column}
\end{columns}

---

# The XAL Paradigm: Key points

- Uses the explanation to answer "why am I giving this instance this prediction?"
- Explains specific instances, not global — better for non-experts.
- Improves labeling quality by exposing the model's reasoning.

---

# Contribution #2: Empirical Study

\begin{columns}
\begin{column}{0.55\textwidth}
\begin{block}{Dataset: Adult Income}
\begin{itemize}
\item Binary prediction: annual income $>$ or $<$ \$80k
\item Model: logistic regression with L2 regularization
\end{itemize}
\end{block}

\vspace{1em}

Annotators receive a \textbf{customer profile} and must judge the income level.
\end{column}
\begin{column}{0.42\textwidth}
\begin{center}
\includegraphics[width=\columnwidth]{imgs/xal_prediction_task.png}
\end{center}
\end{column}
\end{columns}

---

# Experimental Design

- \textbf{Participants}: Amazon Mechanical Turk - 36 participants
- \textbf{Model}: Two learning stages (each participant completed both)
  - Early
  - Late

- \textbf{Three conditions}: (each participant assigned to one)

\begin{columns}
\begin{column}{0.32\textwidth}
\begin{block}{AL}
Standard Active Learning — customer profile only
\end{block}
\end{column}
\begin{column}{0.32\textwidth}
\begin{block}{CL}
Coactive Learning — profile + model prediction
\end{block}
\end{column}
\begin{column}{0.32\textwidth}
\begin{exampleblock}{XAL}
Profile + prediction \textbf{+ explanation}
\end{exampleblock}
\end{column}
\end{columns}

\vspace{0.5em}

- 20 annotations per experiment (condition + stage)
- Domain knowledge training (statistics, practice trials, $2 bonus for consistency with ground-truth)

---

# Design Choices: Active Learning Simulation

\begin{columns}
\begin{column}{0.55\textwidth}
\begin{itemize}
\item Simulation used to define \textbf{early-stage} and \textbf{late-stage} models
\begin{itemize}
\item Early stage → 0 queries (low accuracy)
\item Late stage → 200 queries (accuracy plateaus)
\end{itemize}
\item Queried instances annotated using ground-truth labels in simulation
\end{itemize}

\end{column}
\begin{column}{0.42\textwidth}
\begin{center}
\includegraphics[width=\columnwidth]{imgs/xal_accuracy_curve.png}
\end{center}
\end{column}
\end{columns}

---

# Design Choices: Explanation Format

\begin{columns}
\begin{column}{0.55\textwidth}
\begin{center}
\includegraphics[width=\columnwidth]{imgs/xal_explanation_example.png}
\end{center}
\end{column}
\begin{column}{0.42\textwidth}
\begin{itemize}
\item Local feature importance bar chart (\textbf{top 5 features})
\item \textcolor{primarygreen}{Green} = positive influence on prediction
\item \textcolor{red}{Red} = negative influence
\item Orange baseline = model intercept (\textbf{base chance})
\item Features sorted by importance magnitude
\end{itemize}

\end{column}
\end{columns}

---

# Research Question 1

\begin{center}
\Large How do local explanations impact the \textbf{annotation and training outcomes} of AL?
\end{center}

---

# RQ1: Annotation + Learning Outcomes

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/xal_results_rq1.png}
\end{center}

\begin{exampleblock}{Key Finding}
Overall, \textbf{human accuracy} and \textbf{\% agreement} \textit{decrease} in the later stage, while \textbf{model accuracy} increases.
\end{exampleblock}

---

# Research Question 2

\begin{center}
\Large How do local explanations impact \textbf{annotator experiences}?
\end{center}

\vspace{1em}

\begin{columns}
\begin{column}{0.32\textwidth}
\begin{block}{H1}
Explanations support \textbf{trust calibration}
\end{block}
\end{column}
\begin{column}{0.32\textwidth}
\begin{block}{H2}
Explanations improve \textbf{annotator satisfaction}
\end{block}
\end{column}
\begin{column}{0.32\textwidth}
\begin{block}{H3}
Explanations increase perceived \textbf{cognitive workload}
\end{block}
\end{column}
\end{columns}

---

# RQ2: Trust Calibration (H1)

\begin{center}
\includegraphics[width=0.60\columnwidth]{imgs/xal_trust_calibration.png}
\end{center}

\begin{exampleblock}{H1 Supported}
XAL users show \textbf{low trust early} (model is wrong) and \textbf{increasing trust late} (model improves). AL/CL users trust blindly throughout.
\end{exampleblock}

---

# RQ2: Satisfaction (H2)

\begin{center}
\includegraphics[width=0.60\columnwidth]{imgs/xal_results_h2.png}
\end{center}

\begin{alertblock}{H2 Not Supported}
Explanations have a \textbf{significant negative effect on satisfaction} for those with \textbf{low need for cognition} — they find explanations burdensome rather than helpful.
\end{alertblock}

---

# RQ2: Cognitive Workload (H3)

\begin{center}
\includegraphics[width=0.60\columnwidth]{imgs/xal_results_h3.png}
\end{center}

\begin{exampleblock}{H3 Supported}
XAL induces \textbf{significantly higher workload} for those \textbf{with AI experience} — they engage more deeply with the explanations.
\end{exampleblock}

---

# Research Question 3

\begin{center}
\Large How do \textbf{individual factors} impact annotation and annotator experiences with XAL?
\end{center}

\vspace{1em}

\begin{columns}
\begin{column}{0.32\textwidth}
\begin{block}{H4}
Annotators with \textbf{lower task knowledge} benefit more from XAL
\end{block}
\end{column}
\begin{column}{0.32\textwidth}
\begin{block}{H5}
Annotators \textbf{inexperienced with AI} benefit more from XAL
\end{block}
\end{column}
\begin{column}{0.32\textwidth}
\begin{block}{H6}
Annotators with \textbf{lower need for cognition} have a less positive experience with XAL
\end{block}
\end{column}
\end{columns}

---

# RQ3: Task Knowledge (H4)

\begin{center}
\includegraphics[width=\columnwidth]{imgs/xal_results_h4.png}
\end{center}

\begin{alertblock}{H4 Not Supported}
Participants with \textbf{less task knowledge} had \textbf{lower accuracies} and \textbf{higher blind trust} in XAL condition — they did not benefit more; they anchored on explanations.
\end{alertblock}

---

# RQ3: AI Experience (H5)

\begin{center}
\includegraphics[width=0.60\columnwidth]{imgs/xal_results_h5.png}
\end{center}

\begin{exampleblock}{H5 Supported}
Explanations helped \textbf{calibrate trust for those without AI experience}. Users with AI experience showed higher trust regardless of condition.
\end{exampleblock}

---

# RQ3: Satisfaction and Need for Cognition (H6)

\begin{center}
\includegraphics[width=0.60\columnwidth]{imgs/xal_results_h6.png}
\end{center}

\begin{exampleblock}{H6 Supported}
Explanations have a \textbf{significant negative effect on satisfaction} for those with \textbf{low need for cognition} — they find explanations burdensome rather than helpful.
\end{exampleblock}

---

# Research Question 4

\begin{center}
\Large What kind of \textbf{feedback} do annotators naturally want to provide upon seeing local explanations?
\end{center}

---

# RQ4: Explanation Ratings

\begin{center}
\includegraphics[width=0.60\columnwidth]{imgs/xal_explanation_ratings.png}
\end{center}

\begin{block}{Key Finding}
Explanation ratings are \textbf{higher} when the model is \textbf{correct} and when annotators \textbf{wrongly disagree} with the model in later stage tasks — users judge explanations by outcome, not reasoning quality.
\end{block}

---

# RQ4: Open Form Feedback

What participants wanted to tell the model:

- \textbf{Tuning feature weights} (81 mentions)
- \textbf{Removing, changing direction, or adding features} (28)
- \textbf{Ranking or comparing multiple feature weights} (12)
- \textbf{Reasoning about combinations and relations} (10)
- Logic to make decisions based on feature importance (6)

---

# XAL Conclusions

\begin{columns}
\begin{column}{0.55\textwidth}
\begin{exampleblock}{Key Contributions}
\begin{itemize}
\item New approach for machine teaching: \textbf{XAI + AL = XAL}
\item XAL improves \textbf{trust calibration} and increases \textbf{cognitive engagement}
\item Explanations enable annotators to act as \textbf{machine teachers}
\end{itemize}
\end{exampleblock}
\end{column}
\begin{column}{0.42\textwidth}
\begin{alertblock}{Limitations}
\begin{itemize}
\item Small N (36 AMT workers)
\item Only uncertainty sampling
\item Only one explanation method
\item Only interpretable model (LR)
\item What about image data (pixels)?
\end{itemize}
\end{alertblock}
\end{column}
\end{columns}

---

# XAL Discussion Questions

1. Has anyone used AL in the past? Would adding explanations have been helpful?
2. What applications of XAL are you most excited about? In which scenarios would it work especially well or poorly?
3. Do you think XAL is feasible with less interpretable models or other explanation methods?

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

Example: \texttt{topk(test_data, all)}, \texttt{mistakes(test_data)}, \texttt{cfe(filter(test_data, id, A, =), 10, Q)}
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
