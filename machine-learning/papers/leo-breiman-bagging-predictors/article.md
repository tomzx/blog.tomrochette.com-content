---
title: Leo Breiman - Bagging Predictors (1996)
created: 2017-12-09
taxonomy:
  tag: [Machine learning]
  status: finished
---

## Context

## Learned in this study

## Things to explore

# Overview
* Given a training set $D$ of size $n$, bagging generates $m$ new training sets $D_i$, each of size $n'$, by sampling from $D$ uniformly and with replacement (the same sample may be present multiple times)
* The $m$ models are fitted using the $m$ bootstrap samples and combined by averaging the output (for regression) or voting (for classification)

# Notes
* Bagging (bootstrap aggregating) can push a good but unstable procedure a significant step towards optimality
* On the other hand, it can slightly degrade the performance of stable procedures

# See also

# References
* Breiman, Leo. "Bagging predictors." Machine learning 24.2 (1996): 123-140.
* https://en.wikipedia.org/wiki/Bootstrap_aggregating
