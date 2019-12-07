---
title: Automated time series project
created: 2019-02-02
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview
* Define data sets
* Define forecast horizons
* Define data traversal procedure
* Define metrics

# Automated steps
* Merge datasets into a single dataset
* Detect datetime-like columns
* Detect covariates and non-covariates columns
* Convert categorical columns into either one hot encoding or embeddings
* Generate features (lag, moving average, exponential moving average)
	* On covariates
	* On non-covariates
* Backtest multiple models

# Notes
* In an ideal world, I want to do the following:
	* Drag-and-drop many csv files
	* Select the column that indicates the datetime index (out of columns detected as being datetime)
	* Include/Exclude columns from the data
	* Select the column(s) I want the model to learn to predict
	* Select the loss function (what to optimize)
	* Select the metrics to compute
	* Wait for the system to process my data and run it against multiple models
	* Show me the different models and their results
		* Let me visualize the worst offenders (the rows keeping the loss high/non-zero)

# See also

# References
* https://www.datarobot.com/
