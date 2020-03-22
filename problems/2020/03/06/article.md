---
title: Assessing a dataset quality
created: 2020-03-06
taxonomy:
  type: post
  category: [Problems, Machine learning]
  status: finished
---

# Problem
I've been given a dataset and I need to assess its quality.

# Solution
Use [Pandas Profiling](https://github.com/pandas-profiling/pandas-profiling) to quickly generate a document that will provide you with a first overview of the data.

Your first step should be to look for warnings and messages at the top of the document. Look for entries about missing values, those will point you to variables that may need attention during the data cleaning and data imputation phases of your machine learning problem. As you are doing an assessment, simply indicate that data is missing in these columns and then see if you can determine why by looking at a few examples by loading the data in a pandas dataframe.
