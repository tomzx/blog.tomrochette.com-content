---
title: Identifying python files with no coverage
created: 2020-02-27
taxonomy:
  type: post
  category: [Problems, Python]
  status: finished
---

# Problem
I use pytest with coverage and I want to see the files that have no coverage.

# Solution
~~By default pytest and pytest-cov will not list the files which are not imported during tests. This means that if no tests were written for a part of your code, then you will not see the file listed under the list generated when you run `pytest your-folder --cov=your-folder --cov-report term-missing`.~~

If you are using PyCharm Professional, you can simply run your test with coverage. This will allow you to identify all the files that have currently no coverage as they will appear with coverage = 0%.

As of now I have not found a way to obtain this information from the CLI, but I think it would definitely be useful to have all the files listed as source files, even if they are not even loaded during the testing process. This would allow developers to identify weaknesses in their code, specifically code that is 100% untested.

# References
* https://www.jetbrains.com/help/pycharm/running-test-with-coverage.html
