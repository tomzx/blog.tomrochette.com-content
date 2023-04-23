---
title: AutoGPT
created: 2023-04-23
taxonomy:
  category: [Artificial General Intelligence, ChatGPT]
  status: in progress
---

# Notes
* Like any project, before leaving AutoGPT to its own devices, it is important to set both a time and monetary budget. This is to prevent it from running indefinitely and to prevent it from running up a large bill.
* Like any project, as a project manager, it is important to have regular checks to ensure that the project is on track. Leaving AutoGPT unattended may result in ChatGPT being stuck in a prompt-response loop or having ChatGPT working on something completely unrelated.

# Task distribution
Given that ChatGPT will generally produce a list of tasks to produce in order to achieve a goal, it is possible to distribute those tasks to different agents. This is similar to how a project manager would distribute tasks to different people. This is also similar to how a machine learning engineer would distribute tasks to different machine learning models.

Given that current ChatGPT models take between 10 and 20 seconds to respond, high task parallelism will make better use of our rate limit. Assuming we are using the gpt-3.5-turbo model which has a response time of 10s per request (for 512 output tokens and a temperature of 0.7) and we have 3500 RPM, a single agent will run 6 queries per minute. We would be able to run around 580 agents in parallel.
