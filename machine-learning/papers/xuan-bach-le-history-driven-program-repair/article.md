---
title: Xuan-Bach Le - History Driven Program Repair (2016)
created: 2018-02-23
taxonomy:
  tag: [Machine learning]
  status: finished
---

## Context

## Learned in this study

## Things to explore

# Overview
## Comments
* Small dataset, results may not be significative
* Assumes that test cases aren't buggy
* Filtered projects smaller than 100 MB, which seems to be rather excessive (it is supposed to be text after all)

# Notes
## Abstract
* Many real-world bugs cannot be repaired by existing techniques even after more than 12 of computation in a multi-core cloud environment
* Our main insight is that recurring bug fixes are common in real-world applications, and that previously-appearing fix patterns can provide useful guidance to an automated repair technique
* Our technique first automatically mines bug fix patterns from the history of many projects
* We then employ existing mutation operators to generate fix candidates for a given buggy program
* Candidates that match frequently occurring historical bug fixes are considered more likely to be relevant, and we thus give them a priority in the random search process

## I. Introduction
* To truly improve the quality of real-world software as well as the experience of modern software developers, an ideal technique must be both effective (i.e., able to fix many real bugs) as well as efficient (i.e., able to do so in a short amount of time)
* The most important feature differentiating our new technique from the previous work is that it evaluates the fitness or suitability of a candidate patch by assessing the degree to which it is similar to prior bug-fixing patches, taken from a large repository or real patches
* The important novelty in our technique is that, instead of simply using previous fixes to inform the construction of candidate patches, we use fix history to help assess their potential quality, or fitness
* Our history-based APR technique works in three phases:
	* bug fix history extraction
	* bug fix history mining
	* bug fix generation

## II. Proposed Approach
* The overall goal of our approach is two-fold
	* to generate correct, high-quality bug fixes
	* to quickly present such fixes to developers

### A. Bug Fix History Extraction
* For each retained projects, we iterate through its source control history, seeking to collect commits that exclusively concern bug repair
* We seek a complete set of bug-fixing commits using heuristics, though acknowledge that our approach is best-effort
* We deem a commit a bug fix if it simultaneously satisfies the following conditions:
	* Its commit log contains the keywords such as fix, bug fix, while not containing keywords such as fix typo, fix build or non-fix
	* It includes the submission of at least one test case in that commit
	* It involves changes on no more than two source code lines

### D. Mutation Operators
* We reduce the scope of source statement selection to the same file with the target buggy statement. Previous studies have shown that this is adequate for many automated program repair problems
* We heuristically prioritize in-scope statements

## III. Experiments and Analysis
### A. Dataset
* We filter out bugs that involve more than six changed lines since they are typically too difficult for current automated program repair techniques to fix
* We also filter out too difficult bugs considering the semantics of the bugs, even though they involve changes that are syntactically fewer than six lines. For example, one kind of difficult bugs could be adding a field in a class and use that field for fixing bugs in methods

# See also

# References
* Le, Xuan Bach D., David Lo, and Claire Le Goues. "History driven program repair." Software Analysis, Evolution, and Reengineering (SANER), 2016 IEEE 23rd International Conference on. Vol. 1. IEEE, 2016.
