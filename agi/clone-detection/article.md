---
title: Clone detection
created: 2016-06-05
taxonomy:
  tag: [artificial-general-intelligence]
  status: in progress
  readability: 3
---

## Context

## Learned in this study

## Things to explore
* What is the purpose of studying code clones detection? Is it similar to the goal of being able to compress programs (reduce them to their smallest set of necessary functions)?
	* It allows us to build function libraries based on usage frequency
* Is it possible to construct some sort of truth table based on the properties of code clone types?

# Overview

| Type | Description | Identicalities | Differences |
|------|-------------|
| ? | Identical code | Code | None |
| ? | Identical code except for whitespace/new line | Code | Whitespace/new lines |
| ? | Identical structure, syntax and function called, different argument values | Structure, syntax, function called | Argument values |
| ? | Identical structure, syntax and argument values, different function call | Structure, syntax, argument values | Function calls |
| ? | Identical structure and syntax, different function set called and argument values | Structure, syntax | Function set called, argument values |
| ? | Different structure, partial similarity in function call order | Function call order | Structure |
| ? | Similar function set called, different order | Function set called | Function call order |
| ? | Semantically similar functions (same inputs = same output) | Semantical function| - |


| Code | Structure | Syntax | Function called | Argument values | Semantics |
|------|-----------|--------|-----------------|-----------------|-----------|
| =    | =         | =      | =               | =               | =         |

# See also

# References
* Roy, Chanchal Kumar, and James R. Cordy. "[A survey on software clone detection research.](http://research.cs.queensu.ca/TechReports/Reports/2007-541.pdf)" Queen’s School of Computing TR 541.115 (2007): 64-68.
