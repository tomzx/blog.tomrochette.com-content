---
title: Jurgen Schmidhuber - One Big Net For Everything (2018)
created: 2018-05-11
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore
* Given a single neural network architecture, it might be possible to store different weight values that would represent different views of the environment (this would be akin to a person's consciousness?)

# Overview

# Notes
## 1 Introduction
* To become a general problem solver that is able to run arbitrary problem-solving programs, the controller of a robot or artificial agent must be a general-purpose computer
* Without a teacher, reward-maximizing programs of an RNN must be learned through repeated trial and error, e.g., through artificial evolution or reinforcement learning through policy gradients
* The search space can often be reduced dramatically by evolving compact encodings of RNNs

## 2 One Big RNN For Everything: Basic Ideas and Related Work
* ONE or copies thereof or parts thereof are trained in various ways, in particular
	* by black box optimization/reinforcement learning/artificial evolution without a teacher
	* gradient descent-based supervised or unsupervised learning

## 3 More Formally: ONE and its Self-Acquired Data
* Cumulative reward $CR(t) = \sum_{\tau=1}^t R(\tau)$

### 3.1 Training a Copy of ONE on New Control Tasks Without a Teacher
* One of ONE's goals is to maximize $CR(t_\tau)$
* Copies of successive instances of ONE are trained in a series of trials through a black box optimization method
	* Incremental neuroevolution
	* Hierarchical neuroevolution
	* Hierarchical policy gradient algorithms
	* Asymptotically optimal ways of algorithm transfer learning
* Given a new task and a ONE trained on several previous tasks, such hierarchical/incremental methods may create a copy of the current ONE, freeze its current weights, then enlarge the copy of ONE by adding a few new units and connections which are trained until the new task is satisfactorily solved
	* This process can reduce the size of the search space for new task, while giving the new weights the opportunity to learn to somehow use certain frozen parts of ONE's copy as subroutines

### 3.2 Unsupervised ONE Learning to Predict/Compress Observations
* ONE may further profit from unsupervised learning that compressed the observed data into a compact representation that may make subsequent learning of externally posed tasks easier

# See also

# References
* Schmidhuber, Juergen. "One Big Net For Everything." arXiv preprint arXiv:1802.08864 (2018).
