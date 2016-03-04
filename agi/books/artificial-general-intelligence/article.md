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
* Dynamical systems theory

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
* The user can attach an initial priority value to a task, but the allocation also depends on the current situation of the system, as well as on how well the task processing goes

## 3.6 Autonomy and Creativity
* The system's behavior depends to a certain extent on its own tasks, which are actually more or less dependent of the original processes, even though historically derived from them
* In extreme form, the derived tasks may become so strong that they even prevent the input tasks from being fulfilled
* This can lead to creative and original behaviors, because the system is pursuing goals that are not directly assigned by its environment or its innateness

# The Novamente Artificial Intelligence Engine

## 1.2 Novamente for Knowledge Management and Data Analysis
* Novamente may be used in two complementary ways to work with unstructured text:
	* "Information retrieval" oriented, wherein a text is taken as a series of characters or a series of words, and analyzed statistically
	* Natural language processing (NLP) oriented, wherein an attempt is made to parse the sentences in the texts and extract their meanings into semantic-relationship form
* To interact with human users, the Novamente design supports a variety of different modalities, including coventional search-engine and NLP queries, web forms queries, dynamic visualization and automated report generation

## 2 Enabling Software Technologies
* Make use of an hybrid of NLP and formal languages (such as first-order logic) where one would specify the relations and constraints in his given queries
* Two categories of enabling technologies
	* Distributed software architecture
	* Database integration

## 2.2 Database Integration and Knowledge Integration
* 4 strategies to deal with databases
	* Federation: Create a common GUI for separate DBs
	* Amalgamation: Create formal mappings between the schema of different DBs
	* Schema translation: Create a new RDB combining information from multiple DBs
	* Knowledge integration: Create a translator mapping DB contents into a "universal formal knowledge representation"

## 3.1 What Is General Intelligence?
* Novamente's goal is to create a nonhuman digital intelligent system - one that will complement human intelligence by carrying out data analysis and management tasks far beyond the capability of the human mind; and one that will cooperate with humans in a way that brings out the best aspects of both the human and the digital flavors of general intelligence
* General Intelligence is the ability to achieve complex goals in complex environments
* A system is fully generally intelligence for complexity N if it can achieve any goal of complexity N in any environment of complexity N

## 3.2 The Integrative Approach to AGI
* 3 basic approaches to AGI are possible:
	* Close emulation of the human brain in software
	* Conception of a novel AGI architecture, highly distinct from the brain and also from narrow AI programs
	* An integrative approach, synthesizing narrow AI algorithms and structures in a unique overall framework, perhaps guided to some extent by understanding of the human brain
* Roughly 2/3 of the Novamente design is based on existing narrow AI approaches

## 3.3 Experiential Interative Learning and Adaptive Self-modification
* Software and mathematics alone, no matter how advanced, cannot create an AGI
* Intelligence most naturally emerges through situated and social experience
* Human brains learn to think through being taught, and through diverse social interactions
* For a software system to demonstrate AGI, it must demonstrate:
	* A coherent autonomy as an independent, self-perceiving, self-controlling system
	* The ability to modify and improve itself based on its own observations and analyses of its own performance
	* The ability to richly interact with, and learn from, other minds (such as human minds)

## 4 The Psynet Model of Mind
* The psynet model is based on what Ray Kurzweil calls a "patternist" philosophy
* A mind is neither a physical system, nor completely separate from the physical
* A mind is something associated with the set of patterns in a physical system
* A pattern in an entity is considered as an abstract computer program that is smaller than the entity, and can rapidly compute the entity
* One particular general goal is posited as critical to the goal system of any intelligent system: the creation and recognition of new patterns
* Patterns dynamics
	* Association: Patterns, when given attention, spread some of this attention to other patterns that they have previously been associated with in some way
	* Differential attention allocation: Patterns that have been valuable for goal achievement  are given more attention, and are encouraged to participate in giving rise to new patterns
	* Pattern creation: Patterns that have been valuable for goal achievement are mutated to yield new patterns, and are combined with each other to yield new patterns
	* Relationship reification: Habitual patterns in the system that are found valuable for goal achievement, are explicitly reinforced and made more habitual
* Pattern networks
	* Hierarchical network: Patterns are habitually in relations of control over other patterns that represent more specialized aspects of themselves
	* Heterarchical network: The system retains a memory of which patterns have previously been associated with each other in any way
	* Dual network: Hierarchical and heterarchical structures are combined, the dynamics of the two structures working together harmoniously
	* "Self" structure: A portion of the network of patterns forms into an approximate (fractal) image of the overall network of patterns
* 3 systems built on the psynet model
	* 1994: Antimagicians: An experimental psy-net inspired program in the pure self-organizing-systems vein, with very few built-in structures and an intention for the structures and dynamics of mind to emerge via experience. The anticipated emergence was not observed, and a more engineering-oriented approach was attempted.
	* 1996-2001: The Webmind AI Engine: A large-scale Java software system that derived its software design from the psynet model in a very direct way. Parts of Webmind were successfully used in the domain of financial prediction and information retrieval. A great amount of useful prototyping was done. Directly mapping the psynet model's construct to object-oriented software structures leads to serious problems with computational efficiency.
	* 2001-2009/now: Novamente: An entirely different approach, embodying a highly flexible, computationally efficient AGI framework, which could be used to implement a variety of AI systems. The framework includes 3 main aspects: the DINI architecture, the philosophy of tightly-coupled integrative AI, and the Novamente "Mind OS" architecture.

## 5 The Novamente AGI Design
* The Novamente AI Engine is a large-scale, object-oriented, multithreaded software system
* Written in C++ with a few externally-facing components written in Java
* Development primarily on Linux
* A Novamente system is a collection of analytical clusters, most of them tightly-integrated, some of them more simple and specialized
* Integrate a number of narrow AI approaches
* Here are some majors aspects of the Novamente design:
	* Nodes: May symbolize entities in the external world, embody simple executable processes, symbolize abstract concepts or serve as components in relationship-webs signifying complex concepts or procedures
	* Links: May point to nodes or links. Embody various types of relationships between concepts, percepts or actions. The network of links is a web of relationships.
	* MindAgents: A software object embodying a dynamical process such as importance updating, concept creation, or first-order logical inference. Acts directly on individual Atoms, but is intended to induce and guide system-wide dynamical patterns.
	* Mind OS: Enables diverse MindAgents to act efficiently on large populations of Nodes and Links distributed across multiple machines.
	* Maps: Declarative or procedural knowledge, as a pattern distributed across many Nodes and Links.
	* Units: A collection of Nodes, Links and MindAgents, living on a cluster of machines, collectively devoted to carrying out a particular function.

## 5.1 An Integrative Knowledge Representation
* Knowledge is represented in Novemente on two levels:
	* Atoms: Software objects that come into two species: Nodes or Links.
	* Maps: A set of Atoms that tend to be activated together, or tend to be activated according to a certain pattern.

## 5.2 The Mind OS
* Similar to an operating system:
	* Determines the task that should be executed (MindAgents)
	* Manage the duration of the MindAgent execution
* Communication with a Mind OS can be done through:
	* A shell interface
	* XML
	* A Java/J2EE middleware layer
	* (designed but not implemented) A functional-logical programming language called Sasha
	* (designed but not implemented) A knowledge encoding language called NQL (Novamente Query Language)
* Mind OS does
	* Multi-threading
	* Plugging/Scheduling of heterogeneous agents
	* Distributed knowledge with local proxies and caches
	* Transaction control
	* Communication with external software agents through XML and scripts
	* Task and query processing through ticketing system
	* Adaptive parameter control
	* Dynamic, adaptive load balancing

## 5.3 Atom Types
* Data structures and dynamics have been chosen based mainly on the following criteria:
	* Demonstrated power in narrow AI applications
	* Mutual coherence as an integrative AGI framework
	* Propensity for embodying the dynamics and structures posited by the Psynet Model of Mind
* Different types of nodes
	* Perceptual: Perceived items (word, character, number, pixel)
	* Procedure: Small programs called "schema"
	* Concept: Categories of perceptual or action or conceptual nodes, or portions of maps representing such categories
	* Psyche: Goal and feeling nodes which play a special role in overall system control, in terms of monitoring system health, and orienting overall system behavior
* Different types of links
	* Logical: Symmetric or asymmetric logical relationships among nodes or among links
	* Member: Denotes fuzzy set membership
	* Associative: Denotes generic relatedness, including Hebbian learning and relationships derived from natural language or databases
	* Action-Concept: Conceptual record of the actions taken
	* List and ConcatList: Internally created or externally observed lists

## 5.4 Novamente Maps
* Some Atoms gain meaning only via their coordinated activity involving other Atoms, i.e. their involvement in "maps"
* MaximizeSatisfaction GoalNode is the center of Novamente's motivational system
* Different types of maps found in Novamente
	* Concept map
	* Percept map
	* Schema map
	* Predicate map
	* Memory map
	* Concept-percept map
	* Concept-schema map
	* Percept-concept-schema map
	* Event map
	* Feeling map
	* Goal map

## 5.5 Mind Agents
* Responsible of updating the Atoms in the system
* There are "system maintenance" MindAgents which do things like collecting system statistics, cache Atoms to disk periodically, update caches related to distributed processing, handle queues of queries from users and other machines in the same analytic cluster or other Novamente analytic clusters
* Here is a list of different types of MindAgents
	* First-order inference: Acts on first-order logical links, producing new logical links from old links using the formulas of Probabilistic Term Logic
	* Logical link mining: Creates logical links out of nonlogical links
	* Evolutionary predicate learning: Creates PredicateNodes containing predicates that predict membership in ConceptNodes
	* Clustering
	* Importance updating: Updates Atom importance variables and other related quantities using probabilistic inference
	* Concept formation: Creates speculative, potentially interesting new ConceptNodes
	* Evolutionary optimization: Used for schema and predicate learning and overall optimization of system parameters
* Here is a list of planned Novamente MindAgents
	* High-order inference
	* Logical unification
	* Predicate/Schema formation
	* Hebbian association formation
	* Evolutionary schema learning
	* Schema execution
	* Map encapsulation
	* Map expansion
	* Homeostatic parameter adaptation

## 5.6 Map Dynamics
* A map is a set of Atoms that act as a whole
* Maps may relate to other maps, just like Atoms may relate to each other
* Relationships between maps do not take the form of individual links; they take the form of bundles of links joining Atoms inside on map to the Atoms inside another (no link between maps but links between Atoms inside of each maps)

# Essentials of General Intelligence: The Direct Path to Artificial General Intelligence

## 2 General Intelligence
* Intelligence can be defined simply as an entity's ability to achieve goals - with greater intelligence coping with more complex and novel situations
* General intelligence comprises the essential, domain-independent skills necessary for acquiring a wide range of domain-specific knowledge
* Learning must be autonomous, goal-directed and adaptive
* The mark of a generally intelligent system is not having a lot of knowledge and skills, but being able to acquire and improve them and to be able to appropriately apply them
* An AGI system should be able to learn to recognize and categorize a wide range of novel perceptual patterns
* It should be able to autonomously learn appropriate, goal-directed responses to input contexts (given some feedback mechanism)

## 2.1 Core Requirements for General Intelligence
* Perceived entities/patterns must be stored in a way that facilitates concept formation and generalization
* An effective way to represent complex feature relationships is through vector encoding
* Any practical applications of AGI must inherently be able to process temporal data as patterns in time - not just as static patterns with a time dimension
* AGIs must cope with data from different sense probes and deal with attributes such as: noisy, scalar, unreliable, incomplete, multi-dimensional, etc.
* Another essential requirement of general intelligence is to cope with an overabundance of data
* The system needs to have some control over what input data is selected for analysis and learning - both in terms of which data, and also the degree of detail
* Senses are needed not only for selection and focus, but in order to ground concepts in reality

## 3 Shortcuts to AGI
* In addition to understanding general intelligence, AGI design also requires an appreciation of the differences between artificial (synthetic) and biological intelligence, and between designed and evolved systems
* Work focused on
	* General rather than domain-specific cognitive ability
	* Acquired knowledge and skills, vesus loaded databases and coded skills
	* Bi-directional, real-time interaction, versus batch processing
	* Adaptive attention (focus and selection), vesus human pre-selected data
	* Core support for dynamic patterns, versus static data
	* Unsupervised and self-supervised, versus supervised learning
	* Adaptive, self-organizing data structures, versus fixed neural nets or databases
	* Contextual, grounded concepts, versus hard-coded, symbolic concepts
	* Explicitly engineering functionality, versus evolving it
	* Conceptual design, versus reverse-engineering
	* General proof-of-concept, versus specific real applications development
	* Animal level cognition, versus abstract thought, language, and formal logic
* Self-improvement takes two distinct forms/phases:
	* Coding the basic skills that allow the system to acquire a large amount of specific knowledge
	* The system reaching sufficient intelligence and conceptual understanding of its own design, to enable it to deliberately improve its own design
* Many AI systems do all of their learning in batch mode and have little or no ability to learn incrementally
* In many cases they are unable to adapt beyond the initial training set without reprogramming or retraining
* Intelligent systems must be able to act
	* Acting on the "world" - be it to communicate, to navigate or explore, or to manipulate some external function or device in order to achieve goals
	* Controlling or modifying the system's internal parameters (such as learning rate or noise tolerance, etc.) in order to set or improve functionality
	* Controlling the system's sense input parameters such as focus, selection, resolution (granularity) as well as adjusting feature extraction parameters
* AGI systems must inherently be designed to acquire knowledge by themselves
* They need to control what input data is processed, where specifically to obtain data, in how much detail, and in what format
* All acquired knowledge and skills is encoded in one integrated network-like structure
* One can say that "high-level intelligence is conceptual intelligence"
* Autonomous concept formation is one of the key tests of intelligence
* Design to achieve the desired functionality of the brain rather than try to replicate evolution's design
* Here is a list of desirable cognitive features that can be included in an AGI design that would not exist in a reverse-engineered brain:
	* More effective control of neurochemistry (emotional states)
	* Selecting the appropriate degree of logical thinking versus intuition
	* More effective control over focus and attention
	* Being able to learn instantly, on demand
	* Direct and rapid interfacing with databases, the Internet and other machines - potentially having instant access to all available knowledge
	* Optional "photographic" memory and recall on all senses
	* Better control over remembering and forgetting (freezing important knowledge, and being able to unlearn)
	* The ability to accurately backtrack and review thought and decision processes (retrace and explore logic pathways)
	* Patterns, nodes and links can easily be tagged (labeled) and categorized
	* The ability to optimize the design for the available hardware instead of being forced to conform to the brain's requirements
	* The ability to utilize the best existing algorithms and software techniques - irrespective of whether they are biologically plausible
	* Custom designed AGI can have a simple speed/capacity upgrade path
	* The possibility of comprehensive integration with other AI systems (like expert systems, robotics, specialized sense pre-processors, and problem solvers)
	* The ability to construct AGIs that are highly optimized for specific domains
	* Node, link, and internal parameter data is available as "input data" (full introspection)
	* Design specifications are available (to the designer and to the AGI itself!)
	* Seed AI design: A machine can inherently be designed to more easily understand and improve its own functioning - thus bootstrapping intelligence to ever higher levels
* Discoveries in cognitive psychology point towards generalized pattern processing being the foundational mechanism for all higher level functioning

## 4 Foundational Cognitive Capabilities
* General intelligence requires a number of foundational cognitive abilities:
	* Remember and recognize patterns representing coherent features of reality
	* Relate such patterns by various similarities, differences, and associations
	* Learn and perform a variety of actions
	* Evaluate and encode feedback from a goal system
	* Autonomously adjust its system control parameters
* Pattern acquisition through lazy learning
	* Stored feature patterns with adaptive fuzzy tolerances
	* Recognition/Pattern matching through a competitive winner-take-all, as a set or aggregate of similar patterns, or by forced choice
* The matching algorithm is able to recall patterns by any dimension

## 5 An AGI in the Making
1. Development framework
2. Memory core and interface structure
3. Individual foundational cognitive components
4. Integrated low-level cognition
5. Increased level of functionality

* AGI engine with the following basic components:
	* A set of pluggable, programmable (virtual) sensors and actuators (called probes)
	* A central pattern store/engine including all data and cognitive algorithms
	* A configurable, dynamic 2D virtual world, plus various training and diagnostic tools
* Additional details:
	* Data recorder with playback
	* Data visualization and editing tools
	* A cognitive core with many foundational cognitive algorithms
	* An interface manager which communicates with the probes, the cognitive core and the data recorder

## 5.1 AGI Engine Architecture and Design Features
* Can be separated into three parts:
	* Cognitive core
	* Control/Interface logic
	* Input/Output probes
* Cognitive core
	* Central repository of all static and dynamic data patterns - including all learned cognitive and behavioral states, associations, and sequences
	* All data is stored in a single, integrated node-link structure
* Control and interface logic
	* Coordinates the network's execution cycle, drives various cognitive and housekeeping algorithms, and controls/adapts system parameters
	* Via an interface manager, communicates data and control information to and from the probes
* Probes
	* Programmable feature extractors, variable data resolution, focus and selection mechanisms
* Development environment, language, and hardware
* Implemented in C#/.NET
* Practical/Proof-of-concept prototype performance can be achieved on a single PC (2 GHz, 512 MiB)

# See also

# Sources

* Goertzel, Ben, and Cassio Pennachin. Artificial General Intelligence. Berlin: Springer, 2007.
