---
title: Knowledge transfer
created: 2016-05-11
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview

** How can one transfer the models in his brain/mind in an efficient, low time-active (using as little brain cycles as possible) manner?**
* Type down everything that is in one's mind in a document
* Say aloud everything that is in one's mind and record it in audio documents so that programs may be executed on the content to extract and generate models
* Write down how things are related (simple anonymous relations or highly specified relations)
* Record all written, spoken and visual content in a digital format so that programs may be executed on the content to extract and generate models
* Convert neural signals in the brain (electroencephalogram recording) into frequency functions (use BCI hardware such as OpenBCI)
* Mind uploading: Scan the whole neural substrate/brain and reproduce it in a digital format
	* Copy-and-transfer
	* Gradual replacement

# Notes on building a graph only using pairs

The premise of this section is that at a high level, the brain stores concepts and relations between them. One simple model of such structure is the pair, where two concepts are related to one another through an anonymous relation.

Here we explore how we could efficiently build a graph composed of such concepts and relations and what operations it is possible to apply on such graph.

## Things of interest
* When adding new concepts, it would be interesting to record their creation date
* Easy to add/delete concepts/relations

## Question
* How to separate different concepts using the same identifier?
	* Allocate a uuid?
* How to prevent duplicate entry of information (information already present)
	* Build a management system with autocompletion?
* How to reduce the amount of information that needs to be repeated
	* Use templates?
	* Use discovery in order to attempt to discover the most optimal relation structure?
* Can classes and instances be inferred simply from the data?
	* If we were to structure knowledge through a tree structure (no cycle), the most abstract concepts would be at the top (internal nodes) and the more concrete examples at the bottom (leafs). In other words, the more you are at the center of the graph (near the top of the tree), the more likely you are to be an abstract concept (class), while the further you are from the center of the graph, the more likely you are to be a concrete concept (instance)
* What is the best way to view this multidimensional graph?
	* Central concept with first degree relations?
		* All represented as text/list instead of a graph, where the central concept is at the top and the relations are under it
* Is there value to add a third value describing the relation between two concepts?
	* There probably is, however adding more details obviously complexifies the whole concept of the pair defining relations
	* If we accept to add a third value, then what's to prevent us from adding more values? (slippery slope argument)
* How can certainty be assessed? (some things I am 100% sure, others I can only suppose)
	* Certainty could be assessed as 100% if unspecified, otherwise a measure could be given when specifying a relation
		* A B 0.5
* How can information be extracted/explored in a structured/automated manner?
	* Templates can manually be created and assigned to concepts (not straightforward though, it would require labels (as concepts) to be attached to templates)
* Can some sort of template be constructed based on the information in the graph? (a person generally has a list of friends, a family, went to some schools, has a list of hobbies, etc.)
	* Not really as we have no idea of the type of relations that exist between concepts
	* It is possible to see certain things such that a person has link to other people (friends, family, coworkers, etc.) or some topics that are related to hobbies, sports, music or movie genre preferences, etc. however none of these relations can truly be automatically extracted
* Is the graph view the most appropriate to view and edit this type of information? Would a text visualization be as appropriate?
	* The most appropriate? At this point in time, it seems appropriate, however being the **most** appropriate, I am unsure
	* A text visualization may be as appropriate when visualizing first degree concepts, but as soon as we increase the depth of the visualization, it becomes less and less valuable/easy to understand
* Is there any value in suggesting elements related to an element that was just added?
	* In general, the answer would be no: when defining a new concept as part of a hierarchy, if it is properly placed, then it should be mutually exclusive with its siblings and be transitively related to the abstractions of the concept it was attached to
	* However a concept such as a person may relate to other people and so, by linking a person to another, it is likely that they share similar friends, parents, siblings, coworkers, etc.
* How can the most appropriate concepts be suggested while entering information about a concept? For instance, if I'm filling in information about a new person I just met, how can I get suggestions about linking this relation with "Person" and so on instead of "Anything"? If the City is transitive with the Province and then the Country, I'd rather link a person to his/her City instead of linking to all 3 concepts
	* If enough concepts are related to the newly created concept, it may be possible to attempt to do something like template matching, that is, attempt to identify other concepts which have similar relations and suggest "missing" relations
* What is the most appropriate way to store such information? Are text pairs the most appropriate way? What if I want to keep this information under version control?
	* Text pairs make sense when the size of the graph is small as it is unlikely that duplicate are present
		* However, as soon as duplicates present themselves, then we may want to be able to uniquely identify them which makes this solution less straightforward (requiring elements to be identified using some sort of unique ID)
	* Text format however is one of the most practical way to store data under version control
* If I were provided with an existing graph structure, what would be the most efficient way for me to accept/reject parts of the given graph?
	* It would most likely be required for the user to go over all of the concepts and relations to determine if he agrees or disagrees with them, however that is a huge amount of effort
	* What can be done is to go through the existing structure from the top down, and as soon as a concept is not known, then everything under it may be assumed as unknown as well
		* It is still possible to know concepts under a more abstract concept, thus the user may prefer to add some degree of uncertainty on the concepts that have not been reviewed or simply completely ignore the related concepts
* What would be some ways to minimize the amount of work/effort to build such graph?
	* Import a graph from someone else
	* Build the graph by re-using subgraph shared by others
	* Use of templates/schemas (pre-defined concepts placeholder and relations)
* What is the value in building such graph?
* Is it possible to reduce the amount of time spent reviewing the graph? If so, by which means?
* Can the abstractness/concreteness of a concept be assessed by its relations?
* What is the limit to the sort of relations that can be defined using only pairs?
	* These two things are related, how? I don't know...

# See also

# Sources
