---
title: Ashish Vaswani - Attention Is All You Need (2017)
created: 2017-07-06
taxonomy:
  tag: [Machine learning]
  status: finished
---

## Context

## Learned in this study

## Things to explore

# Overview

# Notes
## 1 Introduction
* Attention mechanisms have become an integral part of compelling sequence modeling and transduction models in various tasks, allowing modeling of dependencies without regard to their distance in the input or output sequences

## 2 Background
* The number of operations required to relate signals from two arbitrary input or output positions grows in the distance between positions, linearly for ConvS2S and logarithmically for ByteNet
* This makes it more difficult to learn dependencies between distant positions
* In the Transformer this is reduced to a constant number of operations, albeit at the cost of reduced effective resolution due to averaging attention-weighted position, an effect we counteract with Multi-Head Attention
* Self-attention, sometimes called intra-attention is an attention mechanism relating different positions of a single sequence in order to compute a representation of the sequence

## 3 Model Architecture
### 3.1 Encoder and Decoder Stacks
* Encoder: The encoder is composed of a stack of $N = 6$ identical layers
* Each layer has two sub-layers
	* The first is a multi-head self-attention mechanism
	* The second is a simple, position-wise fully connected feed-forward network
* We employ a residual connection around each of the two sub-layers, followed by layer normalization
* TO facilitate these residual connections, all sub-layers in the model, as well as the embedding layers, produce outputs of dimension $d_{model} = 512$
* Decoder: The decoder is also composed of a stack of $N = 6$ identical layers
* In addition to the two sub-layers in each encoder layer, the decoder inserts a third sub-layer, which performs multi-head attention over the output of the encoder stack
* We also modify the self-attention sub-layer in the decoder stack to prevent positions from attending to subsequent positions
* This masking, combined with the fact that the output embeddings are offset by one position, ensures that the predictions for position $i$ can depend only on the known outputs at positions less than $i$

### 3.2 Attention
#### 3.2.1 Scaled Dot-Product Attention
* The input consists of queries and keys of dimension $d_k$, and values of dimension $d_v$
* We compute the dot products of the query with all keys, divide each by $\sqrt{d_k}$, and apply a softmax function to obtain the weights on the values
$$
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right) V
$$
* The two most commonly used attention functions are additive attention, and dot-product (multiplicative) attention
	* Dot-product attention is identical to our algorithm, except for the scaling factor $\sqrt{d_k}$
	* Additive attention computes the compatibility function using a feed-forward network with a single hidden layer

#### 3.2.2 Multi-Head Attention
* We found it beneficial to linearly project the queries, keys and values $h$ times with different, learned linear projections
* Multi-head attention allows the model to jointly attend to information from different representation subspaces at different positions
	* With a single attention head, averaging inhibits this

### 3.4 Embeddings and Softmax
* Similarly to other sequence transduction models, we use learned embeddings to convert the input tokens and output tokens to vectors of dimension $d_{model}$
* We also use the usual learned linear transformation and softmax function and convert the decoder output to predicted next-token probabilities

### 3.5 Positional Encoding
* Since our model contains no recurrence and no convolution, in order for the model to make use of the order of the sequence, we must inject some information about the relative or absolute position of the tokens in the sequence
	* To this end, we add "positional encodings" to the input embeddings at the bottoms of the encoder and decoder stacks

## 4 Why Self-Attention
* The total computational complexity per layer
* The amount of computation that can be parallelized, as measured by the minimum number of sequential operations required
* The path length between long-range dependencies in the network
* In terms of computational complexity, self-attention layers are faster than recurrent layers when the sequence length $n$ is smaller than the representation dimensionality $d$, which is most often the case with sentence representation used by SotA models in machine translations

# See also

# References
* Vaswani, Ashish, et al. "Attention Is All You Need." arXiv preprint arXiv:1706.03762 (2017).
