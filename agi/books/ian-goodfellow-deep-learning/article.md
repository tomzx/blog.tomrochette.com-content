---
title: Ian Goodfellow - Deep Learning - 2016
created: 2017-01-01
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview

# Notes
## 1 Introduction
* In the early days of artificial intelligence, the field rapidly tackled and solved problems that are intellectually difficult for human beings but relatively straightforward for computers - problems that can be described by a list of formal, mathematical rules
* The true challenge to artificial intelligence proved to be ... problems that we solve intuitively, that feel automatic, ...
* The book solution to this problem is to allow computers to learn from experience and understand the world in terms of a hierarchy of concepts, with each concept defined in terms of its relation to simpler concepts
* If we draw a graph showing how these concepts are built on top of each other, the graph is deep, with many layers
* Abstract and formal tasks that are among the most difficult mental undertakings for a human being are among the easiest for a computer
* One of the key challenges in artificial intelligence is how to get this informal knowledge into a computer
* The difficulties faced by systems relying on hard-coded knowledge suggest that AI systems need the ability to acquire their own knowledge, by extracting patterns from raw data (known as machine learning)
* The performance of (these) simple machine learning algorithms depends heavily on the representation of the data they are given
* Each piece of information included in the representation ... is known as a feature
* Many artificial intelligence tasks can be solved by designing the right set of features to extract for that task, then providing these features to a simple machine learning algorithm
* Representation learning: To discover not only the mapping from representation to output but also the representation itself
* Learned representation often result in much better performance than can be obtained with hand-designed representations
* An autoencoder is the combination of an encoder function that converts the input data into a different representation, and a decoder function that converts the new representation back into the original format
* When it is nearly as difficult to obtain a representation as to solve the original problem, representation learning does not, at first glance, seem to help us
* Deep learning solves this central problem in representation learning by introducing representations that are expressed in terms of other, simpler representations
* Deep learning allows the computer to build complex concepts out of simpler concepts
* Depth allows the computer to learn a multi-step computer program. Each layer of the representation can be thought of as the state of the computer's memory after executing another set of instructions in parallel
* Networks with greater depth can execute more instructions in sequence
* According to this view of deep learning, not all the information in a layer's activations necessarily encodes factors of variation that explain the input. The representation also stores state information that helps to execute a program that can make sense of the input
* Three waves of development of deep learning
	* 1940-1960 Cybernetics
	* 1980-1990 Connectionism
	* 2006-now Deep learning
* The neural perspective on deep learning is motivated by two main ideas:
	* The brain provides a proof by example that intelligent behavior is possible, and a conceptually straightforward path to building intelligence is to reverse engineer the computational principles behind the brain and duplicate its functionality
	* It would be deeply interesting to understand the brain and the principles that underlie human intelligence, so machine learning models that shed light on these basic scientific questions are useful apart from their ability to solve engineering applications
* Neuroscience has given us a reason to hope that a single deep learning algorithm can solve many different tasks
* We are able to draw some rough guidelines from neuroscience
	* The basic idea of having many computational units that become intelligent only via their interactions with each other is inspired by the brain
	* Greater neural realism has not yet led to an improvement in machine learning performance
	* We do not yet know enough about biological learning for neuroscience to offer much guidance for the learning algorithms we use to train neural network architectures
* One should not view deep learning as an attempt to simulate the brain
* The central idea in connectionism is that a large number of simple computational units can achieve intelligent behavior when networked together
* Distributed representation: Each input to a system should be represented by many features, and each feature should be involved in the representation of many possible inputs
* The amount of skill required (to get good performances from a deep learning algorithm) reduces as the amount of training data increases
* A rough rule of thumb is that a supervised deep learning algorithm will generally achieve acceptable performance with around 5000 labeled examples per category, and will match or exceed human performance when trained with a dataset containing at least 10 million labeled examples
* One of the main insights of connectionism is that animals become intelligent when their neurons work together
* Unless new technologies allow faster scaling, artificial neural networks will not have the same number of neurons as the human brain until at least 2050s

# 2 Linear Algebra
~

# 3 Probability and Information Theory
* There are three possible sources of uncertainty:
	* Inherent stochasticity in the system being modeled
	* Incomplete observability
	* Incomplete modeling
* The expectation or expected value of some function f(x) with respect to a probability distribution P(x) is the average or mean value that f takes on when x is drawn from P. For discrete variables this can be computed with a summation
$$
\mathbb{E}_{\text{x} \sim P}[f(x)] = \sum_x P(x)f(x)
$$
* For continuous variables, it is computed with an integral
$$
\mathbb{E}_{\text{x} \sim p}[f(x)] = \int p(x)f(x)\,dx
$$

## Information theory
* The basic intuition behind information theory is that learning that an unlikely event has occurred is more informative than learning that a likely event has occurred
* The self-information of an event $\text{x} = x$ is
$$
I(x) = -\log P(x)
$$
* We can quantify the amount of uncertainty in an entire probability distribution using the Shannon entropy:
$$
H(\text{x}) = \mathbb{E}_{\text{x} \sim P}[I(x)] = - \mathbb{E}_{\text{x} \sim P}[\log P(x)]
$$

# 4 Numerical Computation
* Ascending an objective function of *discrete* parameters is called hill climbing
* A Lipschitz continuous function is a function f whose rate of change is bounded by a Lipschitz constant $\mathcal{L}$
$$
\forall \textbf{x}, \forall \textbf{y}, |f(\textbf{x}) - f(\textbf{y})| \le \mathcal{L}||\textbf{x}-\textbf{y}||_2
$$
* This property is useful because it allows us to quantify our assumption that a small change in the input made by an algorithm such as gradient descent will have a small change in the output

# 5 Machine Learning Basics
* A computer is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E
* The process of learning itself is not the task
* Learning is our means of attaining the ability to perform the task
* Machine learning tasks are usually described in terms of how the machine learning system should process an example
* An example is a collection of features that have been quantitatively measured from some object or event that we want the machine learning system to process
* Common machine learning tasks:
	* Classification
	* Classification with missing inputs
	* Regression
	* Transcription
	* Machine translation
	* Structured output
	* Anomaly detection
	* Synthesis and sampling
	* Imputation of missing values
	* Denoising
	* Density estimation or probability mass function estimation
* Unsupervised learning involves observing several examples of a random vector $\textbf{x}$, and attempting to implicitly or explicitly learn the probability distribution $p(\textbf{x})$, or some interesting properties of that distribution, while supervised learning involves observing several examples of a random vector $\textbf{x}$ and an associated value or vector $\textbf{y}$, and learning to predict $\textbf{y}$ from $\textbf{x}$, usually by estimating $p(\textbf{y}\ |\ \textbf{x})$
* The ability to perform well on previously unobserved inputs is called generalization
* What separates machine learning from optimization is that we want the generalization error, also called the test error, to be low as well as the training error
* The generalization error is defined as the expected value of the error on a new input
* The i.i.d. assumptions
	* The example in each dataset are independent from each other
	* The training and test sets are identically distributed, that is, drawn from the same probability distribution
* Two central challenges in machine learning: underfitting and overfitting
	* Underfitting occurs when the model is not able to obtain a sufficiently low error value on the training set
	* Overfitting occurs when the gap between the training error and the test error is too large
* We can control whether a model is more likely to overfit or underfit by altering its capacity
* A model capacity is its ability to fit a wide variety of functions
* One way to control the capacity of a learning algorithm is by choosing its hypothesis space, the set of functions that the learning algorithm is allowed to select as being the solution
* Expected generalization error can never increase as the number of training examples increases
* (The no free lunch theorem) means that the goal of machine learning research is not to seek a universal learning algorithm or the absolute best learning algorithm. Instead, our goal is to understand what kinds of distributions are relevant to the "real world" that an AI agent experiences, and what kinds of machine learning algorithms perform well on data drawn from the kinds of data generating distributions we care about
* Regularization is any modification we make to a learning algorithm that is intended to reduce its generalization error but not its training error
* Training set:
	* 80% training examples
	* 20% validation examples (to optimize hyperparameters)
* k-fold cross-validation: a partition of the dataset is formed by spliting it into k non-overlapping subsets. The test error may then be estimated by taking the average test error across k trials
* We often estimate the generalization error by computing the sample mean of the error on the test set

# See also

# References
* Goodfellow, Ian, Yoshua Bengio, and Aaron Courville. Deep learning. MIT Press, 2016.
* https://www.amazon.com/Deep-Learning-Adaptive-Computation-Machine/dp/0262035618