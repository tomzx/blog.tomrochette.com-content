---
title: My path to AGI
created: 2015-10-22
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Learned in this study

## Things to explore

# Preface

If you are interested in a more digestible path through the same content I've experienced, I suggest you look up [my suggested path to AGI](../my-suggested-path-to-agi) article. It basically contains most of the stuff I've gone through myself, but it is organized in a constructive manner to a new comer (at least, in my opinion).

If you have comments and suggestions, feel free to let me know through the comments!

# Overview

## 2014

### Artificial Intelligence: A Modern Approach (2014-01)
Stuart Russell, Peter Norvig

Only reading the content without doing any exercises is about 60-65h of reading.

### Augmenting Human Intellect (2014-02)
Douglas Engelbart

### Playing Atari with Deep Reinforcement Learning (2014-02)
Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Alex Graves, Ioannis Antonoglou, Daan Wierstra, Martin Riedmiller

### Genifer – an artificial general intelligence (2014-03 - ?)
YKY

### How to Create a Mind: The Secret of Human Thought Revealed
Ray Kurzweil

## 2015

### The Essential Turing (2015-06 - ?)
Alan M. Turing, B. Jack Copeland

* On Computable Numbers, with an Application to the Entscheidungsproblem (2015-06 - ?)
* Intelligent Machinery (2015-10)
* Computing Machinery and Intelligence (2015-10)
* Can Digital Computer Think? (2015-10)
* Solvable and Unsolvable Problems (2015-10)
* Systems of Logic Based on Ordinals (2016-01 - ?)

### The First Level of Super Mario Bros. is Easy with Lexicographic Orderings and Time Travel (2015-06)
Tom Murphy VII

### Naive set theory (2015-08 - ?)
Paul R. Halmos

### A Mathematical Theory of Communication (2015-08 - ?)
Claude E. Shannon

### A Model for Recursively Self Improving Programs (2015-09)
Matt Mahoney

### Universal Artificial Intelligence (2015-09 - ?)
Marcus Hutter

### A Collection of Definitions of Intelligence (2015-09)
Shane Legg

### Machine Super Intelligence (2015-09 - ?)
Shane Legg

### Gödel, Escher, Bach: an Eternal Golden Braid (2015-09 - ?)
Douglas R. Hofstadter

### The Society of Mind (2015-11 - 2016-02)
Marvin Minsky

## 2016

* Tensorflow 2016-01

### PHP-Brain (2016-02 - ?)
See [PHP-Brain](../php-brain)

For about two weeks, I spent my time trying to find ways to do efficient string matching and document learning. The reason I wanted to do this was to attempt to learn language through examples. Provided with enough (hopefully valid) documents, it would be possible to assess if a given sentence is valid by matching it with previously seen sentences. It would also allow me to feed it a bunch of my chatlogs so that it may learn my vocabulary behavior and potentially predict what I would type next (basically autocompletion).

With a program that could do not much more than receive texts and match them against previously seen documents, I wanted to figure out a way to match generic data instead of words/sentences.

However, it wasn't only about matching generic data. It was also about being able to match data of different types with one another. In other words, if an image contained a sentence within one of its region, I'd like to be able to reuse that region to store the sentence as well as this region of the image. Thus, using only one run of the data I have two different informations: a sentence and a part of an image.

Furthermore, the idea is also to be able to relate concepts of varying degree of abstraction with one another.

In other to get an idea of how this could be accomplished, I started to reflect on the architecture of the human body and how the brain processes signal/information.

I began by designing a model-based brain, in other words, something that would look like a brain but from the inside would be something different. The main idea was to have a loop that would run forever, which would select tasks to execute. Input from the environment as well as actions to undertake (output) were considered to be tasks. The brain would have to process an input task, which would consist of a stream of data to be parsed and looked for patterns. An output task would be the emission of a stream of data (a stored pattern we expect to produce the desired result) to a target actuator. In other words, the brain would have to learn how to use its outputs through pattern emission, like it would try to learn to decipher the input streams it would receive.

After playing with the idea for a while, I came across an issue: what should I do when a task may take several seconds, even maybe minutes or hours? It doesn't make sense to stop processing everything else until said task is complete. That is not a real time approach. Thus, it meant we'd have to implement some sort of system to do task preemption. PHP being a single threaded language, this would prove to be more complicated than I wanted to deal with. Thus, I decided to move to a language that would support multithreading, C#.

### Sharp-Brain (2016-03 - ?)

The first thing I did when moving to C# was to build a complete body in an object oriented fashion. Body, head, brain, eyes, ears, nerves and so on. The head had eyes, which were attached to their own optic nerve, which would then connect to the brain. The brain was connected to a set of nerves, such as the optic nerve, which could be used either to receive or transmit data/signal.

Since I was now using a multithreaded language, I made each input a thread of its own. Thus, there would be 2 threads for the eyes, one per eye, 2 threads for the ears, one per ear, a thread for the brain, and so on. This would be the model of a human.

However, it was possible to generalize the idea to a robot. If we replaced the eyes with a single webcam, then the architecture would be similar in the sense that the eye, now a webcam, would take a frame and transmit it over the optic nerve to the brain. The brain would receive this array of bytes and process it (whatever that would mean, at this point no processing was done within the brain other than receive the data).

The problem at this point though was that the brain would now build its own network of understanding/patterns, which would make it more opaque and difficult to understand compared to a system of tasks.

### Artificial General Intelligence (2016-02 - ?)
Ben Goertzel, Cassio Pennachin

### The Logic of Intelligence (2016-02)
Pei Wang

### The Novamente Artificial Intelligence Engine (2016-02)
Ben Goertzel

### Essentials of General Intelligence: The Direct Path to Artificial General Intelligence (2016-03)
Peter Voss

### Artificial Brains (2016-03)
Hugo de Garis

### The OpenNARS implementation of the Non-Axiomatic Reasoning System (2016-03)
Patrick Hammer, Tony Lofthouse, Pei Wang

### The New AI: General & Sound & Relevant for Physics (2016-03)
Jürgen Schmidhuber

### Gödel Machines: Fully Self-Referential Optimal Universal Self-improvers (2016-03)
Jürgen Schmidhuber

### Playing Atari with Deep Reinforcement Learning (2016-03)
Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Alex Graves, Ioannis Antonoglou, Daan Wierstra, Martin Riedmiller

### Mastering the Game of Go with Deep Neural Networks and Tree Search (2016-03)
David Silver, Aja Huang, Chris J. Maddison, Arthur Guez, Laurent Sifre, George van den Driessche, Julian Schrittwieser, Ioannis Antonoglou, Veda Panneershelvam, Marc Lanctot, Sander Dieleman, Dominik Grewe, John Nham, Nal Kalchbrenner, Ilya Sutskever, Timothy Lillicrap, Madeleine Leach, Koray Kavukcuoglu, Thore Graepel & Demis Hassabis

### Program Search as a Path to Artificial General Intelligence (2016-03)
Łukasz Kaiser

### The Natural Way to Artificial Intelligence (2016-04)
Vladimir G. Red'ko

### Neural Turing Machines (2016-04)
Alex Graves, Greg Wayne, Ivo Danihelka

### 3D Simulation: the Key to A.I. (2016-04)
Keith A. Hoyes

### Cognitive Science - An Introduction to the Science of the Mind (2016-04 - ?)
José Luis Bermúdez

### Building Machines That Learn and Think Like People (2016-04 - ?)
Breden Lake

### EURISKO: A Program That Learns New Heuristics and Domain Concepts (2016-04)
Douglas Lenat

### A Mathematical Theory of Communication (2016-04 - ?)
Claude Shannon

## In the reading queue

### Design for a brain
William Ross Ashby

### A Method for the Construction of Minimum-Redundancy Codes
David A. Huffman

### Introduction to mathematical logic
Elliott Mendelson

### Artificial general intelligence through recursive data compression and grounded reasoning: a position paper
Arthur Franz

### Hierarchical Temporal Memory
Numenta
