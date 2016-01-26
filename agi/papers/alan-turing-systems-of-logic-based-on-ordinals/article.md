---
title: Alan Turing - Systems of Logic Based on Ordinals (1938)
created: 2015-01-01
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview

# Notes

Mathematical reasoning may be regarded rather schematically as the exercise of a combination of two faculties, which we may call intuition and ingenuity.

**Intuition:** making spontaneous judgments which are not the result of conscious trains of reasoning.
**Ingenuity:** aiding the intuition through suitable arrangements of propositions, and perhaps geometrical figures or drawings.

Let $G$ be an arithmetic formula that is not provable in the system of arithmetic.

Let $G_1$ be the incomplete formal system of arithmetic with G as one of its axiom.

Based on the Gödel construction, we can apply this ad infinitum: $G_1$, $G_2$, $G_3$, ....

Let the system of arithmetic that forms the starting point of this infinite progression be called $L$. The result of adding $G$ to $L$ is called $L_1$, the result of adding $G_1$ to $L_1$ is $L_2$, and so on. Taken together, the systems in the infinite progression $L$, $L_1$, $L_2$, $L_3$, ... form a non-constructive logic.

There are a lot of systems in the progression $L$, $L_1$, $L_2$, $L_3$, .... There is a system that contains the theorems of every one of the systems $L_i$, where $i$ is a finite ordinal. This system is called $L_\omega$ ($\omega$ being the first transfinite ordinal number).

$L_\omega$ is "bigger" than any of the systems $L_i$ in the sense that any $L_i$ considered, $L_\omega$ includes all of its theorems (but not vice versa).

But even $L_\omega$ has a true but unprovable $G_\omega$. Adding $G_\omega$ to $L_\omega$ produces $L_{\omega+1}$. The progression of systems $L$, $L_1$, $L_2$, $L_3$, ..., $L$, $L_{\omega+1}$, $L_{\omega+2}$, $L_{\omega+3}$, ... is an example of an ordinal logic.

## o-machines
Turing introduces a new type of machine which is able to determine, given the description of a machine **m** if it is circle-free. In other words, that machine is able to answer to the halting problem.

In the same manner as was demonstrated that no Turing machine can decide if a given Turing machine description number is circle-free, he proves the existence of mathematical problems of the same nature for o-machines. In other words, no o-machine can decide, of arbitrarily selected o-machine description numbers, which are numbers of circle-free o-machine.

## 2. Effective calculability. Abbreviation of treatment
* A function is said to be "effectively calculable" if its values can be found by some purely mehanical process.

# See also

# Sources
