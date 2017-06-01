---
title: Sercan Arik - Deep Voice: Real-time Neural Text-to-Speech (2017)
created: 2017-06-01
taxonomy:
  category: [Machine Learning]
  status: finished
---

## Context

## Learned in this study

## Things to explore

# Overview
* Uses 5 building blocks/components in their pipeline
* Training take more than a week on 8 TitanX Maxwell GPUs
* Inference is more efficient if done on CPU than on GPU
* Efficient CPU inference appears to require a lot of complex engineering involving multithreading, synchronization, minimizing nonlinearity FLOPs, avoiding cache trashing and thread contention via thread pinning, as well as using custom hardware-optimized routines for matrix multiplication and convolution

# Notes
## Abstract
* Five major building blocks:
	* A segmentation model for locating phoneme boundaries
	* A grapheme-to-phoneme conversion model
	* A phoneme duration prediction model
	* A fundamental frequency prediction model
	* An audio synthesis model

## 1. Introduction
* Our only features are phonemes with stress annotations, phoneme durations, and fundamental frequency (F0)
* We train our entire pipeline on datasets that contains solely audio and unaligned textual transcriptions and generate relatively high quality speech

## 2. Related Work
* Deep Voice is completely standalone; training a new Deep Voice system does not require a pre-existing TTS system, and can be done from scratch using a dataset of short audio clips and corresponding textual transcripts
* Deep Voice minimizes the use of hand-engineered features; it uses one-hot encoded characters for grapheme to phoneme conversion, one-hot encoded phonemes and stresses, phoneme durations in milliseconds, and normalized log fundamental frequency that can be computed from waveforms using any F0 estimation algorithm
* Deep Voice can synthesize audio in fractions of a second, and offers a tunable trade-off between synthesis speed and audio quality

## 3. TTS System Components
### 3.1. Grapheme-to-Phoneme Model
* Model based on the encoder-decoder architecture by Yao & Zweig
* However, we use a multi-layer bidirectional encoder with a gated recurrent unit (GRU) nonlinearity and an equally deep unidirectional GRU decoder
* The initial state of every decoder layer is initialized to the final hidden state of the corresponding encoder forward layer
* The architecture is trained with teacher forcing and decoding is performed using beam search

## 3.2. Segmentation Model
* The connectionist temporal classification (CTC) loss function has been shown to focus on character alignments to learn a mapping between sound and text
* We adapt the convolutional recurrent neural network architecture from a state-of-the-art speech recognition system for phoneme boundary detection
* A network trained with CTC to generate sequences of phonemes will produce brief peaks for every output phoneme
	* Although this is sufficient to roughly align the phonemes to the audio, it is insufficient to detect precise phoneme boundaries
	* To overcome this, we train to predict sequences of phoneme pairs rather than single phonemes

## 3.3. Phoneme Duration and Fundamental Frequency Model
* We use a single architecture to jointly predict phoneme duration and time-dependent fundamental frequency
* The architecture comprises two fully connected layers followed by two unidirectional recurrent layers with GRU cells and finally a fully connected output layer

## 3.4. Audio Synthesis Model
* Our audio synthesis model is a variant of WaveNet

# See also

# References
* Arik, Sercan O., et al. "Deep Voice: Real-time neural text-to-speech." arXiv preprint arXiv:1702.07825 (2017).