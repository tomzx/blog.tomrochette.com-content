---
title: Flemming Nielson - Principles of Program Analysis (1999)
created: 2016-10-27
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview

# Notes
## Chapter 1 - Introduction
## 1.1 The Nature of Program Analysis
* One common theme behind all approaches to program analysis is that in order to remain computable (tractable?) one can only provide approximate answers
* In general, we expect the program analysis to produce a possibly larger set of possibilities than what will ever happen during execution of the program
* All program analyses should be semantics based: this means that the information obtained from the analysis can be proved to be safe (or correct) with respect to a semantics of the programming language
* Program analysis should not be semantics direct: this would mean that the structure of the program analysis should reflect the structure of the semantics

## 1.2 Setting the Scene
## Reaching Definitions Analysis
* An assignment (called a definition in the classical literature) of the form $[x := a]^\ell$ may reach a certain program point (typically the entry or exit of an elementary block) if there is an execution of the program where $x$ was last assigned a value at $\ell$ when the program point is reached

## Chapter 2 - Data Flow Analysis
* Classical data flow analyses:
	* Available expressions
	* Reaching definitions
	* Very busy expressions
	* Live variables

### Initial and final labels
* $init: \bf{Stmt \rightarrow Lab}$
	* Returns the initial label of a statement
* $final: \bf{Stmt \rightarrow \mathcal{P}(Lab)}$
	* Returns the set of final labels in a statement

### Blocks
* $blocks: \bf{Stmt \rightarrow  \mathcal{P}(Blocks)}$
	* Blocks is the set of statements, or elementary blocks
* $labels: \bf{Stmt \rightarrow  \mathcal{P}(Lab)}$
	* The set of labels occurring in a program
* $init(S) \in labels(S)$ and $final(S) \subseteq labels(S)$

### Flows and reverse flows
* $flow: \bf{Stmt \rightarrow \mathcal{P}(Lab \times Lab)}$
	* The set of couples representing transitions between labels
* $flow^R: \bf{Stmt \rightarrow \mathcal{P}(Lab \times Lab)}$
	* The reverse flow
	* $flow^R(S): \{(\ell,\ell') | (\ell',\ell) \in flow(S)\}$

### The program of interest
* $S_*$: the program that we are analysing
* $\bf{Lab_*}$: the labels ($labels(S_*)$) appearing in $S_*$
* $\bf{Var_*}$: the variables ($FV(S_*)$) appearing in $S_*$
* $\bf{Blocks_*}$: the elementary blocks ($blocks(S_*)$) occurring in $S_*$
* $\bf{AExp_*}$: the set of non-trivial arithmetic subexpressions in $S_*$. An expression is trivial if it is a single variable or constant

# See also

# Sources
* Nielson, Flemming, Hanne R. Nielson, and Chris Hankin. Principles of program analysis. Springer, 1999.