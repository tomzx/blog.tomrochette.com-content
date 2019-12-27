---
title: Separability metric
created: 2019-09-29
taxonomy:
  category: [Machine Learning]
  status: in progress
---


## Context
Given a tabular dataset, what is the theoretical limit

## Learned in this study

## Things to explore

# Overview
Number of unique input X/Number of points/rows
Given a tabular dataset, compute the separability metric as follow:
* 1 point: 100% separable
* 2 points: given the target feature to predict, if the other attributes can separate two distinct targets, then 100%, if not, 50%
* x points: if the target is different for all points, yet the attributes are all the same, we should expect the metric to be 1/x
* x points with y, z similar targets: in the case that we have x points with similar attributes, but for which there are y and z similar targets (two groups with the same target), we can at best hope for ...
For a dataset with 1 B and 3 C as output values, we expect the metric to be between 0.25 and 0.75 (1/4 and 3/4)
* sum(count(points for target x with attributes X)/count(points with attributes X))/count(points)
* It may make sense to have a separability metric per target output (when those are categorical)
* In the case of numerical targets, minimizing for distance between all the targets (clustering) would turn the problem into the categorical form


# See also

# References
