---
title: Artificial General Intelligence
created: 2016-02-17
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

* Gödel machines
* The Psynet model

# Overview

# Notes

# Contemporary Approaches to Artificial General Intelligence

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

# The Logic of Intelligence
* NARS is based on the opinion that the essence of intelligence is the ability to adapt with insufficient knowledge and resources.

## 1.1 To Define Intelligence
* Anyone who wants to work on artificial intelligence is facing a two-phase task: to choose a working definition of intelligence, then to produce it in a computer.
* We need to set up a general standard for what makes a definition better than others
* The task "consists in transforming a given more or less inexact concept into an exact one or, rather, in replacing the first by the second"
* The second concept must fulfill the following requirements:
	* Be similar to the concept to be defined
	* Be defined in an exact form
	* Be fruitful in the study
	* Be simple as the other requirements permit

## 1.2 A Working Definition of Intelligence
* Intelligence is the capacity of a system to adapt to its environment while operating with insufficient knowledge and resources.
* The interactions of the system with the environment can be described by the experiences (stimuli) and responses of the system, which are streams of input and output information
* Perceivable patterns of input and producible patterns of output constitute the system's interface language
* To adapt means that the system learns from experience. It adjusts its internal structure to approach its goal, as if future situations will be similar to past situations
* Insufficient knowledge and resources means that the system works under the following conditions:
	* Finite: The system has a constant information-processing capacity
	* Real-time: All tasks have time requirements attached
	* Open: No constraints are put on the knowledge and tasks that the system can accept, as long as they are representable in the interface language
* Various situations a system with insufficient knowledge and resources should be able to handle:
	* extra tasks when all processors are occupied
	* extra memory when all available memory is exhausted
	* tasks with time requirements, such that exhaustive search is not an option
	* new knowledge conflicting with previous knowledge
	* questions for which no sure answer can be deduced from available knowledge
* Intelligence is a highly developed form of mental adaptation
* An unintelligent system is one that does not adapt to its environment

## 1.3 Comparison With Other Definitions
* AI is more concerned with the concept of the model of a mind, a high level description of brain activity in which biological concepts do not appear
* The Turing test requires prior human experience and is more about testing an artificial human than a computer system with artificial intelligence
* In everyday language, intelligent usually applies to people who can solve hard problems. According to this type of definition, intelligence is the capacity to solve hard problem. How the problem are solved is not very important. Hard for whom?
* Hard problems are those for which a solver (human or computer) has insufficient knowledge and resources
* Few would dispute the proposition that adaptation, or learning, is essential for intelligence

## 1.4 Logic and Reasoning Systems
* A reasoning system usually has the following components:
	* a formal language for knowledge representation, as well as communication between the system and its environment
	* a semantics that determines the meaning of the words and the truth values of the sentences in the language;
	* a set of inference rules that match questions with knowledge, infer conclusions from premises, and so on
	* a memory that systematically stores both questions and knowledge, and provides a working place for inferences
	* a control mechanism that is responsible for choosing premises and inference rules for each step of inference
* Complete self-modifying is an illusion. As flexible as the human is, it cannot modify its own "law of thought"
* Many arguments proposed against logical AI, symbolic AI or AI as a whole are against pure-axiomatic systems

## 2.1 Experience-Grounded Semantics
* Truth value becomes a function of the amount of available evidence, therefore inevitably becomes changeable and subjective, though not arbitrary.
* The truth value of a statement indicates the degree to which the statement is confirmed by past experience

## 2.2 Inheritance Statement
* Binary truth is not enough
* The system needs to know the amount of positive and negative evidence (a measure of uncertainty)
* $raven \rightarrow bird$ is an inheritance statement with raven as subject term and bird as predicate term
* The subject is a specialization of the predicate and the predicate is a generalization of the subject
* $S \rightarrow P$, (subject -> predicate)
* $w^+, w^-, w$ is the amount of positive, negative and total evidence
* $w^+ = |S^E \cap P^E| + |P^I \cap S^I|$
* $w^- = |S^E - P^E| + |P^I - S^I|$
* $w = w^+ + w^- = |S^E| + |P^I|$

## 2.4 Syllogistic Inference Rules
* 4 basic inference rules
	* Deduction
	* Induction
	* Abduction
	* Revision

## 2.5 Controlled Concurrency in Dynamic Memory
* Uses "bags" as data structure for resource allocation
	* A bag can contain certain type of items with a constant capacity, and maintains a priority distribution among the items
* There are 3 major operations defined on bags:
	* Put an item into the bag, if the bag is full, remove an item with the lowest priority
	* Take an item out of the bag by key (unique identifier)
	* Take an item out of the bag by priority
* Knowledge and tasks are organized into concepts
* A term T has a corresponding concept $C_T$, which contains all the knowledge and tasks in which T is the subject term or predicate term
* The memory of NARS can be roughly seen as a bag of concepts
* NARS runs by repeatly carrying out the following working cycle:
	* Take a concept from the memory by priority
	* Take a task from the task bag of the concept by priority
	* Take a piece of knowledge from the knowledge bag of the concept by priority
	* According to the combination of the task and the knowledge, call the applicable inference rules on them to derive new tasks and new knowledge
	* Adjust the priority of the involved task, knowledge and concept according to how they behave in this inference step, then put them back into the corresponding bags
	* Put he new (input or derived) tasks and knowledge into the corresponding bags. If certain new knowledge provides the best solution so far for a user-assigned task, report a solution
* The priority value of each item reflects the amount of resources the system plans to spend on it in the near future
	* Long-term factor: Higher priority to more important items, evaluated according to past experience.
	* Short-term factor: Higher priority to more relevant items, evaluated according to the current context. (this works in the same way as having related ideas being activated when thinking of something, such as red, juicy, tasty when thinking of an apple)

## 3.1 Reasonable Solutions
* NARS cannot guarantee that the solutions it generates for tasks are correct, nor optimum
* The solution should however be reasonable in the sense that they are the best summaries of the past experience, given the current resource supply

## 3.2 Unified Uncertainty Processing
* Uncertainty comes from the insufficiency of knowledge and resources
* As a result, the evaluation of uncertainty is changeable and context-dependent
* No concept has a clear-cut boundary. Whether a concept is an instance of another is a matter of degree. Therefore, all concepts in NARS are "fuzzy"
* The membership evaluations are revisable. The priority distribution among the relations from a concept to other concepts also changes from time to time. Therefore, what a concept actually means to the system is variable
* However, the meaning of a concept is not arbitrary or random, but relatively stable, bounded by the system's experience

## 3.3 NARS as a Parallel and Distributed Network
* In NARS, information is not only stored distributively and with duplications, but also processed through multiple pathways
* The generating of a specific solution is the emergent result of lots of local events, not only caused by the events in its derivation path, but also by the activity of other tasks that adjust the memory structure and compete for the resources

## 3.4 Resources Competition
* NARS uses a flexible method to decide how much time to spend on a task, influenced by both the system and the user
* The user can attach an initial priority value to a task, but the allocation also depends on the current situtation of the system, as well as on how well the task processing goes

# See also

# Sources

* Goertzel, Ben, and Cassio Pennachin. Artificial General Intelligence. Berlin: Springer, 2007.
