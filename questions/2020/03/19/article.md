---
title: Data used to solve time series
created: 2020-03-19
taxonomy:
  type: post
  category: [Questions, Time series, Machine learning]
  status: finished
---

# Question
What data do I need to solve a time series problem?

# Answer
There are three values that you must know for each data point of your time series:
* its entity, which represents a unique value identifying the time series (e.g., a product SKU)
* its timestamp, which represents the moment in time the data point was recorded
* its value, which represents the measurement of the data point itself

Such information would look as follow in a table:

| Entity | Timestamp | Value |
|-|-|-|
| A | 1 | 5 |
| A | 2 | 6 |
| A | 3 | 7 |
| B | 1 | 13 |
| B | 2 | 27 |
| B | 3 | 55 |

Additionally, you may also have recorded additional values at the same time, which can be useful

* Entity
* Date
* Target
* Additional variables
