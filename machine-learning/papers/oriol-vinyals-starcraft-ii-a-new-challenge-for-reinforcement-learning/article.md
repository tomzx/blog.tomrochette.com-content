---
title: "Oriol Vinyals - Starcraft II: A New Challenge for Reinforcement Learning (2017)"
created: 2017-10-05
taxonomy:
  tag: [machine learning]
  status: finished
---

## Context

## Learned in this study

## Things to explore

# Notes
## 1 Introduction
* It is a multi-agent problem
* It is an imperfect information game
* The action space is vast and diverse
	* The set of legal actions varies as the player progresses through a tree of possible technologies
* Games typically last for many thousands of frames and actions, and the player must make early decisions with consequences that may not be seen until much later in the game, leading to a rich set of challenges in temporal credit assignment and exploration

## 2 Related Work
* Games offer multiple advantages:
	* They have clear objective measures of success
	* Computer games typically output rich streams of observational data, which are ideal inputs for deep networks
	* They are externally defined to be difficult and interesting for a human to play
	* Games are designed to be run anywhere with the same interface and game dynamics, making it easy to share a challenge precisely with other researchers
	* In some cases a pool of avid humans players exists, making it possible to benchmark against highly skilled individuals
	* Since games are simulations, they can be controlled precisely, and run at scale

## 3 The SC2LE Environment
### 3.1 Full Game Description and Reward Structure
* We define two different reward structure
	* Ternary 1 (win)/0 (tie)/-1 (loss) received at the end of a game
	* Blizzard score
		* It is computed as the sum of current resources and upgrades researched, as well as units and buildings currently alive and being built

### 3.2 Observations
* The main observations come as sets of feature layers which are rendered at $N \times M$ pixels
* Each of these layers represent something specific in the game, for example: unit type, hit points, owner, or visibility
	* Some of these are scalars, while others are categorical
* There are two sets of feature layers:
	* The minimap is a coarse representation of the state of the entire world
	* The screen is a detailed view of a subsection of the world corresponding to the players on-screen view
* Feature layers are rendered via a camera that uses a top down orthographic projection
	* It means the feature layer rendering does not quite match what a human would see

### 3.3 Actions
* An action $a$ is represented as a composition of a function identifier $a^0$ and a sequence of arguments which that function identifier requires: $a^1, a^2, \dots, a^L$

# See also

# References
* Vinyals, Oriol, et al. "StarCraft II: A New Challenge for Reinforcement Learning." arXiv preprint arXiv:1708.04782 (2017).
