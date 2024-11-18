---
title: Apache fink rate limiting
created: 2024-11-17
taxonomy:
  type: post
  status: draft
  tag: [apache, flink, rate limiting]
---

* Implementation of rate limiting
  * This consist mostly in including a call to a blocking implementation of a rate limiter just before you would execute the code you want rate limited. For example if you are rate limiting calls to an API, you would block just before sending your HTTP request.
* Rate limiting in relation to parallelism
  * When defining rate limiting we generally think of the overall rate limit per second. With Apache Flink parallelism, this number ends up being used by each instance, which makes the rate limit useless in this situation, unless it is divided by the number of parallel instances running the code that is rate limited.