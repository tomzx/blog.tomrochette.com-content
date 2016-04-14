---
title: Building Machines That Learn and Think Like People (2016)
created: 2016-04-09
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview

## 1 Introduction
* Two different computational approaches to intelligence
	* Statistical pattern recognition
	* Model-building

## 1.1 What this article is not
* Neural networks have been applied in compelling ways to many type of machine learning problems, demonstrating the power of gradient-based learning and deep hierarchies of latent variables
* We believe that reverse engineering human intelligence can usefully inform AI and machine learning
* Some exciting progress
	* Probabilistic machine learning
	* Automated statistical reasoning techniques
	* Automated techniques for model building and selection
	* Probabilistic programming learning

## 1.2 Overview of the key ideas
* Ingredient: Two pieces of developmental start-up software
	* Intuitive physics
	* Intuitive psychology
* Ingredient: Learning is a form of model building
	* Explaining observed data through the construction of causal models of the world
* Compared to state-of-the-art algorithms in machine learning, human learning is distinguished by its richness and its effeciency
* We suggest that compositionality and learning-to-learn are ingredients that make this type of rapid model learning possible
* Ingredient: How the rich models our minds build are put into action, in real time

## 3 Challenges for building more human-like machines
* Two challenges for machine learning and AI:
	* Learning simple visual concepts
	* Learning to play the Atari game Frostbite

## 3.1 The Characters Challenge
* While humans and neural networks may perform equally well on the MNIST digit recognition task and other large-scale image classification tasks, it does not mean that they learn and think in the same way. There are at least two important differences
	* People learn from fewer examples
	* People learn richer representations
* People learn more than how to do pattern recognition: they learn a concept
* In addition to recognizing new examples, people can also
	* generate new examples
	* parse a character into its most important parts and relations
	* generate new characters given a small set of related characters
* The Characters Challenge: learn more from a lot less and capture human-level learning abilities in machines

## 3.2 The Frostbite Challenge
* Requires temporally extended planning strategies
* The neural networks are trained anew for each game, meaning the visual system and the policy are highly specialized for the games it was trained on (so no inter-game reusability of the trained/learned policy)
* The DQN was trained on 200 million frames from each of the games, which equates to approximately 924 hours of game time (~38 days), or almost 500 times as much experience as the human received (about 2h)
* The differences between the human and machine learning curves suggest that they (the machines) may be learning different kinds of knowledge, using different learning mechanisms, or both
* We speculate that people do this by inferring a general schema to describe the goals of the game and the object types and their interactions, using the kinds of intuitive theories, model-building abilities and model-based planning mechanisms we describe (I think that machine learning and human learning is simply very different because they start from scratch and we already have an immense amount of knowledge to build on top of)
* The DQN (deep Q neural network) is also rather inflexible to changes in its inputs and goals: changing the color or appearance of objects or changing the goals of the network would have devastating consequences on performance if the network is not retrained

# See also

# Sources
* [arXiv:1604.00289v1](https://arxiv.org/abs/1604.00289v1) [cs.AI]