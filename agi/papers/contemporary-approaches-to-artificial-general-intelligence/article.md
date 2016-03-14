---
title: Contemporary Approaches to Artificial General Intelligence
created: 2016-02-17
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview

## 1.1 Some Historical AGI-Related Projects
* AI may be divided in broad categories:
	* symbolic
	* symbolic and probability- or uncertainty-focused
	* neural net-based
	* evolutionary
	* artificial life
	* program search based
	* embedded
	* integrative
* Most of the ambitious AGI-oriented projects undertaken so far have been in the symbolic-AI paradigm
* Most famous and largest symbolic AI effort in existence today: CYC (started in the mid-80's)
	* Consist of encoding all common sense knowledge in first-order predicate logic

### Projects
* General Problem Solver (GPS)
* CYC
* SOAR
* ACT-R
* NARS
* Japanese 5th Generation Computer System
* Novamente system
* CAM-Brain
* Creatures game
* Network Tierra

## 2.1 The Psychology of Intelligence
* The [g-factor](https://en.wikipedia.org/wiki/G_factor_(psychometrics) (general intelligence)
* The system should be capable of learning, especially autonomously and incrementally
* The system should be able to interact with its environment and other entities within the environment and learn from these interactions
* The system should be able to build upon its previous experience, and the skills they have taught it, to learn more complex actions and therefore achieve more complex goals

## 2.2 The Turing Test
* Simulate a human in a text-based conversation interchange
* Intelligence is defined by behavior rather than by mystical qualities

## 2.3 A Control Theory Approach to Defining Intelligence
* An automaton is said to behave "intelligently" if, on the basis of its "training" data which is provided within some context together with information regarding the desired action, it takes the correct action on other data within the same context not seen during training
* Intelligence is the ability to behave appropriately under unpredictable conditions
* Intelligence is the ability to achieve goals in complex environments

## 2.4 Efficient Intelligence
* Intelligence is the ability to work and adapt to the environment with insufficient knowledge and resources
* **AIKR:** Assumption of Insufficient Knowledge and Resources
* A system must be, at the same time
	* A finite system: Computing power and working/storage space is limited
	* A real-time system: Tasks can arrive at anytime and are attached to deadlines
	* An amplitive system: Can retrieve available knowledge and derive sound conclusions from it, but also make refutable hypotheses and guesses based on it when no certain conclusion can be drawn
	* An open system: No restriction is imposed on the relationship between old and new knowledge
	* A self-organized system: Can accomodate itself to new knowledge and adjust its memory structure and mechanism to improve its time and space efficiency, under the assumption that future situations will be similar to past situations
* Efficient intelligence is the ability to achieve intelligence using severely limited resources

## 3 The Abstract Theory of General Intelligence
* Formalize the problem mathematically and then seek a solution using the tools of abstract mathematics
* Start by formalizing the notion of intelligence
* Formalize the notion of computation
* Ask the question: How may one create intelligent computer programs?
* Intelligence is the maximization of a certain quantity, by a system interacting with a dynamic environment
* A simple AI system behaving somewhat similar to AIXItl could be built by creating a program with three parts:
	* the data store
	* the main program
	* the meta-program
* The operations of the meta-program would be as follows:
	* At time t, place within the data store a record containing the complete internal state of the system and the complete sensory input of the system
	* Search the space of all programs P of size |P| < l to find the one that, based on the data in the data store, has the highest expected value for the given maximization criterion
	* Install P as the main program
* This establishes the following contention:
	* If you accept any definition of intelligence of the general form "maximization of a certain function of system behavior",
	* Then the problem of creating AGI is basically a problem of dealing with the issue of space and time efficiency
* The basic idea of OOPS is to run all possible programs, but interleaved rather than one after the other
* As opposed to AIXItl, this strategy allows in the average case, brief and effective programs to rise to the top of the heap relatively quickly

# 4 Toward a Pragmatic Logic
* One of the themes in the history of AGI is formal logic
* Because it has no ways to deal with uncertainty or the fact that different propositions may be based on different amounts of evidence, it is strongly believed that classical formal logic is not going to play a central role in AGI
* One key issue dividing AI researchers is the degree to which logical reasoning is fundamental to their artificial minds
* Logic (not typical, crisp, mathematical logic):
	* has to do with forming and combining estimations of the truth values of various sorts of relationships based on various sorts of evidence
	* is based on incremental processing, in which pieces of evidence are combined step by step to form conclusions, so that at each stage it is easy to see which pieces of evidence were used to give which conclusion
* An important distinction is whether a system gains its knowledge experientially or via being given expert rule type propositions

## 5 Emulating the Human Brain
* Two key computational properties of neural structures (see [wikipedia](https://en.wikipedia.org/wiki/Stephen_Grossberg#New_computational_paradigms)):
	* Complementary computing: Allows different processing streams in the brain to compute complimentary properties.
	* Laminar computing: The organization of the cerebral cortex in layers, with interactions going bottom-up, top-down, and sideways. Contributes to learning, development and attention control.

## 6 Emulating the Human Mind
* There is more focus on emulating the mind than there is to emulate the brain
* Yudkowsky's deliberative general intelligence (DGI), cposed of 5 levels of functional organization
	* Code: The underlying source code of the AI system.
	* Sensory modalities: The five senses (smell, sight, sound, touch, taste). Information processing and feature extraction.
	* Concepts: Categories or symbols abstracted from a system's experience. Recognition and reification of similarity within a group of experiences.
	* Thoughts: Built from structures of concepts. Mental images are built from sensory modalities. Thoughts are viewed as disposable one-time structures built from reusable concepts.
	* Deliberation: Sequence of thoughts. This is the internal narrative of the conscious mind. Includes explanation, prediction, planning, design, discovery and other activities used to solve knowledge problems in the pursuit of real-world goals.

## 7 Creating Intelligence by Creating Life
* Simulate the evolutionary processes that gave rise to the human brain
* Tierra: Gave rise to unicellular organisms. Had no externally defined fitness function, it emerged as a consequence of each creature's ability to replicate itself and adapt to the presence of other creatures.

# See also

# Sources
