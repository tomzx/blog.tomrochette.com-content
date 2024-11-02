---
title: David Silver - Mastering the game of Go without human knowledge (2017)
created: 2017-10-20
taxonomy:
  tag: [Machine learning]
  status: finished
---

## Context

## Learned in this study

## Things to explore
* How is AlphaGo Zero different from natural selection/evolution?

# Overview
* The architecture from AlphaGo is simplified, merging the policy and value network into a single network

# Notes
## Reinforcement learning in AlphaGo Zero
* A deep neural network $f_\theta$ with parameters $\theta$
* The neural network takes as an input the raw board representation $s$ of the position and its history, and outputs both move probabilities and a value, $(p, v) = f_\theta(s)$
* The vector of move probabilities $p$ represents the probability of selecting each move $a$, $p_a = \Pr(a|s)$
* The value $v$ is a scalar evaluation, estimating the probability of the current player winning from position $s$
* Combines both the roles of policy network and value network into a single architecture
* The neural network consists of many residual blocks of convolutional layers with batch normalization and rectifier nonlinearities
* In each position $s$, an MCTS search is executed, guided by the neural network $f_\theta$
* The MCTS search outputs probabilities $\pi$ of playing each move
* The main idea of our reinforcement learning algorithm is to use these search operators repeatedly in a policy iteration procedure: the neural network's parameters are updated to make the move probabilities and value $(p, v) = f_\theta(s)$ more closely match the improved search probabilities and self-play winner $(\pi, z)$
* Each edge $(s, a)$ in the search tree stores a prior probability $P(s, a)$, a visit count $N(s, a)$, and an action value $Q(s, a)$
* Each simulation starts from the root state and iteratively selects moves that maximizes an upper confidence bound $Q(s, a) + U(s, a)$, where $U(s, a) \propto P(s, a) / (1 + N(s, a))$, until a leaf node $s'$ is encountered
* MCTS may be viewed as a self-play algorithm that, given neural network parameters $\theta$ and a root position $s$, computes a vector of search probabilities recommending moves to play, $\pi = \alpha_\theta(s)$, proportional to the exponentiated visit count for each move, $\pi_a \propto N(s, a)^{1/\tau}$, where $\tau$ is a temperature parameter
* First, the neural network is initialized to random weight $\theta_0$. At each subsequent iteration $i \ge 1$, games of self-play are generated
* At each time-step $t$, an MCTS search $\pi_t = \alpha_{\theta_{i-1}}(s_t)$ is executed using the previous iteration of neural network $f_{\theta_{i-1}}$ and a move is played by sampling the search probabilities $\pi_t$
* A game terminates at step $T$ when both player pass, when the search value drops below a resignation threshold or when the game exceeds a maximum length

## Conclusion
* A pure reinforcement learning approach is fully feasible
* A pure reinforcement learning approach requires just a few more hours to train, and achieves much better asymptotic performance, compared to training on human expert data

# See also

# References
* Silver, David, et al. "Mastering the game of go without human knowledge." Nature 550.7676 (2017): 354.
