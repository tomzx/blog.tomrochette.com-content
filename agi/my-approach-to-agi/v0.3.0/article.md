---
title: AGI v0.3.0
created: 2017-08-26
taxonomy:
  tag: [artificial general intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore
* Define what is intelligence
* How does one solve problems?
* How does one decompose problems?
* How does encode to knowledge within an existing agent?
* How much computation power is required to replicate the human abilities and response time?
* How difficult would it be for human beings to actually be able to speak with animals given that their language should be a lot simpler than ours?
* What information stays where and for how long? How does it disintegrate?
* What experiments can one do in order to learn more about the brain?
* Is a brain architecture where trains of thought are constructed an interesting idea?
	* How are trains of thought actually constructed? Aren't trains of thought simply logical reasoning that is made by the conscious mind?

# Overview

# What is the end goal?
To produce an entity or an agent that could be considered as a human being.
This agent would evolve/improve on its own but might be bootstrapped with the knowledge of a initial host.

# What is needed to produce human-like agents?
One major component of such agent is the ability to use language or more specifically a human language such as English.
To be able to use the language, it is likely that you want the agent to be able to associate words or symbols with concrete/physical objects.
Thus, it needs to be able to associate external stimuli with previously experienced stimuli that are similar (similarity metric).
One potential way to create some form of language learning that would appear human would be to apply the same rules as someone that would be learning a new language. For instance first learn the pronouns, then learn basic words that allow you to communicate with others such as want, need, like/dislike, feel, think, afraid, thirsty, hungry, come, see, etc.
Given only pronouns, you still need to be able to associate these symbols with what they represent, generally the person or the object it refers to.
It is questionable whether a verbal and symbolic language should be the low level foundation of such system or whether we should go lower, using something like mathematics as the foundation.
A verbal system would require the agent to have internal concepts that describe what it means to be executing some specific verb.

## A subsymbolic approach
It might be possible to create some sort of vector where each value would be between 0 and 1 and would represent a verb and whether or not this person would want to enact this verb.
This is already something done with sentiment analysis through facial recognition where we try to assess the most likeliest emotion.
In a similar fashion, what we would try to do is to determine what the person wants to be doing. We would not necessarily specify what it applies to but at least we would know the sort of actions the agent would be interested in accomplishing.
This can be seen as competition between various internal needs and wants. The strongest action (the highest value between 0 and 1) is the one being enacted.

# What is the purpose?

# What are the approach with the most chances of success?
## Learn from existing systems
Learn about neurobiology
Understanding how the brain works
Learn about child development
	Specifically we're interested to determine what are innate and what are acquired skills and abilities. For skills that are innate, it means that the information is included as part of the DNA
Learn about genetics
	* Specifically what we believe is included as part of DNA or even more specifically what are the cognitive abilities that are included as part of DNA

## Learn from mathematical/computational models
Learn about machine learning
	Understanding problems through machine learning
Learn about computation and complexity theory

# Intelligence based on neural systems
So far we know one interesting fact which is that there are a lot of other animals which also have all the components of the brain that we have however they are not considered to be as intelligent as human beings
It does not appear to be the amount of neurons that you have in your central nervous system that determines whether or not you have human intelligence level which seems to disprove the idea of the emergence if intelligence by the sheer fact that you have a specific number of neurons (elephants are known to have over 257 billion neurons in their whole nervous system, vs 86 billion neurons for humans, and long-finned pilot whale are known to have 37.2 billion neurons in their cerebral cortex, vs 21 billion neurons for humans)
However it's very important to note that we're generally at the top of the hierarchy in terms of the number of total neurons in the body or in the cerebral cortex
In the case of cerebral cortex neurons it appears that we have at least twice the amount of new run as any land mammal, the closest listed being the gorilla
In terms of number of synapses, the whole human body has about 1.5*10^14 synapses while the closest animal that is listed on Wikipedia is the cat with 1*10^13
It's important to note that there's about a thousand fold difference in the number of synapses between humans and cats however there's only a tenfold difference in number of synapses
=> Might have to do with our prefrontal cortex

If we look at household animals such as the dog and the cat they appear to have some level of intelligence regarding their own "will" regarding where they are and where they want to be
However it's questionable as to whether all of this is mechanical and it's just complexion of that it appears to be will and not just automation
Just one could ask himself how to differentiate between automatic behavior and decisional behavior if such separation is actually possible

Is there a list of where the separation between non intelligent and intelligent being would be? Is it useful to define non-human beings as intelligence and have a scale that could apply to anything?
Most consider only human beings to be intelligent and everything else to be non intelligent, but should there exists degrees of intelligence between species of the animal kingdom?
Can we assume that learning and developing theories based on lower intelligence creatures to more intelligent creatures will allow us to understand the inner workings of the brain and intelligence itself?

Is complexity any good indicator of intelligence or is it something coating for a lot more innate abilities?
How much compression can you assume is part of DNA? In other words, say we have about one kilobyte of information, how big can we expect this to decompress to given that it is likely that the compression dictionary is very close to the same for all human beings (8 billions+ instances of it) (it is defined by protein folding and physically possible molecules or polymers, assemblages, etc.)

Mathematics seems to be the appropriate foundation for a system, as it can scale from really simple problems such as finding the value of x to complex ones with enormous tensors.

# Sensory modalities
Hearing/tasting/touching/seeing/smelling
Possibly easier to start from speech recognition (lower dimension)
Hearing is 3d (location of the source) + 2d (time and energy amplitude)
Smell is the unique recognition of chemical particles in a certain ratio
Taste is similar to smell
Touching is a 3d signal (source) as well as a type and intensity (which may be conveyed through the volume of neurons signaling the same message)
Vision is a 4d signal, that is, a 2d image (x, y) with light intensity/frequency, and time

Is sensory modality the first step?
If there are no senses/inputs, then there is nothing to do

# Roadmap

# References
* https://en.wikipedia.org/wiki/List_of_animals_by_number_of_neurons
