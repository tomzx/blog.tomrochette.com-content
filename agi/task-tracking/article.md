---
title: Task tracking
created: 2016-07-20
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore
* Is it possible to evaluate a task execution objectively without considering the agent objectives/goals?
* Should a decay function be applied to the metric used to order tasks? It is not useful if all tasks decay linearly (as the order will be preserved)

# Overview
List tasks
Associate tasks with other tasks and tasks hierarchies
Assign a priority
A task may be related to the accomplishment on many tasks
Each time a task is executed, evaluate the value of the task in regard to some global evaluation function
* Pleasure
* Drain
* Monetary reward
* Experience
* Novelty
* Repetition/Monotonous
* Timespan until deadline
* Timeframe/time horizon
* Expected timespan before the next reward
* Expected duration
* Required effort
A metric should provide guidance as to whether or not continue to do this task in the future
A metric should provide guidance as to which task should be accomplished next

Tasks grouped/tagged by action
* Actions
* Read
* Write
* Think/Reflect
* Watch
* Listen
* Speak

Example
* Reading
	* Reading about AGI
		* Reading about automated programming
		* Reading about automated refactoring
		* Reading about universal artificial intelligence
		* Reading about intelligence

Observations
* Some things may not be rewarding/valuable at one point in time while our may be later on (due to the inability to understand or to use the task)

How should a work session be assessed?
* Should it be a 1 to 10 score?
* Should it be some sort of reordering operation? (In other words, do this after this has been executed)

List creation and maintenance procedure
* Start with an empty list
* Add needs to the list
* Associate needs to one another
* Organize needs
* Convert needs into actions
* Define expected action duration
* Define order/dependencies

Prioritization methods
* Random
* Prioritized once
* Dynamically prioritized
* Topological
* Best first
* Critical path
* Hierarchically
* Contextually
* Hybrid/multi methods
* Consensus
* Average with some statistical measure (standard deviation)
* Prioritization threshold (only the top x priorities defined, each item compared against the bottom of the stack)
* Push by x in the task, then progressively more as the task doesn't get executed

Task properties
* Name
* Description
* Start/End date
* Contexts
* Tags
* Deadline
* Dependencies (tasks/people/context/resources)
* Estimated effort
* State(active/completed/cancelled)
* Start/End time of execution period
* Evaluation of the execution period (score/would redo/not do)
* Notes

Operations
* Execute
* Delay
* Kill
* Split

# See also

# References
