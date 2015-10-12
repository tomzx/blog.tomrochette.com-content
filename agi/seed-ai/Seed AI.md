# Seed AI

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

# Sources

* https://en.wikipedia.org/wiki/Recursive_self-improvement
* http://wiki.lesswrong.com/wiki/Seed_AI
* http://mattmahoney.net/rsi.pdf
* Turing, Alan. *Intelligent Machinery*. London: National Physical Laboratory, 1948. Ed. B. Jack Copeland. The Essential Turing. Oxford: Clarendon Press, 2004. 430