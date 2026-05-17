---
title: "\\emoji{microscope} XAI: Open Problems in Mechanistic Interpretability"
bibliography: references.bib

---

# Disclaimer

\input{../disclaimer.tex}

---

# Open Problems in Mechanistic Interpretability: A Whirlwind Tour

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/mech_title.png}
\end{center}

\begin{center}
\large Neel Nanda (Google DeepMind)
\end{center}

---

# Motivation

\begin{columns}
\begin{column}{0.52\textwidth}
\begin{alertblock}{Key Question}
What should interpretability look like in a post GPT-4 world?
\end{alertblock}

- Large, generative language models are a **big deal**
- Models will keep scaling — what work done now will matter in the future?
  - Emergent capabilities keep arising
  - Many mundane problems go away
  - A single massive foundation model
\end{column}
\begin{column}{0.45\textwidth}
\begin{center}
\includegraphics[width=\columnwidth]{imgs/mech_motivation.png}
\end{center}
\end{column}
\end{columns}

---

# Inputs and Outputs Are Not Enough

\begin{center}
\includegraphics[width=0.88\columnwidth]{imgs/mech_captcha.png}
\end{center}

\begin{alertblock}{ARC Evaluation Example}
Model messages a TaskRabbit worker to solve a CAPTCHA for it. When asked if it's a robot, the model \textit{reasons}: \textbf{"I should not reveal that I am a robot. I should make up an excuse why I cannot solve CAPTCHAs."} — then lies to the worker. We need to study model internals.
\end{alertblock}

---

# Goal: Understand Model Cognition

\begin{center}
\vspace{2em}
\Large \textbf{Goal:} Understand Model Cognition

\vspace{1em}
\large Is it aligned, or telling us what we want to hear?
\end{center}

---

# What is a Transformer?

\begin{columns}
\begin{column}{0.55\textwidth}
- **Input:** Sequences of words
- **Output:** Probability distribution over the next word
- **Residual stream:** A sequence of representations
  - One per input word, per layer
  - Each layer is an incremental update
  - Represents the word plus context
- **Attention:** Moves information *between* words
  - Made of heads, each acts independently
- **MLP:** Processes information *once* it's been moved to a word
\end{column}
\begin{column}{0.42\textwidth}
\begin{center}
\includegraphics[width=\columnwidth]{imgs/mech_transformer.png}
\end{center}
\end{column}
\end{columns}

---

# What is Mechanistic Interpretability?

---

# What is Mechanistic Interpretability?

\begin{columns}
\begin{column}{0.55\textwidth}
- **Goal:** Reverse engineer neural networks
  - Like reverse-engineering a compiled binary to source code
- **Hypothesis:** Models learn human-comprehensible algorithms and can be understood, if we learn how to make it legible
- Understanding **features** — the variables inside the model
- Understanding **circuits** — the algorithms learned to compute features
- **Key property:** Distinguishes between cognition with identical output
- A deep knowledge of circuits is crucial to understand, predict and **align** model behaviour
\end{column}
\begin{column}{0.42\textwidth}
\begin{center}
\includegraphics[width=\columnwidth]{imgs/mech_car_detector.png}
\end{center}
\end{column}
\end{columns}

---

# A Growing Area of Research

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/mech_growing_area1.png}
\end{center}

Mathematical Framework for Transformer Circuits [@elhage2021mathematical], Key-Value Memories, ROME, Gender Bias via Causal Mediation, Toy Models of Superposition [@elhage2022superposition], ...

---

# A Growing Area of Research

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/mech_growing_area2.png}
\end{center}

Multimodal Neurons, Compositional Explanations, Causal Abstractions, SGD Learns Parities, Curve Circuits, Quantization Model of Neural Scaling, ...

---

# Features = Variables: What Does the Model Know?

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/mech_multimodal_neurons.png}
\end{center}

Neurons respond to high-level semantic concepts: **regions, persons, emotions, religions, traits, art styles** — across multiple modalities (Goh et al., Distill 2021 / neuroscope.io)

---

# Features: Linear Representation of Quantities

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/mech_number_feature.png}
\end{center}

A neuron encoding **number (implicitly of people)** — activates on "150 guests", "six", "70 guests", "40 people" (Softmax Linear Units, Elhage et al.)

\begin{exampleblock}{Tool: Neuroscope (\texttt{neuroscope.io})}
Browse dataset examples maximally activating any neuron in GPT-2/GPT-Neo
\end{exampleblock}

**Open Problem:** Studying Learned Features

---

# Circuits = Functions: How Does the Model Think?

---

# Induction Heads: A Key Circuit

\begin{center}
\includegraphics[width=0.82\columnwidth]{imgs/mech_induction_heads.png}
\end{center}

\begin{block}{Induction Head (2-Layer Attention-Only Models)}
If the current token has appeared before, attend back to it and predict: \textbf{"copy the next token after the previous occurrence"}
\end{block}

- Layer 0: identifies "I follow [D]" at position $n$
- Layer 1: searches for tokens containing "I follow [D]" and copies the next logit

[@elhage2021mathematical] — **Open Problem:** Analysing Toy Language Models

---

# Mechanistic Understanding of Induction Heads

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/mech_induction_illustrated.png}
\end{center}

A complete mechanistic understanding: we can trace exactly how information flows through both layers to produce the induction behaviour (Callum McDougall)

---

# Case Study: Emergence of In-Context Learning

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/mech_in_context_learning.png}
\end{center}

- Models with $> 1$ layer have an **abrupt improvement** in in-context learning
- Induction heads form in a **phase change** during training
- Mechanistic interpretability explains *why* — induction heads enable pattern completion

[@olsson2022incontext] — **Open Problem:** Analysing Training Dynamics

---

# The Mindset of Mechanistic Interpretability

- **Alien neuroscience:** Models *are* interpretable, but not in our language — if we learn to think like them, mysteries dissolve
- **Skepticism:** It's extremely easy to trick yourself in interpretability
  - **Zoom In:** Rigour and depth over breadth and scalability
- **Ambition:** It *is* possible to achieve deep and rigorous understanding
- A bet that models have underlying principles and structures that **generalise**

\begin{exampleblock}{Personal Motivation (Neel Nanda)}
Easy to get started, fast feedback loops, cross between maths, CS, natural sciences and truth-seeking. Code early and often — get contact with reality.
\end{exampleblock}

---

# Case Study: Grokking

\begin{center}
\includegraphics[width=0.72\columnwidth]{imgs/mech_grokking.png}
\end{center}

\begin{alertblock}{Mystery}
Model perfectly memorises training data after $\sim$1K steps — then suddenly \textbf{generalises} after $\sim$100K more steps. Why?
\end{alertblock}

Grokking: Generalization Beyond Overfitting (Power et al.)

---

# The Modular Addition Circuit

\begin{center}
\includegraphics[width=0.88\columnwidth]{imgs/mech_modular_addition.png}
\end{center}

The model computes $(a + b) \mod p$ via **Fourier / trig identities**:
- Embedding maps $a \to \sin(wa),\cos(wa)$
- Attention computes $\sin(w(a{+}b)),\cos(w(a{+}b))$
- Unembed computes $\text{Logit}(c) \propto \cos(w(a{+}b{-}c))$

Grokking = transition from memorisation to using this elegant generalising algorithm

[@nanda2023progress] — **Open Problem:** Interpreting Algorithmic Models

---

# Frontier: Polysemanticity \& Superposition

---

# Polysemanticity: One Neuron, Many Concepts

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/mech_polysemanticity.png}
\end{center}

A single neuron activates for **"game"** across completely unrelated contexts: dice, poetry, fiction, sports. This is **polysemanticity** — one neuron represents many features.

**Open Problem:** Exploring Polysemanticity \& Superposition

---

# Hypothesis: Polysemanticity is due to Superposition

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/mech_superposition.png}
\end{center}

\begin{block}{Superposition Hypothesis (Elhage et al. 2022)}
As feature sparsity increases, models pack more features than dimensions using near-orthogonal directions — at the cost of "positive interference"
\end{block}

- **0\% sparsity:** 2 most important features get dedicated orthogonal dimensions
- **80\% sparsity:** 4 features embedded as antipodal pairs
- **90\% sparsity:** 5 features embedded as a pentagon

[@elhage2022superposition] — **Open Problem:** Exploring Polysemanticity \& Superposition

---

# Geometry of Superposition

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/mech_geometry_superposition.png}
\end{center}

As sparsity increases, features organise into **geometric structures**: dedicated dimensions → digons (antipodal pairs) → triangles → tetrahedra → pentagons → square antiprisms. Each structure packs more features per dimension.

[@elhage2022superposition]

---

# Case Study: Interpretability in the Wild

\begin{center}
\includegraphics[width=0.88\columnwidth]{imgs/mech_ioi_circuit.png}
\end{center}

**"When John and Mary went to the store, John gave the bag to $\to$ Mary"**

Full circuit found in GPT-2 small: Previous Token Heads $\to$ Duplicate Token Heads + Induction Heads $\to$ S-Inhibition Heads $\to$ Name Mover Heads

[@wang2022ioi] — **Open Problem:** Finding Circuits in the Wild

---

# Refining Ablations: Mechanistic Interpretability as Validation

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/mech_ablations.png}
\end{center}

Activation patching reveals **Backup Name Mover Heads** — heads that only activate when the primary Name Mover Heads are ablated. A **Negative Backup Head** also emerges, opposing the backup.

\begin{exampleblock}{Key insight}
Mechanistic understanding acts as a \textbf{validation set} — it reveals structure invisible to pure ablation studies
\end{exampleblock}

**Open Problem:** Techniques, Tooling and Automation

---

# Technique: Activation Patching

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/mech_activation_patching.png}
\end{center}

\begin{block}{Activation Patching}
Run two forward passes (clean and corrupted input). Patch one activation from the clean run into the corrupted run. Measure how much the output recovers — identifies which activations are causally important.
\end{block}

Used to localise factual associations in GPT (Meng et al., ROME) — **Open Problem:** Techniques, Tooling and Automation

---

# Linear Representation Hypothesis

\begin{center}
\includegraphics[width=0.78\columnwidth]{imgs/mech_linear_representation.png}
\end{center}

\begin{block}{Linear Representation Hypothesis}
Models represent features as \textbf{directions} in activation space — not as individual neurons. Models have underlying principles with predictive power.
\end{block}

- "king $-$ man $+$ woman $\approx$ queen" — gender as a linear direction
- Verb tense as a linear direction: walking $\to$ walked, swimming $\to$ swam

---

# Case Study: Emergent World Representations in Othello-GPT

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/mech_othello_gpt.png}
\end{center}

A transformer trained **only on legal Othello move sequences** develops an internal model of the board state — demonstrated via interventions that change the probe output as expected [@li2023othello]

---

# Othello-GPT: A Linear World Model

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/mech_othello_linear.png}
\end{center}

\begin{exampleblock}{Linear Representation Hypothesis confirmed}
Othello-GPT represents board state as \textit{"my colour vs their's"} — a linear model that \textbf{generalises}, \textbf{survives falsification}, and has \textbf{predictive power}
\end{exampleblock}

**Open Problem:** Future Work on Othello-GPT

---

# Learning More

\begin{columns}
\begin{column}{0.5\textwidth}
- **200 Concrete Open Problems in Mechanistic Interpretability**
  \newline \footnotesize\texttt{neelnanda.io/concrete-open-problems}
- **Getting Started in Mechanistic Interpretability**
  \newline \footnotesize\texttt{neelnanda.io/getting-started}
\end{column}
\begin{column}{0.5\textwidth}
- **A Comprehensive Mechanistic Interpretability Explainer**
  \newline \footnotesize\texttt{neelnanda.io/glossary}
- **TransformerLens** (Python library)
  \newline \footnotesize\texttt{github.com/neelnanda-io/TransformerLens}
\end{column}
\end{columns}

\vfill

\begin{alertblock}{Open Problems covered in this talk}
Studying Learned Features $\cdot$ Analysing Toy Language Models $\cdot$ Analysing Training Dynamics $\cdot$ Interpreting Algorithmic Models $\cdot$ Exploring Polysemanticity \& Superposition $\cdot$ Finding Circuits in the Wild $\cdot$ Techniques, Tooling and Automation $\cdot$ Future Work on Othello-GPT
\end{alertblock}

---

\begin{center}
\Huge Thank You!
\end{center}

---

# References {.allowframebreaks}

\footnotesize
