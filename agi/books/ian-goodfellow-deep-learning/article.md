---
title: Ian Goodfellow - Deep Learning - 2016
created: 2017-01-01
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview

# Notes
## 1 Introduction
* In the early days of artificial intelligence, the field rapidly tackled and solved problems that are intellectually difficult for human beings but relatively straightforward for computers - problems that can be described by a list of formal, mathematical rules
* The true challenge to artificial intelligence proved to be ... problems that we solve intuitively, that feel automatic, ...
* The book solution to this problem is to allow computers to learn from experience and understand the world in terms of a hierarchy of concepts, with each concept defined in terms of its relation to simpler concepts
* If we draw a graph showing how these concepts are built on top of each other, the graph is deep, with many layers
* Abstract and formal tasks that are among the most difficult mental undertakings for a human being are among the easiest for a computer
* One of the key challenges in artificial intelligence is how to get this informal knowledge into a computer
* The difficulties faced by systems relying on hard-coded knowledge suggest that AI systems need the ability to acquire their own knowledge, by extracting patterns from raw data (known as machine learning)
* The performance of (these) simple machine learning algorithms depends heavily on the representation of the data they are given
* Each piece of information included in the representation ... is known as a feature
* Many artificial intelligence tasks can be solved by designing the right set of features to extract for that task, then providing these features to a simple machine learning algorithm
* Representation learning: To discover not only the mapping from representation to output but also the representation itself
* Learned representation often result in much better performance than can be obtained with hand-designed representations
* An autoencoder is the combination of an encoder function that converts the input data into a different representation, and a decoder function that converts the new representation back into the original format
* When it is nearly as difficult to obtain a representation as to solve the original problem, representation learning does not, at first glance, seem to help us
* Deep learning solves this central problem in representation learning by introducing representations that are expressed in terms of other, simpler representations
* Deep learning allows the computer to build complex concepts out of simpler concepts
* Depth allows the computer to learn a multi-step computer program. Each layer of the representation can be thought of as the state of the computer's memory after executing another set of instructions in parallel
* Networks with greater depth can execute more instructions in sequence
* According to this view of deep learning, not all the information in a layer's activations necessarily encodes factors of variation that explain the input. The representation also stores state information that helps to execute a program that can make sense of the input
* Three waves of development of deep learning
	* 1940-1960 Cybernetics
	* 1980-1990 Connectionism
	* 2006-now Deep learning
* The neural perspective on deep learning is motivated by two main ideas:
	* The brain provides a proof by example that intelligent behavior is possible, and a conceptually straightforward path to building intelligence is to reverse engineer the computational principles behind the brain and duplicate its functionality
	* It would be deeply interesting to understand the brain and the principles that underlie human intelligence, so machine learning models that shed light on these basic scientific questions are useful apart from their ability to solve engineering applications
* Neuroscience has given us a reason to hope that a single deep learning algorithm can solve many different tasks
* We are able to draw some rough guidelines from neuroscience
	* The basic idea of having many computational units that become intelligent only via their interactions with each other is inspired by the brain
	* Greater neural realism has not yet led to an improvement in machine learning performance
	* We do not yet know enough about biological learning for neuroscience to offer much guidance for the learning algorithms we use to train neural network architectures
* One should not view deep learning as an attempt to simulate the brain
* The central idea in connectionism is that a large number of simple computational units can achieve intelligent behavior when networked together
* Distributed representation: Each input to a system should be represented by many features, and each feature should be involved in the representation of many possible inputs
* The amount of skill required (to get good performances from a deep learning algorithm) reduces as the amount of training data increases
* A rough rule of thumb is that a supervised deep learning algorithm will generally achieve acceptable performance with around 5000 labeled examples per category, and will match or exceed human performance when trained with a dataset containing at least 10 million labeled examples
* One of the main insights of connectionism is that animals become intelligent when their neurons work together
* Unless new technologies allow faster scaling, artificial neural networks will not have the same number of neurons as the human brain until at least 2050s

# See also

# References
* Goodfellow, Ian, Yoshua Bengio, and Aaron Courville. Deep learning. MIT Press, 2016.
* https://www.amazon.com/Deep-Learning-Adaptive-Computation-Machine/dp/0262035618