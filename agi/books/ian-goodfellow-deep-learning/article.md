---
title: Ian Goodfellow - Deep Learning - 2016
created: 2017-01-01
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

$\usepackage{amsmath}$

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

## 2 Linear Algebra
~

## 3 Probability and Information Theory
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

### Information theory
* The basic intuition behind information theory is that learning that an unlikely event has occurred is more informative than learning that a likely event has occurred
* The self-information of an event $\text{x} = x$ is
$$
I(x) = -\log P(x)
$$
* We can quantify the amount of uncertainty in an entire probability distribution using the Shannon entropy:
$$
H(\text{x}) = \mathbb{E}_{\text{x} \sim P}[I(x)] = - \mathbb{E}_{\text{x} \sim P}[\log P(x)]
$$

## 4 Numerical Computation
* Ascending an objective function of *discrete* parameters is called hill climbing
* A Lipschitz continuous function is a function f whose rate of change is bounded by a Lipschitz constant $\mathcal{L}$
$$
\forall \boldsymbol{x}, \forall \boldsymbol{y}, |f(\boldsymbol{x}) - f(\boldsymbol{y})| \le \mathcal{L}||\boldsymbol{x}-\boldsymbol{y}||_2
$$
* This property is useful because it allows us to quantify our assumption that a small change in the input made by an algorithm such as gradient descent will have a small change in the output

## 5 Machine Learning Basics
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
* Bias and variance measure two different sources of error in an estimator
	* Bias measures the expected deviation from the true value of the function or parameter
	* Variance provides a measure of the deviation from the expected estimator value that any particular sampling of the data is likely to cause

### 5.5.2 Properties of Maximum Likelihood
* Under appropriate conditions, the maximum likelihood estimator has the property of consistency, meaning that as the number of training examples approaches infinity, the maximum likelihood estimate of a parameter converges to the true value of the parameter. These conditions are:
	* The true distribution $p_{data}$ must lie within the model family $p_{model}(\cdot; \boldsymbol{\theta})$. Otherwise, no estimator can recover $p_{data}$
	* The true distribution $p_{data}$ must correspond to exactly one value of $\boldsymbol{\theta}$. Otherwise, maximum likelihood can recover the correct $p_{data}$, but will not be able to determine which value of $\boldsymbol{\theta}$ was used by the data generating process
* Consistent estimators can differ in their statistic efficiency, meaning that one consistent estimator may obtain lower generalization error for a fixed number of samples m, or equivalently, may require fewer examples to obtain a fixed level of generalization error
* When the number of examples is small enough to yield overfitting behavior, regularization strategies such as weight decay may be used to obtain a biased version of maximum likelihood that has less variance when training data is limited

### 5.7.2 Support Vector Machines
* Support Vector Machines (SVM) is similar to logistic regression in that it is driven by a linear function $\boldsymbol{w^\top x} + b$
* One key innovation associated with SVM is the kernel trick
	* The kernel trick consists of observing that many machine learning algorithms can be written exclusively in terms of dot products between examples
* The kernel-based function is exactly equivalent to preprocessing the data by applying $\phi(\boldsymbol{x})$ to all inputs, then learning a linear model in the new transformed space
* The kernel trick is powerful for two reasons:
	* It allows us to learn models that are nonlinear as a function of $\boldsymbol{x}$ using convex optimization techniques that are guaranteed to converge efficiently
	* The kernel function k often admits an implementation that is significantly more computationally efficient than naively constructing two $\phi(\boldsymbol{x})$ vectors and explicitly taking their dot products
* The most commonly used kernel is the Gaussian kernel, also known as the radial basis function (RBF) kernel
* A major drawback to kernel machines is that the cost of evaluating the decision function is linear in the number of training examples, because the i-th example contributes a term to the decision function
	* SVM are able to mitigate this by learning an $\boldsymbol{\alpha}$ vector that contains mostly zeros

### 5.7.3 Other Simple Supervised Learning Algorithms
* k-nearest neighbors is a family of techniques that can be used for classification or regression
* One weakness of k-nearest neighbors is that it cannot learn that one feature is more discriminative than another
* Decision trees as they are typically used, with axis-aligned splits and constant outputs within each node, struggle to solve some problems that are easy even for logistic regression (e.g., a two class problem where $x_2 > x_1$, the decision boundary is not axis-aligned and the decision tree will thus need to approximate the decision boundary with many nodes, implementing a step function that constantly walks back and forth across the true decision function with axis-aligned steps)

### 5.8 Unsupervised Learning Algorithms
* There are multiple ways of defining a simpler representation
	* Lower dimensional representations: attempt to compress as much information about x as possible in a smaller representation
	* Sparse representations: embed the dataset into a representation whose entries are mostly zeroes for most inputs
	* Independent representations: attempt to disentangle the sources of variation underlying the data distribution such that the dimensions of the representation are statistically independent

### 5.8.1 Principal Components Analysis
* PCA learns a representation that has lower dimensionality than the original input
* It also learns a representation whose elements have no linear correlation with each other
* The k-means algorithm works by initializing k different centroids to different values, then alternating between two different steps until convergence
	* In one step, each training example is assigned to cluster i, where i is the index of the nearest centroid $\boldsymbol{\mu}^{(i)}$
	* In the other step, each centroid $\boldsymbol{\mu}^{(i)}$ is updated to the mean of all training examples $\boldsymbol{x}^{(j)}$ assigned to cluster i
* Clustering may end up generating different clusters because of the feature that are used to create the clusters (red cars/trucks vs gray cars/trucks, red/gray cars vs red/gray trucks)

### 5.8.2 k-means Clustering
* The k-means clustering algorithm divides the training set into k different clusters of examples that are near each other

### 5.9 Stochastic Gradient Descent
* The insight to stochastic gradient descent is that the gradient is an expectation. The expectation may be approximately estimated using a small set of samples

### 5.10 Building a Machine Learning Algorithm
* Nearly all deep learning algorithms can be described as a particular instance of a fairly simple recipe:
	* a specification of a dataset
	* a cost function
	* an optimization procedure
	* a model

### 5.11 Challenges Motivating Deep Learning
### 5.11.2 Local Constancy and Smoothness Regularization
* The core idea in deep learning is that we assume that the data was generated by the composition of factors or features, potentially at multiple levels in a hierarchy

### 5.11.3 Manifold Learning
* Manifold learning algorithms assume that most of $\mathbb{R}^n$ consists of invalid inputs, and that interesting inputs occur only along a collection of manifolds containing a small subset of points, which interesting variations in the output of the learned function occurring only along directions that lie on the manifold, or with interesting variations happening only when we move from one manifold to another
* Observations in favor of the manifold hypothesis
	* The probability distribution over images, text strings, and sounds that occur in real life is highly concentrated
	* We can imagine neighborhoods and transformations of the manifold

## 6 Deep Feedforward Networks
* It is best to think of feedforward networks as function approximation machines that are designed to achieve statistical generalization
* The general principle of improving models by learning features extends beyond the feedforward networks. It is a recurring theme of deep learning that applies to all kinds of models
* Multiple decisions
	* Activation functions
	* Network architecture
		* How many layers?
		* How the layers should be connected?
		* How many units should be in each layer?
* In modern neural networks, the default recommendation is to use the rectified linear unit (ReLU) defined by the activation function g(z) = max{0, z}

### 6.2 Gradient-Based Learning
* For feedforward neural networks, it is important to initialize all weights to small random values. The biases may be initialized to zero or to small positive values

### 6.2.1.1 Learning Conditional Distributions with Maximum Likelihood
* Most modern neural networks are trained using maximum likelihood

### 6.2.2 Output Units
* The choice of cost function is tightly coupled with the choice of output unit

### 6.2.2.3 Softmax Units for Multinoulli Output Distributions
* Objective functions that do not use a log to undo the exp of the softmax fail to learn when the argument to the exp becomes very negative, causing the gradient to vanish
* In particular, squared error is a poor loss function for softmax units, and can fail to train the model to change its output, even when the model makes highly confident incorrect predictions
* From a neuroscientific point of view, it is interesting to think of the softmax as a way to create a form of competition between the units that participate in it: the softmax outputs always sum to 1 so an increase in the value of one unit necessarily corresponds to a decrease in the value of others
* Softmax => soft argmax

### 6.3 Hidden Units
### 6.3.1 Rectified Linear Units and Their Generalizations
* $g(z) = max\{0, z\}$
* One drawback to rectified linear units is that they cannot learn via gradient-based methods on examples for which their activation is zero
* Three generalizations of rectified linear units are based on using a non-zero slope $\alpha_i$ when $z_i < 0$: $h_i = g(\boldsymbol{z}, \boldsymbol{\alpha})_i = \text{max}(0, z_i) + \alpha_i \text{min}(0, z_i)$
	* Absolute value rectification, $\alpha_i = -1$
	* Leaky ReLU, $\alpha_i \approx 0.01$
	* Parametric ReLU (PReLU), $\alpha_i$ as a learnable parameter

# See also

# References
* Goodfellow, Ian, Yoshua Bengio, and Aaron Courville. Deep learning. MIT Press, 2016.
* https://www.amazon.com/Deep-Learning-Adaptive-Computation-Machine/dp/0262035618