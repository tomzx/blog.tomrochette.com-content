---
title: Alan W. Biermann - Approaches to Automatic Programming
created: 2016-06-03
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore
* Is building a set of inductive/constructive examples more likely to properly induce a program synthesizer toward the appropriate program?
* What is the maximal size of a function such an could generate?
* How complex are the functions that can be generated? Can it handle recursive functions?

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

## 3 Program Synthesis from Examples
## 3.1 Introduction
* Many a programmer has wished for a system that would read in a few examples of the desired program behavior and automatically create that program
* The synthesis task itself from weak input information is incredibly difficult
* The program synthesizer could attempt to do its job by enumerating the set of all possible programs in the language in order of increasing length, testing each one to see if it is capable of the desired behavior
* When it finds such a program, it prints it out as its answer and halts
* We know that the correct answer will exist somewhere in the enumeration so that it will be found eventually
* But this strategy has a severe pitfall because it is not possible to tell for an arbitrary program whether or not it can produce the desired behavior
* Since the halting problem for an arbitrary program on given data is undecidable, one cannot tell what the program might print out, since one cannot tell whether it will even halt
* This problem cannot, in general, be avoided, so that we have a theorem:
	* The programs for the partial recursive functions cannot be generated from samples of input-output behavior
* The only way this strategy can be made to work is to enumerate a subset of the partial recursive functions for which the halting problem is solvable or to allow for a partial solution to the halting problem by limiting the number of steps a program may complete before it halts
* Suppose the solution by enumeration method can be made to work. It is still possible that the system might produce a wrong answer because some program that precedes the correct answer in the enumeration might be able to complete the given examples
* The severest difficulty with the solution by enumeration is the extreme cost of the enumeration
* The target program in (the current example) would be beyond the billionth program in most enumerations, meaning that a great amount of time might pass before even this trivial program could be found
* Therefore, the task of program synthesis from examples is essentially intractable unless these problems can be avoided
* Two methods for making the approach feasible:
	* Limit the class of synthesizable programs
	* Include intermediate information about how each output is obtained from its corresponding input

## 3.2 The Method
* A reasonable technique for generating programs from examples of their behavior executes the following two steps:
	* For each example input $X_i$ and its associated output $Y_i$, determine the sequence $S_i$ of operations required to convert $X_i$ to $Y_i$
	* Find a program that executes each required sequence of operations $S_i$ when given its associated input $X_i$
* The discovery of acceptable sequences $S_i$ can involve an astronomical amount of enumeration
* There may be many sequences $S_i$ that convert $X_i$ to $Y_i$ and a method must be found for discovering which sequence to use for each $i$.

## 3.6 Discussion
* Program construction processes have been speeded up sufficiently through the use of enumeration pruning, limiting assumptions on the class of programs being synthesized, and user-specified example calculations so that programs of practical size can be created automatically
* The approach (described) has the following advantages:
	* The user has no need to learn traditional language syntax
	* The user has direct visual contact with his data structures and can manipulate them in an extremely natural manner with his hands
* Major disadvantages of the approach are:
	* The display terminals are not large enough to display easily large or multidimensional data structures
	* The correctness of automatically generated programs is not always easy to determine
* The "trace" of the computation can be efficiently constructed for large classes of functions from the structures of the input and output lists
* Furthermore, the programs can be built from the traces almost algorithmically with little or no searching

## 4 Synthesis from Formal Input-Output Specifications
## 4.1 Introduction
* Rather than giving examples of the desired program behavior, it may be preferable to specify precisely the required input-output characteristics and have the program automatically generate from these

## 4.3 Problem Reduction Methods
* P{A}Q means that if assertions P are true and program A is executed to halt, then Q will be true
* The program synthesis problem then can be stated: Given input specification I and output specification G, find A such that I{A}G
* A typical reduction step would be to divide A into two segments A1 and A2 and attempt to construct A1 and A2 separately
* A set of intermediate specification Q are determined and the two problems I{A1}Q and Q{A2}G are attacked separately
* The Buchanan and Luckham approach assumes that the system has a large amount of programming knowledge in the form of inference rules. The system also needs domain specific information, called frame information

## 5 Translation of Natural Language Commands
## 5.2 Syntatic Analysis
* Systemic grammars hierarchically decompose utterances into three basic classes:
	* clauses
	* groups
	* words
* Each sentence is broken down into one or more clauses, clauses are primarily made up of groups, and groups are primarily composed of words
* There are four types of groups:
	* noun
	* verb
	* preposition
	* adjective

## 6 Heuristic Knowledge-Based Algorithm Synthesis
## 6.1 Introduction
* A program synthesis is said to be sound if the program produced is guaranteed to meet the specifications input to the system
* A system is said to be complete if it is capable of producing every possible program over the domain of interest (usually the partial recursive functions)
* It is desired that the system should have
	* programming knowledge such as how to declare data structures, build loops and branches, and so forth
	* problem domain knowledge such as what are the significant variables and how are they related
	* debugging knowledge such as how to discover and remove the cause of a discrepancy between program performance and specification
	* knowledge of the user such as what information to expect from him, what information to send him, and how to converse with him in his own language
* A heursitic program will be defined as a program whose input-output characteristics are not easily specified (except perhaps by paraphrasing the program itself)
* While the program synthesizer using heuristics might produce false starts, try various ideas, modify partial solutions, and erase and begin again, it is hoped that it can slowly converge to a reasonable solution, particularly if it can work continuously in an interaction with a human being

# See also

# Sources
* [doi:10.1016/S0065-2458(08)60519-7](http://www.sciencedirect.com/science/article/pii/S0065245808605197)