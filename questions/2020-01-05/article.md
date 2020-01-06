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
Playing against yourself is more complicated. A perfect recording of your actions may not prove difficult to beat. It may send units to the wrong location on the map, be caught off guard moving to a location while you positioned units in the middle of the path, it may react to an attack the other opponent had sent to its base at one point in the game, etc. It is however a start, one example you can train against.

A lot of players who are invested in the game will do [theorycrafting](https://en.wikipedia.org/wiki/Theorycraft) which is basically to use logic and reasoning in order to assess what to do in specific cases. An AI coach could have been provided the game rules, specifically, which units are weak/strong against other units, and look at the game while you are playing. If you attack your opponent and the AI observe a strong concentration of a specific type of units, and it notices you do not have any of the units that counter this unit type, it may suggest that you start building those as soon as possible. On the other hand, it may also notice that your unit composition is weak against the unit composition of your enemy and suggest units to build to balance your army.

We can see this act of theorycrafting as the equivalent of knowing, at a high level, the strategies and counterstrategies
