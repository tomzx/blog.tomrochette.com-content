---
title: General AI Challenge - Round 1
created: 2017-03-17
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---


# Gradual learning

* Sequence learning
* Reinforcement learning based (using a reward signal)
* Different tasks, no signal as to the type of task to solve or whether the task has changed

# Problems

* When have we switched task?
* When should we drop all knowledge we think we've acquired since we moved onto a new task?
* Is it possible to determine how much previous knowledge we can keep if we discovered we have switched task?
	* In other words, can we determine the iteration at which the new task began?
* How can we design a curriculum for which we have to punish as little as possible?
* Can we determine if a given task is easier than another task? Is the Kolmogorov complexity a good metric that can be used as a way to order these

# Systems/Functions

* Task detector/classifier: Which task appears to be under execution?
* Task switch detector: Have we switched onto a new task?
* Task executor: Execute the task that is thought to be under way.
* Task encoder: Encode the knowledge required to accomplish the task.

## Functions

* Set internal memory: Used to remember previous input and/or input/output that led to a reward.
* Unset internal memory: Used to forget about a previously set memory block as the task may have changed since and the information within the memory block is now irrelevant/incorrect.
* Copy a memory block: Used to copy a memory block within the working memory workspace. The copied memory block can then be manipulated if required.

# Comments on microtasks

* I think it would make more sense if the microtask 2.4 - Learning to copy input to output was the first task of the agent. The idea is that initially an agent does not know anything. The next thing it should be able to do is mimic the environment, namely, copy it exactly. All the tasks prior to this task assume that the agent knows the other valid symbols that can be inputted/outputted, while a simply copy agent would only need to know about what it has seen so far.

# Additional microtasks

* Print any of the previous input symbols (of the current task).
* Generate any action in response to any input.
* Return no action (space/silence) to any input.
* Generate anything you know how to generate: Babies are not known to be able to speak right out of the womb. Thus, it makes little sense to expect a machine to do the same. However, babies are able to express themselves through some minimalistic communication methods, which they will improve over time. In a similar fashion, the agent may only be able to express itself through a binary signal, which it would have to learn how to concatenate  0/1 to produce the appropriate byte signal.
* Copy with n-iterations delay.
* Simple Caesar cipher (special case of "Learning a mapping between symbols from input to Output: 1 to 1").
	* The goal here would be to induce the complete relation out of a few examples.
* Tasks with stochastic reward: positive and negative rewards are sometimes given, but it may happen we don't return any reward.
* Learning a mapping between symbols from input to output: N to M: Map a single symbol to more than one other symbols. The purpose is to show that more than one answer may be correct.
* Regex learning

The following tasks purpose are to introduce complexity in the agent decisions.

* Task with opposite reward: return positive reward when it should be negative and negative when it should be positive (punishing for the expected behavior).
* Stochastic reward for good/bad behavior.

I need a way to determine in what order these tasks should be accomplished in relations to the other tasks.

# Other types of microtasks

This section describes other types of ways an agent could learn.

* Multiple stream association: Instead of being given a single byte stream, the agent observes 2..n  byte streams and must discover the association between the streams (if any).
* Microtasks attached with an external agent: Different agents have different ways to reward for a given task, some may punish (negatively reward) you for a specific task while another agent may reward you.
* Offer an initial set of input-reward on which the agent can bootstrap itself (learning by examples).
* Have the agent initiate the interaction with the environment, the environment deciding whether or not to reward the agent.

# Things that have been tried

* Naive byte map.
* A solver per difficulty/problem step, with a solver selector that select the solver that has the currently highest reward streak to determine the next action to take based on input (works up to Micro5Sub1Task).
	* A similar system, but instead of writing the solvers myself, I used the learners provided in the test_micro_tasks file.
		* These learner are expected to learn only a single instance, which means they break as soon as a new instance would be given to them. Furthermore, some of the learners have been written knowing the problem subset of byte allowed, which means that it breaks for the general case.
* A solver per difficulty/problem step, with a solver selector that select the action that is the most suggested.

# Ideas

* A system that can copy/move/duplicate/multiply/map symbols

# Questions

* Given two agents, which one is better as an indicator of success:

	* a lifetime reward (positive and negative)
		* Indicates whether it has been more right than it has been wrong


* a lifetime positive reward (positive only)
		* Indicates only the number of times it was right
		* Does not consider mistakes

# TODO

* Observe the input samples presented
* Learn from the mistakes of others (most solvers are only learning the good behavior, but not the bad ones)
* Extract a list of features based on the different micro tasks and build a neural network using this feature vector

# Observations/Notes

* In a multi-agent system, it is only when the system takes the action of the agent that this agent may be directly punished/rewarded. If its action is not taken, but the other action ends up being rewarded, it does not necessarily mean that the agent action would have been wrong (we cannot conclude anything).


* Gradual learning does not mean that we can't learn orthogonal tasks (or that we have to learn by composition over previous tasks all the time). Learning new things without having to reuse existing knowledge makes it generally easier to grasp the new concept, which can then be merged with existing concepts.
* To accomplish a task, you need to have the basic components to get to the solution. If we were to map this to the linear algebra domain, we'd say that the the basic components are basis vectors, for which a task is the composition of a sequence of basis vectors and where a solution is a point in space. Thus, the through the composition of basis vectors it is possible (or not) to get to a solution. Furthermore, like in linear algebra, if you do not have the necessary basis vectors (components) to reach all point in the space, it may be impossible to reach certain solutions.

## Transcribed notes

* Sequence of inputs, parts of a more complex input
* Hierarchical recognition of more complex constructs
* Construction of complex token detection and association with a task
* State machine based on token parsed
* Input chains and output chains (chains are sequence of symbols)
* Recognize/Categorize similar types of tasks by observing the input/output/reward streams
* Adaptive attention span, which increases the length of the memory buffer allocated to tasks as we progress toward more difficult tasks
* How do you get an agent that is more advanced to recognize earlier tasks?
		* Observe positive/negative rewards (and their associated input/ouput chains)
		* Hypothesize what the current task is
				* Implies that the agent knows how many different tasks there are and what those tasks are
						* Might be open to unsupervised learning/clustering?
* How do you recognize you are dealing with "commandX" vs "c" "o" "m" "m" "a" ... (a particular sequence vs a random sequence)?
* How do you detect (input) and construct (output) structure?
* Track the sequences of symbols and their count
		* Variable length buffer and the count for each time they were seen

| Length | States                         |
| ------ | ------------------------------ |
| 1      | $255^1 = 255$                  |
| 2      | $255^2 = 65025 $               |
| 3      | $255^3 =  16581375$            |
| 4      | $255^4 =  4228250625$          |
| 5      | $255^5 =  1.08 \times 10^{12}$ |
| ...    | ...                            |
| n      | $255^n$                        |

# Similar problems

* Predicting the stock market (when are we moving to a different trend/problem? Based on the current trend/problem, what is the appropriate action?)

# Current WIP approach

* Provide the agent with a fixed-size memory of the input/output/reward stream so that it may reason using it.
* Process input as a stream of tokens, similar to how a parser would process a bit/stream of code.
* Similar to how a computer works, an action (operation) would have operands.
* At some point you start to need a callstack and the ability to stack function calls.

# References

* http://wiki.opencog.org/w/CogPrime_Overview#Measuring_Incremental_Progress_Toward_Human-Level_AGI