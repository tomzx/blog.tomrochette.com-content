---
title: Flemming Nielson - Principles of Program Analysis (1999)
created: 2016-10-27
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview

# Notes
## Chapter 1 - Introduction
## 1.1 The Nature of Program Analysis
* One common theme behind all approaches to program analysis is that in order to remain computable (tractable?) one can only provide approximate answers
* In general, we expect the program analysis to produce a possibly larger set of possibilities than what will ever happen during execution of the program
* All program analyses should be semantics based: this means that the information obtained from the analysis can be proved to be safe (or correct) with respect to a semantics of the programming language
* Program analysis should not be semantics direct: this would mean that the structure of the program analysis should reflect the structure of the semantics

## 1.2 Setting the Scene
## Reaching Definitions Analysis
* An assignment (called a definition in the classical literature) of the form $[x := a]^\ell$ may reach a certain program point (typically the entry or exit of an elementary block) if there is an execution of the program where $x$ was last assigned a value at $\ell$ when the program point is reached

# See also

# Sources
* Nielson, Flemming, Hanne R. Nielson, and Chris Hankin. Principles of program analysis. Springer, 1999.