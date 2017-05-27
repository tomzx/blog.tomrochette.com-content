---
title: Alex Graves - Offline Handwriting Recognition with Multidimensional Recurrent Neural Networks (2009)
created: 2017-04-27
taxonomy:
  category: [Artificial General Intelligence]
  status: finished
---

## Context

## Learned in this study

## Things to explore

# Overview

# Notes
## 1 Introduction
* Goal: Build an offline recognition system that would work on raw pixels
* The online case was solved using LSTM and CTC
* A Naive approach would be to present the images to the network one vertical line at a time, thereby transforming them into 1D sequences
	* Such as system would be unable to handle distortions along the vertical axis
* A more flexible solution is offered by multidimensional recurrent neural networks (MDRNNs)
	* A special case of directed acyclic graph networks
	* Generalize standard RNNs by providing recurrent connections along all spatio-temporal dimensions present in the data
	* These connections make MDRNNs robust to local distortions along any combination of input dimensions (e.g. image rotations and shears, which mix vertical and horizontal displacements) and allow them to model multidimensional context in a flexible way
* How to transform two dimensional images into one dimensional label sequences?
	* The solution is to pass the data through a hierarchy of MDRNN layers, with blocks of actions gathered together after each level
	* The height of the blocks are chosen to incrementally collapse the 2D images onto 1D sequences, which can then be labelled by the output layer

## 2 Method
### 2.1 Multidimensional Recurrent Neural Networks
* The basic idea of multidimensional recurrent neural networks (MDRNNs) is to replace the single recurrent connection found in standard recurrent networks with as many connections as there are spatio-temporal dimensions in the data

### 2.2 Connectionist Temporal Classification
* Connectionist Temporal Classification (CTC) is an output layer designed for sequence labelling with RNNs
* It does not require pre-segmeneted training data, or postprocessing to transform its outputs into transcriptions
* It trains the network to directly estimate the conditional probabilities of the possible labellings given the input sequences

### 2.3 Network Hierarchy
* We created a hierarchical structure by repeatedly composing MDLSTM layers with feedforward layers
* The basic procedure is as follows:
	* The image is divided into small pixels blocks, each of which is presented as a single input to the first set of MDLSTM layers (e.g. a 4x3 block is reduced to a length 12 vector)
		* If the image does not divide exactly into blocks, it is padded with zeroes
	* The four MDLSTM layers scan through the pixel blocks in all directions
	* The activations of the MDLSTM layers are collected into blocks
	* These blocks are given as input to a feedforward layer
* The purpose of the blocks is twofold:
	* Collect local contextual information
	* Reduce the area of the activation arrays
* For most tasks we find that a hierarchy of three MDLSTM/feedforward stages gives the best results
* We use the standard "inverted pyramid" structure, with small layers at the bottom and large layers at the top
* In general we cannot assume that the input images are of fixed size. Therefore it is difficult to choose block heights that ensure that the final activation array will always be one dimensional, as required by CTC. A simple solution is to collapse the final array by summing over all the inputs in each vertical line, i.e. the input at time t to CTC unit k

# See also

# References
* Graves, Alex, and Jürgen Schmidhuber. "Offline handwriting recognition with multidimensional recurrent neural networks." Advances in neural information processing systems. 2009.