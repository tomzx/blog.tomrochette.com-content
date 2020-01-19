---
title: Learning, according to machine learning
created: 2020-01-18
taxonomy:
  type: post
  category: [Questions, Machine Learning]
  status: finished
---

# Question
What is learning according to machine learning?

# Answer
It is (for supervised learning) looking at numerous samples, decomposing them into input variables and their associated target variables, and deriving according to an algorithm how to predict the target variables given input variables.

It is (potentially lossy) compression the observed samples, where the learning algorithm describe the compression/decompression algorithm.

It is the creation of some "memory" of the observed samples. Whereas an untrained model has no memory of the dataset, since it hasn't seen the data, a trained model has some form of memory. A simple model such as
