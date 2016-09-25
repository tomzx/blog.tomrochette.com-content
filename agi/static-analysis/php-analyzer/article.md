---
title: PHP Analyzer
created: 2016-09-22
taxonomy:
  category: [PHP]
  status: in progress
---

## Context
I've come to reason that if I can reason about a program in any language, a computer should be able to do as such. Obviously, this implies and requires a lot of acquired knowledge over time, and in particular, the peculiarities of a given language.

As I've been a PHP developer over many years, I decided to look into the currently available open source on the topic of static code analysis, particularly oriented toward control flow analysis, data flow analysis, and potentially the ability to reason about a piece of code in order to prevent bugs and, tentatively, to automate the process of unit testing.

This analysis is based on [the legacy branch of PHP Analyzer, commit 896beb2d70](https://github.com/scrutinizer-ci/php-analyzer/commit/896beb2d70e05c438b539d507367ffaeed8969b1).

## Learned in this study

## Things to explore
* Describe the technique used to extract the data of interest during a pass

# Overview
* A run command
	* An analyzer which contains a pass config
		* A list of passes to be executed
		* There are 4 passes type
			* Initializing
			* Analysing
			* Reviewing
			* Fixing
	* The analysis consist of running each pass over all the given files

# Pass analysis
The passes do the following...

## Initializing
### TypeScanningPass
Finds all classes/interfaces/traits and add them to the registry. Find all functions and add them to the registry.

#### Uses
* [Comment parser](#comment-parser)
* [Class parser](#class-parser)
* [Function parser](#function-parser)

### TypeInferencePass
Builds a control flow graph (through control flow analysis) (intraprocedural) for each scope level. Using this CFG, we then go through a data analysis pass where we build a lattice that will represent the variables and their type at a given point in the code, given the paths that were taken.

#### Uses
* [Type registry](#type-registry)
* [Semantic reverse abstract interpreter](#semantic-reverse-abstract-interpreter)
* [Function interpreter](#function-interpreter)
* [Class interpreter](#class-interpreter)
* [Comment parser](#comment-parser)
* [Scope creator](#scope-creator)
* [Control flow analysis](#control-flow-analysis)
* [Type inference (data flow analysis)](#type-inference)

### MarkPassedByRefArgsPass
Based on the called function signature, annotates a function argument to indicate whether it is passed by reference or not. This is useful to determine whether a variable can be modified when passed as reference (mostly interesting for non-object types).

#### Uses
* [Type registry](#type-registry)

### VariableReachabilityPass
Computes the nodes that may/must be providing values to the node being examined.

The "maybe" cases are based on branches, initial variables and loops. In different branches, variables may be assigned different values, and thus code after the if/else has executed may depend on which branch was executed. In loops, a variable is generally initialized and used as a condition to terminate the loop. As the loop progresses, this variable's value might have come from the initialization or the update step.

The "must" cases are the linear cases, in other words, any sequence of code (no branches/loops).

#### Uses
* [Control flow analysis](#control-flow-analysis)
* [MayBeReachingUse Analysis](#maybereachinguse-analysis)
* [MustBeReachingDef Analysis](#mustbereachingdef-analysis)

### ReturnTypeScanningPass
Scans only functions and methods in order to determine the type of returned values. If no return is explicitly defined, returns null. Constructs a union of all type potential types that could be returned by the analyzed function/method.

#### Uses
* [Type registry](#type-registry)

### InferTypesFromDocCommentsPass
For any types that could not be inferred through code analysis (e.g., because the type was not specified in the function parameters), the php doc blocks are read in attempt to assign types to parameters and the return type of the function.

#### Uses
* [Type registry](#type-registry)
* [Comment parser](#comment-parser)

### CallGraphPass
Build a call graph (interprocedural) between functions/methods (what calls what).

#### Uses
* [Type registry](#type-registry)

## Analyzing
### CheckParamExpectsRefPass

## Reviewing
### CheckstylePass

### CheckUnreachableCodePass

### CheckAccessControlPass

### CheckForTyposPass

### CheckVariablesPass

### SuspiciousCodePass

### DeadAssignmentsDetectionPass

### VerifyPhpDocCommentsPass

### LoopsMustUseBracesPass

### CheckUsageContextPass

### CheckParamExpectsRefPass

### SimplifyBooleanReturnPass

### PhpunitAssertionsPass

### ReflectionUsageCheckPass

### PrecedenceChecksPass

### CheckBasicSemanticsPass

## Fixing
### DocCommentFixingPass

### ReflectionFixerPass

### UseStatementFixerPass

# Components
## Comment parser

## Class parser

## Function parser

## Type registry

## Semantic reverse abstract interpreter

## Function interpreter

## Class interpreter

## Scope creator

## Control flow analysis

## Type inference

## MayBeReachingUse analysis

## MustBeReachingDef Analysis

# Hierarchy
* DataFlow Analysis
![DataFlow Analysis](./assets/images/DataFlowAnalysis.png)

# See also

# Sources
* [PHP Analyzer](https://github.com/scrutinizer-ci/php-analyzer/tree/legacy)
* [Scrutinizer-ci documentation on PHP Analyzer](https://scrutinizer-ci.com/docs/tools/php/php-analyzer/)