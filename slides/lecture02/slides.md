---
title: "\\emoji{wtf} XAI Lecture 02"
subtitle: "Probing Further into 'Interpretability': Caveats & Challenges"
bibliography: references.bib
---

# Agenda

- Two Papers:
  - Transparency: Motivations and Challenges
  - The Mythos of Model Interpretability
- Discussion

---

# The Mythos of Model Interpretability

\begin{center}
\includegraphics[width=.75\columnwidth]{imgs/liptom.png}
\end{center}
\vfill

[@lipton2018mythos] 

---

# Contributions

- **Goal:** Refine the discourse on interpretability
- Outline **desiderata of interpretability research**
  - Motivations for interpretability are often diverse and discordant
- Identifying **model properties and techniques** thought to confer interpretability

---

# Motivation

- We want models to be **not only good** w.r.t. predictive capabilities, **but also interpretable**
- Interpretation is **underspecified**
  - Lack of a formal technical meaning
- Papers provide **diverse and non-overlapping motivations** for interpretability

---

# Prior Work: Motivations for Interpretability

\begin{center}
\Large \textbf{Interpretability promotes trust}
\end{center}
\vfill
- But **what is trust?**
- Is it faith in model performance?
- If so, why are accuracy and other standard performance evaluation techniques inadequate?

---

# When is interpretability needed?

- Simplified optimization **objectives fail to capture complex real life goals**
  - Algorithm for hiring decisions – productivity **and** ethics
  - Ethics is hard to formulate
- Training data is **not representative of deployment environment**

\vfill

\begin{center}
\Large \textbf{Interpretability serves those objectives that we deem important but struggle to model formally!}
\end{center}


---

# Desiderata

\begin{center}
Understanding motivations for interpretability through the lens of prior literature:
\vfill
\includegraphics[width=.95\columnwidth]{imgs/desiderata.png}
\end{center}

---

# Desiderata: Trust

- Is trust simply confidence that the model will perform well?
\vfill
- A person might **feel at ease with a well understood model**, even if this understanding has no purpose
\vfill
- **Training and deployment objectives diverge**
  - E.g., model makes accurate predictions but not validated for racial biases
\vfill
- **Trust → relinquish control**
  - For which examples is the model right?

---

# Desiderata: Causality

- Researchers hope to **infer properties** (beyond correlational associations) from **interpretations/explanations**
  - Regression reveals strong association between smoking and lung cancer
- However, **task of inferring causal relationships from observational data is a field in itself**
  - [Judea Pearl](https://en.wikipedia.org/wiki/Judea_Pearl) (*left*)
  - [Don Rubin](https://en.wikipedia.org/wiki/Donald_Rubin) (*right*)

\vfill
\begin{center}
\includegraphics[width=.38\columnwidth]{imgs/rubin_pearl.png}
\end{center}

---

# Desiderata: Transferability

- Humans exhibit **richer capacity to generalize, transferring learned skills** to unfamiliar situations
  - Model’s generalization error: gap between performance on training and test data
  - We already use ML in non-stationary environments

\vfill

- **Environment might even be adversarial**
  - Changing pixels in an image tactically could throw off models but not humans

\vfill  

- **Predictive models can often be gamed**
  - In such cases, predictive power loses meaning


---

# Desiderata: Informativeness

- **Predictions → Decisions**
  - Convey additional information to human decision makers
\vfill
- **Example:** Which conference should I target?
  - A one word answer is not very meaningful
\vfill
- **Interpretation might be meaningful even if it does not shed light on model's inner workings**
  - Similar cases for a doctor in support of a diagnosis

---

# Desiderata: Fair & Ethical Decision Making

- **ML is being deployed in critical settings**
  - E.g., healthcare
\vfill

- How can we be sure **algorithms do not discriminate** on the basis of race?
  - AUC is not good enough

\vfill

## Side note
  
  European Union enforces the **Right to explanation**

---

# Properties of Interpretable Models

- **Transparency**
  - How exactly does the model work?
  - Details about its inner workings, parameters etc.

\vfill

- **Post-hoc explanations**
  - What else can the model tell me?
  - E.g., visualizations of learned model, explaining by example

---

# Transparency: Simulatability

- **Can a person contemplate the entire model at once?**
  - Need a very simple model

\vfill

- A human should be able to **take input data and model parameters and calculate prediction**

---

# Transparency: Decomposability

- **Understanding each input, parameter, calculation**
  - E.g., decision trees, linear regression

\vfill

- **Inputs must be interpretable**
  - Models with highly engineered or anonymous features are not decomposable

---

# Transparency: Algorithmic Transparency

- **Learning algorithm itself is transparent**
  - E.g., linear models (error surface, unique solution)

\vfill

- Modern **deep learning methods lack this kind of transparency**
  - We don't understand how the optimization methods work
  - No guarantees of working on new problems

\vfill

## Note:
Humans do not exhibit any of these forms of transparency

---

# Post-hoc: Text Explanations

- Humans often justify decisions verbally (post-hoc)

\vfill

In **Learning from explanations using sentiment and advice in RL** [@krening2016learning]

- **Krening et. al. 2016:** {Learning from explanations using sentiment and advice in RL}
  - One model is a reinforcement learner
  - Another model maps models states onto verbal explanations
  - Explanations are trained to maximize likelihood of ground truth explanations from human players
  - So: **explanations do not faithfully describe agent decisions, but rather human intuition**

\vfill

\begin{center}
\includegraphics[width=.70\columnwidth]{imgs/thoughtland.png}\\
\small Thoughtland’s architecture from 
\end{center}

[@duboue2013feasibility]

---

# Post-hoc: Visualization

- **Visualize high-dimensional data with t-SNE**
  - 2D visualizations in which nearby data points appear close

\vfill

- Perturb input data to enhance **activations of certain nodes in neural nets** (image classification)
  - Helps understand which nodes corresponds to what aspects of the image
  - E.g., certain nodes might correspond to dog faces

\vfill

\begin{center}
\includegraphics[width=.40\columnwidth]{imgs/tsne.png}
\end{center}


---

# Post-hoc: Example Explanations

- Reasoning with **examples**
  - E.g., Patient A has a tumor because he is similar to these k other data points with tumors
\vfill
- k-neighbors can be computed by using some distance metric on learned representations
  - E.g., word2vec [@mikolov2013efficient]

\vfill

\begin{center}
\includegraphics[width=.80\columnwidth]{imgs/word2vec.png}
\end{center}

---

# Post-hoc: Local Explanations

- **Hard to explain a complex model in its entirety**
  - How about explaining **smaller regions**? [@ribeiro2016should]

\vfill

\begin{center}
\includegraphics[width=.25\columnwidth]{imgs/lime.png}
\end{center}


\vfill

- Explains decisions of any model in a local region around a particular point
- Learns sparse linear model

---

# Transparency and Post-hoc Key Insights

\begin{center}
\Large
\textbf{Claims about interpretability must be qualified}
\end{center}

\vfill

- If a model satisfies a form of transparency, highlight that clearly
- For post-hoc interpretability, fix a clear objective and demonstrate evidence

---

# Post-hoc Potential Issues

\begin{center}
\Large
\textbf{Transparency may be at odds with broader objectives of AI}
\end{center}

\vfill

**Example:** Health care

- Choosing interpretable models over accurate ones **to convince decision makers**
- Short term goal of building trust with doctors **might clash** with long term goal of improving health care

---

# Post-hoc interpretations can mislead

\begin{center}
\Large
\textbf{Do not blindly embrace post-hoc explanations!}
\end{center}

\vfill

- Post-hoc explanations can seem **plausible but be misleading**
  - They do not claim to open up the black-box
  - They only provide plausible explanations for its behavior
  - E.g., text explanations

---

# Summary: The Mythos of Model Interpretability

- **Goal:** Refine the discourse on interpretability
\vfill
- Outline **desiderata of interpretability research**
  - Motivations for interpretability are often diverse and discordant
\vfill
- Identifying **model properties and techniques** thought to confer interpretability

---

# Transparency: Challenges and Motivation


\vfill

\begin{center}
\includegraphics[width=.85\columnwidth]{imgs/weller.png}
\end{center}

[@weller2019transparency] 

---

# Contributions

- Characterizing different kinds of transparency, and underlying motivations
- Shedding light on the downsides of having transparency

---

# Types and Goals of Transparency 

- **Type 1:** For a developer, to understand how their system is working, aiming to debug or improve it: to see what is working well or badly, and get a sense for why (**`Internal Debugging`**).

- **Type 2:** For a user, to provide a sense for what the system is doing and why, to enable prediction of what it might do in unforeseen circumstances and build a sense of trust in the technology (**`User Trust`**).

- **Type 3:** For society broadly to understand and become comfortable with the strengths and limitations of the system, overcoming a reasonable fear of the unknown (**`Social Acceptance`**).

\vfill
\begin{center}
\small \textbf{I made up the names myself} \emoji{smiling-face-with-sunglasses}
\end{center}

---

# Types and Goals of Transparency (cont.)

- **Type 4:** For a user to understand why one particular prediction or decision was reached, to allow a check that the system worked appropriately and to enable meaningful challenge (e.g. credit approval or criminal sentencing) (**`Individual Explanation`**).

- **Type 5:** To provide an expert (perhaps a regulator) the ability to audit a pre-diction or decision trail in detail, particularly if something goes wrong (e.g. a crash by an autonomous car). This may require storing key data streams and tracing through each logical step, and will facilitate assignment of accountability and legal liability (**`Expert Audit`**).

\vfill
\begin{center}
\small \textbf{I made up the names myself} \emoji{smiling-face-with-sunglasses}
\end{center}

---

# Types and Goals of Transparency (cont.)

- **Type 6:** To facilitate monitoring and testing for safety standards (**`Safety Monitoring`**). 

- **Type 7:** To make a user (the audience) feel comfortable with a prediction or decision so that they keep using the system. Beneficiary: deployer (**`User Comfort`**).

- **Type 8:** To lead a user (the audience) into some action or behavior (**`Behavioral Influence`**).
  - e.g. Amazon might recommend a product, providing an explanation in order that you will then click through to make a purchase. Beneficiary: deployer.

\vfill
\begin{center}
\small \textbf{I made up the names myself} \emoji{smiling-face-with-sunglasses}
\end{center}

---

# Transparency: Global vs. Local

- **Global**
  - Understanding whole system
  - Types 2 (User Trust) – 3 (Social Acceptance)
\vfill
- **Local**
  - Explanation for a particular prediction
  - Types 4 (Individual Explanation), 5 (Expert Audit), 6 (Safety Monitoring), 7 (User Comfort), 8 (Behavioral Influence)

---

# Key Challenges

\begin{center}
\Large \textbf{Explanations are beneficial to the society only if they are faithful}
\end{center}

\vfill

- Defining criteria and tests for practical faithfulness are important open problems
  - **Context is important!** 

\vfill
\begin{center}
\includegraphics[width=.80\columnwidth]{imgs/context.png}
\end{center}


---

# Key Challenges (cont.)

\begin{center}
\Large \textbf{Understanding and Communication is hard}
\end{center}

\vfill

- Is an explanation good at conveying faithful information in understandable form, and if a human has actually understood it well?
- Context dependent
- Need for deeper probing!

\vfill
\begin{center}
\includegraphics[width=.40\columnwidth]{imgs/boromir.png}
\end{center}

---

# Key Challenges (cont.) 

\begin{center}
\Large \textbf{Comparing Explanations is HARD!}
\end{center}

\vfill

\begin{center}
\includegraphics[width=.60\columnwidth]{imgs/saliency.png} \\
\textbf{If we have different saliency maps, how to know which one is better}
\end{center}

[@gulshad2020explaining]




---

# Possible Dangers: Audience vs. Beneficiary

- **Recommender systems**
  - Amazon (Beneficiary) and its Users (Audience)

\vfill

- **Healthcare**
  - [Google Verily](https://verily.com/) (Beneficiary) and Hospitals/Doctors (Audience)

\vfill

- **Criminal Justice**
  - [COMPAS](https://en.wikipedia.org/wiki/COMPAS_(software)) (Beneficiary) and Courts/Judges (Audience)

---

# Posible Dangers: Government Use of Algorithms (cont.)

- [COMPAS](https://en.wikipedia.org/wiki/COMPAS_(software)) system predicts risk of recidivism
- A prisoner should have some transparency into the decision made by COMPAS
  - To ensure **proper process has been followed**
  - Enable potential challenge
- But, **can there be too much transparency?** (Next topic)
- Also, recent push for making all code/data for such models public. Good idea?

\vfill

## COMPAS Violent recidivism risk scale (Wikipedia version)

The violent recidivism score is meant to predict violent offenses following release. The scale uses data or indicators that include a person's "history of violence, history of non-compliance, vocational/educational problems, the person's age-at-intake and the person's age-at-first-arrest [@enwiki:1303968797]


---

# Posible Dangers: Government Use of Algorithms (cont.)


The violent recidivism risk scale is calculated as follows:

$$s = a(-w) + a_{\text{first}}(-w) + h_{\text{violence}} w + v_{\text{edu}} w + h_{\text{nc}} w$$

where:

**$s$** is the violent recidivism risk score, **$w$** is a weight multiplier , **$a$** is current age, **$a_{\text{first}}$** is the age at first arrest, **$h_{\text{violence}}$** is the history of violence, **$v_{\text{edu}}$** is vocational education scale, and **$h_{\text{nc}}$** is history of noncompliance

The weight, $w$, is *"determined by the strength of the item's relationship to person offense recidivism that we observed in our study data."* [@enwiki:1303968797]

---

# Posible Dangers: Gaming, IP Incentives, and Privacy

- If all details available, the process can be **gamed**
- Less incentive for private IP and slow progress
- Privacy and transparency are often in **conflict**
  - How much transparency is too much in a setting?

\vfill
\begin{center}
\includegraphics[width=.65\columnwidth]{imgs/gamification.png}
\end{center}

---

# Means and Ends

- Transparency → reliability, fairness
- If we are able to develop a good set of "safety checks", then may be it is ok to not have full transparency
  - E.g., autonomous vehicles

\vfill
\begin{center}
\includegraphics[width=.40\columnwidth]{imgs/selfdrive.png}
\end{center}

---

# Societal Considerations

\begin{center}
\large \textbf{Does giving more information to each individual help society?}
\end{center}

\begin{block}{Braess’ paradox}
More information empowers the agents to optimize their own agendas more efficiently, and thus may lead to a worse global outcome
\end{block}

\begin{center}
\includegraphics[width=.25\columnwidth]{imgs/bender.png}
\end{center}

---

# Selective Transparency & Discrimination

- Selective Transparency may hurt people disproportionately

- Furthermore, transparency about certain attributes (e.g., gender) in certain settings is known to cause discriminatory behavior as well


# References {.allowframebreaks}

\footnotesize