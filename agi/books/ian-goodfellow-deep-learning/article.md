---
title: Ian Goodfellow - Deep Learning - 2016
created: 2017-01-01
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

$\usepackage{amsmath}$
$\newcommand{\vector}{\boldsymbol}$

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
\forall \vector{x}, \forall \vector{y}, |f(\vector{x}) - f(\vector{y})| \le \mathcal{L}||\vector{x}-\vector{y}||_2
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
* k-fold cross-validation: a partition of the dataset is formed by splitting it into k non-overlapping subsets. The test error may then be estimated by taking the average test error across k trials
* We often estimate the generalization error by computing the sample mean of the error on the test set
* Bias and variance measure two different sources of error in an estimator
 * Bias measures the expected deviation from the true value of the function or parameter
 * Variance provides a measure of the deviation from the expected estimator value that any particular sampling of the data is likely to cause

#### 5.5.2 Properties of Maximum Likelihood
* Under appropriate conditions, the maximum likelihood estimator has the property of consistency, meaning that as the number of training examples approaches infinity, the maximum likelihood estimate of a parameter converges to the true value of the parameter. These conditions are:
 * The true distribution $p_{data}$ must lie within the model family $p_{model}(\cdot; \vector{\theta})$. Otherwise, no estimator can recover $p_{data}$
 * The true distribution $p_{data}$ must correspond to exactly one value of $\vector{\theta}$. Otherwise, maximum likelihood can recover the correct $p_{data}$, but will not be able to determine which value of $\vector{\theta}$ was used by the data generating process
* Consistent estimators can differ in their statistic efficiency, meaning that one consistent estimator may obtain lower generalization error for a fixed number of samples m, or equivalently, may require fewer examples to obtain a fixed level of generalization error
* When the number of examples is small enough to yield overfitting behavior, regularization strategies such as weight decay may be used to obtain a biased version of maximum likelihood that has less variance when training data is limited

#### 5.7.2 Support Vector Machines
* Support Vector Machines (SVM) is similar to logistic regression in that it is driven by a linear function $\vector{w^\top x} + b$
* One key innovation associated with SVM is the kernel trick
 * The kernel trick consists of observing that many machine learning algorithms can be written exclusively in terms of dot products between examples
* The kernel-based function is exactly equivalent to preprocessing the data by applying $\phi(\vector{x})$ to all inputs, then learning a linear model in the new transformed space
* The kernel trick is powerful for two reasons:
 * It allows us to learn models that are nonlinear as a function of $\vector{x}$ using convex optimization techniques that are guaranteed to converge efficiently
 * The kernel function k often admits an implementation that is significantly more computationally efficient than naively constructing two $\phi(\vector{x})$ vectors and explicitly taking their dot products
* The most commonly used kernel is the Gaussian kernel, also known as the radial basis function (RBF) kernel
* A major drawback to kernel machines is that the cost of evaluating the decision function is linear in the number of training examples, because the i-th example contributes a term to the decision function
 * SVM are able to mitigate this by learning an $\vector{\alpha}$ vector that contains mostly zeros

#### 5.7.3 Other Simple Supervised Learning Algorithms
* k-nearest neighbors is a family of techniques that can be used for classification or regression
* One weakness of k-nearest neighbors is that it cannot learn that one feature is more discriminative than another
* Decision trees as they are typically used, with axis-aligned splits and constant outputs within each node, struggle to solve some problems that are easy even for logistic regression (e.g., a two class problem where $x_2 > x_1$, the decision boundary is not axis-aligned and the decision tree will thus need to approximate the decision boundary with many nodes, implementing a step function that constantly walks back and forth across the true decision function with axis-aligned steps)

### 5.8 Unsupervised Learning Algorithms
* There are multiple ways of defining a simpler representation
 * Lower dimensional representations: attempt to compress as much information about x as possible in a smaller representation
 * Sparse representations: embed the dataset into a representation whose entries are mostly zeroes for most inputs
 * Independent representations: attempt to disentangle the sources of variation underlying the data distribution such that the dimensions of the representation are statistically independent

#### 5.8.1 Principal Components Analysis
* PCA learns a representation that has lower dimensionality than the original input
* It also learns a representation whose elements have no linear correlation with each other
* The k-means algorithm works by initializing k different centroids to different values, then alternating between two different steps until convergence
 * In one step, each training example is assigned to cluster i, where i is the index of the nearest centroid $\vector{\mu}^{(i)}$
 * In the other step, each centroid $\vector{\mu}^{(i)}$ is updated to the mean of all training examples $\vector{x}^{(j)}$ assigned to cluster i
* Clustering may end up generating different clusters because of the feature that are used to create the clusters (red cars/trucks vs gray cars/trucks, red/gray cars vs red/gray trucks)

#### 5.8.2 k-means Clustering
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
#### 5.11.2 Local Constancy and Smoothness Regularization
* The core idea in deep learning is that we assume that the data was generated by the composition of factors or features, potentially at multiple levels in a hierarchy

#### 5.11.3 Manifold Learning
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

##### 6.2.1.1 Learning Conditional Distributions with Maximum Likelihood
* Most modern neural networks are trained using maximum likelihood

#### 6.2.2 Output Units
* The choice of cost function is tightly coupled with the choice of output unit

##### 6.2.2.3 Softmax Units for Multinoulli Output Distributions
* Objective functions that do not use a log to undo the exp of the softmax fail to learn when the argument to the exp becomes very negative, causing the gradient to vanish
* In particular, squared error is a poor loss function for softmax units, and can fail to train the model to change its output, even when the model makes highly confident incorrect predictions
* From a neuroscientific point of view, it is interesting to think of the softmax as a way to create a form of competition between the units that participate in it: the softmax outputs always sum to 1 so an increase in the value of one unit necessarily corresponds to a decrease in the value of others
* Softmax => soft argmax

### 6.3 Hidden Units
#### 6.3.1 Rectified Linear Units and Their Generalizations
* $g(z) = max\{0, z\}$
* One drawback to rectified linear units is that they cannot learn via gradient-based methods on examples for which their activation is zero
* Three generalizations of rectified linear units are based on using a non-zero slope $\alpha_i$ when $z_i < 0$: $h_i = g(\vector{z}, \vector{\alpha})_i = \text{max}(0, z_i) + \alpha_i \text{min}(0, z_i)$
 * Absolute value rectification, $\alpha_i = -1$
 * Leaky ReLU, $\alpha_i \approx 0.01$
 * Parametric ReLU (PReLU), $\alpha_i$ as a learnable parameter
* With large enough k, a maxout unit can learn to approximate any convex function with arbitrary fidelity
* Maxout units typically need more regularization than rectified linear units
* Maxout units can work well without regularization if the training set is large and the number of pieces per unit is kept low
* ReLU and all of these generalizations of them are based on the principle that models are easier to optimize if their behavior is closer to linear

#### 6.3.2 Logistic Sigmoid and Hyperbolic Tangent
* The widespread saturation of sigmoidal units can make gradient-based learning very difficult. For this reason, their use as hidden units in feedforward networks is now discouraged
* The use of sigmoidal units as output units is compatible with the use of gradient-based learning when an appropriate cost function can undo the saturation of the sigmoid in the output layer
* When a sigmoidal activation function must be used, the hyperbolic tangent activation function typically performs better than the logistic sigmoid

### 6.4 Architecture Design
* The word architecture refers to the overall structure of the network: how many units it should have and how these units should be connected to each other
* Most neural networks are organized into groups of units called layers
* Most neural network architectures arrange these layers in a chain structure, with each layer being a function of the layer that preceded it
* The main considerations are to choose the depth of the network and the width of each layer

#### 6.4.1 Universal Approximation Properties and Depth
* The universal approximation theorem states that a feedforward network with a linear output layer and at least one hidden layer with any "squashing" activation function can approximate any Borel measurable function from one finite-dimensional space to another with any desired non-zero amount, provided that the network is given enough hidden units
* Borel measurability: any continous function on a closed and bounded subset of $\mathbb{R}^n$ is Borel measurable
* The universal approximation theorem means that regardless of what function we are trying to learn, we know that a large MLP will be able to represent that function
 * However, we are not guaranteed that the training algorithm will be able to learn that function
* Learning can fail for two reasons:
 * The optimization algorithm used for training may not be able to find the value of the parameters that corresponds to the desired function
 * The training algorithm might choose the wrong function due to overfitting

### 6.5 Back-Propagation and Other Differentiation Algorithms
#### 6.5.10 Higher-Order Derivatives
* Krylov methods are a set of iterative techniques for performing various operations like approximately inverting a matrix or finding approximations to its eigenvectors or eigenvalues, without using any operation other than matrix-vector products

### 6.6 Historical Notes
* 17th century: Chain rule (Leibniz, L'Hôpital)
* 19th century: Gradient descent as a technique for iteratively approximating the solution to optimization problems (Cauchy)
* 1940s: Machine learning models such as the perceptron
* Most of the improvement in neural network performance from 1986 to 2015 can be attributed to two factors:
 * Larger datasets have reduced the degree to which statistical generalization is a challenge for neural networks
 * Neural networks have become much larger, due to more powerful computers, and better software infrastructure
* A small number of algorithmic changes have improved the performance of neural networks noticeably
 * The replacement of mean squared error with the cross-entropy family of loss functions
 * The replacement of the sigmoid hidden units with piecewise linear hidden units, such as the rectified linear units

## 7 Regularization for Deep Learning
* Many strategies used in machine learning are explicitly designed to reduce the test error, possibly at the expense of increased training error
 * These strategies are known collectively as regularization
* Regularization of an estimator works by trading increased bias for reduced variance

### 7.1 Parameter Norm Penalties
$$
\tilde{J}(\vector{\theta}; \vector{X}, \vector{y}) = J(\vector{\theta}; \vector{X}, \vector{y}) + \alpha \Omega(\vector{\theta})
$$
* We want to decrease both the original objective J on the training data and some measure of the size of the parameters $\vector{\theta}$
* For neural networks, we typically choose to use a parameter norm penalty $\Omega$ that penalizes only the weights of the affine transformation at each layer and leaves the biases unregularized

### 7.4 Dataset Augmentation
* The best way to make a machine learning model generalize better is to train it on more data
* Injecting noise in the input to a neural network can be seen as a form of data augmentation

### 7.7 Multi-Task Learning
* A very common form of multi-task learning is one where different supervised tasks (predicting $\textbf{y}^{(i)}$ given $\textbf{x}$) share the same input $\textbf{x}$, as well as some intermediate-level representation $\vector{h}^{(shared)}$ capturing a common pool of factors. The model can generally be divided into two kinds of parts and associated parameters:
 * Task-specific parameters
 * Generic parameters, shared across all the tasks

### 7.8 Early Stopping
* Every time the error on the validation set improves, we store a copy of the model parameters
* When the training algorithm terminates, we return these parameters, rather than the latest parameters
* The algorithm terminates when no parameters have improved over the best recorded validation error for some pre-specified number of iterations
* Early stopping has the advantage over weight decay that early stopping automatically determines the correct amount of regularization while weight decay requires many training experiments with different values of its hyperparameter

### 7.9 Parameter Tying and Parameter Sharing
* While a parameter norm penalty is one way to regularize parameters to be close to one another, the more popular way is to use constraints: to force sets of parameters to be equal

### 7.11 Bagging and Other Ensemble Methods
* Bagging (short for bootstrap aggregating) is a technique for reducing generalization error by combining several models
* The idea is to train several different models separately, then have all of the models vote on the output for test examples
* This is a general strategy in machine learning called model averaging
* Techniques employing this strategy are known as ensemble methods

### 7.12 Dropout
* Dropout trains the ensemble consisting of all sub-networks that can be formed by removing non-output units from an underlying base network
* One advantage of dropout is that it is very computationally cheap
* Another advantage of dropout is that it does not significantly limit the type of model or training procedure that can be used
* Dropout is less effective with very little labeled training examples (<5000)
* One of the key insights of dropout is that training a network with stochastic behavior and making predictions by averaging over multiple stochastic decisions implements a form of bagging with parameter sharing
* Each hidden unit must be able to perform well regardless of which other hidden units are in the model

### 7.13 Adversarial Training
* Training on adversarially perturbed examples from the training set (taking examples, modifying them slightly such that the current network will return a different label than the expected one)
* The primary causes of these adversarial examples is excessive linearity
* Adversarial training discourages highly sensitive locally linear behavior by encouraging the network to be locally constant in the neighborhood of the training data

## 8 Optimization for Training Deep Models
### 8.1 How Learning Differs from Pure Optimization
#### 8.1.3 Batch and Minibatch Algorithms
* Optimization algorithms that use the entire training set are called batch or deterministic gradient methods
* Optimization algorithms that use only a single example at a time are sometimes called stochastic or sometimes online methods

### 8.2 Challenges in Neural Network Optimization
#### 8.2.1 Ill-Conditioning
* Very small steps increase the cost function

#### 8.2.2 Local Minima
* The model identifiability problem: A model is said to be identifiable if a sufficiently large training set can rule out all but one setting of the model's parameter
* Local minima can be problematic if they have high cost in comparison to the global minimum
* A test that can rule out local minima as the problem is to plot the norm of the gradient over time. If the norm of the gradient does not shrink to insignificant size, the problem is neither local minima nor any other kind of critical point

#### 8.2.3 Plateaus, Saddles and Other Flat Regions
* We can think of a saddle point as being a local minimum along one cross-section of the cost function and a local maximum along another cross-section
* For a function $f: \mathbb{R}^n \rightarrow \mathbb{R}$, the expected ratio of the number of saddle points to local minima grows exponentially with $n$

#### 8.2.4 Cliffs and Exploding Gradients
* The cliff can be dangerous whether we approach it from above or below, but fortunately its most serious consequences can be avoided using the gradient clipping heuristic
* The basic idea is that the gradient does not specify the optimal step size, but only the optimal direction within an infinitesimal region
* Cliff structures are most common in the cost functions for recurrent neural networks, because such models involve a multiplication of many factors, with one factor for each time step

#### 8.2.5 Long-Term Dependencies
* The vanishing and exploding gradient problem refers to the fact that gradients through computational graph that contains a path that consists of repeatedly multiplying by a matrix $W$ are also scaled according to $diag(\lambda)^t$
* Vanishing gradients make it difficult to know which direction the parameters should move to improve the cost function
* Exploding gradients can make learning unstable

### 8.3 Basic Algorithms
#### 8.3.1 Stochastic Gradient Descent
* $\epsilon_0$: Initial learning rate
* $\tau$: the number of iterations until $\epsilon_\tau$ is reached
* $\epsilon_\tau$: final learning rate (generally about 1% of $\epsilon_0$)
* Typically, the optimal initial learning rate, in terms of total training time and the final cost value, is higher than the learning rate that yields the best performance after the first 100 iterations or so
* The most important property of SGD is that computation time per update does not grow when the number of training examples becomes very large

#### 8.3.2 Momentum
* The method of momentum is designed to accelerate learning, especially in the face of high curvature, small but consistent gradients, or noisy gradients
* The momentum algorithm accumulates an exponentially decaying moving average of past gradients and continues to move in their direction
* Momentum aims primarily to solve two problems:
	* Poor conditioning of the Hessian matrix
	* Variance in the stochastic gradient

#### 8.3.3 Nesterov Momentum
* A variant of the moment algorithm
* The difference is where the gradient is evaluated
	* Nesterov: the gradient is evaluated after the current velocity is applied

### 8.4 Parameter Initialization Strategies
* Training algorithms for deep learning models are usually iterative in nature and thus require the user to specify some initial point from which to begin the iterations
* The initial parameters need to "break symmetry" between different units
	* If two hidden units have the same initial parameters, then a deterministic learning algorithm applied to a deterministic cost and model will constantly update both of these units in the same way

### 8.5 Algorithms with Adaptive Learning Rates
* The learning rate is reliably one of the hyperparameters that is the most difficult to set because it has significant impact on model performance
* The delta-bar-delta algorithm is an early heuristic approach to adapting individual learning rates for model parameters during training
	* The approach is based on a simple idea:
		* If the partial derivative of the loss, with respect to a given model parameter, remains the same sign, then the learning rate should increase
		* If the partial derivative with respect to that parameter changes sign, then the learning rate should decrease

#### 8.5.1 AdaGrad
* Adapts the learning rates of all model parameters by scaling them inversely proportional to the square root of the sum of all their historical values
* Empirically it has been found that the accumulation of squared gradients from the beginning of training can result in premature and excessive decrease in the effective learning rate

#### 8.5.2 RMSProp
* Modifies AdaGrad to perform better in the non-convex setting by changing the gradient accumulation into an exponentially weighted moving average
* Empirically, RMSProp has been shown to be an effective and practical optimization algorithm for deep neural networks

#### 8.5.3 Adam
* The name "Adam" derives from the phrase "adaptive moments"
* It is perhaps best seen as a variant on the combination of RMSProp and momentum with a few important distinctions:
	* Momentum is incorporated directly as an estimate of the first order moment (with exponential weighting) of the gradient
	* Adam includes bias corrections to the estimates of both the first-order moments (the momentum term) and the (uncentered) second-order moments to account for their initialization at the origin
* Adam is generally regarded as being fairly robust to the choice of hyperparameters, though the learning rate sometimes needs to be changed from the suggested default

### 8.7 Optimization Strategies and Meta-Algorithms
#### 8.7.1 Batch Normalization
* Normalize (subtract the mean and divide by the standard deviation) every entry of a matrix $\vector{H}$ which is a minibatch of activations of the layer to normalize
* In order to maintain the expressive power of the (neural) network, it is common to replace the batch of hidden unit actions $\vector{H}$ with $\vector{\gamma H'} + \vector{\beta}$ rather than the simply normalized $\vector{H'}
	* It's easier to learn $\vector{\gamma}$ and $\vector{\beta}$ than the complicated interaction between the parameters in the layers below $\vector{H}$

#### 8.7.2 Cordinate Descent
* We optimize one coordinate at a time
* Block coordinate descent: Minimizing with respect to a subset of the variables simultaneously
* Coordinate descent is not a very good strategy when the value of one variable strongly influences the optimal value of another variable

#### 8.7.3 Polyak Averaging
* Consists of averaging together several points in the trajectory through parameter space visited by an optimization algorithm
* The basic idea is that the optimization algorithm may leap back and forth across a valley several times without ever visiting a point near the bottom of the valley. The average of all of the locations on either side should be close to the bottom of the valley though

#### 8.7.4 Supervised Pretraining
* Strategies that involve training simple models on simple tasks before confronting the challenge of training the desired model to perform the desired task are collectively known as pretraining

#### 8.7.5 Designing Models to Aid Optimization
* To improve optimization, the best strategy is not always to improve the optimization algorithm
* Most of the advances in neural network learning over the past 30 years (1986-2016) have been obtained by changing the model family rather than changing the optimization procedure
* Modern neural nets have been designed so that their local gradient information corresponds reasonably well to moving toward a distant solution

#### 8.7.6 Continuation Methods and Curriculum Learning
* Many of the challenges in optimization arise from the global structure of the cost function and cannot be resolved merely by making better estimates of local update directions
* The predominant strategy for overcoming this problem is to attempt to initialize the parameters in a region that is connected to the solution by a short path through parameter space that local descent can discover
* Continuation methods are a family of strategies that can make optimization easier by choosing initial points to ensure that local optimization spends most of its time in well-behaved regions of space
* The idea behind continuation methods is to construct a series of objective functions over the same parameters
* To solve complex cost functions, continuation methods would construct easier cost functions by "blurring" the original cost functions
* This blurring preserves enough information about the location of a global minimum that we can find the global minimum by solving progressively less blurred versions of the problem
* This approach can break down in three different ways
	* It might successfully define a series of cost functions where the first is convex and the optimum tracks from one function to the next arriving at the global minimum, but it might require so many incremental cost functions that the cost of the entire procedure remains high
	* The function might not become convex, no matter how much it is blurred
	* The function may become convex as a result of blurring, but the minimum of this blurred function may track to a local rather than a global minimum of the original cost function

## 9 Convolutional Networks
* Convolutional networks are a specialized kind of neural networks for processing data that has a known, grid-like topology
* Employs a mathematical operation called convolution
	* Convolution is a specialized kind of linear operation

### 9.1 The Convolution Operation
* Continuous convolution
$$
s(t) = \int x(a)w(t - a)\,da \\
s(t) = (x * w)(t)
$$
* x is often referred as the input and w as the kernel
* The output is sometimes referred to as the feature map
* Discrete convolution
$$
s(t) = (x * w)(t) = \sum_{a = -\infty}^{\infty} x(a)w(t - a)
$$
* Cross-correlation is also known as convolution in many machine learning libraries

### 9.2 Motivation
* Convolution leverages three important ideas that can help improve a machine learning system
	* Sparse interactions: Not every output unit interacts with every input unit
	* Parameter sharing: The same parameter is used by more than one function in a model
	* Equivariant representations: If the input changes, the output changes in the same way

### 9.3 Pooling
* A typical layer of a convolutional network consists of three stages:
	* The layer performs several convolutions in parallel to produce a set of linear activations
	* Each linear activation is run through a nonlinear activation function, such as the rectified linear activation function (also known as the detector stage)
	* A pooling function is used to modify the output of the layer further
* Replaces the output of the net at a certain location with a summary statistic of the nearby outputs
* Pooling helps to make the representation become approximately invariant to small translations of the input
* For many tasks, pooling is essential for handling inputs of varying size

### 9.4 Convolution and Pooling as an Infinitely Strong Prior
* An infinitely strong prior places zero probability on some parameters and says that these parameter values are completely forbidden, regardless of how much support the data gives to those values
* We can think of the use of convolution as introducing an infinitely strong prior probability distribution over the parameters (weights) of a layer
* Convolution and pooling can cause underfitting

### 9.5 Variants of the Basic Convolution Function
Unshared convolution: similar operation to discrete convolution with a small kernel, but without sharing parameters across locations
* Tiled convolution: a compromise between a convolutional layer and a locally connected layer

### 9.7 Data Types
* Convolution for processing variable sized inputs only makes sense for inputs that have variable size because they contain varying amounts of observations of the same kind
* Convolution does not make sense if the input has variable size because it can optionally include different kind of observations

### 9.9 Random or Unsupervised Features
* Typically, the most expensive part of convolutional network training is learning the features
* One way to reduce the cost of convolutional network training is to use features that are not trained in a supervised fashion
* Three strategies for obtaining convolutional kernels without supervised training:
	* Initialize them randomly
	* Design them by hand
	* Learn the kernels with an unsupervised criterion (e.g., k-means clustering)

## 10 Sequence Modeling: Recurrent and Recursive Nets
* Recurrent neural networks are a family of neural networks for processing sequential data
* Parameter sharing makes it possible to extend and apply the model to examples of different forms (different length) and generalize across them
* Each member of the output is a function of the previous members of the output
* Each member of the output is produced using the same update rule applied to the previous outputs

### 10.1 Unfolding Computational Graphs
* Unfolding is the application of a recurrent function to itself in order to obtain a new function that does not involve recurrence
* Unfolding introduces two major advantages:
	* Regardless of sequence length, the learned model always has the same input size, because it is specified in terms of transition from one state to another state, rather than specified in terms of variable-length history of states
	* It is possible to use the same transition function f with the same parameters at every time step

### 10.2 Recurrent Neural Networks
* Important design patterns for recurrent neural networks:
	* Recurrent networks that produce an output at each time step and have recurrent connections between units
	* Recurrent networks that produce an output at each time step and have recurrent connections only from the output at one time step to the hidden units at the next time step
	* Recurrent networks with recurrent connections between hidden units, that read an entire sequence and then produce a single output

#### 10.2.1 Teacher Forcing and Networks with Output Recurrence
* The advantage of eliminating hidden-to-hidden recurrence is that all the time steps are decoupled for any loss function based on comparing the prediction at time t to the training target at time t
	* Training can thus be parallelized, with the gradient for each step t computed in isolation
* Models that have recurrent connections from their outputs leading back into the model may be trained with teacher forcing
* Teacher forcing is a procedure in which during training the model receives the ground truth output $\vector{y}^{(t)}$ as input at time t+1

#### 10.2.2 Computing the Gradient in a Recurrent Neural Network
* To compute the gradient through a recurrent neural network, simply apply the generalized back-propagation algorithm to the unrolled computational graph

#### 10.2.3 Recurrent Networks as Directed Graphical Models
* It is difficult to predict missing values in the middle of a sequence
* The price recurrent networks pay for their reduced number of parameters is that optimizing the parameters may be difficult
* It relies on the assumption that the same parameters can be used for different time steps
* The assumption is that the conditional probability distribution over the variables at time t+1 given the variables at time t is stationary

### 10.3 Bidirectional RNNs
* In many application we want to output a prediction $\vector{y}^{(t)}$ which may depend on the whole input sequence
* Bidirectional RNNs combine an RNN that moves forward through time beginning from the start of the sequence with another RNN that moves backward through time beginning from the end of the sequence
* Compared to a convolutional network, RNNs applied to images are typically more expensive but allow for long-range lateral interactions between features in the same feature map

### 10.4 Encoder-Decoder Sequence-to-Sequence Architecture
* We often call the input to the RNN the "context"
* An encoder or reader or input RNN processes the input sequence
* The encoder emits the context C, usually a simple function of its final hidden state
* A decoder or writer or output RNN is conditioned on that fixed-length vector to generate the output sequence
* There is no constraint that the encoder must have the same size of hidden layer as the decoder
* One clear limitation of this architecture is when the context C output by the encoder RNN has a dimension that is too small to properly summarize a long sequence

### 10.6 Recursive Neural Networks
* Represent a generalization of recurrent networks with a different kind of computational graph, which is structured as a deep tree, rather than the chain-like structure of RNNs
* One clear advantage of recursive nets over recurrent nets is that for a sequence of the same length $\tau$, the depth can be drastically reduced from $\tau$ to $O(\log \tau)$

### 10.7 The Challenge of Long-Term Dependencies
* The basic problem is that gradients propagated over many stages tend to either vanish or explode
* The difficulty with long-term dependencies arises from the exponentially smaller weights given to long-term interactions compared to short-term ones
* In order to store memories in a way that is robust to small perturbations, the RNN must enter a region of parameter space where gradients vanish
* The problem of learning long-term dependencies remains one of the main challenges in deep learning

### 10.10 The Long Short-Term Memory and Other Gated RNNs
* Based on the idea of creating paths through time that have derivatives that neither vanish nor explode

#### 10.10.1 LSTM
* Composed of an input, an input gate, a forget gate, an output gate and a state (the LSTM "cell")

#### 10.10.2 Other Gates RNNs
* The main difference with the LSTM is that a single gating unit simultaneously controls the forgetting factor and the decision to update the state unit
* A crucial ingredient is the forget gate
* Adding a bias of 1 to the LSTM forget gate makes the LSTM as strong as the best of the explored architectural variants

### 10.12 Explicit Memory
* Neural networks excel at storing implicit knowledge. However, they struggle to memory facts
* Memory networks include a set of memory cells that can be accessed via an addressing mechanism
* Memory networks originally required a supervision signal instructing them how to use their memory cell
* The neural Turing machine is able to learn to read from and to write arbitrary content to memory cells without explicit supervision about which actions to undertake, and allowed end-to-end training without this supervision signal, via the use of a content-based soft attention mechanism
* Each memory cell can be thought of as an extension of the memory cells in LSTMs or GRUs. The difference is that the network outputs an internal state that chooses which cell to read from or write to, just as memory accesses in a digital computer read from or write to a specific address
* It is difficult to optimize functions that produce exact, integer addresses. To alleviate this problem, NTMs actually read to or write from many memory cells simultaneously
	* To read, they take a weighted average of many cells
	* To write, they modify multiple cells by different amounts
* There are two reason to increase the size of the memory cell:
	* We have increased the cost of accessing a memory cell (accessing implies reading a number of cells)
	* Vector-valued memory cells allow for content-based addressing, where the weight used to read or to write from a cell is a function of that cell

## 11 Practical Methodology
* Determine your goals - what error metric to use, and your target value for this error metric
* Establish a working end-to-end pipeline as soon as possible, including the estimation of the appropriate performance metrics
* Instrument the system well to determine bottlenecks in performance. Diagnose which components are performing worse than expected and whether it is due to overfitting, underfitting, or a defect in the data or software
* Repeatedly make incremental changes such as gathering new data, adjusting hyperparameters, or changing algorithms, based on specific findings from your instrumentation

### 11.1 Performance Metrics
* The Bayes error defines the minimum error rate that you can hope to achieve, even if you have infinite training data and can recover the true probability distribution. This is because your input features may not contain complete information about the output variable, or because the system might be intrinsically stochastic
* Precision: the fraction of detections reported by the model that were correct
* Recall: the fraction of true events that were detected
* PR curve: precision on the y-axis and recall on the x-axis
* F-score (precision p, recall r)
$$
F = \frac{2pr}{p+r}
$$
* Coverage: the fraction of examples for which the machine learning system is able to produce a response

### 11.2 Default Baseline Models
* First, choose the general category of model based on the structure of your data
* A reasonable choice of optimization algorithm is SGD with momentum with a decaying learning rate
	* Popular decay schemes include decaying linearly until reaching a fixed minimum learning rate, decaying exponentially, or decreasing the learning rate by a factor of 2-10 each time validation error plateaus
* Another very reasonable alternative is Adam
* Batch normalization can have a dramatic effect on optimization performance, especially for convolutional networks and networks with sigmoidal nonlinearities
* Unless your training data set contains tens of millions of examples or more, you should include some mild forms of regularization from the start
* Early stopping should be used almost universally
* Dropout is an excellent regularizer that is easy to implement and compatible with many models and training algorithms
* Batch normalization also sometimes reduces generalization error and allows dropout to be omitted, due to the noise in the estimate of the statistics used to normalize each variable

### 11.3 Determining Whether to Gather More Data
* It is often much better to gather more data than to improve the learning algorithm
* First, determine whether the performance on the training set is acceptable
	* If performance on the training set is poor, the learning algorithm is not using the training data that is already available, so there is no reason to gather more data
	* Try increasing the size of the model by adding more layers or adding more hidden units to each layer
	* Try improving the learning rate of the algorithm, for example by tuning the learning rate hyperparameters
	* If large models and carefully tuned optimization algorithms do not work well, then the problem might be the quality of the training data
		* The data may be too noisy or may not include the right inputs needed to predict the desired outputs
* Then measure the performance on a test set
	* If the performance on the test set is also acceptable, then there is nothing left to be done
	* If test set performance is much worse than training set performance, then gathering more data is one of the most effective solutions
	* A simple alternative to gathering more data is to reduce the size of the model or improve regularization, by adjusting hyperparameters such as weight decay coefficients, or by adding regularization strategies such as dropout
	* When deciding whether to gather more data, it is also necessary to decide how much to gather. It is helpful to plot curves showing the relationship between training set size and generalization error. By extrapolating such curves, one can predict how much additional training data would be needed to achieve a certain level of performance
	* If gathering much more data is not feasible, the only other way to improve generalization error is to improve the learning algorithm itself

### 11.4 Selecting Hyperparameters
* There are two basic approaches to choosing hyperparameters:
	* Choosing them manually: requires understanding what the hyperparameters do and how machine learning models achieve good generalization
	* Choosing them automatically: greatly reduce the need to understand these ideas, but they are often much more computationally costly

#### 11.4.1 Manual Hyperparameter Tuning
* The goal of manual hyperparameter search is usually to find the lowest generalization error subject to some runtime and memory budget
* The primary goal of manual hyperparameter search is to adjust the effective capacity of the model to match the complexity of the task
* Effective complexity is constrained by three factors:
	* the representational capacity of the model
	* the ability of the learning algorithm to successfully minimize the cost function used to train the model
	* the degree to which the cost function and training procedure regularize the model
* The generalization error typically follows a U-shaped curve when plotted as a function of one of the hyperparameters
* Low capacity, high generalization error because training error is high -> underfitting
* High capacity, high generalization error because the gap between trainig and test error is high -> overfitting
* Somewhere in the middle lies the optimal model capacity, which achieves the lowest possible generalization error
* Not every hyperparameter will be able to explore the entire U-shaped curve
	* Some are discrete, some are binary (thus only a few points along the curve are visited)
* The learning rate is perhaps the most important hyperparameter
* If your error on the training set is higher than your target error rate, you have no choice but to increase capacity
* If your error on the test set is higher than your target error rate, you can take two kind of actions
	* The goal is to reduce to gap between training error and test error without increasing training error faster than the gap decreases
	* To reduce the gap, change regularization hyperparameters to reduce effective model capacity, such as by adding dropout or weight decay

#### 11.4.2 Automatic Hyperparameter Optimization Algorithms
* We are trying to find a value of the hyperparameters that optimizes an objective function, such as validation error, sometimes under constraints (such as a budget for training time, memory or recognition time)
* Hyperparameter otpimization algorithms often have their own hyperparameters, such as the range of values that should be explored for each of the learning algorithm's hyperparameters

#### 11.4.3 Grid Search
* The grid search algorithm trains a model for every joint specification of hyperparameter values in the Cartesian product of the set of values for each individual hyperparameter
* The experiment that yield the best validation set error is then chosen as having found the best hyperparameters
* The obvious problem with grid search is that its computational cost grows exponentially with the number of hyperparameters
	* If there are m hyperparameters, each taking at most n values, then the number of training and evaluation trials required grows as $O(n^m)$

#### 11.4.4 Random Search
* More convenient to use and converges much faster to good values of the hyperparameters (than grid search)
* First we define a marginal distribution for each hyperparameter, then sample based on the given distribution
* A random search can be exponentially more efficient than a grid search, when there are several hyperparameters that do not strongly affect the performance measure

#### 11.4.5 Model-Based Hyperparameter Optimization
* We can build a model of the validation set error, then propose new hyperparameter guesses by performing optimization within this model
* Contemporary approaches to hyperparameter optimization include Spearmint, TPE and SMAC

### 11.5 Debugging Strategies
* We do not know a priori what the intended behavior of the algorithm is
* Most machine learning models have multiple parts that are each adaptive
* Most debugging strategies for neural nets are designed to get around one or both of these two difficulties
	* Either we design a case that is so simple that the correct behavior actually can be predicted, or we design a test that exercises one part of the neural network implementation in isolation
* Some important debugging tests:
	* Visualize the model in action
	* Visualize the worst mistakes
	* Reasoning about software using train and test error
	* Fit a tiny dataset
	* Compare back-propagated derivatives to numerical derivatives
	* Monitor histograms of activations and gradient

## 12 Applications
### 12.1 Large-Scale Deep Learning
* A large population of neurons or features acting together can exhibit intelligent behavior
* One of the key factors responsible for the improvement in neural network's accuracy and the improvement of the complexity of tasks they can solve between the 1980s and today is the dramatic increase in the size of the networks we use

#### 12.1.3 Large-Scale Distributed Implementations
* Asynchronous stochastic gradient descent
	* Several processor cores share the memory representing the parameters
	* Each core reads parameters without a lock, then computes a gradient, then increments the parameters without a lock
* Distributed asynchronous gradient descent remains the primary strategy for training large deep networks and is used by most major deep learning groups in industry

#### 12.1.4 Model Compression
* A key strategy for reducing the cost of inference is model compression
* The basic idea of model compression is to replace the original, expensive model with a smaller model that requires less memory and runtime to store and evaluate
* Model compression is applicable when the size of the original model is driven primarily by a need to prevent overfitting
* We can generate a training set containing infinitely many examples, simply by applying f to randomly sampled points $\vector{x}$
* We train the new, smaller, model to match $f(\vector{x})$ on these points. In order to most efficiently use the capacity of the new, small model, it is best to sample the new $\vector{x}$ points from a distribution resembling the actual test inputs that will be supplied to the model later

#### 12.1.5 Dynamic Structure
* One strategy for accelerating data processing systems in general is to build systems that have dynamic structure in the graph describing the computation needed to be process an input
* Data processing systems can dynamically determine which subset of many neural networks should be run on a given input
* This form of dynamic structure inside neural networks is sometimes called conditional computation
* A venerable strategy for accelerating inference in a classifier is to use a cascade of classifiers
* A simple way to accomplish the union of deep learning and dynamic structure is to train a decision tree in which each node uses a neural network to make the splitting decision
* One can use a neural network, called the gater to select which one out of several expert networks will be used to compute the output, given the current input
* The first version of this idea is called the mixture of experts
* One major obstacle to using dynamically structured systems is the decreased degree of parallelism that results from the system following different code branches for different inputs

### 12.2 Computer Vision
#### 12.2.1 Preprocessing
* Formatting images to have the same scale is the only kind of preprocessing that is strictly necessary
* Many computer vision architectures require images of a standard size, so images must be cropped or scaled to fit that size

##### 12.2.1.1 Contrast Normalization
* One of the most obvious source of variation that can be safely removed from many tasks is the amount of contrast in the image
* Contrast refers to the magnitude of the difference between the bright and the dark pixels in an image
* Global contrast normalization (GCN) aims to prevent images from having varying amounts of contrast by subtracting the mean from each image, then rescaling it so that the standard deviation across its pixels is equal to some constant s
* Local contrast normalization ensures that the contrast is normalized across each small window, rather than over the image as a whole
* One modifies each pixel by subtracting a mean of nearby pixels and dividing by a standard deviation of nearby pixels

### 12.3 Speech Recognition
* The task of speech recognition is to map an acoustic signal containing a spoken natural language utterance into the corresponding sequence of words intended by the speaker

### 12.4 Natural Language Processing
#### 12.4.1 n-grams
* An n-gram is a sequence of n tokens
* Models based on n-grams define the conditional probability of the n-th token given the preceding n - 1 tokens
* A fundamental limitation of maximum likelihood for n-gram models is that $P_n$ as estimated from training set counts is very likely to be zero in many cases
* Two catastrophic outcomes
	* $P_{n-1}$ is zero, the ratio is undefined
	* $P_{n-1}$ is non-zero but $P_n$ is zero, the test log-likelihood is $-\infty$
* To avoid such catastrophic outcomes, most n-gram models employ some form of smoothing
	* One basic technique consists of adding non-zero probability mass to  all the possible next symbol values
	* Another idea is to form a mixture model containing higher-order and lower-order n-gram models, with the higher-order models providing more capacity and the lower-order models being more likely to avoid counts of zero
* One way to view a classical n-gram model is that it is performing nearest-neighbor lookup
* Class-based language models introduce the notion of word categories and then share statistical strength between words that are in the same category

#### 12.4.2 Neural Language Models
* A class of language model designed to overcome the curse of dimensionality problem for modeling natural language sequences by using a distributed representation of words
* These word representations are sometimes called word embeddings
* We view the raw symbols as points in a space of dimension equal to the vocabulary size. The word representations embed those points in a feature space of lower dimension
* In the original space, every word is represented by a one-hot vector, so every pair of words is at Euclidean distance $\sqrt(2)$ from each other
* In the embedding space, words that frequently appear in similar contexts are close to each other

#### 12.4.3 High-Dimensional Outputs
* Vocabulary size being generally verge large, computing a softmax to determine the probability distribution of each word is very expensive (high computational cost to multiply)

##### 12.4.3.1 Use of a Short List
* Initially dealt with the high computational cost by limiting the vocabulary size to 10000 or 20000 words
* The vocabulary $\mathbb{V}$ is split into two lists: a shortlist $\mathbb{L}$ of most frequent words and a tail $\mathbb{T} = \mathbb{V} \setminus \mathbb{L}$ of more rare words
* A disadvantage of the short list approach is that the potential generalization advantage of the neural language models is limited to the most frequent words, where, arguably, it is the least useful

##### 12.4.3.2 Hierarchical Softmax
* One can think of this hierarchy as building categories of words, then categories of categories of words, etc.
* The probability of choosing a word is given by the product of the probabilities of choosing the branch leading to that word at every node on a path from the root of the tree to the leaf containing the word
* An important advantage of the hierarchical softmax is that it brings computational benefits both at training time and at test time, if at test time we want to compute the probability of specific words
* Another important operation is selecting the most likely word in a given context. Unfortunately the tree structure does not provide an efficient and exact solution to this problem
* A disadvantage is that in practice the hierarchical softmax tends to give worse test results than sampling-based methods

##### 12.4.3.3 Important Sampling
* Instead of sampling from the model, one can sample from another distribution, called the proposal distribution, and use appropriate weights to correct for the bias introduced by sampling from the wrong distribution

#### 12.4.4 Combining Neural Language Models with n-grams
* If we use hash tables or trees to access the count (of an n-gram), the computation used for n-grams is almost independent of capacity
* In comparison, doubling a neural network's number of parameters typically also roughly doubles its computation time
* One easy way to add capacity is to combine both approaches in an ensemble consisting of a neural language model and an n-gram language model

#### 12.4.5 Neural Machine Translation
* The task of reading a sentence in one natural language and emitting a sentence with the equivalent meaning in another language

##### 12.4.5.1 Using an Attention Mechanism and Aligning Pieces of Data
* We can think of an attention-based system as having three components:
	* A process that "reads" raw data (such as source words in a source sentence), and converts them into distributed representations, with one feature vector associated with each word position
	* A list of feature vectors storing the output of the reader. This can be understood as a "memory" containing a sequence of facts, which can be retrieved later, not necessarily in the same order, without having to visit all of them
	* A process that "exploits" the content of the memory to sequentially perform a task, at each time step having the ability to put attention on the content of one memory element (or a few, with a different weight)

### 12.5 Other Applications
#### 12.5.1 Recommender Systems
* Two major types of applications: online advertising and item recommendations
* Both rely on predicting the association between a user and an item, either to predict the probability of some action or the expected gain if an ad is shown or a recommendation is made regarding that product to that user
* Often, this association problem is handled like a supervised learning problem: given some information about the item and about the user, predict the proxy of interest
* This often ends up being either a regression problem or a probabilistic classification problem
* Early work on recommender systems relied on minimal information as inputs for these predictions: the user ID and the item ID
* There is a basic limitation of collaborative filtering systems: when a new item or a new user is introduced, its lack of rating history means that there is no way to evaluate its similarity with other items or users, or the degree of association between, say, that new user and existing items. This is called the problem of cold-start recommendations
* A general way of solving the cold-start recommendation problem is to introduce extra information about the individual user and items
* Systems that use such information are called content-based recommender systems

##### 12.5.1.1 Exploration Versus Exploitation
* Many recommendation problems are most accurately described theoretically as contextual bandits
* The term contextual bandits refers to the case where the action is taken in the context of some input variable that can inform the decision (e.g., the user identity)

#### 12.5.2 Knowledge Representation, Reasoning and Question Answering
##### 12.5.2.1 Knowledge, Relations and Question Answering
* In mathematics, a binary relation is a set of ordered pairs of objects
* In the context of AI, we think of a relation as a sentence in a syntactically simple and highly structured language
	* (subject, verb, object)
* We can define an attribute, a concept analogous to a relation, but taking only one argument
	* (subject, attribute)
* Early work used vectors for entities and matrices for relations, with the idea that a relation acts like an operator on entities
* Alternatively, relations can be considered as any other entity, allowing us to make statements about relations, but more flexibility is put in the machinery that combines them in order to model their joint distribution
* A practical short-term application of such models is link prediction: predicting missing arcs in the knowledge graph
* Knowledge of relations combined with a reasoning process and understanding of natural language could allow us to build a general question answering system
* A general question answering system must be able to process input information and remember important facts, organized in a way that enables it to retrieve and reason about them later

## 13 Linear Factor Models
* A linear factor model is defined by the use of a stochastic, linear decoder function that generates $\vector{x}$ by adding noise to a linear transformation of $\vector{h}$
* These models are interesting because they allow us to discover explanatory factors that have a simple joint distribution
* First, we sample the explanatory factors $\vector{h}$ from a distribution
* Next we sample the real valued observable variables given these factors
$$
\vector{x} = \vector{Wh} + \vector{b} + noise
$$

### 13.1 Probabilistic PCA and Factor Analysis
* Principal PCA, factor analysis and other linear factor models are special cases and only differ in the choices made for the noise distribution and the model's prior over latent variable $\vector{h}$ before observing $\vector{x}$
* In factor analysis, the latent variable prior is just the unit variance Gaussian
$$
\vector{\text{h}} \sim \mathcal{N}(\vector{h};\vector{0}, \vector{I})
$$
* The role of the latent variables is to capture the dependencies between the different observed variables

### 13.2 Independent Compnent Analysis (ICA)
* It is an approach to modeling linear factors that seeks to separate an observed signal into many underlying signals that are scaled and added together to form the observed data
* These signals are intended to be fully independent, rather than merely decorrelated from each other

### 13.3 Slow Feature Analysis
* Slow Feature Analysis (SFA) is a linear factor model that uses information from time signals to learn invariant features
* The slowness principle: The important characteristics of scenes change very slowly compared to the individual measurements that make up a description of a scene
* SFA seems to be a reasonably biologically plausible model
* A major advantage of SFA is that it is possible to theoretically predict which features SFA will learn

### 13.4 Sparse Coding
* Training sparse coding with maximum likelihood is intractable
* The training alternates between encoding the data and training the decoder to better reconstruct the data given the encoding

## 14 Autoencoders
* An autoencoder is a neural network that is trained to attempt to copy its input to its output
* Internally, it has a hidden layer $\vector{h}$ that describes a code used to represent the input
* The network may be viewed as consisting of two parts
	* An encoder function $\vector{h} = f(\vector{x})$
	* A decoder that produces a reconstruction $\vector{r} = g(\vector{h})$
* Autoencoders are designed to be unable to learn to copy perfectly
* Autoencoders may be thought of as being a special case of feedforward networks, and may be trained with all the same techniques, typically minibatch gradient descent following gradients computed by back-propagation
* Autoencoders may also be trained using recirculation, a learning algorithm based on comparing the activations of the network on the original input to the activation on the reconstructed input
* Recirculation is regarded as more biologically plausible than back-propagation, but is rarely used for machine learning applications

### 14.1 Undercomplete Autoencoders
* We hope that training the autoencoder to perform the input copying task will result in $\vector{h}$ taking on useful properties
* One way to obtain useful features from the autoencoder is to constrain $\vector{h}$ to have smaller dimension than $\vector{x}$
* An autoencoder whose code dimension is less than the input dimension is called undercomplete

### 14.2 Regularized Autoencoders
* Rather than limiting the model capacity by keeping the encoder and decoder shallow and the code size small, regularized autoencoders use a loss function that encourages the model to have other properties besides the ability to copy its input to its output
* These other properties include
	* Sparsity of the representation
	* Smallness of the derivative of the representation
	* Robustness to noise or to missing inputs
* A regularized autoencoder can be nonlinear and overcomplete but still learn something useful about the data distribution even if the model capacity is great enough to learn a trivial identity function
* Nearly any generative model with latent variables and equipped with an inference procedure (for computing latent representations given input) may be viewed as a particular form of autoencoder

#### 14.2.1 Sparse Autoencoders
* A sparse autoencoder is simply an autoencoder whose training criterion involves a sparsity penalty $\Omega(\vector{h})$ on the code layer $\vector{h}$, in addition to the reconstruction error
* Sparse autoencoders are typically used to learn features for another task such as classification

### 14.2.2 Denoising Autoencoders
* Rather than adding a penalty $\Omega$ to the cost function, we can obtain an autoencoder that learns something useful by changing the reconstruction error term of the cost function
* A denoising autoencoder (DAE) minimizes $\vector{\tilde{x}}$, a copy of $\vector{x}$ that has been corrupted by some form of noise
$$
L(\vector{x}, g(f(\vector{\tilde{x}})))
$$
* Denoising autoencoders must undo this corruption rather than simply copying their input

#### 14.2.3 Regularizing by Penalizing Derivatives
* Another strategy for regularizing an autoencoder is to use a penalty $\Omega$ as in sparse autoencoders, but with a different form of $\Omega$
* This forces the model to learn a function that does not change much when $\vector{x}$ changes slightly
* An autoencoder regularized in this way is called a contractive autoencoder (CAE)

### 14.3 Representational Power, Layer Size and Depth
* One major advantage of non-trivial depth (in autoencoders) is that the universal approximator theorem guarantees that a feedforward neural network with at least one hidden layer can represent an approximation of any function to an arbitrary degree of accuracy, provided that it has enough hidden units
* Depth can exponentially reduce the computational cost of representing some functions
* Depth can also exponentially decrease the amount of training data needed to learn some functions
* A common strategy for training a deep autoencoder is to greedily pretrain the deep architecture by training a stack of shallow autoencoders

### 14.5 Denoising Autoencoders
#### 14.5.1 Estimating the Score
* Score matching is an alternative to maximum likelihood
* It provides a consistent estimator of probability distributions based on encouraging the model to have the same score as the distribution at every training point $\vector{x}$
* A very important property of DAEs is that their training criterion makes the autoencoder learn a vector field $g(f(\vector{x}) - \vector{x})$ that estimates the score of the data distribution
* Denoising training of a specific kind of autoencoder (sigmoidal hidden units, linear reconstruction units) using Gaussian noise and mean squared error as the reconstruction cost is equivalent to training a specific kind of undirected probabilistic model called an RBM with Gaussian visible units
* One may want to use the autoencoder as a generative model and draw samples from this distribution

### 14.6 Learning Manifolds with Autoencoders
* An important characteristic of a manifold is the set of its tangent planes
* An autoencoder can afford to represent only the variations that are needed to reconstruct training examples
* What is most commonly learned to characterize a manifold is a representation of the data points on (or near) the manifold. Such a representation for a particular example is also called its embedding
* There is a fundamental difficulty with local non-parametric approaches to manifold learning: if the manifolds are not very smooth (they have many peaks and troughs and twists), one may need a very large number of training examples to cover each one of these variations, with no chance to generalize to unseen variations

### 14.7 Contractive Autoencoders
* The contractive autoencoder introduces an explicit regularizer on the code $\vector{h} = f(\vector{x})$, encouraging the derivatives of $f$ to be as small as possible
* Denoising autoencoders make the reconstruction function resist small but finite-sized perturbations of the input, while contractive autoencoders make the feature extraction function resist infinitesimal perturbations of the input
* The name contractive arises from the way that the CAE warps space

### 14.8 Predictive Sparse Decomposition
* Predictive sparse decomposition (PSD) is a model that is a hybrid of sparse coding and parametric autoencoders
* A parametric encoder is trained to predict the output of iterative inference
* The model consists of an encoder $f(\vector{x})$ and a decoder $g(\vector{h})$ that are both parametric

# See also

# References
* Goodfellow, Ian, Yoshua Bengio, and Aaron Courville. Deep learning. MIT Press, 2016.
* https://www.amazon.com/Deep-Learning-Adaptive-Computation-Machine/dp/0262035618