---
title: Volodymyr Mnih - Playing Atari with Deep Reinforcement Learning (2013)
created: 2016-03-09
taxonomy:
  tag: [machine learning]
  status: finished
---

## Context

## Learned in this study

## Things to explore

# 1 Introduction
* Reinforcement learning algorithms must be able to learn from a scalar reward signal that is frequently sparse, noisy and delayed
* The delay between actions and resulting rewards can be thousands of timesteps apart
* Most deep learning algorithms assume the data samples to be independent, while in reinforcement learning we typically encounter sequences of highly correlated states
* In reinforcement learning, the data distribution changes as the algorithm learns new behaviors
* The paper presents a convolutional neural network that is trained using a variant of the Q-learning algorithm, with stochastic gradient descent to update the weights
* The challenge is to learn control policies from raw video data
* The goal is to create a single neural network agent that is able to successfully learn to play as many of the games as possible (games for the Atari 2600)

# 2 Background
* $\mathcal{E}$: The environment
* $a_t$: An action at time $t$
* $\mathcal{A} = \{1, ..., K\}$: A set of legal game actions
* $x_t \in \mathbb{R}^d$: An image from the emulator at time $t$
* $r_t$: A reward representing the change in game score at time $t$
* $s_t = x_1, a_1, x_2, a_2, ..., a_{t-1}, x_t$: A sequence of actions and observations used to learn game strategies that depend upon these sequences
* Q-network: A neural network function approximator with weight $\theta$

# 4 Deep Reinforcement Learning
* Use of experience replay
	* Store the agent's experiences at each time step, $e_t = (s_t, a_t, r_t, s_{t+1})$ in a data set $\mathcal{D} = e_1, ..., e_N$

# 4.1 Preprocessing and Model Architecture
* Preprocessing done to reduce the input dimensionality
	* 128 color palette converted to gray-scale representation
	* Frames are down-sampled from 210 x 160 pixels to 110 x 84 pixels
	* The final input is obtained by cropping a 84 x 84 pixels region that roughly captures the playing area
		* This cropping is done in order to use the GPU implementation of 2D convolutions which expects square inputs
* The input to the neural network is a 84 x 84 x 4 image (84 x 84 pixels x 4 last frames)
* The first hidden layer convolves 168 x 8 filters with stride 4 and applies a rectifier nonlinearity
* The second hidden layer convolves 324 x 4 filters with stride 2, again followed by a rectifier nonlinearity
* The final hidden layer is fully-connected and consists of 256 rectifier units
* The output layer is a fully-connected linear layer with a single output for each valid action

# 5 Experiments
* Tested on Beam Rider, Breakout, Enduro, Pong, Q*bert, Seaquest and Space Invaders.
* No modification to the network architecture, learning algorithm or hyperparameters between games
* Trained on 10 million frames (about 46h at 60 frames/second)
* The agent sees and selects actions on every $k^{th}$ frame instead of every frame and its last action is repeated on skipped frames
* k = 4 was used for all games except Space Invaders (due to the beams not being visible on those frames)

# See also
* [Mari/o](../../../agi/mario/article.md): Conceptual use of the replay system

# References
* Mnih, Volodymyr, et al. "Playing atari with deep reinforcement learning." arXiv preprint arXiv:1312.5602 (2013).
* http://arxiv.org/abs/1312.5602
