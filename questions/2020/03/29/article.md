---
title:
created: 2020-03-29
taxonomy:
  type: post
  category: [Questions, Time series]
  status: finished
---

# Question
What are the general steps of a time series forecasting project?

# Answer
## Data profiling
Using a tool such as [pandas-profiling](https://github.com/pandas-profiling/pandas-profiling), the dataset provided by the client is profiled and a variety of summary statistics produced, such as the min, mean, median, max, quartiles, number of samples, number of zeros, missing values, etc. are computed for numerical values. Other types of data also have their own set of properties computed.

These summary statistics allow you to quickly have a glance at the data. You will want to look for missing values in order to assess whether there's a problem with the provided data. Sometimes missing data can imply that you should use the prior value that was set. Sometimes it means that the data isn't available, which can be an issue and may require you to do some form of data imputation down the road.

## Data analysis
Common things to look for in time series data are gaps in data (period of time where no data has been recorded), the trend/seasonality/residual decomposition per time series, the autocorrelation and partial autocorrelation plots, distribution of values grouped by certain period (by month, by week, by day, by day of week, by hour), line/scatter plots of values grouped by the same periods.

## Data cleanup
Data is rarely clean and ready to be consumed. This means a number of things: removing values that are invalid, converting invalid values or values out of range into a valid range, splitting cells that have multiple values in them into separate cells (e.g., "10 cm" split into "10" and "cm").

## Data transformation
A variety of transformations can be applied to the cleaned data, ranging from data imputation (setting values where values are missing using available data), applying a function on the data, such as a power, log, square root, differencing (computing the difference with the prior value), going from time zoned date time to timestamps, etc.

## Feature generation
Common feature generation transformations are applied, such as computing lagged values on variables, moving averages/median, exponential moving averages, extracting the latest min/max, counting the number of peaks encountered so far, etc. Feature generation is where you create additional information for your model to consume with the hope that it will provide it some signal it can make use of.

## Establish a baseline
Before attempting to find a good model for the problem at hand you want to start with simple/naive models. The time series naive model

## Experiment

## Performance analysis

## Model selection

## Deployment
