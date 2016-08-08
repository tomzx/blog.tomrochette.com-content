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
* How to avoid the program synthesizer from building a simple lookup table?
	* Is there times when a lookup table is the most appropriate solution?
* What makes it that some functions are just simpler to write than to provide examples for (or require many more examples than it would take to just implement it)? For instance, a function that receives two boolean and does a specific logic function such as AND/OR/XOR, how many examples would be required to figure out the appropriate function used? In the case of 2 boolean values, you'd need 4 examples.
* Task vs operation
* Debugging/troubleshooting automation
* How can the program synthesizer recognize that a data structure may need to be the composition of various other data structures?

# Overview
* The programmer provides pre-conditions and post-conditions
* The programmer provides input parameters and output with types
* The programmer provides a set of examples (inputs and outputs) for the automatic function synthesis to work through
* Give examples (may not be straightforward for objects)
* Use some sort of natural language/declarative (user-oriented) language to control oriented/procedural languages (use of conditionals)
* Provide examples in order of complexity
* The synthesizer is basically trying to build a proof for your examples, so it has to know the operation it can do and their impact on the state (see SHAKEY)
* Many approaches are possible, namely forward search, backward search, bidirectional search
* As there are many way to accomplish the same function, the first goal of the synthesizer should be to rapidly offer a working function to the user
* Once said function has been discovered, the synthesizer may work with the user in order to improve the current solution
	* *What are some of the improvement that can be expected to be made?*
* Given a set of existing functions (with both input/output types) and their computed "operation complexity" (basically the amount of operations that are executed at the language level, i.e. (x^2+y^2)^0.5 => 4, 3 exponentiation, 1 addition), try the functions in ascending order of operation complexity
* Truth table based construction of conditionals: You provide a list of variables to depend on and then construct a mapping between these variables and a block of code to be executed

# General problems
* How can the program synthesizer create a completely new function? What if this new function needs a set of other functions as well? Should it generate a single huge function and then refactor it into multiple functions or do that straight away?
* How can the program synthesizer determine the functions it needs to use to solve a specific case?
* How can we turn informal specification into a program?

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
* Decompose the required feature in a set of operations that will need to be accomplished
* Construct a collection of sequences of function calls that will accomplish the required feature

# Feature development
* Determine the functions that will require a signature change
* Determine all the functions that will have to be modified due to signature change (calling functions)

# Useful tools during development
* Analyze existing code and generate/execute edge cases for the programmers to review
* Language edge cases assertions such as accepting null as a valid argument for a typed signature in Java or that objects are passed by reference in java
* Identification of thrown exceptions that are not catched
* Partial function testing: select a portion of code and fake data will be generated to test it

# Programming tasks
In the list that follows, you will be able to observe various properties of the tasks required to write a program. Amongst them are:
	* Tasks related to generation
		* create blocks
		* variables
		* parameters definition
		* return definition
		* expressions
	* Tasks related specifically to programming
		* namespacing
		* code location
		* method modifiers
		* dependencies
		* function vs method

## Task list
### Mathematical foundations
Programming is at its core the task of passing values to functions/evaluating statements and receiving results.

* Generate function/method name
* Assign function/method name
* Determine inputs
* Determine parameters name
* Determine parameters type (for typed languages)
* Assign parameters type (for typed languages)
* Determine output
* Determine return type (for typed languages)
* Assign return type (for typed languages)
* Determine logic/sequence of statements to execute within the function/method/block (one of the most difficult tasks, if not the most)
* Generate variable name
* Assign variable name
* Declare variable type (for typed languages)
* Initialize variable
* Generate expression
* Assign expression to variable
* Call function/method
* Assign function/method call arguments

### Programming language specific
There are many tasks that are specifically related to the fact that we're using a language which has been designed with some grammatical constraints. As such, we must respect them. Programming languages also allow us to better structure our work so that it is easier to work with (through code separation in multiple files and namespace for instance).

* Create block boilerplate ({ ... } or indentation (for python))
* Move block to proper location (e.g. in a class definition block)
* Determine code location/filename
* Generate namespace name
* Declare namespace
* Determine function/method namespace
* Determine modifiers (public/protected/private/static/abstract/final/virtual/override) (class/method)
* Determine if it should be written as a function or a class method
* Determine the appropriate class in which a method should be added
* Comment parts of code to express intent/reasoning/decision choices
* Determine dependencies (include/require/use/import)
* Import dependencies

* Determine encapsulation
* Determine function/method/class collaborators
* Determine function/method/class responsibilities
* Determine (temporal) coupling

* Respect syntax
* Respect formatting rules
* Respect naming conventions
* Respect code style

### Block specific
* If
	* Create block (if (...) { ... })
		* Determine predicate
		* Evaluate block pre-conditions based on predicate
	* Create elseif block (elseif (...) { ... })
		* Determine predicate
		* Evaluate block pre-conditions (based on if/elseif predicates)
	* Create else block (else { ... })
		* Evaluate block pre-conditions (based on if/elseif predicates)
* Foreach
* For
* While
* Switch

## Generalized tasks
From the list of tasks we've established so far, we can try to create a list of generalized tasks (operations that do the same thing under different contexts).

* Generate names (for functions/methods/classes/namespaces/variables)
* Type inference/manipulation
* Block localization (function/method/class)

## Task list execution
The execution of tasks as described earlier is most likely done through a while loop, in which the task to execute at any moment appears to be selected at random, such that the code would look something like

```
while (programming) {
	switch (rand() % numberOfTasks) {
		// break; have been removed to better present the idea
		case 0: // task A
		case 1: // task B
		case 2: // task C
	}
}
```

There's also likely to be some sort of evaluative loop that is assessing the code observed for things that will need to be done. In some sense, the internals of the programming loop is more likely to resemble a markov decision process, where certain tasks are very likely to be executed just after a given task was executed (e.g. initializing a variable after it has been declared).

# Observation on the programming tasks
* Some tasks are incredibly easy to solve if you leave them in complete freedom. For instance, if no constraint is applied for variable naming, then any string is valid as any other, as long as they do not overlap with existing variables. However, if you introduce naming conventions, or the more difficult task of assign a "proper" name to a variable, the difficulty of the task increases tremendously.
* Some tasks can only be defined using a high level description. One example of this is the translation of high level requirements into functional logic. This basically entails the search of one solution out of the solution space which fulfills the X different criteria at most (and not more).
* Programming cannot be self-contained. Programming is valuable only when it is associated with the modeling of something that is external to it; modeling the world. A program generator can create an infinite amount of programs, but they will all be meaningless as meaning is only attached to code by the programmer.

# Data structure selection
By observing the properties that can vary in the most common data structure, it is possible to devise a generic decision tree which would allow a program to determine the most appropriate data structure to use given a set of operations that will be applied to the data being manipulated. This list below is by no mean exhaustive but only gives an idea of the process that would go on during data structure selection.

* What is the most common operation on the data structure?
	* Read/Access
	* Write/Modification
* Determine how data is accessed (impacts time complexity)
	* Is it sequential?
	* Is it random?
	* Is it mostly at the beginning or the end?
	* Is it mostly in the middle?
	* Is it for specific keys?
* Determine space constraint (impacts space complexity)
	* Limited
	* Unlimited (or at least as much as available)

* Array
* Vector
* String
* List
	* Singly linked list
	* Doubly linked list
	* Circular linked list
* Queue
* Deque
* Stack
* Set
* Map/Dictionary
* Multiset
* Multimap
* Priority Queue
* Graph
* Tree
	* Binary tree
	* Binary search tree
	* Heap
	* Red-black tree
	* AVL
	* B-tree
	* Splay tree
	* Quadtree/Octree
	* Trie
	* Minimum spanning tree
* Matrix

# Ideas for programming assistants
* Define two procedures (Hewitt75):
	* One to implement the desired transformation
	* One to check if the transformation has in fact been accomplished
* If the programming assistant can aid expert programmers in demonstrating that two rather different implementations produce equivalent behavior, then we can be much more confident that the system will behave in a useful way (Hewitt75)

# See also
* Program induction

# Sources
* https://en.wikipedia.org/wiki/Automatic_programming
* [Approaches to Automatic Programming](http://www.sciencedirect.com/science/article/pii/S0065245808605197)
* Green, Cordell, and David R. Barstow. [A Hypothetical Dialogue Exhibiting a Knowledge Base for a Program-understanding System](http://i.stanford.edu/pub/cstr/reports/cs/tr/75/476/CS-TR-75-476.pdf). Stanford, CA: Stanford University, 1975.
* Hewitt, Carl E., and Brian Smith. "Towards a programming apprentice." IEEE Transactions on Software Engineering 1 (1975): 26-45.
* Newell, Allen. [Report on a General Problem-solving Program](https://www.u-picardie.fr/~furst/docs/Newell_Simon_General_Problem_Solving_1959.pdf). Santa Monica, CA: Rand, 1959.
* Rich, Charles, and Richard C. Waters. "The Programmer's Apprentice: A research overview." Computer 21.11 (1988): 10-25.
* Inductive programming - http://www.inductive-programming.org/
* Program transformation - http://www.program-transformation.org/
* Universal Data Structure - https://groups.google.com/forum/#!topic/magic-list/LhDuHtyas9Q