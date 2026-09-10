---
title: "Memory Feature Matrix"
created: 2026-08-24
updated: 2026-09-10
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, comparison, memory, agent-memory, ai-agents]
readability: 3
audience_notes: >
  Engineers picking a memory approach for agents or AI products who need the deltas at a glance.
  Assumes you know what a knowledge graph, BYOK, and MCP mean; each column links to a full note with sources.
---

This matrix compares the eight memory approaches profiled in this section, feature by feature: the file convention, the session-compression plugin, the cross-model episodic memory engine, the memory-first harness, the two memory APIs, the self-hostable graph pipeline, and the portable memory format.
Everything below was re-verified against live sources on 2026-09-10, with the Cognee column first verified 2026-08-26, the Memoryfields column first verified 2026-09-04, and the Engrim column first verified 2026-09-10.

**For coding agents I would start with plain files and not buy any service on benchmark claims, because the only memory problem files cannot solve at any price is contradiction over time, and Zep is the only vendor whose architecture faces it head on.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.
Each column links to the full research note; every cell below traces to a source cited there or in the references.

## The matrix

| Feature | [claude-mem](../claude-mem/index.md) | [Cognee](../cognee/index.md) | [Engrim](../engrim/index.md) | [Files](../file-based-agent-memory/index.md) | [Letta](../letta/index.md) | [Mem0](../mem0/index.md) | [Memoryfields](../memoryfields/index.md) | [Zep](../zep/index.md) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kind | local plugin, engine plus cloud | OSS platform, library plus cloud | local engine, CLI plus hooks and MCP | convention, no vendor | platform, harness plus cloud | hosted service, self-hostable | open file format, spec plus tooling | hosted service, enterprise |
| Memory model | compressed observations, SQLite FTS5 plus optional vectors | graph plus vector plus relational | curated episodic records, SQLite FTS5 plus model2vec vectors, 4,000-char boot pack | plain markdown files | editable memory blocks, learned | vector plus graph plus KV | flat markdown pages plus optional SQLite vector index | temporal knowledge graph |
| Self-host | ✓ fully local by default | ✓ full engine, BYO backends | ✓ fully local, one SQLite file | ✓ no infra needed | ~ V1 server archived | ✓ OSS SDK and server | ✓ fully local, it is just files | ~ Graphiti engine only |
| Open source license | ✓ Apache-2.0 | ✓ Apache-2.0, whole engine | ✓ MIT, whole engine | ~ memU Apache-2.0 | ✓ Apache-2.0 | ✓ Apache-2.0 | ✓ AGPL-3.0 tool, MIT skill and spec | ~ Graphiti Apache-2.0 |
| Contradiction and decay handling | ~ summaries and compaction | ~ bi-temporal memory on Enterprise BYOC only | ~ manual supersede, merge resolution, opt-in prune | ✗ manual pruning | ~ sleep-time consolidation | ~ Dream, temporal retrieval | ✗ nothing beyond page edits | ✓ bi-temporal invalidation |
| Cross-user, cross-app memory | ✗ machine-local, cloud sync optional | ✓ documented multi-user mode | ~ cross-CLI on one machine, merge for multi-machine, not cross-user | ✗ machine-local, per-repo | ~ agent-scoped persistence | ✓ apps and thousands of users | ~ corpus is transport-portable (S3, git, HTTP), single-corpus | ✓ millions of per-user graphs |
| Integration surface | hooks, MCP, skills, 8+ agents | Python/TS/Rust SDKs, MCP, HTTP, CLI | hooks, MCP, CLI, skills, 5 agent CLIs | file conventions, native everywhere | SDK, CLI, cloud API | API, MCP, CLI, skills | skill, CLI, any file transport | API, MCP, plugins |
| Audit trail | ~ queryable observation store | ? | ~ origin-agent provenance and flight-recorder log | ~ git diffs only | ~ inspectable blocks | ? | ~ readable pages, sha256-pinnable, no provenance | ✓ fact-to-episode provenance |
| Pricing model | free local, $20/mo cloud, $333/seat team | OSS free, cloud $1.00 per 1M tokens plus $5 per workspace | free, MIT, no hosted tier | free | free BYOK, $20/mo, per-agent metering | freemium, $19 to $249/mo | free | credits, $104/mo entry |
| Lock-in risk | low-medium, SQLite local, cloud optional | low, engine is portable | low, plain SQLite file, bus factor one | none, plain text | medium, pivot churn | medium, paid-only brain | none, plain text zip | high, managed engine core |

## Reading the matrix

**The Kind row is really an architecture row: the five non-convention members each put memory in a different place, beside the agent as a plugin (claude-mem) or a cross-model engine (Engrim), inside the harness (Letta), beside it as an API (Mem0), or under it as governed infrastructure (Zep), and the convention puts it in your repo.**
That placement decision drives every other row, from integration surface to lock-in.
**Memoryfields is the new extremum on the same axis: it removes the architecture entirely by shipping memory as a spec'd data format, which is why its row is the cheapest and the thinnest at once.**

**The contradiction row is the only one with a clean winner, and it is the row I would weight most.**
Zep's bi-temporal invalidation marks old facts invalid instead of overwriting them; Mem0's April 2026 rewrite added entity linking and temporal retrieval, a convergence its own note reads as Zep validating the architecture first; Letta consolidates at sleep time; files just rot, and conflicting rules get resolved arbitrarily.

**The file column wins every row it appears in on price, and loses exactly two: cross-user memory and audit.**
Auto memory is machine-local and per-repository, so the moment memory must follow users across apps and machines, the free option drops out, which is the precise boundary where the services earn their keep.
Engrim is the second zero-cost column, and it loses the same two rows (audit partial, cross-user absent), which makes the two free local options the natural pair for personal memory.

**Open source here does not mean what the license row suggests, and the self-host row is the correction.**
Letta's 24.7k-star repo is a landing page with the V1 server archived unsupported; Zep's self-hostable Community Edition is discontinued and only the Graphiti engine remains open; Mem0's benchmarked brain is the paid platform while the OSS SDK is directionally weaker.
**Cognee and Engrim are the exceptions the row now proves: Cognee's entire engine is Apache-2.0 with no paid-only core, and Engrim is MIT over a plain SQLite file, which is why their lock-in cells are the only lows among the tools.**
**The only column with no gap between what is open and what runs is the convention, because there is nothing to close.**

**Pricing spreads from zero to $104/month at entry, a 5.5x gap between the two services at their first paid tier, and what the premium buys is governance (provenance, access control, compliance), not memory quality.**
Mem0's $19 Starter undercuts everyone; Zep's credit metering prices the audit trail, not the tokens.

## Choosing from the matrix

- Coding agent in one repo, one machine: write the AGENTS.md/CLAUDE.md pair, prune monthly, pay nothing.
- User-facing personalization across apps and thousands of users: Mem0, accepting a managed dependency.
- Facts change over time (preferences, roles, prices) and "why did the agent say that" needs an auditable answer: Zep.
- Always-on agents that must accumulate a self, or you want to hack on where memory is going: Letta, or steal its memory-block and sleep-time patterns into a harness you already run.
- Must self-host everything: Cognee (the whole engine runs on your backends), files, or Mem0 OSS, or Graphiti plus your own graph database if you can operate one.
- Memory across many users with flat billing instead of seats or credits: Cognee Cloud at $1.00 per 1M tokens processed.
- Solo builder on no budget: files, full stop; Zep's own note says the graph stack is heavy at small scale.
- One developer, multiple agent CLIs, one repo: Engrim, the only column that keeps one provenance-tagged store every CLI reads.
- Memory that must follow you across machines and apps without a vendor: Memoryfields, with the caveat that the spec is a two-week-old draft and its contradiction-handling row is empty.

## See also

- [Context Management Patterns](../context-management-patterns/index.md) - where memory sits among the other context techniques
- [Harness Feature Matrix](../harness-feature-matrix/index.md) - the tools whose file-memory conventions fill the first column
- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - the map these columns plug into
- [AGENTS.md](../agents-md/index.md) - the standard behind the convention column
- [MCP](../mcp/index.md) - the protocol behind the integration-surface row

## References

- https://code.claude.com/docs/en/memory - CLAUDE.md hierarchy, auto memory limits, adherence caveats for the Files column
- https://agents.md - the convention standard and adoption count for the Files column
- https://github.com/letta-ai/letta-code - the active Letta harness, memory blocks, license
- https://docs.letta.com/pricing - Letta plan structure and per-agent metering
- https://github.com/mem0ai/mem0 - Mem0 stars, April 2026 algorithm, OSS-versus-platform disclaimer
- https://mem0.ai/pricing - Mem0 tiers and quotas for the pricing row
- https://www.getzep.com/pricing - Zep plans and credit metering for the pricing row
- https://github.com/getzep/graphiti - the temporal graph engine, self-host requirements for the Zep column
- https://github.com/topoteretes/cognee - the Cognee column: whole-engine Apache-2.0, backends, multi-user docs
- https://www.cognee.ai/pricing - Cognee cloud per-token rate, workspace fee, and the Enterprise bi-temporal memory listing, as of 2026-09-10
- https://github.com/thedotmack/claude-mem - the claude-mem column: hook architecture, SQLite storage, license, adoption
- https://docs.claude-mem.ai/architecture/overview - the compression flow and integration surfaces for the claude-mem column
- https://claude-mem.ai - claude-mem pricing tiers for the pricing row
- https://calpaterson.com/memoryfields.html - the Memoryfields column: format thesis, design decisions, objections FAQ
- https://github.com/calpaterson/memoryfield-spec/blob/main/SPEC.md - the Memoryfields spec: flat directories, page limits, transports, embedding codes
- https://github.com/timgordontg/engrim - the Engrim column: repo, MIT, 220 stars, 42 commits, release cadence (as of 2026-09-10)
- https://raw.githubusercontent.com/timgordontg/engrim/main/README.md - Engrim architecture, provenance, CLI surface, and security notes
- https://pypi.org/pypi/engrim/json - Engrim release history and license for the Engrim column
- https://hn.algolia.com/api/v1/items/49594008 - the Engrim launch thread: traction and the in-repo-docs counterpoint
