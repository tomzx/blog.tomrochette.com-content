---
title: Seed AI
created: 2015-09-26
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

A seed AI is an initial computer program that is able to recursively self-improve. This means that once it is started, one of its main goals will be to improve its existing code into a better one and then switch to this newer implementation in order to benefit from the changes it has made to it.

Seed AI is interesting because it would mean writing a very bad version of it initially which would get improved by the algorithm itself. Furthermore, it would also mean that you might be able to give it external programs and it may propose improvements to it.

In other words, a seed AI is one that would learn and understand how program works, what their purpose is and what meaningful improvements can be made.

## Learned in this study

## Things to explore

* What are the issues with writing a program generator?
* What are the tools that we currently have to solve those issues?
* Look at theoretical implications of program generation (probabilities)
* Define the problem and the goal
* There are infinite programs that can be built, what does that mean?
    * What does it means if you consider those programs can help improve the existing program?
    * Is there such a thing as a *single* "perfect" program?
* Isomorphisms of programs considered/identified as integers
* What kind of analysis can be done in order to reduce/discover isomorphic programs?
* Are sleep() calls put into code *always* candidate for optimisation?
* What is the impact of rand() in testing for algorithmic improvement?
* DNA is code, and it most likely didn't start the length it is now.
	* In order to lenghten, smaller parts could have merged together (working programs merged/concatenated to one another)
	* https://en.wikipedia.org/wiki/Origin_of_replication (What are the origin of DNA?)
* Generating programs amount to generating graphs, what does that imply?
* Learn "valuable" programs from a training set (SL), then use MCTS + Q-Learning (policy network + value network) to determine the direction in which newer programs should be searched (RL)

# Overview

The goal of this study is to look into the constraints and requirements that goes into building what is called a *Seed AI*, that is, a program that is able to improve itself.

The goal of building such a program is to then allow it to run free and hope that it will be able to rapidly (hopefully at an exponential rate) improve itself. With such rapid rate of improvement, it should be able to catch up with our intelligence rapidly (assuming intelligence is only a manifestation of the emergence of knowledge) and once it has surpassed us, *hopefully* help us improve our understanding of the world and answer questions we haven't been able to answer ourselves yet.

We will obviously neglect discussing about means to control this seed AI as well as any negative consequences related to building such an AI. Those are extremely important topics, however they are not the focus of this article.

Let us first start by designing a naive program generator, with the hope we can build something simple enough that it can run on its own and evolve.

# The program tree

When we write programs, we can think of the all the code concatenated together as a single string. That string is the program.

We can think about each program as being part of a tree where the root is the empty program. From that program can spawn (127 + 1) - 32 = 96 programs (we assume the range characters used in the program are from ASCII 32 to 127).

Each level **n** of the tree represent the strings of length **n**. The root of the tree has level **n** = 0 and thus has a length of 0 while a string at level **n** = 10 has a length of 10.

# Naive program generator

A 10 character long program in the range of ASCII 32 - 127 will have approximately $((127 + 1) - 32)^{10} = 6.6 \times 10^{19}$ (that's 66 quintillion) possible permutations.

To put 66 quintillion in perspective, let say we can test approximately 10^4 programs per second (ignoring the fact that the longer the programs get, the longer the compiler will take to *process* the program, but in the case of a 10 character program, it's neglectable). We're left with about $2.1 \times 10^8$ years of computation to do ($\frac{6.6 \times 10^{19} programs}{10^4 \frac{programs}{s} \times 365 \frac{day}{year} \times 24 \frac{h}{day} \times 60 \frac{m}{h} \times 60 \frac{s}{m}}$). Obviously we could use various methods to improve our odds of getting there faster, for instance by using parallelism (using multiple cores, multiple processors, multiple computers).

However, testing those 66 quintillion programs seems like a big waste of time, power and resources. Only a certain percentage of those 66 quintillion permutations are valid code. Thus, it is obvious that generating all those permutations is a naive way to generate *potentially* valid programs.

Furthermore, to truly understand the issue here, we're talking about generating *only* the set of all valid strings of length 10, which is terribly small. Increase the length by one and you now have $((127 + 1) - 32)^{11} - ((127 + 1) - 32)^{(11 - 1)} = 6.3 \times 10^{21}$ (6 sextillion) of programs of length 11 to check (note that we excluded all programs of length 10 or less). Thus, building any *real* program that can get into the millions of lines of code and with an average of 10 characters per line, will require you to be wait for a while.

One interesting problem here is that very small programs can be valid. For instance `0;` is a valid program. For that matter, any number should be a valid program in C (in our little 10 character program, we can generate $10^9$ programs based only on numbers: 9 numbers from 0-9 and a semi-colon (;) to terminate, considering all programs are wrapped within the obligatory `void main() { code here }`). This means we can basically generate many programs that basically do nothing other than creating giant numbers. Furthermore, there's also a ton of programs that will do arithmetic but never print out anything. Or print a ton of garbage/random. Maybe it is something we want... But often it's not.

It's also important to notice that a certain space of the program tree will represent equivalent code, just using different variable names. The same can be said about variable definition being permutated without any effect, or calculation order being permutated without having any effect. **What kind of analysis can be done in order to reduce/discover isomorphic programs?**

From this little analysis, we can deduce a few *rules*:
* A program should *produce* something, in other word generate some sort of output (doing arithmetic without returning anything amounts to running NOPs). This can be rephrased by saying that any program that is dead code should not be considered valuable.
* If it does not produce an output, then it should alter its input. In doing so, the altered input IS the output of the program.

# Improving the naive program generator

What we can do to greatly reduce the search space is to teach the program generator a little bit:

* Give it a grammar of the language it is using. There is no point in generating code that "should" not compile (it can be useful if what you're doing is verifying that the grammar is properly implemented).
* Promote function reuse. Once some functionality has been programmed, there's no point in writing that bit of code again. This means that we can remove/ignore all of the nodes in the program tree that have this string place somewhere else or is there more than once.
* TODO

# Reducing the search scope

In an attempt to reduce the volume of valid, but isomorphic programs, we will spend a bit of time studying what make different programs (or functions) isomorphic (different at the high level language but the same from a low level perspective).

We'll assume we're using a high level language with typing.

```cpp
function x(A a, B b) = function y(B b, A a)
```

Two functions which have the exact same internal logic but different parameters order are isomorphic. In order to reduce the amount of functions generated with the same internal logic but different signature, we'll establish the following rule:

**Parameter ordering rule:** Each parameter shall be ordered by their lexicographical ordering (that is (a, b) <= (a', b') if and only if a < a' or (a = a' and b <= b')).

For a number $x$ of different parameters there is at most $x!$ signatures permutations. Using the **Parameter ordering rule**, we can limit it to 1.

If there are $x$ types in the system, for a function with $y$ parameters we have at most $y^x$ permutations. Following the **Parameter ordering rule**, we can limit it to $\binom{y+(x-1)}{x-1}$. For example, a system with 3 types and a function with 3 parameters will have $\binom{3+(3-1)}{3-1} = \binom{5}{3} = 10$ potential function signatures and not $3^3 = 27$.

Another thing we may do in order to limit the amount of generatable functions is to add artificial constraints such as "functions shall not have more than 10 statements" or "functions shall not have more than 3 levels of indentations" or "functions shall contain at most 1 level of indirection" (law of demeter). Using design guidelines and best practices, it may be possible to shape and reduce down the number of "acceptable" functions within our programs.

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

## Seed AIs

* https://en.wikipedia.org/wiki/Eurisko
