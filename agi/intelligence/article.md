---
title: Intelligence
created: 2016-02-17
taxonomy:
  tag: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore
* At what point does intelligence emerges from non-intelligence?
	* (GEB p411) Turing suggests that above a certain level of complexity a qualitative difference appears, so that "super-critical" machines will be quite unlike the simple ones hitherto envisaged
	* I believe intelligence emerges from complexity. By stacking simple concepts onto one another, intelligence appears.
* To understand intelligence as a phenomenon must include an understanding of learning (J.R. Quinlan Induction of decision trees)
* How can AGI/intelligence emerge out of randomness? Can it emerge out of randomness (or is that too improbable/operationally impossible)?
* What is intelligence? Is it measurable?
	* Should intelligence be measured against time? (in other words, faster = better)
* Can intelligence be measured indirectly through tests such as nearest neighbor of faces?
* How can we recognize a superintelligence?
* Intelligence is the ability to best fit a probability distribution, the closer you are to the true distribution, the more intelligent you appear/are

# Overview

# Recognizing intelligence
## Relative to your own
### Below
* Recognition of errors you made in the past
* Make more mistakes
* Cannot resolve problems one can
* Solves problem more slowly
* Solution is not appropriate for the problem at hand
* Unable to predict your behaviors, recognizes none of your patterns

### In the same range
* Make the same amount of mistakes
* Problem resolution in which there is trade-off between the solutions (no real winner)
* Similar efficiency in problem resolution
* Preference for different tools
* Disagreement on the most important aspect of a solution
* Able to predict some of your behaviors, recognize some of your patterns

### Over
* Make less mistakes
* Recognition of more effective solutions to similarly faced problems
* Ability to resolve problems one cannot resolve himself
* Solve problems faster
* Problems are more thoroughly resolved and in greater depth
* Can predict your behaviors, recognizes most of your patterns

# Measuring intelligence
* Factors of interest in the formula
	* Memory
	* Speed
	* Number of mistakes

# Indicators of human intelligence
* Tries to improve the intelligence of others
* Listens instead of talking
	* Absorbs as much information as possible
	* Does not show what they might not know
* Knows about a wide variety of topics
* Has hidden abilities that may only be used when necessary
* Does not attempt to make others look stupid
* Does not dwell on things when they go wrong, as they can always be corrected
* Is curious

# Quotes
> Do we want to copy the structure of human intelligence (i.e. the way our brains work), our behavior (i.e. make the same mistakes as humans), our capabilities (i.e. do stuff previously only humans could do), our cognitive functions (e.g. ability to perceive, learn, reason, etc.), or the principle of intelligence/rationality?

**Source:** https://www.reddit.com/r/artificial/comments/4rzp2m/is_anyone_in_aimachine_learning_community_working/d55mwjh

# Unformatted
Intelligence in itself is nothing more than zeros and ones. Given an input stream of seemingly random 0 and 1, "an intelligent being" will start to output its own stream of 0 and 1 in return.
<!-- Why would it start outputting and not stay silent? What if it has no ability to actually output? -->
This generates communication between two or more entities.
At this point however the problem is that communication is nothing more than junk being sent between entities. What can happen is that an entity might start outputting a stream based on an input stream that went through a function $f(x)$ (for example $f(x) = x$, $f(x) = x!$).

Through this function, it would start to look as if the entity had some form of intelligence as it is manipulating the input in some deterministic/reproducible manner. Thus, the logical next step would be more complex functions acting on the input stream, functions accepting multiple input streams at once, functions accepting its own output as input stream (feedback). An entity then slowly starts to look like a neural network implementation where each node is given a function and some form of activation function (which will output based on the node function output).

One of the things I wonder about is how functions get generated and why they decide to stay in memory and begin to be executed.
There is also the question of how an entity can determine that its output is being used by another entity, and if that former entity is basing its own thoughts on the latter entity, how will it be able to determine if that it is the case? Is that a problem? How would an entity be able to determine it is "discussing" with a clone of itself? Would it have to execute all its own functions against the clone to figure that out? If the clone is a superset of the initial entity, that clone would implement all of the original entity functions yet implement additional functions
how would the entity be able to probe for missing or additional (or different) functions?
<!-- The goal here I think is to determine when one is influenced by others, which themselves are influenced by us. -->

How is an entity suppose to evolve from what is a seemingly random input stream and start recognizing patterns? I think that question can be answered by neural networks. They weight tensors are generally initialized with random values and the stream of output they see most likely appears meaningless to them. However, an input stream attached with some form of desired output is then able to produce the necessary ingredients for the network to correct its weights such that when it sees a given pattern, its output will try to be as close as possible to the desired output.

However if we look at that question from another angle, namely how can an entity determine how to split-up a random input stream into input "packets" so it can do pattern recognition, that is a more difficult question. We know that neurons form and lose connections throughout our lifetime. This means that a single neuron (entity) has to adapt to the addition and subtraction of inputs (new axon terminals connected to their dendrites).

The brain is nothing more than processing. Memory is simply a side effect of its processing capabilities (part of its programming if you will). Can we consider programming/code to be memory in some way? Similarly, DNA would be our program?

* What is the parallel between atoms, neurons and society? In each case, you have groups of individuals that form something greater than themselves.

Let's consider a neuron as the same thing as a transistor, that is to say a boolean switch.
By itself the neuron can accept a certain amount of connections but it will only help put a 0/1 value. So it effectively computes a function that returns a yes or no answer.
This effectively means that anything that can be for lated as a yes or no question can be answered through a neuron.
All that you actually need is the appropriate features or if you prefer inputs.
We considered the neuron to be answering in a yes no fashion because it actually is dependent on some threshold which will determine whether or not the input signal is strong enough for an output signal to occur.
So as long as your chain of neurons is deep then it should mean that you can create more and more abstract concepts as they build upon simpler concepts.
The fact that new connections can appear from unrelated neurons means that it is possible for the neuron to fire for incorrect reasons. This should generally mean that disconnection will get pruned sooner or later as it is an inappropriate trigger.
Neurons also communicate through some form temporal signaling. Neurons may spike at a given interval based on the input it receives up until a certain point of saturation. At this point the neuron cannot fire any faster.

# See also
* [Definitions](definitions/article.md)
* [Tests](tests/article.md)

# References
* http://journal.frontiersin.org/article/10.3389/fnana.2011.00029/full

# Comparing relative intelligence
* http://www.lifehack.org/articles/communication/10-signs-someone-smarter-than-you.html
* http://www.lifespan.com/7-signs-someone-smarter/
* https://www.quora.com/How-can-you-tell-whether-someone-is-smarter-than-you
