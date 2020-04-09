---
title: Data profiling
created: 2020-03-30
taxonomy:
  type: post
  category: [Questions, Time series]
  status: finished
---

# Question
What is data profiling?

# Answer
Data profiling is the process of extracting information about data. Given tabular data (think of an Excel spreadsheet), we commonly want to extract the following properties about each column:
* number of rows
* number of cells without data
* number of cells with a value of zero
* number of distinct/unique values
* minimum, mean, median, maximum, quantiles, range, standard deviation, variance, sum
* values distribution
* most common values

The process of data profiling allows a data scientist or engineer to identify quickly potential sources of problems in the data such as:
* negative numbers when numbers should all be positive
* missing values which may need to be imputed or for which the row may have to be removed
* issues with the distribution of values such as class imbalance if we plan to solve a classification problem

In an ideal situation, data profiling reports:
* no missing cells
