---
title: Tom Mitchell - Never-ending learning (2018)
created: 2018-05-03
taxonomy:
  category: [Machine Learning]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview

# Notes
## Abstract
* We suggest that people learn better than computers precisely because (they learn many different types of knowledge from diverse experiences over many years and become better learners overtime whereas machine learning systems learn just a single function or data model)
* We suggest a key direction for machine learning research is to develop software architectures that enable intelligent agents to also learn many types of knowledge, continuously over many years, and to become better learners over time

## 1. Introduction
* Humans learn cumulatively: as they learn one thing this new knowledge helps them to more effectively learn the next, and if they revise their beliefs about the first then this change refines the second
* The thesis of our research is that we will never truly understand machine or human learning until we can build computer programs that, like people
	* learn many different types of knowledge of functions
	* from years of diverse, mostly self-supervised experience
	* in a staged curricular fashion, where previously learned knowledge enables learning further types of knowledge,
	* where self-reflection and the ability to formulate new representations and new learning tasks enable the learner to avoid stagnation and performance plateaus

## 3. Never-Ending Learning
* We define a never-ending learning agent to be a system that, like humans, learns many types of knowledge, from years of diverse and primarily self-supervised experience, using previously learned knowledge to improve subsequent learning, with sufficient self-reflection to avoid plateaus in performance as it learns
* The never-ending learning problem faced by the agent consists of a collection of learning tasks, and constraints that couple their solutions
* We define a never-ending learning problem $\mathcal{L}$ to be an ordered pair consisting of
	* a set $L = \{L_i\}$ of learning tasks, where the $i$th learning task $L_i = \langle T_i, P_i, E_i \rangle$ is to improve the agent's performance, as measured by performance metric $P_i$, on a given performance task $T_i$, through a given type of experience $E_i$
	* a set of coupling constraints $C = \{\langle \phi_k, V_k \rangle\}$ among the solutions to these learning tasks, where $\phi_k$ is a real-valued function over two or more learning tasks, specifying the degree of satisfaction of the constraint, and $V_k$ is a vector of indices over learning tasks, specifying the arguments to $\phi_k$
* Each performance task $T_i$ is a pair $T_i = \langle X_i, Y_i \rangle$ defining the domain and range of a function to be learned $f_i^*: X_i \rightarrow Y_i$
* The performance metric $P_i: f \rightarrow \mathbb{R}$ defines the optimal learned function $f_i^*$ for the $i$th learning task:
$$
f_i^* \equiv \arg\max_{f \in F_i} P_i(f)
$$
where $F_i$ is the set of all possible functions from $X_i$ to $Y_i$

# See also

# References
* Mitchell, Tom, et al. "Never-ending learning." Communications of the ACM 61.5 (2018): 103-115.
