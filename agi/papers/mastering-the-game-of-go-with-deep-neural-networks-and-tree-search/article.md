---
title: Mastering the Game of Go with Deep Neural Networks and Tree Search
created: 2016-03-09
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview
* Use of deep convolutional neural networks
* The input is the 19 x 19 board
* Use of multiple policies networks
	* $p_\sigma$: Supervised learning
	* $p_\pi$: Fast policy
	* $p_\rho$: Reinforcement learning
* $v_\theta$: Value network, predicts the winner of games played by the RL policy network against itself

# 1 Supervised Learning of Policy Networks
* SL policy network $p_\sigma(a|s)$ alternates between convolutional layers and rectifier non-linearities (similar to what was done in [Playing Atari with Deep Reinforcement Learning](../playing-atari-with-deep-reinforcement-learning))
* A final softmax layer outputs a probability distribution over all legal moves $a$
* The policy network is trained to maximize the likelihood of choosing the human move $a$ when in state $s$
* The SL policy network is 13 layers
* It was trained using 30 million positions from the KGS Go Server
* The "fast" policy, $p_\pi$, was also trained in a similar fashion, it is less accurate but much faster (takes 2μs to select an action vs 3ms for the SL policy network)

# 4 Searching with Policy and Value Networks
* To efficiently combine MCTS (monte carlo tree search) with deep neural network, AlphaGo uses an asynchronous multi-threaded search that executes simulation on CPUs, and computes policy and value networks in parallel on GPUs
* The final version of AlphaGo used
	* 40 search threads
	* 48 CPUs
	* 8 GPUs
* A distributed version of AlphaGo was implemented that exploited multiple machines, 40 search threads, 1202 CPUs and 176 GPUs.

# 5 Evaluating the Playing Strength of AlphaGo
* A tournament was ran among variants of AlphaGo and several other Go programs such as commercial programs Crazy Stone and Zen, open source programs Pachi, Fuego and GnuGo.
* AlphaGo won 494/495 games against other Go programs
* With an handicap of 4 stones, AlphaGo won 77% of games against Crazy Stone, 86% of games against Zen and 99% of games against Pachi
* Distributed AlphaGo won 77% of games against single machine AlphaGo

# 6 Discussion
* Go is examplary in many ways to the difficulties faced by artificial intelligence:
	* a challenging decision-making task
	* an intractable search space
	* an optimal solution so complex it appears infeasible to directly approximate using a policy or value function

# See also
* [The Future of Artificial Intelligence](../../presentations/the-future-of-artificial-intelligence): A presentation by Demis Hassabis which covers some of the content covered in this paper

# Sources
* https://vk.com/doc-44016343_437229031?dl=56ce06e325d42fbc72