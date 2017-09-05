---
title: Understanding games
created: 2015-10-25
taxonomy:
  category: [Artificial General Intelligence]
  status: draft
---

## Context
Games are complex, self-contained environment from which an AGI can learn. Games most often have a user interface and a set of rules, which are generally easily understood by their players. However, is it possible for simple vision algorithms (and maybe more) to understand and extract the mechanics of a game?

I'd like to explore 7 types of games:
* Real Time Strategy (Starcraft)
* First Person Shooter (Counter-Strike, Halo, Battlefield, CoD)
* Simulation/Sandbox (Minecraft, Sims)
* (MMO)RPG (WoW, Diablo, Dark Souls)
* MOBA (LoL, Dota 2)
* Platformers (Super Mario, Sonic, Mega Man)
* Action/Adventure (Zelda)

## Learned in this study

## Things to explore

# Overview

# Real Time Strategy
<tbc></tbc>

# First Person Shooter
<tbc></tbc>

# Simulation/Sandbox
<tbc></tbc>

# (MMO)RPG
<tbc></tbc>

# MOBA
<tbc></tbc>

# Platformers
Platformers are an interesting genre because they can easily be seen as a path through a level that needs to be optimized. If we take a game such as Super Mario Bros., we only have one real constraint: we must finish the level before the given 300 seconds (5 minutes). Using this single constraint though makes it hard for our AGI to learn as there is no clear gradient from the initial state to the final state (you would have to wait 5 minutes for an episode to complete and have the agent negatively rewarded). Thus, we need to add a couple more constraints/goals.

In order to make the levels more challenging, other constraints such as not dying to enemies or falling into holes are part of the game.

If we look at the game from a reward/punishment point of view, we would reward the AGI for going as far as possible in the level within the least amount of time. Every time the player the AGI controls ends up falling in a hole and dying or touching an enemy and dying or losing its tall Mario aspect, punishment would be applied as we want to avoid these circumstances.

By providing the AGI with a couple of do/do not, it is possible for us to let it learn on its own through reinforcement learning.

In my article [Mari/o](../mario), I write on the topic of Neuroevolution of augmenting topologies[^1]. NEAT is a genetic algorithm which goal is to generate and improve artificial neural networks in order to best respond to some selection criteria (generally a single evaluation metric).

The algorithm works similarly to how a reinforcement algorithm would work, in the sense that it will promote genes/neural networks which better suit the goal given to it. In this particular exercise, the only reward that was given was based on how far Mario had move to the right (toward the end of the level goal).

The game was basically replaced by a 13x13 grid where there exist 2 types of blocks: white to represent the ground and black to represent enemies or sprites. Thus, the NEAT algorithm was learning to play a dumbed down version of the game. And yet, it took it many hours to get to the point it would be able to complete the level without dying and its performance was still average at best.

On the surface, the NEAT algorithm appears to learn, however I'd suggest that it is far from that. Instead, what it is doing is trying numerous cases that are part of the search space, supposedly attempting to find a balance between the fitness of evolved solutions and their diversity[^1] which should lead to a better action model for the same number of attempts compared to a random action agent.

One of the major issues with this approach is that it does not "learn" to infer that something is bad. For instance, if a neural network is configured such that if it sees a hole in front of him and that the action should be to walk directly into that hole, and that the agent is punished for that event, it should attempt to propagate this information backward, for instance by putting more emphasis on recently occurred decisions such as "walk right if hole in front" being a negative/bad decision.

# Action/Adventure
<tbc></tbc>

# See also
[^1]: https://en.wikipedia.org/wiki/Neuroevolution_of_augmenting_topologies
