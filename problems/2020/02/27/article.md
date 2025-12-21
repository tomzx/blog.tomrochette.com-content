---
title: Identifying python files with no coverage
created: 2020-02-27
taxonomy:
  type: post
  tag: [problems, python]
  status: finished
  readability: 3
---

# Problem
I use pytest with coverage and I want to see the files that have no coverage.

# Solution
It appears that pytest and pytest-cov will not list someof the files that are under namespace packages, while it will work fine for files in regular packages (see [PEP 420](https://www.python.org/dev/peps/pep-0420/) on the topic of implicit namespace packages).

To fix this problem, one solution is to add `__init__.py` files in all of your directories in order to create regular packages.

If you are using PyCharm Professional, you can simply run your test with coverage. This will allow you to identify all the files that have currently no coverage as they will appear with coverage = 0%.

# References
* https://www.jetbrains.com/help/pycharm/running-test-with-coverage.html
