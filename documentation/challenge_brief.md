# Challenge Assignment

**Aprendizagem Computacional / Machine Learning, 2026**
DEI, FCT, University of Coimbra

---

## Context and Goals

The goal of this assignment is that ML students get acquainted with ML algorithms and models sharing with the class their achievements. As the traditional way of achieving this goal (building simple projects) has been obliterated by LLMs, we will flip the classroom in this assignment.

The class will be organized into four groups of three students (tentative). Each group will receive one topic by random allocation. The goal is then to fully exploit that topic and present it in class.

## Objectives

Build a **small interactive demonstration** that teaches your classmates how a simple machine learning model works, why it succeeds in some situations, and why it fails in others.

Your demonstration must connect the model's underlying mechanism to observable changes in its predictions and performance. **All group members must understand the complete demonstration and contribute to its development and discussion.**

The objective of the challenge is then to use **Python** to create a **runnable notebook** or a **lightweight application**. A notebook with clearly identified parameters that can be changed and rerun is sufficient; sliders and other widgets are optional. Use established libraries such as scikit-learn. Implementing the full learning algorithm from scratch is not required. Start with a **small synthetic dataset** that you can generate and control. Use one or two input features for the **main visual explanation**. Additional features may be introduced in experiments. Real datasets may be added as an optional illustration but are not required.

## General Requirements

To meet the goal, here are a set of minimum requirements:

1. **A favourable case.** Construct a situation in which the model works well. Show what it learns and explain why its assumptions or decision mechanism suit the data.
2. **A controlled failure.** Change one relevant aspect of the data or model configuration. State your expected outcome before running the experiment, then explain the observed change.
3. **An attempted improvement.** Adjust the model or preprocessing to address the failure. Compare the results and discuss any remaining limitation. An unsuccessful correction is acceptable if it is analysed convincingly.

Additionally:

4. Show how the model produces a prediction for at least one selected observation, using a small calculation, a decision path, neighbours, or feature contributions, as appropriate.
5. Include plots that show its behaviour, such as decision regions, fitted curves, class probabilities, or a tree diagram.
6. Before each experiment, record your prediction of what will happen and why. Keep that prediction in the final notebook, even when the result contradicts it.
7. End with three practical lessons about when and how to use the model.

## Experimental Requirements

Describe the data generation process, the target, and the reason for choosing each experimental condition. Set random seeds so that your results can be reproduced.

Keep training and testing data separate. Fit preprocessing only on training data. If you select hyperparameters using performance, use a validation split or cross-validation within the training data; reserve test data for final evaluation.

Choose metrics suitable for the task and justify them. Report training and test results where relevant. When comparing conditions, keep the evaluation protocol and unrelated settings fixed, and explain any deliberate changes.

Keep the experiments small enough to rerun during the discussion. Extensive hyperparameter searches, large datasets, and elaborate interfaces are not required.

## Deliverables and Deadlines

- **Submission deadline:** November 9, 2027, 1PM *(as written in the brief; likely 2026)*
- **Demonstration and discussion:** November 9, 2027, 2PM–6PM

Submit the following through InforEstudante. All written material and the presentation must be in English:

- A brief **PDF report**, up to four pages excluding references. Include the group members, assigned topic, explanation of the model, experimental design, key results and figures, limitations, and three practical lessons.
- A **ZIP file** containing the notebook or application, any additional code, a requirements file, and a short README with setup and execution instructions. Include the data or the script that generates them. Keep the executed notebook outputs available.

Within the report, include a short contribution statement for each member and an AI use declaration. Cite external sources and acknowledge reused code or visual material.

## Demonstration and Discussion

Each group will have 20 minutes to demonstrate its work, followed by approximately 10 minutes of questions and discussion with questions for all group members. All members must participate in the demonstration and be ready to explain any part of the work.

During the discussion, there can be requests to change a parameter or a data condition, predict the effect before running the code, and interpret the result. The change will remain within the scope of your assigned topic. Individual answers must reflect your own understanding, without assistance from AI tools or other group members.

Progress checkpoints will take place during classes. Bring your proposed data setup, the three experiments, and your expected outcomes so that the scope and feasibility can be discussed before completion.

## Use of Generative AI

You may use generative AI to support coding, debugging, explanations, reporting, or presentation. You remain responsible for the correctness of all submitted material and must verify generated code and claims against your experiments and reliable sources.

Your AI use declaration must identify the tools used, explain what they supported, and describe one concrete verification or correction you performed. If you did not use generative AI, state this explicitly. Full conversation histories are not required. Do not fabricate results or replace your original experimental predictions with explanations written after seeing the outcomes. You must be able to explain, modify, and defend all submitted code and conclusions.

## Assessment Criteria

| Component | Weight | Breakdown |
| --- | --- | --- |
| Group | 60% | Clarity of the demonstration (20%), experimental design and interpretation (25%), reproducibility and quality of the submitted material (15%) |
| Individual | 40% | Understanding of the model and experimental choices (25%), ability to predict, explain, and respond to a small change during the discussion (15%) |

High predictive accuracy alone does not earn a high mark. Assessment focuses on what your experiments demonstrate and how well you explain it. Interface sophistication is not an assessment criterion.

## Topics

Each group must address the core elements below. Select a manageable subset of the suggested changes for your three minimum requirements; you are not expected to test every option.

### Topic 1 – Decision Trees

Explain how feature thresholds split the input space and how a leaf produces a prediction. Show a tree and its decision regions, and trace one observation from the root to a leaf.

Explore tree depth or minimum leaf size, comparing training and test performance.

Suggested changes include label noise, a small training set, or a slight change to the training observations. Discuss overfitting and the stability of the learned tree.

### Topic 2 – K Nearest Neighbors

Explain how distance and neighboring observations determine a prediction. For one query point, show the selected neighbors and how their labels are combined.

Explore the effect of k and feature scaling.

Suggested changes include rescaling one feature, adding irrelevant features, or changing the density of the observations. Explain when scaling helps and why choosing a larger k does not always improve performance; demonstrate the bias–variance tradeoff.

### Topic 3 – Naive Bayes

Use with continuous and/or discrete features. Explain class priors, class conditional likelihoods, and the conditional independence assumption. For one observation, show how these quantities combine to produce class scores or probabilities.

Compare a favorable case with a controlled change to class conditional feature dependence or distribution shape. Visualize the data and predicted probabilities. Discuss whether the change affects classification performance, probability quality, or both; dependence does not automatically imply poor accuracy.

### Topic 4 – Linear and Logistic Regression

Use linear regression to illustrate prediction of a continuous target, and logistic regression to illustrate binary classification.

Explain the role of coefficients and show how a logistic regression score becomes a probability and then a class prediction.

Keep one model as your main experimental focus and use the other for a short comparison of outputs and interpretation.

Suggested changes include a nonlinear relationship, outliers in linear regression, or changes to regularization or the classification threshold in logistic regression. Explain the distinction between changing a threshold and retraining a model.
