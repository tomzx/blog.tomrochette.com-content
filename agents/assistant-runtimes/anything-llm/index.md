---
title: AnythingLLM
created: 2026-09-27
updated: 2026-10-06
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, assistant-runtimes, local-first, rag, desktop-apps]
readability: 3
audience_notes: >
  Engineers who need to hand a private local AI workspace to non-engineers, or who are comparing
  self-hosted RAG platforms and want to know what the one-click abstraction hides.
---

AnythingLLM is a local-first, MIT-licensed AI workspace from Mintplex Labs that packages RAG workspaces, an agent runtime, and MCP support into a one-click desktop app, with a multi-user Docker image for self-hosting and paid hosted tiers on top.

**AnythingLLM won the local-AI desktop by hiding the machinery (vector database, embeddings, providers) from the user, and that same choice caps it for engineers: it is the app I hand to non-engineers, not the harness I build on.**

## What it is

An Electron desktop app for macOS, Windows, and Linux, plus a Docker image with multi-user management and permissions, a hosted cloud, and an Android mobile app.
Workspaces are the organizing unit: documents go in, retrieval comes out, and the default LanceDB vector database plus built-in embedding model mean most users never see either.
Providers swap freely between local (Ollama, LM Studio, KoboldCPP, or the built-in engine) and cloud (Anthropic, OpenAI, Gemini, Bedrock, OpenRouter, and more).
The agent layer is substantial: built-in skills for SQL, file systems, Gmail, Google Calendar, Outlook, and scheduled jobs, a no-code Agent Flows builder, MCP compatibility on desktop and Docker, and a Community Hub for sharing skills and connectors.
Beta features push it toward an OS-level assistant: AI computer use and live document sync, plus Magic dictation and screen-aware tools in the Pro tier.

## Status

Active and steadily shipped: 66,739 stars, 7,451 forks, and 321 open issues as of 2026-10-06, created 2023-06-04, pushed the same day.
v1.17.0 was released 2026-10-01, following v1.16.2 (2026-09-22), and the docs changelog shows an unbroken cadence back through v1.6.x.
The founder Tim Carambat introduced the desktop app on Hacker News in September 2024 (368 points), framing the mission as layperson-accessible private AI, and the thread is a useful record of both praise and the first round of critiques.
The repo's own topics now include computer use and agent harness terms, which tells you the center of gravity has moved from document chat to agents.

## Strengths

- The lowest-friction install in this category: a consumer laptop, one download, and a working private assistant in minutes.
- Provider and vector database swaps happen in settings, not config files, which is the point.
- Agents, flows, MCP, and scheduled jobs live in the same app, so non-engineers get real automation without a terminal.
- MIT-licensed with a genuine multi-user Docker path for teams that outgrow the desktop.

## Cautions

- The launch-thread critiques still rhyme: citation windows rendered garbled content, and Linux installs needed a root-ownership workaround for the sandbox.
- Hiding retrieval machinery means hiding retrieval quality; engineers debugging a RAG pipeline will miss the knobs.
- The Electron stack is heavy compared with the CLI-first runtimes elsewhere in this category.
- Commercialization is increasingly visible: Pro upsells, hosted tiers, and watermark-free documents as a paid perk, which is fair but worth tracking.

## Pricing

Desktop is free and MIT-licensed; the optional Pro subscription removes daily limits on the Magic features (Echo dictation, Beacon, Tab completion) that all have free tiers.
Hosted AnythingLLM Cloud starts at Basic $50/month for a private instance and Pro $99/month with priority resources and a 72-hour support SLA, with Enterprise custom (as of 2026-09-27).

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09 | Cloud Basic, Cloud Pro, Desktop Pro | Baseline as observed: Cloud Basic $50/mo, Cloud Pro $99/mo, Enterprise custom; Desktop free with opt-in Pro add-on. | [anythingllm.com/pricing](https://anythingllm.com/pricing) |

## Compared to

- [Open WebUI](../open-webui/index.md): the maximalist self-hosted web UI with the heavier license; choose AnythingLLM for simplicity and MIT, Open WebUI for administration depth.
- [Eigent](../eigent/index.md): the Apache-2.0 desktop for supervised multi-agent workforces; choose AnythingLLM for single-player polish, Eigent for parallel specialist agents.
- [Hermes](../hermes/index.md): the learning-loop runtime sibling in this category; choose it when the assistant should improve from use rather than serve documents.

## Bottom line

**Recommended as the default way to give non-engineers a private, local, multi-provider AI workspace.**
Not for engineers who want to inspect and tune the retrieval pipeline themselves.
The disagreeable claim I will defend: the layperson focus that made AnythingLLM popular is exactly why engineers should not pick it for themselves, because the abstraction that removes setup also removes control.

## Changes

- 2026-09-27 - Created when the owner's GitHub-stars scan surfaced it.

## See also

- [Open WebUI](../open-webui/index.md) - the feature-maximal self-hosted rival this note's abstraction contrasts with
- [Eigent](../eigent/index.md) - the multi-agent desktop alternative
- [Hermes](../hermes/index.md) - the learning-loop runtime for engineer-facing use
- [LlamaIndex](../../retrieval/llamaindex/index.md) - the RAG framework layer AnythingLLM internalizes

## References

- https://api.github.com/repos/Mintplex-Labs/anything-llm - stars, forks, issues, license, and dates as of 2026-10-06
- https://github.com/Mintplex-Labs/anything-llm - repository and positioning
- https://api.github.com/repos/Mintplex-Labs/anything-llm/releases?per_page=4 - v1.17.0 released 2026-10-01
- https://docs.anythingllm.com/ - features, agents, MCP compatibility, Docker self-hosting, Community Hub
- https://docs.anythingllm.com/pro/overview - the Pro tier scope and the free-tier commitment
- https://anythingllm.com/pricing - hosted tiers and enterprise contact as of 2026-09-27
- https://news.ycombinator.com/item?id=41457633 - the Show HN thread (368 points), including the citation and sandbox critiques, fetched via the Algolia items API
