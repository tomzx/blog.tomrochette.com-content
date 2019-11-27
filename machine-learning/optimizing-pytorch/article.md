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
* Use cases
	* Code is not using 100% of the CPU/RAM
		* Increase batch size
		* Parallelize data loading with GPU computation
	* Data does not fit in GPU RAM
		* Reduce batch size
	* GPU usage is 100% yet there is no progress
		* This might be due to using multithreading and having GPU trashing occurring

# Notes
* Run your script with python's profiler to determine which part of your script is CPU expensive
```
python -m cProfile -o my_profile.prof train.py
```
* Free up the memory you used with `del` (e.g., `del my_tensors`)

# See also

# References
* https://sagivtech.com/2017/09/19/optimizing-pytorch-training-code/
