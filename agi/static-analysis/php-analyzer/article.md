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
* [Class parser](#class-parser)
* [Comment parser](#comment-parser)
* [Function parser](#function-parser)

### TypeInferencePass
Builds a control flow graph (through control flow analysis) (intraprocedural) for each scope level. Using this CFG, we then go through a data analysis pass where we build a lattice that will represent the variables and their type at a given point in the code, given the paths that were taken.

#### Uses
* [Class interpreter](#class-interpreter)
* [Comment parser](#comment-parser)
* [Control flow analysis](#control-flow-analysis)
* [Function interpreter](#function-interpreter)
* [Scope creator](#scope-creator)
* [Semantic reverse abstract interpreter](#semantic-reverse-abstract-interpreter)
* [Type inference (data flow analysis)](#type-inference)
* [Type registry](#type-registry)

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
* [Comment parser](#comment-parser)
* [Type registry](#type-registry)

### CallGraphPass
Build a call graph (interprocedural) between functions/methods (what calls what).

#### Uses
* [Type registry](#type-registry)

## Analyzing
### CheckParamExpectsRefPass
Verifies that functions expecting a reference are indeed called with an argument that can be used as a reference.

#### Uses
* [Type registry](#type-registry)


## Reviewing
### CheckstylePass
Does basic style checks such as curly braces placement and name format for local variables, interfaces, classes, methods, functions, properties, etc.

### CheckUnreachableCodePass
Given a control flow graph, determines which nodes can/cannot be reached using fixed point graph traversal.

Appears to be inspired by [Google closure compiler fixed point graph traversal](https://github.com/google/closure-compiler/blob/master/src/com/google/javascript/jscomp/graph/FixedPointGraphTraversal.java).

#### Uses
* [Control flow analysis](#control-flow-analysis)

### CheckAccessControlPass
For all classes properties that are being accessed, determine whether the access is correct for the given context. Public properties are always accessible, protected properties are accessible from the declaring class and all descendants and private properties are only accessible from within the class (or trait).

#### Uses
* [Type registry](#type-registry)

### CheckForTyposPass
For all property fetch, static call or method call, we check if the given name exist, and if it does not, then a name fix is suggested (name similarity is computed using [similar_text](http://php.net/manual/en/function.similar-text.php) .

#### Uses
* [Type registry](#type-registry)

### CheckVariablesPass
Verifies the presence of a variable definition before it is being used.

### SuspiciousCodePass
Inspects the code in order to find common code constructs that leads to errors:

* Empty catch blocks without comment
* Fall-through switch cases without comment
* Assignment of null return value (no return value in called function)
* InstanceOf with non-existent class
* Catch block with non-existent class
* Overriding closure use (variable not used as reference)
* Use statement alias conflict

#### Uses
* [Type registry](#type-registry)

### DeadAssignmentsDetectionPass
Detects variables to which a value is assigned, but which are never used afterward.

See [Live variable analysis](https://en.wikipedia.org/wiki/Live_variable_analysis).

#### Uses
* [Control flow analysis](#control-flow-analysis)
* [LiveVariables Analysis](livevariables-analysis)

### VerifyPhpDocCommentsPass
Analyzes functions and methods phpdoc blocks to make sure their params and return types are correctly defined and specific enough.

#### Uses
* [Comment parser](#comment-parser)
* [Type registry](#type-registry)

### LoopsMustUseBracesPass
A very basic, token stream based, analyzer that verifies that loops are always constructed with their block defined with braces.

### CheckUsageContextPass
Verifies that usage of a function or variable is appropriate given the context.

* Method calls on non-objects (null)
* Foreach expression is traversable
* Foreach variable as reference is valid reference
* Missing argument on function/method calls
* Argument type check

#### Uses
* [Argument checker](#argument-checker)
* [Type checker](#type-checker)
* [Type registry](#type-registry)

### SimplifyBooleanReturnPass
Attempts to simplify "simple" boolean expressions (`if ($x) { return true } else { return false; }`).

### PhpunitAssertionsPass
Analyzes PHPUnit specific code in order to suggest more specific assertion functions to use.

#### Uses
* [Type registry](#type-registry)

### ReflectionUsageCheckPass
Analyzes `Reflection`-classes specific code due to issues present in PHP.

#### Uses
* [Type registry](#type-registry)

### PrecedenceChecksPass
Analyzes expressions which contain multiple expressions in order to avoid precedence issues.

* Assignments in conditions
* Comparisons with bit operations

### CheckBasicSemanticsPass
Verifies that a class with declared methods as abstract are declared as abstract or suggests that the modifier be removed or the method be implemented.

#### Uses
* [Type registry](#type-registry)

## Fixing
### DocCommentFixingPass
.

### ReflectionFixerPass
.

### UseStatementFixerPass
.

# Components
## Comment parser
.

## Class parser
.

## Function parser
.

## Type registry
.

## Semantic reverse abstract interpreter
.

## Function interpreter
.

## Class interpreter
.

## Scope creator
.

## Control flow analysis
.

## Type inference
.

## MayBeReachingUse analysis
.

## MustBeReachingDef analysis
.

## LiveVariables analysis
.

## Type checker
.

## Argument checker
.

# Hierarchy
## DataFlow Analysis
![DataFlow Analysis](./assets/images/DataFlowAnalysis.png)

# See also

# Sources
* [PHP Analyzer](https://github.com/scrutinizer-ci/php-analyzer/tree/legacy)
* [Scrutinizer-ci documentation on PHP Analyzer](https://scrutinizer-ci.com/docs/tools/php/php-analyzer/)