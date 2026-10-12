---
title: Mini-SWE-agent
created: 2026-10-10
updated: 2026-10-11
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, cli, coding-agent, research, swe-bench, minimalism]
readability: 3
audience_notes: >
  Engineers and researchers who want the smallest harness that still solves repository issues, and anyone choosing a baseline agent for evaluation work.
  Assumes you know what SWE-bench and a system prompt are.
---

Mini-SWE-agent is the SWE-bench team's deliberately minimal coding agent, a roughly hundred-line Python loop around a bash shell that its own parent project now points new users to.

## What it is

A terminal CLI (`mini`), a batch SWE-bench runner, a trajectory inspector, and Python bindings, all MIT-licensed and installed from PyPI as `mini-swe-agent`.
It is built by the Princeton and Stanford team behind SWE-bench and SWE-agent, and its design point is subtraction: the model gets a shell, a fixed system template, and nothing else, so the harness disappears from the measurement.
Models arrive through litellm, OpenRouter, or Portkey, and execution runs locally or inside docker/podman, singularity/apptainer, bubblewrap, Contree, or Modal environments.
This is version 2, a rewrite documented in a migration guide from the v1 that first made the hundred-line claim.

## Status

Active and heavily used, mostly out of sight: 8,411 stars, pushed 2026-10-06, on a repository created 2025-06-28 (GitHub API, as of 2026-10-12), with v2.4.6 (2026-07-23) still the latest release (verified 2026-10-12).
PyPI counted 11,605,679 downloads in the last month as of 2026-10-12, which is batch-evaluation traffic, not desktop installs.
The parent `SWE-agent` repository (20,526 stars, last release v1.1.0 in May 2025, default branch last pushed 2026-07-16) carries a README notice saying most development effort has moved to mini-swe-agent and recommending it going forward, so the lineage has formally superseded its ancestor.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=SWE-agent/mini-swe-agent&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=SWE-agent/mini-swe-agent&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=SWE-agent/mini-swe-agent&type=date&legend=top-left" />
</picture>

The team claims over 74 percent on SWE-bench Verified with Gemini 3 Pro, and a self-reported adoption list spanning Meta, NVIDIA, IBM, Anyscale, Essential AI, and Nebius.
The independent-footprint signal is thin in the other direction: its Show HN drew 7 points in July 2025, so the adoption argument rests on the download counter and the team's name, not community discussion.

## Strengths

- **The whole harness fits in your head, which is exactly what a baseline needs.**
- The strongest batch-evaluation surface in this section: SWE-bench runs, trajectory files, an inspector, and Python bindings for subclassing the loop.
- Broad model reach through litellm, OpenRouter, and Portkey, including local servers through litellm's `api_base`.

## Cautions

- Nothing else ships: no subagents, no MCP, no IDE integration, no hooks, no rules files, because the point is the baseline, not the daily driver.
- The hundred-line pitch has drifted: the v2 core agent file is 190 lines, and the package around it is far larger than the marketing line suggests.
- The release train has been quiet since v2.4.6 on July 23, 2026, and the adoption list is self-reported.

## Pricing

Free and MIT-licensed via PyPI.
There is no paid tier; you bring your own provider API keys, so the only cost is the tokens your provider charges.

## Compared to

- [Pi](../pi/index.md): the other deliberate-minimalism bet, but a polished daily-driver TUI with extensions, where mini is a research loop you are meant to read and rewrite.
- [Claude Code](../claude-code/index.md): the platform benchmark this project measures against, closed and feature-complete where mini is open and bare.
- SWE-agent (no note): the heavier ancestor whose config-driven search and interface mini deliberately deletes; use it only when you need its tool scaffolds rather than the shell.

## Bottom line

Recommended for researchers who need a readable baseline harness and for teams running batch evaluations.
Not for daily driving, and not for anyone who needs subagents, MCP, or editor integration, because none of it exists here by design.

## Changes

- 2026-10-10 - Created from the awesome-ai-coding-tools scan, admitted as the live carrier of the SWE-agent lineage that its parent repository now supersedes.

## See also

- [Pi](../pi/index.md) - the other frozen-core minimalism bet, with the extension system mini refuses to have
- [Zerostack](../zerostack/index.md) - the footprint bet in a Rust binary, likewise stripped by stance
- [Claude Code](../claude-code/index.md) - the platform benchmark whose results these minimal harnesses contextualize
- [Harness Feature Matrix](../harness-feature-matrix/index.md) - the capability comparison this column joins

## References

- https://mini-swe-agent.com/latest/ - the overview: hundred-line pitch, v2, adoption claims, and the over-74-percent SWE-bench Verified claim
- https://mini-swe-agent.com/latest/faq/ - model support through litellm and OpenRouter, API key handling, and the FAQ frame for mini versus SWE-agent
- https://mini-swe-agent.com/latest/models/local_models/ - local models through litellm `api_base` with the vLLM and Ollama examples
- https://api.github.com/repos/SWE-agent/mini-swe-agent - 8,411 stars, MIT, created 2025-06-28, pushed 2026-10-06, as of 2026-10-12
- https://api.github.com/repos/SWE-agent/mini-swe-agent/contents/src/minisweagent/agents/default.py - the v2 core agent file at 190 lines, grounding the pitch-drift caution
- https://api.github.com/repos/SWE-agent/SWE-agent - the ancestor's 20,526 stars and v1.1.0 last release
- https://api.github.com/repos/SWE-agent/SWE-agent/readme - the supersession notice pointing development effort to mini-swe-agent
- https://pypistats.org/api/packages/mini-swe-agent/recent - 11,605,679 downloads in the last month as of 2026-10-12
- https://hn.algolia.com/api/v1/items/44682897 - the 7-point Show HN, cited as the thin independent-footprint signal
