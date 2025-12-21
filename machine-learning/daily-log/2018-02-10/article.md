---
title: "2018-02-10"
created: 2018-02-10
taxonomy:
  tag: [machine-learning]
  status: in progress
  readability: 3
---

## Context

## Learned in this study

## Things to explore

# Problems faced

# Overview
I attempted to map data from ManicTime with data in a time log. The idea was that given existing mapped time in the time log (datetime -> project id), I would associate the ManicTime `GroupId` with the time log project id. The `GroupId` was limited such that the `TimelineId` associated with it was only Applications and not the Documents. Thus I would try to learn a mapping from applications to projects. Obviously that does not necessarily mean the model will learn any association using this feature alone, since it is provided with additional data related to the time the measurement was taken (year, month, day, hour, minute)

# See also

# References
