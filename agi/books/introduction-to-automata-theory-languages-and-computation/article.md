---
title: Introduction to Automata Theory, Languages, and Computation - 2006
created: 2016-07-30
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---
$\require{extpfeil}\Newextarrow{\xRightarrow}{5,5}{0x21D2}$

## Context

## Learned in this study

## Things to explore

# Overview

# Notes
## Chapter 1 - Automata: The Methods and the Madness
* (p1) 1930 - Alan Turing - Turing machines
* (p1) 1940-1950 - Finite automata
* (p1) Late 1950 - Noam Chomsky - Formal grammar
* (p1) 1969 - Stephen Cook - What can and cannot be computed
* (p31) The only important constraint on what can be a language is that all alphabets are finite
* (p31) In automata theory, a problem is the question of deciding whether a given string is a member of some particular language
	Given a string $w$ in $\Sigma*$, decide whether or not $w$ is in $L$

## Chapter 2 - Finite Automata
* (p45) A deterministic finite automaton consists of:
	* A finite set of states, often denoted $Q$
	* A finite set of input symbols, often denoted $\Sigma$
	* A transition function that takes as argument a state and an input symbol and returns a state. The transition function will commonly be denoted $\delta$
	* A start state, one of the states in $Q$
	* A set of final or accepting states $F$. The set $F$ is a subset of $Q$
* (p52) The language of a DFA $A = (Q, \Sigma, \delta, q_0, F)$ is denoted $L(A) = \{w\ |\ \hat{\delta}(q_0, w)\mathrm{\ is\ in\ }F\}$
* (p59) The language of an NFA $A = (Q, \Sigma, \delta, q_0, F)$ is denoted $L(A) = \{w\ |\ \hat{\delta}(q_0, w) \cap F \not= \emptyset\}$

## Chapter 3 - Regular Expressions and Languages

## Chapter 4 - Properties of Regular Languages
* (p128) The pumping lemma: If a language is regular, then every sufficiently long string in the language has a nonempty substring that can be "pumped," that is, repeated any number of times while the resulting strings are also in the language
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
* (p154) Testing if, given string w and a regular language L, w is in L
	* Takes $O(n)$ for a DFA
	* Takes $O(ns^2)$ for NFA, epsilon-NFA and regular expression $O(s)+O(ns^2)$
* (p160) $O(n^2)$ rounds to check if regular language are equivalent, $O(n^2)$ time per round to verify if one of their successor pairs has been found distinguisable, thus $O(n^4)$ to run the table-filling algorithm
	* Can be reduced to $O(n^2)$ using lists tracking which pairs depends on which pairs (and once a pair is proven distinguishable, it's simply a matter of going through that list and marking the pair as distinguishable)
* (p160) Minimization of DFA's
	* First, eliminate any state that cannot be reached from the start state
	* Then, partition the remaining states into blocks, so that all states in the same block are equivalent, and no pair of states from different blocks are equivalent
	* Use the table-filling algorithm to find all the pairs of equivalent states
	* Partition the set of states Q into blocks of mutually equivalent states
	* Construct the minimum-state equivalent DFA B by using the blocks as its state
* (p166) Operations that preserve the property of being a regular language:
	* union
	* concatenation
	* closure
	* intersection
	* complementation
	* difference
	* reversal
	* homomorphism
	* inverse homomorphism

## Chapter 5 - Context-Free Grammars and Languages
* (p173) Definition of a context-free grammar G = (V = variables, T = terminals, P = productions, S = start symbol):
	* There is a finite set of symbols that form the strings of the language being defined (called terminals or terminal symbols)
	* There is a finite set of variables, also called sometimes nonterminals or syntactic categories. Each variable represents a language
	* One of the variables represents the language being defined; it is called the start symbol. Other variables represents auxiliary classes of strings that are used to help define the language of the start symbol
	* There is a finite set of productions or rules that represent the recursive definition of a language. Each production consists of:
		* A variable that is being partially defined by the production. This variable is often called the head of the production
		* The production symbol $\rightarrow$
		* A string of zero or more terminals and variables. This string, called the body of the production, represents one way to form strings in the language of the variable of the head
* (p175) Recursive inference: Use the rules from body to head
* (p175) Derivation: Use the rules from head to body
* (p177) In order to restrict the number of choices we have in deriving a string, it is often useful to require that at each step we replace the leftmost variable by one of its production bodies. Such a derivation is called a leftmost derivation, and we indicate that a derivation is leftmost by using the relations $\xRightarrow[lm]{}$ and $\xRightarrow[lm]{*}$
* (p177) Similarly, it is possible to require that at each step the rightmost variable is replaced by one of its bodies. If so, we call the derivation rightmost and use the symbols $\xRightarrow[rm]{}$ and $\xRightarrow[rm]{*}$
* (p183) The parse trees for G = (V, T, P, S) are trees with the following conditions:
	* Each interior node is labeled by a variable in V
	* Each leaf is labeled by either a variable, a terminal, or $\epsilon$. However, if the leaf is labeled $\epsilon$, then it must be the only child of its parent
	* If an interior node is labeled A, and its children are labeled $X_1, X_2, ..., X_k$ respectively, from the left, then $A \rightarrow X_1X_2...X_k$ is a production in P.
* (p185) The concatenation of the leaves of any parse tree, taken from them left, is called the yield of the tree
* (p208) A CFG G = (V, T, P, S) is ambiguous if there is at least one string w in T* for which we can find two different parse trees, each with root labeled S and yield w. If each string has at most one parse tree in the grammar, then the grammar is unambiguous
* (p209) There is no algorithm that can tell us whether a CFG is ambiguous
* (p210) A factor is an expression that cannot be broken apart by any adjacent operator

## Chapter 6 - Pushdown Automata
* (p225) The pushdown automaton is essentially an epsilon-NFA with the addition of a stack
* (p225) We define two different versions of the pushdown automaton:
	* One that accepts by entering an accepting state
	* One that accepts by emptying its stack, regardless of the state it is in
* (p230) Instantaneous description of a PDA (q, w, $\gamma$)
	* q is the state
	* w is the remaining input
	* $\gamma$ is the stack contents

## Chapter 8 - Introduction to Turing Machines
* (p316) Proving formally that there is no program to do a stated task is quite tricky
* (p318) We know there are infinitely fewer programs than there are problems
* (p318) If a problem as an algorithm that always tells correctly whether an instance of the problem has answer "yes" or "no," then the problem is said to be "decidable". Otherwise, the problem is "undecidable"
* (p321) Suppose that we know problem $P_1$ is undecidable, and $P_2$ is a new problem that we would like to prove is undecidable as well
* (p322) In order to make a proof that problem $P_2$ is undecidable, we have to invent a construction that converts instances of $P_1$ to instances of $P_2$ that have the same answer
* (p322) Any string in the language $P_1$ is converted to some string in the language $P_2$, and any string over the alphabet of $P_1$ that is not in the language of $P_1$ is converted to a string that is not in the language $P_2$
* (p322) Once we have this construction, we can solve $P_1$ as follows:
	* Given an instance of $P_1$, that is, given a string $w$ that may or may not be in the language $P_1$, apply the construction algorithm to produce a string $x$
	* Test whether $x$ is in $P_2$, and give the same answer about $w$ and $P_1$
* (p325) Using the Turing machine notation, we shall prove undecidable certain problems that appear unrelated to programming
* (Formal description of a Turing machine skipped)
* (p334) There is another notion of "acceptance" that is commonly used for Turing machines: acceptance by halting. We say that a TM halts if it enters a state q, scanning a tape symbol X, and there is no move in this situation; i.e., $\delta(q, X)$ is undefined
	* We assume that a TM always halts when it is in an accepting state
* (p341) As with programs in general, it helps to think of Turing machines as built from a collection of interacting components, or "subroutines"
* (p345) Every language accepted by a multitape TM is recursively enumerable
* (p346) The running time of TM $M$ on input $w$ is the number of steps that $M$ makes before halting
	* If $M$ doesn't halt on $w$, then the running time of $M$ is infinite
* (p346) The time complexity of TM $M$ is the function $T(n)$ that is the maximum, over all inputs $w$ of length $n$, of the running time of $M$ on $w$
* (p347) The difference between polynomial time and higher growth rates in running time is really the divide between what we can solve by computer and what is in practice not solvable
* (p348) A nondeterministic Turing machine (NTM) accepts no languages not accepted by a deterministic TM (or DTM)
* (p348) If $M_N$ is a nondeterministic Turing machine, then there is a deterministic Turing machine $M_D$ such that $L(M_N) = L(M_D)$
* (p353) A TM with a semi-infinite tape (there are no cells to the left of the initial head position) can simulate one whose tape is infinite in both directions
	* Simply construct a tape with 2 tracks, one representing the positive positions, the second one, the negative positions
* (p355) If we give a PDA two stacks, then it can accept any language that a TM can accept
* (p359) A two-counter machine is enough to simulate a Turing machine and therefore to accept every recursively enumerable language
* (p369) If a computer:
	* Has only instructions that increase the maximum word length by at most 1, and
	* Has only instructions that a multitape TM can perform on words of length $k$ in $O(k^2)$ steps or less
	* then the Turing machine can simulate $n$ steps of the computer in $O(n^3)$ of its own steps

## Chapter 9 - Undecidability
* (p377) Does this Turing machine accept (the code for) itself as input?
	* Cannot be solved by a computer
* (p377) We divide problems that can be solved by a Turing machine into two classes:
	* Those that have an algorithm (i.e., a Turing machine that halts whether or not it accepts its input)
	* Those that are only solved by Turing machines that may run forever on inputs they do not accept
* (p378) Our long-range goal is to prove undecidable the language consisting of pairs (M, w) such that:
	* M is a Turing machine with alphabet {0, 1}
	* w is a string of 0's and 1's
	* M accepts input w
* If this problem with inputs restricted to the binary alphabet is undecidable, then surely the more general problem, where TM's may have any alphabet, is undecidable
* (p382) $L_d$ (the diagonalization language) is not a recursively enumerable language. That is, there is no Turing machine that accepts $L_d$
* (p383) We call a language L recursive if L = L(M) for some Turing machine M such that:
	* If w is in L, then M accepts (and therefore halts)
	* If w is not in L, then M eventually halts, although it never enters an accepting state
* (p383) If we think of the language L as a "problem," then problem L is called decidable if it is a recursive language, and it is called undecidable if it is not a recursive language
* (p386) If L is a recursive language, so is the complement of L (every language that L accepts should be rejected by its complement, and every language that L rejects should be accepted by its complement)
* (p386) If both a language L and its complement are recursively enumerable, then L is recursive
* (p397) Our intuition tells us that a problem and its complement are really the same problem. To solve one, we can use an algorithm for the other, and at the last step, complement the output: say "yes" instead of "no," and vice-versa. That instinct is exactly right, as long as the problem and its complement are recursive.
* (p397) All nontrivial properties of the RE languages are undecidable, in the sense that it is impossible to recognize by a Turing machine those binary strings that are codes for a TM whose language has the property.
* (p397) A *property* of the RE languages is simply a set of RE languages
* (p397) A property is *trivial* if it is either empty, or is all RE languages. Otherwise it is *nontrivial*
* (p399) Rice's theorem does not imply that everything about a TM is undecidable. For instance, questions that ask about the states of the TM, rather than about the language it accepts, could be decidable
* (p401) An instance of Post's Correspondence Problem (PCP) consists of two lists of strings over some alphabet $\Sigma$; the two lists must be of equal length. We generally refer to the A and B lists, and write $A = w_1, w_2, ..., w_k$ and $B = x_1, x_2, ..., x_k$, for some integer k. For each i, the pair $(w_i, x_i)$ is said to be a corresponding pair. We say this instance of PCP has a solution, if there is a sequence of one or more integer $i_1, i_2, ..., i_m$ that, when interpreted as indexes for strings in the A and B lists, yield the same string. That is, $w_{i_1} w_{i_2} \cdots w_{i_m} = x_{i_1} x_{i_2} \cdots x_{i_m}$. We say the sequence $i_1, i_2, ..., i_m$ is a solution to this instance of PCP
* (p407) Rules:
	1. The first pair is

	| List A | List B |
	|--------|--------|
	| $\#$   | $\#q_0w\#$ |

	where $w$ is the initial input

	2. Add tape symbols and the separator # to both list

	| List A | List B |
	|--------|--------|
	| X | X |
	| Y | Y |
	| $\#$ | $\#$ |

	3. For each non-terminating transition, create an entry in the list. When the tape is moved to the left, we have to consider all terminal symbols that may lie on the left.

	| List A | List B | |
	|--------|--------|-|
	| qX | Yp | if $\delta(q, X) = (p, Y, R)$ |
	| XqX | pXZ | if $\delta(q, X) = (p, Z, L)$ |
	| XqY | pXZ | if $\delta(q, Y) = (p, Z, L)$ |
	| q# | Yp# | if $\delta(q, B) = (p, Y, R)$ |
	| Xq# | pXY# | if $\delta(q, B) = (p, Y, L)$ |
	| Yq# | pYY# | if $\delta(q, B) = (p, Y, L)$ |

	4. Complete the partial solution. For all tape symbols

	| List A | List B |
	|--------|--------|
	| XqX | q |
	| XqY | q |
	| YqX | q |
	| YqY | q|
	| Xq | q |
	| Yq | q |
	| qX | q |
	| qY | q |

	5. Once the final state has consumed all tape symbols, it stands alone as the last ID on the B string

	| List A | List B |
	|--------|--------|
	| q## | # |

* (p411) Post's Correspondence Problem is undecidable
* (p415) It is undecidable whether a context-free grammar is ambiguous
* (p419) The languages accepted by Turing machines are called recursively enumerable (RE), and the subset of RE languages that are accepted by a TM that always halts are called recursive
* (p419) The recursive languages are closed under complementation, and if a language and its complement are both RE, then both languages are actually recursive. Thus, the complement of an RE-but-not-recursive language can never be RE.

## Chapter 10 - Intractable problems
* (p425) Experience has shown that the dividing line between problems that can be solved in polynomial time and those that require exponential time or more is quite fundamental. Practical problems requiring polynomial time are almost always solvable in an amount of time that we can tolerate, while those that require exponential time generally cannot be solved except for small instances
* (p426) $\mathcal{P}$ problems solvable in polynomial time by deterministic TMs
* (p426) $\mathcal{NP}$ problems solvable in polynomial time by nondeterministic TMs
* (p426) A Turing machine M is said to be of time complexity T(n) if whenever M is given an input w of length n, M halts after making at most T(n) moves, regardless of whether or not M accepts
* (p431) We say a language L is in the class $\mathcal{NP}$ if there is a nondeterministic TM M and a polynomial time complexity T(n) such that L = L(M),and when M is given an input of length n, there are no sequences of more than T(n) moves of M
* (p433) Our principal metholody for proving that a problem $P_2$ cannot be solved in polynomial time (i.e., $P_2$ is not in $\mathcal{P}$) is the reduction of a problem $P_1$, which is known not to be in $\mathcal{P}$, to $P_2$
* (p434) In the theory of intractability we shall use polynomial-time reductions only. A reduction from $P_1$ to $P_2$ is polynomial-time if it takes time that is some polynomial in the length of the $P_1$ instance. Note that as a consequence, the $P_2$ instance will be of length that is polynomial in the length of the $P_1$ instance
* (p434) Let L be a language (problem). We say L is NP-complete if the following statements are true about L:
	* L is in $\mathcal{NP}$
	* For every language L' in $\mathcal{NP}$ there is a polynomial-time reduction of L' to L
* (p434) Since it appears that $\mathcal{P} \not= \mathcal{NP}$, and in particular, all NP-complete problems are in $\mathcal{NP} - \mathcal{P}$, we generally view a proof of NP-completeness for a problem as a proof that the problem is not in $\mathcal{P}$
* (p434) If $P_1$ is NP-complete, $P_2$ is in $\mathcal{NP}$, and there is a polynomial-time reduction of $P_1$ to $P_2$, then $P_2$ is NP-complete
* (p435) If some NP-complete problem P is in $\mathcal{P}$, then $\mathcal{P} = \mathcal{NP}$
* (p439) The satisfiability problem is: Given a boolean expression, is it satisfiable (can be it true)?
* (p440) (Cook's Theorem) SAT is NP-complete
* (p447) 3SAT is still a problem about satisfiability of boolean expressions, but these expressions have a very regular form: they are the AND of "clauses," each of which is the OR of exactly three variables or negated variables
* (p448) A boolean expression is said to be in conjunctive normal form or CNF, if it is the AND of clauses
* (p448) An expression is said to be in k-conjunctive normal form (k-CNF) if it is the product of clauses, each of which is the sum of exactly k distinct literals
	* Ex. (x + y)(y + z) => 2-CNF
	* (x + y + z)(a + b + c) => 3-CNF
* (p450) Every boolean expression E is equivalent to an expression F in which the only negations occur in literals; i.e., they apply directly to variables. Moreover, the length of F is linear in the number of symbols of E, and F can be constructed from E in polynomial time
* (p451) CSAT is NP-complete
* (p457) 3SAT is NP-complete
* (p458) When we discover a problem to be NP-complete, it tells us that there is little chance an efficient algorithm can be developed to solve it
* (p459) As we introduce new NP-complete problems, we shall use a stylized form of definition, as follows:
	* The name of the problem, and usually an abbreviation
	* The input to the problem: what is represented, and how
	* The output desired: under what circumstances should the output be "yes"?
	* The problem from which a reduction is made to prove the problem NP-complete
* (p478) NP-Complete problems:
	* SAT, CSAT, 3SAT
	* Independent set
	* Node cover
	* Directed and undirected versions of the Hamilton circuit problem
	* Traveling-salesman problem

## Chapter 11 - Additional Classes of Problems
* co-$\mathcal{NP}$: The class of complements of $\mathcal{NP}$ languages
* $\mathcal{PS}$: All the problems that can be solved by a Turing machine using an amount of tape that is polynomial in the length of its input and is allowed to use an exponential amount of time, as long as they stay within a limited region of the tape
* $\mathcal{RP}$: Languages that have an algorithm that runs in polynomial time, using some "coin flipping" or (in practice) a random-number generator. The algorithm either confirms membership of the input in the language, or says "I don't know". Moreover, if the input is in the language, then there is some probability greater than 0 that the algorithm will report success, so repeated application of the algorithm will, with probability approaching 1, confirm membership
* $\mathcal{ZPP}$ (zero-error, probabilistic polynomial): Algorithms for languages in this class either say "yes" the input is in the language, or "no" it is not. The expected running time of the algorithm is polynomial. However, there might be runs of the algorithm that take more time than would be allowed by any polynomial bound
* (p488) $\mathcal{P} \subseteq \mathcal{PS}$, $\mathcal{NP} \subseteq \mathcal{NPS}$, $\mathcal{PS} = \mathcal{NPS}$, $\mathcal{P} \subseteq \mathcal{NP} \subseteq \mathcal{PS}$
* (p492) We define a problem P to be complete for $\mathcal{PS}$ (PS-complete) if:
	* P is in $\mathcal{PS}$
	* All languages L in $\mathcal{PS}$ are polynomial-time reducible to P
* (p492) Suppose P is a PS-complete problem. Then:
	* If P is in $\mathcal{P}$, then $\mathcal{P} = \mathcal{PS}$
	* If P is in $\mathcal{NP}$m then $\mathcal{NP} = \mathcal{PS}$
* (p493) A quantified boolean formula is a boolean expression with the addition of the operators $\forall$ ("for all") and $\exists$ ("there exists")

# See also

# Sources