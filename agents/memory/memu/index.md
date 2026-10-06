---
title: memU
created: 2026-10-06
updated: 2026-10-06
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, memory, agent-memory, file-based, skills]
readability: 3
audience_notes: >
  Engineers who use several agent CLIs (ChatGPT, Claude Code, Cursor, OpenClaw) and want one
  personal memory and skill library that follows them across all of them.
  Assumes you know what a session log and an agent skill are.
---

memU is an Apache-2.0 personal memory layer that stores knowledge as a wiki of markdown files the agent itself distills from session history, shared across sessions, agents, and devices.

**Its bet is that memory quality comes from making the agent do the curating: a scheduled task hands the agent its own session log, and the agent decides what becomes a page, a skill, or nothing.**

## What it is

A lightweight system from NevaMind with a core of about 500 lines, installable through the memu-cli Python package (PyPI 0.10.0).
Each supported host gets an adapter binary that binds two seams: record (a scheduled bridging task slices new session logs into self-contained jobs) and inject (a standing instruction in the host's instruction file tells the agent to retrieve before answering).
The judgment stays inside the agent: it reads related existing pages, then chooses to do nothing, patch a page, or create one, and the service only stores, embeds, and retrieves the markdown.
Automatic skill extraction turns useful history into named markdown skills with workflows, branches, and pitfalls, which any connected agent can retrieve later.
The README's support matrix covers ChatGPT (Work mode), Claude Code, Cursor, OpenClaw, Hermes Agent, and WorkBuddy across macOS, Windows, and Linux.
Deployment is a free hosted service (API key from memu.so, cross-device) or a self-hosted mode (private, single-device, your own embedding key).

## Status

**Quietly large: 14.5k stars rank it seventh of the fourteen members profiled here, while its discussion footprint is nearly empty.**
14,499 stars with the repository pushed 2026-10-01, created 2025-07-29, as of 2026-10-06 (GitHub API).
The Hacker News record is two threads: an 11-point Show HN in January 2026 (4 comments) and a 4-point story in July 2026 (0 comments), so the 14.5k stars rest on trend cycles and word of mouth, not public scrutiny.
Development is active, with the README's host matrix and skill-extraction flow revised against current releases.
The same stars-ahead-of-discussion pattern this section has flagged on Supermemory, Cabinet, and Graphify.

## Strengths

- **The agent does the distilling, so there is no extraction pipeline of yours to run or pay for**: the service stores, embeds, and retrieves, and the judgment is your chosen model's.
- The wiki is plain markdown, so the memory is readable, greppable, and editable by any tool including you.
- Skill extraction is the standout: repeated workflows become named, embedded, retrievable markdown skills that every connected agent shares.
- Broad host coverage for a young project, including ChatGPT and Claude Code on the same memory.

## Cautions

- **The free, unlimited hosted tier is the more capable path, which is an inverted pitch**: self-hosting is single-device and requires your own embedding key, so the multi-device experience currently exists only on infrastructure you do not control.
- Free-unlimited hosted tiers are a beta positioning, and nothing published says what they become when the beta ends.
- Retrieval support is uneven per the README's own matrix (OpenClaw retrieve marked unverified, some host and model combinations flagged with failures).
- The agent both writes and reads the wiki, so memory quality tracks the distilling model, and there is no benchmark or independent evaluation of either.
- Third-party scrutiny is nearly absent: two thin HN threads, no independent writeups found.

## Pricing

Free: the hosted service is free and unlimited as of 2026-10-06, and the self-hosted mode is Apache-2.0 under your own embedding account.
No paid tier is published.

## Compared to

- [File-based agent memory](../file-based-agent-memory/index.md): the convention memU automates; use the convention when you want memory in the repo, memU when you want it across agents and machines.
- [claude-mem](../claude-mem/index.md): session-compression memory bound to coding-agent hooks; memU is cross-agent, wiki-shaped, and skill-producing instead of observation-compressing.
- [Memoryfields](../memoryfields/index.md): both bet on markdown as the canonical store; Memoryfields is a portable format spec with minimal tooling, memU is a working service with the embedding and retrieval built.

## Bottom line

**Recommended for people who live in two or more agent CLIs and want one self-maintaining memory and skill library.**
Not for teams needing multi-user memory APIs, contractual hosting terms, or any independent evidence about memory quality.

## Changes

- 2026-10-06 - Created from the 2026-10-06 entrant scan, with seven fetched sources and the thin-discussion footprint recorded as the critical signal.

## See also

- [Memory Feature Matrix](../memory-feature-matrix/index.md) - the category comparison this note joins
- [File-based agent memory](../file-based-agent-memory/index.md) - the convention this automates and extends across devices
- [claude-mem](../claude-mem/index.md) - the single-harness session-memory alternative
- [Memoryfields](../memoryfields/index.md) - the portable-format sibling with the same markdown bet

## References

- https://github.com/NevaMind-AI/memU - repository, 14,499 stars, push record, license file (Apache-2.0 text), as of 2026-10-06
- https://raw.githubusercontent.com/NevaMind-AI/memU/main/README.md - the record/inject seams, skill-extraction flow, host support matrix with its own limitations, and the hosted-versus-self-host split
- https://memu.pro - product surface: agent-driven memory, cross-agent memory, skill extraction, readable markdown
- https://memu.pro/SKILL.md - the agent-facing install skill: memu-cli install path and the per-host adapter binaries
- https://memu.so - the hosted API-key surface (free, cross-device)
- https://pypi.org/pypi/memu-cli/json - memu-cli 0.10.0
- https://hn.algolia.com/api/v1/items/46511540 - the January 2026 Show HN (11 points, 4 comments), the launch record
- https://hn.algolia.com/api/v1/items/49070470 - the July 2026 story (4 points, 0 comments), the thin-discussion signal
