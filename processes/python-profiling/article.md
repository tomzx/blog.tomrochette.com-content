---
title: Python profiling
created: 2019-12-20
taxonomy:
  type: post
  category: [Programming, Python, Processes]
  status: draft
---

Run your program with `python -m cProfile -o profile my-script.py`

Install `pyprof2calltree` to convert the cprofile to a kcachegrind compatible profile.
