---
title: Scott Aaronson - Why Philosophers Should Care About Computational Complexity (2011)
created: 2017-08-24
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview

# Notes
## 2 Complexity 101
* Complexity theory asks the question: how do the resources needed to solve a problem scale with some measure $n$ of the problem size
	* reasonably, like $n$ or $n^2$
	* unreasonably, like $2^n$ or $n!$
* Theoretical computer scientists generally call an algorithm "efficient" if its running time can be upper-bounded by any polynomial function of $n$, and "inefficient" if its running time can be lower-bounded by any exponential function of $n$

## 4 Computational Complexity and the Turing Test
* According to the Incompleteness Theorem, one thing that a computer making deductions via fixed formal rules can never do is to "see" the consistency of its own rules. Yet this, they (Lucas and Penrose) assert, is something that human mathematicians can do, via some sort of intuitive perception of Platonic reality
* What does one even mean in saying one has a task that "humans can perform but computers cannot"?

### 4.1 The Lookup-Table Argument
* In practice, people judge each other to be conscious after interacting for a very short time, perhaps as little as a few seconds
* This suggests that we can put a finite upper bound - to be generous, let us say $10^{20}$ - on the number of bits of information that two people A and B would ever realistically exchange, before A had amassed enough evidence to conclude that B was conscious
* Given a lookup table of all the possible history H of A and B conversations, we can say that the lookup table would be finite, by the assumption that there is a finite upper bound on the conversation length
* This implies that the function $f_B$ is computable
* From these simple considerations, we conclude that if there is a fundamental obstacle to computers passing the Turing Test, then it is not to be found in computability theory
* (Speculation) (CLAIM1) Any computer program that passed the Turing Test would need to be exponentially-inefficient in the length of the test - as measured in some resource such as time, memory usage, or the number of bits needed to write the program down. In other words, the astronomical lookup table is essentially the best one can do.

### 4.2 Relation to Previous Work
* An exponential-sized lookup table that passed the Turing Tet would not be sentient (or conscious, intelligent, self-aware, etc.), but a polynomially-bounded program with exactly the same input/output behavior would be sentient
	* Furthermore, the latter program would be sentient because it was polynomially-bounded

### 4.3 Can Humans Solve NP-Complete Problems Efficiently?
* Are there any reasons to accept the claim (CLAIM1) - the claim that humans are not efficiently simulable by Turing machines?
* Despite occasional claims to the contrary, I personally see no reason to believe that humans can solve NP-complete problems in polynomial time, and excellent reasons to believe the opposite
* Even if humans were not efficiently simulable by Turing machines, the "direction" in which they were hard to simulate would almost certainly be different from the directions usually considered in complexity theory
* Two (hypothetical) ways this could happen
	* The task that humans were uniquely good at - like painting or writing poetry - could be incomparable with mathematical tasks like solving NP-complete problems, in the sense that neither was efficiently reducible to the other
	* Humans could have the ability to solve interesting special cases of NP-complete problems faster than any Turing machine (e.g., the Pigeonhole Principle, where the Boolean satisfiability algorithms would have to try all variants (exponential))

# See also

# References
* Aaronson, Scott. "Why philosophers should care about computational complexity." arXiv preprint arXiv:1108.1791 (2011).