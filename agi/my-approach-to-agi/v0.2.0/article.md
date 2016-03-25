---
title: AGI v0.2.0
created: 2016-03-24
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Learned in this study

## Things to explore

# Overview

There are many different routes one might want to look into.

First, we look into mathematical models and formal approaches such as AIXI/OOPS/Gödel machines where what we are doing is searching for programs using a proof searcher and a programmer runner. This approach thus requires the implementation of a proof searcher as well as some system that can execute the programs that have been found. It also requires some sort of goal from which it'll be possible to estimate some form of reward for which the AGI will try to optimize itself. The difficulty of this approach is figuring out the how to reward the AGI properly so that it does significant work.

Another approach is to build some sort of task systems, where perception is one of many tasks the system has to deal with. Other tasks are internal decisions, evaluations, priorization, etc. In this approach, we have to implement most of the internals of the AGI. The nice thing about this approach is that we can program it in such a way that we may inspect and understand it, however it also means that it will most likely be limited to how it was designed and will make it difficult to evolve.

An approach similar to the previous one could be to use many specialized neural networks together in order to accomplish specific tasks. Each neural network would be trained for a single purpose and a general neural network would be tasked with determining which specialized neural network should process the task at hand. Using an approach similar to the one presented by AlphaGo, this AGI would use a policy network and a value network in order to drive its decisions. The policy network would be used to evaluate the potential actions based on previous experiences (and their probabilities) while the value network would help the policy network decide toward which direction it should go.

# See also

# Sources