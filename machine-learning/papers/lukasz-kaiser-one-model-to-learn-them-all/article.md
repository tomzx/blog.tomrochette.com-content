---
title: Lukasz Kaiser - One Model To Learn Them All (2017)
created: 2017-06-22
taxonomy:
  category: [Machine Learning]
  status: finished
---

## Context

## Learned in this study

## Things to explore

# Overview
* A network composed of convolution blocks, attention blocks and of mixture-of-experts blocks which can process categorical data, text, audio and images
* The network is able to improve its accuracy on existing tasks by learning tasks from another domain (image classification vs text translation)

# Notes
## 1 Introduction
* Can we create a unified deep learning model to solve tasks across multiple domains?
* Two key insights are crucial to making it (the MultiModel) work at all and are the main contributions of this work
	* Small modality-specific sub-networks convert into a unified representation and back from it
		* The unified representation is variable-size
		* Different tasks from the same domain share modality nets
	* Computational blocks of different kinds are crucial for good results on various problems

## 2 MultiModel Architecture
* The MultiModel consists of a few small modality-nets, an encoder, I/O mixer, and an autoregressive decoder
* The encoder and decoder are constructed using 3 computational blocks to get good performance across different problems:
	* Convolutions allow the model to detect local patterns and generalize across space
	* Attention layers allow to focus on specific elements to improve performance of the model
	* Sparsely-gated mixture-of-experts gives the model capacity without excessive computational cost

### 2.1 Convolutional Blocks
* A block of convolutions gets as input as tensor of shape [batch size, sequence length, feature channels] and returns a tensor of the same shape, processed as follows
* For convolution operations, we use depthwise separable convolutions
	* They are defined by a convolution on each feature channel separately, followed by a pointwise convolution to project to the desired feature depth
* Noted $SepConv_{d,s,f}(W, x)
	* d: dilation factor
	* s: stride
	* f: number of kernels of size $h \times w$
	* W: weights
	* x: input tensor
* We use convolutions in blocks that consist of three components:
	* A ReLU activation of the inputs
	* A $SepConv$
	* A layer normalization (LN)
* A complete convolution step is defined as
$$
ConvStep_{d,s,f}(W, x) = LN(SepConv_{d,s,f}(W, ReLU(x)))
$$
* The convolutional steps are composed into blocks by stacking them and adding residual connections
* We use stacks of four convolutional blocks with two skip-connections between the stack input and the outputs of the second and fourth convolutional steps

### 2.2 Attention Blocks
* We use a multi-head dot-product attention mechanism
* The inputs to the attention layer are two tensors: a source tensor and a target tensor both with the shape [batch size, sequence length, feature channels]
* The target tensor is additively composed with a timing signal and mixed using two convolutional blocks

### 2.3 Mixture-of-Experts Blocks
* We use sparsely-gated mixture-of-experts layers: A mixture-of-expert layer consists of a number of simple feed-forward neural networks (experts) and a trainable gating network which selects a sparse combination of the experts to process each input

### 2.4 Encoder and Mixer and Decoder
* To allow the decoder to produce outputs for different tasks even with the same modality, we always start decoding with a command-token, such as To-English or To-Parse-Tree
* We learn an embedding vector corresponding to each of the tokens during training

### 2.5 Modality Nets
* 4 modality nets
	* Language (text)
	* Images
	* Audio
	* Categorical data

# See also

# References
