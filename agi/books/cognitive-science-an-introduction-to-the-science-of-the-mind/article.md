---
title: Cognitive Science: An Introduction to the Science of the Mind
created: 2016-04-14
taxonomy:
  category: [Artificial General Intelligence, Cognitive Science]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview

# Notes
* (p21) The human perceptual systems are information channels with built-in limits of about 7 items, or around 3 bits
* (p21) Chunking can be used to work around this limitation
* (p21) Natural language is the ultimate chunking tool
* (p22) The phenomenon of selective attention occurs in every sense modality
* (p22) Broadbent intepreted the dichotic listening experiments as showing that we can only attend to a single information channel at a time (assuming that each ear is a separate channel) - and that the selection between information channels is based purely on physical characteristics of the signal
* (p24) Information is everywhere, but in order to use it organisms need to represent it
* (p25) (the idea that) Information processing is done by dedicated and specialized systems
* (p29) Cognition can be understood as information processing and information processing can be understood as an algorithmic process
* (p29) One can try to understand how particular cognitive systems work by breaking down the cognitive tasks that they perform into more specific and determinate tasks
* (p34) SHRDLU consists of twelve different systems. Winograd himself divides these into three groups. Each group carries out a specific job
	* Syntactic analysis
	* Semantic analysis
	* Integrating the information acquired with the information the system already possesses
* (p34) We can identify distinct components for each of these jobs - the syntactic system, the semantic system, and the cognitive-deductive system
* (p34) What makes this possible for these systems to call upon each other is that their different forms of knowledge are all represented in a similar way: they are all represented in terms of procedures
* (p47) Marr distinguishes three different levels for analyzing cognitive systems
	* The top level is the computational level (computational theory)
		* to translate a general description of the cognitive system into a specific account of the particular information-processing problem that the system is configured to solve
		* to identify the constraints that hold upon any solution to that information-processing task
	* The middle level down is the algorithmic level (representation and algorithm)
		* tells us how the cognitive system actually solves the specific information-processing task identified at the computational level
		* tells us how the input information is transformed into the output information
	* The bottom level is the implementational level (hardware implementation)
		* find a physical realization for the algorithm - that is to say, to identify physical structures that will realize the representational states over which the algorithm is defined and to find mechanisms at the neural level that can properly be described as computing the algorithm in question
* (p49) Marr drew two conclusions about how the visual system functions from Warrington's neuropsychological observations
	* Information about the shape of an object must be processed separately from information about what the object is for and what it is called
	* The visual system can deliver a specification of the shape of an object even when that object is not in any sense recognized
* (p50) Marr's theory of vision uses 3 different types of representations
	* primal sketch: distribution of light intensity across the retinal image, basic geometry of the field of view
	* 2.5D sketch: depth and orientation of visible surfaces from the viewer's perspective
	* 3D sketch: viewer-independent representation
* (p53) What are the starting-points for the information processing that will yield as its output an accurate representation of the layout of surfaces in the distal environment?
	* The visual system needs to start with discontinuities in light intensity, because these are  a good guide to boundaries between objects and other physically relevant properties
	* Representational primitives: zero-crossings (registers of sudden changes in light intensity), blobs, edges, segments, and boundaries
* (p62) Anatomists distinguish three different parts of the mammalian brain
	* the forebrain
	* the midbrain
	* the hindbrain
* (p129) The more informationally encapsulated an information system is, the less significant the frame problem will be
* (p130) In what format does a particular cognitive system carry information?
* (p130) How does that cognitive system transform information?
* (p132) How is the mind organized so that it can function as an information processor?
* (p142) Newell and Simon's characterization of physical symbol systems
	* Symbols are physical patterns
	* These symbols can be combined to form complex symbol structures
	* The physical symbol system contains processes for manipulating complex symbol structures
	* The processes for generating and transforming complex symbol structures can themselves be represented by symbols and symbol structures within the system
* (p148) Means-end analysis
	1. Evaluate the difference between the current state and the goal state
	2. Identify a transformation that reduces the difference between current state and goal state
	3. Check that the transformation in (2) can be applied to the current state
		* If it can, then apply it and go back to step (1)
		* If it can't then return to step (2)
* (p149) The trick in writing the GPS program, is building into it search strategies and sub-routines that will ensure that it reaches the goal state as efficiently as possible
* (p155) Fodor's computer model of the mind
	1. Causation through content is ultimately a matter of causal interactions between physical states
	2. These physical states have the structure of sentences and their sentence-like structure determines how they are made up and how they interact with each other
	3. Causal transitions between sentences in the language of thought respect the rational relations between the contents of those sentences in the language of thought
* (p164) (In reply to Searle Chinese room argument) Using an English dictionary to look up words up is not entirely straightforward, and what Searle is envisaging is more complex by many orders of difficulty. The person inside the room needs to be able to discriminate between different Chinese symbols - which is no easy matter, as anyone who has tried to learn Chinese well knows. They will also need to be able to find their way around the instruction manual (which at the very least requires knowing how the symbols are ordered) and then use it to output the correct symbols. The person inside the room is certainly displaying and exercising a number of sophisticated skills
* (p199) SHAKEY's five level of functionality
	1. Robot vehicle and connections to user programs: To navigate and interact physically with a realistic environment
	2. Low-level actions (LLAs): To give the basic physical capabilities of the robot
	3. Intermediate-level actions (ILAs): Packages of LLAs
	4. STRIPS: A planning mechanism constructing MACROPS (sequences of ILAs) to carry out specific tasks
	5. PLANEX: Executive program that calls up and monitors individual MACROPS
* SHAKEY's software packages are built around this basic idea that complex behaviors are hierarchically organized

# See also

# Sources
* Bermúdez, José Luis. Cognitive Science: An Introduction to the Science of the Mind. Cambridge: Cambridge University Press, 2010.
