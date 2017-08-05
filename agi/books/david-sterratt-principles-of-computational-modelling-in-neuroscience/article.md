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

# See also

# References
* Sterratt, David, et al. Principles of computational modelling in neuroscience. Cambridge University Press, 2011.