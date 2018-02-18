---
title: Yingfei Xiong - Precise Condition Synthesis for Program Repair (2017)
created: 2018-02-17
taxonomy:
  category: [Machine Learning]
  status: in progress
---

## Context

## Learned in this study

## Things to explore
* Tested only against 4 of the 6 projects of Defects4J, is it to have good results to show?
	* I'm skeptical because they take to mention that the precision/recall is the best reported so far...

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

# See also

# References
* Xiong, Yingfei, et al. "Precise condition synthesis for program repair." Proceedings of the 39th International Conference on Software Engineering. IEEE Press, 2017.