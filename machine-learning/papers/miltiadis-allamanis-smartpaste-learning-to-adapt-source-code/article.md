---
title: "Miltiadis Allamanis - SmartPaste: Learning to Adapt Source Code (2017)"
created: 2017-05-25
taxonomy:
  tag: [machine learning]
  status: finished
---

## Context

## Learned in this study

## Things to explore

# Notes
## 1 Introduction
* Existing machine learning models of source code capture its shallow, textual structure, e.g. as a sequence of tokens, as parse trees, or as a flat dependency networks of variables
* In this work, we take advantage of two additional elements of source code: data flow and execution paths
* The key insight is that exposing these semantics explicitly as input to a machine learning model lessens the requirements on amounts of training data, model capacity and training regime and allows us to solve tasks that are beyond the current state of the art
* To achieve high accuracy on SmartPaste, we need to learn representations of program semantics
* First an approximation of the semantic role of a variable (e.g., "is it a counter?", "is it a filename?") needs to be learned
* Second, an approximation of variable usage semantics (e.g., "a filename is needed here") is required

## 2 The SmartPaste Task
* Only variable identifiers need to be filled in
* Several identifiers need to be filled in at the same time and thus all choices need to be made synchronously, reflecting interdependencies

# See also

# References
