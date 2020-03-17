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
* Verify code implements the desired feature and that the requirements are completed
* For a bug fix, verify that the fix is applied at the right location and will not "fix the symptoms, not the cause"
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
* In a weak typed or type hinted language, are parameters and return of functions/methods typed?
* Check code for code style issues

When reviewing
* Provide specific and actionable feedback
* Clearly mark nitpicks and optional comments
* Assume competence
* Provide rationale or context
* Consider how comments may be interpreted
* Don't criticize the person, criticize the code
* Don't use harsh language

# Reference
* https://en.wikipedia.org/wiki/SOLID
* https://medium.com/palantir/code-review-best-practices-19e02780015f
* https://phauer.com/2018/code-review-guidelines/
* https://smartbear.com/learn/code-review/guide-to-code-review-process/
* https://smartbear.com/learn/code-review/best-practices-for-peer-code-review/
* https://nyu-cds.github.io/effective-code-reviews/03-checklist/
* https://google.github.io/eng-practices/
* https://testing.googleblog.com/2019/11/code-health-respectful-reviews-useful.html
