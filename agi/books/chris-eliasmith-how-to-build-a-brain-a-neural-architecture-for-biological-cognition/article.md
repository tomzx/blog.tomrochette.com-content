---
title: Chris Eliasmith - How to Build a Brain: A Neural Architecture for Biological Cognition - 2015
created: 2017-08-17
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview

# Notes
## 1. The Science of Cognition
### 1.1 The Last 50 Years
* Explaining reaction times addresses only a small part of cognitive system dynamics in general, and the ACT-R explanations rely on assuming a 50 ms "cycle time," which itself is not explained
* If you want to build a fast cognitive system - one that directly interacts with the physics of the world - then the most salient constraints on your system are the physical dynamics of actions and perception
* What is a cognitive system? A system that integrates all aspects of sophisticated behavior. It is a system that must simultaneously realize a wide array of biological behaviors
* Good questions outrank easy answers

### 1.2 How We Got Here
* I consider a cognitive architecture to be "a general proposal about the representations and processes that produce intelligent thought"
* In the last half-century, there have been three major approaches to theorizing about the nature of cognition
	* The classical symbolic approach (symbolicism or Good Old-fashioned Artificial Intelligence)
	* Connectionism (Parallel Distributed Processing)
	* Dynamicism: Cognitive systems are non-representational, low-dimensional, dynamical systems. Cognitive systems can only be properly understood by characterizing their state changes through time
* Classical control theory characterizes physical systems by identifying a "transfer function" that directly maps inputs to outputs
	* Does not consider the internal states of a system
* Once cognitive scientists began to think of minds as computers, a number of new theoretical tools became available for characterizing cognition
* It suggested novel philosophical theses
	* Functionalism: the notion that only the mathematical function computed by a system is relevant for its being a mind or not
	* Multiple realizability: the notion that a mind could be implemented in pretty much any substrate - water, silicon, interstellar gas, etc. - as long as it computed the appropriate function

### 1.3 Where We Are
* What are the Core Cognitive Criteria (CCC)?
	* Dynamicism: Cognition is distinguished from other kinds of complex natural processes... by at least two deep features: ... a dependence on knowledge; and distinctive kinds of complexity, as manifested most clearly in structural complexity of natural languages
	* Connectionism: They must explain motor control, perception, memory, and language
	* Symbolism: problem solving, decision making, routine action; memory, learning, skill; perception, motor behavior; language; motivation, emotion; imagining, dreaming, daydreaming
* Commonalities among these descriptions of cognitive behavior:
	* Language
	* The importance of adaptability and flexibility
	* Motor control and perception as important to understanding cognition
* Three explicit constraints on what it takes to be a cognitive system (according to Fodor and Pylyshyn)
	* Productivity: The ability of a system to generate a large number of representations based on a few basic representations (a lexicon) and rules for combining them (a grammar)
	* Systematicity: The fact that some sets of representations are intimately linked
	* Compositionality: The meaning of complex representations is a direct composition (i.e., adding together) of the meaning of the basic representations
* Jackendoff challenges to address when explaining cognition:
	* The massiveness of the binding problem (i.e., that very many basic representations must be bound to construct a complex representation)
	* The problem of two (i.e., how multiple instances of one representational token can be distinguished)
	* The problem of variables (i.e., how roles in a complex representation can be generically represented)
	* How to incorporate long-term and working memory into cognition
* Don Norman description of human cognition
	* Robust
	* Flexible
	* Reliant on "content-addressable" memory
* Two of the most important considerations for good scientific theories are those of unity and simplicity
	* Unity: The more sources of data, and the more scientific disciplines that they are consistent with, the better the theory

### 1.4 Questions and Answers
* How is semantic captured in the system?
* How is syntactic structure encoded and manipulated by the system?
* How is the flow of information flexibly controlled in response to task demands?
* How are memory and learning employed in the system?
* A semantic pointer is a neural representation that carries partial semantic content and is composable into representational structures needed to support complex cognition
* The relation between a semantic pointer and what it points to can be usefully thought of as a kind of compression
* Any characterization of a cognitive system has to provide some explanation for how relevant information is propagated through time, and how the system can adapt using its past experience

## 2. An Introduction to Brain Building
### 2.2 A Framework for Building a Brain
* The following three principles form the core of the Neural Engineering Framework(NEF)
	* Neural representations are defined by the combination of nonlinear encoding (exemplified by neuron tuning curves and neural spiking) and weighted linear decoding (over population of neurons and over time)
	* Transformations of neural representations are functions of the variables represented by neural populations. Transformations are determined using an alternately weighted linear decoding
	* Neural dynamics are characterized by considering neural representations as state variables of dynamic systems. Thus, the dynamics of neurobiological systems can be analyzed using control (or dynamic systems) theory
* It seems that neurons tend to encode approximately two to seven bits of information per spike
* It is reasonable to begin with the hypothesis that "higher-level" properties are inferred on the basis of representations of properties more like those that physicists talk about
	* In other words, the encoding of "edible" depend, in some complex way, on encodings of "lower-level" physical properties like wavelength, velocity, and so forth
* One crucial aspect of the NEF principle of representation is that it can be used to characterize arbitrarily complex representations
* A second crucial aspect of this principle is that it distinguishes the mathematical object being represented from the neurons that are representing it
	* I refer to the former as the "state space" and the latter as the "neuron space"
* A third crucial aspect of this principle is that it embraces the heterogeneity of neural representation

#### 2.2.2 Transformation
* A transformational decoder is a kind of biased decoding. That is, in determining a transformation, we extract information other than what the population is taken to represent
* In general, we can characterize non-linear functions of multiple scalars or vectors as linear decoding of some higher-dimensional representation in a population of neurons

### 2.3 Levels
* Some have suggested that because the reduction of one science to another has failed, the sciences must be independent
* Consequently, Fodor has argued that to understand cognitive systems, which lie in the domain of psychology, appeal to lower-level sciences is largely useless
* Levels should be taken as pragmatically identified sets of descriptions that share assumptions
* Most systems composed of parts have parts that interact
* If the parts of a system are organized in such a way that their interaction results in some regular phenomena, then they are called "mechanisms"
* Mechanisms are often analyzed by decomposing them into their simpler parts, which may also be mechanisms

# See also

# References
* Eliasmith, Chris. How to build a brain: A neural architecture for biological cognition. Oxford University Press, 2013.