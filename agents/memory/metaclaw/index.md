---
title: MetaClaw
created: 2026-10-02
updated: 2026-10-03
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, memory, meta-learning, skill-evolution, assistant-runtime]
readability: 3
audience_notes: >
  Engineers running OpenClaw-family assistant agents who want the agent's memory and skills to improve automatically from conversations.
  Assumes you know what a coding or personal agent harness is; RL details are explained inline.
---

MetaClaw is an MIT-licensed meta-learning layer that sits in front of OpenClaw-family assistant agents and evolves their skills and cross-session memory from everyday conversations, with optional reinforcement-learning updates scheduled into idle hours.

**Its bet is that agent improvement should be a background process the user never operates: talk normally, and a memory layer plus sleep-time training turns each conversation into better skills and recall.**

## What it is

A CLI (`metaclaw setup`, then `metaclaw start`) from an academic lab (aiming-lab) with a technical report that ranked first on Hugging Face Daily Papers in March 2026.
It wraps multiple assistant harnesses (OpenClaw, IronClaw, PicoClaw, ZeroClaw, CoPaw, NanoClaw, NemoClaw) and runs in three modes: skills-only, reinforcement-learning-only, or auto (skills plus scheduled RL).
The RL path trains against Tinker or MinT backends over APIs, so no GPU cluster is required, and slow updates only run during sleep hours, idle time, or calendar meetings, with support/query separation to keep stale rewards out.
The memory side persists cross-session context per user and project (facts, preferences, history retrieved into prompts), ingests turns incrementally instead of at session end, and ships as a one-click OpenClaw extension.

## Status

Dormant-leaning: v0.4.1 released 2026-04-11 and no repository push since 2026-06-07 as of 2026-10-03, roughly four months quiet.
**The attention record is unusual: first place on Hugging Face Daily Papers and 3,455 stars, but no Hacker News discussion at all, so the buzz came from the paper ranking rather than user adoption.**
A research artifact with a real feature history through April, then silence; treat it as a promising experiment on pause, not maintained infrastructure.

## Strengths

- The mode menu is genuinely useful: skills-only mode improves behavior with no training stack at all, while auto mode adds scheduled RL for people who want it.
- Sleep-hours training with support/query separation addresses the two classic continual-learning failures, catastrophic overwriting and stale reward signals, at the scheduler level.
- Incremental memory ingestion (every five turns by default) shrinks the mid-session blackout window most memory layers have.
- Multi-claw support means one learning layer covers most of the OpenClaw-family ecosystem, not a single harness.
- The paper plus reproducible CLI is a legible research artifact: claims are checkable against the report.

## Cautions

- Four months without a push and no release since April: the OpenClaw family it wraps moves fast, and pinned integration points rot.
- RL quality is only as good as the reward signals scraped from conversations, and the note-sized documentation does not include field results beyond the paper's own benchmarks.
- Academic-project risk: the lab's roadmap, not users, decides whether v0.5 ever happens.
- The daily-papers ranking measures paper attention, not deployment safety; nothing here is audited for the failure modes of an agent that rewrites its own skills.
- No independent community footprint: no HN threads, no third-party writeups found.

## Pricing

Free and open source under MIT.
Skill-only mode costs nothing beyond your model APIs; RL mode adds the Tinker or MinT training API as a separate bill. No GPU purchase required.

## Compared to

- [claude-mem](../claude-mem/index.md): session-memory compression for Claude Code specifically; MetaClaw is cross-claw and adds training, not just recall.
- [Cognee](../cognee/index.md): knowledge-graph memory pipelines for applications; MetaClaw closes the loop by feeding learned skills back into the agent.
- [OpenClaw](../../assistant-runtimes/openclaw/index.md): the harness MetaClaw most directly extends; use OpenClaw alone for capability, add MetaClaw for automatic improvement.

## Bottom line

**Recommended for OpenClaw-family users and researchers who want a working, cited starting point for self-improving agent memory and skills.**
Not for production assistants (the project is dormant and unaudited), or anyone who needs a maintained dependency.

## Changes

- 2026-10-02 - Created.

## See also

- [Memory Feature Matrix](../memory-feature-matrix/index.md) - the category comparison this note joins
- [claude-mem](../claude-mem/index.md) - the single-harness session-memory alternative
- [Cognee](../cognee/index.md) - the knowledge-graph memory pipeline alternative
- [OpenClaw](../../assistant-runtimes/openclaw/index.md) - the primary harness this layer extends
- [File-based agent memory](../file-based-agent-memory/index.md) - the zero-infrastructure memory pattern this automates

## References

- https://github.com/aiming-lab/MetaClaw - repository, MIT license, modes, multi-claw support, memory layer, and the push record as of 2026-10-03
- https://arxiv.org/abs/2603.17187 - the technical report "MetaClaw: Just Talk" grounding the meta-learning and RL-scheduling claims
- https://huggingface.co/papers/2603.17187 - the Hugging Face Daily Papers ranking (first place, March 2026) behind the attention claim
- https://github.com/aiming-lab/MetaClaw/releases - the v0.4.1 release (2026-04-11) anchoring the version and dormancy timeline
- https://github.com/aiming-lab/MetaClaw/blob/main/README.md - the mode documentation, incremental-memory changelog, and OpenClaw plugin path
