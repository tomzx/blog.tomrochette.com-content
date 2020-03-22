---
title: David Silver - The Predictron: End-To-End Learning and Planning (2016)
created: 2017-06-23
taxonomy:
  category: [Machine learning]
  status: finished
---

## Context

## Learned in this study

## Things to explore

# Overview

# Notes
## 3 Predictron Architecture
* The predictron is composed of four main components
	* A state representation $\textbf{s} = f(s)$ that encodes raw input $s$
	* A model $\textbf{s}'$, $\textbf{r}$, $\boldsymbol{\gamma} = m(\textbf{s}, \beta)$ that maps from internal state $\textbf{s}$ to subsequent internal state $\textbf{s}'$, internal reward $\textbf{r}$, and internal discount $\boldsymbol{\gamma}$
	* A value function $v$ that outputs internal values $\textbf{v} = v(\textbf{s})$ representing the future, internal return from internal state $\textbf{s}$ onwards
	* An accumulator, which combines together internal rewards, discounts, and values, into an overall estimate of value $\textbf{g}$

# See also

# References
* Silver, David, et al. "The predictron: End-to-end learning and planning." arXiv preprint arXiv:1612.08810 (2016).
