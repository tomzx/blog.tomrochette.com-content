---
title: Jack Copeland - Computable Numbers: A Guide
created: 2015-01-09
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview

# Notes

## 1. Turing Machines
* A scanner and a limitless memory-tape
* Atomic operations: erase, print, move and change state

## 2. Standard Descriptions and Description Numbers
### Standard Description
* Single words of the form $\mathbf{q}_iS_jS_kM\mathbf{q}_l$
	* $\mathbf{q}_i$: Current state
	* $S_j$: Scanned symbol
	* $S_k$: Printed symbol
	* $M$: Direction of movement of the scanner
	* $\mathbf{q}_l$: Next state
* Read and printed symbols: Replace letters and numbers by D followed by *n* repetitions of C
	* -: D
	* 0: DC
	* 1: DCC
	* 2: DCCC
* State: Replace letters and numbers by D followed by *n* repetitions of A
	* a: DA
	* b: DAA
	* c: DAAA
* a-0Rb; b--Rc; c-1Rd; d--Ra;
* aDDCRb; bDDRc; cDDCCRd; dDDRa;

| a-0Rb; | b--Rc; | c-1Rd; | d--Ra; |
|-------|-------|-------|-------|
| DADDCRDAA; | DAADDRDAAA; | DAAADDCCRDAAAA; | DAAAADDRDA; |

* D is used to mark the beginning of a segment

### Description Number
* A standard description can be converted into a description number

| A | C | D | L | R | N | ; |
|---|---|---|---|---|---|---|
| 1 | 2 | 3 | 4 | 5 | 6 | 7 |

| a-0Rb; | b--Rc; | c-1Rd; | d--Ra; |
|-------|-------|-------|-------|
| DADDCRDAA; | DAADDRDAAA; | DAAADDCCRDAAAA; | DAAAADDRDA; |
| 3133253117 | 31133531117 | 311133225311117 | 3111335317 |

## 3. Subroutines
* Programmes used as components of other programmes

## 4. The Universal Computing Machine
* Control the function of a computing machine by storing a programme of symbolically encoded instructions in the machine's memory
* A single machine of fixed structure is able to carry out every computation that can be carried out by any Turing machine whatsoever, i.e. is universal
* Write a description that explains what the machine should do in every configuration in which it might find itself

## 5. Turing, von Neumann, and the Computer
* A *practical* programming code should not only be universal, but must in addition:
	* employ basic operations that can be realized simply, reliably, and efficiently by electronic means
	* enable the "actually important problems" to be solved on the machine as rapidly as the eletronic hardware permits
	* be as easy as possible for the human "problem planner" to work with

## 6. Turing and Babbage
* Differential Engine to produce mathematical tables
* Analytical Engine with memory and a central processing unit
	* Would have had conditional branching (select alternative actions based on the previous actions)
* The Analytical Engine was universal

## 7. Origins of the Term "Computer Programme"
* Programme: a planned sequence of events

## 8. Circular and Cirle-Free Machines
* 0/1 are symbols "of the first kind"
* 2, *, x, blank, etc. are symbols "of the second kind"
* A computing machine is said by Turing to be *circular* if it never prints more than a finite number of symbols of the first kind.
* A computing machine that will print an infinite number of symbols of the first kind is said to be *circle-free*

## 9. Computable and Uncomputable Sequences
* A sequence of binary digits is said to be a *computable* sequence if it is the sequence computed by some circle-free computing machine.
* 010 is NOT a computable sequence
* By definition, no finite sequence is a computable sequence
* Modern writers usually define "computable" in such a way that every finite sequence is a computable sequence (since each of them can be computed)
* Not every infinite sequence of binary digits is a computable sequence (through the diagonal argument)
* The diagonal argument

# See also

# Sources

* Turing, Alan, and B. Jack Copeland. The Essential Turing Seminal Writings in Computing, Logic, Philosophy, Artificial Intelligence, and Artificial Life, plus the Secrets of Enigma. Oxford: Clarendon Press ;, 2004.