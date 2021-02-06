---
title: "Kelvin Xu - Show, Attend and Tell: Neural Image Caption Generation with Visual Attention (2015)"
created: 2017-07-06
taxonomy:
  category: [Machine learning]
  status: finished
---

## Context

## Learned in this study

## Things to explore

# Overview

# Notes
## 1. Introduction
* Two attention-based image caption generators under a common framework:
	* A "soft" deterministic mechanism trainable by standard back-propagation methods
	* A "hard" stochastic attention mechanism trainable by maximizing an approximate variational lower bound or equivalently by REINFORCE

## 3. Image Caption Generation with Attentio Mechanism
### 3.1. Model Details
#### 3.1.1. Encoder: Convolutional Features
* We use a convolutional neural network in order to extract a set of feature vectors which we refer to as annotation vectors
* The extractor produces $L$ vectors, each of which is a $D$-dimensional representation  corresponding to a part of the image
* In order to obtain a correspondence between the feature vectors and portions of the 2D image, we extract features from a lower convolutional layer

#### 3.1.2 Decoder: Long Short-Term Memory Network
* We use a long short-term memory (LSTM) network that produces a caption by generating one word at every time step conditioned on a context vector, the previous hidden state and the previously generated words

# See also

# References
* Xu, Kelvin, et al. "Show, attend and tell: Neural image caption generation with visual attention." International Conference on Machine Learning. 2015.
