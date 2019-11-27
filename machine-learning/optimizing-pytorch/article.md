---
title: Optimizing PyTorch
created: 2019-11-26
taxonomy:
  category: [Machine Learning]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview

# Notes
* Run your script with python's profiler to determine which part of your script is CPU expensive
```
python -m cProfile -o my_profile.prof train.py
```
* Free up the memory you used with `del` (e.g., `del my_tensors`)

# See also

# References
* https://sagivtech.com/2017/09/19/optimizing-pytorch-training-code/
