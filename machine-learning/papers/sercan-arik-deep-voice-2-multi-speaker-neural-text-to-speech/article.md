---
title: "Sercan Arik - Deep Voice 2: Multi-Speaker Neural Text-to-Speech (2017)"
created: 2017-06-01
taxonomy:
  tag: [machine-learning]
  status: finished
  readability: 3
---

## Context

## Learned in this study

## Things to explore
* Which building blocks of the Deep Voice (1) model can be trained and shared on all the speakers voice?
* Which part of the Deep Voice pipeline is unique to each speaker (its speech signature/fingerprint)?

# Overview
* Multi-speaker support is added by augmenting the existing model with an embedding vector which represents a speaker

# Notes
## 3 Single-Speaker Deep Voice 2
* One major difference between Deep Voice 2 and Deep Voice 1 is the separation of the phoneme duration and frequency models

### 3.1 Segmentation Model
* The major architecture changes in Deep Voice 2 are the addition of batch normalization and residual connections in the convolutional layers
* We introduce a small post-processing step to correct segmentation mistakes for boundaries between silence phonemes and other phonemes: whenever the segmentation model decodes a silence boundary, we adjust the location of the boundary with a silence detection heuristic

### 3.2 Duration Model
* Instead of predicting a continuous-valued duration, we formulate duration prediction as a sequence labeling problem
* We discretize the phoneme duration into log-scaled buckets, and assign to each input phoneme the bucket label corresponding to its duration

## 4 Multi-Speaker Models with Trainable Speaker Embeddings
* In order to synthesize speech from multiple speakers, we augment each of our models with a single low-dimensional speaker embedding vector per speaker
* We use speaker embeddings to produce recurrent neural network (RNN) initial states, nonlinearity biases, and multiplicative gating factors, used throughout the network

### 4.2 Multi-Speaker Tacotron
#### 4.2.1 Character-to-Spectrogram Model
* The Tacotron character-to-spectrogram architecture consists of
	* a convolution-bank-highway-GRU (CBHG) encoder
	* an attentional decoder
	* a CBHG post-processing network

# See also

# References
* Arik, Sercan, et al. "Deep Voice 2: Multi-Speaker Neural Text-to-Speech." arXiv preprint arXiv:1705.08947 (2017).
