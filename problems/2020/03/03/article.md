---
title: Mypy and implicit namespaces
created: 2020-03-03
taxonomy:
  type: post
  tag: [Problems, Python]
  status: finished
---

# Problem
I use mypy but it doesn't seem to scan all my files. Why?

# Solution
You might be using implicit namespaces in your code (see [PEP 420](https://www.python.org/dev/peps/pep-0420/)). Support for implicit namespaces in `mypy` is rather flaky as of 2020-03-03.

One solution for the moment is to add `__init__.py` and make all your namespaces explicit.

Another solution is to replace your calls to `mypy some-path` with `mypy $(find some-path -name "*.py")`.
