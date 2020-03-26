---
title: Slow click CLI
created: 2020-02-29
taxonomy:
  type: post
  category: [Problems, Python]
  status: finished
---

# Problem
My [click CLI](https://click.palletsprojects.com/) is slow, even just to show the help. How do I make it go faster?

# Solution
In most cases, the reason your click CLI is slow is that you have large imports at the top of the files where you have declared your commands.

The typical pattern is as follows:

train.py
```python
import click

@click.command()
def train():
	pass
```


predict.py
```python
import click
import

@click.command()
def predict():
	pass
```
