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

## 5 The Problem of Logical Omniscience
* The problem of logical omniscience: Can we give some formal account of "knowledge" able to accommodate people learning new things without leaving their armchairs?
* One vacuous "solution" would be to declare that your knowledge is simply a list of all the true sentences that you "know"
* Intuitively, we want to say that your "knowledge" consists of various facts, together with some simple logical consequences of those facts, but not necessarily all the consequences, and certainly not all consequences that involve difficult mathematical reasoning
* As soon as we try to formalize this idea, we run into problems
* The most obvious problem is the lack of a sharp boundary between the facts you know right away, and those you "could" know, but only after significant thought
* A related problem is the lack of a sharp boundary between the facts you know "only if asked about them," and those you know even if you're not asked
* There's a third problem that seems much more serious than either of the two above. Namely, you might "know" a particular fact if asked about it one way, but not if asked in a different way
* Do you possess an internal algorithm, by which you can answer a large (and possibly-unbounded) set of questions of some form?
	* ... answer in a reasonable amount of time ...

### 5.1 The Cobham Axioms
* Function Polynomial-Time (FP): the set of all functions of natural numbers $f: \mathbb{N} \rightarrow \mathbb{N}$ that are computable in polynomial time by a deterministic Turing machine
* FP is "morally" the same as the class P: they differ only in that P is a class of decision problems (or equivalently, functions of $f: \mathbb{N} \rightarrow \{0, 1\}$), whereas FP is a class of functions with integer range
* Cobham axioms:
	* Every constant function $f$ is efficiently computable, as is every function which is nonzero only finitely often.
	* Pairing: If $f(x)$ and $g(x)$ are efficiently computable, then so is $\langle f(x), g(x) \rangle$, where $\langle , \rangle$ is some standard pairing function for the natural numbers.
	* Composition: If $f(x)$ and $g(x)$ are efficiently computable, then so is $f(g(x))$.
	* Grab Bag: The following functions are all efficiently computable:
		* the arithmetic functions $x + y$ and $x \times y$
		* $|x| = \lfloor \log_2 x \rfloor + 1$ (the number of bits in $x$'s binary representation)
		* the projection functions $\Pi_1 (\langle x, y \rangle) = x$ and $\Pi_2 (\langle x, y \rangle) = y$
		* bit $(\langle x, i \rangle)$ (the $i^{th}$ bit of $x$ binary representation, or 0 if $i > |x|$)
		* diff $(\langle x, i \rangle)$ (the number obtained from $x$ by flipping its $i^{th}$ bit)
		* $2^{|x|^2}$ (called the "smash function")
	* Bounded Recursion: Suppose $f(x)$ is efficiently computable, and $|f(x)| \le |x|$ for all $x \in \mathbb{N}$. Then the function $g(\langle x, k \rangle)$, defined by
$$
g(\langle x, k \rangle) = \left\{
	\begin{array}{ll}
		f(g(\langle x, \lfloor k/2 \rfloor \rangle)) & \mbox{if k > 1} \\
		x & \mbox{if k = 1}
	\end{array}
\right.
$$
is also efficiently computable.
* The class FP, of functions $f: \mathbb{N} \rightarrow \mathbb{N}$ computable in polynomial time by a deterministic Turing machine, satisfies Cobham axioms, and is the smallest class that does so

### 5.2 Omniscience Versus Infinity
* We could refuse to define an agent's "knowledge" in terms of which individual questions she can quickly answer, and insist of speaking instead about which infinite families of questions she can quickly answer
* The main objections to the "infinity cure"
	* We've simply pushed the problem of logical omniscience somewhere else
	* The infinite families have not been specified
		* The relevant issue will be whether there exists a generalization $G$ of $Q$ (a question), such that the agent knows a fast algorithm for answering questions of type $G$, and also recognize that $Q$ is of type $G$ (e.g., determining whether a number ending in 0 is composite or not, based on the fact that it will be a multiple of 10)
	* The relationship between asymptotic complexity and finite statements
		* The usual response: Asymptotic statements are always vulnerable to being rendered irrelevant, if the constant factors turned out to be ridiculous

## 7 PAC-Learning and the Problem of Induction
* In this theory, we consider an idealized "learner," who is presented with points $x_1, \dots, x_m$ drawn randomly from some large set $\mathcal{S}$, together with the "classifications" $f(x_1), \dots, f(x_m)$ of those points
* The learner's goal is to infer the function $f$, well enough to be able to predict $f(x)$ for most future points $x \in \mathcal{S}$

# See also

# References
* Aaronson, Scott. "Why philosophers should care about computational complexity." arXiv preprint arXiv:1108.1791 (2011).