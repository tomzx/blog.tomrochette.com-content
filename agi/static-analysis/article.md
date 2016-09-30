---
title: Static analysis
created: 2016-09-15
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore
* Spectral graph theory

## Tools
* Graph/tree theory
* Linear algebra

# Overview

* Use adjacency matrices to represent cfg, allows you to do operations easily (get children (nodes to which a given node may go) = V * A, get parents (nodes from which a given node might come from) = V * transpose(A))

# See also
* [PHP Analyzer](php-analyzer)

# Sources
* http://llvm.org/docs/Passes.html
* http://llvm.org/docs/WritingAnLLVMPass.html

## Theory
* https://en.wikipedia.org/wiki/Control_flow_graph
* https://en.wikipedia.org/wiki/Loop-invariant_code_motion
* https://en.wikipedia.org/wiki/Dominator_(graph_theory)
* https://www.youtube.com/watch?v=I0KXjN67hkA
* http://www.viva64.com/en/a/0045/