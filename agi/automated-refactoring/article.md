---
title: Automated refactoring
created: 2016-06-03
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore
* Abstraction level assignment ((semi-)automatically assign an abstract level to a function such that abstraction levels are respected, use similar abstraction levels in a function)

# Overview
One of the goal of code refactoring is to reduce the amount of duplicated code such that it is easier to make changes in a single place rather than make the same change at multiple places.

Another goal of refactoring is to promote code reuse and abstraction.

As a software project matures, its low level functions should require to be changed rarely while higher level features relying on those lower level functions change more often. This would be similar to assembly language changing very rarely compared to higher level languages.

## Standard operations
* Remove deprecated code
* Update code relying on deprecated/obsolete APIs
* Simplify logic

## Classical refactoring methods
* Extract method
* Pull up method
* Form template method
* Substitute algorithm

## Regular refactoring
* Pyramid logic to precondition testing
* Extraction of repetitive conditions
* Restructuring of a function into multiple functions (convert a 100 lines function into 20x 5 liners)
	* The difficulty here is to give significative name to the newly created functions
* Abstract existing code through parameter instantiation (pass a parameter instead of using a hardcoded value)

# See also
* Clone detection

# Sources
