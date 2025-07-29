---
title: Allen Newell - The heuristic of George Pólya and its relation to artificial intelligence (1981)
created: 2016-06-15
taxonomy:
  tag: [artificial general intelligence]
  status: finished
---

## Context

## Learned in this study

## Things to explore

# Notes
## 2 Pólya's Heuristic
* A set of heuristics for problem-solving, cast in the form of brief questions (What is the unknown?) and commands (Draw a figure!), within a frame of four problem solving stages:
	* Understand the problem
	* Obtain a plan
	* Carry out the plan
	* Look back at the solution

## 2.1 Model of Human Problem Solving
* AI views a problem solver as an information processing system, which acquires a problem from a task environment by encoding it in an internal data structure, and which solves the problem by processing these structures by (a sequence of) internally available methods, making use of bodies of encoded knowledge
* AI declares thereby for a general theory of problem solving, applicable to humans, computers, animals or Martians
* Differences exist between different types of problem solvers
* These differences arise from specific features in the architecture - different tradeoffs in speed, memory and accessing, which induce different styles of problem solving, different choices of methods, etc.
* 3 characteristics that loom largest in Pólya's treatment
	* Attention must be focused: Problem solving happens when the human attends to various aspects of a problem
	* Memory must be tickled: Contact must be made with what the problem solver already knows
	* Problem solvers must be motivated
* Humans have a tendency to block, i.e., to get into cognitive ruts, and that they must do special things to open themselves up to alternatives that break out of the restrictive sets

## 2.2 Problem Solving Methods
* As far as the problem solver's structure is concerned, they presume only that it attempts problems by setting goals and is capable of following procedures
* The earmarks of what has come in AI to be called a method:
	* It is a specific way to proceed
	* It is a rational way to proceed
	* It involves subgoals and subplans
	* Its occurrence is observable
* Other methods of interest
	* Reductio ad absurdum
	* Method of loci
	* Go back to definitions
	* Sequence of convertible transformations
	* Working backwards
	* Accumulate knowledge
	* Test by dimension
	* Interpret the formula
	* Switch the unknown

## 2.4 Preparing for Future Problem Solving
* A large stock of specific problems, their solutions, and the specific method of their solution is a necessary feature of a good problem solver

## 2.5 Credibility of Inductions and Analogies
* The process of problem solving continuously generates new problems - transformation of the original problem as well as auxiliary problems

## 2.6 Heuristics
* Heuristics are rules of thumb and bits of knowledge, useful (though not guaranteed) for making various selections and evaluations
* A few examples of separate heuristics that do occur in Pólya's work:
	* Work in letters not numbers
	* Treat symmetric elements symmetrically
	* If you can't construct a figure, construct one geometrically similar
	* Check only "touchy" parts of an argument
	* If the unknown is a derivative, then introduce derivatives generally
	* Two proofs are better than one
	* Good problems, like mushrooms, grow in clusters
	* Do not believe anything, but doubt only what is worth doubting
	* Teachers should ask questions that are simple, general, unobtrusive and from a short list
	* An idea which can be used only once is a trick. If one can use it more than once it becomes a method

## 3.5 Thesis: Future Orientation is still Beyond AI
* The main aspect of successful problem solving is detailed knowledge of a massive number of specific problems, solutions and methods

## 4.1 The Space of Auxiliary Problems
* Thesis (reformulation): Auxiliary problems require problem spaces that are still beyond AI's capability

## 4.1.1 Problem spaces
* A central hypothesis in AI is that intelligent action occurs by means of search in a problem space
* A problem space consists of a set of states and a set of operators that when applied to states yield new states
* Thus, the operators provide paths through the space
* A problem is given by giving an initial state and specifying in some fashion a class of goal states plus possibly some path constraints - the problem being to get from the initial state to any of the goal states along a path that does not violate any of the constraints
* A problem solver's basic capabilities are expressed by the problem spaces it can employ. It is able to work on any problem in a space. It may not solve the problem, but it can attempt it and engage in appropriate problem-solving behavior. Problems outside this space lie outside the problem solver's competence or even comprehension. A problem solver may be able to work in many problem spaces, its total competence being expressed in their union
* Even where the knowledge is sufficient, there is always a contextual threat of combinatorial search

## 4.1.3 Object-centered problem spaces
* A great communality exists in these problem spaces: They are all object-centered

## 4.2 Finding an Auxiliary Problem
* Pólya's view is clearly that auxiliary problems are to be found in the problem solver's prior experience, i.e., in his long term memory

## 4.3.1 The independence of using from finding
* Thesis (second reformulation): AI cannot handle auxiliary problems, because AI does not yet know how to handle wild subproblems
* Wild subproblem: A subproblem whose use in the main problem is still a problem, even after it is solved
* The connection problem: How to connect the solved auxiliary problem with the main problem

# See also
* [How to Solve It](../../books/how-to-solve-it/article.md)

# References
