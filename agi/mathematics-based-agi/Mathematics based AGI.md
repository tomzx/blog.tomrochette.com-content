# Mathematics based AGI

## Learned in this study

## Things to explore

# Overview

As human beings in relatively well educated societies, we're taught early on about mathematics. We're taught about numbers and how they relate to one another, how to manipulate them, transform them and use them to solve complex problems.

One of the fundamental tools we're presented is `functions`. Functions allows us to transform a set of values (called `domain`) into a second set of values (called `image`).

Functions are easy to think about and are a powerful tool as well. Through an equation, is it possible to express a table of possibly an infinite amount of domain -> image relations.

| x | y |
|---|---|
| 0 | 1 |
| 1 | 2 |
| ... | ... |
| n | n+1 |

This simple relation can be represented with the equation y = x + 1. With that equation, it is possible to represent a relation over an infinite amount of integers. Thus, we could say that we have reduced the space of all integers over all integers + 1 using a single equation composed of 5 symbols.

In this sense, we can say that functions are generators, in the sense that they are not values until you replace the variables that they contain. Once you do fill out the variables and generate solutions, you are increasing your "generated solution space".

Since functions allow us to express the relations between two sets much more concisely than by enumerating each and every possible case, it means that is must be an important tool in our toolbox for summarizing data sets.

Much like lossy compression, functions can be approximated with a certain degree of error. Using approximation allows us to have better compression through generalization at the cost of a higher rate of error.

One can consider a function as two different things:

1. A transformation of inputs into outputs
2. A sequence of transformations applied on the initial output, where the output are assigned to internal variables and possibly transformed by other functions within the initial function (functions calling functions)

## Notes

Much of machine learning is geared toward fitting a given function as closely as possible without under/over-fitting the function in question.
