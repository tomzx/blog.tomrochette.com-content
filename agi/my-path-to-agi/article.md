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

If you are interested in a more digestible path through the same content I've experienced, I suggest you look up [my suggested path to AGI](../my-suggested-path-to-agi/article.md) article. It basically contains most of the stuff I've gone through myself, but it is organized in a constructive manner to a new comer (at least, in my opinion).

If you have comments and suggestions, feel free to let me know through the comments!

Note: The dates in parenthesis indicate when I started and finished reading a given book/paper, not their publication date.

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

### How to Create a Mind: The Secret of Human Thought Revealed (2014-03)
Ray Kurzweil

### Coursera - Machine Learning (2014-03)
Andrew Ng

## 2015

### The Essential Turing (2015-06 - ?)
Alan M. Turing, B. Jack Copeland

* On Computable Numbers, with an Application to the Entscheidungsproblem (2015-06 - ?)
* Intelligent Machinery (2015-10)
* Computing Machinery and Intelligence (2015-10)
* Can Digital Computer Think? (2015-10)
* Solvable and Unsolvable Problems (2015-10)
* Systems of Logic Based on Ordinals (2016-01 - ?)
* Can Automatic Calculating Machines Be Said to Think?
* Lecture on the Automated Computing Engine
* The Chemical Basis of Morphogenesis
* Chess

### The First Level of Super Mario Bros. is Easy with Lexicographic Orderings and Time Travel (2015-06)
Tom Murphy VII

### Naive set theory (2015-08 - ?)
Paul R. Halmos

### A Mathematical Theory of Communication (2015-08 - 2016-05)
Claude E. Shannon

### A Model for Recursively Self Improving Programs (2015-09)
Matt Mahoney

### Universal Artificial Intelligence (2015-09 - ?)
Marcus Hutter

### A Collection of Definitions of Intelligence (2015-09)
Shane Legg

### Gödel, Escher, Bach: an Eternal Golden Braid (2015-09 - ?)
Douglas R. Hofstadter

### The Society of Mind (2015-11 - 2016-02)
Marvin Minsky

### The Computer and the Brain (2015-12)
John von Neumann

## 2016

* Tensorflow 2016-01

### PHP-Brain (2016-02 - ?)
See [PHP-Brain](../prototypes/php-brain/article.md)

For about two weeks, I spent my time trying to find ways to do efficient string matching and document learning. The reason I wanted to do this was to attempt to learn language through examples. Provided with enough (hopefully valid) documents, it would be possible to assess if a given sentence is valid by matching it with previously seen sentences. It would also allow me to feed it a bunch of my chatlogs so that it may learn my vocabulary behavior and potentially predict what I would type next (basically autocompletion).

With a program that could do not much more than receive texts and match them against previously seen documents, I wanted to figure out a way to match generic data instead of words/sentences.

However, it wasn't only about matching generic data. It was also about being able to match data of different types with one another. In other words, if an image contained a sentence within one of its region, I'd like to be able to reuse that region to store the sentence as well as this region of the image. Thus, using only one run of the data I have two different informations: a sentence and a part of an image.

Furthermore, the idea is also to be able to relate concepts of varying degree of abstraction with one another.

In other to get an idea of how this could be accomplished, I started to reflect on the architecture of the human body and how the brain processes signal/information.

I began by designing a model-based brain, in other words, something that would look like a brain but from the inside would be something different. The main idea was to have a loop that would run forever, which would select tasks to execute. Input from the environment as well as actions to undertake (output) were considered to be tasks. The brain would have to process an input task, which would consist of a stream of data to be parsed and looked for patterns. An output task would be the emission of a stream of data (a stored pattern we expect to produce the desired result) to a target actuator. In other words, the brain would have to learn how to use its outputs through pattern emission, like it would try to learn to decipher the input streams it would receive.

After playing with the idea for a while, I came across an issue: what should I do when a task may take several seconds, even maybe minutes or hours? It doesn't make sense to stop processing everything else until said task is complete. That is not a real time approach. Thus, it meant we'd have to implement some sort of system to do task preemption. PHP being a single threaded language, this would prove to be more complicated than I wanted to deal with. Thus, I decided to move to a language that would support multithreading, C#.

### Sharp-Brain (2016-03 - ?)
See [Sharp-Brain](../prototypes/php-brain/article.md)

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
David Silver, Aja Huang, Chris J. Maddison, Arthur Guez, Laurent Sifre, George van den Driessche, Julian Schrittwieser, Ioannis Antonoglou, Veda Panneershelvam, Marc Lanctot, Sander Dieleman, Dominik Grewe, John Nham, Nal Kalchbrenner, Ilya Sutskever, Timothy Lillicrap, Madeleine Leach, Koray Kavukcuoglu, Thore Graepel, Demis Hassabis

### Program Search as a Path to Artificial General Intelligence (2016-03)
Łukasz Kaiser

### The Natural Way to Artificial Intelligence (2016-04)
Vladimir G. Red'ko

### Neural Turing Machines (2016-04)
Alex Graves, Greg Wayne, Ivo Danihelka

### 3D Simulation: the Key to A.I. (2016-04)
Keith A. Hoyes

### Cognitive Science - An Introduction to the Science of the Mind (2016-04 - 2016-07)
José Luis Bermúdez

### Building Machines That Learn and Think Like People (2016-04 - 2016-08)
Breden Lake

### EURISKO: A Program That Learns New Heuristics and Domain Concepts (2016-04)
Douglas Lenat

### Why AM and Eurisko Appear to Work (2016-05)
Douglas Lenat

### AM: An Artificial Intelligence Approach to Discovery in Mathematics as Heuristic Search (2016-05 - 2016-06)
Douglas Lenat

### Discovery Systems: From AM to CYRANO (2016-05)
Ken Haase

### AM: A Case Study in AI Methodology (2016-05)
G.D. Ritchie, F.K. Hanna

### Report on a General Problem-Solving Program (2016-05)
Allen Newell, John Clifford Shaw, Herbert A. Simon

### The Logic Theory Machine: A Complex Information Processing System (2016-05)
Allen Newell, Herbert A. Simon

### The Copycat Project: A Model of Mental Fluidity and Analogy-Making (2016-05 - ?)
Douglas Hofstadter, Melanie Mitchell

### Minds, Machines and Gödel (2016-05)
J.R. Lucas

### Automated programming (2016-06 - ?)
Began research related to automated programming. The main goal is to determine what is doable at the moment (based on current knowledge of the field).

### Automated refactoring (2016-06 - ?)
Began research related to automated refactoring. The main goal is to determine a list of refactoring tools that can be developed to simplify the job of refactoring of programmers.

### Approaches to Automatic Programming (2016-06)
Alan Biermann

### Duplicated Code Refactoring Advisor (DCRA) (2016-06)
Francesco Zanoni

### How to Solve It: A New Aspect of Mathematical Method (2016-06 - ?)
George Pólya

### The heuristic of George Polya and its relation to artificial intelligence (2016-06)
Allen Newell

### Neuroscience: Exploring the Brain (2016-06 - 2016-11)
Mark F. Bear, Barry W. Connors, Michael A. Paradiso

### A Concise Introduction to Logic (2016-06 - 2016-12)
Patrick J. Hurley

### A Hypothetical Dialogue Exhibiting a Knowledge Base For a Program-Understanding System (2016-06 - 2016-07)
Cordell Green, David Barstow

### Machine Learning (2016-06 - (2016-09))
Peter Flach

### On Intelligence (2016-06 - 2016-08)
Jeff Hawkins

### Programs with common sense (2016-06)
John McCarthy

### Universal Value Function Approximators (2016-06 - 2016-07)
Tom Schaul, Dan Horgan, Karol Gregor, David Silver

### The Programmer's Apprentice: A Research Overview (2016-07)
Charles Rich, Richard C. Waters

### Towards a Programming Apprentice (2016-07)
Carl E. Hewitt, Brian Smith

### Artificial Intelligence -- a personal view (2016-07)
David Marr

### Automated research (2016-08 - ?)
Began research related to automated research. The main goal is to determine a basic research flow and automate most of the process (researching papers, establishing important papers, determine a reading order, create a wordcloud of the most important terms, define which papers cite which papers, etc.).

### Introduction to Automata Theory, Languages, and Computation (2016-08 - 2016-10)
 John E. Hopcroft, Rajeev Motwani, Jeffrey D. Ullman

### Theory of self-reproducing automata (2016-08 - 2016-10)
John von Neumann

### From Seed AI to Technological Singularity via Recursively Self-Improving Software (2016-08)
Roman V. Yampolskiy

### Self-improving AI: an Analysis (2016-08)
John Storrs Hall

### Engineering Utopia (2016-08)
John Storrs Hall

### Toward a Standard Metric of Machine Intelligence (2016-08)
Richard Yonck

### From the Phenomenology to the Mechanisms of Consciousness: Integrated Information Theory 3.0 (2016-08)
Masafumi Oizumi, Larissa Albantakis, Giulio Tononi

### Automatic Learning of Context-Free Grammar (2016-08)
Tai-Hung Chen, Chun-Han Tseng, Chia-Ping Chen

### TensorFlow for Machine Intelligence (2016-09)
Sam Abrahams, Danijar Hafner, Erik Erwitt, Ariel Scarpinelli

### Language Identification in the Limit (2016-09)
E. Mark Gold

### How to Invent Functions (2016-09)
J. Roland Olsson

### Can Intelligence Explode? (2016-09)
Marcus Hutter

### A Complete Theory of Everything (will be subjective) (2016-09)
Marcus Hutter

### Automated test generator (2016-09 - ?)
Began research related to automated test generator. The main goal of this project is to use the knowledge I've acquired thinking about automated programming and refactoring and attempt to apply it to test generation. One of the goals is to develop a tool which will automate most of the process of testing PHP OOP code, specifically MVC-oriented websites using frameworks such as Laravel or Symfony.

### Static analysis (2016-09 - ?)
My research into static analysis is related to my research on automated programming, automated refactoring and automated test generator. The main goal is to produce a piece of software that will be able to reason as a programmer would reason about a program in his head.

### Automating Software Testing Using Program Analysis (2016-10)
Patrice Godefroid, Peli de Halleux, Aditya Nori, Sriram Rajamani, Wolfram Schulte, Nikolai Tillmann, Michael Y. Levin

### Software Testing: A Craftsman's Approach (2016-10 - 2016-11)
Paul Jorgensen

### Advanced Symbolic Analysis for Compilers (2016-10 - 2016-11)
Thomas Fahringer, Bernhard Scholz

### Principles of Program Analysis (2016-10 - 2016-12)
Flemming Nielson, Hanne R. Nielson, Chris Hankin

## 2017

### Programming the Semantic Web (2017-01)
Toby Segaran, Colin Evans, Jamie Taylor

### Deep Learning (2017-02 - 2017-05)
Ian Goodfellow, Yoshua Bengio, Aaron Courville

### Reinforcement Learning (2017-02 - 2017-03)
David Silver

### A Framework for Searching for General Artificial Intelligence (2017-02)
Marek Rosa, Jan Feyereisl, The GoodAI Collective

### Knowledge base (2017-02)
I wrote a polymer/javascript-based application which dealt with triples in order to manage knowledge. Everything is considered to be a node and nodes can be associated to one another through anonymous.

See [Knowledge base](../knowledge-base/article.md).

### Curriculum Learning (2017-04)
Yoshua Bengio, Jérôme Louradour, Ronan Collobert, Jason Weston

### A Postulate on the Brain's Basic Wiring Logic (2017-04)
Joe Z. Tsien

### Brain Computation Is Organized via Power-of-Two-Based Permutation Logic (2017-04)
Kun Xie, Grace E. Fox, Jun Liu, Cheng Lyu, Jason C. Lee, Hui Kuang, Stephanie Jacobs, Meng Li, Tianming Liu, Sen Song, Joe Z. Tsien

### How to Make a Complete Map of Every Thought (2017-04)
Lion Kimbro

### Induction of Decision Trees (2017-04)
J.R. Quinlan

### Handwriting recognition (2017-04 - ?)
Began experimenting with the problem of handwriting recognition. The main goal is to be able to feed a page through a camera/webcam/scanner and have its text content extracted.

### Traitement automatique des langues (2017-04)
Hugo Larochelle

### RobustFill: Neural Program Learning under Noisy I/O (2017-04)
Jacob Devlin, Jonathan Uesato, Surya Bhupatiraju, Rishabh Singh, Abdel-rahman Mohamed, Pushmeet Kohli

### Generative Adversarial Nets (2017-04)
Ian J. Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville, Yoshua Bengio

### Offline Handwriting Recognition with Multidimensional Recurrent Neural Networks (2017-04)
Alex Graves, Jürgen Schmidhuber

### Auto-Encoding Variational Bayes (2017-04)
Diederik P. Kingma, Max Welling

### Tacotron: Towards End-To-End Speech Synthesis (2017-05)
Yuxuan Wang, RJ Skerry-Ryan, Daisy Stanton, Yonghui Wu, Ron J. Weiss, Navdeep Jaitly, Zongheng Yang, Ying Xiao, Zhifeng Chen, Samy Bengio, Quoc Le, Yannis Agiomyrgiannakis, Rob Clark, Rif A. Saurous

### DeepZip: Lossless Compression using Recurrent Networks (2017-05)
Kedar Tatwawadi

### Scan, Attend and Read: End-to-End Handwritten Paragraph Recognition with MDLSTM Attention (2017-05)
Théodore Bluche, Jérôme Louradour, Ronaldo Messina

### Neural machine translation by jointly learning to align and translate (2017-05)
Dzmitry Bahdanau, Kyunghyun Cho, Yoshua Bengio

### Deepcoder: Learning to Write Programs (2017-05)
Matej Balog, Alexander L. Gaunt, Marc Brockschmidt, Sebastian Nowozin, Daniel Tarlow

### Neural Architecture Search With Reinforcement Learning (2017-05)
Barret Zoph, Quoc V. Le

### SMARTPASTE: Learning to Adapt Source Code (2017-05)
Miltiadis Allamanis, Marc Brockschmidt

### Third-Person Imitation Learning (2017-05)
Bradly C. Stadie, Pieter Abbeel, Ilya Sutskever

### Elements of Information Theory (2017-05 - (2017-07))
Thomas M. Cover, Joy A. Thomas

### Deep Voice: Real-time Neural Text-to-Speech (2017-06)
Sercan O. Arik, Mike Chrzanowski, Adam Coates, Gregory Diamos, Andrew Gibiansky, Yongguo Kang, Xian Li, John Miller, Andrew Ng, Jonathan Raiman, Shubho Sengupta, Mohammad Shoeybi

### Deep Voice 2: Multi-Speaker Neural Text-to-Speech (2017-06)
Sercan Arik, Gregory Diamos, Andrew Gibiansky, John Miller, Kainan Peng, Wei Ping, Jonathan Raiman, Yanqi Zhou

### Toward an Architecture for Never-Ending Language Learning (2017-06)
Andrew Carlson, Justin Betteridge, Bryan Kisiel, Burr Settles, Estevam R. Hruschka, Tom M. Mitchell

### Human-level control through deep reinforcement learning (2017-06)
Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Andrei A. Rusu, Joel Veness, Marc G. Bellemare, Alex Graves, Martin A. Riedmiller, Andreas Fidjeland, Georg Ostrovski, Stig Petersen, Charles Beattie, Amir Sadik, Ioannis Antonoglou, Helen King, Dharshan Kumaran, Daan Wierstra, Shane Legg, Demis Hassabis

### SophoLab; experimental computational philosophy (2017-06 - (2017-07))
Vicent Wiegel

### Multi-Dimensional Recurrent Neural Networks (2017-06)
Alex Graves, Santiago Fernandez, Juergen Schmidhuber

### Grid Long Short-Term Memory (2017-06)
Nal Kalchbrenner, Ivo Danihelka, Alex Graves

### One Model To Learn Them All (2017-06)
Lukasz Kaiser, Aidan N. Gomez, Noam Shazeer, Ashish Vaswani, Niki Parmar, Llion Jones, Jakob Uszkoreit

### Schema Networks: Zero-shot Transfer with a Generative Causal Model of Intuitive Physics (2017-06)
Ken Kansky, Tom Silver, David A. Mély, Mohamed Eldawy, Miguel Lázaro-Gredilla, Xinghua Lou, Nimrod Dorfman, Szymon Sidor, Scott Phoenix, Dileep George

### The Predictron: End-To-End Learning and Planning (2017-06)
David Silver, Hado van Hasselt, Matteo Hessel, Tom Schaul, Arthur Guez, Tim Harley, Gabriel Dulac-Arnold, David Reichert, Neil Rabinowitz, André Barreto, Thomas Degris

### Automated Curriculum Learning for Neural Networks (2017-06)
Alex Graves, Marc G. Bellemare, Jacob Menick, Rémi Munos, Koray Kavukcuoglu

### The Strategic Student Approach for Life-Long Exploration and Learning (2017-06)
Manuel Lopes, Pierre-Yves Oudeyer

### Attention Is All You Need (2017-07)
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia

### Show, Attend and Tell: Neural Image Caption Generation with Visual Attention (2017-07)
Kelvin Xu, Jimmy Ba, Ryan Kiros, Kyunghyun Cho, Aaron C. Courville, Ruslan Salakhutdinov, Richard S. Zemel, Yoshua Bengio

### Deep Reinforcement Learning from Human Preferences (2017-07)
Paul F. Christiano, Jan Leike, Tom Brown, Miljan Martic, Shane Legg, Dario Amodei

### The Master Algorithm: How the Quest for the Ultimate Learning Machine Will Remake Our World (2017-07 - 2017-08)
Pedro Domingos

### Algorithms to Live By: The Computer Science of Human Decisions (2017-07 - 2017-08)
Brian Christian, Tom Griffiths

### Programmable Agents (2017-08)
Misha Denil, Sergio Gomez Colmenarejo, Serkan Cabi, David Saxton, Nando de Freitas

### Principles of Computational Modelling in Neuroscience (2017-07 - (2017-08))
David Sterratt, Bruce Graham, Andrew Gillies, David Willshaw

### How to Build a Brain: A Neural Architecture for Biological Cognition (2017-08 - ?)
Chris Eliasmith

### Why Philosophers Should Care About Computational Complexity (2017-08 - 2017-09)
Scott Aaronson

### Superintelligence: Paths, Dangers, Strategies (2017-08 - 2017-11)
Nick Bostrom

### The Brain: The Story of You (2017-08 - 2017-09)
David Eagleman

### The Consciousness Prior (2017-09)
Yoshua Bengio

### Learning with Opponent-Learning Awareness (2017-09)
Jakob N. Foerster, Richard Y. Chen, Maruan Al-Shedivat, Shimon Whiteson, Pieter Abbeel, Igor Mordatch

### StarCraft II: A New Challenge for Reinforcement Learning (2017-09)
Oriol Vinyals, Timo Ewalds, Sergey Bartunov, Petko Georgiev, Alexander Sasha Vezhnevets, Michelle Yeo, Alireza Makhzani, Heinrich Küttler, John Agapiou, Julian Schrittwieser, John Quan, Stephen Gaffney, Stig Petersen, Karen Simonyan, Tom Schaul, Hado van Hasselt, David Silver, Timothy P. Lillicrap, Kevin Calderone, Paul Keet, Anthony Brunasso, David Lawrence, Anders Ekermo, Jacob Repp, Rodney Tsing

### Is the theory of everything merely the ultimate ensemble theory? (2017-09)
Max Tegmark

### The Allure of Machinic Life: Cybernetics, Artificial Life, and the New AI (2017-10 - ?)
John Johnston

### Developmental Biology (2017-10 - ?)
Scott Gilbert

### Mastering the game of Go without human knowledge (2017-10)
David Silver, Julian Schrittwieser, Karen Simonyan, Ioannis Antonoglou, Aja Huang, Arthur Guez, Thomas Hubert, Lucas R Baker, Matthew Lai, Adrian Bolton, Yutian Chen, Timothy P. Lillicrap, Fan Xin Hui, Laurent Sifre, George van den Driessche, Thore Graepel, Demis Hassabis

### Fast and Slow with Deep Learning and Tree Search (2017-10)
Thomas Anthony, Zheng Tian, David Barber

### Rainbow: Combining Improvements in Deep Reinforcement Learning (2017-11)
Matteo Hessel, Joseph Modayil, Hado van Hasselt, Tom Schaul, Georg Ostrovski, Will Dabney, Daniel Horgan, Bilal Piot, Mohammad Gheshlaghi Azar, David Silver

### Reverse Curriculum Generation for Reinforcement Learning (2017-11)
Carlos Florensa, David Held, Markus Wulfmeier, Pieter Abbeel

### The Consciousness Prior (2017-12)
Yoshua Bengio

### Deep Voice 3: 2000-Speaker Neural Text-to-Speech (2017-12)
Wei Ping, Kainan Peng, Andrew Gibiansky, Sercan Ömer Arik, Ajay Kannan, Sharan Narang, Jonathan Raiman, John Miller

### Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm (2017-12)
David Silver, Thomas Hubert, Julian Schrittwieser, Ioannis Antonoglou, Matthew Lai, Arthur Guez, Marc Lanctot, Laurent Sifre, Dharshan Kumaran, Thore Graepel, Timothy Lillicrap, Karen Simonyan, Demis Hassabis

### Bandit Based Monte-Carlo Planning (2017-12)
Levente Kocsis, Csaba Szepesvári

### R-MAX - A General Polynomial Time Algorithm for Near-Optimal Reinforcement Learning (2017-12)
Ronen I. Brafman, Moshe Tennenholtz

### Life 3.0: Being Human in the Age of Artificial Intelligence (2017-12 - 2018-02)
Max Tegmark

## 2018

### Speculations concerning the first ultraintelligent machine (2018-01)
Irving John Good

### A Decision-Theoretic Generalization of On-Line Learning and an Application to Boosting (2018-01)
Yoav Freund, Robert E. Schapire

### Voice detection (2017-09 - 2018-01)
I have recorded a ton of audio of myself while I use my computer at home. I wanted to be able to find the slices of time where I speak and say something intelligible in order to extract those regions and then potentially send them to a service such as Google Voice to have it converted into text.

### A Trainable Spaced Repetition Model for Language Learning (2018-02)
Burr Settles, Brendan Meeder

### When will computer hardware match the human brain? (2018-02)
Hans Moravec

### Machine Super Intelligence (2015-09 - 2018-02)
Shane Legg

### The free-energy principle: a unified brain theory? (2018-02)
Karl Friston

### Precise Condition Synthesis for Program Repair (2018-02)
Yingfei Xiong, Jie Wang, Runfa Yan, Jiachen Zhang, Shi Han, Gang Huang, Lu Zhang

### Intrinsically Motivated Learning of Hierarchical Collections of Skills (2018-02)
Satinder P. Singh, Andrew G. Barto, Nuttapong Chentanez

### History Driven Program Repair (2018-02)
Xuan-Bach D. Le, David Lo, Claire Le Goues

### Machine Theory of Mind (2018-02)
Neil C. Rabinowitz, Frank Perbet, H. Francis Song, Chiyuan Zhang, S. M. Ali Eslami, Matthew M Botvinick

### One Big Net For Everything (2018-05 - ?)
Jurgen Schmidhuber

### PowerPlay: training an increasingly general problem solver by continually searching for the simplest still unsolvable problem (2018-05 - ?)
Jurgen Schmidhuber
