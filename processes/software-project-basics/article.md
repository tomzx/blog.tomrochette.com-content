---
title: Software project basics
created: 2019-05-25
taxonomy:
  type: post
  tag: [software-development, processes]
  status: draft
---

* Code changes are stored in git
* Setup continuous integration (e.g., GitHub Actions)
* Use dependency management (e.g., uv)
* Have a testing framework (e.g., pytest)
* Define a code standard, enforced through tools and not documentation (e.g., ruff)
* Prefer typed function/method over dynamic types
* On every commit to git
	* Code quality check
	* Code style check
	* Unit/functional/integration/system tests
		* Code coverage should be recorded during tests and a report made available
* Prior to pushing
	* Use an LLM tool to review the changes to identify potential issues
* On pushes, the CI should
	* Code quality check
  * Code style check
  * Unit/functional/integration/system tests
* A project repository must have
	* a `README.md` explaining how to run the project on your own computer
	* a `RELEASING.md` explaining how to release the code
	* a `CHANGELOG.md` listing relevant changes made
* Responsibilities are made explicit in terms of roles
* Critical roles, such as project lead, must have a backup/shadow individual
* Setup telemetry, alerts, profiling, logging
