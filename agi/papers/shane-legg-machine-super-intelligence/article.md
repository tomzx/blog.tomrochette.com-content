---
title: Shane Legg - Machine Super Intelligence (2008)
created: 2018-01-04
taxonomy:
  category: [Artificial General Intelligence]
  status: finished
---

## Context

## Learned in this study
* The definition of universal intelligence given in this thesis emphasizes that being able to solve simple problems is more important than solving complex ones
	* As such, agents able to accomplish complex tasks but not simple ones that other agents can will be classified as having lower intelligence

## Things to explore
* Is it possible to formalize machine intelligence based on the idea of a computer/program/data?
* Is a young child as intelligent as an adult?
* Is it possible to determine if an individual may or may not be able to learn something given enough time? And if so, is it possible to estimate the amount of time required?
* Is it possible to devise a test of intelligence for which it is not necessary to communicate any instruction to the entity being tested?
* Is it easier to design anthropocentric AI/AGI vs universal AI/AGI?
* Tegmark definition of intelligence does not contain the part about "in a wide range of environments"... How could this be turned into something more abstract such as "in a wide range of potential state systems"?

# Overview

# Notes
## 1. Nature and Measurement of Intelligence
* When standard intelligence tests are correctly applied and interpreted, they all measure approximately the same thing
* Furthermore, what they measure is both stable over time in individuals and has significant predictive power, in particular for future academic performance and other mentally demanding pursuits

### 1.1. Theories of intelligence
* A central question in the study of intelligence concerns whether intelligence should be viewed as one ability, or many

### 1.2. Definitions of human intelligence
* The most elementary common feature of these definitions is that intelligence is seen as a property of an individual who is interacting with an external environment, problem or situation
* Another common feature is that an individual's intelligence is related to their ability to succeed or profit. This implies the existence of some kind of objective or goal
* Intelligence measures an agent's ability to achieve goals in a wide range of environments
* Must an agent be able to tackle some task immediately, or perhaps after a short period of time during which learning can take place, or perhaps it only matters that they can eventually learn to deal with the problem?
* Intelligence seems to be the ability to adapt and learn as quickly as possible given the constraints imposed by the problem at hand

### 1.3. Definitions of machine intelligence
* A key goal of artificial intelligence is to find algorithms which have the greatest efficiency of intelligence, that is, which achieve the most intelligence per unit of computational resources consumed

### 1.4. Intelligence testing
* There are many properties that a good test of intelligence should have
	* The test should be repeatable, in the sense that it consistently returns about the same score for a given individual
	* Should be valid in the sense that it appears to be testing what it claims it is testing for
	* A test should have predictive power, for example the ability to predict future academic performance, or performance in other cognitively demanding tasks

### 1.6 Animal intelligence tests
* It is not always clear how to validate an intelligence test for animals: if survival or the total number of offspring was a measure of success, then bacteria would be the most intelligent life on earth!
* One interesting difficulty when testing animal intelligence is that we are unable to directly explain to the animal what its goal is


## 2. Universal Artificial Intelligence
### 2.1. Inductive inference
* Inductive inference is the process by which one observes the world and then infers the causes behind what has been observed
* There typically exist many hypothesis which are consistent with all of the available data (Epicurus)
	* Keep all hypotheses that are consistent with the data

### 2.8. Agent-environment model
* The agent-environment model
	* The model consists of two entities called the agent and the environment
		* The agent receives input information from the environment, which we will refer to as perceptions, and sends output information back to the environment, which we call actions
		* The action receives actions from the agent as input and generates perceptions as output
	* Each perception consists of an observation component and a reward component
		* Observations are just regular information, however rewards have a special significance because the goal of the agent is to try to gain as much reward as possible from the environment
* The agent sends information to the environment by sending symbols from some finite alphabet of symbols. We call this set the action space and denote it by $\mathcal{A}$
* The environment sends signals to the agent with symbols from an alphabet called the perception space, which we denote $\mathcal{X}$
* The reward space, denoted by $\mathcal{R}$, is always a subset of the rational unit interval $[0, 1] \cap \mathbb{Q}$
* Every perception consists of two separate parts: an observation and a reward
* The agent is a function, denoted by $\pi$, which takes the current history as input and chooses the next action as output

### 2.9. Optimal informed agents
* Which of these two agents is the better one? The answer depends on how we value reward at different points in the future
	* In some situations we may want our agent to perform well quickly, and thus place more value on short term rewards. In others, we might only care that it eventually reaches a level of performance that is as high as possible, thus place relatively high value on rewards far into the future
* We need to formally express our temporal preferences
	* A general approach is to weight, or discount, each reward in a way that depends on which cycle it occurs in
* The optimal agent for an environment $\mu$ and discounting $\gamma$ is the agent $\pi^\mu$ that has maximal expected future discounted reward
$$
\pi^\mu := \underset{\pi}{\arg\max} V_\gamma^{\pi\mu}
$$
* An agent $\pi$ is Pareto optimal if there is no other agent $\rho$ such that $\forall \mu \in \mathcal{E}$, $\forall ax_{< t}$
$$
V_\gamma^{\rho\mu}(ax_{< t}) \ge V_\gamma^{\pi\mu}(ax_{< t})
$$
* We say that $\pi$ is self-optimising for the set of environments $\mathcal{E}$ if it is self-optimising for every environment in $\mathcal{E}$
* We say that a set of environments $\mathcal{E}$ admits self-optimising agents if there exists an agent $\pi$ that is self-optimising for $\mathcal{E}$

## 3. Taxonomy of Environments
### 3.1. Passive environments
* A Bernoulli scheme is an environment $(\mathcal{A}, \mathcal{X}, \mu)$ such that $\forall ax_{1:k}$
$$
\mu(ax_{< t}a\underline{x}_k) = \mu(\underline{x}_k)
$$
* A Markov chain is an environment $(\mathcal{A}, \mathcal{X}, \mu)$ that is a Bernoulli scheme $\forall ax_1$, and $\forall ax_{1:k}$ with $k > 1$
$$
\mu(ax_{< k}a\underline{x}_k) = \mu(o_{k-1}\underline{x}_k)
$$
* A Totally Passive Environment is an environment $(\mathcal{A}, \mathcal{X}, \mu)$ such that $\forall ax_{1:k}$
$$
\mu(ax_{< k}a\underline{x}_k) = \mu(o_{< k}\underline{x}_k)
$$
* A Passive Environment is an environment $(\mathcal{A}, \mathcal{X}, \mu)$ such that $\forall ax_{< k}a\underline{o}_k$
$$
\mu(ax_{< k}a\underline{o}_k) = \mu(o_{< k}\underline{o}_k)
$$
* A Sequence Prediction Problem is a passive environment $(\mathcal{A}, \mathcal{X}, \mu)$ such that $\forall ax_{1:k}$
$$
\mu(ax_{< k}ao\underline{r}_k) = \mu(ao\underline{r}_k)
$$

### 3.2. Active environments
* The simplest active environment is one where the next perception $x_k$ depends on only the last action $a_k$
* A Bandit is an environment $(\mathcal{A}, \mathcal{X}, \mu)$ such that $\forall ax_{1:k}$
$$
\mu(ax_{< k}a\underline{x}_k) = \mu(a\underline{x}_k)
$$
* A (stationary) Markov Decision Process (MDP) is an environment $(\mathcal{A}, \mathcal{X}, \mu)$ that is a Bernoulli scheme $\forall ax_1$, and $\forall ax_{1:k}$ with $k > 1$
$$
\mu(ax_{< k}a\underline{x}_k) = \mu(o_{k-1}a\underline{x}_k)
$$
* A (stationary) $n^{th}$ order Markov Decision Process (MDP) is an environment $(\mathcal{A}, \mathcal{X}, \mu)$ that is a Bernoulli scheme $\forall ax_1$, and $\forall ax_{1:k}$ with $k > 1$, where $m := \min\{n, k\}$
$$
\mu(ax_{< k}a\underline{x}_k) = \mu(o_{k-m}ao_{k-m+1:k-1}a\underline{x}_k)
$$
* A Partially Observable Markov Decision Process (POMDP) is an environment $(\mathcal{A}, \mathcal{X} = \mathcal{O} \times \mathcal{R}, \mu)$ defined as follow
	* Let $(\mathcal{A}, \tilde{\mathcal{X}} = \tilde{\mathcal{O}} \times \mathcal{R}, \tilde{\mu})$ be an MDP called the core MDP
	* Let $\phi: \tilde{\mathcal{X}} \times \mathcal{X} \rightarrow [0, 1]$ be a conditional probability measure of the form $\phi(\tilde{x}\underline{x})$ which expresses the probability of perceiving $x$ when the core MDP outputs $\tilde{x}$
	* Define $\forall ax_{1:k} \in (\mathcal{A} \times \mathcal{X})^k$
$$
\mu(a\underline{x}_{1:k}) := \sum_{\tilde{x}_{1:k} \in \tilde{\mathcal{X}}^k} \tilde{\mu}(a\tilde{\underline{x}}_1)\phi(\tilde{x}_1\underline{x}_1)\tilde{\mu}(\tilde{o}_1a\tilde{\underline{x}}_2)\phi(\tilde{x}_2\underline{x}_2) \cdots \tilde{\mu}(\tilde{o}_{k-1}a\tilde{\underline{x}}_k)\phi(\tilde{x}_k\underline{x}_k)
$$

### 3.3. Some common problem classes
* A Function Maximisation Problem is an environment $(\mathcal{A}, \mathcal{X}, \mu)$ such that $\mathcal{O} =  \mathcal{R}$ and for some objective function $f: \mathcal{A} \rightarrow \mathcal{R}$ we have $\forall ax_{1:k}$
$$
\mu(ax_{< k}a\underline{x}_k) := \left\{
	\begin{array}{ll}
		1 & \text{if }o_k = f(a_k) \wedge r_k = \max\{o_1, \dots, o_k\},\\
		0 & \text{otherwise}.
	\end{array}
\right.
$$
* A Repeated Strategic Game is an environment $(\mathcal{A}, \mathcal{X}, \mu)$ where $\exists l \in \mathbb{N}$, where $m := \lfloor k/l \rfloor$ is the number of the episode when in cycle $k$, and $l$ is the episode length
$$
\mu(ax_{< k}a\underline{x}_k) = \mu(ao_{lm:k-1}a\underline{x}_k)
$$
* A Classification Problem <tbc></tbc>

### 3.4. Ergodic MDPs
* We say that two observations communicate if it is possible to go from one observation to the other and return after some finite number of steps
* A communicating class is a set of observations that all communicate with each other, and do not communicate with any observations outside this set
* If all observations of the Markov chain belong to the same communicating class, we say that the Markov chain is irreducible
* An observation has period k if any return to the observation must occur in some multiple of k time steps and k is the largest number with this property
	* If an observation has period 1 then it is aperiodic
	* If all observations are aperiodic we say that the Markov chain is aperiodic
* A Markov chain environment $(\mathcal{A}, \mathcal{X}, \mu)$ is ergodic if and only if it is irreducible and aperiodic

### 3.5. Environments that admit self-optimising agents
* Environment are accessible when there are no observations that have zero probability of ever being observed

## 4. Universal Intelligence Measure
### 4.1. A formal definition of machine intelligence
* Intelligence measures an agent's ability to achieve goals in a wide range of environments
	* This definition contains three essential components:
		* An agent
		* Environments
		* Goals
* The agent and the environment must be able to interact with each other, specifically, the agent needs to be able to send signals to the environment and also receive signals being sent from the environment
* The environment must be able to send and receive signals
* Intelligence, at least the concrete kind that interests us, comes into effect when the agent has an objective or goal that it actively pursues by interacting with its environment
* The existence of a goal raises the problem of how the agent knows what the goal is
	* We need to allow agents that are more flexible, specifically, we need to be able to inform the agent of what the goal is
* We define an additional communication channel with the simplest possible semantics: a signal that indicates how good the agent's current situation is. We will call this signal the reward. The agent simply has to maximise the amount of reward it receives, which is a function of the goal
* Unfortunately, maximising reward is not sufficient to define how the agent should behave over time. We have to define some kind of a temporal preference that describes how much the agent should value near term rewards vs rewards further into the future
* What is important is not that an intelligent succeeds in any given situation, but rather that it takes actions that we would expect to be the most likely ones to lead to success
* Often intelligence is thought of as the ability to deal with complexity
* If we want to reward agents on average for correctly using Occam's razor, we must weight the environments according to their complexity, not their difficulty

### 4.2. Universal intelligence of various agents
* A random agent. The agent with the lowest intelligence, at least among those that are not actively trying to perform badly, would be one that makes uniformly random actions
	* In general such an agent will not be very successful as it will fail to exploit any regularities in the environment, even trivial ones
* A very specialised agent. An agent could have very low universal intelligence but still perform extremely well at a few very specific and complex tasks
* The universal intelligence measure strongly emphasises the ability to solve simple problems. If any system cannot do this, even if it can do something relatively complex like play chess, then it is considered to have very little intelligence
* A general but simple agent. Imagine an agent that performs very basic learning by building a table of observation and action pairs and keeping statistics on the rewards that follow. Each time an observation that it has seen before occurs, the agent takes the action with highest estimated expected reward in the next cycle with 0.9 probability, or a random action with 0.1 probability. It is clear that many environments, both complex and very simple, will have at least some structure that such an agent would take advantage of
* A simple agent with more history. A natural extension is to use a longer history of actions, observations and rewards in the agent's internal table
* A simple forward looking agent. In some environments simply trying to maximise the next reward is not sufficient, the agent must also take into account the rewards that are likely to follow further into the future, that is, the agent must plan ahead
* A very intelligent agent. Would perform well in simple environments, and reasonably well compared to most other agents in more complex environments
* A super intelligent agent. By definition, a "perfect" agent would always pick the action which had greatest expected future reward
* A human. For simple environments, a human should be able to identify their structure and exploit this to maximise reward. However, for more complex environments it is hard to know how well a human would perform

### 4.3. Properties of universal intelligence
* For an intelligence measure for machines we have to base the test on something more general and principled: universal Turing computation
* By weighting different environments depending on their Kolmogorov complexity, and by considering the space of all computable environments, we have avoided having to define intelligence with respect to any particular culture, species, etc.

### 4.4. Response to common criticisms
* We do not care whether the agent is efficient, due to some clever algorithm, or absurdly inefficient, for example by using an unfeasibly gigantic look-up table of precomputed answers
* The important point for us is that the machine has an amazing ability to solve a huge range of problems in a wide variety of environments
* When we say that an agent has low intelligence, what we mean is that there does not exist any reasonable test setup such that the agent exhibits intelligent behaviour

## 5. Limit of Computational Agents
* If you can accurately predict what is coming next you do not need to use much information to encode what the data actually is, and vice versa

## 7. Discussion
### 7.2. How could intelligent machines be developed?
#### Brain simulation
* The first point to note is that building a working simulation of something does not require understanding everything about how the system works
	* What is required is that the basic units which comprise the system can be faithfully reproduced and connected together
* Another important point is that much of the brain's complexity is not relevant. A significant part of the human brain is a jumble of different subsystems that take care of basic instinctive things like breathing, heart beat, blood pressure, reproduction, hunger, thirst, rhythms such as sleeping and body temperature, fight of flight response and so on
* The key, it seems, lies in understanding the neocortex, and its interaction with two smaller structures, namely, the thalamus and the hippocampus
* Essentially the whole neocortex has the same six layer structure
* What this suggests is that the same information processing mechanism is being applied across the neocortex, and that the variations in function across different regions are actually adaptations to the information passing through each region

# See also
* [General AI Challenge - Round 1](../../competitions/general-ai-challenge/round-1)

# References
* Legg, Shane. Machine super intelligence. Diss. Università della Svizzera italiana, 2008.