---
title: Mathematics based AGI
created: 2015-08-21
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

* Consider getting an optimal AGI as an optimization in itself (gradient descent)

# Overview

# Functions

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

# Integer-based reasoning

Concepts are basically numbers
Everything can be represented by a number (basically the concept of primary key -> set of data)
We learn to associate images, sounds, experiences (samples) with a specific concept (number)

# Logic/Rule-based AGI
Conjecture: An AGI can be built from the composition of millions of rules (if-then constructs)
* How to efficiently pick the appropriate rules to execute?
Context
* How to pick the appropriate context?
Rules that define the presence of a context
* How are rules composed?
Small programs which can evaluate things at time t
* How are rules generated?
Trial and error (random) then guided by previous successes
* How to evaluate success/failure?
Observe others successful at the task and derive one or many metrics/evaluation functions
* How do you find appropriate examples of success?
Either the task we want to improve came from observing others (thus we were provided with initial examples) or we want to learn about the rules of a specific domain (which are to be determined)

## Structures for efficient selection of rules
Rules are decomposed into their parts, each part is a key in a dictionary such that when a part is triggered, its corresponding rules are fetched and readied to be intersected with the next triggered part

## Notes

Much of machine learning is geared toward fitting a given function as closely as possible without under/over-fitting the function in question.

## Reasoning on AGI
Given that programs are part of the integer space (with length in the same space), one can be certain that a program within this infinite space will be considered an AGI. It is highly likely that many such programs exists. In fact, if one such program exist, an infinity of its variants will exist as well (longer programs containing this "seed AI").

If we accept this as a fact, then the obvious next question is "what is the length of this shortest seed AGI?" The answer is likely to be platform specific. For instance, our DNA is believed to be the equivalent to nature's AGI program. DNA is itself about 3 billion nucleotides. As there are 4 valid nucleotides/bases, there are $(2^2)^{(3 \times 10^9)}$ possible combinations/programs, a single program being approximately 6 Gbits or 750 MBytes. What those 750 MB of data allow us to do is to construct a huge variety of cells/proteins that end up having lives of their own.

If we take this amount of information as a basis to determine the size of a potential AGI, we have to ask ourselves if what we "really" need is a subset of this information, or all if it is needed. In the former case, then we can hope to reduce our search space possibly considerable, in the latter, it means that we at least have an upper bound for something that should produce human-like intelligence levels.

This "upper bound" or threshold has a couple of interesting properties. Let's consider the smallest AGI being a program of length $l$. This means that for all programs $p$ smaller than $l$, in other words $L(p) < l$ (where $L(p)$ is the length of program $p$), the probability that we execute a program $p_{AGI}$ that is AGI is $P(\mathrm{p\ exhibits\ AGI}|L(p) < l) = 0$, in other word we will at best observe sub-AGI intelligence but not AGI itself.

On the other hand, for any program larger or equal to $l$, we may assume that it is sufficient for a program $p$ to contain the program $p_{AGI}$ somewhere in its string definition. In other terms, if this program $p$ contains the substring (from index $a$ to $b$) $p_{a,b}$ that is the AGI program $p_{AGI}$, in other words $p_{a,b} = p_{AGI}$, then  $P(\mathrm{p\ exhibits\ AGI}|L(p_{a,b}) \ge l)) =\ ?$.

What is the probability of finding an AGI program?
* function of AGI length
* Alphabet $A$ of $s$ symbols
* $l = L(p_{AGI})$ length of the smallest AGI
* how many programs of length $L(p)$? $s^{L(p)}$ 
* $s^{L(p_{a,b})}$ number of programs of length $L(p_{a,b})$
* $P(\mathrm{p\ exhibits\ AGI}|L(p_{a,b}) = l)) = \frac{1}{s^{L(p_{a,b})}} = \frac{1}{s^{L(p_{AGI})}} =  \frac{1}{s^l}$
* $p_{x,y}$ contains $p_{a,b} = p_{AGI}$, thus $L(p_{x,y}) \ge L(p_{AGI})$
* for a program $p_{x,y}$ one symbol longer than $p_{a,b}$ 
	* $s$ programs with prefix $p_{a,b}$
	* $s$ programs with suffix $p_{a,b}$ (same as prefix)
	* when the length difference $d$ increases, then we have permutations (where X is any symbol of the alphabet):
		* length 2 XX_, X_X, _XX => $3s^2$
		* length 3 XXX_, XX_X, X_XX, _XXX => $4s^3$
		* length n => $(n+1)s^n$
* $L_{p \to AGI} = L(p_{x,y}) - L(p_{AGI})$ the length difference between a program $p_{x,y}$ longer than $p_{AGI}$
* for $s > 1$ and $l = L(p_{AGI}) > 1$, (something is not right with this equation as the probability can go over 1 if $L(p_{x,y}) >s^{L(p_{AGI})}$)
$$\begin{split}
P(\mathrm{p\ exhibits\ AGI}|L(p_{x,y}) > l)) &= (L_{p \to AGI} + 1) \times \frac{s^{L_{p \to AGI}}}{s^{L(p_{x,y})}} \\
&= [L(p_{x,y}) - L(p_{AGI}) + 1] \times \frac{s^{L(p_{x,y}) - L(p_{AGI})}}{s^{L(p_{x,y})}} \\
&= [L(p_{x,y}) - L(p_{AGI}) + 1] \times \frac{s^{L(p_{x,y})} \times s^{-L(p_{AGI})}}{s^{L(p_{x,y})}}  \\
&= \frac{L(p_{x,y}) - L(p_{AGI}) + 1}{s^{L(p_{AGI})}} \\
\end{split}$$

Thus, the larger the smallest AGI program is, the more difficult it is to find it in the solution space. Another obvious conclusion is that as the program $p$ length tends to infinity, the probability it contains the AGI program increases to almost 100% certainty, $P(\mathrm{p\ exhibits\ AGI}|\lim_{(y-x) \rightarrow \infty}L(p_{x,y})) \approx 1$.

# See also
* [Observations on DNA](observations-on-dna)

# Sources
