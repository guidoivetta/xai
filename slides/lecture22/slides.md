---
title: "\\emoji{wtf} XAI: Compiled Transformers as a Laboratory for Interpretability"
bibliography: references.bib

---

# Disclaimer

\input{../disclaimer.tex}

---

# Compiled Transformers as a Laboratory for Interpretability

\begin{center}
\Large\textbf{Compiled Transformers as a Laboratory for Interpretability}
\end{center}

\vspace{1em}

\begin{center}
David Lindner, János Kramár, Matthew Rahtz, Tom McGrath, Vladimir Mikulik

\vspace{0.5em}

DeepMind — April 2023
\end{center}

[@lindner2023compiled]

---

# The Core Problem: No Ground Truth

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/no_ground_truth.png}
\end{center}

\begin{alertblock}{Problem}
Interpretability is hard because there is \textbf{no ground truth} to verify explanations against.
\end{alertblock}

---

# What If We Had Ground Truth?

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/ground_truth_loop.png}
\end{center}

If we build a network from a **known mechanism**, we can check whether the explanation matches what we compiled in.

---

# Introducing Tracr: A Transformer Compiler for RASP

\begin{center}
\includegraphics[width=0.7\columnwidth]{imgs/tracr_intro.png}
\end{center}

\begin{center}
Known Mechanism (RASP program) $\longrightarrow$ Neural Network weights
\end{center}

[@lindner2023compiled]

---

# Plan for Today

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/plan_overview.png}
\end{center}

\begin{enumerate}
\item Building a \textbf{compiler} for transformer models
\item Studying \textbf{superposition} in compiled models
\end{enumerate}

---

# Part 1: Building the Compiler

---

# Hand-Coding Weights: Useful but Not Scalable

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/hand_coding.png}
\end{center}

- Hand-coding weights $\Rightarrow$ very good measure of understanding, but \textbf{difficult to scale}
- This approach is like **programming in byte-code**

{\footnotesize Cammarata et al., "Curve Circuits", Distill, 2021}

---

# Tracr Analogous to a Compiler Pipeline

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/compiler_analogy.png}
\end{center}

| Tracr | Traditional compiler |
|---|---|
| RASP | Programming language |
| craft | Assembly |
| Neural network | Machine code |

---

# Three-Step Translation

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/three_steps.png}
\end{center}

1. **RASP** — human-readable domain-specific language
2. **craft** — basis-independent representation of vector spaces and transformers
3. **Neural network weights** — standard transformer implementation

---

# RASP: A Language for Transformer Computations

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/rasp_language.png}
\end{center}

\begin{columns}
\begin{column}{0.48\textwidth}
\textbf{Arbitrary element-wise functions} \texttt{f( )}

$\longleftrightarrow$ MLP layers
\end{column}
\begin{column}{0.48\textwidth}
\textbf{"Select-aggregate" operations} $\square$

$\longleftrightarrow$ Attention layers (with some limitations)
\end{column}
\end{columns}

\vspace{0.5em}

RASP = "Restricted Access Sequence Programming"

{\footnotesize Weiss, Gail, Yoav Goldberg, and Eran Yahav. "Thinking like transformers." ICML 2021.} [@weiss2021thinking]

---

# An Example RASP Program

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/rasp_example.png}
\end{center}

```
is_x     = (tokens == "x")
prevs    = select(indices, indices, <=)
frac_prev = aggregate(prevs, is_x)
```

On `["a", "x", "b", "x", "c"]`:
- `is_x` $= [0, 1, 0, 1, 0]$
- `frac_prev` $= [0,\; 1/2,\; 1/3,\; 2/4,\; 2/5]$

---

# Translating a RASP Program into a craft Transformer

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/rasp_to_craft.png}
\end{center}

\begin{columns}
\begin{column}{0.45\textwidth}
\textbf{Step 1:} Create computational graph

\textbf{Step 2:} Infer inputs/outputs

\textbf{Step 3:} Create model components

\textbf{Step 4:} Assign components to layers

\textbf{Step 5:} Assemble craft model
\end{column}
\begin{column}{0.52\textwidth}
Result: \texttt{no-op attn} $\to$ \texttt{MLP: is\_x} $\to$ \texttt{Attn: prevs} $\to$ \texttt{no-op mlp}
\end{column}
\end{columns}

---

# Implementing MLP Layers

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/mlp_implementation.png}
\end{center}

\begin{columns}
\begin{column}{0.48\textwidth}
\begin{block}{Categorical variables}
MLP = \textbf{Lookup table}
\end{block}
\end{column}
\begin{column}{0.48\textwidth}
\begin{block}{Numerical variables}
\textbf{Approximate using ReLU}

Exact on a discrete set of possible inputs.
\end{block}
\end{column}
\end{columns}

---

# Implementing Attention Heads

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/attention_implementation.png}
\end{center}

- \texttt{select(indices, indices, <=)} $\;\longrightarrow\; W_Q^T W_K$
- \texttt{aggregate(prevs, is\_x)} $\;\longrightarrow\; W_O^T W_V$
- Use **low softmax temperature** to make attention patterns binary
- Add **beginning-of-sequence (BOS)** token to handle "attend to nothing"

---

# craft Models Map to Any Transformer

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/craft_to_transformer.png}
\end{center}

- craft = abstract representation making it easy to reason about vector spaces
- Can be mapped to **any GPT-like transformer** implementation
- Primarily supports a standard **haiku** transformer implementation

---

# Capabilities and Limitations of Tracr

\begin{columns}
\begin{column}{0.48\textwidth}
\begin{exampleblock}{Programs we can compile}
\begin{itemize}
\item Count tokens and compute histograms
\item Detect all occurrences of a pattern
\item Sort the input sequence
\item Check balanced parentheses (Dyck-$n$)
\end{itemize}
\end{exampleblock}
\end{column}
\begin{column}{0.48\textwidth}
\begin{alertblock}{Limitations of RASP}
\begin{itemize}
\item Binary attention patterns
\item Designed for algorithmic, not probabilistic tasks
\item Programs still close to transformer architecture
\end{itemize}
\end{alertblock}

\begin{alertblock}{Limitations of Tracr}
\begin{itemize}
\item Resulting models are large and inefficient
\item Many possible optimizations missing
\item Some advanced RASP features unsupported
\end{itemize}
\end{alertblock}
\end{column}
\end{columns}

---

# We Can Now Compile RASP Programs!

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/compiled_residual_stream.png}
\end{center}

Residual stream visualization: Input $\to$ no-op Attn $\to$ \textbf{MLP: is\_x indicator} $\to$ \textbf{Attn: fraction} $\to$ no-op MLP

---

# Part 2: Studying Superposition in Compiled Models

---

# The Superposition Hypothesis

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/superposition_hypothesis.png}
\end{center}

- **Obs 1:** Neurons sometimes correspond to clearly interpretable features {\footnotesize [Cammarata et al., "Thread: Circuits", Distill, 2020]}
- **Obs 2:** Neurons sometimes represent *multiple* interpretable features {\footnotesize [Olah et al., "Feature Visualization", Distill, 2017]}
- **Obs 3:** A linear representation can embed **exponentially more features than dimensions** {\footnotesize [Elhage et al., "Toy Models of Superposition", 2022]}

[@elhage2022superposition]

---

# Superposition and Polysemanticity

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/superposition_polysemanticity.png}
\end{center}

- Neural networks simulate a **larger network with disentangled features**
- These hypothetical features are **projected** into the actual network via superposition
- This results in **polysemanticity** when looking at single neurons

{\footnotesize Elhage et al., "Toy Models of Superposition", Transformer Circuits Thread, 2022.}

---

# Superposition Occurs in Toy Models

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/toy_model_superposition.png}
\end{center}

$h = Wx, \quad x' = \text{ReLU}(W^T h + b), \quad L = \sum_x \sum_i I_i (x_i - x'_i)^2$

Empirical result: features are stored in superposition when they are **sparse**, **important**, and the model has **fewer dimensions than features**.

---

# Compressing Tracr Models to Induce Superposition

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/compress_tracr.png}
\end{center}

\begin{columns}
\begin{column}{0.48\textwidth}
\textbf{Toy model conditions:}
\begin{enumerate}
\item Features are \textbf{sparse}
\item Some features more \textbf{important}
\item Model uses \textbf{fewer dimensions}
\end{enumerate}
\end{column}
\begin{column}{0.48\textwidth}
\textbf{In Tracr models:}
\begin{enumerate}
\item Features are \textbf{sparse} \checkmark
\item Some features more \textbf{important} \checkmark
\item Can we \textbf{compress} to fewer dimensions?
\end{enumerate}
\end{column}
\end{columns}

\vspace{0.5em}

\textbf{Motivation:} Learn about superposition in realistic models; make Tracr models more naturalistic.

---

# Linearly Compressing the Residual Stream

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/linear_compression.png}
\end{center}

Train only $W \in \mathbb{R}^{D \times d}$ to minimize:

$$\mathcal{L}(W, x) = \mathcal{L}_\text{out}(W, x) + \mathcal{L}_\text{layer}(W, x)$$

- $\mathcal{L}_\text{out}$: minimize output loss $\ell(f(x),\, \hat{f}_W(x))$
- $\mathcal{L}_\text{layer} = \sum_i (h_i(x) - \hat{h}_{W,i}(x))^2$: implement the same computation at each layer

---

# Embeddings Show Superposition

\begin{center}
\includegraphics[width=0.85\columnwidth]{imgs/embeddings_superposition.png}
\end{center}

The learned $W^T W$ (embedding size 8) is **qualitatively different** from the PCA solution — features with low importance and high linear independence are stored in superposition.

---

# Which Features Are Stored in Superposition?

\begin{center}
\includegraphics[width=0.75\columnwidth]{imgs/which_features_superposition.png}
\end{center}

Features stored in superposition are determined by:

- **Feature importance** (weight in loss)
- **Feature density** (sparsity)
- **Linear independence** (correlation with other features)

\begin{alertblock}{Open question}
Can we find a more \textbf{predictive} description of which features will be stored in superposition?
\end{alertblock}

---

# Future Directions for Tracr

\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/future_work.png}
\end{center}

**Making Tracr models more naturalistic:**

1. Can we use Tracr to create **evaluation benchmarks** for interpretability tools?
2. Can we **revert superposition** in Tracr models? (e.g., sparse coding, dictionary learning)
3. Can we use Tracr to **manually replace** model components that we (think we) understand?

---

# Summary

\begin{columns}
\begin{column}{0.55\textwidth}
\begin{itemize}
\item \textbf{Tracr}: RASP program $\to$ transformer weights with known mechanism
\item Provides \textbf{ground truth} for evaluating interpretability methods
\item Compiler pipeline: RASP $\to$ craft $\to$ neural network
\item Compiled models \textbf{exhibit superposition} when residual stream is compressed
\item Superposition follows toy-model predictions: importance, density, linear independence
\end{itemize}
\end{column}
\begin{column}{0.42\textwidth}
\begin{exampleblock}{Open source}
\url{https://github.com/deepmind/tracr}

\vspace{0.5em}

arXiv: 2301.05062
\end{exampleblock}
\end{column}
\end{columns}

---

\begin{center}
\Huge Thank You!
\end{center}

---

# References {.allowframebreaks}

\footnotesize
