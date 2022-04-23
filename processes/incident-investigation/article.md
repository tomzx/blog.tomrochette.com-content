---
title: Incident investigation
created: 2022-04-14
taxonomy:
  type: post
  category: [Processes]
  status: draft
---

* Define the incident owner
* Define the incident secretary/communicator
* Create and document
	* observations (link to metrics dashboards with absolute timestamps as much as possible)
	* hypotheses/theories
	* who made them
	* when
	* if they have been validated/invalidated
	* the actions taken
	* by whom
	* if it had the desired effect
	* screenshots
	* links to logs
	* etc.
* In the situation where an incident has been caused by the introduction of a code regression, revert the change and deploy as soon as possible
* Start by reducing/relieving the impact of the incident before searching for a root cause
* Use multiple data sources when data sources do not agree
* Diagram all the implicated systems and the relationship to one another in order to identify the potential locations where the problem might be
* Test your hypotheses to verify if they hold or not
