---
title: Automated programming
created: 2016-06-04
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore
* How to avoid these synthesizer from building a simple lookup table?

# Overview

* The programmer provides pre-conditions and post-conditions
* The programmer provides input parameters and output with types
* The programmer provides a set of examples (inputs and outputs) for the automatic function synthesis to work through
* Define types in/out 
* Give examples (may not be straightforward for objects)
* Use some sort of natural language/declarative language to control oriented language (use of conditionals)
* Provide examples in order of complexity
* The synthesizer is basically trying to build a proof for your examples, so it has to know the operation it can do and their impact on the state (see SHAKEY)
* Many approaches are possible, namely forward search, backward search, bidirectional search
* As there are many way to accomplish the same function, the first goal of the synthesizer should be to rapidly offer a working function to the user
* Once said function had been discovered, three synthesizer may work with the user in order to improve the current solution
	* *What are some of the improvement that can be expected to be made?*


# Feature planning
* Assert what the system already does (expectations)
* Specify the feature, what does it do that the system currently does not
(Scope of the change)
* Determine what exist
* Determine what is missing and will need to be added (creative part)
* Determine which functions will be required 
* Determine which data will be required
* Determine where the data is in the required state (precondition) (points of insertion)
* Create the necessary functions to obtain data that cannot currently be obtained
* Construct a collection of sequences of function calls that will accomplish the required feature

# See also

# Sources
