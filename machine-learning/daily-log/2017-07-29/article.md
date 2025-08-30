---
title: "2017-06-29"
created: 2017-06-29
taxonomy:
  tag: [machine-learning]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Problems faced
* How to deal with loading and batching huge amount of data, more particularly in the form of images?
	* Loading thousands of images directly from the filesystem is efficient due to a lot of system calls
	* It seems straightforward to pack these images into more concise structures, such as numpy arrays and using compressed files such as npz
	* However, how does one deal with loading all this data at training time, such that 10 GB of compressed data does not equal 20 GB of RAM used all throughout training?

# Overview

# See also

# References
