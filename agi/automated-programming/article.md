---
title: Automated programming
created: 2016-06-04
taxonomy:
  tag: [artificial general intelligence, programming, automation, machine learning, software development]
  status: in progress
---

## Context
Automated programming has been a goal for computer scientists since the inception of the field. Being able to generate code either by providing examples of inputs/outputs or a specification description is not without its share of difficulties. In this article, we explore the process of programming, with the objective of discovering what can be automated and how, and what causes serious challenges.

## Learned in this study
* Communication is difficult
* Understanding is difficult
* A part of the job of the programmer is to construct a model of the software of the client so that it can understand how a requirement/change fits into this model
* A programmer needs to know how many systems works: the programming language, third-party libraries, the file system, the database, the network, external APIs

## Things to explore
* How to avoid the program synthesizer from building a simple lookup table?
	* Is there times when a lookup table is the most appropriate solution?
* What makes it that some functions are just simpler to write than to provide examples for (or require many more examples than it would take to just implement it)? For instance, a function that receives two boolean and does a specific logic function such as AND/OR/XOR, how many examples would be required to figure out the appropriate function used? In the case of 2 boolean values, you'd need 4 examples.
* Task vs operation
* Debugging/troubleshooting automation
* How can the program synthesizer recognize that a data structure may need to be the composition of various other data structures?
* Provide the program synthesizer with all the required functions, it just needs to "put the plumbing together" (call the functions in the right order and with the right parameters)
	* What are the implications of such constraint?
* Learn how to code from looking at commit comments and code changes
* English description to function parts
* Programming requires communication: the client explaining what it needs the system to do to the programmer, the programmer converting these requirements into a high level language code, the code being converted into computer instructions.
	* Where does automated programming comes in?
* The basic strategy of a beginner programmer is generally to copy and paste code. Is it possible to reproduce and use this behavior effectively in an automated manner?
* What is the difference between writing a program from scratch and modifying an existing program?
* How hard is it for an AI to learn programming languages? Assembly, C, C++, etc.
* Is it possible to construct a neural network where function calls are replaced/identified by numbers (somefunction() = 3, otherfunction() = 13)?
	* Can we use tools from NN-NLP to build programs?
* Use an ontology of algorithm to determine which ones should be used within a function
	* Use the vocabulary associated with each type of algorithm to identify actions (sort the items by ..., group the items by ..., find the shortest path between ...)
* Any program is going to be composed of (at most) loops, conditions, expressions and statements
* Say you have a thousand (and more) projects source code in a given language, and you want to extract common programming constructs (similar code but with different variable names or function names, or slightly different statements), how would you go about doing that in an efficient way?
* Extract the most common programming construct by looking at a lot of code
* Use something like CharRNN, but instead of applying it to characters, apply it to programming language tokens
* The learned model can be used to predict the next token type to be used
	* The next token type is likely to be inferable from the grammar alone

# Overview
We can think of automated programming as the ability to convert some form of specification which uses vague terms into an extremely specific, programming language constrained, description of the specification. This requires a lot of prior experience in order to understand the purpose and intent of each and every requirement. In other words, part of the task of automated programming is the ability to translate, given experience and context, a set of requirements (a specification) into a program.

* The programmer provides preconditions and postconditions
* The programmer provides input parameters and output with types
* The programmer provides a set of examples (inputs and outputs) for the automatic function synthesis to work through
* Give examples of input/output combinations (may not be straightforward for objects)
* Provide examples in order of complexity
* Use some sort of natural language/declarative (user-oriented) language to control oriented/procedural languages (use of conditionals)
* The synthesizer is basically trying to build a proof for your examples, so it has to know the operation it can do and their impact on the state (see [SHAKEY](https://en.wikipedia.org/wiki/Shakey_the_robot))
* Many approaches are possible, namely forward search, backward search, bidirectional search
* As there are many way to accomplish the same function, the first goal of the synthesizer should be to rapidly offer a working function to the user
* Once said function has been discovered, the synthesizer may work with the user in order to improve the current solution
	* Decide on the memory/computation tradeoff within the solution
	* *What are some of the improvement that can be expected to be made?*
* Given a set of existing functions (with both input/output types) and their computed "operation complexity" (basically the amount of operations that are executed at the language level, i.e. (x^2+y^2)^0.5 => 4, 3 exponentiation, 1 addition), try the functions in ascending order of operation complexity
* Truth table based construction of conditionals: You provide a list of variables to depend on and then construct a mapping between these variables and a block of code to be executed

# General problems
* How can the program synthesizer create a completely new function? What if this new function needs a set of other functions as well? Should it generate a single huge function and then refactor it into multiple functions or do that straight away?
* How can the program synthesizer determine the functions it needs to use to solve a specific case?
* How can we turn informal specification into a program?
* What should happen if, given a set of existing functions, the synthesizer cannot build the requested function?

# Keyword-based code identification
* File identification: List all the files containing the given set of keywords
* Evaluation of complexity based on the reach of these files (this implies that smaller, highly cohesive files are preferred as they reduce the reach)
* Compile the list of terms (functions, classes) visible at this point
* The program constructs a dictionary of synonyms, which it will be able to reuse in the future when looking up for a given keyword

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
* Determine the state in which you expect the data (preconditions)
* Determine where the data is in the required state (points of insertion)
* Determine what should be the final state of the data after being processed (postconditions)
* Create the necessary functions to obtain data that cannot currently be obtained
* Decompose the required feature in a set of operations that will need to be accomplished
* Construct a collection of sequences of function calls that will accomplish the required feature
* Assess if changes can be done to existing functions (do we want this change to apply to existing functionality or be a new case?)

# Feature development
* Determine the functions that will require a signature change
* Determine all the functions that will have to be modified due to signature change (calling functions)

# Useful tools during development
* Analyze existing code and generate/execute edge cases for the programmers to review
* Language edge cases assertions such as accepting null as a valid argument for a typed signature (in Java) or that objects are passed by reference (in Java)
* Identification of thrown exceptions that are not caught
* Partial function testing: select a portion of code and fake data will be generated to test it

# Programming tasks
In the list that follows, you will be able to observe various properties of the tasks required to write a program. Amongst them are:

* Tasks related to generation
	* create blocks
	* variables
	* parameters definition
	* return definition
	* statements
	* expressions
* Tasks related specifically to programming
	* namespacing
	* code location
	* method modifiers
	* dependencies
	* function vs method

## Task list
### Mathematical foundations
Programming is at its core the task of passing values to functions, evaluating statements and receiving results.

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
* Determine preconditions
* Determine postconditions
* Determine invariants
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

* Iterate over a collection (loops)
* Order a collection (sorting)

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
		* Evaluate block preconditions based on predicate
	* Create elseif block(s) (elseif (...) { ... })
		* Determine predicate
		* Evaluate block preconditions (based on if/elseif predicates)
	* Create else block (else { ... })
		* Evaluate block preconditions (based on if/elseif predicates)
* Foreach
	* Create block (foreach (...) { ... })
		* Determine iterator
		* Determine item name
* For
	* Create block (for (...) { ... })
		* Determine initial conditions
		* Determine predicate
		* Determine afterthought (what to do at the end of an iteration)
* While
	* Create block (while (...) { ... })
		* Determine predicate
* Switch
	* Create block (switch (...) { ... })
		* Determine expression to evaluate
	* Create case block (case ...: { ... })
		* Determine predicate
* Function/Method
	* Create block (function X(...) { ... })
		* Determine identifier/name
		* Determine parameters

## Generalized tasks
From the list of tasks we've established so far, we can try to create a list of generalized tasks (operations that do the same thing under different contexts).

* Generate names (for functions/methods/classes/namespaces/variables)
* Type inference/manipulation
* Block localization (function/method/class)

## Task list execution
The execution of tasks as described earlier is most likely done through a while loop, in which the task to execute at any moment appears to be selected at random, such that the code would look something like

<pre><code class="language-php line-numbers">
while (programming) {
	switch (rand() % numberOfTasks) {
		// break; have been removed to better present the idea
		case 0: // task A
		case 1: // task B
		case 2: // task C
	}
}
</code></pre>


There's also likely to be some sort of evaluative loop that is assessing the code observed for things that will need to be done. In some sense, the internals of the programming loop is more likely to resemble a Markov decision process, where certain tasks are very likely to be executed just after a given task was executed (e.g. initializing a variable after it has been declared).

### Task stack
There is some aspect of programming that makes it look like a programmer is processing tasks from a call stack. For instance, initially his call/task stack will be empty. The first thing he will have to do is either to examine the code for things to do or improve, or look at an existing list of tasks.

When the programmer has found at least one task to work on (his stack not being empty anymore), he can then start working on this task. A complex task, which may have one or many sub-tasks, will then be decomposed into its more simpler tasks, which are stacked on the "work" stack from last task to first task, such that the top of the stack (and thus the next elected task) will be the first sub-task of the task that was initially started.

As the programmer progresses through a task assignment, he may encounter things that he did not expect: a missing function, the unexpected behavior of an existing function, the task being ill-defined or missing information, etc. This may cause the programmer to either drop the initial task completely from his task stack, or to stack on a new task which purpose is to resolve the current task issue.

In the ideal case, task decomposition and sub-task stacking occurs in a very natural way. In a less ideal way, a task is frequently interrupted by unexpected new tasks, which, instead of advancing the main task, add to the current workload of the programmer.

# Observation on the programming tasks
* Some tasks are incredibly easy to solve if you have complete freedom. For instance, if no constraint is applied for variable naming, then any string is valid as any other, as long as they do not overlap with existing variables. However, if you introduce naming conventions, or the more difficult task of assign a "proper" name to a variable, the difficulty of the task increases tremendously.
* Some tasks can only be defined using a high level description. One example of this is the translation of high level requirements into functional logic. This basically entails the search of one solution out of the solution space which fulfills the X different criteria at most (and not more).
* Programming cannot be self-contained. Programming is valuable only when it is associated with the modeling of something that is external to it; modeling the world. A program generator can create an infinite amount of programs, but they will all be meaningless as meaning is only attached to code by the programmer and its users.

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

# Ideas for programming assistants
* Define two procedures [@hewitt1975towards]:
	* One to implement the desired transformation
	* One to check if the transformation has in fact been accomplished
* If the programming assistant can aid expert programmers in demonstrating that two rather different implementations produce equivalent behavior, then we can be much more confident that the system will behave in a useful way

# Automated programming seen as a reinforcement learning problem
* The actions are to select which functions to call and which arguments to give these functions
	* More generally, the actions are to determine which grammatical construct to use
* The states are the different programs (complete/working or partial/non-working)
	* The state space can then be seen as transitions between partial programs and complete programs, which can then become partial again as a new function (with missing parameters) is added
* The reward signal is difficult to determine
	* Partial programs could be given either a negative reward or a zero reward
	* A positive reward is obviously given for the programs that do what we expect of them (given input-output examples)
	* Programs which are complete but do not accomplish what we expect of them are better than partial programs because they compile, however their value in solving the problem we want to solve is questionable
		* Based on RL, any of the states which are used to get from the initial state to an end of epoch state would have their value policy updated accordingly
	* Do we want the reward signal to be different for each program we want? If so, then it basically means the reward signal "is" the program
		* It would make more sense to have a reward signal which is based on the number of correct instances of a problem it can solve
* To simplify the search space, we assume that a program is constructed sequentially <tbc>(what did I mean by that?)</tbc>, which lets us avoid all the partial programs where we start by defining all the functions that will be called without defining their arguments
	* It would however be valuable to determine if this space could help reaching a solution faster/more efficiently

# Function rewriting/optimization
* Given a single function entry point
	* Find all function calls recursively
	* Merge all low level logic (no function call) into a single function
	* Restructure the code

# 2018-02-08
* Discover all existing classes, methods and functions
* Construct dependency graphs between classes, methods and functions
* Build flow graphs

* Follow the programmer through a programming assignment
	* Define the task to accomplish
		* Different flows depending on whether a task is a bug or a feature
	* Identify the existing features that will help in accomplishing the given task

* Bug
	* Reproduce the issue locally
	* Identify the source of the problem
	* Suggest a fix

* Feature
	* Define the missing functionalities
	* Implement the functionalities
		* Identify existing functionalities that may be reused

* "I need something that lets me add X"

# See also
* [Automated refactoring](../automated-refactoring/article.md)
* Program induction

## Papers
* [DeepCoder: Learning to Write Programs](../../machine-learning/papers/matej-balog-deepcoder-learning-to-write-programs/article.md)

# References
* https://en.wikipedia.org/wiki/Automatic_programming
* [Approaches to Automatic Programming](http://www.sciencedirect.com/science/article/pii/S0065245808605197)
* Green, Cordell, and David R. Barstow. [A Hypothetical Dialogue Exhibiting a Knowledge Base for a Program-understanding System](http://i.stanford.edu/pub/cstr/reports/cs/tr/75/476/CS-TR-75-476.pdf). Stanford, CA: Stanford University, 1975.
* Hewitt, Carl E., and Brian Smith. "Towards a programming apprentice." IEEE Transactions on Software Engineering 1 (1975): 26-45.
* Newell, Allen. [Report on a General Problem-solving Program](https://www.u-picardie.fr/~furst/docs/Newell_Simon_General_Problem_Solving_1959.pdf). Santa Monica, CA: Rand, 1959.
* Rich, Charles, and Richard C. Waters. "The Programmer's Apprentice: A research overview." Computer 21.11 (1988): 10-25.
* Data structure chooser - http://ds.shlegeris.com/
* Inductive programming - http://www.inductive-programming.org/
* Program transformation - http://www.program-transformation.org/
* Universal Data Structure - https://groups.google.com/forum/#!topic/magic-list/LhDuHtyas9Q
* https://sergeyzhuk.me/2018/12/29/code_review/
