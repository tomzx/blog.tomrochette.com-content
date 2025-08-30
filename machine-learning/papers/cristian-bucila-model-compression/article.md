---
title: Cristian Bucila - Model Compression (2006)
created: 2017-07-07
taxonomy:
  tag: [machine-learning]
  status: finished
---

## Context

## Learned in this study

## Things to explore
* When is it not possible to compress an ensemble model?
* Is there a concept of lossy vs lossless compression of models?
* Why wasn't MUNGE compared against SMOTE, given it existed in the literature at that point (2002)?
* In most cases covered by the experiment, a complex NN/ensemble can be compressed to a single layer of hidden units, however, can this also apply to problems where we would use CNN/RNN?

# Overview
* Replace an ensemble by a simpler neural network (let a NN replicate the decisions a larger model would take)
* The technique is similar to having humans go through unlabeled data, labeling them, and then passing them along to a neural network to learn
* MUNGE is some sort of nearest neighbor data generator (takes example e, find the closest example e' in the training data set and uses the features of these two examples to create a new example)

# Notes
## 1. Introduction
* We show how to train compact artificial neural nets to mimic the function learned by ensemble selection
* We use the ensemble to label a large unlabeled data set and then train the neural net on this much larger, ensemble labeled, data set
* The key difficulty when compressing complex ensembles into simpler models this way is the need for a large  unlabeled data set

## 2. Model Compression
* The main idea behind model compression is to use a fast and compact model to approximate the function learned by a slower, larger, but better performing model
* An important question is how do we get the pseudo data (to train the model)
* It is important that the synthetic data match well the distribution of the real train and future test cases
* Usually real data lay in a small submanifold of the complete attribute space. If the synthetic data is drawn from a distribution that has little overlap to this manifold, the labeled synthetic points will fail to capture the target function in the region of interest
* On the other hand, if the distribution from which the synthetic data is simpled is too broad, only a fraction of the points will be drawn from the true manifold and many more samples will be necessary to adequately sample the region of interest

### 2.1 RANDOM
* The RANDOM method for generating pseudo data uses a nonparametric bootstrap approach
	* For each attribute, a value is selected uniformly at random from the multiset (bag) of all values for that attribute present in the train set
* When attribute values are generated independently, all conditional structure is lost and the pseudo examples are generated from a distribution that is usually much broader than the true distribution of the data
* As a consequence many of the generated pseudo examples will cover uninteresting parts of the space, and this may prevent the mimic model from focusing on the important regions

### 2.2 NBE
* Estimate the joint distribution of attributes using the training set, then sample pseudo examples from this joint distribution
* Assuming that the true joint distribution can be estimated well, the conditional structure of the domain would be preserved and the new artificial examples would cover well the interesting regions of the space
* One way to estimate the joint distribution of a set of variables is to use mixture model algorithms. These algorithms model the data as coming from a mixture of components, each component with a different distribution
* We use NBE to estimate the joint distribution of the attributes because it handles mixed attributes (discrete vs continuous), it is simple to use, it performs as well as learning a Beyesian Network from the same data, and it is readily available

### 2.3 MUNGE
* Estimating a full joint distribution is difficult when there are many attributes and a few training cases
* Starting from the original training set, we visit each example once and determine its closest neighbor (Euclidean distance for continuous attributes and Hamming distance for nominal attributes)
* Given example $e$ and its closest other example $e'$, the values for each noncontinuous attribute are swapped between $e$ and $e'$ with probability $p$ and are left unchanged with probability $1 - p$
* For each continuous attribute $a$, with probability $p$, $e_a$ is assigned a random value drawn from a normal distribution with mean $e'_a$ and standard deviation $sd = \frac{|e_a - e'_a|}{s}$, and $e'_a$ is assigned a random value drawn from the normal distribution with mean $e_a$ and the same standard deviation $sd$

## 3. Experimental Evaluation
### 3.2 Results
* On average, once the pseudo training set contains 100k or more data, the mimic neural nets perform considerably better than the best individual models in the ensemble libraries, and nearly as well as the target ensemble itself
* This is remarkable given that the mimic neural nets are 100-100000 times smaller than the ensembles, and 100 to 10000 times faster to execute
* It suggests that much smaller high performing models are possible if we only knew how to train them on the original training data
* Interestingly, ADULT is the only data set that has high-arity nominal attributes. The three attributes with the highest arity have 14, 16, 41 unique values. To train a neural net on ADULT, these attributes must first be converted to 14, 16, and 41 distinct binary attributes. The ADULT problem has only 14 attributes to begin with, yet these three attributes alone expand to 71 sparsely coded binary inputs. It is possible that neural nets are not well suited for this kind of problem, and may prevent the mimic neural net from learning the ensemble target function
	* An alternative possibility is that the MUNGE procedure is not effective at generating pseudo data for this kind of problem

## 4. Discussion
* The expense of model compression is justified only when high performing models must be used in applications with limited storage or computation power, in applications where predictions are needed in real time, or where there will be very many test cases

# See also

# References
* Buciluǎ, Cristian, Rich Caruana, and Alexandru Niculescu-Mizil. "Model compression." Proceedings of the 12th ACM SIGKDD international conference on Knowledge discovery and data mining. ACM, 2006.
