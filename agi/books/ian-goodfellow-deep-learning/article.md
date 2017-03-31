--- title: Ian Goodfellow - Deep Learning - 2016
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
* With large enough k, a maxout unit can learn to approximate any convex function with arbitrary fidelity
* Maxout units typically need more regularization than rectified linear units
* Maxout units can work well without regularization if the training set is large and the number of pieces per unit is kept low
* ReLU and all of these generalizations of them are based on the principle that models are easier to optimize if their behavior is closer to linear

### 6.3.2 Logistic Sigmoid and Hyperbolic Tangent
* The widespread saturation of sigmoidal units can make gradient-based learning very difficult. For this reason, their use as hidden units in feedforward networks is now discouraged
* The use of sigmoidal units as output units is compatible with the use of gradient-based learning when an appropriate cost function can undo the saturation of the sigmoid in the output layer
* When a sigmoidal activation function must be used, the hyperbolic tagent activation function typically performs better than the logistic sigmoid

### 6.4 Architecture Design
* The word architecture refers to the overall structure of the network: how many units it should have and how these units should be connected to each other
* Most neural networks are organized into groups of units called layers
* Most neural network architectures arrange these layers in a chain structure, with each layer being a function of the layer that preceded it
* The main considerations are to choose the depth of the network and the width of each layer

### 6.4.1 Universal Approximation Properties and Depth
* The universal approximation theorem states that a feedforward network with a linear output layer and at least one hidden layer with any "squashing" activation function can approximate any Borel measurable function from one finite-dimensional space to another with any desired non-zero amount, provided that the network is given enough hidden units
* Borel measurability: any continous function on a closed and bounded subset of $\mathbb{R}^n$ is Borel measurable
* The universal approximation theorem means that regardless of what function we are trying to learn, we know that a large MLP will be able to represent that function
 * However, we are not guaranteed that the training algorithm will be able to learn that function
* Learning can fail for two reasons:
 * The optimization algorithm used for training may not be able to find the value of the parameters that corresponds to the desired function
 * The training algorithm might choose the wrong function due to overfitting

### 6.5 Back-Propagation and Other Differentiation Algorithms
### 6.5.10 Higher-Order Derivatives
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
\tilde{J}(\boldsymbol{\theta}; \boldsymbol{X}, \boldsymbol{y}) = J(\boldsymbol{\theta}; \boldsymbol{X}, \boldsymbol{y}) + \alpha \Omega(\boldsymbol{\theta})
$$
* We want to decrease both the original objective J on the training data and some measure of the size of the parameters $\boldsymbol{\theta}$
* For neural networks, we typically choose to use a parameter norm penalty $\Omega$ that penalizes only the weights of the affine transformation at each layer and leaves the biases unregularized

### 7.4 Dataset Augmentation
* The best way to make a machine learning model generalize better is to train it on more data
* Injecting noise in the input to a neural network can be seen as a form of data augmentation

### 7.7 Multi-Task Learning
* A very common form of multi-task learning is one where different supervised tasks (predicting $\textbf{y}^{(i)}$ given $\textbf{x}$) share the same input $\textbf{x}$, as well as some intermediate-level representation $\boldsymbol{h}^{(shared)}$ capturing a common pool of factors. The model can generally be divided into two kinds of parts and associated parameters:
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
* Another advantage of dropout is that it does not significantly limit tyhe type of model or training procedure that can be used
* Dropout is less effective with very little labeled training examples (<5000)
* One of the key insights of dropout is that training a network with stochastic behavior and making predictions by averaging over multiple stochastic decisions implements a form of bagging with parameter sharing
* Each hidden unit must be able to perform well regardless of which other hidden units are in the model

### 7.13 Adversarial Training
* Training on adverserially perturbed examples from the training set (taking examples, modifying them slightly such that the current network will return a different label than the expected one)
* The primary causes of these adversarial examples is excessive linearity
* Adversarial training discourages highly sensitive locally linear behavior by encouraging the network to be locally constant in the neighborhood of the training data

## 8 Optimization for Training Deep Models
### 8.1 How Learning Differs from Pure Optimization
### 8.1.3 Batch and Minibatch Algorithms
* Optimization algorithms that use the entire training set are called batch or deterministic gradient methods
* Optimization algorithms that use only a single example at a time are sometimes called stochastic or sometimes online methods

### 8.2 Challenges in Neural Network Optimization
### 8.2.1 Ill-Conditioning
* Very small steps increase the cost function

### 8.2.2 Local Minima
* The model identifiability problem: A model is said to be identifiable if a sufficiently large training set can rule out all but one setting of the model's parameter
* Local minima can be problematic if they have high cost in comparison to the global minimum
* A test that can rule out local minima as the problem is to plot the norm of the gradient over time. If the norm of the gradient does not shrink to insignificant size, the problem is neither local minima nor any other kind of critical point

### 8.2.3 Plateaus, Saddles and Other Flat Regions
* We can think of a saddle point as being a local minimum along one cross-section of the cost function and a local maximum along another cross-section
* For a function $f: \mathbb{R}^n \rightarrow \mathbb{R}$, the expected ratio of the number of saddle points to local minima grows exponentially with $n$

### 8.2.4 Cliffs and Exploding Gradients
* The cliff can be dangerous whether we approach it from above or below, but fortunately its most serious consequences can be avoided using the gradient clipping heuristic
* The basic idea is that the gradient does not specify the optimal step size, but only the optimal direction within an infinitesimal region
* Cliff structures are most common in the cost functions for recurrent neural networks, because such models involve a multiplication of many factors, with one factor for each time step

### 8.2.5 Long-Term Dependencies
* The vanishing and exploding gradient problem refers to the fact that gradients through computational graph that contains a path that consists of repeatedly multiplying by a matrix $W$ are also scaled according to $diag(\lambda)^t$
* Vanishing gradients make it difficult to know which direction the parameters should move to improve the cost function
* Exploding gradients can make learning unstable

### 8.3 Basic Algorithms
### 8.3.1 Stochastic Gradient Descent
* $\epsilon_0$: Initial learning rate
* $\tau$: the number of iterations until $\epsilon_\tau$ is reached
* $\epsilon_\tau$: final learning rate (generally about 1% of $\epsilon_0$)
* Typically, the optimal initial learning rate, in terms of total training time and the final cost value, is higher than the learning rate that yields the best performance after the first 100 iterations or so
* The most important property of SGD is that computation time per update does not grow when the number of training examples becomes very large

### 8.3.2 Momentum
* The method of momentum is designed to accelerate learning, especially in the face of high curvature, small but consistent gradients, or noisy gradients
* The momentum algorithm accumulates an exponentially decaying moving average of past gradients and continues to move in their direction
* Momentum aims primarily to solve two problems:
	* Poor conditioning of the Hessian matrix
	* Variance in the stochastic gradient

### 8.3.3 Nesterov Momentum
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

### 8.5.1 AdaGrad
* Adapts the learning rates of all model parameters by scaling them inversely proportional to the square root of the sum of all their historical values
* Empirically it has been found that the accumulation of squared gradients from the beginning of training can result in premature and excessive decrease in the effective learning rate

### 8.5.2 RMSProp
* Modifies AdaGrad to perform better in the non-convex setting by changing the gradient accumulation into an exponentially weighted moving average
* Empirically, RMSProp has been shown to be an effective and practical optimization algorithm for deep neural networks

### 8.5.3 Adam
* The name "Adam" derives from the phrase "adaptive moments"
* It is perhaps best seen as a variant on the combination of RMSProp and momentum with a few important distinctions:
	* Momentum is incorporated directly as an estimate of the first order moment (with exponential weighting) of the gradient
	* Adam includes bias corrections to the estimates of both the first-order moments (the mometum term) and the (uncentered) second-order moments to account for their initialization at the origin
* Adam is generally regarded as being fairly robust to the choice of hyperparameters, though the learning rate sometimes needs to be changed from the suggested default

### 8.7 Optimization Strategies and Meta-Algorithms
### 8.7.1 Batch Normalization
* Normalize (substract the mean and divide by the standard deviation) every entry of a matrix $\boldsymbol{H}$ which is a minibatch of activations of the layer to normalize
* In order to maintain the expressive power of the (neural) network, it is common to replace the batch of hidden unit actions $\boldsymbol{H}$ with $\boldsymbol{\gamma H'} + \boldsymbol{\beta}$ rather than the simply normalized $\boldsymbol{H'}
	* It's easier to learn $\boldsymbol{\gamma}$ and $\boldsymbol{\beta}$ than the complicated interaction between the parameters in the layers below $\boldsymbol{H}$

### 8.7.2 Cordinate Descent
* We optimize one coordinate at a time
* Block coordinate descent: Minimizing with respect to a subset of the variables simultaneously
* Coordinate descent is not a very good strategy when the value of one variable strongly influences the optimal value of another variable

### 8.7.3 Polyak Averaging
* Consists of averaging together several points in the trajectory through parameter space visited by an optimization algorithm
* The basic idea is that the optimization algorithm may leap back and forth across a valley several times without ever visiting a point near the bottom of the valley. The average of all of the locations on either side should be close to the bottom of the valley though

### 8.7.4 Supervised Pretraining
* Strategies that involve training simple models on simple tasks before confronting the challenge of training the desired model to perform the desired task are collectively known as pretraining

### 8.7.5 Designing Models to Aid Optimization
* To improve optimization, the best strategy is not always to improve the optimization algorithm
* Most of the advances in neural network learning over the past 30 years (1986-2016) have been obtained by changing the model family rather than changing the optimization procedure
* Modern neural nets have been designed so that their local gradient information corresponds reasonably well to moving toward a distant solution

### 8.7.6 Continuation Methods and Curriculum Learning
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
* Cross-correlation is also known as convolution in many machine learnin libraries

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

# See also

# References
* Goodfellow, Ian, Yoshua Bengio, and Aaron Courville. Deep learning. MIT Press, 2016.
* https://www.amazon.com/Deep-Learning-Adaptive-Computation-Machine/dp/0262035618