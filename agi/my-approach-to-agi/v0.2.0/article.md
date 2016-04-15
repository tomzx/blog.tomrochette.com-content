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

## Mathematical and formal approach

First, we look into mathematical models and formal approaches such as AIXI/OOPS/Gödel machines where what we are doing is searching for programs using a proof searcher and a program runner. This approach thus requires the implementation of a proof searcher as well as some system that can execute the programs that have been found. The AGI will also need some form of reward stream or evaluation function which will allow it to determine if a newer program is superior to the current running program. This reward stream has the purpose to guide the AGI toward a given goal and as such, it will optimize itself to get to that goal as fast as possible.  The difficulty of this approach is figuring out  how to reward the AGI properly so that it does significant work or in other words, the reward evaluation function.

### What is missing?

* The seed proof searcher
* The evaluation function

## Tasks system approach

Another approach is to build some sort of task runner system, where perception is one of many tasks the system has to deal with. Other tasks are internal decisions, evaluations, priorization, etc. In this approach, we have to implement most of the internals of the AGI. The nice thing about this approach is that we can program it in such a way that we may inspect and understand it, however it also means that it will most likely be limited to how it was designed and will make it difficult to evolve on its own.

### What is missing?

* The necessary functions
* The code for all these functions
* How to hook everything together

## Neural network approach

An approach similar to the previous one could be to use many specialized neural networks together in order to accomplish specific tasks. Each neural network would be trained for a single purpose and a general neural network would be tasked with determining which specialized neural network should process the task at hand.

Using an approach similar to the one presented by AlphaGo, this AGI would use a policy network and a value network in order to drive its decisions. The policy network would be used to evaluate the potential actions based on previous experiences (and their probabilities) while the value network would help the policy network decide toward which direction it should go.

### What is missing?

* How to feed the network
* How to train the network
* What is the architecture of the network(s)?

## Brain replication approach
This approach is very much related to the neural network approach. The idea is to reverse engineer how the human body and the brain work in order to accomplish goals.

It makes sense to start first with how human embryos grow into humans simply through the use of the genetic code that was provided by its parents. This code is responsible for the formation of all the parts of the body through the consumption of energy and the obtention of the appropriate "construction" components from its host, its mother. This code could effectively be considered to be the bootstrapping code of the AGI.

But the information provided by the "growth" code may not be useful in itself to the purpose of the AGI we are searching for: one that can accomplish tasks given a goal. It may only be of interest to understand how the fully grown neural system works in concert with the different modalities of the body.

The interesting aspect of this approach is that it uses us, as human, as a proof that it is possible to produce such machine. Given the proper nutritive medium and the embryo, a host can birth a child that will be able to accomplish goals and have a life of its own.

### What is missing?

* 

# See also

# Sources