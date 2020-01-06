---
title: AI coach for video games
created: 2020-01-01
taxonomy:
  type: post
  category: [Questions, Artificial Intelligence]
  status: finished
---

# Question
How would you build an AI that does coaching for games like StarCraft or Dota/LoL?

# Answer
I see coaching as similar to the loss function of a machine learning model. I also see coaching as trying to optimize a function by figuring out where the largest improvements can be made. In a game like Starcraft, that would basically mean pointing out the macro level mistakes a playing is making instead of the micro level mistakes he's making.

To coach you thus need to have a model of what actions have impact on the game, and how much impact they have. A learning algorithm/model like AlphaZero generally exhibits two types of learning: learning from observation and learning by playing against itself.

## Learning from observation
In the first phase, the model simply observes what happens during gameplay. In competitive games, the only reward signal is the victory/loss at the end of a game.

The model will need at some point to be able to establish its own scoring system so it can give itself some intermediate rewards. It will also need to learn how to segment a sequence of actions into repeatable units such as constructing unit X, attacking playing Y, defending zone Z.

## Learning by playing against yourself
