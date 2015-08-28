# Entropy

## Learned in this study

## Things to explore

# Overview

Entropy is an important concept to understand if one wishes to compress a function (data) as closely as possible to the theoretical limit.

If your goal is to get as much compression as possible and you are okay with losing information, then lossy compression will allow you to go past what lossless compression would give you.

![](assets/images/Binary_entropy_plot.svg)

$$
\Eta(X) = -\sum_{i} {\mathrm{P}(x_i) \log_b \mathrm{P}(x_i)}
$$


## Questions

* What happens as the volume of binary information grows?
* Is it always possible to compress binary data past a certain amount of data? Even if this data is at its peak entropy?

## Sources

1. https://en.wikipedia.org/wiki/Entropy_(information_theory)