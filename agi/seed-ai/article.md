---
title: Seed AI
created: 2015-09-26
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

A seed AI is an initial computer program that is able to recursively self-improve. This means that once it is started, one of its main goals will be to improve its existing code into a better one and then switch to this newer implementation in order to benefit from the changes its made to it.

Seed AI is interesting because it would mean writing a very bad version of it initially which would get improved by the algorithm itself. Furthermore, it would also mean that you might be able to give it external programs and it would proprose improvements to it.

In other words, a seed AI is one that would learn and understand how program works, what their purpose is and what meaningful improvements can be made.

## Learned in this study

## Things to explore

* What are the issues with writing a program generator
* What are the tools that we currently have to solve those issues
* Look at theoretical implications of program generation (probabilities)
* Define the problem and the goal
* There are infinite programs that can be built, what does that mean?
    * What does it means if you consider those programs can help improve the existing program?
    * Is there such a thing as a *single* "perfect" program?
* Isomorphisms of programs considered/identified as integers
* Are sleep() calls put into code *always* candidate for optimisation?
* What is the impact of rand() in testing for algorithmic improvement?

# Overview

The goal of this study is to look into the constraints and requirements that goes into building what is called a *Seed AI*, that is, a program that is able to improve itself.

The goal of building such a program is to then allow it to run free and hope that it will be able to rapidly (hopefully at an exponential rate). With such rapid rate of improvement, it should be able to catch up with our intelligence rapidly and once it has surpassed us, *hopefully* help us improve our understanding of the world and answer questions we haven't been able to answer ourselves yet.

# Naive program generator

A 10 character long program in the range of ASCII 32 - 127 will have approximately ((127 + 1) - 32)^10 = 6.6 x 10^19 (that's 66 quintillion) possible permutations.

To put 66 quintillion in perspective, let say we can test approximately 10^4 programs per second (ignoring the fact that the longer the programs get, the longer the compiler will take to *process* the program). We're left with about 2.1 x 10^8 years of computation to do. Obviously we could use various methods to improve our odds of getting there faster by using parallelism (using multiple cores, multiple processors).

However, a very little percentage of those 66 quintillion permutations will be valid code. Thus, it is obvious that generating all those permutations is a naive way to generate valid programs.

Furthermore, to truly understand the issue here, we're talking about generating *only* the set of all valid strings of length 10, which is terribly small. Increase the length by one and you now have ((127 + 1) - 32)^11 - ((127 + 1) - 32)^(11 - 1) = 6.3 x 10^21 (6 sextillion) of programs of length 11 to check. Thus, building any *real* program that can get into the millions of line of code, with an average of 10 characters per line, you're going to be waiting for a while to get that program.3

# The program tree

When we write programs, we can think of the all the code concatenated together as a single string. That string is the program.

We can think about each program as being part of a tree where the root is the empty program. From that program can spawn (127 + 1) - 32 programs (we assume the range characters used in the program are from ASCII 32 to 127).

Each level n of the tree represent the strings of length n. So, the root as level = 0 has a length of 0, and a string at level 10 has a length of 10.

# Improving the naive program generator

What we can do to greatly reduce the search space is to teach the program generator a little bit:

* Give it a grammar of the language it is using. There is no point in generating code that "should" not compile (it can be useful if what you're doing is verifying that the grammar is properly implemented).
* Promote function reuse. Once some functionality has been programmed, there's no point in writing that bit of code again. This means that we can remove/ignore all of the nodes in the program tree that have this string place somewhere else or is there more than once.
* TODO

# Some problems that remain

However, even given these *tools*, the program generator still can spend an immense amount of time generating useless programs:

* It can generate infinitely long *valid* text strings.
* It can generate infinitely long *valid* expressions.
* It can generate an infinitely long *valid* sequence of function calls that do not produce any valuable result.
* and so on...

# Testing programs for improvement

When we think of programs and algorithms quality, we generally think of them in terms of complexity of time and space. Thus, in order to look for improvements in an algorithm (a unit of a program), the seed AI would have to execute said algorithm with various test cases in order to see the impact it has both on time and space. This would be considered the empirical approach to testing algorithms for improvement.

Another approach, known as theoretical approach, consists of analyzing the algorithm in terms of the operation it accomplishes (such as for/foreach/while loops). This approach is very interesting as it does not require the seed AI to test many cases in order to establish if a change was an improvement or not (this is akin to doing white box testing).

Finally, there is an hybrid approach, which combines the previous two approaches. If you are only able to analyze the algorithm with some degree of confidence, then it is possible to validate if your estimates are correct by running various test cases against the algorithm. If your estimates are correct, then you can proceed to work on something else, otherwise you may have to review your analysis.

## Criteria for *properly* testing programs for improvement

Assuming an already correct algorithm (one that is devoid of any incorrect behavior), the seed AI...

* Must test that the change does not modify the output for the same input (if any)
	* In the case that no output is generated by a function (think of object oriented programming), the internal state must remain the same
* Must respect/have the same preconditions/postconditions of the original algorithm
* Must test for various inputs in order to observe their impact (black box testing)
* May analyze the source code in order to understand how the inputs affect computation time and space (white box testing)

This list is however constraining. A simple example of that constraint is asking a seed AI to optimize an algorithm such as quicksort. If it is already divided into its main parts, picking a pivot, separating values on each side of the pivot, recursively sorting, then it may not be possible to optimize any part separately. However, it may be possible to optimize the algorithm as a whole.

It is important to be able to make the difference between the API and its internal, since the goal of optimizing a program is generally to rewrite the internals, however they might have been assembled, into a new structure that is more optimized for the task.

# Sources

* https://en.wikipedia.org/wiki/Recursive_self-improvement
* http://wiki.lesswrong.com/wiki/Seed_AI
* http://mattmahoney.net/rsi.pdf
* Turing, Alan. *Intelligent Machinery*. London: National Physical Laboratory, 1948. Ed. B. Jack Copeland. The Essential Turing. Oxford: Clarendon Press, 2004. 430
