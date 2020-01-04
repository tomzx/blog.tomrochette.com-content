---
title: Reviewing code
created: 2019-05-25
taxonomy:
  type: post
  category: [Software development, Processes]
  status: draft
---

* Verify that the build/tests pass
* Understand the feature and associated requirements that are supposed to be implemented
* Check code implements the desired feature and that the requirements are completed
* Check code contains tests
	* Is all the new code covered by those tests?
* Verify the location of new files
	* Are the files in the right directory?
	* Are they appropriately named?
* Verify classes, methods, functions, parameters naming
	* Are they significant of their purpose?
	* Are they clear enough?
	* Are they respecting the naming convention?
* Does the code respect [SOLID](https://en.wikipedia.org/wiki/SOLID)?
* Consider that when functions/methods signature change, code may now be backward incompatible.
	* Discuss whether this is necessary
	* Backward incompatible changes should be documented
* Are there TODOs that should be completed within this review?
* Check code for code style issues

# Reference
* https://en.wikipedia.org/wiki/SOLID
* https://medium.com/palantir/code-review-best-practices-19e02780015f
* https://phauer.com/2018/code-review-guidelines/
* https://smartbear.com/learn/code-review/guide-to-code-review-process/
* https://nyu-cds.github.io/effective-code-reviews/03-checklist/
