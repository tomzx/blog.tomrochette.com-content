---
title: Diablo
created: 2018-12-29
taxonomy:
  type: post
  status: draft
  tag: [games]
---

A table of probabilities is built
The ratio 1/drop chance is used to compute a total drop chance
A number is generated in the range 0-total drop chance
A table lookup is done to find the associated item
Item properties are randomly rolled
Different table lookup may be built depending on the difficulty setting as well as the current act
The rarity of an enemy pack may either change the random generator distribution or some other mean to modify the probability of higher quality items from dropping
The pseudo random number generator is initialized each game and does not depend on the current time (to avoid issue with reading some timer which may have the same value over many iterations or may be slow to read)
When an enemy is killed, we want to determine how many items will drop
