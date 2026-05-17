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
\includegraphics[width=0.85\columnwidth]{imgs/ttm_paper.png}
\end{center}

[@slack2023talktomodel]

---

# Motivation: The XAI Landscape

\begin{center}
\includegraphics[width=\columnwidth]{imgs/ttm_background_methods.png}
\end{center}

\begin{columns}
\begin{column}{0.32\textwidth}
\begin{center}
\textbf{LIME}
Local linear approximation around a point
\end{center}
\end{column}

\begin{column}{0.32\textwidth}
\begin{center}
\textbf{Counterfactuals}
Minimal changes to flip prediction
\end{center}
\end{column}

\begin{column}{0.32\textwidth}
\begin{center}
\textbf{SHAP}
Feature importance via Shapley values
\end{center}
\end{column}

\end{columns}

---

# Motivation: The Practitioner's Dilemma

A nurse or doctor (or someone who is not an AI specialist) trying to use XAI:

1. Which method to choose for my application?
2. Which one would you trust?
3. How should they interpret the explanations?
4. How would they use these methods?
5. How would they \textbf{interact} with the method?
6. What if they have follow-up questions?

---

# Motivation

\begin{alertblock}{Root problem}
Every XAI tool requires its own expertise — there is no \textbf{universal, conversational interface}.
\end{alertblock}

\vspace{1em}

\begin{alertblock}{The XAI Bottleneck}
\begin{itemize}
\item Simple explanations are a \textbf{bottleneck to adoption}
\item There are inherently interpretable models; however, black box models are more flexible and accurate.
\item Post-hoc methods are hard to use empirically:
\begin{itemize}
\item Which method to pick?
\item How to interpret results?
\item How to ask follow-up questions?
\end{itemize}
\end{itemize}
\end{alertblock}

---

# Related Work

\begin{columns}
\begin{column}{0.50\textwidth}
\begin{itemize}
\item \textbf{Language-Interpretability Tool (LiT)}: Open-source NLP model understanding. Uses LIME, aggregate stats, counterfactuals.
\item \textbf{What-If Tool}: Helps users perform counterfactual analysis for models.
\item \textbf{explainerdashboard}: Used as baseline. Tab-based dashboard with SHAP, CFE, feature dependence.
\end{itemize}
\end{column}
\begin{column}{0.50\textwidth}

\begin{center}
\includegraphics[width=\columnwidth]{imgs/ttm_lit_tool.png}
\end{center}

\end{column}
\end{columns}

\vspace{1em}

\begin{alertblock}{Common problem}
Relatively \textbf{high barrier to entry} and \textbf{no follow-up questions} — users are passive consumers of explanations.
\end{alertblock}

---

# Problem Statement

\begin{definition}{}
Design a system that makes it easy for \textbf{lay practitioners} to apply post-hoc interpretability methods to black-box models.
\end{definition}

\vspace{1em}

\textbf{Desiderata:}

- \textbf{Dialogue system} handling many conversation topics (data trends, specific predictions, etc.)
- \textbf{Variety} of data types and model classes (treatment prediction, risk of relapse, etc.)
- Does \textbf{not require} high ML expertise

---

# Summary of Contributions: TalkToModel

\begin{exampleblock}{TalkToModel}
Open-ended dialogue for understanding any \textbf{dataset + classifier} pair
\end{exampleblock}

\vspace{0.5em}

\textbf{Capabilities:} why a prediction occurred, how it changes if data changes, how to flip predictions, general data statistics, etc.

\vspace{1em}

\begin{columns}
\begin{column}{0.48\textwidth}
\textbf{Problem}
\begin{enumerate}
\item Which method to choose?
\item Which would a practitioner trust?
\item How to interpret?
\item How to use?
\item How to interact?
\end{enumerate}
\end{column}
\begin{column}{0.48\textwidth}
\textbf{TalkToModel}
\begin{enumerate}
\item Uses \textbf{many} post-hoc methods
\item Picks the \textbf{"best"} explanation
\item Answers in \textbf{natural language}
\item Only needs \textbf{model + data}
\item Communicate via \textbf{natural language}
\end{enumerate}
\end{column}
\end{columns}

---

# Talking to the Model: TalkToModel's Answers

\begin{columns}
\begin{column}{0.48\textwidth}

\textbf{Three components:}
\begin{enumerate}

\item \textbf{Dialogue engine} — LLM backend translating utterances to operations
\item \textbf{Execution engine} — runs many explanations and picks the best one
\item \textbf{Text interface} — enables natural language conversations
\end{enumerate}

\end{column}
\begin{column}{0.48\textwidth}

\begin{center}
\includegraphics[width=\columnwidth]{imgs/ttm_system_overview.png}
\end{center}
\end{column}
\end{columns}

---

# Talking to the Model: TalkToModel's Answers

\begin{center}
\includegraphics[width=\columnwidth]{imgs/ttm_method_pipeline_1.png}
\end{center}

---

# Talking to the Model: TalkToModel's Answers

\begin{center}
\includegraphics[width=\columnwidth]{imgs/ttm_method_pipeline_2.png}
\end{center}

---

# Talking to the Model: TalkToModel's Answers

\begin{center}
\includegraphics[width=\columnwidth]{imgs/ttm_method_pipeline_3.png}
\end{center}

---

# Talking to the Model: TalkToModel's Answers

\begin{center}
\includegraphics[width=\columnwidth]{imgs/ttm_method_pipeline_4.png}
\end{center}

---

# Talking to the Model: TalkToModel's Answers

\begin{center}
\includegraphics[width=\columnwidth]{imgs/ttm_method_pipeline_5.png}
\end{center}

---

# Dialogue Engine: The Grammar

\begin{columns}
\begin{column}{0.55\textwidth}
\begin{block}{Domain-Specific Language (DSL)}
To represent the intentions behind user utterances in a structured form, TalkToModel relies on a grammar defining a domain specific language for model understanding.
\end{block}

\vspace{0.5em}

The grammar includes:
\begin{enumerate}
\item All \textbf{operations} TalkToModel can run
\item The \textbf{arguments} for each operation
\item The \textbf{relations} between operations
\end{enumerate}
\end{column}
\begin{column}{0.42\textwidth}
\begin{center}
\includegraphics[width=\columnwidth]{imgs/ttm_dialogue_engine.png}
\end{center}
\end{column}
\end{columns}

---

# Dialogue Engine: Grammar Operations

\begin{columns}
\begin{column}{0.50\textwidth}
\begin{center}
\includegraphics[width=0.95\columnwidth]{imgs/ttm_grammar_operations.png}
\end{center}
\end{column}
\begin{column}{0.42\textwidth}
\footnotesize
\textbf{Data:} Supports data exploration and filtering operations.

\vspace{1em}
\textbf{Explainability:} Supports interpretation and explanation of model behavior.

\vspace{1em}
\textbf{ML:} Supports prediction and evaluation tasks for machine learning models.

\vspace{1em}
\textbf{Conversational:} Supports contextual and follow-up interactions.

\vspace{1em}
\textbf{Description:} Provides general information about functions, data, and models.
\end{column}
\end{columns}

---

# Dialogue Engine: Dataset-Specific Grammar

\begin{alertblock}{Challenge}
It is challenging to use a \textbf{general grammar} that works for all datasets.
\end{alertblock}

\vspace{1em}

TalkToModel uses a grammar that is \textbf{dependent on the dataset features}.

\vspace{1em}

\begin{exampleblock}{Example}
The arguments for operations like \texttt{filter} or \texttt{topk} are automatically filled with the actual feature names from the user's provided dataset.
\end{exampleblock}

---

# Dialogue Engine: Fine-Tuning LLM (seq2seq)

\begin{center}
\includegraphics[width=0.65\columnwidth]{imgs/ttm_dialogue_engine_seq_2_seg.png}
\end{center}

"To parse user utterances into the grammar, we fine-tune an LLM to translate utterances into the grammar in a \textbf{seq2seq fashion}."

\vspace{1em}

\begin{columns}
\begin{column}{0.48\textwidth}
\begin{center}
\textbf{Input:} User utterances

\footnotesize "How likely is a 40-year-old woman to have diabetes?"
\end{center}
\end{column}
\begin{column}{0.48\textwidth}
\begin{center}
\textbf{Output:} Grammar parses

\footnotesize \texttt{likelihood(filter(data, age, 40, =))}
\end{center}
\end{column}
\end{columns}

---

# Dialogue Engine: Training Data Generation

\begin{enumerate}
\item Authors write \textbf{50 (utterance, parse) pairs} per domain — every operation appears $\geq$ 2×
\item MTurk: paraphrase each utterance \textbf{8 ways} = 400 pairs
\item MTurk: rate fidelity of paraphrase (keep $\geq$ 3/4 avg over 5 raters)
\item Manual filtering by authors
\item Enumerate wildcards with dataset features $\rightarrow$ \textbf{20k–40k training pairs}
\end{enumerate}

---

# Dialogue Engine: Example Paraphrases

\begin{block}{Original utterance}
"What is your reasoning for determining if people older than 20 are likely to commit crimes?"
\end{block}

\vspace{0.5em}

\begin{exampleblock}{MTurk paraphrases}
\begin{itemize}
\item "Why do you think people over the age of twenty are likely to commit a crime?"
\item "How did you determine the likelihood of people over 20 committing crimes?"
\item "Can you reason why people over twenty would likely commit crimes?"
\end{itemize}
\end{exampleblock}

---

# Dialogue Engine: Responding Conversationally

\begin{block}{Template-based responses}
After TalkToModel executes a parse, it \textbf{composes the results} of the operations into a natural language response using \textbf{templates} associated with each operation.
\end{block}

\vspace{0.5em}

- Each operation has an associated \textbf{response template}
- TalkToModel can run \textbf{multiple operations simultaneously} — it joins response templates ensuring semantic coherence

---

# Dialogue Engine: Complete Pipeline

\begin{center}
\begin{enumerate}
\item \textbf{Constructing a grammar} — DSL with operations, arguments, relations
\item \textbf{Generate fine-tuning data} — 50 pairs $\rightarrow$ wildcard enumeration $\rightarrow$ 20k–40k pairs
\item \textbf{Fine-tuning LLM} (T5) — translate utterances to parses (seq2seq)
\item \textbf{Respond conversationally} — templates composed into natural language
\end{enumerate}
\end{center}

---

# Execution Engine

\begin{center}
\includegraphics[width=\columnwidth]{imgs/ttm_execution_engine.png}
\end{center}

---

# Execution Engine: Selecting the Best Explanation

\begin{alertblock}{Key design choice}
Instead of providing raw LIME or SHAP values, TalkToModel \textbf{tests multiple methods} and reports the \textbf{most faithful} one.
\end{alertblock}

\vspace{1em}

\textbf{Setup:}

- $f$: model outputting probability $y$ of a class
- $\phi$: feature importances for model $f$ on instance $x$ (greater magnitude = higher importance)
- Methods evaluated: LIME with kernels $\{0.25, 0.5, 0.75, 1.0\}$ + KernelSHAP

---

# Execution Engine: The Fudge Score

\textbf{Intuition:} More important features should cause \textbf{larger perturbations} in the prediction when noise is added.

$$\text{Fudge}(f, \mathbf{x}, \mathbf{m}) = \frac{1}{N}\sum_{n=1}^N |f(\mathbf{x}) - f(\mathbf{x} + \epsilon_n \odot \mathbf{m})|$$

Average magnitude of prediction perturbation when adding Gaussian noise \textbf{masked by} $\mathbf{m}$.

---

# Execution Engine: Faith Score

\textbf{Feature Importance Faithfulness} (Faith):

$$\text{Faith}(\phi, f, x, K) = \sum_{k=1}^{K} \text{Fudge}(f, x, \mathbf{1}(k, \phi))$$

$$\text{where } \mathbf{1}(k, \phi) \text{ is a binary mask that selects the top-}k\text{ most important features}$$

- Computed for LIME (4 kernels) and KernelSHAP
- \textbf{Report the one with highest Faith}

\vspace{0.5em}

\begin{exampleblock}{Outcome}
TalkToModel automatically selects the most faithful explanation — the user never has to choose.
\end{exampleblock}

---

# Experiments: Overview

\begin{columns}
\begin{column}{0.32\textwidth}
\begin{block}{Experiment 1}
\textbf{LLM Experiment} — Is the LLM accurately interpreting user questions?
\end{block}
\end{column}
\begin{column}{0.32\textwidth}
\begin{block}{Experiment 2}
\textbf{Grammar Experiment} — Is the grammar expressive enough for all XAI questions?
\end{block}
\end{column}
\begin{column}{0.32\textwidth}
\begin{block}{Experiment 3}
\textbf{User Experiment} — Do users prefer TalkToModel over a standard dashboard?
\end{block}
\end{column}
\end{columns}

---

# Experiment 1: LLM Evaluation

\textbf{Goal:} Is the LLM accurately interpreting user questions?

\begin{block}{Method}
\begin{itemize}
\item Create a \textbf{"Gold Dataset"}: ground-truth (utterance, parse) pairs specific to each domain
\item Evaluate \textbf{Exact Match Accuracy} of LLM translation
\item Compare along \textbf{easy} (IID) and \textbf{hard} (compositional) splits
\item Compare few-shot GPT-J vs. fine-tuned T5 at different sizes
\end{itemize}
\end{block}

---

# Experiment 1: Datasets and Gold Data

\begin{columns}
\begin{column}{0.48\textwidth}
\begin{block}{Domains}
\begin{itemize}
\item \textbf{Diabetes}: 768 women, 8 features, 400→190 questions
\item \textbf{Credit}: 1000 applicants, 20 features, 400→200 questions
\item \textbf{Recidivism (COMPAS)}: 11757 defendants, 43 features, 400→146 questions
\end{itemize}
\end{block}
\end{column}
\begin{column}{0.48\textwidth}
\begin{block}{Data Collection}
\begin{enumerate}
\item Authors: 50 (utterance, parse) pairs per domain
\item MTurk: 8 paraphrases per utterance
\item MTurk: fidelity rating (keep $\geq$ 3/4 avg)
\item Manual filtering
\end{enumerate}
\end{block}
\end{column}
\end{columns}

\vspace{0.5em}
Splits:

\begin{columns}
\begin{column}{0.48\textwidth}
\begin{exampleblock}{IID (Easy)}
Order of operations \textbf{seen in training} — only arguments differ
\end{exampleblock}
\end{column}
\begin{column}{0.48\textwidth}
\begin{alertblock}{Compositional (Hard)}
Order of operations \textbf{not seen before} in training data
\end{alertblock}
\end{column}
\end{columns}

---

# Experiment 1: LLM Results

\begin{center}
\includegraphics[width=0.88\columnwidth]{imgs/ttm_llm_results.png}
\end{center}

---

# Experiment 2: Grammar Coverage

\textbf{Goal:} Is the grammar expressive enough to capture all XAI questions?

\begin{exampleblock}{Method}
\begin{itemize}
\item Use a curated \textbf{XAI question bank} (31 questions, informed by design expert interviews)
\item Manually review if grammar operations can answer each question
\end{itemize}
\end{exampleblock}

\begin{block}{Result}
\textbf{30/31} questions can be answered by the grammar.

The remaining question was deemed out of scope.
\end{block}

[@questions_xia]

---

# Experiment 3: User Study

- \textbf{45 healthcare workers} + 12 ML grad students
- Diabetes dataset
- Answer \textbf{10 XAI multiple-choice questions}, divided into 2 blocks of 5: One block was answered using TalkToModel, and the other using \textbf{explainerdashboard}

- Metrics
  - Ease of use, confidence, speed, and likability (subjective)
  - Completion rate, Accuracy (objective)

\footnotesize Example: "Is glucose more important than age for the model's predictions for data point 49?"

---

# explainerdashboard vs TalkToModel Interface

\begin{columns}
\begin{column}{0.50\textwidth}
\begin{center}
\includegraphics[width=\columnwidth]{imgs/ttm_explainerdashboard.png}
\end{center}
\end{column}
\begin{column}{0.50\textwidth}
\begin{center}
\includegraphics[width=\columnwidth]{imgs/ttm_interface_screenshot.png}
\end{center}
\end{column}
\end{columns}

---

# Experiment 3: Results

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

\begin{columns}
\begin{column}{0.55\textwidth}
\begin{exampleblock}{Strengths}
\begin{itemize}
\item \textbf{Elegant UI}: natural language makes model interpretation accessible
\item \textbf{Highly extensible}: handles a variety of XAI methods and problem domains
\item \textbf{Reasonably accurate}: fine-tuned T5 interprets user intent well
\item \textbf{Low barrier}: only need your own dataset to deploy
\end{itemize}
\end{exampleblock}
\end{column}
\begin{column}{0.42\textwidth}
\begin{alertblock}{Limitations}
\begin{itemize}
\item Not tested in \textbf{real-world settings}
\item No user \textbf{flexibility} in explanation selection
\item No guarantees on \textbf{data quality} for fine-tuning
\item No \textbf{domain knowledge} beyond the grammar
\item Low accuracy on \textbf{compositional split}
\end{itemize}
\end{alertblock}
\end{column}
\end{columns}

\vspace{0.5em}

\textbf{Discussion Questions:} Is the TalkToModel LLM itself interpretable?

---

\begin{center}
\Huge Thank You!
\end{center}

---

# References {.allowframebreaks}

\footnotesize
