---
title: "Théodore Bluche - Scan, Attend and Read: End-to-End Handwritten Paragraph Recognition with MDLSTM Attention (2016)"
created: 2017-05-19
taxonomy:
  tag: [machine-learning]
  status: finished
  readability: 3
---

## Context

## Learned in this study

## Things to explore
* I'm not sure why the decoder would have to support a full paragraph of decoding (which requires a lot of memory). It seems it would make more sense to have the attention network take care of pointing out where to read next, then have decoding of the observed section and then maybe later on a translation state from the "incorrect" detection into the corrected ground truth
* How is training/prediction done? Do we feed it the whole image and it returns a single character prediction?
	* Yes, the image is fed the number of times there are characters in it
* Is the network actually split in two, that is, the encoder step, which is computed once per image, and the attention + state + decoder which is computed as many time as necessary to recover each character in the image?
* How are the images fed to the network? Grayscale or RGB? Based on the IAM handwriting DB used for training, that would be grayscale.

# Overview

# Analysis of the network architecture
## Encoder
* The input is fed to 4 MDLSTM layers, where each layer is a given a scanning direction (L: left, R: right, b: bottom, t: top)(LR-TB, TB-RL, RL-BT, BT-LR)
* Each of these layer is linked to a separate convolutional layer
* All the convolutional layers are then merged into a single sum layer
* The sum layer then goes through the same process a second time (4 MDLSTM, 1-1 MDLSTM-Convolution, sum layer)
* A third layer of 4 MDLSTM layers
* For each layer of the MDLSTM layer, a separate linear/dense layer is applied
* As for the previous groups of layers (MDLSTM-Convolution-Sum), a sum is applied to the linear/dense layer

## Attention
* The input is fed to 4 MDLSTM layers, where each layer is a given a scanning direction (L: left, R: right, b: bottom, t: top)(LR-TB, TB-RL, RL-BT, BT-LR)
* For each layer of the MDLSTM layer, a separate linear/dense layer is applied
* The attention is then applied to the output of the encoder in order to "mask" important/non-important features

## State


## Decoder
* A dense layer is applied to do the final classification (predict the next character)

## Overall comments
* As a first impression, it seems that the input to the network likely will have to be a fixed size, which might be an issue if we're trying to deal with images of varying size while keeping the same overall scanning strategy
* That is also likely to mean that a certain "range" of line distance will be expected based on the training data, which might cause issues in documents where text is sparse
* The attention + state sections are dedicated to figuring out where we should be looking at next. It basically takes care of moving the "detection" pointer on the page

# Notes
## Experiments
### 5.4 Toward Paragraph Recognition
* Backpropagation through time of the decoder was truncated to 30 timesteps in order to address the memory issue
* Uses curriculum learning during training by increasing the length of sequences sampled (single lines to paragraphs)

## 6 Discussion
* The time and memory consumption is prohibitive for most industrial applications

# See also

# References
* Bluche, Théodore, Jérôme Louradour, and Ronaldo Messina. "Scan, attend and read: End-to-end handwritten paragraph recognition with mdlstm attention." arXiv preprint arXiv:1604.03286 (2016).
* http://www.tbluche.com/scan_attend_read.html
