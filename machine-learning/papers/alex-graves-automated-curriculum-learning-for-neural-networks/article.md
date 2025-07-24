---
title: Alex Graves - Automated Curriculum Learning for Neural Networks (2017)
created: 2017-06-23
taxonomy:
  tag: [machine learning]
  status: finished
---

## Context

## Learned in this study

## Things to explore
* Neural architecture search where picking the right action is seen as a multi-armed bandit

# Overview

# Notes
## 1. Introduction
* One reason for the slow adoption of curriculum learning is that its effectiveness is highly sensitive to the mode of progression through the tasks
* One popular approach is to define a hand-chosen performance threshold for advancement to the next task, along with a fixed probability of returning to earlier tasks, to prevent forgetting
* We propose to treat the decision about which task to study next as a stochastic policy, continuously adapted to optimize some notion of learning progress

## 2. Background
* We consider supervised or unsupervised learning problems where target sequences $\textbf{b}^1, \textbf{b}^2, \dots$ are conditionally modelled given their respective input sequences $\textbf{a}^1, \textbf{a}^2, \dots$
* We suppose that the targets are drawn from a finite set $\mathcal{B}$
* As is typical for neural networks, sequences may be grouped together in batches $(\textbf{b}^{1:B}, \textbf{a}^{1:B})$ to accelerate training
* The conditional probability output by the model is
$$
p(\textbf{b}^{1:B}, \textbf{a}^{1:B}) = \prod_{i,j} p(\textbf{b}_j^i\ |\ \textbf{b}_{1:j-1}^i, \textbf{a}_{1:j-1}^i)
$$
* We consider each batch as a single exemple $\textbf{x}$ from $\mathcal{X} := (\mathcal{A} \times \mathcal{B})^N$, and write $p(\textbf{x}) := p(\textbf{b}^{1:B}, \textbf{a}^{1:B})$ for its probability
* A task is a distribution $D$ over sequences from $\mathcal{X}$
* A curriculum is an ensemble of tasks $D_1, \dots, D_N$
* A sample is an example drawn from one of the tasks of the curriculum
* A syllabus is a time-varying sequence of distributions over tasks

### 2.1. Curriculum Learning
* We consider two related settings:
	* The multiple tasks setting, the goal is to perform as well as possible on all tasks in the ensemble
	* The target task setting, the goal is to minimize the loss on the final task, the other tasks acting as a series of stepping stones to the real problem

### 2.2 Adversarial Multi-Armed Bandits
* We view a curriculum containing $N$ tasks as an $N$-armed bandit, and a syllabus as an adaptive policy which seeks to maximize payoffs from this bandit
* In the bandit setting, an agent selects a sequence of arms (actions) $a_1, \dots, a_T$ over $T$ rounds of play ($a_t \in \{1, \dots, N\}$)
* After each round, the selected arm yields a payoff $r_t$; the payoffs for the other arms are not observed
* The classical algorithm for adversarial bandits is Exp3, which uses multiplicative weight updates to guarantee low regret with respect to the best arm
* On a round $t$, the agent selects an arm stochastically according to a policy $\pi_t$. This policy is defined by a set of weights $w_{t, i}$:
$$
\pi_t^{\text{EXP3}}(i) := \frac{e^{w_{t,i}}}{\sum_{j=1}^N e^{w_{t,j}}}
$$

## 3. Learning Progress Signals
* Ideally we would like the policy to maximize the rate at which we minimize the loss, and the reward should reflect this rate
* However, it usually is computationally undesirable or even impossible to measure the effect of a training sample on the target objective, and we therefore turn to surrogate measures of progress
* Two types of measures:
	* Loss-driven, in the sense that they equate reward with a decrease in some loss
	* Complexity-driven, when they equate reward with an increase in model complexity

### 3.2. Complexity-driven Progress
* According to the Minimum Description Length (MDL) principle, increase in the model complexity by a certain amount is only worthwhile if it compresses the data by a greater amount
	* We would therefore expect the complexity to increase most in response to the training examples from which the network is best able to generalize

## 5. Conclusion
* We note that uniformly sampling from all tasks is a surprisingly strong benchmark. We speculate that this is because learning is dominated by gradients from the tasks on which the network is making fastest progress, inducing a kind of implicit curriculum, albeit with the inefficiency of unnecessary samples

# See also

# References
* Graves, Alex, et al. "Automated Curriculum Learning for Neural Networks." arXiv preprint arXiv:1704.03003 (2017).
