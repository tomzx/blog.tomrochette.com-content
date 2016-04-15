---
title: EURISKO: A Program That Learns New Heuristics and Domain Concepts (1982)
created: 2016-04-15
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview

* Automated Mathematician (AM) was an automatic programming system, whose primitive actions were modifications to pieces of LISP code, code which represented the characteristic functions of various math concepts

## 1 Design Decisions in Constructing the EURISKO Program
* The EURISKO project was first conceived in 1976
* Over 6 years, there has been an accumulation of "design ideas" which have been tested

## 1.1 Ideas about representing concepts
* **Rules need not distinguish "slots" from "functions"**
* EURISKO basic representation employs frames (units) with slots
* Each slot can be viewed as a unary function which is handed a unit-name and returns a value
* Other unary functions exist and can be defined in terms of these more primitive slots
* The decision about which functions are implemented as primitive (slots), and which are computed dynamically from others, is invisible to the rules, and may change from time to time (e.g., after a great amount of experience is accumulated in some domain, it may be apparent that a certain function is requested so often that it should be stored primitively)
* All a "concept" is is a legal argument for a list of functions (mostly unary ones)
* **"GET" knows why it's being called, "PUT" knows how the value is justified**
* GET Cf: get the value stored in slot f of concept C
* f(C): GET Cf
* Different reasons to query for f(C): is there any value, what is the length of the set of values, what are some of the values
* Due to the limitation on the amount of available resources to expend (time or space or number of queries to the human user), an extra argument was added to each call on GET
* This argument would specify the reason behind the call (Existence, Length, Some, Up-to-date) and how much resources can be spent (Time, Cells, Queries)
* Calls on PUT are more standard; they may trigger some flurry of re-writing, but the only extra argument one wishes to supply is an indication of the justification of the value being changed
* **"The size of ships" can mean different things, and there should be a place for each**
* Each meaning should be unambiguously representable
* **Each kind of slot has a unit describing it**
* Each kind of slot should "know" what it means to have a value stored on itself
* Should we redundantly cache (store) this value, or just assume we'll recompute it whenever we need it?
* The optimal answer will depend on how the knowledge base grows, changes and is used
* When an entry is added or removed from an IsA slot, we expect the "inverse link" to be likewise added or removed

## 1.2 Ideas about control (agendae, reasons, and heuristic rules)
* **The control structure of the system is represented as part of the knowledge base** 
* While an AM-like agenda mechanism has been retained, the precise control algorithm is represented within EURISKO as a set of concepts, so the system can modify it itself
* Basically, there is a Select-Execute-PostMortem loop represented as a unit
* Specializations of this unit form the three nested loops that characterize the EURISKO program:
	* select and work on a topic
		* given a topic, select and work on a promising task
			* given a task, select and obey a relevant individual heuristic rule
* Representing the control structure explicitly had three benefits so far
	* It facilitates explanation; EURISKO can more coherently explain what it is doing at any given moment, when asked by the user
	* It allows enforced semantics
	* It is possible for EURISKO to notice when it's in danger of being in an infinite loop, even a subtle one in which there is no obvious infinite recursion or circular list structure involved
* The original motivation for explicitly representing control was to enable the program to meaningfully modify its own control code, but this has always resulted in bugs (due to an inadequate mastery of programming, of models of learning, and so on)
* **Multiple agendae**
* The human research sticks with a topc for an extended period of time
* Party this is due to the difficulty of "swapping in" a whole new set of concepts, heuristics, etc.
* How does EURISKO stay focused on a single topic for a nontrivial period of time?
* Some (initially eight) of EURISKO's concepts (e.g., Games, DevicePhysics, NumberTheory) represent "topics"
* Each topic has a slot called Agenda, which contains its own agenda of tasks dealing with that topic (concept) and/or with one or more of its specializations
* There is no longer one central agenda; rather, there is a "current topic", and its agenda is the one being used for a while
* **Dynamic creation and elimination of agendae (topics)**
* If agenda A contains more than four times as many tasks as the average agenda, then (try to) split A into about three pieces
* If the number of units called on per task, when working on tasks of agenda A, is more than ten times the rate at which other agendae inspect units, then (try to) split A into two pieces
* When an agenda shrinks too small, rules cause it to be merged into all appropriate immediate generalizations' agendae


# See also

# Sources
