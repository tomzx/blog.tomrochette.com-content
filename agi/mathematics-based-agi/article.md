---
title: Mathematics based AGI
created: 2015-08-21
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study
* Much of machine learning is geared toward fitting a given function as closely as possible without under/over-fitting the function in question.

## Things to explore
* Consider getting an optimal AGI as an optimization in itself (gradient descent)
* A lot of the reasoning about AGI in the "Reasoning about AGI" seems also to relate to the idea of genetically engineered functionalities, where under a certain length no functionality exists
	* This also seems to match the idea of Turing where certain things only emerge after a certain size
* Is the DNA/genome the same length for all individuals?
	* If it is the case
		* How is that possible?
		* Why does it have to be the exact same length?
	* If it is not the case
		* What is the impact of the missing/added parts?

# Overview

# Functions
As human beings in relatively well educated societies, we're taught early on about mathematics. We're taught about numbers and how they relate to one another, how to manipulate them, transform them and use them to solve complex problems.

One of the fundamental tools we're presented are `functions`. Functions allow us to transform a set of values (called `domain`) into a second set of values (called `image`).

Functions are easy to think about and are a powerful tool as well. Through an equation, is it possible to express a table of an infinite amount of `domain` $\rightarrow$ `image` relations.

| x | y |
|---|---|
| 0 | 1 |
| 1 | 2 |
| ... | ... |
| n | n+1 |

This simple relation can be represented with the equation y = x + 1. With that equation, it is possible to represent a relation over an infinite amount of integers (or reals). Thus, we could say that we have reduced the space of all integers over all integers + 1 using a single equation composed of 5 symbols.

In this sense, we can say that functions are generators, in that they are not values until you replace the variables that they contain. Once you do fill out the variables and generate solutions, you are increasing your "generated solution space".

Since functions allow us to express the relations between two sets much more concisely than by enumerating each and every possible case, it means that is must be an important tool in our toolbox for summarizing data sets.

Much like lossy compression, functions can be approximated with a certain degree of error. Using approximation allows us to have better compression through generalization at the cost of a higher rate of error.

One can consider a function as two different things:

1. A transformation of inputs into outputs
2. A sequence of transformations applied on the initial output, where the output are assigned to internal variables and possibly transformed by other functions within the initial function (functions calling functions)

# Integer-based reasoning
Concepts are basically numbers
Everything can be represented by a number (basically the concept of primary key $\rightarrow$ set of data)
We learn to associate images, sounds, experiences (samples) with a specific concept (number)

# Logic/Rule-based AGI
Conjecture: An AGI can be built from the composition of millions of rules (if-then constructs).

This conjecture is based on the idea that anything can be reduced to a string of yes/no (if/then) questions being answered. For instance, to construct this sentence, given the space of lowercase/uppercase letters, we'd have 26 + 26 options to go through each time we'd want to select a letter. This in turn would amount to doing a binary search within this alphabet tree to pick the appropriate letter.

But to simplify our thinking, it's easier to think of question spaces. If we want to do a given action, then we have to enter the appropriate question space, which then has the appropriate questions to answer. Thus, as a whole, the process is always about answering yes/no, but through a higher level layer, it is simpler to think of just picking the right set of questions and computing the appropriate answers. In the end, these values are yes/no (binary).

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
If no observations are available, consider success as being something different than the last state and failure as staying in the same state. Success/failure is determined by the agent's own sense of value, which may sometimes be controlled by a process similar to reinforcement learning, where certain things make the agent feel worse/better
* How do you find appropriate examples of success?
Either the task we want to improve came from observing others (thus we were provided with initial examples) or we want to learn about the rules of a specific domain (which are to be determined)

## Structures for efficient selection of rules
Rules are decomposed into their parts, each part is a key in a dictionary such that when a part is triggered, its corresponding rules are fetched and readied to be intersected with the next triggered part

## Reasoning on AGI
Given that programs are part of the integer space (with length in the same space), one can be certain that a program within this infinite space will be considered an AGI. It is highly likely that many such programs exists. In fact, if one such program exist, an infinity of its variants will exist as well (longer programs containing this "seed AI"). Assuming that programs with this seed AI code can also exhibit the same functionality, the previous assumption can hold. Otherwise, it means that even though the seed AI code is present within the program's string, it cannot be activated. For example, given a C program that is a seed AI, any junk at its beginning or end may render the program uncompilable. For the sake of analysis, we'll prefer to work within a language that considers this seed AI string as active wherever it is found.

If we accept that "a seed AI program exists" as a fact, then the obvious next question is "what is the length of this shortest seed AGI?" The answer is likely to be language specific. For instance, our DNA is believed to be the equivalent to nature's AGI program. DNA is itself about 3 billion nucleotides. As there are 4 valid nucleotides/bases, there are $(2^2)^{(3 \times 10^9)}$ possible combinations/programs, a single program being approximately 3 [Gbases](https://en.wiktionary.org/wiki/gigabase), 6 Gbits or 750 MBytes. What those 750 MB of data allow us to do is to construct a huge variety of cells/proteins that end up having lives of their own.

If we take this amount of information as a basis to determine the size of a potential human-like AGI, we have to ask ourselves if what we "really" need is a subset of this information, or all of it is needed. In the former case, then we can hope to reduce our search space  considerably, in the latter, it means that we at least have an upper bound for something that should produce human-like intelligence levels.

This "upper bound" or threshold has a couple of interesting properties. Let's consider the smallest AGI being a program of length $l$. This means that for all programs $p$ smaller than $l$, in other words $|p| < l$ (where $|p|$ is the length of program $p$), the probability that we execute a program $p_{AGI}$ that is AGI is $P(\mathrm{p\ exhibits\ AGI} \mid |p| < l) = 0$, in other word we will at best observe sub-AGI intelligence but not AGI itself.

On the other hand, for any program larger or equal to $l$, we may assume that it is sufficient for a program $p$ to contain the program $p_{AGI}$ somewhere in its string definition. In other terms, if this program $p$ contains the substring (from index $a$ to $b$) $p_{a,b}$ that is the AGI program $p_{AGI}$, in other words $p_{a,b} = p_{AGI}$, then $P(\mathrm{p\ exhibits\ AGI} \mid |p| \ge l \wedge |p_{a,b}| = |p_{AGI}|) = 1$. Finally, we may ask ourselves what is the probability of finding an AGI program, given a program of length $|p|$ and a know seed AGI program $p_{AGI}$ which is a subprogram/substring of $p$, $P(\mathrm{p\ exhibits\ AGI} \mid |p| \ge l \wedge p_{AGI}) =\ ?$. More interestingly, we can ask what is the probability of finding an AGI program, given that we "know" the minimal program length of an existing AGI but do not have the code, $P(\mathrm{p\ exhibits\ AGI} \mid |p| \ge l) =\ ?$.

Since we said that for a program to exhibit AGI it would have to contain a seed AGI as a substring of itself, we can be simplify $\mathrm{p\ exhibits\ AGI}$ as $p_{a,b} = p_{AGI}$. Thus, one of our question becomes $P(p_{a,b} = p_{AGI} \mid |p| \ge l) =\ ?$, which means "given that our program $p$ is longer than an expected seed AI of length $l$, what is the probability that as part of its code (a substring) is $p_{AGI}$?".

### Deduction

What is the probability of finding an AGI program? To answer this question, we go through a deductive process which is detailed below.

* the probability of finding an AGI program is based on the existence of such a program
* the probability is based on the minimum length of a program exhibiting AGI, as the set of longer programs will necessarily include this smaller program within them
* thus, past a certain length, we have 100% certainty that the AGI program exist within the set of programs

* a program is composed of an alphabet $\Sigma$ of $s$ symbols
	* $\Sigma$: Alphabet
	* $s$: Number of symbols in the alphabet
		* $s$ cannot be 0 nor 1 as we need to convey information, which requires at least two symbols
* the smallest AGI program has a given length $l$
	* $l = |p_{AGI}|$: length of the smallest AGI
* how many programs are of length $|p|$? $s^{|p|}$
* $s^{|p_{a,b}|}$ number of programs of length $|p_{a,b}|$
* $P(\mathrm{p\ exhibits\ AGI} \mid |p_{a,b}| = l) = \frac{1}{s^{|p_{a,b}|}} = \frac{1}{s^{|p_{AGI}|}} =  \frac{1}{s^l}$
* $p_{x,y}$ contains $p_{a,b} = p_{AGI}$, thus $|p_{x,y}| \ge |p_{AGI}|$
* for a program $p_{x,y}$ one symbol longer than $p_{a,b}$
	* $s$ programs with prefix $p_{a,b}$
	* $s$ programs with suffix $p_{a,b}$ (same as prefix)
* when the length difference $d = |p_{x,y}| - |p_{a,b}|$ increases, then we have permutations (where X is any symbol of the alphabet):
	* length 2 XX_, X_X, _XX => $3s^2$
	* length 3 XXX_, XX_X, X_XX, _XXX => $4s^3$
	* length n => $(n+1)s^n$
* $L_{p \to AGI} = |p_{x,y}| - |p_{AGI}|$ the length difference between a program $p_{x,y}$ longer than $p_{AGI}$
* for $s > 1$ and $l = |p_{AGI}| > 1$, (something is not right with this equation as the probability can go over 1 if $|p_{x,y}| - |p_{AGI}| + 1 >s^{|p_{AGI}|}$)
$$
\begin{split}
P(\mathrm{p\ exhibits\ AGI} \mid |p_{x,y}| > l \wedge p_{AGI}) &= (L_{p \to AGI} + 1) \times \frac{s^{L_{p \to AGI}}}{s^{|p_{x,y}|}} \\
&= [|p_{x,y}| - |p_{AGI}| + 1] \times \frac{s^{|p_{x,y}| - |p_{AGI}|}}{s^{|p_{x,y}|}} \\
&= [|p_{x,y}| - |p_{AGI}| + 1] \times \frac{s^{|p_{x,y}|} \times s^{-|p_{AGI}|}}{s^{|p_{x,y}|}}  \\
&= \frac{|p_{x,y}| - |p_{AGI}| + 1}{s^{|p_{AGI}|}} \\
\end{split}
$$

A couple conclusions:

* The larger the smallest AGI program is, the more difficult it is to find it in the solution space
* As the program $p$ length tends to infinity, the probability it contains the AGI program increases to almost 100% certainty, $P(\mathrm{p\ exhibits\ AGI}|\lim_{(y-x) \rightarrow \infty}|p_{x,y}|) \approx 1$

# See also
* [Observations on DNA](observations-on-dna)
