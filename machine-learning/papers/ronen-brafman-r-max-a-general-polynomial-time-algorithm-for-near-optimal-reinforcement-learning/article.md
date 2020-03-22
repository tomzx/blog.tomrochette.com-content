---
title: Ronen Brafman - R-max – A General Polynomial Time Algorithm for Near-Optimal Reinforcement Learning (2002)
created: 2017-12-08
taxonomy:
  category: [Machine learning]
  status: finished
---

## Context

## Learned in this study

## Things to explore
* Why do they say "Since there is only a polynomial number of parameters to learn"? What are those parameters?

# Overview

# Notes
* R-max improves upon several previous algorithms
	* It is simpler and more general than Kearns and Singh's $E^3$ algorithm, covering zero-sum stochastic games
	* It has a built-in mechanism for resolving the exploration vs exploitation dilemma
	* It formally justifies the "optimism under uncertainty" bias used in many RL algorithms
	* It is simpler, more general, and more efficient than Brafman and Tennenholtz's LSG algorithm for learning in single controller stochastic games
	* It generalizes the algorithm by Monderer and Tennenholtz for learning in repeated games
	* It is the only algorithm for learning in repeated games, to date, which is provably efficient, considerably improving and simplifying previous algorithms by Banos and by Megiddo

## 1. Introduction
* THe major insight behind the R-max algorithm is that the optimal policy with respect to the real model: it is always either optimal or it leads to efficient learning
* The approach taken by R-max is not new. It has been referred to as the optimist in the face of uncertainty heuristic

## 2. Preliminaries
### 2.1 Stochastic Games
* A game is a model of multi-agent interaction
* In a game, we have a set of players, each of whom chooses some action to perform from a given set of actions
* A common description of a game is as a matrix. This is called a game in strategic form
	* The rows of the matrix correspond to the agent's actions and the columns correspond to the adversary's actions. The entry in row $i$ and column $j$ in the game matrix contains the rewards obtained by the agent and the adversary if the agent plays his $i^{th}$ action and the adversary plays his $j^{th}$ action

### 2.2 Assumptions, Complexity and Optimality
* We make two central assumptions:
	* We assume that the agent always recognizes the identity of the state it reached and that after playing a game, it knows what actions were taken by its adversary and what payoffs were obtained
	* We assume that the maximal possible reward $R_{max}$ is known ahead of time
* We start learning at some state $s$ in which the optimal action is $a$
	* If we do not execute the action $a$ in $s$, we reach some state $s'$ that has a lower value
	* A learning algorithm without any prior knowledge cannot be expected to immediately guess that $a$ should be done in $s$
	* Without such prior knowledge, it cannot conclude that $a$ is a good action unless it tries the other actions in $s$ and compares their outcome to that of $a$
	* One can expect an agent to learn a near-optimal policy only if the agent can visit state $s$ sufficiently many times to learn about the consequences of different options in $s$

# See also

# References
* Brafman, Ronen I., and Moshe Tennenholtz. "R-max-a general polynomial time algorithm for near-optimal reinforcement learning." Journal of Machine Learning Research 3.Oct (2002): 213-231.
