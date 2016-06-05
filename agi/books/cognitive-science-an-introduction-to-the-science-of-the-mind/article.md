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
* (p236) The backpropagation algorithm is not very biologically plausible. There is no evidence that error is propagated backwards in the brain. And nature rarely provides feedback as detailed as the algorithm requires
* (p236) However, there are other learning algorithms. Competitive networks using Hebbian learning do not require explicit feedback, and there is evidence for local learning in the brain
* (p243) Fodor thinks of the process of acquiring a language as a lengthy process of mastering the appropriate rules, starting with the simplest rules governing the meaning of everyday words, moving on to the simpler syntatic rules governing the formation of sentences, and then finally arriving at the complex rules such as those allowing sentences to be embedded within further sentences and the complex transformational rules discussed by Chomsky and other theoretical linguists
* (p245) Fodor argues that learning a language has to involve learning truth rules
* (p245) Learning a public language such as English, even if it is your first language, requires you to formulate, test, and revise hypotheses about the truth rules governing individual words. These hypotheses have to be formulated in some language. A truth rule is, after all, just a sentence. But which language are truth rules formulated in?
* (p245) Fodor thinks that it cannot be the language being learnt. You cannot use the language that you are learning to learn that language
* (p245) It can only be the language of thought
* (p247) There are robust data indicating that children go through three principal stages in learning how to use the past tense in English
* (p247) In the first stage you language learners employ a small number of very common words in the past tense. Most of these verbs aer irregular and the standard assumption is that children learn these past tenses by rote
* (p247) In the second stage children use a much greater number of verbs in the past tense, some of which are irregular but most of which employ the regular past tense ending of "-ed" added to the root of the verb. [...] Surprisingly, children at this stage take a step backwards. They make mistakes on the apst tense of the irregular verbs that they had previously given correctly. These errors are known as over-regularization errors
* (p247) In the third stage children cease to make these over-regularization errors and regain their earlier performance on the common irregular verbs while at the same time improving their command of regular verbs
* (p254) According to James, neonates inhabit a universe radically unlike our own, composed solely of sensations, with no sense of differentiation between self and objects or between self and other, and in which the infant is capable only of reflex actions. It takes a long time for this primitive form of existence to become the familiar world of people and objects and for reflexes to be replaced by proper motor behavior
* (p254) Researchers have developed techniques for exploring the expectations that infants have about how objects will behave. It is now widely held that even very young infants inhabit a highly structured and orderly perceptual universe. The most famous technique in this area is called the dishabituation paradigm
* (p255) The basic idea behind the dishabituation paradigm is that infants look longer at events that they find surprising
* (p256) Baillargeon's drawbridge experiments, together with other experiments using the same paradigm, have been taken to show that even very young infants have the beginnings of what is sometimes called folk physics (or naïve physics) - that is to say, an understanding of some of the basic principles governing how physical objects behave and how they interact
* (p257) Elizabeth Spelke four principles:
	* Principle of cohesion: surfaces belong to a single individual if and only if they are in contact
	* Principle of contact: only surfaces that are in contact can move together
	* Continuity constraint: an object cannot be present and then suddenly absent (peekaboo)
	* Solidity constraint: it is impossible for more than one object to be in a single place at one time
* (p262) According to the neural networks approach to object permanence, the expectations that infants have about how objects will behave reflect the persistence of patterns of neural activation - patterns that vary in strength as a function of the number of neurons firing, the strength and number of the connections between them, and the relations between their individual firing rates
* (p271) Fodor and Pylyshyn's argument against neural networks being a serious competitor of the physical symbol system hypothesis (aka Fodor-Pylyshyn dilemma)
	1. Either artificial neural networks contain representations with separable and
	recombinable components, or they do not.
	2. If they do contain such representations, then they are simply implementations of
	physical symbol systems.
	3. If they do not contain such representations, then they cannot plausibly be described as
	algorithmic information processors.
	4. Either way, therefore, artificial neural networks are not serious competitors to the
	physical symbol system hypothesis.
* (p281) An agent is a system that perceives its environment through sensory systems of some type and acts upon that environment through effector systems
* (p286) Horizontal faculty psychology: Domain-general
* (p286) Vertical faculty psychology: Domain-specific
* (p287) Domain-specific faculties are informationally encapsulated, they can only call upon a very limited range of information
* (p287) Each vertical cognitive faculty has its own database of information relevant to the task it is performing, and it can use only information in this database (Fodor call these cognitive faculties cognitive modules)
* (p288) Modular processes have the following four characteristics:
	* Domain-specificity: Modules are highly specialized mechanisms that carry out very specific and circumscribed information-processing tasks
	* Informational encapsulation: Modular processing remains unaffected by what is going on elsewhere in the mind. Modular systems cannot be "infiltrated" by background knowledge and expectations, or by information in the databases associated with different modules
	* Mandatory application: Cognitive modules respond automatically to stimuli of the appropriate kind, rather than being under any executive control. It is evidence that certain types of visual processing are modular that we cannot help but perceive visual illusions, even when we know them to be illusions
	* Speed: Modular processing transforms input (e.g. patterns of intensity values picked up by photoreceptors in the retina) into output (e.g. representations of three-dimensional objects) quickly and efficiently
* (p289) Two further features that sometimes characterize modular processes:
	* Fixed neural architecture
	* Specific breakdown patterns

# See also

# Sources
* Bermúdez, José Luis. Cognitive Science: An Introduction to the Science of the Mind. Cambridge: Cambridge University Press, 2010.
