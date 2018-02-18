---
title: Andrew Barto - Intrinsically Motivated Learning of Hierarchical Collections of Skills (2004)
created: 2018-02-15
taxonomy:
  category: [Machine Learning]
  status: finished
---

## Context

## Learned in this study

## Things to explore
* In their example, complexity comes from composition, but it seems sometimes that more difficult skills are not necessarily about complexity, but precision

# Overview

# Notes
## 1. Introduction
* Today's machine learning algorithms fall far short of the possibilities for machine learning
	* They are typically applied to single, isolated problems for each of which they have to be hand-tuned and for which training data sets have to be carefully prepared
	* They do not have the generative capacity required to significantly extend their abilities beyond initially built-in representations
	* They do not address many of the reasons that learning is so useful in allowing animals to cope flexibly with new problems as they arise over extended periods of time
* An agent's activity is said to be intrinsically motivated if the agent engages in it for its own sake rather than as a step toward solving a specific problem

## 3. Intrinsic Motivation in Reinforcement Learning
### Skills
* Autonomous mental development should result in a collection of reusable skills
* An option is something like a subroutine. It consists of
	* an option policy that directs the agent's behavior for a subset of the environment states
	* an initiation set consisting of all the states in which the option can be initiated
	* a termination condition, which specifies the conditions under which the option terminates
* An option is not a sequence of actions; it is a closed-loop control rule, meaning that it is responsive to on-going state changes

### Developing Hierarchical Collections of Skills
* It is clear that children accumulate skills while they engage in intrinsically motivated behavior, e.g., while at play
* When they notice that something they can do reliably results in an interesting consequence, they remember this in a form that will allow them to bring this consequence about if they wish to do so at a future time when they think it might contribute to a specific goal
* Whatever the details of how intrinsic reward is defined, it should diminish with continued repetition of the activity that generates it
* Similarly, exploration of regions about which the agent is not ready to learn should be aversive to the agent
* This process will naturally produce what Utgoff and Stracuzzi called "many-layered" learning in which the agent learns what is easy to learn first, then uses this knowledge to learn harder things

# See also

# References
* Barto, Andrew G., Satinder Singh, and Nuttapong Chentanez. "Intrinsically motivated learning of hierarchical collections of skills." Proceedings of the 3rd International Conference on Development and Learning. 2004.