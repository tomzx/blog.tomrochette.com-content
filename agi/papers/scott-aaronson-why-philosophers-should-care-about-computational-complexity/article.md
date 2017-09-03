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
* For simplicity, we often assume that $\mathcal{S}$ is a set of binary strings, and that the function $f$ maps each $x \in \mathcal{S}$ to a single bit, $f(x) \in \{0, 1\}$
* The important assumptions are the following:
	* Each of the sample points $x_1, \dots, x_m$ is drawn independently from some (possibly-unknown) "sample distribution" $\mathcal{D}$ over $\mathcal{S}$. Furthermore, the future points $x$ on which the learner will need to predict $f(x)$ are drawn from the same distribution
	* The function $f$ belongs to a known "hypothesis class" $\mathcal{H}$. This $\mathcal{H}$ represents "the set of possibilities" the learner is willing to entertain" (and is typically much smaller than the set of all $2^{|\mathcal{S}|}$ possible functions from $\mathcal{S}$ to $\{0, 1\}$)
* Theorem 2 (Valiant) Consider a finite hypothesis class $\mathcal{H}$, a Boolean function $f : \mathcal{S} \rightarrow \{0, 1\} \in \mathcal{H}$, and a sample distribution $\mathcal{D}$ over $\mathcal{S}$, as well as an error rate $\epsilon > 0$ and a failure probability $\delta > 0$ that the learner is willing to tolerate. Call a hypothesis $h : \mathcal{S} \rightarrow \{0, 1\}$ "good" if
$$
\Pr_{x \sim \mathcal{D}} [h(x) = f(x)] \ge 1 - \epsilon
$$
* Also, call sample points $x_1, \dots, x_m$ "reliable" if any hypothesis $h \in \mathcal{H}$ that satisfies $h(x_i) = f(x_i)$ for all $i \in \{1, \dots, m\}$ is good. Then
$$
m = \frac{1}{\epsilon}\ln\frac{\mathcal{H}}{\delta}
$$
* samples points $x_1, \dots, x_m$ drawn independently from $\mathcal{D}$ will be reliable with probability at least $1 - \delta$
* In other words, if, by some unspecified means, the learner manages to find any hypothesis $h \in \mathcal{H}$ that makes correct predictions on all its past data points $x_1, \dots, x_m$, then provided $m$ is large enough (and as it happens, $m$ doesn't need to be very large), the learner can be statistically confident that $h$ will also make the correct predictions on most future points

### 7.1 Drawbacks of the Basic PAC Model
* The first drawback is that the Theorem 2 works only for finite hypothesis classes
* One could solve this problem by simply discretizing the parameters, but then the number of hypothesis would depend on how fine the discretization was
* Fortunately, we can avoid such difficulties by realizing that the learner only cares about the "differences" between two hypothesis insofar as they lead to different predictions
	* This leads to the fundamental notion of VC-dimension
* Definition 3 (VC-dimension) A hypothesis class $\mathcal{H}$ shatters the sample points ${x_1, \dots, x_k} \subseteq \mathcal{S}$ if for all $2^k$ possible settings of $h(x_1), \dots, h(x_k)$, there exists a hypothesis $h \in \mathcal{H}$ compatible with those settings. Then $VCdim(\mathcal{H})$, the VC-dimension of $\mathcal{H}$, is the largest $k$ for which there exists a subset ${x_1, \dots, x_k} \subseteq \mathcal{S}$ that $\mathcal{H}$ shatters (or if no finite maximum exists, then $VCdim(\mathcal{H}) = \infty$)
* Theorem 4 (Blumer et al.) For some universal constant $K > 0$, the bound on $m$ in Theorem 2 can be replaced by
$$
m = \frac{K\ VCdim(\mathcal{H})}{\epsilon}\ln\frac{\mathcal{H}}{\delta\epsilon}
$$
* with the theorem now holding for any hypothesis class $\mathcal{H}$, finite or infinite
* In some sense, Theorem 4 is telling us that finite VC-dimension is a necessary and sufficient condition for scientific induction to be possible
* The second drawback of Theorem 2 is that it gives us no clues about how to find a hypothesis $h \in \mathcal{H}$ consistent with the sample data. All it says is that, if we find such an $h$, then $h$ will probably be close to the truth
* Learning and cryptography are "dual" problems: a learner wants to find patterns in data, while a cryptographer wants to generate data whose patterns are hard to find
* The third drawback of Theorem 2 is the assumption that the distribution $\mathcal{D}$ from which the learner is tested is the same as the distribution from which the sample points were drawn
* The goal of science is not merely to summarize observations, and thereby let us make predictions about similar observations. Rather, the goal is to discover explanations with "reach," meaning the ability to predict what would happen in novel or hypothetical situations

# See also

# References
* Aaronson, Scott. "Why philosophers should care about computational complexity." arXiv preprint arXiv:1108.1791 (2011).