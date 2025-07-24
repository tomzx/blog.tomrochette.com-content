---
title: Components of a machine learning project
created: 2018-08-05
taxonomy:
  tag: [machine learning]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview
* Data: The units of data from which information/knowledge will be extracted (text, csv, binary, json, databases)
* Extract, Transform, Load (ETL)/Feature extractor pipeline: A set of tools/procedure to convert the data into a format more appropriate for further processing, as well as storing (google refine)
* Model/Architecture: The machine learning model that converts incoming data into predictions/decisions (tensorflow, keras, torch)
* API: HTTP endpoint that can be easily called to pass information to the system or query the model for information (flask)
	* Request data from data source
	* Run inference given data
* Benchmark: Test changes to your model to see how they fare against previous models
* Containers: Encapsulates the tools and procedures used to process data and turn it into information. The container makes it easy to install dependencies and to reproduce the environment on other machines (docker)
* Container-orchestrator: Takes care of running containers according to certain policies, making it possible to scale a project if required (kubernetes, helm)

# See also

# References
* https://www.infoworld.com/article/3198252/machine-learning/data-in-intelligence-out-machine-learning-pipelines-demystified.html
