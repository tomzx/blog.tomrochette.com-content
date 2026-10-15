---
title: Cole Medin
created: 2026-10-15
updated: 2026-10-15
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, people, publications, video, agentic-engineering, tutorials]
readability: 3
audience_notes: >
  Engineers who learn agent building by building, deciding whether this channel's tutorials and his Archon tool are worth their time.
  Assumes you have used a coding assistant and know what an AI agent is.
---

Cole Medin is the AI-agent educator behind YouTube's largest build-your-own-agent channel and the open-source Archon workflow engine, the video band's tool-shipping tutorial slot.

**His channel teaches agent construction by shipping agent tooling in public, which puts the value in Archon rather than in the videos: the tutorials are beginner-to-intermediate with sponsor reads, while the tool itself is a 23.7k-star MIT project the orchestration category already profiles on its product reality.**

## What it is

A YouTube channel (youtube.com/@colemedin, about 228,000 subscribers as of 2026-10-15) plus a pair of open-source repositories, run by a developer who teaches AI-agent building through code-along builds.
The breakout is [Archon](https://github.com/coleam00/Archon), introduced on 2025-03-03 as "an AI agent that builds AI agents" and iterated in public ever since; the [orchestration category's note](../../orchestration/archon/index.md) records its product reality as a YAML workflow runner over Claude Code, Codex SDK, and local-model harnesses.
The companion [ottomator-agents](https://github.com/coleam00/ottomator-agents) repository collects his reference agent implementations.
His stated upload schedule is at least weekly, Wednesdays on the channel description, and the archive shows 325 videos.

## Status

Active at high cadence as of 2026-10-15.
The Archon repository shows 23,687 stars under the MIT license with a push dated 2026-10-15, so the tool side is under daily development.
The channel is his publication of record: there is no blog or newsletter, and his written record lives in repository documentation and video descriptions.
His agent-domain breakout, the Archon build-in-public series, first surfaced in March 2025, inside this section's coverage window, which is why he qualifies as a new voice rather than an established one pivoting in.

## Strengths

- He ships the thing he teaches: the Archon videos walk a shipped repository through successive versions, so a viewer can diff the claims against the code the same day.
- The build-in-public format shows the failure states most tutorials cut: version pivots, rewrites of the agent-generation approach, and the migration from "agent that builds agents" to workflow runner are all documented on camera.
- The ottomator-agents collection gives his patterns in runnable form, which makes his teaching unusually checkable for the video band.
- His coverage of agent architecture (sub-agents, MCP wiring, task management, knowledge bases) is the most complete free build sequence available on the builder side.

## Cautions

- Tutorial depth stops at beginner-to-intermediate: the videos teach construction patterns, not the verification and evaluation discipline the eval-focused members of this category demand.
- The teaching carries commerce: paid-community (Dynamis) funnels and sponsor segments sit inside the tutorials, so tool recommendations need discounting against members who publish under no-sponsor commitments.
- The tool-first lens cuts both ways: his architectural advice trends toward what a workflow runner can enforce, which reads as product marketing for Archon when the question is which harness to pick.
- The reference repository is aging: ottomator-agents last saw a push on 2025-11-09, so treat it as a snapshot of his patterns rather than a live project.

## Pricing

Free to watch on YouTube.
Revenue comes from a paid community (Dynamis), course funnels, and sponsor segments inside videos; none of the content itself is paywalled.

## Compared to

- [IndyDevDan](../indydevdan/index.md): the two weekly video educators split by object of worship, Dan sells frameworks and a worldview, Medin ships an actual tool; take Dan for the conceptual stack and Medin when you want to read code.
- [Owain Lewis](../owain-lewis/index.md): both are clone-and-run builders, but Lewis builds software factories from existing harnesses while Medin builds the agent tooling layer itself.
- [AI Jason](../ai-jason/index.md): Jason demonstrates finished workflows end to end at slower cadence; Medin teaches the construction underneath at higher cadence with lower polish.

## Bottom line

**Recommended for engineers who learn agent construction by building and want a maintained, starred codebase to follow rather than opinions alone.**
Not for anyone evaluating harnesses or model choices, where his register is tutorial-enthusiast with commerce attached, and not as a substitute for the eval-discipline voices.

## Top 5 recommended reading

- [The OFFICIAL Archon Guide - 10x Your AI Coding Workflow](https://www.youtube.com/watch?v=DMXyDpnzNpY) - The current canonical walkthrough of the tool he ships, from install through the knowledge-and-task workflow that is his actual thesis.
- [Introducing Archon - an AI Agent that BUILDS AI Agents](https://www.youtube.com/watch?v=GjR5UsVGE60) - The 2025-03-03 breakout that named the project, the starting point for his build-in-public method and the version roadmap on camera.
- [Build an ARMY of AI Agents on Autopilot with Archon, Here's How](https://www.youtube.com/watch?v=-Fpp4CBo14g) - The most instructive architecture video: sub-agents, MCP wiring, and multi-service patterns in runnable form.
- [Archon repository](https://github.com/coleam00/Archon) - The tool itself, whose README and version history document the build-in-public process (23,687 stars, MIT, as of 2026-10-15).
- [ottomator-agents repository](https://github.com/coleam00/ottomator-agents) - His reference agent implementations (5,790 stars, MIT), the runnable half of his teaching, read as a November 2025 snapshot.

## Changes

- 2026-10-15 - Created as the video band's tool-shipping tutorial slot, admitted on the in-window Archon breakout (March 2025) with all cited URLs fetched this run.

## See also

- [Archon](../../orchestration/archon/index.md) - the orchestration category's profile of the tool he builds and teaches, including its workflow-runner product reality
- [IndyDevDan](../indydevdan/index.md) - the video band's weekly worldview slot beside his build-the-tool slot
- [Owain Lewis](../owain-lewis/index.md) - the clone-and-run factory builder nearest his format
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the harness landscape his tutorials build on

## References

- https://www.youtube.com/@colemedin - the channel: stated weekly schedule, video archive, and the about-228,000-subscriber footprint (as of 2026-10-15)
- https://github.com/coleam00/Archon - Archon: 23,687 stars, MIT, pushed 2026-10-15, grounding the active status
- https://github.com/coleam00/ottomator-agents - the reference-agents repository: 5,790 stars, MIT, last push 2025-11-09, grounding the snapshot caution
- https://www.youtube.com/watch?v=DMXyDpnzNpY - the Archon guide video, grounding the tutorial format and the sponsor-segment caution
- https://www.youtube.com/watch?v=GjR5UsVGE60 - the 2025-03-03 Archon introduction, grounding the in-window breakout date
- https://www.youtube.com/watch?v=-Fpp4CBo14g - the multi-agent army video, grounding the architecture-teaching strength
