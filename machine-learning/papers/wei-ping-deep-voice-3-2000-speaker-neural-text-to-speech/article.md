---
title: "Wei Ping - Deep Voice 3: 2000-Speaker Neural Text-to-Speech (2017)"
created: 2017-12-07
taxonomy:
  tag: [machine-learning]
  status: finished
---

## Context

## Learned in this study
* Attention Error Modes: mispronunciations, skipped words, and repeated words

## Things to explore

# Overview

# Notes
## 1 Introduction
* A fully-convolutional character-to-spectrogram architecture, which enables fully paralleled computation over elements in a sequence and trains an order of magnitude faster than analogous architectures using recurrent cells

## 2 Related Work
* In contrast to Deep Voice 1 & 2, Deep Voice 3 employs an attention-based sequence-to-sequence model, yielding a more compact architecture
* Deep Voice 3 avoids RNNs to speed up training and alleviates several challenging error modes that attention models fall into

## 3 Model Architecture
* Deep Voice 3 architecture consists of three components:
	* Encoder: A fully-convolutional encoder, which converts textual features to an internal learned representation
	* Decoder: A fully-convolutional causal decoder, which decodes the learned representation with a multi-hop convolutional attention mechanism into a low-dimensional audio representation (mel-band spectrograms) in an auto-regressive manner
	* Converter: A fully-convolutional post-processing network, which predicts final output features (depending on the waveform synthesis method) from the decoder hidden states. Unlike the decoder, the converter is non-causal and can thus depend on future context information

### 3.1 Text Preprocessing
* Uppercase all characters in the input text
* Remove all intermediate punctuation marks
* End every utterance with a period or question mark
* Replace spaces between words with special separator characters which indicate the duration of pauses inserted by the speaker between words

## 4 Results
* Fast Training
	* The average training iteration time is 0.06 seconds using one GPU as opposed to 0.59 seconds for Tacotron
	* Converges after ~500K iterations for all three datasets in our experiment, while Tacotron requires ~2M iterations
	* This significant speedup is due to the fully-convolutional architecture of Deep Voice 3, which highly exploits the parallelism of a GPU during training

# See also

# References
* Ping, Wei, et al. "Deep Voice 3: 2000-Speaker Neural Text-to-Speech." arXiv preprint arXiv:1710.07654 (2017).
