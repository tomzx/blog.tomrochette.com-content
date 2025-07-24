---
title: Tomas Mikolov - Efficient Estimation of Word Representations in Vector Space (2013)
created: 2017-07-14
taxonomy:
  tag: [machine learning]
  status: finished
---

## Context

## Learned in this study

## Things to explore

# Overview

# Notes
## 1 Introduction
### 1.1 Goals of the Paper
* We expect that not only will similar words tend to be close to each other (in vector space), but that words can have multiple degrees of similarity

## 2 Model Architectures
* The training complexity is proportional to
$$
O = E \times T \times Q
$$
where $E$ is the number of training epochs, $T$ is the number of the words in the training set and $Q$ is defined further for each model architecture

### 2.1 Feedforward Neural Net Language Model (NNLM)
* At the input layer, $N$ previous words are encoded using 1-of-V coding, where V is the size of the vocabulary
* The input layer is then projected to a projection layer $P$ that has dimensionality $N \times D$, using a shared projection matrix
* As only $N$ inputs are active at any given time, composition of the projection layer is a relative cheap operation
* The NNLM architecture becomes complex for computation between the projection and the hidden layer, as values in the projection layer are dense
* In our model, we use hierarchical softmax where the vocabulary is represented as a Huffman binary tree

## 3 New Log-linear Models
* Most of the complexity is caused by the non-linear hidden layer in the model
* The new architectures directly follow those proposed in our earlier work, where it was found that neural network language model can be successfully trained in two steps:
	* continuous word vectors are learned using simple model
	* the N-gram NNLM is trained on top of these distributed representation of words

### 3.1 Continuous Bag-of-Words Model
* The first proposed architecture is similar to the feedforward NNLM, where the non-linear hidden layer is removed and the projection layer is shared for all words; thus, all words get projected into the same position (their vectors are averaged)
* We call this architecture a bag-of-words model as the order of words in the history does not influence the projection
* We also use words from the future; we have obtained the best performance on the task introduced [in the next section] by building a log-linear classifier with four future and four history words at the input, where the training criterion is to correctly classify the current (middle) word

### 3.2 Continuous Skip-gram Model
* The second architecture is similar to CBOW, but instead of predicting the current word based on the context, it tries to maximize classification of a word based on another word in the same sentence
* We use each current word as an input to a log-linear classifier with continuous projection layer, and predict words within a certain range before and after the current word

## 4 Results
* We follow previous observation that there can be many different types of similarities between words, for example, word big is similar to bigger in the same sense that small is similar to smaller
* We further denote two pairs of words with the same relationship as a question, as we can ask: "What is the word that is similar to small in the same sense as biggset is similar to big"
* These questions can be answered by performing simple algebraic operations with the vector representation of words
	* To find a word that is similar to small in the same sense as biggest is similar to big, we can simply compute vector $X = vector("biggest") - vector("big") + vector("small")
	* Then, we search in the vector space for the word closest to $X$ measured by cosine distance, and use it as the answer to the question

### 4.2 Maximization of Accuracy
* It can be seen that after some point, adding more dimensions or adding more training data provides diminishing improvements
* We have to increase both vector dimensionality and the amount of the training data together

# See also

# References
* Mikolov, Tomas, et al. "Efficient estimation of word representations in vector space." arXiv preprint arXiv:1301.3781 (2013).
