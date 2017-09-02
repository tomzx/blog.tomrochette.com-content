---
title: Max Tegmark - Is "the theory of everything" merely the ultimate ensemble theory? (1998)
created: 2017-09-01
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview

# Notes
## I. Introduction
* The requirements for a theory of everything
	* It should be a self-consistent theory encompassing quantum field theory and general relativity as special cases
	* It should have predictive power so as to be falsifiable in Popper's sense
* It is far from clear which of our experimental results we should expect it to predict with certainty and which it should predict only in a statistical sense

### A. A classification of TOEs
* Two categories of TOEs depending on their answer to the following question: Is the physical world purely mathematical, or is mathematics merely a useful tool that approximately describes certain aspects of the physical world?
	* More formally, is the physical world isomorphic to some mathematical structure?
* A category 1 TOE
	* There are one or more mathematical structures that exist not only in the mathematical sense, but in a physical sense as well
	* Self-aware structures (SASs) might inhabit some of these structures, and we humans are example of such SASs
* A classification scheme
	1. The physical world is completely mathematical
		a. Everything that exists mathematically exists physically
		b. Some things that exist mathematically exist physically, others do not
		c. Nothing that exists mathematically exists physically
	2. The physical world is not completely mathematical
* The beliefs of most physicists probably fall into categories 2 and 1b
* In this paper, we propose that category 1a is the correct one

### B. How to make predictions using this theory
* In any theory, we can make quantitative predictions in the form of probability distributions by using Bayesian statistics
* According to the 1a TOE, we must go further and include our uncertainty about other aspects of mathematical structure as well, for instance, uncertainty as to which equations to use

### C. So what is new?
* Can the 1a TOE be distinguished from the others in practice, or is this entire discussion merely a useless metaphysical digression?
* The task of any theory is to compute probability distributions for the outcomes of future experiments given our previous observations
* Given the subjective perceptions of a SAS, a theory should allow us to compute probability distributions for (at least certain quantitative aspects of) its future perceptions
* Since this calculation involves summing over all mathematical structures, the 1a TOE makes the following two predictions that distinguish it from the others categories:
	* Prediction 1: The mathematical structure describing our world is the most generic one that is consistent with our observations
	* Prediction 2: Our observations are the most generic ones that are consistent with our existence

### D. Is this related to the anthropic principle?
* Yes, marginally: the weak anthropic principle must be taken into account when trying to rule the theory out based on prediction 2
* Prediction 2 implies that the 1a TOE is ruled out if there is anything about the observed Universe that is surprising, given that we exist
* Investigation of the effects of varying physical parameters has gradually revealed that virtually no physical parameters can be changed by large amount without causing radical qualitative changes to the physical world
* In conclusion, when comparing the merits of TOE 1a and the others, it is important to calculate which aspects of the physical world are necessary for the existence of SASs and which are not
* Any clearly demonstrated feature of "fine tuning" would immediately rule out the 1a TOE

## II. Mathematical Structures
* Our proposed TOE can be summarized as follows:
	* Physical existence (PE) is equivalent to mathematical existence (ME)
* Mathematical existence is merely freedom from contradiction
	* If the set of axioms that define a mathematical structure cannot be used to prove both a statement and its negation, then the mathematical structure is said to have ME

### A. Formal systems
* A formal system consists of
	* A collection of symbols which can be strung together into strings
	* A set of rules for determining which such strings are well-formed formulas, abbreviated WFFs and pronunced "woofs" by logicians
	* A set of rules for determining which WFF are theorems

### B. Boolean algebra
* The formal system known as Boolean algebra can be defined using the symbols "~", "$\vee$", "[" and "]" and a number of letters "x", "y", ... (these letters are referred to as variables)
* The set of rules for determining what is a WFF are recursive
	* A single variable is a WFF
	* If the strings S and T are WFFs, then the string $[\sim S]$ and $[S \vee T]$ are both WFFs
* The rules for determining what is a theorem consist of two parts: a list of WFFs which are stated to be theorems (the WFFs on this list are called axioms), and rules of inference for deriving further theorems from the axioms
* The axioms are the following
	* $[[x \vee x] \mapsto x]$
	* $[x \mapsto [x \vee y]]$
	* $[[x \vee y] \mapsto [y \vee x]]$
	* $[[x \mapsto y] \mapsto [[z \vee x] \mapsto [z \vee y]]]$
* The symbol "$\mapsto$" appearing here is not part of the formal system. The string "$x \mapsto y$" is merely a convenient abbreviation for "$[\sim x] \vee y$"

# See also

# References
* Tegmark, Max. "Is “the theory of everything” merely the ultimate ensemble theory?." Annals of Physics 270.1 (1998): 1-51.