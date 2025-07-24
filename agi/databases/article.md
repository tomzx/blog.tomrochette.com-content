---
title: Databases
created: 2015-11-01
taxonomy:
  tag: [artificial general intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview

# Properties
* Predefined schema (structured)
	* All rows have the exact same format (homogeneity)
* Data is tightly packed together (locality)
* Easy to go at a particular record index since all rows are the same length (uniformity)
* System of index based either on hashing (unique keys) or B-trees (regular indexes, duplicates are allowed) to speed up search
* System of foreign keys to ensure referential integrity (relate to data in a different structure)
* Data can be written (insert/update/delete) or read (select)
* Database normalization principles aim at reducing the amount of redundant data in order to prevent data desynchronization issues (data being different in 2 tables while they should be the same) as well as reducing values to their most atomical concept
* Tables generally represent the entities to be modeled by the system

# Notes
<pre>
<tomzx> well, my understanding of turing so far is that you can represent pretty much anything as a number
<tomzx> except those non-computable numbers
<tomzx> so every word can be represented as a number, phrase (order of words) as a number, documents as a number, thoughts as a number, etc.
<tomzx> basically everything can be labelled
<tomzx> then you can "easily" say A <-> B
<tomzx> in the sense that the entity represented by A is related to the entity represented by B
<tomzx> although I don't think that gets us very far
</pre>

# How to grow a mind
* Universal data structure framework
* Universal language for representing all these form of structure -> using graphs

# See also

# References
* https://www.blazegraph.com/download/
* https://neo4j.com/
