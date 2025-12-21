---
title: The OpenNARS implementation of the Non-Axiomatic Reasoning System
created: 2016-03-06
taxonomy:
  tag: [artificial-general-intelligence]
  status: finished
  readability: 3
---

## Context

## Learned in this study

## Things to explore

# Overview

# 1 Introduction
* NARS has a memory, a logic component and a control component
* The logic component consists of inference rules that work on statements, where the statements are goals, questions and beliefs
	* A statement can be eternal (non time-dependent) or events (time-dependent)
	* Beliefs are statements that the system believes to be true to a certain extent
	* An inference task is a statement to be processed, with additional control relevant information
* NAL: Non-Axiomatic Logic
* Narsese: Language for representing statements

# 2 Memory
* 3 primary operations:
	* Return the best ranked belief or goal for inference within concepts (local inference)
	* Provide a pair of contextually relevant and semantically related statements for inference between concepts (general inference)
	* Add statements to memory whilst maintaining constraints on the system
* The main loop:
	* Get a concept from memory
	* Get a task and belief related to the selected concept
	* Derive new tasks from the selected task and belief
	* Put the involved items back into the corresponding bags
	* Put the new tasks into the corresponding bags
* System of metadata (budget and stamp)
	* Used to prevent certain forms of invalid inference such as double counting evidence and cyclic reasoning
	* Abstracts temporal requirements away from the Narsese grammar
	* Provides certain implementation efficiencies
* A budget determines the allocation of system resources (time and space) and is defined as $(p, d, q) \in [0, 1] x (0, 1) x [0, 1]$
	* $p$: priority
	* $d$: durability
	* $q$: quality
* A stamp is defined as $(id, t_{cr}, t_{oc}, C, E) \in \mathbb{N} \times \mathbb{N} \times \mathbb{N} \times \mathcal{P}(\mathbb{N})$
	* $id$: unique id
	* $t_{cr}$: creation time
	* $t_{oc}$: occurrence time
	* $C$: syntactic complexity (the number of subterms in the associated term)
	* $E$: an evidential set
* Curve bag is a data structure that supports a probabilistic selection according to the item priority distribution
* The priority value p of the items in the bag maps to their access frequency by a predefined monotonically increasing function
* Called a curve bag because it allows the user to define a custom curve which is highly flexbile and allows emotional parameters and introspective operators to have influence on this selection
* The memory consists of a curve bag of concepts, where a concept is a container for: a concept term, tasklink curve bag, term link curve bag, belief tables and goal tables

# Logic Module
* Composed of two components: an inference rule domain specific language (Meta Rule DSL) and an inference rule execution unit
* The Meta Rule DSL != NAL grammar rules
* Meta Rule DSL: provides a flexible methodology to quickly experiment with alternate inference rules, to support the goal of creating a literate program, and to substantially improve the quality of the software implementation
* Meta inference rules take the following form:
$T, B, P_1, ..., P_n \vdash (C1, ..., C_n)$
	* $T$: the task to be processed
	* $B$: the belief retrieved for the task
	* $P1, ..., P_n$: logical predicates dependent on $T, B, C_1, ..., C_n$
	* $C_1, ..., C_n$: conclusions in the form $(D_i, M_i)$ where $D_i$ is the term of the derived task the conclusion $C_i$ defines, and $M_i$ provides additional meta-information, such as which truth function will be used to decide the truth or desire of the conclusion, how the temporal information will be processed, or whether backwards inference is allowed
* The inference rule execution unit roles are:
	* Parse the Meta Rule DSL into an efficient and executable representation
	* Select and execute the relevant inference rules

# 4 Temporal Inference Control
* In order to support temporal reasoning, the non-temporal NAL inference rules are extended by adding temporal variants:
	* Temporal window: Events occurring within a specified temporal window will be deemed to have occurred at the same time
	* Temporal chaining: Semantically unrelated events are linked together if they are temporally following one another
	* Interval handling: Events patterns which occur at a given interval from one another can be detected/observed
	* Projection
	* Eternalization
	* Anticipation

# 5 Projection and Eternalization
* When a truth value for a statement is projected in time, its value decreases according to the following function:
* $c_{new} = (1 - k_c) \times c_{old}$
	* $c_{new}$: new confidence value the belief
	* $c_{old}$: old confidence value the belief
	* $k_c$: confidence decay
* $k_c = \frac{|t_B - t_T|}{|t_B - t_C| + |t_T - t_C|}$
	* $k_c$: confidence decay
	* $t_B$: original occurrence time of the belief
	* $t_T$: projected occurrence time of the belief
	* $t_C$: current time
* In eternalization, the occurrence time is dropped, so the conclusion is about the general situation
* $c_{new} = \frac{1}{k + c_{old}}$
	* $c_{new}$: new confidence value the belief
	* $c_{old}$: old confidence value the belief
	* $k$: a global evidence horizon personality parameter

# 6 Anticipation
* Based on the observation of an antecedent and behavior, a consequent is excepted (anticipated)
* In the event that an antecedent and behavior is observed, and the consequent is also observed, nothing special needs to be done
* In the opposite case, then the system needs to recognize that the prediction may not be 100% appropriate. Such event will have a high budget and will significantly influence the attention of the system (in order to rectify the situation)

# 7 Evidence Tracking
* The truth value of a statement is a $(w_+, w_-)$ pair, where $w_+$ represents positive evidence and $w_-$ represents negative evidence
* Can alternatively be represented as a confidence and frequency tuple, where
	* $c = \frac{w_+ + w_-}{k + w_+ + w_-}$
	* $f = \frac{w_+}{w_+ + w_-}$
	* $k$: global personality parameter that indicates a global evidential horizon
* Evidence follows the following principles:
	* Evidence can only be used once for each statement
	* A record of evidence used in each derivation must be maintained, although given AIKR (assumption of insufficient knowledge and resources), this is only a partial record, which is not an issue in practice
	* There can be positive and negative evidence for the same statement
	* Evidence is not only the key factor to determine truth, but also the key to judge the independence of the premises in a step of inference

# 8 Processing of New and Derived Tasks
* Temporal chaining
* Ranking
* Adding to belief/desire table
* Selecting belief for inference
* Revision
* Decision

# 9 Attentional Control
* 3 phases process:
	* Select contextually relevant and semantically related tasks for inference
	* Create or update budget values based on user requirements and/or inference results
	* Update memory with results of the updated task and concepts
* Phase 1: Premises for inference are selected according to the following scheme
	* Select a concept from memory
	* Select a tasklink from this concept
	* Select a termlink from this concept
	* Select a belief from the concept the termlink points to ranked by the task
* Phase 2: Formation of new statements (tasks), with new metadata, from the derivations.
* Phase 3: Process the new tasks and insert them into memory.

# See also

# References
* [Paper: The OpenNARS implementation of the Non-Axiomatic Reasoning System (4th Draft for Comment)](https://groups.google.com/forum/#!topic/open-nars/k7oGlT0UnqI)
