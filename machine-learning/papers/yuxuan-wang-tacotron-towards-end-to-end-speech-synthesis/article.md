---
title: "Yuxuan Wang - Tacotron: Towards End-to-End Speech Synthesis (2017)"
created: 2017-01-20
taxonomy:
  tag: [machine learning]
  status: finished
---

## Context

## Learned in this study

## Things to explore

# Overview

# Notes
* A text-to-speech synthesis system typically consists of multiple stages, such as
	* a text analysis frontend
	* an acoustic model
	* an audio synthesis module

## 1 Introduction
* It is common for statistical parametric TTS to have a text frontend extracting various linguistic features, a duration model, an acoustic feature prediction model and a complex signal-processing-based vocoder
* TTS is a large-scale inverse problem: a highly compressed source (text) is "decompressed" into audio
* Tacotron is an end-to-end generative TTS model based on the sequence-to-sequence (seq2seq) with attention paradigm
* The model takes characters as input and outputs raw spectrogram, using several techniques to improve the capability of a vanilla seq2seq model

## 2 Related Work
* WaveNet
	* Slow due to its sample-level autoregressive nature
	* Requires conditioning on linguistic features from an existing TTS frontend (thus is not end-to-end, it only replaces the vocoder and acoustic model)
* DeepVoice
	* Replaces every component in a typical TTS pipeline by a corresponding neural network
	* Each component is independently trained, and it's nontrivial to change the system to train in an end-to-end fashion
* Wang et al.
	* Earliest work touching end-to-end TTS using seq2seq with attention
	* It requires a pre-trained hidden Markov model (HMM) aligner to help the seq2seq model learn the alignment
	* A few tricks are used to get the model trained, which the authors note hurts prosody
	* It predicts vocoder parameters hence needs a vocoder
	* The model is trained on phoneme inputs and the experimental results seem to be somewhat limited
* Char2Wav
	* Predicts vocoder parameters before using a SampleRNN neural vocoder, whereas Tacotron directly predicts raw spectrogram
	* The seq2seq and SampleRNN models need to be separately pre-trained (while Tacotron's model can be trained from scratch)

## 3 Model Architecture
* The backbone of Tacotron is a seq2seq model with attention
* The model includes an encoder, an attention-based decoder, and a post-processing net
* The model takes characters as input and produces spectrogram frames, which are then converted to waveforms

## 5 Experiments
### 5.2 Mean Opinion Score Tests
* Tacotron outperforms the parametric system, but is outperformed by the concatenative system

# See also

# References
* Wang, Yuxuan, et al. "[Tacotron: Towards End-to-End Speech Synthesis.](https://arxiv.org/abs/1703.10135)" arXiv preprint arXiv:1703.10135 (2017).
