---
title: Tools I use daily and can contribute to
created: 2020-01-30
taxonomy:
  type: post
  category: [Questions]
  status: finished
---

# Question
What are the tools I use daily that I could contribute to?

# Answer
## General
* [Visual Studio Code](https://github.com/microsoft/vscode) My text editor of choice when I don't need an IDE. I've implemented a few plugins for VSC and use it daily to write personal notes as well as blog articles. I sometimes make use of its diff tool to merge changes from Sourcetree.
* [Pycharm](https://github.com/JetBrains/intellij-community) My IDE of choice when I write python. Very powerful, easy to get used to if you've used other Jetbrains IDE (I've used PHPStorm for more than 5 years). Extremely useful to run a specific unit test using pytest or to debug a complex issue by putting breakpoints and investigating the internal state of the program.
* [Docker](https://github.com/moby/moby) I use docker at work to containerize all of our dependencies so that it is somewhat easy to deploy what we develop in "any" environment, that is, an environment where docker (or similar, such as Kubernetes) is installed.
* [Drone CI](https://github.com/drone/drone) We use Drone CI at work to do continuous integration and I consider this tool to be an essential part of my daily work. When people push code to github and it fails on Drone CI, I can use this information to help them fix their issues. We also use it has part of our PR process to ensure that the PR passes all the expected tests so that we do not introduce faulty code into our master branch.
* [Dependabot](https://github.com/dependabot/dependabot-core) A few months ago I had introduced dependabot into my dependency management practices. It was highly useful to get automated PRs with updates to libraries we depended on. However, since the release of poetry 1.0.0, dependabot has not been able to update my python dependencies and has been left unused. I've created a [PR](https://github.com/dependabot/dependabot-core/pull/1621) which I hope will move this issue forward and get dependabot working again with poetry.
* [Plotly](https://github.com/plotly/plotly.js) I used to use the highcharts plotting library until someone at work introduced me to plotly. Plotly.js is open source software and released under the MIT license, which makes it an ideal library to use in personal as well as commercial software.

## Python specific
* [Pandas](https://github.com/pandas-dev/pandas) I do machine learning development for a living nowadays and I depend highly on pandas. I don't think there's a single work day that goes by in which I don't whip out at least one `pd.DataFrame`.
* [Scikit-learn](https://github.com/scikit-learn/scikit-learn) Similar to my dependency on pandas, my dependency on Scikit-learn is on a daily basis. Unlike the [DummyRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyRegressor.html) documentation suggests, I use it for real problems and it's definitely useful!
* [Dask](https://github.com/dask/dask) / [Distributed](https://github.com/dask/distributed) In order to scale both horizontally and vertically machine learning problems I've leaned on dask and distributed. Their use of [delayed](https://docs.dask.org/en/latest/delayed.html) and [Futures]()
* [pytest](https://github.com/pytest-dev/pytest)
* [mypy](https://github.com/python/mypy)
* [isort](https://github.com/timothycrosley/isort)
* [black](https://github.com/psf/black)
* [prospector])(https://github.com/PyCQA/prospector)
* [poetry](https://github.com/python-poetry/poetry)
