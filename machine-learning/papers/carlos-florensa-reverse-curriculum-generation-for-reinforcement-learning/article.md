---
title: Carlos Florensa - Reverse Curriculum Generation for Reinforcement Learning (2017)
created: 2017-11-04
taxonomy:
  category: [Machine learning]
  status: finished
---

## Context

## Learned in this study

## Things to explore
* Given a start and end state, how is inversing the two actually any better?
	* It looks like this is basically creating some sort of field that indicates the direction to take from the current position to the end position
		* It would mean this method needs the ability to generate cases from the end, which is not something that is possible in video games for instances
* How is the basic RL approach different than A*?

# Overview
* RL applied to the robotics domain where one can start from the end state and learn its way backwards until it reaches the start state

# Notes
## Abstract
* We propose a method to learn tasks without requiring any prior knowledge other than obtaining a single state in which the task is achieved. The robot is trained in "reverse", gradually learning to reach the goal from a set of start states increasingly far from the goal

## 1 Introduction
* In our work, we avoid all reward engineering or use of demonstrations by exploiting two key insights
	* It's easier to reach the goal from states nearby the goal, or from states nearby where the agent already knows how to reach the goal
	* Applying random actions from one such state leads the agent to new feasible nearby states, from where it is not too much harder to reach the goal

## 2 Related Work
* Our approach can be understood as sequentially composing locally stabilizing controllers by growing a tree of stabilized trajectories backwards from the goal state
	* This can be viewed as a "funnel" which takes start states to the goal state via a series of locally valid policies

## 3 Problem Definition
### 3.3 Assumptions for reverse curriculum generation
* Assumption 1: We can arbitrarily reset the agent into any start state $s_0 \in \mathcal{S}$ at the beginning of all trajectories
* Assumption 2: At least one state $s^g$ is provided such that $s^g \in S^g$
* Assumption 3: The Markov Chain induced by taking uniformly sampled random actions has a communicating class including all start states $S^0$ and the given goal state $s^g$

## 6 Conclusions and Future Directions
* A limitation of the current approach is that it generates start states that grow from a single goal uniformly outwards, until they cover the original start state distribution $\text{Unif}(S^0)$

# See also
* [Mari/o](../../../agi/mario/article.md)

# References
* Florensa, Carlos, et al. "Reverse Curriculum Generation for Reinforcement Learning." arXiv preprint arXiv:1707.05300 (2017).
