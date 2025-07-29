---
title: Hugo de Garis - Artificial Brains (2007)
created: 2016-03-05
taxonomy:
  tag: [artificial general intelligence]
  status: finished
---

## Context

## Learned in this study

## Things to explore

# 1 Introduction
* Using genetic algorithms and neural nets, one can evolve one behavior
* If one can evolve one behavior, one can evolve many
* The concept of an artificial nervous system (automated responses to stimuli)
* One of the first issue with the idea of having one module per behavior was that the addition of new module would slow the overall simulation speed, making it impractical for more than a dozen modules
* Thus, the idea was to make the modules in hardware, at hardware speeds

## 2 Evolvable Hardware
* "Configured" cellular automata to behave as neural networks, which grew, signaled and evolved
* The large number of rules to make this cellular automata (CA) was a problem
* The 2D version required 11000 rules, the 3D version required over 60000 rules
* A simplified model was developed
* It is a 3D model, based on CA
* A neuron is modeled by a single 3D CA cell
* The CA trails (axons and dendrites) are only 1 cell wide
* Every 3D CA cell is given 6 growth bits from the chromosome, one bit per cubic face
* At the first tick of growth clock, each neuron checks the bit at each of its 6 faces
	* If a bit is set to 1, the neighboring blank cell touching the corresponding face of the neuron is made an axon cell
	* If the bit is a 0, then the neighboring blank cell is made a dendrite cell
	* Thus a neuron can grow a maximum of 6 axons or 6 dendrites, and all combinations in between
* At the next clock tick, each blank cell looks at the bit of the face of the filled neighbor that touches it
	* If that filled cell face bit is a 1, then the blank cell becomes the cell type (axon or dendrite) of the touching filled neighbor
	* The blank cell also sets a pointer towards its parent cell (known as parent pointers)
	* These parent pointers are used during the neural signaling phase to tell the 1-bit signals which way to move as they travel along axons and dendrites
* This cellular growth process continues at each clock tick for several hundred ticks until the arborization of the axons and dendrites is saturated in the 3D space
* The collision point between an axon and a dendrite is called a synapse
* The signal is transfered from the axon to the dendrite, and then toward the dendrite's neuron
* Each face of the neuron cube is genetically asigned a sign bit
	* If this bit is a 1, the signal will add 1 to the neuron's 4-bit counter value
	* If the bit is a 0, the signal will substract 1 from the neuron's counter
	* If the counter value exceeds a threshold, usually 2, it resets to zero, and the neuron fires, sending a 1-bit signal to its axons at the next clock tick

## 3 The CAM-Brain Machine (CBM)
* CAM: Cellular Automata Machine
* Consists of 6 main components
	* Cellular Automata Unit: Contains the cellular automata cells in which the neurons grow their axons and dendrites, and transmit their signals
	* Genotype/Phenotype Memory Unit: Contains the 100K bit chromosomes that determine the growth of the neural circuits. The Phenotype Memory Unit stores the state of the CA cells (blank, neuron, axon, dendrite)
	* Fitness Evaluation Unit: Saves the output bits, converts them to an analog form and then evaluates how closely the target and the actual outputs match
	* Genetic Algorithm Unit: Performs the genetic algorithm on the population of competing neural circuits, eliminating the weaker circuits and reproducing and mutating the stronger circuits
	* Module Interconnection Memory Unit: Stores the brain architects inter-module connection specifications (for example "the 2nd output of module 3102 connects to the 134th input of module 63195)
	* External Interface Unit: Controls the input/output of signals from/to the external world (sensors, camera eyes, microphone ears, motors, antenna I/O, etc.)


# See also

# References
* DOI: [10.1007/978-3-540-68677-4_5](https://dx.doi.org/10.1007/978-3-540-68677-4_5)
