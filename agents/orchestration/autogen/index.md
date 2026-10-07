---
title: AutoGen
created: 2026-09-27
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, multi-agent, python, microsoft]
readability: 3
audience_notes: >
  Engineers who adopted Microsoft's conversational multi-agent framework and need to know what maintenance mode means for them.
  Assumes you know Python packaging and have used at least one agent framework.
---

AutoGen is Microsoft's Python framework for applications where multiple agents, and humans, talk to each other in conversations to finish tasks, and as of its own README it is in maintenance mode: no new features, community managed, with Microsoft Agent Framework as the designated successor.

**The most instructive fact in this note is that the best-known corporate multi-agent framework reached maintenance mode within three years of launch, and Microsoft's own README now routes new users elsewhere.**

## What it is

A framework where AssistantAgent and UserProxyAgent converse, execute code, and iterate, with the v0.4+ architecture splitting an AgentChat high-level API from a Core event-driven runtime and shipping extensions per model provider.
It is Python (3.10+), installable as `autogen-agentchat` plus `autogen-ext`, with AutoGen Studio as the no-code GUI on top.
The repo sits at 61,253 stars with about 9.3k forks, created 2023-08-18 (GitHub API, as of 2026-10-02).
The published packages remain MIT (autogen-agentchat 0.7.5 on PyPI), while GitHub's license detection on the repo root now reports CC-BY-4.0, a quirk worth knowing before you vendor anything.
Its research lineage is real: the framework came out of Microsoft Research and Pennsylvania State University work on multi-agent conversations.

## Status

Maintenance mode, by its own declaration: the README carries an orange maintenance-mode badge and a caution box stating AutoGen "will not receive new features or enhancements and is community managed going forward".
New users are pointed to Microsoft Agent Framework (MAF), the enterprise successor that merged the AutoGen and Semantic Kernel lines; MAF shows 13,944 stars, MIT, and a push on 2026-10-04 (GitHub API, as of 2026-10-05).

[![Star History Chart](https://api.star-history.com/chart?repos=microsoft/autogen&type=date&legend=top-left)](https://www.star-history.com/?repos=microsoft%2Fautogen&type=date&legend=top-left)

AutoGen's own repo was last pushed 2026-04-15 and its latest release is python-v0.7.5 from 2025-09-30, so the code is stable but frozen.
Microsoft ships a migration guide on Learn, and the README also still carries the v0.2-to-v0.4 migration path, a reminder that this project already survived one breaking rewrite.
The successor is production-ready per the README, which calls MAF 1.0 stable with long-term support and A2A plus MCP interoperability.

## Strengths

- **Conversation as the coordination primitive was the right abstraction for research**, and it made multi-agent experimentation accessible to thousands of teams that could not write their own message loop.
- The v0.4 rewrite was genuine infrastructure work: event-driven core, provider extensions, and observable tracing, done before abandonment rather than after.
- AutoGen Studio gave the no-code crowd a real on-ramp, which fed the 61k stars.
- The code is stable, MIT at the package level, and widely deployed, so existing deployments do not decay quickly.

## Cautions

- **Frozen by its maintainer**: no new features, community management only, and a successor with a different API, so new projects here are dead ends.
- Migration is a rewrite, not an upgrade; the AutoGen-to-MAF guide exists precisely because the abstractions do not map one to one.
- The original launch drew a plagiarism accusation from the CAMEL authors in a small HN thread, which the discussion contested but never cleanly resolved.
- Corporate framework churn is the real lesson: AutoGen users were already migration veterans by the time Microsoft asked them to migrate again, this time to MAF.

## Pricing

Free and open source at the package level; your costs are model bills and whatever Azure services you attach.
Microsoft Agent Framework is likewise MIT and free.

## Compared to

- [MetaGPT](../metagpt/index.md): the pipeline rival; MetaGPT hard-codes a software company, AutoGen gives you conversations you assemble, and both are now past-tense frameworks.
- Microsoft Agent Framework: the successor; choose it for new .NET or Python work that wants Microsoft support, A2A, and MCP, at the cost of restarting your learning curve.
- [Claude Code](../../harnesses/claude-code/index.md): the counterargument from the harness world, where a single well-tooled agent made most conversational multi-agent orchestration unnecessary for coding work.

## Bottom line

Recommended for existing deployments that value stability, and for researchers who want the canonical conversational multi-agent codebase to read.
Not for new projects; start on Microsoft Agent Framework or a non-Microsoft stack entirely.
My disagreeable claim: conversation-first multi-agent programming, the pattern AutoGen mainstreamed, lost to single-agent harnesses for real work, and maintenance mode is Microsoft admitting it.

## Changes

- 2026-09-27 - Created when the owner's GitHub-stars scan surfaced it.
- 2026-10-07 - Added the microsoft/autogen star history chart to the Status section.

## See also

- [MetaGPT](../metagpt/index.md) - the other museum-piece multi-agent framework from the same wave
- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this column joins
- [Claude Code](../../harnesses/claude-code/index.md) - the single-agent harness that outcompeted the conversation pattern
- [Assistant runtimes](../../assistant-runtimes/_index.md) - where its successor's deploy targets live

## References

- https://api.github.com/repos/microsoft/autogen - GitHub API (200): 61,179 stars, pushed 2026-04-15, created 2023-08-18, license detection CC-BY-4.0 (as of 2026-09-27)
- https://raw.githubusercontent.com/microsoft/autogen/main/README.md - maintenance-mode badge, successor pointer, install and migration text (200) (critical source)
- https://github.com/microsoft/autogen/releases - releases (200): python-v0.7.5 latest, published 2025-09-30
- https://microsoft.github.io/autogen/stable/ - official documentation, live (200)
- https://pypi.org/pypi/autogen-agentchat/json - PyPI metadata (200): autogen-agentchat 0.7.5, MIT, Python 3.10+
- https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen/ - Microsoft's AutoGen to MAF migration guide (200)
- https://api.github.com/repos/microsoft/agent-framework - successor repo (200): 13,816 stars, MIT, pushed 2026-09-25 (as of 2026-09-27)
- https://hn.algolia.com/api/v1/items/37926741 - launch thread (200): 163 points, 54 comments, 2023-10-18
- https://hn.algolia.com/api/v1/items/38398775 - plagiarism-accusation thread (200): 8 points, 2023-11-23 (critical source)
- https://hn.algolia.com/api/v1/items/46377537 - Microsoft Agent Framework thread (200): 58 points, 27 comments, 2025-12-24
