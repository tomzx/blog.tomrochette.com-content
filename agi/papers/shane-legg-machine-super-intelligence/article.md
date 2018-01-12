---
title: Shane Legg - Machine Super Intelligence (2008)
created: 2018-01-04
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore
* Is it possible to formalize machine intelligence based on the idea of a computer/program/data?
* Is a young child as intelligent as an adult?
* Is it possible to determine if an individual may or may not be able to learn something given enough time? And if so, is it possible to estimate the amount of time required?
* Is it possible to devise a test of intelligence for which it is not necessary to communicate any instruction to the entity being tested?
* Is it easier to design anthropocentric AI/AGI vs universal AI/AGI?
* Tegmark definition of intelligence does not contain the part about "in a wide range of environments"... How could this be turned into something more abstract such as "in a wide range of potential state systems"?

# Overview

# Notes
## 1. Nature and Measurement of Intelligence
* When standard intelligence tests are correctly applied and interpreted, they all measure approximately the same thing
* Furthermore, what they measure is both stable over time in individuals and has significant predictive power, in particular for future academic performance and other mentally demanding pursuits

### 1.1. Theories of intelligence
* A central question in the study of intelligence concerns whether intelligence should be viewed as one ability, or many

### 1.2. Definitions of human intelligence
* The most elementary common feature of these definitions is that intelligence is seen as a property of an individual who is interacting with an external environment, problem or situation
* Another common feature is that an individual's intelligence is related to their ability to succeed or profit. This implies the existence of some kind of objective or goal
* Intelligence measures an agent's ability to achieve goals in a wide range of environments
* Must an agent be able to tackle some task immediately, or perhaps after a short period of time during which learning can take place, or perhaps it only matters that they can eventually learn to deal with the problem?
* Intelligence seems to be the ability to adapt and learn as quickly as possible given the constraints imposed by the problem at hand

### 1.3. Definitions of machine intelligence
* A key goal of artificial intelligence is to find algorithms which have the greatest efficiency of intelligence, that is, which achieve the most intelligence per unit of computational resources consumed

### 1.4. Intelligence testing
* There are many properties that a good test of intelligence should have
	* The test should be repeatable, in the sense that it consistently returns about the same score for a given individual
	* Should be valid in the sense that it appears to be testing what it claims it is testing for
	* A test should have predictive power, for example the ability to predict future academic performance, or performance in other cognitively demanding tasks

### 1.6 Animal intelligence tests
* It is not always clear how to validate an intelligence test for animals: if survival or the total number of offspring was a measure of success, then bacteria would be the most intelligent life on earth!
* One interesting difficulty when testing animal intelligence is that we are unable to directly explain to the animal what its goal is


## 2. Universal Artificial Intelligence
### 2.1. Inductive inference
* Inductive inference is the process by which one observes the world and then infers the causes behind what has been observed
* There typically exist many hypothesis which are consistent with all of the available data (Epicurus)
	* Keep all hypotheses that are consistent with the data

### 2.8. Agent-environment model
* The agent-environment model
	* The model consists of two entities called the agent and the environment
		* The agent receives input information from the environment, which we will refer to as perceptions, and sends output information back to the environment, which we call actions
		* The action receives actions from the agent as input and generates perceptions as output
	* Each perception consists of an observation component and a reward component
		* Observations are just regular information, however rewards have a special significance because the goal of the agent is to try to gain as much reward as possible from the environment
* The agent sends information to the environment by sending symbols from some finite alphabet of symbols. We call this set the action space and denote it by $\mathcal{A}$
* The environment sends signals to the agent with symbols from an alphabet called the perception space, which we denote $\mathcal{X}$
* The reward space, denoted by $\mathcal{R}$, is always a subset of the rational unit interval $[0, 1] \cap \mathbb{Q}$
* Every perception consists of two separate parts: an observation and a reward
* The agent is a function, denoted by $\pi$, which takes the current history as input and chooses the next action as output

### 2.9. Optimal informed agents
* Which of these two agents is the better one? The answer depends on how we value reward at different points in the future
	* In some situations we may want our agent to perform well quickly, and thus place more value on short term rewards. In others, we might only care that it eventually reaches a level of performance that is as high as possible, thus place relatively high value on rewards far into the future
* We need to formally express our temporal preferences
	* A general approach is to weight, or discount, each reward in a way that depends on which cycle it occurs in
* The optimal agent for an environment $\mu$ and discounting $\gamma$ is the agent $\pi^\mu$ that has maximal expected future discounted reward
$$
\pi^\mu := \underset{\pi}{\arg\max} V_\gamma^{\pi\mu}
$$

# See also

# References
* Legg, Shane. Machine super intelligence. Diss. Università della Svizzera italiana, 2008.