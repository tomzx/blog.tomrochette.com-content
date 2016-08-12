---
title: Introduction to Automata Theory, Languages, and Computation - 2006
created: 2016-07-30
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview

# Notes
* (p1) 1930 - Alan Turing - Turing machines
* (p1) 1940-1950 - Finite automata
* (p1) Late 1950 - Noam Chomsky - Formal grammar
* (p1) 1969 - Stephen Cook - What can and cannot be computed
* (p31) The only important constraint on what can be a language is that all alphabets are finite
* (p31) In automata theory, a problem is the question of deciding whether a given string is a member of some particular language
	Given a string $w$ in $\Sigma*$, decide whether or not $w$ is in $L$
* (p45) A deterministic finite automaton consists of:
	* A finite set of states, often denoted $Q$
	* A finite set of input symbols, often denoted $\Sigma$
	* A transition function that takes as argument a state and an input symbol and returns a state. The transition function will commonly be denoted $\delta$
	* A start state, one of the states in $Q$
	* A set of final or accepting states $F$. The set $F$ is a subset of $Q$
* (p52) The language of a DFA $A = (Q, \Sigma, \delta, q_0, F)$ is denoted $L(A) = \{w\ |\ \hat{\delta}(q_0, w)\mathrm{\ is\ in\ }F\}$
* (p59) The language of an NFA $A = (Q, \Sigma, \delta, q_0, F)$ is denoted $L(A) = \{w\ |\ \hat{\delta}(q_0, w) \cap F \not= \emptyset\}$
* (p128) The pumping lemma
	* $y \not= \epsilon$
	* $|xy| \leq n$
	* For all $k \geq 0$, the string $xy^kz$ is also in $L$
* (p129) Every string longer than the number of states must cause a state to repeat

# See also

# Sources