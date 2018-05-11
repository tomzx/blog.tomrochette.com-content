---
title: AGI black box
created: 2018-05-10
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context
The ultimate goal of a simple AGI program is to be able to receive a set of inputs and to produce the desired output while having as little input from the user.

## Learned in this study

## Things to explore

# Overview

# Supported problems
* X to C (constant) mapping
	* (a, b, c, ..., z) -> alphabet
	* (0, 1, 2, ..., 1000) -> number
* X to X mapping (identity)
	* a -> a, b -> b, c - c, ..., z -> z
	* 0 -> 0, 1 -> 1, 2 -> 2, ..., 1000 -> 1000
* X to Y mapping
	* 0 -> a, 1 -> b, 2 -> c, ..., 26 -> z
	* a -> 0, b -> 1, c -> 2, ..., z -> 26
* Delayed X to Y mapping (the Y value should be produced with a delay t in the output sequence)
	* a -> ., b -> ., c -> a, d -> b, e -> c, ..., z -> x
* X to Y mapping where the mapping changes over time
	* 0 -> 5, 10 -> 25, 0 -> 10, 10 -> 30, 0 -> 12, 10 -> 23

# Requirements
* The user must define inputs and outputs that are to be learned in order to reduce the problems' space
* In some cases, the black box agent should be able to generate optimal solutions given constraints

# See also

# References
