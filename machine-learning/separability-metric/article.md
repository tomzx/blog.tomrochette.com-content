---
title: Separability metric
created: 2019-09-29
taxonomy:
  tag: [machine learning, partially-ai-generated, llm=deepseek]
  status: in progress
---

## Context
Given a tabular dataset, what is the theoretical limit on the number of entries we can accurately predict?
Many real world problems are not functions (i.e., they are non-functional relations), that is to say that the same inputs may produce different outputs.
In many cases a hidden variable is missing that would allow us to properly separate the data in a deterministic way.
What should be returned when X's image is a set of distinct values?

## Learned in this study

## Things to explore
* If this [feature importance/selection](https://en.wikipedia.org/wiki/Feature_selection)?
* Is this the [Bayes error rate](https://en.wikipedia.org/wiki/Bayes_error_rate)?
* How to deal with continuous values? Binning? Discretization?

# Overview
In machine learning, we try to minimize the concept of a loss. When a X (set of features) is known to generate different potential Y, such a system will optimize to choose the output with the highest probability.

## Setup
We are given a dataset of features, where we want to predict a feature Y given a set of features X. For some X, we may have different values of Y.

| X | Y |
|---|---|
| 1 | 3 |
| 1 | 4 |
| 1 | 3 |

## Cases
In order to reflect on this problem, we use an iterative approach.

### 1 point
When a dataset is composed of 1 point, then we have 100% separability.

### 2 points
If we have 2 distinct X, then we can separate the dataset into two distinct sets, which leads to 100% separability.

If we have 2 X with the same values, then the separability will depend on the Y value:
* If the Y value is the same for both points, then we have 100% separability, since both X have the same Y.
* If the Y value is different, then we only have 50% separability. This is due to the fact that, given no additional information, the best we can do is to randomly pick one of the two options for Y.

## Definition and Formula

For each unique value \( x_i \) of \( X \), the separability \( S(x_i) \) is defined as the proportion of the most frequent \( Y \) value among all \( Y \) values associated with \( x_i \):

\[
S(x_i) = \frac{\max_{j} N(x_i, y_j)}{N(x_i)}
\]

where:
- \( N(x_i) \) is the total number of instances with input \( x_i \),
- \( N(x_i, y_j) \) is the number of times \( y_j \) appears with \( x_i \).

To obtain an overall separability metric for the entire dataset, we compute a weighted average of \( S(x_i) \) across all unique \( x_i \), with weights proportional to the frequency of each \( x_i \):

\[
S_{\text{total}} = \sum_{i} \left( \frac{N(x_i)}{N} \times S(x_i) \right)
\]

where \( N \) is the total number of instances in the dataset.

### Example Calculation

Consider the following dataset:

| X | Y |
|---|---|
| 1 | 3 |
| 1 | 4 |
| 1 | 3 |
| 2 | 5 |
| 2 | 5 |
| 3 | 6 |
| 3 | 7 |
| 3 | 6 |

For \( X = 1 \):
- \( Y = 3 \) appears 2 times,
- \( Y = 4 \) appears 1 time.
- \( S(1) = \frac{2}{3} \approx 0.6667 \)

For \( X = 2 \):
- \( Y = 5 \) appears 2 times.
- \( S(2) = \frac{2}{2} = 1 \)

For \( X = 3 \):
- \( Y = 6 \) appears 2 times,
- \( Y = 7 \) appears 1 time.
- \( S(3) = \frac{2}{3} \approx 0.6667 \)

Overall separability:

\[
\begin{aligned}
S_{\text{total}} &= \left( \frac{3}{8} \times 0.6667 \right) + \left( \frac{2}{8} \times 1 \right) + \left( \frac{3}{8} \times 0.6667 \right) \\
&\approx 0.75
\end{aligned}
\] 

### Interpretation and Applications

- **High \( S_{\text{total}} \)**: Indicates a dataset where \( Y \) is highly predictable from \( X \), suggesting the feature set provides enough information to predict the \( Y \).
- **Low \( S_{\text{total}} \)**: Suggests ambiguity in \( Y \) given \( X \), indicating the need for additional features that may improve separability.

This metric is valuable in feature selection, where features with higher separability are preferred, and in assessing the inherent predictability of datasets in machine learning tasks.

# Notes
Number of unique input X/Number of points/rows
Given a tabular dataset, compute the separability metric as follow:
* 1 point: 100% separable
* 2 points: given the target feature to predict, if the other attributes can separate two distinct targets, then 100%, if not, 50%
* x points: if the target is different for all points, yet the attributes are all the same, we should expect the metric to be 1/x
* x points with y, z similar targets: in the case that we have x points with similar attributes, but for which there are y and z similar targets (two groups with the same target), we can at best hope for ...
For a dataset with 1 B and 3 C as target values, we expect the metric to be between 0.25 and 0.75 (1/4 and 3/4)
* In an optimization scenario we expect the model to pick predicting C over B as it has a higher likelihood of being correct
* sum(count(points for target x with attributes X)/count(points with attributes X))/count(points)
* It may make sense to have a separability metric per target output (when those are categorical)
* In the case of numerical targets, minimizing for distance between all the targets (clustering) would turn the problem into the categorical form
* Datasets with defined inputs and target are often not functions (i.e, the same inputs may produce different outputs)
* If we compute the separability metric of each individual feature we should expect that having 2 features would provide us with at least the minimum separability of those 2 features and at best that it improves it. If having 2 features doesn't improve the separability, then one feature's information may be contained into the other.
* Selecting the features providing the most separability until things don't improve anymore could be seen as a greedy implementation of feature selection.
* For datasets with numerous features, in order to improve the efficiency of feature selection, one could simply look at the examples which could benefit from an additional feature to increase separability instead of computing the metric over the whole dataset.

# See also

# References
* https://towardsdatascience.com/rip-correlation-introducing-the-predictive-power-score-3d90808b9598
* https://github.com/8080labs/ppscore
