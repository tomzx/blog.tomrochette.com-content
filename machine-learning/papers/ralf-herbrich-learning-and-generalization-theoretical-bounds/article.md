---
title: "Ralf Herbrich - Learning and Generalization: Theoretical Bounds (2001)"
created: 2017-06-30
taxonomy:
  tag: [machine-learning]
  status: in progress
  readability: 3
---

## Context

## Learned in this study

## Things to explore

# Overview

# Notes
## 1 Introduction
* The fundamental difference between a system that learns and one that merely memorizes is that the learning system generalizes to unseen examples

## 2 Formalization of The Learning Problem
* An unknown distribution $\mathbf{P}_{XY}$ over an input space $\mathcal{X}$ and an outcome space $\mathcal{Y}$
* We are only given a sample $z \in (\mathcal{X} \times \mathcal{Y})^m = \mathcal{Z}^m$ which is assumed to be drawn iid from $\mathbf{P}_{XY} = \mathbf{P}_Z$
* In an attempt to discover the unknown relation $\mathbf{P}_{Y|X = x}$ between inputs and outputs, a learning algorithm $\mathcal{A}$ chooses a deterministic hypothesis $h: \mathcal{X} \rightarrow \mathcal{Y}$ solely based on a given training sample $z \in \mathcal{Z}^m$
* The performance of the learning algorithm is judged according to a loss function $l: \mathcal{Y} \times \mathcal{Y} \rightarrow \mathbb{R}^+$ which measures the cost of the prediction $\hat{y}$ if $y$ is the correct output
* The learning problem is to find an hypothesis $h: \mathcal{X} \rightarrow \mathcal{Y}$ such the expected risk, $R[h] = E_{XY}[l(h(X), Y)]$, is minimized
* If we knew $\mathbf{P}_Z$, the solution of the learning problem would be straightforward
$$
h_{opt}(x) = \underset{y\ \in\ \mathcal{Y}}{\arg\min} E_{Y|X = x}[l(y, Y)]
$$

# See also

# References
* Herbrich, Ralf, and Robert C. Williamson. "Learning and generalization: Theoretical bounds." Handbook of Brain Theory and Neural Networks (2002): 3140-3150.
