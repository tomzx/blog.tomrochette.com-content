---
title: Burr Settles - A Trainable Spaced Repetition Model for Language Learning (2016)
created: 2018-02-01
taxonomy:
  tag: [machine learning]
  status: finished
---

## Context

## Learned in this study

## Things to explore

# Notes
## 1 Introduction
* The spacing effect is the observation that people tend to remember things more effectively if they use spaced repetition practice (short study periods spread out over time) as opposed to massed practice (i.e., "cramming")
* The lag effect is the related observation that people learn even better if the spacing between practices gradually increases

## 2 Duolingo
### 2.2 Spaced Repetition and Practice
* Once a lesson is completed, all the target words being taught in the lesson are added to the student model. This model captures what the student has learned, and estimates how well she can recall this knowledge at any given time

## 3 Spaced Repetition Models
### 3.1 The Pimsleur Method
* Graduated-interval recall, whereby new vocabulary is introduced and then tested at exponentially increasing intervals, interspersed with the introduction or review of other vocabulary
* This approach is limited since the schedule is pre-recorded and cannot adapt to the learner's actual ability

### 3.2 The Leitner System
* The main idea is to have a few boxes that correspond to different practice intervals: 1-day, 2-day, 4-day, and so on
* All cards start out in the 1-day box, and if the student can remember an item after one day, it gets "promoted" to the 2-day box. Conversely, if she is incorrect, the card gets "demoted" to a shorter interval box

### 3.3 Half-Life Regression: A New Approach
* Ebbinghaus model, also known as the forgetting curve
	* Memory decays exponentially over time
$$
p = 2^{-\delta/h}
$$
* $p$ is the probability of correctly recalling an item (e.g., a word)
* $\delta$ is the lag time since the item was last practiced
* $h$ is the half-life or measure of strength in the learner's long term memory
$$
\hat{h}_\Theta = 2^{\Theta \text{x}}
$$
* $\text{x}$ denotes a feature vector that summarizes a student's previous exposure to a particular word
* $\Theta$ contains weights that correspond to each feature variable in $\text{x}$
* We want to fit $\Theta$ empirically to learning trace data, and accommodate an arbitrarily large set of interesting features

# See also

# References
* Settles, Burr, and Brendan Meeder. "A trainable spaced repetition model for language learning." Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers). Vol. 1. 2016.
