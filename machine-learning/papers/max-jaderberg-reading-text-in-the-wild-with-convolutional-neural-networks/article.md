---
title: Max Jaderberg - Reading Text in the Wild with Convolutional Neural Networks (2014)
created: 2017-07-02
taxonomy:
  category: [Machine learning]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview

# Notes
## 2 Overview of the Approach
* The stages of the approach:
	* Word bounding box proposal generation
	* Proposal filtering and adjustments
	* Text recognition
	* Final merging
* The detection stage is based on weak-but-fast detection methods to generate word bounding box proposals
* This draws on the success of the R-CNN object detection framework where region proposals are mapped to a fixed size for CNN recognition
* The use of region proposals avoids the computational complexity of evaluating an expensive classifier with exhaustive multi-scale, multi-aspect-ratio sliding window search
* A combination of Edge Box proposals and a trained aggregate channel features detector is used to generate candidate word bounding boxes
* Due to the large number of false-positive proposals, a random forest classifier is used to filter the number of proposals to a manageable size
* Inspired by the success of bounding box regression in DPM and R-CNN, more accurate bounding boxes are regressed from the seeds of the proposal algorithms which greatly improves the average overlap ratio of positive detections with ground truth
* A text recognition result is produced for each proposal generated from the detection stage
* A whole-word approach is taken to recognition, providing the entire cropped region of the word as input to a deep convolutional neural network
* A dictionary model is used in order to classify against 90k possible words
* The models are trained purely from synthetic data
* Multiple rounds of non-maximal suppression and bounding box regression are applied to update the detection results

## 4 Proposal Generation
* Two detection mechanisms are combined
	* Edge Boxes region proposal algorithm
	* A weak aggregate channel feature detector

### 4.1 Edge Boxes
* The key intuition behind Edge Boxes is that since objects are generally self contained, the number of contours wholly enclosed by a bounding box is indicative of the likelihood of the box containing an object
* Edges tends to correspond to object boundaries, and so if edges are contained inside a bounding box this implies objects are contained within the bounding box, whereas edge which cross the border of the bounding box suggest there is an object that is not wholly contained by the bounding box
* Compute the edge response map using the Structured Edge detector and perform Non-Maximal Suppression orthogonal to the edge responses, sparsifying the edge map
* A candidate bounding box $b$ is assigned a score $s_b$ based on the number of edges wholly contained by $b$, normalized by the perimeter of $b$
* The boxes $b$ are evaluated in a sliding window manner, over multiple scales and aspect ratios, and given a score $s_b$
* The boxes are sorted by score and non-maximal suppression is performed: a box is removed if its overlap with another box of higher score is more than a threshold

# See also

# References
* Jaderberg, Max, et al. "Reading text in the wild with convolutional neural networks." arXiv preprint arXiv:1412.1842 (2014).
