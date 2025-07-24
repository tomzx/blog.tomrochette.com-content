---
title: Alex Graves - Multi-Dimensional Recurrent Neural Networks (2007)
created: 2017-06-16
taxonomy:
  tag: [machine learning]
  status: finished
---

## Context

## Learned in this study

## Things to explore

# Overview

# Notes
## 2 Multi-Dimensional Recurrent Neural Networks
* The basic idea of MDRNNs is to replace the single recurrent connection found in standard RNNs with as many recurrent connections as there are dimensions in the data
* The data must be processed in such a way that when the network reaches a point in an n-dimensional sequence, it has already passed through all the points from which it will receive its previous activations

### 2.1 Multi-directional MDRNNs
* BRNNs (Bidirectional RNNs) contain two separate hidden layers that process the input sequence in the forward and reverse directions. The two hidden layers are connected to a single output layer, thereby providing the network with access to both past and future context
* BRNNs can be extended to n-dimensional data by using $2^n$ separate hidden layers, each of which processes the sequence using the ordering defined (the network must have passed through all the points from which it will receive its previous activations), but with a different choice of axes. More specifically, the axes are chosen so that their origins lie on the $2^n$ vertices of the sequence

### 2.2 Multi-dimensional Long Short-Term Memory
* For standard RNN architectures, the range of context that can practically be used is limited. The problem is that the influence of a given input on the hidden layer, and therefore on the network output, either decays or blows up exponentially as it cycles around the network's recurrent connections. This is usually referred to as the vanishing gradient problem

## 3 Experiments
### 3.1 Air Freight Data
* Multi-directional MDRNN with 4 LSTM hidden layers
* Each layer consists of 25 memory blocks, each containing 1 cell, 2 forget gates, 1 input gate, 1 output gate and 5 peephole weights
* Input is size 3 (red, green, blue component of the pixels)
* Output is size 155 (one unit for each textural class)
* Input and output activation functions are tanh, and the activation function for the gates is the logistic sigmoid
* Softmax activation at the output layer, with cross-entropy objective function

pixels
(
	-> 25*LSTM(2 forget, 1 input, 1 output, 5 peephole, tanh)
	-> 25*LSTM(2 forget, 1 input, 1 output, 5 peephole, tanh)
	-> 25*LSTM(2 forget, 1 input, 1 output, 5 peephole, tanh)
	-> 25*LSTM(2 forget, 1 input, 1 output, 5 peephole, tanh)
)
-> softmax

### 3.2 MNIST Data
* We carried out a slightly modified task where each pixel was classified according to the digit it belonged to, with an additional class for background pixels
* The results on the warped MNIST data set suggests that MDRNNs are more robust to input warping than convolution networks

### 3.3 Analysis
* One benefit of two dimensional tasks is that the operation of the network can be easily visualized

# See also

# References
* Graves, Alex, Santiago Fernández, and Jürgen Schmidhuber. "Multidimensional recurrent neural networks." Proceedings of the international conference on artificial neural networks. 2007.
