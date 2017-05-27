---
title: Dzmitry Bahdanau - Neural Machine Translation by Jointly Learning to Align and Translate (2015)
created: 2017-05-20
taxonomy:
  category: [Machine Learning]
  status: finished
---

## Context

## Learned in this study

## Things to explore
* It seems (at least based on the Scan, attend, read paper) that the attention mechanism may have more difficulty with short "attention span" (short sentences) at the benefit of longer sentences, why is that?
* How different is a RNN from a feature vector including the preceding/following features?
	* Is that similar to an HMM?

# Overview
* The current encoder-decoder approach with fixed-length (word) vector is likely the source of problems with long sentences
* A bidirectional RNN encoder is used to encode preceding/following words to form a context
* A RNN decoder is trained to use the context and to determine where to focus its attention during decoding

# Notes
## 1 Introduction
* Most of the proposed neural machine translation models belong to a family of encoder-decoders, with an encoder and a decoder for each language
* A potential issue with this encoder-decoder approach is that a neural network needs to be able to compress all the necessary information of a source sentence into a fixed-length vector
	* This may make it difficult for the neural network to cope with long sentences, especially those that are longer than the sentences in the training corpus
	* Cho et al. showed that indeed the performance of a basic encoder-decoder deteriorates rapidly as the length of an input sentence increases
* An extension to the encoder-decoder model is introduced, which learns to align and translate jointly

## 3 Learning to Align and Translate
* The new architecture consists of a bidirectional RNN as an encoder and a decoder that emulates searching through a source sentence during decoding a translation

# See also

# References
* Bahdanau, Dzmitry, Kyunghyun Cho, and Yoshua Bengio. "Neural machine translation by jointly learning to align and translate." arXiv preprint arXiv:1409.0473 (2014).