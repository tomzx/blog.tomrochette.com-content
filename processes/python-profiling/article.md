---
title: Python profiling
created: 2019-12-20
taxonomy:
  type: post
  category: [Programming, Python, Processes]
  status: draft
---

Run your program with `python -m cProfile -o profile.cprofile my-script.py`

Install `snakeviz` (`pip install snakeviz`) to visualize the generated profile.

`snakeviz profile.cprofile `

Alternative approach

Install `pyprof2calltree` to convert the cprofile to a kcachegrind compatible profile.

`pyprof2calltree -i profile.cprofile -o callgrind.profile.cprofile`

# References
* https://benbernardblog.com/tracking-down-a-freaky-python-memory-leak/
* https://tech.buzzfeed.com/finding-and-fixing-memory-leaks-in-python-413ce4266e7d
* https://varblog.org/blog/2018/05/24/profiling-and-optimizing-machine-learning-model-training-with-pytorch/
