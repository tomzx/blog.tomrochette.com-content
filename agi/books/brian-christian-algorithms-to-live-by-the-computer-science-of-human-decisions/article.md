---
title: Brian Christian - Algorithms to Live By: The Computer Science of Human Decisions - 2016
created: 2017-07-27
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore
* Optimal stopping

# Overview

# Notes
## Introduction
* How can one know that something is the best unless you have a baseline to judge it against?
* The more information you gather, the better you'll know the right opportunity when you see it - but the more likely you are to have already passed by it
* It requires some sort of balance between looking and leaping
* You should spend 37% of your time exploring options, the rest of the time is about finding the best options
* The algorithms that researchers have developed to solve the hardest classes of problems have moved computers away from an extreme reliance on exhaustive calculation. Instead, tackling real-world tasks requires being comfortable with chance, trading off time with accuracy, and using approximations

## 1 Optimal Stopping
* When have you met enough people to know who your best match is?
* What if acquiring the data costs you that very match?
* The optimal solution takes the form of what we'll call the Look-Then-Leap Rule: You set a predetermined amount of time for "looking" - that is, exploring your options, gathering data - in which you categorically don't choose anyone, no matter how impressive. After that point, you enter the "leap" phase, prepared to instantly commit to anyone who outshines the best applicant you saw in the look phase
* In the face of slim pickings, lower your standards. With more fish in the sea, raise them
* The overall rate at which people found the best possible applicant was pretty good: about 31%, not far from the optimal 37%
* For people there's always a time cost (which makes them stop earlier than when optimal)
* Neil Bearden: "After searching for a while, we humans just tend to get bored. It's not irrational to get bored, but it's hard to model that rigorously."

## 2 Explore/Exploit
* Exploration is gathering information, exploitation is using the information you have to get a known good result
* In computer science, the tension between exploration and exploitation takes its most concrete form in a scenario called the "multi-armed bandit problem"
* The explore/exploit tradeoff isn't just a way to improve decisions about where to eat or what to listen to. It also provides fundamental insights into how our goals should change as we age, and why the most rational course of action isn't always trying to choose the best

### Regret and Optimism
* Regret is the result of comparing what we actually did with what would have been best in hindsight
* Assuming you're not omniscient, your total amount of regret will probably never stop increasing, even if you pick the best possible strategy - because even the best strategy isn't perfect every time
* Regret will increase at a slower rate if you pick the best strategy than if you pick others; what's more, with a good strategy regret's rate will go down over time, as you learn more about the problem and are able to make better choices
* The minimum possible regret - again assuming non-omniscience - is regret that increases at a logarithmic rate with every pull of the handle
* In a multi-armed bandit problem, an Upper Confidence Bound algorithm says, quite simply, to pick the option for which the top of the confidence interval is highest
* An Upper Confidence Bound algorithm doesn't care which arm has performed the best so far; instead, it chooses the arm that could reasonably perform best in the future
* Upper Confidence Bound algorithms implement a principle that has been dubbed "optimism in the face of uncertainty"
	* By focusing on the best that an option could be, given the evidence obtained so far, these algorithms give a boost to possibilities we know less about

# See also

# References
* https://en.wikipedia.org/wiki/Optimal_stopping