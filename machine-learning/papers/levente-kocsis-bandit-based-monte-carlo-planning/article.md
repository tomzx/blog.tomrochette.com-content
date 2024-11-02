---
title: Levente Kocsis - Bandit based Monte-Carlo Planning (2006)
created: 2017-12-08
taxonomy:
  tag: [Machine learning]
  status: finished
---

## Context

## Learned in this study

## Things to explore
* Can UCT be used to rapidly determine "interesting values" in black box testing?

# Overview

# Notes
## 1 Introduction
* We are interested in Monte-Carlo planning algorithms with two important characteristics:
	* small error probability if the algorithm is stopped prematurely
	* convergence to the best action if enough time is given
* The main idea of the algorithm proposed in this paper is to sample actions selectively
* Let us consider problems with a large number of actions and assume that the lookahead is carried out at a fixed depth D
* If sampling can be restricted to say half of the actions at all stages then the overall work reduction is $(1/2)^D$
* If one is able to identify a large subset of the suboptimal actions early in the sampling procedure then huge performance improvements can be expected
* By definition, an action is suboptimal for a given state, if its value is less than the best of the action-values for the same state

## 2 The UCT algorithm
### 2.1 Rollout-based planning
* A rollout-based algorithm builds its lookahead tree by repeatedly sampling episodes from the initial state
* An episode is a sequence of state-action-reward triplets that are obtained using the domains generative model

### 2.2 Stochastic bandit problems and UCB1
* A policy is said to resolve the exploration-exploitation tradeoff if its regret growth rate is within a constant factor of the best possible regret rate
* UCB1 keeps track of the average rewards for all the arms and chooses the arm with the best upper confidence bound

### 2.3 The proposed algorithm
* In UCT the action selection problem is treated as a separate multi-armed bandit for every (explored) internal node

# See also

# References
* Kocsis, Levente, and Csaba Szepesvári. "Bandit based monte-carlo planning." ECML. Vol. 6. 2006.
