---
title: ChatGPT limitations
created: 2023-04-22
taxonomy:
  category: [Artificial General Intelligence, ChatGPT]
  status: in progress
---

## Context

## Learned in this study

## Things to explore
* Collaboration between ChatGPT agents

# Overview
## Execution of actions/behaviors
It does not execute actions, but it can generate text explaining what actions to take. While this is a current limitation that is addressed by plugins, the next logical step is to have ChatGPT execute actions. As an example of a machine learning engineer working on a project, while ChatGPT can help with devising a plan, it cannot execute the plan. If I already have infrastructure and I want help testing different models and hyperparameters, I still need to write the necessary prompts for ChatGPT, verify the code implements my desired intent, copy the generated code, execute it, and then analyze the results. Furthermore, any execution of machine learning code can take from minutes to hours to execute. In other words, while it helps me reduce the amount of time spent on certain tasks such as reflecting, generating a plan, writing code, because it does not execute those, I am still left with doing them myself.

See [Produce a classification model](../produce-a-classification-model/article.md)

## Recognizing proper responses/behaviors
While it generates text responses, it is not always clear whether those responses are appropriate and whether they will lead to the desired outcome. For the sake of this argument, we could imagine ChatGPT returning as a task to generate a program that will execute a `while true` loop. This indicates that we need to set a timeout on any execution of code as to prevent it from getting stuck at a given step. We may alternatively run steps outside of the main execution loop. We however will need to find a way to increase the timeout when necessary if execution requires it (e.g., training a machine learning model that takes hours). Here we're already faced with the [halting problem](https://en.wikipedia.org/wiki/Halting_problem).

## Remembering prior conversations
It is common to ask ChatGPT to behave a certain way in order to modulate its output. While this may work for a few prompts, ChatGPT will soon revert to its default behavior, forgetting to respect whatever constraint you might have imposed on it in prior prompts.

## Rate limits
While only a technical limitation, if you plan on running many agents in parallel you will need to consider the rate limits imposed. Ignoring the two first levels (free trial users and pay-as-you-go users for the first 48 hours), you will be able to send 3500 requests per minute and 90000 tokens per minute.

# Notes

# See also

# References
* [Produce a classification model](../produce-a-classification-model/article.md)

* https://github.com/Significant-Gravitas/Auto-GPT
* https://github.com/reworkd/AgentGPT
* https://github.com/yoheinakajima/babyagi
