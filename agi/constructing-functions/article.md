---
title: Constructing functions
created: 2016-08-18
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview
Let's assume that all that is available to us to write a new function is a list of existing functions.

First we want look at parameterless functions.

```cpp
SomeType myFunction() {
	// ...
}
```

A parameterless function can do three of the following things:
* Return data (an intrinsic value or some structure/object)
* Call other parameterless functions
* Call other functions with parameters by instantiating the required arguments internally through a call to other parameterless functions

## Return data (Instantiator)
```cpp
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
```

* It can return consumable data
* It can instantiate static data

## Call other parameterless functions (Delegator)
```cpp
// Instantiator
SomeType myOtherFunction() {
	// ...
}

// Delegator
SomeType myFunction() {
	return myOtherFunction();
}
```

Overall, the "functions" of such a function are:
* Encapsulating functions ($f() = g()$)
* Encapsulating sequence of functions ($f() = g(),h(),i()$)
* Function composition/Chaining functions calls ($f = g \circ h \circ i = g(h(i()))$)
* Recursive function calls ($f = f^n$)

## Call other functions with parameters
```cpp
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
```

Here we observe that calling functions with parameters only amounts to calling the appropriate instantiator and passing the result to the function expecting an argument.

We can consider the following program

```cpp
SomeType myOtherFunction(int x) {
	// ...
}

SomeType myFunction() {
	return myOtherFunction(3);
}
```

to be convertible into

```cpp
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
```

# See also

# Sources