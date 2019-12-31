---
title: Python profiling
created: 2019-12-20
taxonomy:
  type: post
  category: [Programming, Python, Processes]
  status: draft
---

Run your program with `python -m profile.cprofile -o profile my-script.py`

Install `pyprof2calltree` to convert the cprofile to a kcachegrind compatible profile.

`pyprof2calltree -i profile.cprofile -o callgrind.profile.cprofile`

# References
* https://tech.buzzfeed.com/finding-and-fixing-memory-leaks-in-python-413ce4266e7d
