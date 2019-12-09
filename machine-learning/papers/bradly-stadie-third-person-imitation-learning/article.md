---
title: Bradly Stadie - Third-Person Imitation Learning (2017)
created: 2017-05-26
taxonomy:
  category: [Machine Learning]
  status: finished
---

## Context

## Learned in this study

## Things to explore

# Overview
* Learning in the third-person is posed as the adversarial challenge of replicating an expert trace (sequence of actions/states) which are considered as optimal under some unknown reward policy

# Notes
## 1 Introduction
* One of the major weaknesses of RL is the need to manually specify a reward function
* This weakness is addressed by the field of Inverse Reinforcement Learning (IRL)
	* Given a set of expert trajectories, IRL algorithms produce a reward function under which these expert trajectories enjoy the property of optimality
* While IRL algorithms are appealing, they impose the somewhat unrealistic requirement that the demonstrations should be provided from the first-person point of view with respect to the agent
* The high-level idea is to introduce an optimizer under which we can recover both a domain-agnostic representation of the agent's observations, and a cost function which utilizes this domain-agnostic representation to capture the essence of expert trajectories

## 2 Related Work
* The approach uses Trust Region Policy Optimization

## 3 Background and Preliminaries
* In the (first-person) imitation learning setting, we are not given the reward function. Instead we are given traces (i.e., sequences of states traversed) by an expert who acts according to an unknown policy $\pi_E$. The goal is to find a policy $\pi_\theta$ that performs as well as the expert against the unknown reward function
* Find a policy $\pi_\theta$ that makes it impossible for a discriminator to distinguish states visited by the expert from states visited by the imitator agent

## 4 A Formal Definition of the Third-Person Imitation Learning Problem
* Formally, the third-person imitation learning problem can be stated as follows
* Suppose we are given two Markov Decision Processes $M_{\pi_E}$ and $M_{\pi_\theta}$
* Suppose further there exists a set of traces $\rho = \{(s_1, \dots, s_n)\}_{i=0}^n$ which were generated under a policy $\pi_E$ acting optimally under some unknown reward $R_{\pi_E}$
* In third-person imitation learning, one attempts to recover by proxy through $\rho$ a policy $\pi_\theta = f(\rho)$ which acts optimally with respect to $R_{\pi_\theta}$

# See also

# References
* Stadie, Bradly C., Pieter Abbeel, and Ilya Sutskever. "Third-Person Imitation Learning." arXiv preprint arXiv:1703.01703 (2017).