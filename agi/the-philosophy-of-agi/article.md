---
title: The Philosophy of AGI
created: 2017-05-26
taxonomy:
  tag: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study
* Do we initially accept any kind of decision/belief we're taught as being true, or do we go through a phase where many of the conflicting beliefs are brought forth and we try to determine which one appears to be the most appropriate?

## Things to explore
* Describe someone's position on various topics through a questionnaire, which in turn positions them in a multidimensional space (where each dimension is effectively the value given to a question in the questionnaire)

# Overview
Part of the reason I write this, is to understand how an AGI goes through the process of thinking about anything, and by doing so, is able to come up with an "optimal" answer or position on any given topic. It is my hope that by doing so, it will put to light some practices that can be applied to human beings as well.

# Opinions
## Forming and changing opinion
* Opinions should be volatile, that is, they should be subject to change over time, but exist and be relied on at any given time to form composite opinions (opinions based on prior opinions)
* The idea of volatility is that an AGI agent needs to be able to take decisions and proceed further into its thinking
	* In order to take decisions, it needs to make some initial (possibly wrong) assumptions on which it will base its subsequent decisions
		* Without these assumptions, it may not possible to make any decision that is constructive (based on other decisions)
* If at some point arguments are brought up that goes against what the agent believes in, these arguments should be evaluated against the existing framework that has been built
	* In the case the arguments that have been brought up are considered valid (or more valid than the existing framework in place), the affected scaffold of reasoning should be marked as "risky" or "to be re-evaluated", which would prompt the agent to determine the quality of these prior decisions against the new information if they are conflicting or cannot be merged together
* When evaluating a position on a topic, it is important to consider the veracity of the facts presented
* It is also important to evaluate how often an opinion and its related facts have been useful to us compared to our existing position

## Opinions as Reinforcement Learning Problems
* In reinforcement learning, our objective is to maximize total reward
* We can see our beliefs as different states in a state space, where initially we have no beliefs, and through the acquisition of beliefs (actions), we transition from one state (set of beliefs) to another
* Reinforcement learning is about exploration and exploitation
	* Exploration of new states to determine their value (infrequent)
	* Exploitation of existing states, to benefit from the best discovered path so far (frequent)
* Contrary to reinforcement learning as implemented in computers, life cannot start from scratch in order to attempt a new path/sequence of actions to discover the value of the state it arrives at
	* However, it is possible to mentally simulate such given action sequence, either by starting from scratch or by starting from our current state
		* It is important to note that it is hard for human beings to evaluate another state without being biased by their current state. Doing so would require the ability to ignore/forget all of their existing preconceptions/decisions
* Similarly to reinforcement learning, given a metric (function) to determine whether a position is better than another position, it would be possible to order the states from lowest to highest total reward
	* One could say that the meaning of life in this case would be to discover and ascend this reward ladder
* Most human beings agree on a set of "values" which are important to a "good" life: happiness, health, comfort, thus it would seem appropriate to try and encode these values within the state evaluation metric
	* See Maslow's hierarchy of needs

# Unsorted
* One knows as much as there is to learn through (supervised) learning
* Observe as many examples as you can in order to produce the most accurate model
* As a fixed size neural network, we have a limited amount of learning possible. We may either learn to overfit a domain (learn a specialty) or prefer to generalize better (become a generalist)

* Why is it that it is so difficult for us to abandon the way we do things so that we may do them in a radically different way?
	* Is it because our current way has proven itself to work for so long that there's no reason to believe that the other way would be even more successful? Or that it's not worth trading what was acquired to learn something new that, in the end, will only be a trade-off (moving from one local minima to another)?
	* Or is it based on the argument presented in "On Intelligence"/"The Society of Mind", where we build upon previous experiences like an onion, and so abandoning these previous experiences would require a lot of work?
	* It would seem that the brain is averse to change, for instance when trying to implement new habits, and thus radically changing opinion on something would require this change to propagate through the existing relations that exists within the brain

# See also

# References
* https://en.wikipedia.org/wiki/Computational_theory_of_mind
* https://www.quora.com/Is-there-something-like-computational-philosophy
* https://en.wikipedia.org/wiki/Digital_philosophy
* https://plato.stanford.edu/entries/computational-mind/
