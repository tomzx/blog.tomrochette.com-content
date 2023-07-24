---
title: ChatGPT self
created: 2023-07-23
taxonomy:
  category: [Artificial General Intelligence, ChatGPT]
  status: in progress
---

## Context
The goal of this study is to reflect on ways to implement a prompt or enough context such that ChatGPT could accurately act as you.

## Learned in this study

## Things to explore

# Overview

# Notes
* As of 2023-07-23 (with both gpt-3.5 and gpt-3.5-turbo-16k), providing your own personal description as part of the system prompt or initial user prompt will quickly result in ChatGPT not using said prompt context anymore. In simple tests, after 1 user-assistant interaction, ChatGPT has already forgotten it's impersonating someone and indicates its an AI.

## Probing
* By asking questions to the model you can identify parts of its personality that doesn't match yours. With this knowledge in hand, you can add more information to the original context you provide to ChatGPT

### Probing questions
* What do you like/dislike?

## Context
* ChatGPT gets all its information about what to say from the context you provide it. Context tokens are however limited and so it is not possible to feed all past information to ChatGPT for it to remember. While it may be possible to fine-tune a model with all the information you want it to remember, this would require cycles of discuss/fine-tune/discuss, which is not ideal.

# See also

# References
