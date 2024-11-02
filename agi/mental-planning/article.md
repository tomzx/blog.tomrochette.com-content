---
title: Mental planning
created: 2016-07-02
taxonomy:
  tag: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore
* How do we support overlapping operations?
* How can we build an extremely modular planning system where most actions/functions can be done through a variety of implementation? (This is basically the definition of a strategy) However in our case the strategy may be tangle with the operation to accomplish
* What generates variability in a plan? (Why is it that sometimes ordering food will take precedence over thinking about the food that is available closer to our current location?)

# Overview
In the following sections I'll attempt to analyze a couple of problems in order to better understand how I personally think about a task, how I deconstruct it, attempt to solve it and the various aspects of the task that ends up being considered. The objective is manyfold, one of them being to determine the complexity of various tasks, another being to observe whether or not certain types of tasks end up "exploding", in the sense that even though they may appear simple on the surface, if you destructure them, you soon realize that they are composed of an enormous amount of subtasks.

## Sorting
Define what you want to accomplish
I want to sort a list

Extract what is to be done (based on verbs)
Sort

Extract concepts (based on nouns)
A list

Define the particularities of the accomplished operations
Sorted ascending


Todo:
Determine how many verbs there are
Determine on how many entities a verb can apply

## Build a tree structure
I want to build a tree according to its leaves

Build = Construct

Tree (output)
Leaves (input)

## Satiate one's hunger
I am hungry

Determine what to eat
Evaluate how hungry I am

Determine what is available
Access memory to recall food locations
Access memory to recall what is available at each locations

Evaluate what best matches my current cravings
Evaluate meal preparation duration
Evaluate current energy
Evaluate urgency
Evaluate potential alternatives

I want you to eat an apple

What does “eat an apple” entails?
Get an X(apple)
Determine closest proximity to X(apple)
Access memory to determine potential locations
Evaluate distance
Walk toward location
Visually confirm presence

Pick the apple
Move arm
Grab apple
Move arm

Put X(apple) in mouth
Move arm - this could be done through other means
Open mouth

Chew apple

Move apple away from the mouth

What defines appropriate boundaries for functions?
When does “eating an apple” starts and stops
Is this function responsible for finding an apple to eat?
What about finishing the apple?
What about throwing it in the trash when done?

# See also

# References
