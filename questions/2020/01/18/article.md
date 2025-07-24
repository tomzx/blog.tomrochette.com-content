---
title: Learning according to machine learning
created: 2020-01-18
taxonomy:
  type: post
  tag: [questions, machine learning]
  status: finished
---

# Question
What is learning according to machine learning?

# Answer
It is (for supervised learning) looking at numerous samples, decomposing them into input variables and their associated target variable, and deriving according to an algorithm how to predict the target variable given input variables.

It is the (potentially lossy) compression of the observed samples, where the learning algorithm describes the compression/decompression algorithm. The compressed data is the information necessary for the algorithm to make predictions (decompression).

It is the creation of some "memory" of the observed samples. Whereas an untrained model has no memory of the dataset since it hasn't seen the data, a trained model has some form of memory. A simple model such as sklearn's [DummyRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyRegressor.html) will learn and memorize the mean of the target variable. It may not have learned and memorized much, but it has built its internal model of the data.

It is to imitate as closely as possible the source of data it is trained on. This means that given input variables, it should produce target values that are as close as possible to those observed during training (learning).

# References
* [Learning](../../../../agi/learning/article.md)
