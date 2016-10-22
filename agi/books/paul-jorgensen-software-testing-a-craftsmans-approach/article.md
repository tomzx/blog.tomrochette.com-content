---
title: Paul Jorgensen - Software Testing: A Craftsman's Approach (2008)
created: 2016-10-20
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview

# Notes
## Chapter 1 - A Perspective on Testing
* Error: Mistake, bug
* Fault: result of an error
	* Fault of comission: we enter something into a representation that is incorrect
	* Fault of omission: we fail to enter correct information (missing information)
* Failure: when the code corresponding to a fault executes
* Incident: The symptoms associated with a failure occurrence
* Test: The act of exercising software with test cases
	* 2 goals:
		* find failures
		* demonstrate correct execution
* Test case: A set of inputs and expected outputs

## 1.5 Fault Taxonomies
* Input/Output Faults
* Logic Faults
* Computation Faults
* Interface Faults
* Data Faults

## 1.6 Levels of Testing
* White-box testing at the unit level
* Black-box testing at the system (integration) level

# Chapter 4 - Graph Theory for Testers
## 4.1.6 Condensation Graphs
* Given a graph G = (V, E), its condensation graph is formed by replacing each component by a condensing node
* The condensation graph of a given graph is unique

## 4.1.7 Cyclomatic Number
* The cyclomatic number of a graph G is given by V(G) = e - n + p where
	* e is the number of edges in G
	* n is the number of nodes in G
	* p is the number of components in G

## 4.2.2 Types of Nodes
* A node with indegree = 0 is a source node
* A node with outdegree = 0 is a sink node
* A node with indegree != 0 and outdegree != 0 is a transfer node
* A node that is both a source and a sink node is an isolated node

## 4.2.5 Reachability Matrix
* The reachability matrix of a directed graph D = (V, E) with m nodes is an $m \times m$ matrix R = (r(i, j)), where r(i, j) is a 1 if and only if there is a path from node i to node j; otherwise the element is 0
* The reachability matrix of a directed graph D can be calculated from the adjacency matrix A as $R = I + A + A^2 + A^3 + \ldots + A^k$, where k is the length of the longest path in D, and I is the identity matrix

### 4.2.6 n-Connectedness
* Two nodes $n_i$ and $n_j$ in a directed graph are
	* 0-connected iff no path exists between $n_i$ and $n_j$
	* 1-connected iff a semipath but no path exists between $n_i$ and $n_j$
	* 2-connected iff a path exists between $n_i$ and $n_j$
	* 3-connected iff a path goes from $n_i$ to $n_j$ and a path goes from $n_j$ to $n_i$

## 4.2.7 Strong Components
* A strong component of a directed graph is a maximal set of 3-connected nodes
* Strong components let us simplify by removing loops and isolated nodes

## 4.3 Program Graphs
* Nodes are program statements, and edges flow of control
* Nodes are either entire statements or fragments of a statement, and edges represent flow of control

## 5 Boundary Value Testing
* Four variations of boundary value testing
	* Normal boundary value testing
	* Robust boundary value testing
	* Worst-case boundary value testing
	* Robust worst-case boundary value testing
* The rationale behind boundary value testing is that errors tend to occur near the extreme values of an input variable
* The single fault assumption: Failures are only rarely the result of the simultaneous occurrence of two (or more) faults

# See also

# Sources
