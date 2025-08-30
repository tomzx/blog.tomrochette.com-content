---
title: "Ken Kansky - Schema Networks: Zero-shot Transfer with a Generative Causal Model of Intuitive Physics (2017)"
created: 2017-06-22
taxonomy:
  tag: [machine-learning]
  status: finished
---

## Context

## Learned in this study

## Things to explore

# Overview
* Schema Networks are implemented as probabilistic graphical models
* The state is represented as a set of entity-attributes (e.g., ball at position (x, y))
* The learning objective for Schema Networks is designed to understand causality within these environments

# Notes
## 1. Introduction
* Despite remarkable progress on individual tasks like Atari 2600 games and Go, the ability of state-of-the-art models to trasnfer learning from one environment to the next remains limited

## 2. Related Work
* Schema Networks offer two key advantages:
	* Latent physical properties and relations need not be hardcoded
	* Planning can make use of backward search
* Schema Networks are implemented as probabilistic graphical models (PGMs), which provide practical inference and structure learning techniques

## 3. Schema Networks
### 3.2 Model Definition
* A Schema Network is a structured generative model of an MDP
* A Schema Network is a factor graph that contains all grounded instantiations of a set of ungrounded schemas over some window of time
* For simplicity, suppose the number of entities and the number of attributes are fixed at N and M respectively
* Let $E_i$ refer to the $i^{th}$ entity and let $\alpha_{i,j}^{(t)}$ refer to the $j^{th}$ attribute value of the $i^{th}$ entity at time $t$
* We use the notation $E_i^{(t)} = (\alpha_{i,1}^{(t)}, \dots, \alpha_{i,M}^{(t)})$ to refer to the state of the $i^{th}$ entity at time $t$
* The complete state of the MDP modeled by the network at time $t$ is then $s^{(t)} = (E_i^{(t)}, \dots, E_N^{(t)})
* Actions and rewards are also represented with sets of binary variables, denoted $a^{(t)}$ and $r^{(t+1)}$ respectively
* Let $\phi^k$ denote the variable for grounded schema $k$
* A grounded schema is connected to its precondition entity-attributes with an AND factor, written as $\phi^k = \text{AND}(\alpha_{i_1,j_1}, \dots, \alpha_{i_H,j_H}, a)$ for $H$ entity-attribute preconditions and an optional action $a$
* An ungrounded schema (or template) is represented as $\Phi_l(E_{x_1}, \dots, E_{x_H}) = \text{AND}(\alpha_{x_1,y_1}, \dots, \alpha_{x_H,y_H})$ where $x_h$ determines the relative entity index of the $h$-th precondition and $y_h$ determines which attribute variable is the precondition
* The ungrounded schema is a template that can be bound to multiple specific entities and locations to generate grounded schemas

### 3.3. Construction of Entities and Attributes
* In practice we assume that a vision system is responsible for detecting and tracking entities in an image
* Recent work has demonstrated one possible method for unsupervised entity construction using autoencoders

## 4. Learning and Planning in Schema Networks
### 4.1. Training Procedure
* Given a series of actions, rewards and images, we represent each possible action and reward with a binary variable, and we convert each image into a set of entity states
* While gathering data, actions are chosen by planning using the schemas that have been learned so far
* We use an $\epsilon$-greedy approach to encourage exploration, taking a random action at each timestep with small probability

### 4.2. Schema Learning
* For this algorithm to work, no contradictions can exist in the input data (such as the same input appearing twice with different labels). Such contradictions might appear in stochastic environments and would not be artifacts in real environments, so we preprocess the input data to remove them

# See also

# References
* Kansky, Ken, et al. "Schema Networks: Zero-shot Transfer with a Generative Causal Model of Intuitive Physics." arXiv preprint arXiv:1706.04317 (2017).
