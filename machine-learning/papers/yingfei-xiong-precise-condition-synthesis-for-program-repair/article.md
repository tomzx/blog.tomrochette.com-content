---
title: Yingfei Xiong - Precise Condition Synthesis for Program Repair (2017)
created: 2018-02-17
taxonomy:
  tag: [machine learning]
  status: finished
---

## Context

## Learned in this study
* Most errors are fixed by exception-throwing, then value-returning, then by narrowing

## Things to explore
* Tested only against 4 of the 6 projects of Defects4J, is it to have good results to show?
	* I'm skeptical because they take to mention that the precision/recall is the best reported so far...
* Given the low amount of generated fixes, I feel like many of the results (such as claiming that document analysis is useful because it has prevented 1 incorrect patch) might not be statistically significant
* Using a simple mechanism to introduce known errors into programs (mutations), it would have been possible to generate a much larger test set, albeit not necessarily a realistic one

# Overview

# Notes
## Abstract
* Three key insights
	* It is important to know what variables in a local context should be used in an "if" condition
	* The API documentation can be used to guide the repair process
	* It is important to know what predicates should be performed on the set of variables

## I. Introduction
* Most techniques (of automatic program repair) generate a patch for a defect aiming at satisfying a specification
* A patch that passes all tests is known as a plausible patch
* We use precision to refer the proportion of defects correctly fixed by the first plausible patch among all plausibly fixed defects
* The reason for low precision is that correct patches are sparse in the spaces of repair systems, while plausible ones are relatively much more abundant
* A fundamental way to address this problem is to rank the patches by their probabilities of being correct, and return the plausible patch with the highest probability, or report failure when the highest probability is not satisfactory
* Different approaches
	* Rank the patches using models learned from existing patches
	* Rank the patches by their distance from the original program
	* Rank the patches by their statistical correlation with the expected results
* An important reason for this imprecision, as we conjecture, is that the existing ranking approaches are too coarse-grained. The existing approaches cannot distinguish many common plausible "if" conditions from the correct condition, and will give them the same rank
* Condition synthesis has been used in several existing repair systems and is shown to be one of the most effective techniques
* Our approach combines three heuristic ranking techniques that exploit the structure of the buggy program, the document of the buggy program, and the conditional expressions in existing projects
* We view the condition synthesis as two steps
	* Variable selection: deciding what variables should be used in the conditional expression
	* Predicate selection: deciding what predicate should be performed on the variables
* Three techniques for ranking variables and predicates
	* Dependency-based ordering: The more recent a variable in a topological ordering of dependency is, the more likely it will be used in a conditional expression
	* Document analysis: When variables are mentioned in the javadoc, we restrict the selection to only the mentioned variables
	* Predicate mining: We mine predicates from existing projects, and sort them based on their frequencies in contexts similar to the target condition

### III. Approach
#### A. Overview
* The first type is to directly return the oracle (expected value/exception)
* We first identify the last executed statement $s$ in the failed test, and then insert one of the following statement before $s$ to prevent the failure
	* Value-Returning: if (c) return v;
	* Oracle-Throwing: if (c) throw e;
* When the failed test expects a return value, value-returning is used, otherwise oracle-throwing is used
* v or e is the expected return value or exception, and c is the synthesized condition
* We use heuristic rules to check whether the synthesized c is a boundary check, and discard the patch if it is not a boundary check
* We always insert before the last executed statement because, if the defect leads to crash, for example, the program fails to check a null pointer, we usually need to place the guarded return statement right before the crashed statement
* The second type is the modification of an existing condition
* We first locate a potentially faulty "if" condition c', and then apply one of the following modifications based on the result of predicate switching
	* Widening: if (c') => if (c' || c)
	* Narrowing: if (c') => if (c' && !c)
* If predicate switching negates the original condition from true to false, we apply the narrowing template, otherwise we apply the widening template

#### B. Returning the Oracle
##### Extracting the Oracle
* To extract a functional oracle, we first identify the related pieces of code by performing slicing
* We first perform backward slicing from the oracle expression (the oracle slice), then perform backward slicing from the test input arguments (the input slices), and subtract the input slices from the oracle slice
* Finally, we rename the variables representing the test input arguments to the formal parameter names of the target method

#### C. Variable Ranking
##### Preparing Candidate Variables
* Four types of variables
	* local variables
	* method parameters
	* this pointer
	* expressions used in other "if" conditions in the current method

###### Sorting by Dependency
* To sort the variables, we create a dependency graph between variables
	* The nodes are variables, the edges are dependency relations between variables
* The following types of intra-procedural dependencies are considered
	* Data dependency: Given an assignment statement x = exp, x depends on all the variables in exp
	* Control dependency: Given a conditional statement such as if (cond) { stmts } else { stmts' }, or while (cond) { stmts }, all variables assigned in stmts ans stmts' depend on variables in cond
* Then we perform a topological sorting to ensure the most dependent variables are sorted first
* First collapse all cycles into a node containing multiple variables
* Then identify the nodes with no incoming edges and give them priority 0
* Remove these variables and their outgoing edges from the graph
* We identify the nodes with no incoming edges and give them priority 1 (then repeat)
* There may be multiple variables with the same priority
* We further sort the variables by distance between the potentially faulty condition and the assignment statement that initializes the variable

#### D. Predicate Ranking
##### Mining Related Conditions
* Given a repository of software projects, we first collect the conditional expressions that are in a similar context to the conditional expression being synthesized
* We use variable type, variable name, and method name to determine a context
* We say two variables or methods names are similar if we decompose the names by capitalization into two sets of words, the intersection of the two sets are not empty
* We say a variable name is meaningful if its length is longer than two
* Assuming we are synthesizing a condition c with variable x in the method m
	* A conditional expression c' is considered to be in a similar context of c, if
		* it contains one variable x'
		* x' has the same type as x
		* the name of x' is similar to x when the name of x is meaningful, or the name of the method surrounding c' is similar to m when the name of x is not meaningful
* GitHub search engine is used to search for existing source code

# See also

# References
* Xiong, Yingfei, et al. "Precise condition synthesis for program repair." Proceedings of the 39th International Conference on Software Engineering. IEEE Press, 2017.
