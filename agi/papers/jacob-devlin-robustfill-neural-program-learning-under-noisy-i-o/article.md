---
title: Jacob Devlin - RobustFill: Neural Program Learning under Noisy I/O (2017)
created: 2017-04-22
taxonomy:
  category: [Artificial General Intelligence]
  status: finished
---

## Context

## Learned in this study

## Things to explore
* What is so special about GetSpan() that it is used to solve about 20% of the test instances?

# Overview

## Notes
* 2 competing approaches for automatic program learning have received significant attention
  * Neural program synthesis, where a neural network is conditioned on input/output examples and learns to generate a program
  * Neural program induction, where a neural network generates new outputs directly using a latent program representation

## 1. Introduction
* The primary task evaluated for this work is a Programming By Example (PBE) system for string transformations similar to FlashFill
* We develop a novel variants of the attentional RNN architecture to encode a variable-length unordered set of input-output examples
* For program representation, we have developed a domain-specific language (DSL) that defines an expressive class of regular expression-based string transformations
* The neural network is then used to generate a program in the DSL (for synthesis) or an output string (for induction)

## 3. Problem Overview
* A set of input-output string examples $(I_1, O_1), \dots, (I_n, O_n)$
* A set of input strings $I_1^y, \dots, I_m^y$
* The goal is to generate the corresponding output strings $O_1^y, \dots, O_n^y$
* For each example set, we assume there exists at least one program $P$ that will correctly transform all these examples
	* $P(I_1) \rightarrow O_1, \dots, P(I_n) \rightarrow O_n, P(I_1^y) \rightarrow O_1^y, \dots, P(I_n^y) \rightarrow O_n^y$
* The success metric is whether a generated program generalizes to the corresponding assessment examples, $P(I_j^y) \rightarrow O_j^y$

### 3.2 The Domain Specific Language
* $GetSpan(r_1, i_1, y_1, r_2, i_2, y_2)$: returns the substring between the $i_1^{th}$ occurrence of regex $r_1$ and the $i_2^{th}$ ocurrence of regex $r_2$, where $y_1$ and $y_2$ denotes either the start or end of the corresponding regex matches
	* GetSpan() seems like a generalization (the encapsulation) of the composition of 2 regexes search with starting position for each regex, in other words, a much more advanced/complex form of SubStr()

### 3.3. Training Data and Test Sets
* Using the DSL, sample programs are generated and verified to ensure they are executable, do not throw exceptions, etc.
* Given these programs, a set of input strings are generated, and their associated output strings computed using the sampled program

## 4. Program Synthesis Model Architecture
* We model program synthesis as a sequence-to-sequence generation task
* The observed input-output are encoded using a series of recurrent neural networks, and generate P using another RNN one token at a time

## 5. Program Synthesis Results
### 5.1. Comparison to Past Work
* Late pooling allows us to effectively incorporate powerful attention mechanism into the model
* The previous SotA (Parisotto et al. 2017) performed pooling at the I/O encoding level and as such, it could not exploit the attention mechanisms developed here
* The DSL used here is more expressive, especially the GetSpan() function, which was required to solve approximately 20% of the test instances

## 6. Program Induction Results
### 6.1. Comparison of Induction and Synthesis Models
* It is possible to model both approaches (synthesis and induction) using nearly-identical network architectures
* The induction model evaluated is identical to synthesis Attention-A with late pooling, except for the following two modifications:
	* Instead of generating P, the system generates the new output string $O^y$ character-by-character
	* There is an additional LSTM to encode $I^y$. The decoder layer $O^y$ uses double attention on $O_j$ and $I^y$
* Induction is comparable to synthesis with a Beam = 1
* The induction model uses a beam of 3, and does not improve with a larger search because there is no way to evaluate candidates after decoding

# See also

# References
* Devlin, Jacob, et al. "[RobustFill: Neural Program Learning under Noisy I/O.](https://arxiv.org/abs/1703.07469)" arXiv preprint arXiv:1703.07469 (2017).