---
title: On Designing and Deploying Internet-Scale Services
created: 2021-05-21
taxonomy:
  category: []
  status: in progress
---

* 3 tenets
	* Expect failures
	* Keep things simple
	* Automate everything
* The entire service must be capable of surviving failure without human administrative interaction
* The best way to test the failure path is never to shut the service down normally. Just hard-fail it
* The acid test: is the operations team willing and able to bring down any server in the service at any time without draining the work load first?
	* If they are, then there is synchronous redundancy (no data loss), failure detection, and automatic take-over
* Large clusters of commodity servers are much less expensive than the small number of large servers they replace
* Server performance continues to increase much faster than I/O performance, making a small server a more balanced system for a given amount of disk
* Power consumption scales linearly with servers but cubically with clock frequency, making higher performance servers more expensive to operate
* A small server affects a smaller proportion of the overall service workload when failing over
* Two factors that make some services less expensive to develop and faster to evolve than most packaged products are
	* the software needs to only target a single internal deployment
	* previous versions don't have to be supported for a decade as is the case for enterprise-targeted products
* Basic design tenets
	* Design for failure
	* Implement redundancy and fault recovery
	* Depend upon a commodity hardware slice
	* Support single-version software
	* Enable multi-tenancy
* Each pod should be as close to 100% independent and without interpod correlated failures
* What isn't tested in production won't work, so periodically the operations team should a fire drill using these tools
* If the service-availability risk of a drill is excessively high, then insufficient investment has been made in the design, development, and testing of the tools
* Some form of throttling or admission control is common at the entry to the service, but there should also be admission control at all major components boundaries
* The general rule is to attempt to gracefully degrade rather than hard failing and to block entry to the service before giving uniform poor service to all users
* Partitions should be infinitely-adjustable and fine-grained, and not be bounded by any real world entity
	* We recommend using a look-up table at the mid-tier that maps fine-grained entities, typically users, to the system where their data is managed
* Expect to run in a mixed-version environment. The goal is to run single version software but multiple versions will be live during rollout and production testing
* Best practices in designing for automation include
	* Be restartable and redundant
	* Support geo-distribution
	* Automatic provisioning and installation
	* Configuration and code as a unit
	* Manage server roles or personalities rather than servers
	* Multi-system failures are common
	* Recover at the service level
	* Never rely on local storage for non-recoverable information
	* Keep deployment simple
	* Fail services regularly
* Dependency management
	* Expect latency
	* Isolate failures
	* Use shipping and proven components
	* Implement inter-service monitoring and alerting
	* Dependent services require the same design point
	* Decouple components
* Testing in production is a reality and needs to be part of the quality assurance approach used by all internet-scale services