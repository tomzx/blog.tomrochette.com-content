---
title: Thomas Fahringer - Advanced Symbolic Analysis for Compilers (2003)
created: 2016-10-27
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore
* Is static analysis memory consumption a good representation of how much resources is required by a programmer to understand a piece of code?

# Overview

# Notes
## 1. Preface
* The objective of program analysis is to automatically determine the properties of a program
* Advanced program analysis can:
	* help to find program errors
	* detect and tune performance-critical code regions
	* ensure assumed constraints on data are not violated
	* tailor a generic program to suit a specific application
	* reverse-engineer software modules
	* etc.
* Many symbolic analyses are based on abstract interpretation and an abstraction of program input data
* The program context:
	* variables values
	* assumptions about and constraints between variable values
	* conditions under which control flow reaches a program statement

## 2. Introduction
```
read(A, B)
A := A + B
B := A - B
A := A - B
```

* Instead of computing numbers for variable A and B we assign them symbolic values. Let us assume that variable A and B are undefined. We denote this undefined variable binding of A and B as follows
	* $A = \bot$
	* $B = \bot$
* As A and B are assigned, we assign them a symbolic value where $\triangledown_1$ and $\triangledown_2$ denote the input values of the read statement
	* $A = \triangledown_1$
	* $B = \triangledown_2$
* We propagate symbolic value of A and B
	* $A = \triangledown_1 + \triangledown_2$
	* $B = \triangledown_2$

# See also

# Sources
* Fahringer, Thomas, and Bernhard Scholz. Advanced symbolic analysis for compilers: new techniques and algorithms for symbolic program analysis and optimization. Vol. 2628. Springer, 2003.
