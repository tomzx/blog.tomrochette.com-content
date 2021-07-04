---
title: Temporal multi-armed bandits
created: 2021-07-04
taxonomy:
  category: [Machine learning]
  status: in progress
---

# Variations
* With preference for recently chosen arm
* With preference with least recently chosen arm

# Notes
* In some cases where you have a lot of arms to choose from and very few evaluation for each of them (less than 5), with many more arms which have never been chosen, you need a strategy to pick from those arms
	* One option is to use contextual bandits and provide some information you may have about the options you've never explored (e.g., the number of people who picked the arm in the past, the average reward)
		* In my use case, I'm trying to decide which book to read next. We can translate the previous example as the number of people who have read the book and the average rating of the book
