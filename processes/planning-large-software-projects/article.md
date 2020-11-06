---
title: Planning large software projects
created: 2020-11-06
taxonomy:
  type: post
  category: [Software development, Processes]
  status: draft
---

* List all the features you would like to develop
* Define an appetite for the task (day, week, month, quarter)
* Identify the features where the appetite differs between individuals and discuss them to reach consensus
* Define the roles necessary to complete the task
* Identify dependencies between features
* Categorize the dependencies
	* Soft: somewhat depends on this other feature but isn't blocked by its absence from the codebase
	* Hard: depends on this other feature and is blocked by its absence from the codebase
* Prioritize the features
	* [Use the RICE framework](https://about.gitlab.com/handbook/product/product-processes/#using-the-rice-framework)
	* Priority can also be skipped if using ROI as prioritization metric
* Estimate the value of a features in dollars
* Calculate a ROI (return on investment) as the estimated value of the feature divided by the defined appetite
* Order tasks according to dependencies and ROI
