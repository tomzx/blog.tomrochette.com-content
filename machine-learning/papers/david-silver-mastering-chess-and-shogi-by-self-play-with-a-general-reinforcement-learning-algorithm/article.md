---
title: David Silver - Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm (2017)
created: 2017-12-06
taxonomy:
  tag: [machine learning]
  status: finished
---

## Context

## Learned in this study

## Things to explore

# Overview

# Notes
* Instead of an alpha-beta search with domain-specific enhancements, AlphaZero uses a general-purpose Monte-Carlo tree search (MCTS) algorithm
* The AlphaZero algorithm described in this paper differs from the original AlphaGo Zero algorithm in several respects
	* AlphaGo Zero estimates and optimises the probability of winning, assuming binary win/loss outcomes. AlphaZero instead estimates and optimises the expected outcome, taking into account of draws or potentially other outcomes
	* In AlphaGo Zero, self-play games were generated by the best player from all previous iterations. After each iteration of training, the performance of the new player was measured against the best player; if it won by a margin of 55% then it replaced the best player and self-play games were subsequently generated by this new player. In contrast, AlphaZero simply maintains a single neural network that is updated continually, rather than waiting for an iteration to complete
	* In AlphaZero we reuse the same hyper-parameters for all games without game-specific turning. The sole exception is the noise that is added to the prior policy to ensure exploration; this is scaled in proportion to the typical number of legal moves for that game type
* AlphaZero searches just 80 thousand positions in chess and 40 thousand in shogi, compared to 70 million for Stockfish and 35 million for Elmo
* AlphaZero compensates for the lower number of evaluations by using its deep neural network to focus much more selectively on the most promising variations - arguably a more "human-like" approach to search, as originally proposed by Shannon

# See also

# References
