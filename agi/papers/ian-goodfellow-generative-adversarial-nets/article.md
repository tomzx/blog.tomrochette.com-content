---
title: Ian Goodfellow - Generative Adversarial Nets (2014)
created: 2017-04-22
taxonomy:
  category: [Artificial General Intelligence]
  status: finished
---

## Context

## Learned in this study

## Things to explore

# Overview
* The discriminative model acts as a custom optimization function/objective
* In the Turing test context, the generative model can be seen as the machine which tries to emulate a human being as well as possible while the discriminative model is the human that has to determine whether it is discussing with a machine or another human
* The discriminator can be seen as an expert while the generative model as the student
* The generative model is trained on the worst case inputs, which are really hard for the model

# Notes
* A generative model G and a discriminative model D that estimates the probability that a sample came from the training data rather than G
* The goal of G is to maximize the probability that D will make a mistake
* In other words, we want G to look as much as the training data as possible (or become indistinguishable from what it models)

## 1 Introduction
* The problem: deep generative models have had less of an impact (vs classification models) due to the difficulty of approximating many intractable probabilistic computations that arise in maximum likelihood estimation and related strategies, and due to difficulty of leveraging the benefits of piecewise linear units in the generative context
* In the proposed adversarial nets framework, the generative model is pitted against an adversary: a discriminative model that learns to determine whether a sample is from the model distribution or the data distribution

## 6 Advantages and disadvantages
* Disadvantages
	* There is no explicit representation of $p_g(x)$
	* D must be synchronized well with G during training (in particular, G must not be trained too much without updating D, in order to avoid "the Helvetica scenario" in which G collapses too many values of $\textbf{z}$ to the same value of $\textbf{x}$ to have enough diversity to model $p_{data}$)
* Advantages
	* Markov chains are never needed
	* Only backprop is used to obtain gradients
	* No inference is needed during learning
	* A wide variety of functions can be incorporated into the model
	* Adversarial models may gain some statistical advantage from the generator network not being updated directly with data examples, but only with gradients flowing through the discriminator
	* They can represent very sharp, even degenerate distributions, while methods based on Markov chains require that the distribution be somewhat blurry in order for the chains to be able to mix between modes

# See also

# References
* Goodfellow, Ian, et al. "[Generative adversarial nets.](http://papers.nips.cc/paper/5423-generative-adversarial-nets.pdf)" Advances in neural information processing systems. 2014.
* [NIPS 2016 Workshop on Adversarial Training - Ian Goodfellow - Introduction to GANs](https://www.youtube.com/watch?v=RvgYvHyT15E)