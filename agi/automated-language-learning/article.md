---
title: Automated language learning
created: 2016-11-17
taxonomy:
  status: in progress
  tag: [artificial general intelligence]
---

## Context

## Learned in this study

## Things to explore
* Build a generalization tree

# Overview
* Words can be represented as integers (or vectors in a vector space)
	* Given a vectorial representation, it might be possible construct a semantic representation such that adding word vectors lead to words that are the composition of the given "sub-words"
* There exists some groups with distinctive properties (punctuation, uppercase, lowercase, spaces)
* Groups in turn become abstractions of their members (letters -> words -> first name -> full name)
* Some textual constructs have some internal structure such that it is composed of multiple components
* Some of these components may not always be present
* They may follow different rules and formats yet represent the same thing/information
* Learning is initially based on association combined with reinforcement learning
* At some point it becomes possible to indicate to the agent that something should be remembered (forced learning)

## Declarative vs procedural memory
* Procedural memory relies on many parts of the network to function properly but at the same time it is based on strongly redundant subnetworks (networks composed of the same function multiple times but with slight variations)
* Declarative memory on the other hand is stored more compactly and with less redundancy, thus it is a lot less resilient than procedural memory
* Furthermore, accessibility of a declarative memory is based on the capacity of the network to activate enough related/associated memories for the target memory to activate

## Memory pruning: when, why and how
* When: pruning is done over a period of time, as a memory (or associated relations) is not often used, its association to other memories slowly disintegrate until it becomes unaccessible or distorted
* Why: memory eviction policy is least (recently) accessed, or possibly least strongly associated (with the least amount of referents)
* How: pruning occurs naturally through the competition of memories with one another. The memories that are the most referred to are likely to be important, and thus their links are kept strong, which makes them unlikely to fade

# See also

# References
