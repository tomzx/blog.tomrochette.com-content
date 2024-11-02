---
title: Thomas Anthony - Thinking Fast and Slow with Deep Learning and Tree Search (2017)
created: 2017-10-20
taxonomy:
  tag: [Machine learning]
  status: finished
---

## Context

## Learned in this study

## Things to explore

# Overview

# Notes
## 1 Introduction
* According to dual-process theory, human reasoning consists of two different kinds of thinking
	* System 1: a fast, unconscious and automatic mode of thought (also known as intuition or heuristic process)
	* System 2: an evolutionary recent process unique to humans, slow, conscious, explicit and rule-based mode of reasoning
* At a low leve, ExIt can be viewed as an extension of Imitation Learning (IL) methods to domains where the best known experts are unable to achieve satisfactory performance
* In IL an apprentice is trained to imitate the behavior of an expert policy
* Within ExIt, we iteratively resolve the IL problem
* Between each iteration, we perform an Expert Improvement step, where we bootstrap the (fast) apprentice policy to increase the performance of the (comparatively slow) expert
* In a typical implementation of ExIt, the apprentice is implemented as a deep neural network, and the expert by a Tree Search algorithm

## 2 Preliminaries
### 2.2 Imitation Learning
* In Imitation Learning, we attempt to solve the MDP by mimicking an expert policy $\pi^*$ that has been provided
* The simplest approach is simply to ask the expert to name an optimal move $\pi^*(a|s)$

## 3 Expert iteration
* To achieve Expert Improvement, we bootstrap the most recent apprentice policy learned in the Imitation Learning
* If the expert is able to find policies much stronger than the bootstrapped apprentice policy, each iteration will result in a large improvement in the apprentice's play strength
* The Imitation Learning step is analogous to a human improving their intuition for the task by studying example problems, while the Expert Improvement step is analogous to a human using their improved intuition to guide future analysis

### 3.1 Choice of expert and apprentice
* The learning rate of ExIt is controlled by two factors:
	* the size of the performance gap between the apprentice policy and the improved expert
		* Induces an upper bound on the new apprentice's performance at each iteration
	* how close the performance of the new apprentice is to the expert it learns from
		* Describes how closely we approach the upper bound
* The role of the expert is to perform exploration, and thereby to accurately determine strong move sequences, from a single position
* The role of the apprentice is to generalize the policies that the expert discovers across the whole state space, and to provide rapid access to that strong policy for bootstrapping
* The canonical choice of expert is a tree search algorithm
* Possible tree search algorithms include Monte Carlo Tree Search, $\alpha-\beta$ search, and greedy search
* The canonical apprentice is a deep neural network parametrization of the policy

### 3.3 Online expert iteration
* In each step of ExIt, Imitation Learning is restarted from scratch

## 7 Related work
* DQN can be seen as a special case of ExIt where the expert performs a single-sample single-step lookahead

# See also

# References
* Anthony, Thomas, Zheng Tian, and David Barber. "Thinking Fast and Slow with Deep Learning and Tree Search." arXiv preprint arXiv:1705.08439 (2017).
