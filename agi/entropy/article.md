---
title: Entropy
created: 2015-08-27
taxonomy:
  tag: [artificial-general-intelligence]
  status: in progress
  readability: 3
---

## Learned in this study
* Information is not the same as data. The same information can be expressed (coded) using more or less data

## Things to explore

# Overview
Entropy is an important concept to understand if one wishes to compress a function (data) as closely as possible to the theoretical limit.

If your goal is to get as much compression as possible and you are okay with losing information, then lossy compression will allow you to go past what lossless compression would give you.

![](images/Binary_entropy_plot.svg)

$$
Η(X) = -\sum_{i} {\mathrm{P}(x_i) \log_b \mathrm{P}(x_i)}
$$


## Questions
* What happens as the volume of binary information grows?
* Is it always possible to compress binary data past a certain amount of data? Even if this data is at its peak entropy?

## References

1. https://en.wikipedia.org/wiki/Entropy_(information_theory)
