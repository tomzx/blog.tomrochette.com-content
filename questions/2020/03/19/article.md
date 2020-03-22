---
title: Data used to do time series forecasting
created: 2020-03-19
taxonomy:
  type: post
  category: [Questions, Time series, Machine learning]
  status: finished
---

# Question
What data do I need to do time series forecasting?

# Answer
There are three values that you must know for each data point of your time series:
* its entity, which represents a unique value identifying the time series (e.g., a product SKU). Without this information, it is not possible to construct a sequence of points since there's no logical grouping between the points.
* its timestamp, which represents the moment in time the data point was recorded. Without this information, it is not possible to construct a sequence of points since there's no sequential ordering between the points.
* its target, which represents the measurement of the data point itself that we want to predict. Without this information, we have effectively nothing to base ourself on.

Such information would look as follow when organized in a table:

| Entity | Timestamp | Target |
|-|-|-|
| A | 1 | 5 |
| A | 2 | 6 |
| A | 3 | 7 |
| B | 1 | 13 |
| B | 2 | 27 |
| B | 3 | 55 |

Additionally, you may also have recorded additional values at the same time, which can be useful source of information when trying to predict a time series.

| Entity | Timestamp | Target | Other value |
|-|-|-|-|
| A | 1 | 5 | 3 |
| A | 2 | 6 | 2 |
| A | 3 | 7 | 1 |
| B | 1 | 13 | 47 |
| B | 2 | 27 | 33 |
| B | 3 | 55 | 5 |
