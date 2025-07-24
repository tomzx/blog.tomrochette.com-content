---
title: Software project basics
created: 2019-05-25
taxonomy:
  type: post
  tag: [software development, processes]
  status: draft
---

* Code changes are stored in git
* Setup continuous integration
* Have a testing framework
* Use dependency management
* Define a code standard
* Prefer function/method typing over dynamic types
* On every push to git
	* Code quality check
	* Code style check
	* Unit/functional/integration/system tests
		* Code coverage should be recorded during tests and a report made available
* A project repository must have a README.md explaining how to run the project on your own computer
* A project repository must have a RELEASING.md explaining how to release the code
* Responsibilities are made explicit in terms of roles
* Critical roles, such as project lead, must have a backup/shadow individual
* Setup telemetry, alerts, profiling, logging
