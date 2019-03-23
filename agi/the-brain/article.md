---
title: The brain
created: 2016-06-25
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore
* Is the whole neural architecture designed such that types (input/output formats) are already defined by the time we are born? In other words, the neural architecture is static and definitive (e.g. it has X, Y, Z layers of type A, B, C to process vision)
* How is it decided which neuron will take responsibility for recalling something? Is there any mechanism that prevents the neuron's "memory" from being replaced by something else?
* What prevents others species from accomplishing the same thing as human beings?
* Is the brain architecture such that it adapted to the format of its various sensory inputs or is it generic enough that it will "adapt" to any input format (2x2 grid vs scrambled input)
	* It can adapt to changes (such as replacing left/right vision) but it might not be flexible enough to deal with too much variability (i.e., the scrambled input case)
* Is the brain able to process signal in a manner similar to an FFT? Such that images and sounds can be compared in the frequency domain for variations/changes
* How are the various neural signals able to stay synchronized with one another (such as the signals from the eyes or ears)?
* What is the likeliest next iteration in our senses? The ability to interact with a computer interface?

# Overview

## What we think we know
* Many billions of neurons, $86 \times 10^9$ neurons[^2]
* Approximately $150 \times 10^12$ synapses[^4]
* The maximum firing rate of a neuron is between 250-1000 Hz (maximum based on the absolute refractory rate, which is about 1 ms), with an average of 0.1-2 Hz[^3].
	* It takes between 400 and 550 ms to process speech and comprehend it consciously[^6], which means at best 550 neuron layers deep
		* Sound registered (50-150 ms)
		* Emotional tone registered (150-200 ms)
		* Structure of word stream analyzed and meaning of words extracted (250-350 ms)
		* Meaning consciously comprehended (400-550 ms)
	* It takes about 350 ms to produce speech[^7]
		* Concepts to words (-250 ms)
		* Words to phonology (-200 ms)
		* Phonology to syllables (-150 ms)
		* Articulation (-100 ms)
		* Fine control of articulation (100 ms)
* A neuron fires around 0.16 times per second[^3]. In other words, 16% of your brain is active at any time (on average). Thus $8.6 \times 10^{10} \times \frac{16}{100} = 1.37 \times 10^{10}$ neurons are firing at any particular second.
	* The cortex would generate $2.7 \times 10^9$ spikes per second[^5]
* Small integrative unit that can represent any function
* Synchronous activation increases the propensity of neurons to fire again together
* 6 layers of different neurons types within the cortex
* Numerous Brodmann regions with apparently some specialized functions
	* occipital lobe: vision
	* temporal lobe: auditory stimuli processing, memory, speech
	* parietal lobe: movement, orientation, recognition, perception of stimuli
	* frontal lobe: reasoning, planning, parts of speech, movement, emotions, and problem solving
* The capability for the brain to adapt from certain parts being damaged or removed
* Some damage cannot be recovered
* Some of the brain architecture is incomplete at birth and will complete during the early years of development (which may last up to 10 years for humans)
* The selectivity of overdeveloped neurites is converted into a choice in the same way observing an electron collapses the wave function

# Replicating the brain[^1]
* The human brain contains approximately $10^{11}$ neurons and $10^{15}$ synapses
* An equivalent artificial neural network would require about $10^{15}$ bytes of memory and $10^{17}$ operations per second
* We learn at a rate of 2 bits per second and have a long term memory capacity of $10^9$ bits
* We communicate information at the same rate, 2 bits per second

# As a neural network
* If all neurons are linked to one another as a binary tree (1 parent, 2 children), then the depth of the tree would be approximately 34-35 neurons

# Good/Average/Bad
## Good
* Association
* Recognition

## Average
* Computing small mathematical operations

## Bad
* Computing complex/large numbers
* Rapid and precise computation
* Repetitive computation

# Unsorted
* Brain construction
	* Sequential, produces the 6 layers that are part of the cortex
	* Appears to imply that the construction process follows a specific construction schedule/plan/program
	* Neurons are created, then located, then converted to a given type, then associated with neighboring cells

# See also
* [Senses](../senses)

# References
[^1]: http://mattmahoney.net/agi2.html
[^2]: Herculano-Houzel, Suzana. "The human brain in numbers: a linearly scaled-up primate brain." Frontiers in human neuroscience 3 (2009): 31.
[^3]: http://aiimpacts.org/rate-of-neuron-firing/
[^4]: https://en.wikipedia.org/wiki/List_of_animals_by_number_of_neurons
[^5]: http://aiimpacts.org/metabolic-estimates-of-rate-of-cortical-firing/
[^6]: The human brain book, p148
[^7]: The human brain book, p149

* https://en.wikipedia.org/wiki/List_of_animals_by_number_of_neurons
* https://en.wikipedia.org/wiki/Neural_coding
* https://www.quora.com/How-powerful-is-the-brain-compared-to-a-computer
