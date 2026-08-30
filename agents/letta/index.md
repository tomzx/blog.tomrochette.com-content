---
title: Letta
created: 2026-08-24
updated: 2026-08-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, agent-memory, agent-frameworks]
readability: 3
audience_notes: >
  Engineers tracking agent-memory architecture, assumed to have run at least one coding harness and read the MemGPT idea somewhere.
  Useful both to harness shoppers and to people who only want the design patterns.
---

Letta is the company and platform built by the MemGPT creators: a memory-first coding agent (Letta Code), a cloud/API tier, and a research program on agents that learn.
Facts below verified as of 2026-08-24.

**Letta has the deepest research lineage in agent memory and the least settled product strategy, and I think the pattern it popularized will outlive its current packaging.**

## What it is

Out of UC Berkeley's Sky Computing Lab (founders Charles Packer and Sarah Wooders, advised by Ion Stoica and Joey Gonzalez), the team shipped the MemGPT paper, then a stateful-agent server, and now Letta Code: an Apache 2.0 npm harness where agents persist across sessions and rewrite their own context.
Memory is explicit and white-box: editable "memory blocks", a `/remember` command, sleep-time consolidation ("dreaming"), and MemFS, which tracks agent context in git.
**The design bet is that memory belongs inside the harness as tokens the agent can edit, not in a retrieval service beside it.**
Surfaces now include the CLI, desktop app, chat.letta.com, messaging channels, an Agent SDK, and Letta Cloud.

## Status

**Active, research-first, mid-pivot.**
The `letta-ai/letta` repository (24.4k stars as of 2026-08-24) is now a landing page; the retired V1 API server lives on an unsupported archive branch with no security fixes, which strands self-hosters.
Real development moved to `letta-ai/letta-code` (3.1k stars, 3,202 commits).
The company raised a $10M seed led by Felicis at a $70M post-money valuation in September 2024.
Letta Code launched December 2025 claiming the #1 model-agnostic OSS harness on TerminalBench; its HN thread drew 83 points and 37 comments, respect, not adoption-scale buzz.

## Strengths

- **Memory you can actually inspect**: every block is visible and editable, and `/init` ingests AGENTS.md/CLAUDE.md, so it interoperates with file conventions instead of fighting them.
- The research is real and public: MemGPT, sleep-time compute, context repositories, and memory models form the most coherent learning-over-time agenda in the field.
- Skill learning distills repeated work into markdown skills other agents can reuse.
- Everything is Apache 2.0, and BYOK (including Z.ai and ChatGPT coding plans) works on the free tier.

## Cautions

- **The 24k-star repo is a tombstone**: the artifact most people find first is explicitly not the product, and the archived V1 server should not run in production.
- Product surface churned three times in two years (framework server, SDK, coding agent); each pivot resets the integration investment.
- HN commenters in the launch thread called long-term memory for coding "dubious" and flagged context poisoning as a risk memory systems amplify.
- Community footprint is modest relative to the paper's fame; the ideas spread faster than the software.

## Pricing

Free: BYOK plus 3 stateful agents.
Pro $20/month (up to 20 agents), API plan $20/month plus $0.10 per active agent per month and $0.00015 per second of tool execution, Teams $20 per seat, Enterprise custom, as of 2026-08-24.
**The free tier is genuinely usable because the expensive part (models) is yours.**

## Compared to

- [Mem0](../mem0/index.md): a memory API you bolt on; choose it when your agent framework is already chosen.
- [Zep](../zep/index.md): temporal knowledge-graph memory as a service; choose it over Letta when audit and fact invalidation outrank agent autonomy.
- [Claude Code](../claude-code/index.md): the incumbent harness; choose Letta Code when cross-session learning is the point rather than a bonus.

## Bottom line

**Recommended for engineers who want to study (and hack on) where agent memory is going, and for always-on agents that must accumulate a self.**
Not for teams wanting stable infrastructure: the V1 server burial proves the roadmap can strand you, and my disagreeable claim is that most of Letta's value today is importable, steal the memory-block and sleep-time patterns into a harness you already run.

## See also

- [Mem0](../mem0/index.md) - the API-first alternative and benchmark rival
- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - where a memory-first harness sits in the map
- [Claude Code](../claude-code/index.md) - the session-first incumbent this positions against
- [Codex](../codex/index.md) - the other open harness steering OSS agent expectations

## References

- https://www.letta.com/ - company surface, research timeline, backers
- https://github.com/letta-ai/letta - landing-page status and archived V1 server, stars as of 2026-08-24
- https://github.com/letta-ai/letta-code - the active harness, features, license
- https://www.letta.com/blog/letta-code - the memory-first launch post and TerminalBench claim
- https://arxiv.org/abs/2310.08560 - MemGPT: the paper the field cites
- https://techcrunch.com/2024/09/23/letta-one-of-uc-berkeleys-most-anticipated-ai-startups-has-just-come-out-of-stealth/ - seed round and origin
- https://docs.letta.com/pricing - plan structure as of 2026-08-24
- https://news.ycombinator.com/item?id=46294274 - launch thread with founder answers and skeptic pushback
