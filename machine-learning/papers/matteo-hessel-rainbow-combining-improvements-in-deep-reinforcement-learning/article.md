---
title: "Matteo Hessel - Rainbow: Combining Improvements in Deep Reinforcement Learning (2017)"
created: 2017-11-04
taxonomy:
  category: [Machine learning]
  status: finished
---

## Context

## Learned in this study

## Things to explore

# Overview
* Prioritized replay and multi-step learning appears to have the most impact on performance
* Rainbow is able to obtain much better result faster (less seen frames) than any of the other approaches by themselves

# Notes
## Introduction
* Double DQN addresses an overestimation bias of Q-learning by decoupling selection and evaluation of the bootstrap action
* Prioritized experience replay improves data efficiency by replaying more often transitions from which there is more to learn
* The dueling network architecture helps to generalize across actions by separately representing state values and actions advantages
* Learning from multi-step bootstrap targets shifts the bias-variance trade-off and helps to propagate newly observed rewards faster to earlier visited states
* Distributional Q-learning learns a categorical distribution of discounted returns instead of estimating the mean
* Noisy DQN uses stochastic network layers for exploration

## Analysis
### Ablation studies
* Prioritized replay and multi-step learning were the two most crucial components of Rainbow, in that removing either component caused a large drop in median performance
* In the case of double Q-learning, the observed difference in median performance is limited, with the component sometimes harming or helping depending on the game

## Discussion
* Optimality tightening uses multi-step returns to construct additional inequality bounds instead of using them to replace the 1-step targets used in Q-learning
* Eligibility traces allow a soft combination over n-step returns
* Episodic control focuses on data efficiency, and was shown to be very effective in some domains. It improves early learning by using episodic memory as a complementary learning system, capable of immediately re-enacting successful action sequences

# See also

# References
* Hessel, Matteo, et al. "Rainbow: Combining Improvements in Deep Reinforcement Learning." arXiv preprint arXiv:1710.02298 (2017).
