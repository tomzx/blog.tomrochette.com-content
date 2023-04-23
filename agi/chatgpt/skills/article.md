---
title: AGI skills
created: 2023-04-22
taxonomy:
  category: [Artificial General Intelligence, ChatGPT]
  status: in progress
---

What are some skills that an AGI based on ChatGPT would need to have?

* Prompt the operator to disambiguate
* Extract instructions/actions from text
* Generate code
* Execute code
* Identify useful behavior that can be reused
* Recognize when we're in a prompt-response loop
	* A prompt-response loop is when we ask ChatGPT something, it responds, we ask it something else, it responds, but not progress is being made. We're stuck in a loop.
	* If we're in a prompt-response loop, we need to be able to break out of it.
	* At a high level, identifying that we're in a prompt-response loop is difficult. We could ask ChatGPT whether it thinks that the last few prompt-response are somewhat identical, and if so, we could ask it to prompt the operator for help.
	* Ideally we would want to avoid having to do prompt-response loop detection, possibly by tracking some form of plan and identifying when we're not making progress towards the next step. This could be done for example, by recording how many prompt-response cycles we've done for a given step of a plan and prompting ChatGPT for a status update.

# References
* [Limitations](../limitations/article.md)
* [Seed AI](../seed-ai/article.md)
* [Setup passive income streams](../setup-passive-income-streams/article.md)
