---
title: A procedure for writing programs
created: 2015-10-22
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Learned in this study

## Things to explore

* What are the steps one goes through when writing a program/algorithm to solve a specific problem?

# Overview

When I want to write a program, may it be small or big, I generally approach it in a top down fashion. This means I first go over the high level concepts that I will need to make it work. Then I go into each concepts and drill down until I get to the implementation details.

Here's a list of the many things that are considered while writing a program:

* Pre-requirements (what is needed in order to develop it)
* Dependencies (what it needs to know about when running)
* Relationships (what will depend on it and what it will depend on)
* Requirements (what does it need to do)
* Performance (what are its constraints)
	* Time (how fast should it return a result)
	* Space (how much space should it use to do its task)


Here's a few questions I will ask myself before starting to write some code.

* Is this functionality already available in the existing codebase?
* Is there a library that already does this (either in the project or online)? partially or completely?
* Is there an implementation already available online? Can I produce a better implementation?
* Do I know how to implement this?


```mermaid
graph TD;
	0[Is this functionality already available in the existing codebase?]
	0 --Yes--> 100[Use it]
	0 --No--> 1["Is there a library that already does this (either in the project or online)? partially or completely?"]
	1 --Yes--> 101[Use it]
	1 --No--> 2[Is there an implementation available online?]
	2 --No--> 3[Do I know how to implement this?]
	3 --No--> 4[Search how to implement it]
	3 --Yes--> 5[Implement it]
	2 --Yes--> 102[Can I produce a better implementation?]
	102 --No--> 104[Use existing implementation]
	102 --Yes--> 103[Implement it]
```