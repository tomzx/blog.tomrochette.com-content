---
title: Automated Test Generator
created: 2016-09-09
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore
* How to reflect on laravel-like proxy classes which can be mocked on demand?
* How do you represent knowledge such as $a === $b, or is_null($x) => true if $x is null
	* Is a lookup table good enough?

# Overview
* Specify extended class (defaults to \PHPUnit_Framework_TestCase)
* Setup mock dependencies with Mockery
	* Use reflection to discover classes to mock
* Expand function calls graphs (replace calls with corresponding tree)

* Generate case where each method argument is null
* Generate case for each if using mocked instances to generate the appropriate cases
* Generate case that throw exceptions

# Other
* Taint analysis data (sources, securing functions, sinks)

# Notes/Inspection
* We're concerned about branches/conditions
* We want to figure out the truth table -> branch in order to create a test for each branch
* Easiest cases are code with no conditions and dependency
* Anything that depends on the value of a returned function call must be investigated
* When testing a function or block, we are not concerned with callees, only what the return value might be (assume null or mixed in PHP)
* Functions cannot be mocked in PHP, which means that a function calling another function will require us to inject this function in the code in order to analyze it
* In the case we are calling mocked objects, and conditions depends on said mocked object, it is “easy” to produce the necessary value at the required time
* We need to be able to reason enough to know how to read protected/private variables during tests (know getter/setters)

* Phpstorm call a script on file save (generate test file for saved file)

# Analysis
## Blocks
### Code
```php
{

}
```

### Notes
* Depending on the language, the block should indicate that variables initialized within the block are scoped to this block, in other words, when we reach the end of the block, the variable is not available anymore
	* However, in languages like php, a variable is considered live until the end of the function, or if `unset()` was called with the variable as an argument

## Conditions
### Code
```php
if ($a === $b && $c === $d) {

}
```

### Notes
* Conditions can first be seen as true/false cases, which may hide more complex boolean logic

## Sequential conditions
### Code
```php
if ($a) {

}
if ($b) {

}
```

### Statements
| a | b |
|---|---|
| T | T |

### Branches
| a | b |
|---|---|
| T | T |
| F | F |

### Path
| a | b |
|---|---|
| F | F |
| F | T |
| T | F |
| T | T |

## Nested conditions
### Code
```php
if ($a) {
	if ($b) {

	}
}
```

### Statements
| a | b |
|---|---|
| T | T |

### Branches
| a | b |
|---|---|
| T | T |
| F | x |

As soon as `$a` is false, the value of `$b` does not matter.

### Path
| a | b |
|---|---|
| F | x |
| T | F |
| T | T |

As soon as `$a` is false, the value of `$b` does not matter.

## Loops
### Code
```php
for ($i = 0; $i < 100; ++$i) {

}

while (--$i) {

}

do {

} while (--$i);

foreach ($a as $b) {

}
```

### Notes
* Loops present a condition, and thus present the same challenges (sequential loops and nested loops)

## Functions
### Code
```php
function a() {
	b();
}

function b() {
	a();
}

function c() {
	c();
}
```

### Notes
*

# My testing process
* Select a class to create tests for
* Create a setUp method which will instantiate the class with the appropriate dependencies as mocks
* Enumerate all public methods
* Determinate all "manipulation" methods, that is, methods which can be used to alter the internal state of the object (generally setters)
* For each public method, inspect the internal working
	* For each condition in the execution of a public method, create 2 tests, one when it is true and one when it is false
	* When a mock function is called, expect (test) the given argument

## MVCSR architecture
## Model
* Mostly getter/setter logic
* Test default values (track changes)

## Controller
* Services dependencies are injected during the `setUp()`
* Should test the type of the returned data (view vs JSON)
* Should check the JSON top-level keys if an object is returned

## View
Not tested.

## Service
* Services and repositories dependencies are injected during the `setUp()`

## Repository
Not tested.

# Things to implement
* Control flow analysis
	* Control flow graph
* Data flow analysis
	* Data flow lattice/Variable reference graph
	* Forward analysis
		* Constant propagation
		* Available expressions
	* Backward analysis
		* Live variables analysis
		* Very busy expressions
* Abstract interpretation
* Variable reachability
* Call graph analysis
* Type safety check
* Dead assignments/unused code
* Security analysi
* Traces (show what variables look like given a specific case)
* Construct database (function, interface, class, trait, method, property, constant, variable)
* Array logic (implement reverse functions, some methods being very complicated to implement, such as the reverse to map/reduce)
* String logic (implement reverse functions)

## Very difficult
* Array logic
* String logic

# Coverage level
* $C_0$ Statement
* Segment
* $C_1$ Branch
* $C_{1p}$ Multiple condition
* $C_\infty$ Path

# To consider
* Exception handling
* Randomly generated data
* Time based data

# Things to test
* Null pointer exceptions
* Index out of bounds
* Stack overflow
* Branch never entered

# How do I?
## Set a condition to a desired truth value
* Find condition
* Create a truth table using all the expressions in the condition
* Build a data flow graph
* Find the flow of instructions using/assigning to variables in the condition from the function entry point to the condition
	* This may be quite difficult for objects as we may most likely need to find where we can inject values to set the class properties
* Use a SAT solver

## Cover all statements/branch/paths
* Find all conditions (that are expression driven, not based on constants)
* Depending on the level of coverage you want, generate appropriate condition values (true/false)
	* It may happen that some cases are impossible (dead code)
* In the simplest cases, the variables used in conditions are the parameters of the function and they are not modified in the path from the function entry point to the condition
* In more complicated cases, the variable gets modified in the path from the function entry point to the condition. It is then necessary to build the inverse function, such that given a truth value, we are given the parameter value to use

### Alternative
* Replace variable with expression

# Development iterations
* No loop support (only if/elseif/else, make sure that loops evaluate to false)
	* List all conditions
	* Trace all conditions
* Switch support
* Loop support (while/do/for)
	*
* Iterator support (foreach)

# Dependencies
* [PHPUnit](https://github.com/sebastianbergmann/phpunit)
* [Mockery](https://github.com/padraic/mockery)
* [nikic/PHP-Parser](https://github.com/nikic/PHP-Parser)

# See also
* [Automated programming](../automated-programming)
* [Automated refactoring](../automated-refactoring)

# Sources
* http://cseweb.ucsd.edu/classes/sp00/cse231/report/node13.html
* https://www.youtube.com/watch?v=8eZ8YWVl-2s
* https://www.youtube.com/watch?v=rKlHvAw1z50
* https://speakerdeck.com/schmittjoh/improving-code-quality-continuously