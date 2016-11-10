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

## 6 Equivalence Class Testing
* Two problems occur with robust forms
	* The specification does not define what the expected output for an invalid input should be
	* Strongly typed languages eliminate the need for the consideration of invalid inputs

## 6.1 Equivalence Classes
* The idea of equivalence class testing is to identify test cases by using one element from each equivalence class. If the equivalence classes are chosen wisely, this greatly reduces the potential redundancy among test cases

## 6.3.1 Weak Normal Equivalence Class Testing
* Weak normal equivalence class testing is accomplished by using one variable from each equivalence class (interval) in a test case
* What can we learn from a weak normal equivalence class test case that fails, that is, one for which the expected and actual outputs are inconsistent?
	* There could be a problem with $x_1$, or a problem with $x_2$, or maybe an interaction between the two

## 6.3.2 Strong Normal Equivalence Class Testing
* Strong normal equivalence class testing is based on the multiple fault assumption, so we need test cases from each element of the Cartesian product of the equivalence classes

## 6.3.3 Weak Robust Equivalence Class Testing
* The process of weak robust equivalence class testing is a simple extension of that for weak normal equivalence class testing - pick test cases such that each equivalence class is represented

## 6.3.4 Strong Robust Equivalence Class Testing
* We obtain test cases from each element of the Cartesian product of all the equivalence classes, both valid and invalid

## 7 Decision Table-Based Testing
## 7.1 Decision Tables
* Decision tables in which all the conditions are binary are called Limited Entry Decision Tables (LETDs)
* If conditions are allowed to have several values, the resulting tables are called Extended Entry Decision Tables (EEDTs)

## 7.7 Guidelines and Observations
* The decision table technique is indicated for applications characterized by any of the following:
	* Prominent if-then-else logic
	* Logical relationships among input variables
	* Calculations involving subsets of the input variables
	* Cause-and-effect relationships between inputs and outputs
	* High cyclomatic complexity
* Decision tables do not scale up very well. There are several way to deal with this - use extended entry decision tables, algebraically simplify tables, "factor" large tables into smaller ones, and look for repeating patterns of condition entries

## 8 Path Testing
## 8.2 DD-Paths
* A DD-path is a sequence of nodes in a program graph such that
	* Case 1: It consists of a single node with indeg = 0 (single sink)
	* Case 2: It consists of a single node with outdeg = 0 (single source)
	* Case 3: It consists of a single node with indeg >= 2 or outdeg >= 2
	* Case 4: It consists of a single node with indeg = 1 and outdeg 1
	* Case 5: It is a maximal chain of length >= 1

## 8.3 Program Graph-Based Coverage Metrics
* Given a set of test cases for a program, they constitute node coverage if, when executed on the program, every node in the program graph is traversed
* Given a set of test cases for a program, they constitute edge coverage if, when executed on the program, every edge in the program graph is traversed
* Given a set of test cases for a program, they constitute chain coverage if, when executed on the program, every chain of length greater or equal to 2 in the program graph is traversed
* Given a set of test cases for a program, they constitute path coverage if, when executed on the program, every path from the source node to the sink node in the program graph is traversed

## 8.3.3.5 Modified Condition Decision Coverage
* MCDC requires
	1. Every statement must be executed at least once
	2. Every program entry point and exit point must be invoked at least once
	3. All possible outcomes of every control statement are taken at least once
	4. Every nonconstant Boolean expression has been evaluated to both true and false outcomes
	5. Every nonconstant condition in a Boolean expression has been evaluated to both true and false outcomes
	6. Every nonconstant condition in a Boolean expression has been shown to independently affect the outcomes (of the expression)
* 1 and 2 translate to node coverage
* 3 and 4 translate to edge coverage
* Unique-Cause MCDC (requires) a unique cause (toggle a single condition and change the expression result) for all possible (uncoupled) conditions
* Unique-Cause + Masking MCDC (requires) a unique cause (toggle a single condition and change the expression result) for all possible (uncoupled) conditions. In the case of strongly coupled conditions, masking (is allowed) for that condition only, i.e., all other (uncoupled) conditions will remain fixed
* Masking MCDC allows masking for all conditions, coupled and uncoupled (toggle a single condition and change the expression result) for all possible (uncoupled) conditions. In the case of strongly coupled conditions, masking (is allowed) for that condition only (i.e., all other (uncoupled) conditions will remain fixed)

## 8.4.1 McCabe's Basis Path Method
* The cyclomatic number of a strongly connected graph is the number of linearly independent circuits in the graph
* We can force this to begin to look like a vector space by defining notions of addition and scalar multiplication: path addition is simply one path followed by another path, and multiplication corresponds to repetitions of a path
* We can check the independence of paths by examining the path/edges traversed incidence matrix. The edges that appear in exactly one path must be independent
* A path is independent if it cannot be expressed in terms of the other paths without introducing unwanted edges
* The baseline method
	* Select a baseline path, which should correspond to some "normal case" program execution (it is advised to choose a path with as many decision nodes as possible)
	* The baseline path is retraced, and in turn each decision is "flipped". When a node of outdegree >= 2 is reached, a different edge must be taken

## 9 Data Flow Testing
## 9.1 Define/Use Testing
* Node $n \in G(P)$ is a defining node of the variable $v \in V$, written as DEF(v, n), if and only if the value of variable $v$ is defined as the statement fragment corresponding to node $n$
* Node $n \in G(P)$ is a usage node of the variable $v \in V$, written as USE(v, n), if and only if the value of the variable $v$ is used as the statement fragment correspond to node n
* A usage node USE(v, n) is a predicate use (denoted as P-use) if and only if the statement $n$ is a predicate statement; otherwise, USE(v, n) is a computation use (denoted C-use)
	* The nodes corresponding to predicate uses always have an outdegree >= 2, and nodes corresponding to computation uses always have an outdegree <= 1
* A definition/use path with respect to a variable v (denoted du-path) is a path in PATHS(P) such that, for some $v \in V$, there are define and usage nodes DEF(v, m) and USE(v, n) such that $m$ and $n$ are the initial and final nodes of the path
* A definition-clear path with respect to a variable v (denoted dc-path) is a definition/use path in PATHS(P) with initial and final nodes DEF(v, m) and USE(v, n) such that no other node in the path is a defining node of $v$

## 9.1.7 Define/Use Test Coverage Metrics
* T is a set of paths in the program graph G(P) of a program P, with the set V of variables
* The set T satisfies the All-Defs criterion for the program P if and only if for every variable $v \in V$, T contains definition-clear paths from every defining node of $v$ to a use of $v$
* The set T satisfies the All-Uses criterion for the program P if and only if for every variable $v \in V$, T contains definition-clear paths from every defining node of $v$ to every use of $v$, and to the successor node of each USE(v, n)
* The set T satisfies the All-P-Uses/Some C-Uses criterion for the program P if and only if for every variable $v \in V$, T contains definition-clear paths from every defining node of $v$ to every predicate use of $v$; and if a definition of $v$ has no P-uses, a definition-clear path leads to at least one computation use
* The set T satisfies the All-C-Uses/Some P-Uses criterion for the program P if and only if for every variable $v \in V$, T contains definition-clear paths from every defining node of $v$ to every computation use of $v$; and if a definition of $v$ has no C-uses, a definition-clear path leads to at least one predicate use
* The set T satisfies the All-DU-paths criterion for the program P if and only if for every variable $v \in V$, T contains definition-clear paths from every defining node of $v$ to every use of $v$ and to the successor node of each USE(v, n), and that these paths are either single loop traversals or they are cycle free

![Rapps-Weyuker data flow coverage metrics](assets/images/rapps-weyuker dataflow coverage metrics.png)

## 9.2 Slice-Based Testing
* A program slice is a set of program statements that contributes to, or affects the value of, a variable at some point in a program
* Given a program P and a set V of variables in P, a slice on the variable set V at statement n, written S(V, n), is the set of all statements fragments in P that contribute to the values of variables in V at node n
* Backward slices refer to statement fragments that contribute to the value of v at statement n
* Forward slices refer to all the program statements that are affected by the value of v and statement n
* In a backward slice S(v, n), statement n is nicely understood as a Use node of the variable v, that is, Use(v, n)
* Given a program P and a program graph G(P) in which statements and statement fragments are numbered, and a set V of variables in P, the static, backward slice on the variable set V at statement fragment n, written S(V, n), is the set of node numbers of all statement fragments in P that contribute to the values of variables in V at statement fragment n
* Five form of USE:
	* P-use: used in a predicate (decision)
	* C-use: used in computation
	* O-use: used for output
	* L-use: used for location (pointers, subscripts)
	* I-use: used for iteration (internal counters, loop indices)
* Two forms of definition nodes:
	* I-def: defined by input
	* A-def: defined by assignment

## 10 Retrospective on Unit Testing
* Low to high semantic content
	* Code-based testing
		* Path testing
		* Data flow testing
		* Slice testing
	* Spec-based testing
		* Boundary value testing
		* Equivalence class testing
		* Decision table testing

## 10.3 Evaluating Test Methods
* We can use the notion of program execution paths, which provide a good formulation of test effectiveness
* When a particular path is traversed more than once, we might question the redundancy
* We assume that a specification-based testing technique M generates m test cases, and that these test cases are tracked with respect to a code-based metric S that identifies s elements in the unit under test. When the m test cases are executed, they traverse n of the s structural elements
* The coverage of a methodology M with respect to a metric S is the ratio of n to s. We denote it as C(M, S)
	* Deals with gaps
	* When this value is less than 1, there are gaps in the coverage with respect to the metric
	* When C(M, S) = 1, algebra forces R(M, S) = NR(M, S)
* The redundancy of a methodology M with respect to a metric S is the ratio of m to s. We denote it as R(M, S)
	* The bigger the value, the greater the redundancy
* The net redundancy of a methodology M with respect to a metric S is the ratio of m to n. We denote it as NR(M, S)
	* The things actually traversed, not to the total space of things to be traversed

# See also

# Sources
* Jorgensen, Paul C. Software Testing: A Craftsman’s Approach. CRC press, 2016.