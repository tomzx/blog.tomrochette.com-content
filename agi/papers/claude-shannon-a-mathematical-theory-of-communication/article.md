---
title: Claude Shannon - A Mathematical Theory of Communication (1948)
created: 2015-08-13
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

*A Mathematical Theory of Communication* is a critical piece of knowledge for anyone interested in the topic of information.

## Learned in this study

## Things to explore

# Overview

Capacity is defined as

$$
C = \lim_{T\to\infty} \frac{\log N(T)}{T}
$$

We want the capacity of a discrete channel to be as high as possible (highest throughput possible).
At the same time, we want the message that are transmitted to be as small as possible.

Binary entropy function

$$
H = -(p \log p + q \log q)
$$

![](images/Binary_entropy_plot.svg)

## 8 Representation of the encoding and decoding operations
* A transducer can be described by two functions:
$$
y_n = f(x_n, \alpha_n)
$$
$$
\alpha_{n+1} = g(x_n, \alpha_n)
$$
where
* $x_n$ is the $n^{th}$ input symbol
* $\alpha_n$ is the state of the transducer when the $n^{th}$ input symbol is introduced
* $y_n$ is the output symbol (or sequence of output symbols) produced when $x_n$ is introduced if the state is $\alpha_n$

# See also

# References
* Shannon, Claude E. (October 1948). "A Mathematical Theory of Communication". Bell System Technical Journal 27 (4): 623–656. doi:[10.1002/j.1538-7305.1948.tb00917.x](https://dx.doi.org/10.1002%2Fj.1538-7305.1948.tb00917.x).
* https://en.wikipedia.org/wiki/Binary_entropy_function

