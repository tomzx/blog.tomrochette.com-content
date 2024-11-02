---
title: Geoffrey Hinton - Distilling the Knowledge in a Neural Network (2015)
created: 2017-07-07
taxonomy:
  tag: [Machine learning]
  status: finished
---

## Context

## Learned in this study
* One should train complex models in order to extract a model from a given dataset, then train simpler/smaller/faster/more efficient models that can be used to do inference/prediction

## Things to explore
* Is it possible to reproduce the effect of CNN without using them?
	* How much computation would that require vs using them directly?
* The more abstract idea is, given a set of functions you can use to build a function f, if we were to remove a subset of this set of functions, would it still be possible to reproduce this function?
	* On first thought, I'd say it is not possible, as you might be missing pieces (or similarly, trying to produce a given vector with a set of vectors, where no combination of these vectors can produce a certain point in the space (doesn't span the whole space))

# Overview
* Soft targets can transfer a great deal of knowledge
* Train a smaller neural network so that it learns the softmax (last layer) activations of the larger neural network

# Notes
## 1 Introduction
* In large-scale machine learning, we typically use very similar models for the training stage and the deployment stage despite their very different requirements
* The analogy with insects suggests that we should be willing to train very cumbersome models if that makes it easier to extract structure from the data. The cumbersome model could be an ensemble of separately trained models or a single very large model trained with a very strong regularizer such as dropout. Once the cumbersome model has been trained, we can then use a different kind of training, which we call "distillation" to transfer the knowledge from the cumbersome model to a small model that is more suitable for deployment
* A conceptual block that may have prevented more investigation of this very promising approach is that we tend to identify the knowledge in a trained model with the learned parameter values and this makes it hard to see how we can change the form of the model but keep the same knowledge
* A more abstract view of the knowledge, that frees it from any particular instantiation, is that it is a learned mapping from input vectors to output vectors
* An obvious way to transfer the generalization ability of the cumbersome model to a small model is to use the class probabilities produced by the cumbersome model as "soft targets" for training the small model
* When the cumbersome model is a large ensemble of simpler models, we can use an arithmetic or geometric mean of their individual predictive distributions as to soft targets
* When the soft targets have high entropy, they provide much more information per training case than hard targets and much less variance in the gradient between training cases, so the small model can often be trained on much less data than the original cumbersome model and using a much higher learning rate

## 2 Distillation
* In the simplest form of distillation, knowledge is transferred to the distilled model by training it on a transfer set and using a soft target distribution for each case in the transfer set that is produced by using the cumbersome model with a high temperature in its softmax
	* The same high temperature is used when training the distilled model, but after it has been trained it uses a temperature of 1

# 7 Relationship to Mixtures of Experts
* It is much easier to parallelize the training of multiple specialists
* We first train a generalist model and then use the confusion matrix to define the subsets that the specialists are trained on
* Once these subsets have been defined the specialists can be trained entirely independently
* At test time we can use the predictions from the generalist model to decide which specialists are relevant and only these specialists need to be run

# See also

# References
* Hinton, Geoffrey, Oriol Vinyals, and Jeff Dean. "Distilling the knowledge in a neural network." arXiv preprint arXiv:1503.02531 (2015).
