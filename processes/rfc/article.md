---
title: RFC
created: 2019-11-17
taxonomy:
  type: post
  tag: [teamwork, processes, software-development]
  status: draft
---

* Keep all RFCs under a single location
* Uniquely identify RFCs
* Use a shared template
	* Editor: Name &lt;email&gt;
	* Status: Draft/Review/Approved/Abandoned/Implemented
	* Required approvers: Name &lt;email&gt; (why), Name &lt;email&gt; (why), ...
	* Approvers: Name &lt;email&gt; (date), Name &lt;email&gt; (date), ...
	* Created on: &lt;date&gt;
	* Updated on: &lt;date&gt;
	* Overview: A high level description of what you're describing in the document
	* Background/Context: Context relevant to understanding the document
	* Problem description: Describe what you are currently cannot do and want to be able to do
	* Motivation/Why: Why is it relevant to solve this problem now?
	* Drawbacks/Why not: What are the downsides of solving this problem?
	* Proposed solution: What is the best solution proposed?
	* Alternative solutions: What are the alternative solutions considered and why aren't they the proposed solution?
	* Impact and risks: What will be the impact of this change on existing systems, processes, or stakeholders?
	* Unresolved questions: What are the questions that need to be answered but don't have an answer to yet?
	* References: Documents/URLs that can be useful to consult
* If a RFC is abandoned, the reasons why should be made explicit in the document

# References
* https://en.wikipedia.org/wiki/Request_for_Comments
* https://github.com/rust-lang/rfcs/blob/master/0000-template.md
* https://wiki.en.it-processmaps.com/index.php/Checklist_Request_for_Change_RFC
* Sourcegraph RFC template: https://docs.google.com/document/d/1TRVmwpLzTgYWhBqPwkSWpzPYvXI3Z2miJSmBN2G7ygc/edit
* https://about.sourcegraph.com/handbook/engineering/rfcs
* https://blog.pragmaticengineer.com/scaling-engineering-teams-via-writing-things-down-rfcs/
* https://github.com/golang/proposal/blob/master/design/TEMPLATE.md

## Repositories with RFCs
* https://github.com/rust-lang/rfcs
* https://github.com/reactjs/rfcs
* https://github.com/yarnpkg/rfcs
