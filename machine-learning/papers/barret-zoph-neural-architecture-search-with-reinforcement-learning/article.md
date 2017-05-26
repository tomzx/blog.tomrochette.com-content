---
title: Barret Zoph - Neural Architecture Search with Reinforcement Learning (2017)
created: 2017-05-25
taxonomy:
  category: [Machine Learning]
  status: finished
---

## Context

## Learned in this study

## Things to explore
* It seems that the purpose of this research would be to optimize the time it takes to find an "optimal" architecture, thus what is important is both the length of time/number of architecture tested to get a satisfying architecture as well as the quality of the found architecture
	* It would be interesting to know, compared to a grid search, how much time we'd expect to save
* Not much information about how much reinforcement actually occurs during training
	* There is however a figure that shows perplexity improvement over random search
* How are the number of parameters actually determined? And in the case of this work, how are they generated/determined?
* On p10 it is said that "the average of top models is also much better"... Is that to say they created an architecture where they merged the top X models into one and evaluated that model?
	* Considering figure 6, I'm not sure how it is that adding more models actually improves perplexity, as you'd expect that "worse" models should decrease the improvement on performance

# Overview
* Searching for the best neural network for a given problem can be seen as trying to come up with a set of actions that will result in this best neural network
	* The actions are to determine which layers to use, their sequence, connectivity, as well as their hyperparameters
* Seen as a reinforcement learning problem, we can define the resulting accuracy $R$ of a network over a validation set as the reward signal/value
* A lot of this work seems to rely on the available of a lot of computation power (testing and obtaining the accuracy of over 10k models using 400 CPUs or 800 GPUs)

# Notes
## 1 Introduction
* Our work is based on the observation that the structure and connectivity of a neural network can be typically specified by a variable-length string

## 3 Methods
### 3.1 Generate Model Descriptions With a Controller Recurrent Neural Network
* A controller is used to generate architectural hyperparameters of neural networks
* The controller is implemented as a recurrent neural network (to be flexible)
* The controller generates hyperparameters as a sequence of tokens
* Once the controller RNN finishes generating an architecture, a neural network with this architecture is built and trained. At convergence, the accuracy of the network on a held-out validation set is recorded. The parameters of the controller RNN are then optimized in order to maximize the expected validation accuracy of the proposed architectures

### 3.2 Training With REINFORCE
* The list of tokens that the controller predicts can be viewed as a list of actions $a_{1:T}$ (where T is the number of hyperparameters) to design an architecture for a child network
* At convergence, this child network will achieve an accuracy $R$ on a held-out dataset. We can use this accuracy $R$ as the reward signal and use reinforcement learning to train the controller

# See also

# References
* Zoph, Barret, and Quoc V. Le. "Neural architecture search with reinforcement learning." arXiv preprint arXiv:1611.01578 (2016).