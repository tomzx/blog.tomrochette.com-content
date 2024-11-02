---
title: Constructing functions
created: 2016-08-18
taxonomy:
  tag: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview
Let's assume that all that is available to us to write a new function is a list of existing functions.

First we want look at parameterless functions.

<pre><code class="language-cpp line-numbers">
SomeType myFunction() {
	// ...
}
</code></pre>

A parameterless function can do three of the following things:
* Return data (an intrinsic value or some structure/object)
* Call other parameterless functions
* Call other functions with parameters by instantiating the required arguments internally through a call to other parameterless functions

## Return data (Instantiator)
<pre><code class="language-cpp line-numbers">
struct SomeType {
	int a;
	double b;
};

// Instantiator
SomeType myFunction() {
	SomeType c;
	c.a = 3;
	c.b = 3.1415;
	return c;
}
</code></pre>

* It can return consumable data
* It can instantiate static data

## Call other parameterless functions (Delegator)
<pre><code class="language-cpp line-numbers">
// Instantiator
SomeType myOtherFunction() {
	// ...
}

// Delegator
SomeType myFunction() {
	return myOtherFunction();
}
</code></pre>

Overall, the "functions" of such a function are:
* Encapsulating functions ($f() = g()$)
* Encapsulating sequence of functions ($f() = g(),h(),i()$)
* Function composition/Chaining functions calls ($f = g \circ h \circ i = g(h(i()))$)
<!-- TODO: This is not the proper way to write that a given function calls itself n times -->
* Recursive function calls ($f = f^n$, $f = \circ^n f$ ,$f = \underbrace{f \circ f \circ \dots \circ f}_{n}$)

## Call other functions with parameters
<pre><code class="language-cpp line-numbers">
// Instantiator
int myIntFunction() {
	return 3;
}

// Instantiator/Mutator
SomeType myOtherFunction(int x) {
	// ...
}

// Delegator/Chainer
SomeType myFunction() {
	int x = myIntFunction();
	return myOtherFunction(x);
}
</code></pre>

Here we observe that calling functions with parameters only amounts to calling the appropriate instantiator and passing the result to the function expecting an argument.

We can consider the following program

<pre><code class="language-cpp line-numbers">
SomeType myOtherFunction(int x) {
	// ...
}

SomeType myFunction() {
	return myOtherFunction(3);
}
</code></pre>

to be convertible into

<pre><code class="language-cpp line-numbers">
int myIntFunction() {
	return 3;
}

SomeType myOtherFunction(int x) {
	// ...
}

SomeType myFunction() {
	int x = myIntFunction();
	return myOtherFunction(x);
}
</code></pre>

# See also

# References
