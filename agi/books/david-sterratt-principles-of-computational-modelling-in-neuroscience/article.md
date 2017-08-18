---
title: David Sterratt - Principles of Computational Modelling in Neuroscience - 2011
created: 2017-07-29
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore
*  Given a dendrogram at various stages of development (times $t_n$), can a RNN model accurate learn how to reproduce such process?
* Is there data available online on neurite development in the form of dendrograms?

# Overview

# Notes
## Chapter 1 - Introduction
### 1.1 What is this book about?
#### 1.1.1 Theories and mathematical models
* A theory is described in words, or perhaps with a diagram
* To derive predictions from the theory we can deploy verbal reasoning and further diagrams
* We are faced with the problem that there is only one theory but two possible conclusions; the theory is logically inconsistent
	* The problem has arisen for two reasons:
		* The theory was not clearly specified to start with
		* The theory is now too complex for qualitative verbal reasoning to be able to turn it into a prediction
* The solution to this problem is to specify the theory more precisely, in the language of mathematics (mathematical model)

#### 1.1.2 Why do computational modelling?
* Modelling is used as an aid to reasoning
* Modelling removes ambiguity from theories
* The models that have been developed for many neurobiological systems, particularly at the cellular level, have reached a degree of sophistication such that they are accepted as being adequate representation of the neurobiology
* Advances in computer technology mean that the number of interacting elements, such as neurons, that can be simulated is very large and representative of the system being modelled
* In principle, testing hypotheses by computational modelling could supplement experiments in some cases

## Chapter 2 - The basis of electrical activity in the neuron
* Neurons can be represented as an electrical circuit

### 2.1 The neuronal membrane
* Typically, there is greater concentration of extracellular sodium ($Na^+$) than intracellular sodium, and conversely for potassium ($K$)
* The bulk of the membrane is composed of the 5 nm thick lipid bilayer

## Chapter 3 - The Hodgkin-Huxley model of the action potential
### 3.1 The action potential
* Action potentials are characterised by a sharp increase in the membrane potential (depolarisation of the membrane) followed by a somewhat less sharp decrease toward the resting potential (repolarisation)
* The main difference between the propagation of action potentials and passive propagation of signals is that action potentials are regenerative, so their magnitude does not decay during propagation

### 3.3 Simulated action potentials
#### 3.3.1 Space clamped action potentials
* During the absolute refractory period after an action potential, it is impossible to generate a new action potential by injecting current
* Thereafter, during the relative refractory period, the threshold is higher than when the membrane is at rest, and action potentials initiated in this period have a lower peak voltage
* It should be harder to generate an action potential during this period for two reasons
	* The inactivation of the sodium conductance means that any increase in $m$ due to increasing voltage will not increase the sodium conductance as much as it would when $h$ is at its higher resting value
	* The prolonged activation of the potassium conductance means that any inward sodium current has to counteract a more considerable outward potassium current than in the resting state

### 3.5 Building models using the Hodgkin-Huxley formalism
#### 3.5.1 Model approximations
* Each channel type is permeable to only one type of ion
	* Implicit in the HH model is the notion that channels are selective for only one type of ion
* The independence principle
	* It is assumed that each type of current does not depend on the concentration of other types of ion
* The linear instantaneous I-V characteristic
	* All the ionic currents that flow through open gates have a linear, quasi-ohmic dependence on the membrane potential

## Chapter 4 - Compartmental models
### 4.2 Constructing a multi-compartmental model
* The general approach is to represent quasi-isopotential sections of neurite (small pieces of dendrite, axon or soma) by simple geometric objects, such as spheres or cylinders, which we term compartments

#### 4.2.1 Mapping morphology
* There may not necessarily be a one-to-one correspondence between the representation of morphology with simple geometric shapes and the final electrical circuit. A single long dendrite may be represented adequately by a single cylinder, but to model the voltage variations along the dendrite it should be represented by multiple compartments

#### 4.2.2 Compartment size
* In compartment modelling, the choice of compartment size is an important parameter in the model
* It is assumed that each compartment is effectively isopotential
* Using a small compartment size reduces the error but increases the number of compartments needed to represent the morphology, and consequently the overall computation for simulations
* A general and often quoted rule of thumb is to make the compartment size no longer than 10% of the length constant $\lambda$
* An alternative rule of thumb is to make the compartment size no more than 10% of $\lambda_f$, where $f$ is chosen to be high enough that the transmembrane current is largely capacitive

### 4.3 Using real neuron morphology
##### 4.3.1 Morphological errors
* Many fixation procedures lead to shrinkage or distortion of the slice and, consequently, the reconstructed neuron
* Shrinkage factors can have a serious impact on the overall surface area of the cell
* It is possible to quantify the amount of shrinkage and apply these correction factors to the final data. This can be done by measuring the overall slice shrinkage and assuming that cells shrink in a uniformly similar manner

##### 4.3.3 Simplifying the morphology
* Passive dendrites are equivalent electrically to a singly cylinder, provided that they obey the following rules:
	* Specific membrane resistance ($R_m$) and specific axial resistance ($R_a$) must be the same in all branches
	* All terminal branches must end with the same boundary conditions
	* The end of each terminal branch must be the same total electrotonic distance from the origin at the base of the tree
	* For every parent branch, the relationship between the parent branch diameter ($d_1$) and its two child branches diameters ($d_2$ and $d_3$) is given by (known as the '3/2' diameter rule)
$$
d_1^{3/2} = d_2^{3/2} + d_3^{3/2}
$$

### 4.6 Adding active channels
#### 4.6.1 Ion channel distributions
* One of the immediate consequences of adding active channels is the explosion in the number of parameters in the model and a significant increase in the number of degrees of freedom
* One approach to reducing the number of degrees of freedom is to parameterise channel densities throughout a dendrite in terms of distribution functions
* The simplest of these would be a uniform distribution where a single maximum conductance density parameter is used in all compartments of the tree
* Linear distributions, where the conductance density changes with a linear gradient as a function of distance from the soma, is an example of a slightly more complex distribution function

## Chapter 10 - The development of the nervous system
### 10.1 The scope of developmental computational neuroscience
#### 10.1.1 Background
* The development of the nervous system occurs after a complex series of developmental steps, many of which are common to the development of very different multicellular organisms
* Stages of development
	* Cell division
	* Gastrulation
	* Neurulation
	* Development of the nervous system
* Typical research problems investigated
	* The development of neural morphology
	* How nerve cells know where to go
	* The development of patterns of nerve connections
	* Features

### 10.2 Development of nerve cell morphology
#### 10.2.1 Development of morphology
* The cell's morphological development can be characterised into a number of stages:
	* neurite initiation
	* neurite differentiation and elongation
	* neurite (axon and dendrites) elaboration
		* elongation and branching
		* axon pathfinding
		* dendrite space filling
* To formulate a model of neurite development, the first question to ask is: which particular aspects of neurite morphology do we seek to reproduce in our model?

#### 10.2.3 Modelling cell growth
* Models of development seek to capture how neuritic morphology evolves with time. Such growth algorithms may still be statistical, but now need to specify how the distributions of the fundamental parameters change over time
* Basic models describe the elongation rate and branching rate of neurite segments, and how these rates may change with time and tree growth
* Two approaches have been followed
	* Formulate the simplest possible description of the elongation and branching rates that generates trees with realistic morphology
	* Describe branching and elongation rates as functions of identifiable biophysical parameters
* The BESTL algorithm
	* Aims to reproduce the branching structure and segment lengths of dendrites
	* Does not consider diameters
	* Only terminal segments are assumed to lengthen and branch, with branching events resulting in bifurcations
	* Segment branching and elongation are handled as independent processes specified by a branching rate and an elongation rate
	* The branching rate of each terminal segment $j$ is
$$
p^j(t) = D(t)C(t)2^{-S\gamma_j}n(t)^{-E}
$$
where
$$
C(t) = \frac{n(t)}{\sum_{j=1}^{n(t)} 2^{-S\gamma_j}}
$$
* $D(t)$ is the basic branching rate at time $t$
* $C(t)$ is a normalising factor
* $n(t)$ is the number of terminal segments
* $\gamma_j$ is the centrifugal order of terminal segment $j$
* $S$ is a constant determining the dependence of branching on centrifugal order
* $E$ is a constant determining the dependence of branching on the number of terminals
* Elongation is handled independently of branching. Following a branching event, the algorithm proceeds by giving each daughter branch an initial, short length and an elongation rate, both drawn from gamma distributions
* Elongation may continue after branching has ceased, with developmental time being divided into an initial branching phase followed by an elongation-only phase
* Elongation rates in the latter phase may be different from the branching phase

#### 10.2.4 Biophysical models of cell growth
* A basic example of this approach considers the production and transportation of the protein tubulin along a growing neurite
* Free tubulin has concentration $c(x, t)$ at a point $x$ along the neurite at time $t$
* Tubulin molecules move by active transport $a$ and diffusion $D$, and degrade with rate $g$
* In the cell body ($x = 0$) synthesis of tubulin occurs at a fixed rate $\epsilon_0 c_0$
* At the distal end of the neurite ($x = l$) assembly of tubulin onto microtubules occurs at rate $\epsilon_l c$, and spontaneously disassembly with rate $\zeta_l$
* Three growth modes are evident in this model
	* Growth to long lengths is determined by active transport of tubulin to the growth tip
	* Growth to short lengths is dominated by diffusion
	* Moderate lengths are achieved by a balance of active transport and diffusion
* An alternative model assumes that, rather than determining the elongation rate, the tubulin concentration at a neurite tip determines the branching rate $p(t)$ of the terminal

# See also

# References
* Sterratt, David, et al. Principles of computational modelling in neuroscience. Cambridge University Press, 2011.