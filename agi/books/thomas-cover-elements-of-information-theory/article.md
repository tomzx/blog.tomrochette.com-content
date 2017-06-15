---
title: Thomas Cover - Elements of Information Theory - 2006
created: 2017-05-26
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview

# Pre-requisites
* Mathematics
	* Statistics
		* Random variables
		* Conditional probabilities
		* Mass function
	* Functions
	* Intervals
	* Derivatives
	* Series
		* Taylor series

# Notes
## Chapter 1 - Introduction and Preview
* Information theory answers two fundamental questions in communication theory:
	* What is the ultimate data compression (answer: the entropy $H$)
	* What is the ultimate transmission rate of communication (answer: the channel capacity $C$)
* The complexity of a string of data can be defined by the length of the shortest binary computer program for computing the string
* We consider Kolmogorov complexity to be more fundamental than Shannon entropy
* One can think about computational complexity (time complexity) and Kolmogorov complexity (program length or descriptive complexity) as two axes corresponding to program running time and program length. Kolmogorov complexity focuses on minimizing along the second axis, and computational complexity focuses on minimizing along the first axis

### 1.1 Preview of the Book
* The entropy of a random variable X with a probability mass function p(x) is defined by
$$
H(X) = - \sum_x p(x)\log_2 p(x)
$$
* Logarithm base 2, measures the entropy in bits
* The entropy is a measure of the average uncertainty in the random variable
* It is the number of bits on average required to describe the random variable
* We can define conditional entropy $H(X|Y)$, which is the entropy of a random variable conditional on the knowledge of another random variable. The reduction in uncertainty due to another random variable is called the mutual information
* For two random variables X and Y this reduction the mutual information
$$
I(X; Y) = H(X) - H(X|Y) = \sum_{x,y} p(x, y)\log \frac{p(x, y)}{p(x)p(y)}
$$
* A communication channel is a system in which the output depends probabilistically on its input. It is characterized by a probability transition matrix $p(y|x)$ that determines the conditional distribution of the output given the input. For a communication channel with input $X$ and output $Y$, we can define the capacity $C$ by
$$
C = \max_{p(x)} I(X; Y)
$$

## Chapter 2 - Entropy, Relative Entropy and Mutual Information
### 2.1 Entropy
* Let $X$ be a discrete random variable with alphabet $\mathcal{X}$ and probability mass function $p(x) = \text{Pr}\{X = x\}, x \in \mathcal{X}$
* The entropy $H(X)$ of a discrete random variable $X$ is defined by
$$
H(X) = - \sum_{x \in \mathcal{X}} p(x) \log p(x)
$$
* Some of the basic properties of entropy
	* It is a concave function of the distribution
	* Equals 0 when p = 0 or 1

### 2.2 Joint Entropy and Conditional Entropy
* The joint entropy $H(X, Y)$ of a pair of discrete random variable $(X, Y)$ with a joint distribution $p(x, y)$ is defined as
$$
H(X, Y) = - \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} p(x, y) \log p(x, y)
$$
which can also be expressed as
$$
H(X, Y) = -E \log p(X, Y)
$$
* If $(X, Y) \sim p(x, y)$, the conditional entropy $H(Y|X) is
$$
H(Y|X) = -E \log p(Y|X)
$$
$$
H(X, Y) = H(X) + H(Y|X)
$$
$$
\log p(X, Y) = \log p(X) + \log p(Y|X)
$$
$$
H(X, Y|Z) = H(X|Z) + H(Y|X, Z)
$$

### 2.3 Relative Entropy and Mutual Information
* The relative entropy is a measure of the distance between two distributions
* The relative entropy or Kullback-Leibler distance between two probability mass functions $p(x)$ and $q(x)$ is defined as
$$
\begin{split}
D(p||q) &= \sum_{x \in \mathcal{X}} p(x) \log \frac{p(x)}{q(x)} \\
&= E_p \log \frac{p(X)}{q(X)}
\end{split}
$$
* Mutual information is a measure of the amount of information that one random variable contains about another random variable
* It is the reduction in the uncertainty of one random variable due to the knowledge of the other
* Consider two random variables $X$ and $Y$ with a joint probability mass function $p(x, y)$ and marginal probability mass function $p(x)$ and $p(y)$. The mutual information $I(X; Y)$ is the relative entropy between the joint distribution and the production distribution $p(x)p(y)$
$$
\begin{split}
I(X; Y) &= \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} p(x, y) \log \frac{p(x, y)}{p(x)p(y)} \\
&= D(p(x, y)||p(x)p(y)) \\
&= E_{p(x, y)} \log \frac{p(X, Y)}{p(X)p(Y)}
\end{split}
$$

### 2.4 Relationship Between Entropy and Mutual Information
* We can rewrite the definition of mutual information $I(X; Y)$ as
$$
I(X; Y) = H(X) - H(X|Y)
$$
* Thus, the mutual information $I(X; Y)$ is the reduction in the uncertainty of $X$ due to the knowledge of $Y$
* By symmetry, it also follows that
$$
I(X; Y) = H(Y) - H(Y|X)
$$
$$
I(X; Y) = I(Y; X)
$$
* Since $H(X, Y) = H(X) + H(Y|X)$
$$
I(X; Y) = H(X) + H(Y) - H(X, Y)
$$
$$
I(X; X) = H(X) - H(X|X) = H(X)
$$
* Thus, the mutual information of a random variable with itself is the entropy of the random variable

### 2.5 Chain Rules For Entropy, Relative Entropy, and Mutual Information
* Let $X_1, X_2, \dots, X_n$ be drawn according to $p(x_1, x_2, \dots, x_n)$. Then
$$
H(X_1, X_2, \dots, X_n) = \sum_{i=1}^n H(X_i|X_{i-1}, \dots, X_1)
$$
* The conditional mutual information of random variables $X$ and $Y$ given $Z$ is defined by
$$
\begin{split}
I(X; Y|Z) &= H(X|Z) - H(X|Y, Z) \\
&= E_{p(x, y, z)} \log \frac{p(X, Y|Z)}{p(X|Z)p(Y|Z)}
\end{split}
$$
$$
I(X_1, X_2, \dots, X_n; Y) = \sum_{i=1}^n I(X_i; Y|X_{i-1}, X_{i-2}, \dots, X_1)
$$
$$
D(p(x, y)||q(x, y)) = D(p(x)||q(x)) + D(p(y|x)||q(y|x))
$$

### 2.6 Jensen's Inequality and its Consequences
* A function $f(x)$ is said to be convex over an interval $(a, b)$ if for every $x_1, x_2 \in (a, b)$ and $0 \le \lambda \le 1$
$$
f(\lambda x_1 + (1 - \lambda)x_2) \le \lambda f(x_1) + (1 - \lambda) f(x_2)
$$
* A function is said to be strictly convex if equality holds only if $\lambda = 0$ or $\lambda = 1$
* A function $f$ is concave if $-f$ is convex
* If the function $f$ has a second derivative that is non-negative (positive) over an interval, the function is convex (stricly convex) over that interval
* (Jensen's inequality) If $f$ is a convex function and $X$ is a random variable
$$
Ef(X) \ge f(EX)
$$
* Moreover, if $f$ is strictly convex, the equality implies that $X = EX$ with probability 1
* (Information inequality) Let $p(x)$, $q(x)$, $x \in \mathcal{X}$, be two probability mass functions. Then
$$
D(p||q) \ge 0
$$
with equality if and only if $p(x) = q(x)$ for all $x$
* (Nonnegativity of mutual information) For any two random variables, $X$, $Y$,
$$
I(X; Y) \ge 0
$$
with equality if and only if $X$ and $Y$ are independent
$$
D(p(y|x)||q(y|x)) \ge 0
$$
with equality if and only if $p(y|x) = q(y|x)$ for all $y$ and $x$ such that $p(x) > 0$
$$
I(X; Y|Z) \ge 0
$$
with equality if and only if $X$ and $Y$ are conditionally independent given Z
* (Conditioning reduces entropy)(Information can't hurt)
$$
H(X|Y) \le H(X)
$$
with equality if and only if $X$ and $Y$ are independent

### 2.8 Data-Processing Inequality
* The data processing inequality can be used to show that no clever manipulation of the data can improve the inferences that can be made from the data
* Random variables $X$, $Y$, $Z$ are said to form a Markov chain in that order (denoted $X \rightarrow Y \rightarrow Z$) if the conditional distribution of $Z$ depends only on $Y$ and is conditionally independent of $X$. Specifically, $X$, $Y$, $Z$ form a Markov chain $X \rightarrow Y \rightarrow Z$ if the joint probability mass function can be written as
$$
p(x, y, z) = p(x)p(y|x)p(z|y)
$$
* Some simple consequences are as follows:
	* $X \rightarrow Y \rightarrow Z$ if and only if $X$ and $Z$ are conditionally independent given $Y$
	* $X \rightarrow Y \rightarrow Z$ implies that $Z \rightarrow Y \rightarrow X$
	* If $Z = f(Y)$, then $X \rightarrow Y \rightarrow Z$
* If $X \rightarrow Y \rightarrow Z$, then $I(X; Y) \ge I(X; Z)$
* If $Z = g(Y)$, we have $I(X; Y) \ge I(X; g(Y))$
	* Thus functions of the data Y cannot increase the information about X

### 2.9 Sufficient Statistics
* A function $T(X)$ is said to be a sufficient statistic relative to the family $\{f_\theta(x)\}$ if $X$ is independent of $\theta$ given $T(X)$ for any distribution on $\theta$
* A statistic $T(X)$ is a minimal sufficient statistic relative to $\{f_\theta(x)\}$ if it is a function of every other sufficient statistic $U$
	* A minimal sufficient statistic maximally compresses the information about $\theta$ in the sample
	* Other sufficient statistics may contain additional irrelevant information

### 2.10 Fano's Inequality
* Let $P_e = \text{Pr}\{\hat{X}(Y) \ne X\}$. Then
$$
H(P_e) + P_e \log |\mathcal{X}| \ge H(X|Y)
$$
* If $X$ and $X'$ are independent and identically distributed, then
$$
\text{Pr}(X = X') \ge 2^{-H(X)}
$$

## Chapter 3 - Asymptotic Equipartition Property
-

## Chapter 4 - Entropy Rates of a Stochastic Process
### 4.1 Markov Chains
* A stochastic process is said to be stationary if the joint distribution of any subset of the sequence of random variables is invariant with respect to shifts in the time index; that is
$$
\text{Pr}\{X_1 = x_1, X_2 = x_2, \dots, X_n = x_n\} = \text{Pr}\{X_{1+l} = x_1, X_{2+l} = x_2, \dots X_{n+l} = x_n\}
$$
for every $n$ and every shift $l$ and for all $x_1, x_2, \dots, x_n \in \mathcal{X}$
* A discrete stochastic process $X_1, X_2, \dots$ is said to be a Markov chain or a Markov process if for $n = 1, 2, \dots$
$$
\text{Pr}(X_{n+1} = x_{n+1} | X_n = x_n, X_{n-1} = x_{n-1}, \dots, X_1 = x_1) = \text{Pr}(X_{n+1} = x_{n+1} | X_n = x_n)
$$
for all $x_1, x_2, \dots, x_n, x_{n+1} \in \mathcal{X}$
* The Markov chain is said to be time invariant if the conditional probability $p(x_{n+1}|x_n)$ does not depend on $n$; that is, for $n = 1, 2, \dots$
$$
\text{Pr}\{X_{n+1} = b | X_n = a\} = \text{Pr}\{X_2 = b | X_1 = a\}
$$
for all $a, b \in \mathcal{X}$

### 4.2 Entropy Rate
* The entropy of a stochastic process $\{X_i\}$ is defined by
$$
H(\mathcal{X}) = \lim_{n \rightarrow \infty} \frac{1}{n} H(X_1, X_2, \dots, X_n)
$$
when the limit exists
$$
H'(\mathcal{X}) = \lim_{n \rightarrow \infty} H(X_n | X_{n-1}, X_{n-2}, \dots, X_1)
$$
* For a stationary stochastic process, the limits exists and are equal:
$$
H(\mathcal{X}) = H'(\mathcal{X})
$$
$H'(\mathcal{X})$ is the conditional entropy on the last random variable given the past

### 4.3 Example: Entropy Rate of a Random Walk on a Weighted Graph
* It is easy to see that a stationary random walk on a graph is time-reversible; that is, the probability of any sequence of states is the same forward or backward
$$
\text{Pr}(X_1 = x_1, X_2 = x_2, \dots, X_n = x_n) = \text{Pr}(X_n = x_1, X_{n-1} = x_2, \dots, X_1 = x_n)
$$
* Any time-reversible Markov chain can be represented as a random walk on an undirected weighted graph

## Chapter 5 - Data Compression
### 5.1 Examples of Codes
* A source code $C$ for a random variable $X$ is a mapping from $\mathcal{X}$, the range of $X$, to $\mathcal{D}^*$, the set of finite-length strings of symbols from a $D$-ary alphabet. Let $C(x)$ denote the codeword corresponding to $x$ and let $l(x)$ denote the length of $C(x)$
* The expected length $L(C)$ of a source code $C(x)$ for a random variable $X$ with probability mass function $p(x)$ is given by
$$
L(C) = \sum_{x \in \mathcal{X}} p(x)l(x)
$$
* A code is said to be nonsingular if every element of the range of $X$ maps into a different string in $\mathcal{D}^*$; that is
$$
x \ne x' \Rightarrow C(x) \ne C(x')
$$
* The extension $C^*$ of a code $C$ is the mapping from finite-length strings of $\mathcal{X}$ to finite-length strings of $\mathcal{D}$, defined by
$$
C(x_1x_2x\cdots x_n) = C(x_1)C(x_2)\cdots C(x_n)
$$
where $C(x_1)C(x_2)\cdots C(x_n)$ indicates concatenation of the corresponding codewords
* A code is called uniquely decodable if its extension is non-singular
* A code is called a prefix code or an instantaneous code if no codeword is a prefix of any other codeword
	* An instantaneous code is a self-punctuating code

# See also

# References
* Thomas, Joy A., and Thomas M. Cover. Elements of information theory. John Wiley & Sons, 2006.