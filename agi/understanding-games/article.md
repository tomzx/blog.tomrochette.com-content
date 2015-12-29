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
* Real Time Strategy (Starcraft 2)
* First Person Shooter (Counter-Strike, Halo, Battlefield, CoD)
* Simulation/Sandbox (Minecraft, Sims)
* (MMO)RPG (WoW, Dark Souls)
* MOBA (LoL, Dota 2)
* Platformers (Super Mario, Sonic, Mega Man)
* Action/Adventure (Zelda)

## Learned in this study

## Things to explore

# Overview

# Real Time Strategy

# First Person Shooter

# Simulation/Sandbox

# (MMO)RPG

# MOBA

# Platformers

Platformers are an interesting genre because they can easily be seen as a path through a level that needs to be optimized. If we take a game such as Super Mario Bros., we only have obw real constraint: we must finish the level before the given 300 seconds (5 minutes). Using this single constraint though makes it hard to give it a purpose to our AGI. Thus, we need to add a couple more constraints/goals.

In order to make the levels more challenging, other constraints such as not dying to enemies of falling into holes are part of the game.

If we look at the game from a reward/punishment point of view, we would reward the AGI for going as far as possible in the level within the least amount of time. Every time the player the AGI controls ends up falling in a hole and dying or touching an enemy and dying or losing its tall Mario aspect, punishment would be applied as we want to avoid these circumstances.

By providing the AGI with a couple of do/do not, it is possible for us to let it learn on its own through reinforcement learning.

In my article [Mari/o](../mario), I write on the topic of [Neuroevolution of augmenting topologies](https://en.wikipedia.org/wiki/Neuroevolution_of_augmenting_topologies). NEAT is a genetic algorithm which goal is to generate and improve artificial neural networks in order to best respond to some selection criteria (generally a single evaluation metric).

The algorithm works similarly to how a reinforcement algorithm would work, in the sense that it will promote genes/neural networks which better suit the goal given to it. In this particular exercise, the only reward that was given was based on how far Mario had move to the right (toward the end of the level goal).

The game was basically replaced by a 13x13 grid where there exist 2 types of blocks: white to represent the ground and black to represent enemies or sprites. Thus, the NEAT algorithm was learning to play a dumbed down version of the game

# Action/Adventure

# See also
