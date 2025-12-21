---
title: EURISKO-like AGI
created: 2016-04-28
taxonomy:
  tag: [artificial-general-intelligence]
  status: in progress
  readability: 3
---

## Context

## Learned in this study

## Things to explore

# Overview
Use a system similar to NARS where there is a budget as well as some sort of score about the current interest/value of the task
The AI would be responsible of assigning you what to do, it would attempt to do task prioritization for you and make sure to respect schedule as well as current interests

It should be possible to read and import from external systems such as redmine

The system should be able to inform you if there will be any conflicts in your schedule as soon as it is aware of it

You should be able to assign time period in which certain types of tasks may be accomplished (work, personal, etc.)

Use an abstraction like EURISKO where everything is considered within the context of an agenda -> Record on what time was spent, how much progress was made, are we getting closer to our goal, have new tasks been generated from the task that was just executed, etc.

Some tasks may have soft/hard start/end dates, others may be executed at any time

Scheduling API, send in a task name/description and a start/end deadline as well as any dependencies
Simple user interface with the list of tasks for the day
The user can auto complete a task by typing it
The system might guess when the user is awake in order to better schedule work
Assume a push model of integration instead of a pull model
Support some sort of callback mechanism to inform users/external services of necessary

Redmine integration
Add a new field to all types which contains sync metadata (task id)

# See also

# References
