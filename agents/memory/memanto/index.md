---
title: Memanto
created: 2026-10-11
updated: 2026-10-11
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, memory, memory-agent, typed-memory, mcp, open-source]
readability: 3
audience_notes: >
  Engineers running several agents who want memory managed for them, profiled against
  the engines that only store and serve. Assumes you know what vector search and MCP are.
---

Memanto is an MIT-licensed memory agent from Moorcheh AI: a second agent that runs beside your fleet and manages its shared memory, deciding what to keep, what conflicts, what expires, and what each agent is briefed with before it acts.

**Its bet is that storage is solved and management is not: consolidation, contradiction handling, and forgetting should run as an agent on a schedule, not as code you write against a memory API.**

## What it is

A CLI-first system (pip install memanto, Python 3.10+) with Python, TypeScript, and Go SDKs, a local REST API, a browser dashboard, and MCP.
Memory falls into 13 typed categories (instruction, fact, decision, goal, commitment, preference, relationship, context, event, learning, observation, artifact, error), so recall filters by type instead of ranking one undifferentiated blob.
Two backends: fully local (Docker plus Ollama, no account, no outbound calls) or Moorcheh Cloud (free API key, 100,000 free operations), switchable with one command.
The whole estate exports as Open Knowledge Format markdown (memanto memory export --okf), and memanto migrate imports from Mem0, Letta, Supermemory, Zep, and Hindsight.
memanto connect wires capture and recall into 13 coding CLIs (Claude Code, Codex, Cursor, Windsurf, Antigravity, Gemini CLI, Cline, Continue, OpenCode, Goose, Roo, GitHub Copilot, Augment).
Made by Moorcheh AI, with the April 2026 paper (arXiv 2604.22085) behind the retrieval engine.

## Status

**Active, young, and vendor-led.**
2,311 stars and 734 forks, created 2026-03-23, pushed 2026-10-09, MIT, as of 2026-10-11 (GitHub API).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=moorcheh-ai/memanto&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=moorcheh-ai/memanto&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=moorcheh-ai/memanto&type=date&theme=dark&legend=top-left" />
</picture>

PyPI is at 0.2.27 (2026-10-07) with about 40 releases since spring, and npm is in sync at 0.2.27.
The paper claims 89.8 percent on LongMemEval and 87.1 percent on LoCoMo through Moorcheh's Information Theoretic Search engine, with datasets and a harness published on Hugging Face.
The Hacker News record is modest: a 14-point thread in June 2026 (11 comments) and a 3-point Mem0-migration story in September.
**The fork-to-star ratio (about one fork per three stars as of 2026-10-11) is far above every peer in this category, which makes the raw engagement numbers harder to read than the star count suggests.**

## Strengths

- **It manages rather than stores**: nightly consolidation, contradiction surfacing for review, policy-driven expiry with restore, and pre-task briefing are scheduled behaviors, which most members here leave to your application code.
- The README's benchmark caveat is the category's most self-critical: it says cross-project scores are not comparable and to treat every number, including its own, as directional.
- Estate portability is first-class: OKF markdown export, one-command migration in from five named rivals, and a working format the README calls deliberately implementable by competitors.
- The fully local path runs Docker plus Ollama with no account, scoped per-agent namespaces, and confidence plus provenance stamps on every belief.

## Cautions

- **The headline numbers are the vendor's own paper**: no independent run exists, and the README's own caveat concedes the configuration decides the score.
- The free cloud key is a Moorcheh account funnel (100,000 operations), and no paid tier is published in the fetched surfaces, so the hosted economics are unknown.
- A 0.2.x project with the team concentrated at one vendor, so bus factor and roadmap risk come with the age.
- The fork-to-star anomaly (734 forks on 2,311 stars) deserves a second look before citing adoption.

## Pricing

Local mode is free under MIT (Docker plus Ollama, no account).
The Moorcheh Cloud backend has a free key tier with 100,000 operations per the docs.
No paid tier is published in the fetched surfaces, as of 2026-10-11.

## Compared to

- [Hindsight](../hindsight/index.md): both consolidate and learn rather than pile up rows; Hindsight serves memory as an API you call, Memanto runs as an agent above whichever stores you already have.
- [mem0](../mem0/index.md): the adoption leader's SDK is the pipeline Memanto positions itself above, and the migrate command imports Mem0 estates directly.
- [Memoryfields](../memoryfields/index.md): both make plain markdown the portable truth; Memoryfields is a spec with minimal tooling, Memanto is a running manager that emits OKF markdown.

## Bottom line

Recommended for engineers running three or more agents across CLIs who want contradictions and expiry handled on a schedule and will accept a young vendor-led dependency.
Not for anyone needing independent benchmark evidence, a published commercial ladder, or a multi-tenant hosted service.
My disagreeable claim: the management layer, not the store, is where memory products will actually compete, and Memanto is the clearest early bet on that position.

## Changes

- 2026-10-11 - Created from the 2026-10-11 Awesome-Agent-Memory entrant scan, with seven fetched sources and the self-published-benchmark-plus-fork-ratio profile recorded as the critical angle.

## See also

- [Memory Feature Matrix](../memory-feature-matrix/index.md) - the category comparison this note joins
- [Hindsight](../hindsight/index.md) - the API-serving consolidation engine Memanto wraps a manager around
- [mem0](../mem0/index.md) - the hosted pipeline it positions above and imports from
- [Memoryfields](../memoryfields/index.md) - the portable-format sibling of the OKF export
- [File-based agent memory](../file-based-agent-memory/index.md) - the convention whose rot-without-pruning problem the expiry policies automate

## References

- https://github.com/moorcheh-ai/memanto - repository, MIT, 2,311 stars, 734 forks, created 2026-03-23, pushed 2026-10-09, verified through the GitHub API as of 2026-10-11
- https://raw.githubusercontent.com/moorcheh-ai/memanto/main/README.md - the memory-agent model, the six behaviors, 13 memory types, OKF export, the migrate command, local mode, and the benchmark caveat
- https://docs.memanto.ai - the two backends (Moorcheh Cloud free key, on-prem Docker plus Ollama), install paths, and SDK references
- https://arxiv.org/abs/2604.22085 - the paper (April 2026): typed semantic memory, information-theoretic retrieval, and the 89.8/87.1 claims
- https://pypi.org/pypi/memanto/json - memanto 0.2.27 (2026-10-07) and the release count
- https://hn.algolia.com/api/v1/search?query=memanto&tags=story - the discussion record (14-point June 2026 thread, 3-point September migration story)
- https://github.com/TeleAI-UAGI/Awesome-Agent-Memory - the entrant source that surfaced it, as of 2026-10-11
