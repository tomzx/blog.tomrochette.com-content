---
title: List outdated packages using poetry
created: 2020-03-04
taxonomy:
  type: post
  category: [Problems]
  status: finished
---

# Problem
I use poetry as my python package manager and I'd like to know the packages that I depend on that are currently outdated.

# Solution
An easy way to get this list is to run `poetry show --outdated`. This will return you a list of all the packages that are outdated, their current version, the latest version, as well as a description of the package.

There are in my opinion three missing features here:
* having the command respect the semantic versioning constraint and only letting you see the latest version according to those constraints
* having a flag to switch between showing the latest version available without semantic versioning constraint vs the latest version constrained by semantic versioning
* having a flag to list only the packages that are direct dependencies (listed in the `pyproject.toml` file)

# References
* [Poetry show command](https://python-poetry.org/docs/cli/#show)
