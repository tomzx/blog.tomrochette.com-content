---
title: Lilian Weng (Lil'Log)
created: 2026-08-29
updated: 2026-08-29
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=big-pickle, people, publications, research, agents, reference]
readability: 3
audience_notes: >
  Engineers who want the clearest written reference for the concepts behind agents, prompted models, and reasoning, before going deeper into papers.
  Assumes you can read technical writing and want a survey-level map rather than hands-on tooling.
---

Lil'Log, the blog of Lilian Weng, is the reference-quality written map of how large language models and autonomous agents actually work, maintained by a former OpenAI research and safety leader.
Facts below verified as of 2026-09-05.

**Her "LLM Powered Autonomous Agents" post is the canonical survey of agent architecture, the planning, memory, and tool use decomposition that nearly every later engineering discussion of agents cites.**

## What it is

A long-running technical blog by Lilian Weng, a machine learning researcher who served as Vice President of Research and Safety at OpenAI and now works at OpenAI on alignment and safety.
She has documented her learning notes there since 2017.
The famous [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) post from June 2023 lays out the planning, memory, and tool use components of an agent with the LLM as its controller.

## Status

Active, though at a low and variable frequency as of 2026-09-02.
The most recent post, "Harness Engineering for Self-Improvement" (2026-07-04), is directly on-topic for this section, discussing recursive self-improvement and the harnesses that let a model improve its own pipeline.
The blog moved to the lilianweng.github.io repo; the older lilianweng/lil-log repo is marked deprecated.

## Strengths

- The posts are dense, reference-laden surveys that map an entire subfield, so they function as durable citation anchors.
- She writes with unusual clarity about research that most practitioners only meet as buzzwords, from reasoning to reward hacking to inference optimization.
- She is frank about model limitations, including reliability problems and adversarial attacks, which makes the survey a useful skeptical baseline.
- The LLM-powered-agents post is the reference that agentic engineering discussions keep returning to, which is why it still matters three years on.

## Cautions

- Cadence is slow and irregular, so it is a reference to consult, not a feed to follow for current events.
- The writing is survey-level and research-oriented, not hands-on tooling guidance.
- Much of her public writing predates the current agentic-development-tool era, so readers need to map concepts to current harnesses themselves.
- She is a frontier-lab insider writing on alignment and safety, so the framing reflects that vantage point rather than the open-source practitioner's.

## Pricing

Free to read.
No paywall and no commercial model.

## Compared to

- [Andrej Karpathy](../andrej-karpathy/index.md): both are frontier-lab researchers who write reference material, but Karpathy sets vocabulary while Weng documents the research canon; read Weng for the mechanism, Karpathy for the framing.
- [Chip Huyen](../chip-huyen/index.md): both cover foundations, but Huyen writes the production systems view while Weng writes the research view.
- [Nathan Lambert](../nathan-lambert/index.md): both explain the model-and-agent research layer, but Lambert focuses on post-training and open models while Weng spans the broader agent and alignment research.

## Bottom line

**Recommended for any engineer who wants to understand the mechanism under an agent, a reasoning model, or a reward-hacking story, because the posts are the clearest written references available.**
Not for practitioners who want current tooling guidance or a daily feed.

## See also

- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - the current harnesses that realize the agent architecture she surveys
- [Context Management Patterns](../context-management-patterns/index.md) - the memory and tool use components of her agent decomposition, made concrete
- [Andrej Karpathy](../andrej-karpathy/index.md) - the companion frontier-research vocabulary-setter
- [Scaling the LLM Agent Company](../../scaling-the-llm-agent-company/index.md) - the supervision problem that her reasoning about autonomous agents implies

## References

- https://lilianweng.github.io/ - the Lil'Log homepage with the post archive and her OpenAI affiliation
- https://lilianweng.github.io/posts/2023-06-23-agent/ - "LLM Powered Autonomous Agents", the canonical agent survey
- https://lilianweng.github.io/posts/2026-07-04-harness/ - the July 2026 post on harness engineering for self-improvement
- https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/ - her adversarial attack and jailbreak survey, a skeptical baseline
- https://www.antoinebuteau.com/lessons-from-lilian-weng/ - an independent profile of her work and its influence
