---
title: Łukasz Kaiser - Program Search as a Path to Artificial General Intelligence
created: 2016-03-25
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview

## 1 Intelligence and the Search for Programs
* The core of intelligence is neither the knowledge nor the specific method to use it, but the general way to learn from previous experience
* This is not limited to adopting new knowledge, but also includes learning new ways to use what we know, extending it by reasoning, and even improving learning methods to learn more efficiently
* We claim that the informal notion of a method for solving certain tasks can be expressed in mathematical terms as a Turing machine
* To justify this, we use the Church-Turing thesis, the assumption that everything that is computable, any complex behaviour of a system, can be computed or modelled using only a small set of simple abstract operations
* The thesis of Church and Turing justifies that any informally understood method for solving a problem can be defined as an algorithm, a Turing machine that takes the instance of the problem as input and returns the solution
* We have modeled problem solving as searching for Turing machines with specified properties
* Determining if such a machine exists is of course undecidable and the problem is intractable in general, but we can make some additional assumptions
	* We can assume that we do not only want the machine, but also a proof that it satisfies the formula and that such a machine with a proof exists
	* We will not consider the cases when the problem is not solvable or it cannot be proved that the solution is correct
* Learning amounts to improving the procedure (of the agent), so that after a number of problem instances have been solved it will solve other similar instances more efficiently
* The problem we face with such a theoretical solution is that it would not be usable in practice if implemented in a direct way
	* The time required for it to improve to a level of efficiency that would give any tangible results would be enormous

## 2 Theoretical Results
* Let us now consider the Turing machines defined in set theory together with the axioms of set theory as formalized by Zermelo and Fränkel
* Program search problem: Given a formula $\varphi(x_1, ..., x_n)$ in first order logic on the structure defined above (TM and ZFC) with free variables $x_1, ..., x_k$ denoting Turing machines, find a proof of $\varphi(m_1, ..., m_k)$ for some Turing machines $m_1, ..., m_k$.
* Fact 1: There exists an algorithm that computes the solution to the program search problem if any solution exists, so given $\varphi(x_1, ..., x_k)$ it computes $m_1, ..., m_k$ and the proof of $\varphi(m_1, ..., m_k)$, assuming that for some machines such a proof exists.
	* Proof: Since Turing machines, programs, and proofs are enumerable and it can be determined algorithmically whether a sequence of formulas forms a proof of a given claim, we can use the following algorithm to prove this fact:
		1. Set length to 1
		2. Enumerate all k-tuples $m_1, ..., m_k$ of Turing machines shorter than length and all proofs shorter than length and check if there is any proof among these that proves $\varphi(m_1, ..., m_k)$
		3. If the correct machines and proof were found, return them, else increase length by one and return to 2

## 2.1 Program Search in the Standard AI Model
* To be able to construct well-acting agents we have to assume something about the environment, or, at least, something about its probabilistic behaviour
* One sensible assumption is that the environment, or at least the probability distribution of events, is driven by some program (TM)
* We want to create an agent that will behave in a worse way than the optimal agent, if one exists, only for some period of time, and that will later act optimally
* Let our agent store the following internal variables:
	* a list of interwoven events and actions called history, intially empty
	* a program model that models the environment, initially any short one
	* a program actor that models the suspected optimal behaviour of the agent, initially any trivial program
	* two numbers max size and max time, initially set to 1
* We consider a model of the environment $m_1$ to be better than $m_2$ if we can prove that there is an agent that achieves, using $m_1$, a better assessment than any agent can achieve using $m_2$
* When a new event is encountered
	* Append the event to history
	* Search for any program smaller than max size that generates history in less time than max time. Among such environment models, consider only the best ones as defined above, and update model to be one of the shortest of the best programs
	* Search for a proof, shorter than max size, that shows that some program, smaller than max size and halting on every input, can achieve a better assessment in environment model than the program actor. In that case, update actor to be one of the shortest of such programs
	* Increase max time and max size by one
	* Calculate the response of actor to the input event, append the response to history, and output it
* Fact 2: If a Turing machine can describe the behaviour of the environment and there is a provably optimal agent for this environment, then the presented agent gets assessment smaller than the optimal one only for some period of time, and behaves optimally afterwards
	* If the environment is a program, then after some running time it will generate output that distinguishes it from any shorter program
	* Since we assumed that there is a provably optimal agent, this agent and the proof of its optimality have some length
	* When max size exceeds this length, the variable actor will be set to the optimal program. Therefore, the agent will start to behave optimally after detecting the correct environment and the necessary proof

# See also

# Sources
