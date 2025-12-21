---
title: Mass refactoring
created: 2016-06-03
taxonomy:
  tag: [artificial-general-intelligence]
  status: in progress
  readability: 3
---

## Context

## Learned in this study

## Things to explore
* How to properly build a PR since refactoring can have a major impact on the code?
* What are the reasons against code refactoring?
	* Applying refactoring that go against the developers coding guidelines
* Is it possible for two automated agents (a refactorer and a verifier) to exchange refactoring changes without the need for human intervention?

# Overview

# Procedure
* Scan github.com for a list of projects in your target language, possibly starting with the most popular projects
* Automatically clone many projects to one or many machines
* Apply all refactoring supported by your refactoring tools
* Create a commit per semantic change
* Create a commit with all the changes
* Obtain the amount of code added/removed and compute how much impact the refactoring would have on the project
* Automatically submit a pull request to the projects, indicating the refactoring that was applied

# See also

# References
