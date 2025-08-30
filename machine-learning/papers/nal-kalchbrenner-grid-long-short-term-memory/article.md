---
title: Nal Kalchbrenner - Grid Long Short-Term Memory (2016)
created: 2017-06-16
taxonomy:
  tag: [machine-learning]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview

# Notes
## 1 Introduction
* N-dimensional Grid LSTM (N-LSTM for short) can naturally be applied as feed-forward networks as well as recurrent ones
* One-dimensional Grid LSTM corresponds to a feed-forward network that uses LSTM cells in place of transfer functions such as tanh and ReLU
	* These networks are related to Highway Networks where a gated transfer function is used to successfully train feed-forward networks with up to 900 layers of depth
* Grid LSTM with two-dimensions is analogous to the Stacked LSTM, but it adds cells along the depth dimension too
* Grid LSTM with three or more dimensions is analogous to Multidimensional LSTM, but differs from it not just by having the cells along the depth dimension, but also by using the proposed mechanism for modulating the N-way interaction that is not prone to the instability present in Multidimensional LSTM

## 3 Architecture
### 3.1 Grid LSTM Blocks

# See also
* [Multi-Dimensional Recurrent Neural Networks](../alex-graves-multi-dimensional-recurrent-neural-networks/article.md)

# References
* Kalchbrenner, Nal, Ivo Danihelka, and Alex Graves. "Grid long short-term memory." arXiv preprint arXiv:1507.01526 (2015).
