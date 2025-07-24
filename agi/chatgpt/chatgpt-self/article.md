---
title: ChatGPT self
created: 2023-07-23
taxonomy:
  tag: [artificial general intelligence, chatgpt]
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
* ChatGPT gets all its information about what to say from the context you provide it. Context tokens are however limited and so it is not possible to feed all past information to ChatGPT for it to remember. While it may be possible to fine-tune a model with all the information you want it to remember, this would require cycles of discuss/fine-tune/discuss, which is not ideal. This seems to point to the necessity of an external system to store and retrieve information from. When the system would receive a prompt from the user, it would first attempt to retrieve any relevant context from the context store and then append it to the prompt before sending it to ChatGPT. ChatGPT would then have more context than only the user prompt, helping it answer using prior knowledge.
* One challenge is context retrieval, i.e., figuring out how to retrieve context and what to return
* Another challenge is context storage, i.e., figuring out what to store (raw conversation, summary, tags, etc.)
	* A raw conversation could be converted into chunks and embeddings created from those chunks

# See also

# References
* https://platform.openai.com/docs/guides/gpt-best-practices/tactic-use-embeddings-based-search-to-implement-efficient-knowledge-retrieval
