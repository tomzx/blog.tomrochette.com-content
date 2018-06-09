---
title: Study - Program analysis
created: 2016-06-16
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview
* Look at interesting classes

* Start by finding the entry points
	* In PHP, those are generally files that execute code (at the root level)
		* Some cases to ignore:
			* If(function_exist(*))

* Assuming we're in a class file
	* Scan the code from top to bottom
	* Record constructor dependencies
	* Record all calls to external dependencies (this is the interface between the two classes)
	* Record parameters of methods, those are dependencies between the classes

# When analyzing a method, what happens mentally
* Read method name
* Read and record method parameters type and variables identifier
* Read the code from top to bottom
* Simulate code execution mentally, creating and assigning things as they are in the code
* Generate dependencies as required, instantiating as little information as possible

## Things that this lets us do
* Create minimalist interfaces describing the objects we're working with by recording the methods called on them as well as the arguments given during those calls

## Types of things we need to be able to do
* Create a path from entry to exit of a functions/methods
	* We assume that all called functions/methods will return
* Create a mock
* While traversing the path,

# Initiation to a new code base
* Use of prior knowledge/experience to infer functionality
	* For instance, look at framework libraries to construct a dictionary of components
* Generate a components dictionary based on file names, functions names, classes names, namespaces names, etc.
* Scan folders to get a sense of the structure
* Find entry point and build a list of available values/objects at a given point in execution time/the code
* Infer code style from current code
* Determine service boundaries (where code may not be freely changed for to external dependents)

# See also

# References
