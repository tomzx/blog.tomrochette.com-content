---
title: Paul R. Halmos - Naive Set Theory - 1960
created: 2016-01-14
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview
* (p1) Sets have elements or members
* (p1) Sets may be elements of sets
* (p2) If $A$ and $B$ are sets and if every element of $A$ is an element of $B$, $A$ is a subset of $B$ or $B$ includes $A$
	* $A \subset B = B \supset A$
* (p2) This implies $A \subset A$
	* The set inclusion is reflexive
* (p2) If $A$ and $B$ are sets such that $A \subset B$ and $A \not= B$, then $A$ is a proper subset or $B$ or $B$ properly includes $A$ (proper inclusion)
* (p2) If $A$, $B$ and $C$ are sets such that $A \subset B$ and $B \subset C$, then $A \subset C$ (set inclusion is transitive)
* (p2) If $A \subset B$ and $B \subset A$, then A and B have the same elements and therefore, by the axiom of extension, $A = B$. (antisymmetric)
* (p2) To prove that two sets are equals, you prove that $A \subset B$ and then $B \subset A$.
* (p2) Inclusion is always reflexive and transitive
* (p2) Belonging is never reflexive nor transitive
* (p6) Nothing contains everything
* (p7) There is no universe
* (p8) There exists a set
	* (p8) There exists a set with no elements
	* Symbol: $\varnothing$  (empty set)
	* $\varnothing \subset A$ for every $A$
* (p8) To prove that something is true (about the empty set), prove that it cannot be false
* (p10) If $a$ is a set, we may form the unordered pair $\{a, a\}$. That unordered pair is denoted by $\{a\}$ and is called the singleton of $a$.
* (p10) $a \in A \iff \{a\} \subset A$
* (p13) $\bigcup\{X: X \in \varnothing\} = \varnothing$
* (p13) $\bigcup\{X: X \in \{A\}\} = A$
* (p13) $\bigcup\{X: X \in \{A, B\}\} = A \cup B$
* (p13) $A \cup B = \{x: x \in A\ or\ x \in B\}$
* (p14) $A \cap B = \{x \in A: x \in B\} = \{x \in B: x \in A\} = \{x: x \in A\ and\ x \in B\}$
* (p15) If $A \cap B =  \varnothing$, the sets $A$ and $B$ are called disjoint
* (p15) $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$
* (p15) $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$
* (p17) $A - B = \{x \in A: x \not\in B\}$
* (p17) De Morgan laws: $(A \cup B)' = A' \cap B'$, $(A \cap B)' = A' \cup B'$
* (p18) $A + B = (A - B) \cup (B - A)$
* (p20) The power set of a finite set with $n$ elements has $2^n$ elements.
* (p22) Order c b d a = {c} {c, b} {c, b, d} {c, b, d, a}
* (p23) Ordered pair (a, b) = {{a}, {a, b}}
* (p24) Cartesian product: $A \times B = \{x: x = (a, b)\ for\ some\ a\ in\ A\ and\ some\ b\ in\ B\}$
* (p27) Relation: $z = (x, y)$, $x R y$
* (p27) Domain: $dom R = \{x: for\some\ y\ (x R y)\}$
* (p27) Range: $ran R = \{y: for\some\ x\ (x R y)\}$
* (p27) reflexive if $x R x$ for every $x$ in $X$
* (p27) symmetric if $x R y$ implies $y R x$
* (p27) transitive if $x R y$ and $y R z$ imply $x R z$
* (p28) equivalence relation if it is reflexive, symmetric and transitive
* (p28) A partition of $X$ is a disjoint collection $\mathcal{C}$ of non-empty subsets of $X$ whose union is $X$
* (p45) A family $\{x_i\}$ whose index set is either a natural number or else the set of all naturals numbers is called a sequence
* (p 47) No natural number is a subset of any of its elements
* (p 47) Every element of a natural number is a subset of it
* (p 48) **Recursion theorem:** If $a$ is an element of a set $X$, and if $f$ is a function from $X$ into $X$, then there exists a function $u$ from $\omega$ into $X$ such that $u(0) = a$ and such that $u(n^+) = f(u(n))$ for all $n$ in $\omega$.

# Axioms

## Axiom of extension
Two sets are equal if and only if they have the same elements.

## Axiom of specification
To every set $A$ and to every condition $S(x)$ there corresponds a set $B$ whose elements are exactly those elements $x$ of $A$ for which $S(x)$ holds.

## Axiom of pairing
For any two sets there exists a set that they both belong to.

## Axiom of unions
For every collection of sets there exists a set that contains all the elements that belong to at least one set of the given collection.

## Axiom of powers
For each set there exists a collection of sets that contains among its elements all the subsets of the given set.

## Axiom of infinity
There exists a set containing 0 and containing the successor of each of its elements.

## Peano axioms
1. $0 \in \omega$
2. $if\ n \in \omega,\ then\ n^+ \in \omega$
3. $if\ S \subset \omega, if\ 0 \in \omega,\ and\ if\ n^+ \in S\ whenever\ n \in S,\ then\ S = \omega$
4. $n^+\ \not= 0\ for\ all\ n\ in\ \omega$
5. $if\ n\ and\ m\ are\ in\ \omega,\ and\ if\ n^+ = m^+,\ then\ n = m$

# Operators
* $\wedge$: and
* $\vee$: or (either or both)
* $\neg$: not
* $\Rightarrow$: if-then (implies)
* $\iff$: if and only if
* $\exists$: for some (there exists)
* $\forall$: for all

# See also

# References
* Halmos, Paul Richard. Naive set theory. Springer Science & Business Media, 1960.