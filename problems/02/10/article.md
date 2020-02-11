---
title: AST in python
created: 2020-02-09
taxonomy:
  type: post
  category: [Problems, Software development, Python]
  status: finished
---

# Problem
I want to analyze a python script to extract something from it. How do I do that?

# Solution
Python has an [abstract syntax tree](https://en.wikipedia.org/wiki/Abstract_syntax_tree) like most programming language.

You can use the [ast module](https://docs.python.org/3/library/ast.html) to parse a string that contains the code you want to analyze.

```python
import ast

class ClassVisitor():
	pass

class FunctionVisitor():
	pass

visitors = [
	ClassVisitor(),
	FunctionVisitor()
]

with open(file, "r") as f:
	code = f.read()

	tree = ast.parse(code)

	for visitor in visitors:
		visitor.visit(tree)
```

# Reference
* https://greentreesnakes.readthedocs.io/en/latest/index.html
