---
title: "\\emoji{wtf} XAI: Inherently Interpretable Models"
bibliography: references.bib
---

# Agenda

- Recap: Interpretability Overview
- Inherently Interpretable Models
  - Linear Models
  - Decision Trees
  - Rule-Based Models
  - Generalized Additive Models (GAMs)
- Trade-offs: Accuracy vs. Interpretability
- Discussion

---

# Recap: What is Interpretability?

\\begin{definition}{}
\\begin{center}
\\Large Ability to explain or to present in understandable terms to a human
\\end{center}
\\end{definition}

**Key Points:**

- Not all ML systems require interpretability
- Needed when problem formalization is incomplete
- Multiple desiderata: Trust, Causality, Transferability, Fairness

---

# Recap: Two Approaches to Model Understanding

**Approach 1: Inherently Interpretable Models**

- Build models that are interpretable by design
- E.g., linear models, decision trees, rule lists

**Approach 2: Post-hoc Explanations**

- Explain complex black-box models after training
- E.g., LIME, SHAP, saliency maps

\\begin{center}
\\textbf{Today: Focus on Inherently Interpretable Models}
\\end{center}

---

# Why Inherently Interpretable Models?

**Advantages:**

- Transparency at every step
- Easier to debug and validate
- Natural explanations from model structure
- Often satisfy regulatory requirements

**Challenges:**

- May have lower predictive accuracy
- Limited expressiveness for complex patterns
- Scalability concerns for high-dimensional data

---

# Linear Models

\\begin{center}
\\textbf{The Simplest Interpretable Model}
\\end{center}

**Linear Regression:**

$$y = \\beta_0 + \\beta_1 x_1 + \\beta_2 x_2 + \\ldots + \\beta_p x_p + \\epsilon$$

**Logistic Regression:**

$$P(y=1|x) = \\frac{1}{1 + e^{-(\\beta_0 + \\beta_1 x_1 + \\ldots + \\beta_p x_p)}}$$

<!-- \\includegraphics[width=1.0\\columnwidth]{imgs/linear_model.png} -->

---

# Linear Models: Interpretability

**Why are they interpretable?**

- **Coefficients** $\\beta_i$ show feature importance
- **Sign** indicates direction of effect (positive/negative)
- **Magnitude** indicates strength of effect
- **Additivity** makes reasoning straightforward

**Example:** Credit scoring

- $\\beta_{\\text{income}} = +0.5$: Higher income increases approval probability
- $\\beta_{\\text{debt}} = -0.3$: Higher debt decreases approval probability

---

# Linear Models: Limitations

**When do linear models struggle?**

- **Non-linear relationships**
  - E.g., U-shaped or threshold effects

- **Feature interactions**
  - Effect of age depends on income

- **Complex decision boundaries**
  - XOR-like patterns

<!-- \\includegraphics[width=1.0\\columnwidth]{imgs/linear_limits.png} -->

---

# Making Linear Models More Expressive

**Techniques:**

1. **Polynomial features**: $x_1, x_1^2, x_1^3, \\ldots$
2. **Interaction terms**: $x_1 \\times x_2$
3. **Basis expansion**: Splines, wavelets

**Trade-off:**

- Increased expressiveness
- Decreased interpretability (more coefficients)
- Risk of overfitting

---

# Regularization for Interpretability

**Sparse Linear Models:**

**LASSO (L1 regularization):**

$$\\min_{\\beta} \\sum_{i=1}^{n} (y_i - \\beta^T x_i)^2 + \\lambda \\sum_{j=1}^{p} |\\beta_j|$$

**Benefits:**

- Automatic feature selection (some $\\beta_j = 0$)
- Improves interpretability by reducing features
- Prevents overfitting

<!-- \\includegraphics[width=1.0\\columnwidth]{imgs/lasso.png} -->

---

# Decision Trees

\\begin{center}
\\textbf{Hierarchical Decision Making}
\\end{center}

**Structure:**

- Internal nodes: Feature-based splits
- Edges: Decision outcomes
- Leaf nodes: Predictions

**Example:** Medical diagnosis

```
Is fever > 38°C?
├─ Yes: Is cough present?
│  ├─ Yes: Predict Flu (80%)
│  └─ No: Predict Infection (60%)
└─ No: Predict Healthy (95%)
```

<!-- \\includegraphics[width=1.0\\columnwidth]{imgs/decision_tree.png} -->

---

# Decision Trees: Training

**CART Algorithm** (Classification and Regression Trees)

**Splitting criteria:**

- **Classification**: Gini impurity, Entropy
- **Regression**: Mean squared error

**Gini Impurity:**

$$G = 1 - \\sum_{i=1}^{C} p_i^2$$

where $p_i$ is the proportion of class $i$ in the node.

---

# Decision Trees: Interpretability

**Why are they interpretable?**

- **Visual structure**: Easy to draw and understand
- **Logical rules**: Can be expressed as IF-THEN statements
- **Feature importance**: By split position and frequency
- **Non-parametric**: No distributional assumptions

**Simulatability:**

- Small trees can be mentally traced
- Clear decision path for each prediction

---

# Decision Trees: Limitations

**Challenges:**

1. **Instability**: Small data changes → large tree changes
2. **Overfitting**: Deep trees memorize training data
3. **Greedy learning**: Locally optimal splits may not be globally optimal
4. **Bias towards features with many levels**

**Size-Interpretability Trade-off:**

- Small trees: Interpretable but may underfit
- Large trees: More accurate but less interpretable

<!-- \\includegraphics[width=1.0\\columnwidth]{imgs/tree_complexity.png} -->

---

# Rule-Based Models

\\begin{center}
\\textbf{Sets of IF-THEN Rules}
\\end{center}

**General Form:**

```
IF (condition₁ AND condition₂ AND ...) THEN prediction
```

**Types:**

1. **Unordered rules**: All rules evaluated independently
2. **Ordered rules (decision lists)**: Rules evaluated sequentially
3. **Rule sets**: Collections with priority/conflict resolution

---

# Rule Lists

**Sequential Decision Making**

[@letham2015interpretable]

**Example: Stroke Risk Assessment**

```
IF (age ≥ 75) THEN high_risk
ELSE IF (age ≥ 65 AND diabetes = yes) THEN high_risk
ELSE IF (hypertension = yes AND smoking = yes) THEN medium_risk
ELSE low_risk
```

**Properties:**

- Rules evaluated in order (like switch/case)
- First matching rule determines prediction
- Default rule at the end

<!-- \\includegraphics[width=1.0\\columnwidth]{imgs/rule_list.png} -->

---

# Rule Lists: Learning

**Bayesian Rule Lists (BRL)** [@letham2015interpretable]

**Objective:**

- Find short, accurate rule lists
- Balance between accuracy and simplicity
- Use Bayesian approach for model selection

**Key Idea:**

$$P(\\text{model}|\\text{data}) \\propto P(\\text{data}|\\text{model}) \\times P(\\text{model})$$

- Prior favors shorter lists (Occam's razor)
- Posterior balances fit and complexity

---

# Rule Sets

**Non-Sequential Rules**

[@lakkaraju2016interpretable]

**Example: Loan Approval**

```
Rule 1: IF (income > 50K AND credit_score > 700) THEN approve [support=35%, accuracy=92%]
Rule 2: IF (age > 30 AND employed=yes) THEN approve [support=28%, accuracy=85%]
Rule 3: IF (debt_ratio < 0.3) THEN approve [support=22%, accuracy=88%]
Default: reject
```

**Differences from Rule Lists:**

- Multiple rules can match simultaneously
- Need conflict resolution strategy
- More flexible but potentially less interpretable

<!-- \\includegraphics[width=1.0\\columnwidth]{imgs/rule_set.png} -->

---

# Interpretable Rule Sets

**Learning Certifiably Optimal Rule Lists (CORELS)** [@angelino2017learning]

**Goals:**

- Provably optimal rule lists
- User-specified interpretability constraints
- Efficient learning via branch-and-bound

**Falling Rule Lists** [@wang2017falling]

- Rules with monotonically decreasing probability
- Natural ordering by confidence
- Easier to understand and trust

---

# Rule-Based Models: Interpretability

**Advantages:**

- **Logical transparency**: Clear reasoning path
- **Modular**: Each rule can be understood independently
- **Actionable**: Rules suggest interventions
- **Domain alignment**: Can incorporate expert knowledge

**Measuring Interpretability:**

- Number of rules
- Average rule length (number of conditions)
- Overlap between rules
- Consistency with domain knowledge

---

# Generalized Additive Models (GAMs)

\\begin{center}
\\textbf{Flexible Yet Interpretable}
\\end{center}

**Model Form:**

$$g(E[y]) = \\beta_0 + f_1(x_1) + f_2(x_2) + \\ldots + f_p(x_p)$$

where:
- $g$ is a link function
- $f_i$ are smooth functions (e.g., splines)

**Key Property:** Additivity is preserved, but functions can be non-linear

<!-- \\includegraphics[width=1.0\\columnwidth]{imgs/gam.png} -->

---

# GAMs: Interpretability

**Why are GAMs interpretable?**

- **Additive structure**: Each feature contributes independently
- **Visualizable**: Can plot $f_i(x_i)$ for each feature
- **Shape functions**: Reveal complex patterns (U-shapes, thresholds)
- **No feature interactions**: Simplifies reasoning

**Example Interpretation:**

- Plot shows age effect is non-linear (U-shaped)
- Risk increases for very young and very old
- Middle age has lowest risk

<!-- \\includegraphics[width=1.0\\columnwidth]{imgs/gam_shape.png} -->

---

# GAMs: Extensions

**Limitations of Standard GAMs:**

- No interactions between features
- May miss important combined effects

**GA²Ms** (Generalized Additive² Models) [@lou2013accurate]

$$g(E[y]) = \\beta_0 + \\sum_i f_i(x_i) + \\sum_{i<j} f_{ij}(x_i, x_j)$$

**Benefits:**

- Captures pairwise interactions
- Maintains interpretability (can visualize pairs)
- Better accuracy than GAMs

---

# Explainable Boosting Machines (EBM)

[@nori2019interpretml; @lou2012intelligible]

**Modern GAMs with Boosting:**

- Use gradient boosting to learn shape functions
- Automatically detect and include interactions
- State-of-the-art accuracy among interpretable models

**InterpretML Library:**

- Open-source implementation
- Visualization tools
- Comparison with other interpretable models

<!-- \\includegraphics[width=1.0\\columnwidth]{imgs/ebm.png} -->

---

# Accuracy vs. Interpretability Trade-off

\\begin{center}
\\textbf{The Central Dilemma}
\\end{center}

<!-- \\includegraphics[width=1.0\\columnwidth]{imgs/accuracy_interpretability.png} -->

**General Pattern:**

- Linear models: High interpretability, lower accuracy
- Decision trees: Moderate on both dimensions
- GAMs/EBMs: Good balance
- Neural networks: High accuracy, low interpretability

**Question:** Is this trade-off fundamental or an artifact of our methods?

---

# Case Study: COMPAS Risk Assessment

[@dressel2018accuracy]

**Context:**

- Criminal justice recidivism prediction
- COMPAS: Proprietary black-box system
- Controversy over accuracy and fairness

**Findings:**

- Simple linear models matched COMPAS accuracy
- Interpretable models performed competitively
- Non-experts could achieve similar performance with simple rules

**Implications:**

- Complex models may not always be necessary
- Interpretability can be achieved without sacrificing accuracy

---

# When Interpretable Models Fall Short

**High-Dimensional Data:**

- Images, text, speech
- Too many features for simple models

**Complex Interactions:**

- Non-additive effects
- High-order dependencies

**Representation Learning:**

- Need to learn features, not just weights
- E.g., word embeddings, image features

\\begin{center}
\\textbf{In these cases, post-hoc explanations become necessary}
\\end{center}

---

# Hybrid Approaches

**Combining Interpretability and Accuracy:**

1. **Distillation**: Train complex model, then distill to interpretable one
   - [@craven1996extracting; @frosst2017distilling]

2. **Selective Prediction**: Use interpretable model when confident, complex model otherwise

3. **Hierarchical Models**: Interpretable model makes coarse decisions, complex model refines

<!-- \\includegraphics[width=1.0\\columnwidth]{imgs/hybrid.png} -->

---

# Best Practices: Choosing Interpretable Models

**Guidelines:**

1. **Start simple**: Try linear models first
2. **Understand trade-offs**: Accuracy vs. interpretability for your domain
3. **Consider stakeholders**: Who needs to understand the model?
4. **Validate interpretations**: Are explanations actually meaningful?
5. **Measure interpretability**: Use proxy metrics (model size, depth, etc.)

**Questions to Ask:**

- Can domain experts validate the model's logic?
- Can users simulate model predictions mentally?
- Are the features themselves interpretable?

---

# Evaluation of Interpretable Models

**Beyond Accuracy:**

1. **Functional Metrics**:
   - Model size (number of parameters/rules)
   - Model depth (for trees)
   - Number of non-zero coefficients

2. **Human Studies**:
   - Can users understand the model?
   - Can users predict model behavior?
   - Do users trust the model more?

3. **Task Performance**:
   - Debugging: Can users find errors?
   - Decision support: Does model improve decisions?

---

# Research Frontiers

**Open Challenges:**

1. **Theory**: Formal definitions of interpretability
2. **Scaling**: Interpretable models for big data
3. **Deep Learning**: Can we make neural networks interpretable by design?
4. **Interactions**: Handling high-order interactions interpretably
5. **Evaluation**: Better metrics and benchmarks

**Emerging Directions:**

- Concept-based models
- Neural-symbolic integration
- Structured neural networks

---

# Summary: Inherently Interpretable Models

**Key Takeaways:**

- Multiple model classes offer interpretability
  - Linear models: Simple, transparent
  - Decision trees: Visual, logical
  - Rule-based models: Modular, actionable
  - GAMs: Flexible, visualizable

- Interpretability is multifaceted
  - Simulatability, decomposability, transparency

- Trade-offs exist but can be managed
  - Modern methods (EBMs) achieve strong accuracy
  - Domain-specific evaluation is crucial

---

# Next Class

**Post-hoc Explanation Methods:**

- LIME (Local Interpretable Model-agnostic Explanations)
- SHAP (SHapley Additive exPlanations)
- Counterfactual Explanations
- Saliency Maps and Attribution Methods

**Reading:**

- [@ribeiro2016should] - "Why Should I Trust You?"
- [@lundberg2017unified] - "A Unified Approach to Interpreting Model Predictions"

---

# Discussion Questions

1. In what domains would you prefer interpretable models over black-boxes?

2. How would you evaluate if a decision tree with 20 nodes is "interpretable"?

3. Can regularization (L1/L2) be considered an interpretability technique?

4. Should we always prefer inherently interpretable models in high-stakes domains?

5. How do you balance the needs of different stakeholders (developers, users, regulators)?

---

# References {.allowframebreaks}

\\footnotesize
