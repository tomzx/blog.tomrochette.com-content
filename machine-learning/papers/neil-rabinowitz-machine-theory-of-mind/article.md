---
title: Neil Rabinowitz - Machine Theory of Mind (2018)
created: 2018-02-24
taxonomy:
  tag: [machine-learning]
  status: finished
---

## Context

## Learned in this study

## Things to explore
* What is the different between being biased and having a strong/rich prior
* It seems as if ToMnet is able to learn things such as A*, given an agent that deterministically follows this policy

# Overview

# Notes
## 1. Introduction
* What does it actually mean to "understand" another agent?
* Our goal is not to assert a generative model of agents' behavior and an algorithm to invert it. Rather, we focus on the problem of how an observer could learn autonomously how to model other agents using limited data

### 1.1. Our approach
* At test time, we want to be able to encounter a novel agent whom we have never met before, and already have a strong and rich prior about how they are going to behave
* As we see this agent act in the world, we wish to be able to collect data about their latent characteristics and mental states that will enable us to improve our predictions about their future behavior
* Over the course of training, the observer should get better at rapidly forming predictions about new agents from limited data
* The observer should also learn an effective prior over the agents' behavior that implicitly captures the commonalities between agents within the training population
* We introduce two concepts to describe components of this observer network and their functional role
	* General theory of mind: the learned weights of the network, which encapsulate predictions about the common behaviour of all agents in the training set
	* Agent-specific theory of mind: the "agent embedding" formed from observations about a single agent at test time, which encapsulates what makes this agent's character and mental state distinct from others'
	* These correspond to a prior and posterior over agent behavior

## 2. Model
### 2.2. The architecture
* The ToMnet is composed of three modules:
	* a character net: characterise the presented agent, by parsing observed past episode trajectories, into a character embedding
	* a mental state net: mentalise about the presented agent during the current episode (i.e., infer its mental state), by parsing the current episode trajectory, up to time t-1 into a mental state embedding, using a learned neural network
	* a prediction net: leverage the character and mental state embeddings to predict subsequent behaviour of the agent

# See also

# References
