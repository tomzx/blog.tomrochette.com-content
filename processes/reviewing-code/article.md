---
title: Reviewing code
created: 2019-05-25
taxonomy:
  type: post
  category: [Software development, Processes]
  status: draft
---

* Understand the feature and associated requirements that are supposed to be implemented
* Check code implements the desired feature and that the requirements are completed
* Check code contains tests
* Verify that the build/tests pass
* Check code for code style issues
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

# Reference
* https://en.wikipedia.org/wiki/SOLID
* https://smartbear.com/learn/code-review/guide-to-code-review-process/
