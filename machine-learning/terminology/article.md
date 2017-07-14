---
title: Machine learning terminology
created: 2016-02-04
taxonomy:
  category: [Machine Learning]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview
**Activation function** Given a value, the activation function returns a value (they are functions after all!). The purpose of activation functions are to return a value based on the sum of all the input arriving at the unit. Certain activation functions will return -1 or 0 for very large negative values and 1 for very large positive values (sigmoid/logistic, tanh or softsign). Other types of activation functions will not saturate (e.g., min to -1 or max to 1), which may cause the network to become unstable due to numerical instability of operations of large numbers against small numbers (or small numbers with small numbers and large numbers with large numbers).
**Add-one smoothing** Assign a count of 1 to unseen n-grams. This is done so that they at least have a very minor probability instead of none.
**BLAS** Basic Linear Algebra Subprograms. Generally, those are optimized linear algebra procedures that can be executed more efficiently on certain hardware.
**CNN** Convolutional neural network. A type of neural network layer based on the concept of applying **convolutions**. CNN are useful for translation invariance, that is, they will detect features wherever they are located within the image. CNN are mostly used in the context of vision/image problems or problems where the space structure provides additional information the network may benefit from.
**Convolution** The concept of convolution can be seen as the operation of applying a filter/kernel on a tensor. A convolution is generally the operation of multiplying the kernel (another tensor with defined values) at each location in the tensor with the associated cells, then summing all the associated values, which becomes the value of the cell in the produced tensor.
**Epsilon-greedy strategy/policy** (Reinforcement learning) An action in a set of actions A is selected at random with probability $\epsilon$ while we may pick the action that gives the maximum amount of reward (greedy) with probability $1 - \epsilon$.
**Filter** A tensor used in a convolution operation.
**Fingerprinting** Converting a large space into a small space for faster comparison. Common fingerprinting algorithms are hashes such as md5/sha1.
**One-hot encoding** The process of converting a nominal number into a **One-hot vector**, that is to say convert a value that is generally considered as part of an enumeration into a different representation. The purpose of one-hot encoding is to convert something that isn't numeric into a tensor representation. The reason nominal numbers can't be used directly in a neural network is that they do not represent linearity in the feature, that is to say nominal numbers 1, 2, 3, 4 representing "dog", "cat", "horse", "bird" do not represent that the "intermediate" of a dog and a horse is a cat; every item is a unique entity. This process thus turns a single feature into multiple features that represent the presence or absence of this nominal value (yes, this is a bird, no it is not a dog, a horse or a cat).
**n-gram** A sequence of N items, generally from a sequence of text. n-gram are generally used as atomic units in other systems, such as neural networks, where instead of representing two words, their bigram is given a unique **nominal number** and then is **one-hot encoded**.
**Nominal number** A number (generally an integer) that serves as a unique identifier for a more complex value, for instance a string. A nominal number can be thought of as the primary key in a SQL table, it only serves to unique represent the row but generally has no meaning by itself.
**Normalization** The process of converting numbers with arbitrary range so that they are contained within the [-1, 1] or [0, 1] range. This is mainly done because within neural networks the scale of various features can have an impact on the first layer and any subsequent layers if the first layer does not saturate.
**One-hot vector** A vector which is 0 in most dimension and 1 in a single dimension. Ex: [0, 0, 0, 0, 0, 1, 0, 0, 0]. One-hot vectors are generally used to encode **Nominal number**.
**Skip-grams** Generalization of **n-grams** in which the components (typically words) need not be consecutive in the text under consideration, but may leave gaps that are skipped over. Thus, in a sentence such as "This is a simple example sentence.", a skip-gram could be "This a", "is simple", "a example", "simple sentence" for a 1-skip bigram. In the same fashion as **n-grams**, probabilities would be associated with the skip-grams, allowing our system to better predict subsequent items.
**Syntactic n-grams** **n-grams** defined by paths in syntactic dependency or constituent trees rather than the linear structure of the text. Syntactic n-grams can be thought as **skip-grams** where the distance varies based on the length of the syntactic item.

# See also

# References
