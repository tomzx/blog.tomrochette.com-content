---
title: Pei Wang - The Logic of Intelligence (2007)
created: 2016-02-19
taxonomy:
  category: [Artificial General Intelligence]
  status: finished
---

## Context

## Learned in this study

## Things to explore

# Overview

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
* The user can attach an initial priority value to a task, but the allocation also depends on the current situation of the system, as well as on how well the task processing goes

## 3.6 Autonomy and Creativity
* The system's behavior depends to a certain extent on its own tasks, which are actually more or less dependent of the original processes, even though historically derived from them
* In extreme form, the derived tasks may become so strong that they even prevent the input tasks from being fulfilled
* This can lead to creative and original behaviors, because the system is pursuing goals that are not directly assigned by its environment or its innateness

# See also

# Sources
* DOI: [10.1007/978-3-540-68677-4_2](https://dx.doi.org/10.1007/978-3-540-68677-4_2)