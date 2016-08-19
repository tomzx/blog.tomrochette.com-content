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
* (p139) The reversal of a string $a_1a_2...a_n$ is the string written backwards, that is, $a_na_{n-1}...a_1$. We use $w^R$ for the reversal of string $w$
* (p139) The reversal of a language $L$, written $L^R$, is the language consisting of the reversals of all its strings
* (p140) A string homomorphism is a function on strings that works by substituting a particular string for each symbol
* (p150) Fundamental questions about languages:
	* Is the language described empty?
	* Is a particular string $w$ in the described language?
	* Do two descriptions of a language actually describe the same language? (This question is often called "equivalence" of languages)
* (p151) Converting either an NFA or epsilon-NFA into a DFA can require exponential time in the number of states of the NFA, $O(n^32^n)$
	* Computing the epsilon-closure of $n$ states takes $O(n^3)$
	* The dominant cost of subset construction is, in principle, the number of states of the DFA, which can be $2^n$
		* For each state, we can compute the transitions in $O(n^3)$ time by consulting the epsilon-closure information and the NFA's transition table for each of the input symbols
* (p152) DFA-to-NFA conversion takes $O(n)$ time on an n-state DFA
* (p152) Automaton-to-Regular-Expression conversion, $O(n^34^n)$ for DFA, $O(8^n4^{2^n})$ for NFA (doubly exponential)
* (p152) Regular-Expression-to-Automaton conversion, $O(n)$ to build an epsilon-NFA, $O(n^3)$ to convert the epsilon-NFA to an ordinary NFA

# See also

# Sources