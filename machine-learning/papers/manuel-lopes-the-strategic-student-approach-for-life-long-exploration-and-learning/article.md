---
title: Manuel Lopes - The Strategic Student Approach for Life-Long Exploration and Learning (2012)
created: 2017-06-24
taxonomy:
  tag: [Machine learning]
  status: finished
---

## Context

## Learned in this study

## Things to explore

# Overview

# Notes
## 1. Introduction
* Learning approaches
	* Ordered training examples provided by an external teacher
		* Optimal teaching techniques
		* Curriculum learning
	* Internal mechanisms of maturation
	* Internal mechanisms for active choice of either training examples, tasks to be explored, learning methods to be used, or questions to pose to a teacher
* Two broad strategies have been investigated
	* Methods devised around the strategy consisting in first exploring what is maximally complex (e.g., uncertain, high prediction errors, least visited) and then progressively explore what is more simple
	* First exploring what is simpler, and then progressively exploring what is more complex
* To realize developmental exploration, mechanisms of intrinsically motivated exploration and learning were introduced, modeling aspects of human spontaneous exploration and motivation
* Learning progress: measuring how learning performance improve over time or over learning methods
* We show that, if certain underlying properties of the learning problems are present (sub-modularity), an optimal developmental solution to this class of problem can be achieved through greedy maximization of learning progress

## 2. The Strategic Student Problem
* We imagine a student that is going to be tested in $K$ different topics and there are still $N$ days before the exam
* The problem for the student is to decide, each day, how to allocate the time to study each particular topic
* We assume that the topics are learnable at different rates and with different expected final scores
* Two effects of the learning curve between different subjects being different:
	* For the same allocated time on a given topic the expected score differs
	* The learning rate decreases with the total allocated time
* The problem can then be defined as finding the time allocation that maximize the average scores on all the different subjects with the restriction that the total time allocated is equal to the total time until the exam N
* $n_i$ is the total amount of time taken with topic $i$ and $q_i(n_i)$ is a function that describes the expected score on topic $i$ if $n_i$ time is used to study it
* The strategic student has to solve the following problem
$$
\begin{align*}
\max_{n_1, \dots, n_K} \sum_{i=1}^K q_i(n_i) \\
s.t. \sum_i n_i = N & , & n_i \ge 0
\end{align*}
$$
* When studying for some topics some chapters might be common with some other topics. [...] We can make a more complex model that represents this correlation betweens topic
* We can make the total score per subject depend on the time taken on all subjects
* We define a new function $q_i(\sum_{j=1}^K \phi_{ij}n_j)$ where the weights $\phi_{ij}$ represent how the different topics are related
* We can select, at each time instant:
	* the topic with less time allocated
	* the topic with lower expected score
	* the topic with score closest to the maximum
	* the topic with maximum expected improvement in score
* We consider $K$ topics each one with a standard power law for the scores
* $p_i$ is the difficulty of topic $i$
* The expected total score is the sum of the subject's score, $q_i = C_i(1 - e^{-\frac{n_i}{p_i}}) + B_i$
* The coefficient C and B make it explicit that it is not possible to achieve the same score in all topics and that some topics weight more than others
* For a known time frame $N$, the strategic student problem can be defined as
$$
\begin{align*}
\max_{n_i} \sum_{i} C_i(1 - e^{-\frac{n_i}{p_i}}) + B_i \\
s.t. \sum_i n_i = N & , & n_i \ge 0
\end{align*}
$$
* Heuristic of learning progress: At each time instant the student chooses the task where the expected progress is maximum, in other words, the task whose learning curve has a higher derivative (as long as learning is done under a smooth learning curve)

## 3. SSP: A Solution
* A simple greedy algorithm will provide a solution that is close to optimal for the case of submodular functions thus solving the combinatorial aspect of the problem
* Two main difficulties we have:
	* The case of non-submodular functions
	* The score function needs to be estimated empirically
* Both problems require a stochastic approach to either assure that early low learning progress is not due to ill behaved score functions and to balance between exploration, to estimate the progress, and exploitation, to select the topic with higher learning progress
* To have an initial solution to the SSP we can rely on the EXP4 algorithm

# See also

# References
* Lopes, Manuel, and Pierre-Yves Oudeyer. "The strategic student approach for life-long exploration and learning." Development and Learning and Epigenetic Robotics (ICDL), 2012 IEEE International Conference on. IEEE, 2012.
