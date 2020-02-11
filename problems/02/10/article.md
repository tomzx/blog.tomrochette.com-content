---
title: AST in python
created: 2020-02-10
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

A simple example is as follow. It will read a file defined in the `file` variable, use `ast` to parse it, returning a `tree` that can then be traversed using the [visitor pattern](https://refactoring.guru/design-patterns/visitor). Defining visitors lets you separate the responsibility of each of them, making the code that analyzes code easier to understand.

```python
import ast

class ClassVisitor(ast.NodeVisitor):
	def visit_ClassDef(self, node):
		# Do some logic specific to classes
		self.generic_visit(node)

class FunctionVisitor(ast.NodeVisitor):
	def visit_FunctionDef(self, node):
		# Do some logic specific to functions
		self.generic_visit(node)

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
