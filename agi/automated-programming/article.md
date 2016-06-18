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
* How to avoid the synthesizer from building a simple lookup table?
* What makes it that some functions are just simpler to write than to provide examples for (or require many more examples than it would take to just implement it)? For instance, a function that receives two boolean and does a specific logic function such as AND/OR/XOR, how many examples would be required to figure out the appropriate function used? In the case of 2 boolean values, you'd need 4 examples.

# Overview

* The programmer provides pre-conditions and post-conditions
* The programmer provides input parameters and output with types
* The programmer provides a set of examples (inputs and outputs) for the automatic function synthesis to work through
* Define types in/out
* Give examples (may not be straightforward for objects)
* Use some sort of natural language/declarative (user-oriented) language to control oriented/procedural languages (use of conditionals)
* Provide examples in order of complexity
* The synthesizer is basically trying to build a proof for your examples, so it has to know the operation it can do and their impact on the state (see SHAKEY)
* Many approaches are possible, namely forward search, backward search, bidirectional search
* As there are many way to accomplish the same function, the first goal of the synthesizer should be to rapidly offer a working function to the user
* Once said function has been discovered, the synthesizer may work with the user in order to improve the current solution
	* *What are some of the improvement that can be expected to be made?*
* Given a set of existing functions (with both input/output types) and their computed "operation complexity" (basically the amount of operations that are executed at the language level, i.e. (x^2+y^2)^0.5 => 4, 3 exponentiation, 1 addition), try the functions in ascending order of operation complexity

# Keyword-based code identification
* File identification: List all the files containing the given set of keywords
* Evaluation of complexity based on the reach of these files (this implies that smaller, highly cohesive files are preferred as they reduce the reach)
* Compile the list of terms (functions, classes) visible at this point
* The program constructs a dictionary of synonyms, which he'll be able to reuse in the future when looking up for a given keyword

# Feature decomposition
* Components identification
* Association of available components to required components
* Identification of constraints (languages, platforms, API providers, available existing code (internal or third parties), target audience/consumers, etc.)

# Feature planning
* Assert what the system already does (expectations)
* Specify the feature, what does it do that the system currently does not (scope of the change)
* Determine what exist and is required for this feature (dependencies)
* Determine what is missing and will need to be added (creative part)
* Determine which functions will be required
* Determine which data will be required
* Determine the state in which you expect the data (pre-conditions)
* Determine where the data is in the required state (points of insertion)
* Determine what should be the final state of the data after being processed (post-conditions)
* Create the necessary functions to obtain data that cannot currently be obtained
* Construct a collection of sequences of function calls that will accomplish the required feature

# Feature development
* Determine the functions that will require a signature change
* Determine all the functions that will have to be modified due to signature change (calling functions)

# Useful tools during development
* Analyze existing code and generate/execute edge cases for the programmers to review
* Language edge cases assertions such as accepting null as a valid argument for a typed signature in Java or that objects are passed by reference in java
* Identification of thrown exceptions that are not catched
* Partial function testing: select a portion of code and fake data will be generated to test it

# See also

# Sources
* https://en.wikipedia.org/wiki/Automatic_programming
* [Approaches to Automatic Programming](http://www.sciencedirect.com/science/article/pii/S0065245808605197)