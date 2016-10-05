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

## Cases
### Block
```php
{

}
```

* Depending on the language, the block should indicate that variables initialized within the block are scoped to this block, in other words, when we reach the end of the block, the variable is not available anymore
	* However, in languages like php, a variable is considered live until the end of the function, or if `unset()` was called with the variable as an argument

### Conditions
```php
if ($a === $b && $c === $d) {

}
```

* Conditions can first be seen as true/false cases, which may hide more complex boolean logic

### Function
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

*

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
* Abtract interpretation
* Variable reachability
* Call graph analysis
* Type safety check
* Dead assignments/unused code
* Security analysi
* Traces (show what variables look like given a specific case)
* Construct database (function, interface, class, trait, method, property, constant, variable)

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
* Use a SAT solver

# Dependencies
* [PHPUnit](https://github.com/sebastianbergmann/phpunit)
* [Mockery](https://github.com/padraic/mockery)
* [nikic/PHP-Parser](https://github.com/nikic/PHP-Parser)

# See also

# Sources
* http://cseweb.ucsd.edu/classes/sp00/cse231/report/node13.html
* https://www.youtube.com/watch?v=8eZ8YWVl-2s
* https://www.youtube.com/watch?v=rKlHvAw1z50
* https://speakerdeck.com/schmittjoh/improving-code-quality-continuously