---
title: Report on a General-Problem Solving Program (1959)
created: 2016-05-12
taxonomy:
  tag: [Artificial General Intelligence]
  status: finished
---

## Context

## Learned in this study

## Things to explore

# Overview

# Notes

* The major features of the program that are worthy of discussions are:
	* The recursive nature of its problem-solving activity
	* The separation of problem content from problem-solving technique as a way of increasing the generality of the program
	* The two general problem-solving techniques that now constitute its repertoire: means-ends analysis, and planning
	* The memory and program organization used to mechanize the program
* The principal means of investigation is synthesis: programming large digital computers to exhibit intelligent behavior, studying the structure of these computer programs, and examining the problem-solving and other adaptive behaviors that the programs produce
* A genuine problem-solving process involves the repeated use of available information to initiate exploration, which discloses, in turn, more information until a way to attain the solution is finally discovered

## The Executive Program and the Task Environment
* GPS operates on problems that can be formulated in terms of objects and operators
* An operator is something that can be applied to certain objects to produce different objects
* The objects can be characterized by the features they possess, and by the differences that can be observed between pairs of objects
* Operators may be restricted to apply to only certain kinds of objects; and there may be operators that are applied to several objects as inputs, producing one or more objects as output
* To operate generally within a task environment characterized by objects and operators, GPS needs several main components:
	* A vocabulary, for talking about the task environment
	* A vocabulary, dealing with the organization of the problem-solving processes
	* A set of programs defining the terms of the problem-solving vocabulary by terms in the vocabulary for describing the task environment
	* A set of programs applying the terms of the task-environment vocabulary to a particular environment: symbolic logic, trigonometry, algebra, integral calculus
* To specify problems and subproblems, GPS has a discrete set of goal types
* With each goal type is associated a set of methods related to achieving goals of that type
* When an attempt is made to achieve a goal, it is first evaluated to see whether it is worthwhile achieving and whether achievement seems likely
* All the heuristics apply the following general principle:
	* The principle of subgoal reduction: Make progress by substituting for the achievement of a goal the achievement of a set of easier goals

## Planning as a Problem-Solving Technique
* This planning method consists in
	* abstracting by omitting details of the original objects and operators
	* forming the corresponding problem in the abstract task environment
	* when the abstract problem has been solved, using its solution to provide a plan for solving the original problem
	* translating the plan back into the original task environment and executing it

# See also

# References
* https://www.u-picardie.fr/~furst/docs/Newell_Simon_General_Problem_Solving_1959.pdf