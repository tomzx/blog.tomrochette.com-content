---
title: Alan W. Biermann - Approaches to Automatic Programming
created: 2016-01-01
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview

# Notes
## 2 Extensions to Traditional Automatic Programming Methods
* The same patterns seem to appear again and aagin in the code (of traditional compiled languages)
* The development of higher level languages has largely been involved with discovering these patterns and designing constructs that implement them automatically
* Three kinds of patterns and languages that save the user from having to code them by hand:
	* DO-loops (or FOR-loops)
	* searching with automatic backtracking
	* the representation and handling of certain mathematical entities such as sets and relations in some higher level languages

## 2.2 Higher Level Languages
* Efficient compilation of code can be extremely difficult because the constructs of the language differ so greatly from the hardware capabilities of the machine
* For example, sets can be represented as linear linked lists, binary trees, bit strings, hash tables, fixed length arrays, and others, and the choice of data structure greatly affects the efficiency of the program
* Ordinarily these decisions concerning representation would be made by the programmer, who knows the nature of his data and how they should be ordered and accessed
* The higher level language compiler must either make arbitrary decisions at the risk of terrible performance or gather information about the usage of each data structure and attempt to make optimum decisions
* Low has written a compiler for a subset of SAIL that also makes use of statement execution counts obtained by running the program
* Higher level languages take the user one step farther away from the machine, enabling him to write programs more quickly, more concisely and more reliably
* Higher level languages will probably be successful to the extent that they embody the structure and processing that fit the user's problems and the user's concept of his problems
* These languages usually are considerably less computationally efficient than more traditional languages because their processors are not able to utilize completely special domain-dependent information in the way that a human coder could

## 2.3 Special Purpose Program Generator

# See also

# Sources
* [doi:10.1016/S0065-2458(08)60519-7](http://www.sciencedirect.com/science/article/pii/S0065245808605197)