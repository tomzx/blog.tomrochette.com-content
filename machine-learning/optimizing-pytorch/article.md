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
* Multi-GPU usage
* Training multiple models on a single GPU in multiple processes

# Overview
* Use cases
	* Code is not using 100% of the CPU/RAM
		* Increase batch size
		* Parallelize data loading with GPU computation
	* Data does not fit in GPU RAM
		* Reduce batch size
	* GPU usage is 100% yet there is no progress
		* This might be due to using multithreading and having CPU/GPU trashing occurring
			* In my experiment I've seen 100% GPU usage, not completely sure about CPU usage

# Notes
* Run your script with python's profiler to determine which part of your script is CPU expensive
```
python -m cProfile -o my_profile.prof train.py
```
* Free up the memory you used with `del` (e.g., `del my_tensors`)
* If running PyTorch in multiple processes, make sure to configure `OMP_NUM_THREADS` to a low number as PyTorch uses multithreaded BLAS to do linear algebra on CPU. If this is not specified, the processes will likely attempt to use all cores, which will cause issues since each process will be effectively trying to use all the cores as well

# See also

# References
* https://sagivtech.com/2017/09/19/optimizing-pytorch-training-code/
* https://github.com/Kaixhin/grokking-pytorch
* https://pytorch.org/docs/stable/notes/multiprocessing.html
* https://www.dangdatascience.com/articles/writing-fast-pytorch/
