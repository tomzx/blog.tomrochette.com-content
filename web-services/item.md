---
title: Web services
created: 2015-11-02
taxonomy:
  category: [Programming]
  tag: [api]
  status: draft
---

## Context

![](images/doge.jpg)

## Learned in this study

## Things to explore

* What creates a service database?
* What should happen if a service removes a feature? How should that change propagate to the billing service?

# Overview

Goal: produce a system that reproduces how amazon *internal* API works.

# The ingredients

You will need:
* authentication
* authorization
* a way to bill based on usage
* one or many services *serviced* by the previously listed components

Services should be written such that tracking their usage is secondary (it can be bolted on later on). Develop them as if you were not developing them within an ecosystem that has authentication, authorization and billing in mind.

In the context of this article, we'll think of the following systems:

* An authentication & authorization API
* A billing API
* A service A
* A service B

# Authentication

Authentication is a simple mean to get recognized as a particular user within a system. Once authenticated, you can grant/deny authorizations within the context of the authenticated user.

# Authorization

Authorization makes it possible to do specified things within a service.

If I give you the ability to add users on service A through the `A.addUsers` authorization, then you can do that.

? Where are the authorization defined? Is it the responsibility of the A&A API to know the available list?

What seems the most appropriate convention for naming authorization is a schema that is namespaced, such that service A starts with `A.` and service B with `B.`:

* `A.addUsers`
* `A.removeUsers`
* `B.addUsers`
* `B.runTasks`
* `...`

Depending on how granular you get with permissions, you may end up with as little as 3-5 permissions per app to a hundred or more.

# Billing

The billing service purpose is to know who users what service. It has to track when a service is to expire. It has to be able to explain in enough details how a bill was incurred by a user.

* Features are comparable to various instances of EC2


# Database-based service

Say you offer a service which can run off a database: a small customizable store or a forum. The code is always the same, but clients can customize it to their liking (and enable features they want).

You want to be able to run your service on new servers if demand increases. Furthermore, you'd rather not tie down a user to a specific server for load balancing purposes. What does this imply?

* You need to move sessions out of the service server onto a database
* You have to be able to connect to the appropriate database based on the `HOST` you received

## Sessions

Sessions can be moved to a key-value store such as redis.

## Connecting to the appropriate database

To determine the database credentials to use for your service, you will have to query a database. However, doing this for every request will obviously add an unwanted lag to your requests. At this point, multiple solutions exists:

* Query on a need-to-know basis and cache for X minutes/hours (easiest)
* Poll the configuration database server (where database credentials for every user instance are stored) every X minutes/hours and cache it for that period (easy)
* Construct a network with publisher/subscriber where the configuration database server publishes any changes and services subscribe to those events (hard)

# The whole process from the perspective of a new client

The following depicts what the process of obtaining `service A` would be like for a client. (in italic are the actions the system will take)

1. Register on `my super services`
	1. *Create a new user*
2. Enable `service A`
	1. Configure `service A` to have extensions `X` and `Y`
		1. *Create database for service A AND/OR update its settings to provide extensions X and Y*
		2. *Notify billing that a new billing cycle may begin*
3. Done

At the end of the month, the client is billed.

# The whole process from the perspective of a user of a client's service

The following depicts what the process of using `service A` from our previous client looks like.

1. Go to `service-a.com`
	1. *Find which user instance is linked to service-a.com*
		1. *Cache the given result for further use*
	2. *Configure the database connection to use the given user instance database credentials*
2. Register to use `service a`
3. Done

# Responsibilities


![](images/architecture.png)

## Service provider

* Authenticate users
* Add/Modify/Delete services for a given user
	* Configure properties of services (additional features)
* Communicate with the billing service about changes in provided services to a user

## Billing service

* Track service usage (usage begins/ends, rate, features, discounts)
* Provide/Generate bills
* Store user billing details

## Service

* Offer value to the customer
* Provide a mean to enable features through an API. Only the service configurator may call this API
* Publish a list of extensions users can opt-in

## Service configurator

* Configures the service with the given extensions/parameters
* Provide the service with the database credentials of the running instance

# See also

# Sources
