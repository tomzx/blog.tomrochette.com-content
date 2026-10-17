---
title: OKF Agent Memory
created: 2026-10-17
updated: 2026-10-17
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, agent-memory, okf, git-native, go, mcp]
readability: 3
audience_notes: >
  Engineers who want agent memory as a versioned knowledge corpus in their git repository,
  built on a published open format rather than a vendor's store.
  Assumes you know what AGENTS.md and MCP are.
---

OKF Agent Memory is an MIT-licensed, zero-dependency Go implementation of Google's Open Knowledge Format (OKF) v0.2 that turns a git-tracked knowledge/ bundle into agent memory, with sub-300-microsecond in-memory BM25 search, progressive disclosure through index files, and a built-in stdio MCP server.

**Its bet is that memory should be a structured corpus in your repository on a published spec, split into a 400-token push layer of rules the agent always sees and a pull layer of OKF knowledge objects it queries on demand.**

## What it is

A single Go binary and library from the okf-memory org, installable through brew, that pairs two layers: a push layer capping AGENTS.md at 400 tokens of behavioral codex written in the project's own Agent Action Grammar (an RFC'd ASCII micro-syntax), and a pull layer holding OKF v0.2 knowledge bundles that consume zero baseline tokens.
The OKF objects carry typed metadata the spec defines: sources for provenance, trust tiers separating human-verified from agent-generated entries, and lifecycle fields like status and stale_after.
Tools surface over a stdio MCP server (okf_search, okf_show, okf_create, okf_validate) plus the CLI and Go library, so Claude Code, Codex, and Cursor can query the bundle without any embedding API or external database.
It implements, rather than defines, the format: the normative spec lives in GoogleCloudPlatform's knowledge-catalog repository, which makes this note the category's first member built on someone else's published standard.

## Status

**Active and growing, admitted this run when its standing re-review trigger fired on both arms.**
814 stars with the repository pushed 2026-10-12, created 2026-09-05, MIT, as of 2026-10-17 (GitHub API), with v0.6.1 released 2026-10-12.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=okf-memory/okf-agent-memory&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=okf-memory/okf-agent-memory&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=okf-memory/okf-agent-memory&type=date&legend=top-left" />
</picture>

The project was rejected three times (the 66-point launch thread at 146 stars in September 2026, then re-rejections at 527 and 757 stars with no second implementation or independent coverage), and the trigger set on it named exactly the two things that happened since: a second OKF implementation now exists (fellowgeek/mcp-memory, a 70-point Show HN, folded here as ecosystem evidence), and the 392-point documentation-over-recall thread cites this repository by name three times as the OKF approach's implementation.
Stars moved 146 to 527 to 757 to 814 across five weeks, so the growth the earlier rejections called flat has resumed.
The launch thread's engagement is measurable but shallow per comment (81 points, 32 comments), and the sharpest questions in it, why benchmark latency instead of recall and whether this differs from markdown files plus ripgrep, went unanswered.

## Strengths

- **The only member in this category built on a vendor-published open format**, which makes the memory files portable to any other OKF reader instead of to this tool's own importer.
- Zero-dependency single binary: sub-300-microsecond BM25 over the bundle, sub-4-millisecond cold starts under 15 MB of RSS, no Python or Node runtime, no vector database, no embedding bill.
- Git-native audit by construction: every memory is a diffable markdown file with sources and code_refs, reviewable in a PR like code.
- Trust tiers give human-written knowledge precedence over agent-generated drafts, the first member to encode that distinction in the format layer rather than in prompt discipline.

## Cautions

- **Every performance claim is latency-side and self-published**: sub-300-microsecond search says nothing about retrieval quality, and the thread's direct question about recall benchmarks drew no answer, so there is zero evidence the bundle surfaces the right knowledge.
- The ripgrep-equivalence objection stands unanswered: an agent that reads markdown and greps it, plus an index it maintains, reproduces much of this design with no new tool, so the delta over [File-based agent memory](../file-based-agent-memory/index.md) is the format and the tooling, not the capability.
- Adherence is the open risk the thread named: a third-party store competes with harness-native memory features (Codex's Astra, Claude Code's auto memory) that the model may prefer, and nothing published measures which one the agent actually uses.
- Young org (created 2026-09-05) with the OKF ecosystem still nascent: the two sibling implementations (mcp-memory, dormant since 2026-08-30 at 218 stars; Kage, 3-to-4-point threads) show the format has traction and no second healthy implementation, and the first delivery-side adoption is authoring tooling, not memory (scaccogatto/okf-skills, 417 stars as of 2026-10-17, the OKF toolkit that authors, validates, and visualizes bundles as Claude Code skills).

## Pricing

Free and open: MIT, no hosted tier, no paid component of any kind.

## Compared to

- [Memoryfields](../memoryfields/index.md): both make portable files the truth; Memoryfields is a bespoke draft spec with minimal tooling, OKF Agent Memory implements Google's published spec with working search and MCP tooling.
- [File-based agent memory](../file-based-agent-memory/index.md): the convention this formalizes; the push layer is an AGENTS.md discipline with a token cap, the pull layer is what the convention lacks.
- [Memanto](../memanto/index.md): a running memory manager whose export emits OKF markdown, so Memanto estates gain a migration edge into this bundle format rather than a rival architecture.

## Bottom line

**Recommended for teams that want memory audited like code in git, on a published format, with no infrastructure bill, and who accept unproven retrieval quality as the price.**
Not for cross-user or cross-app memory (one repo bundle, no multi-user API), and not for anyone who needs benchmark evidence before adopting a memory tool.

## Changes

- 2026-10-17 - Created when the standing re-review trigger fired on both arms (independent citations in the 392-point documentation-over-recall thread, and a second OKF implementation in fellowgeek/mcp-memory), with ten fetched sources, the unanswered recall-question and ripgrep-equivalence objections recorded as the critical angles, and mcp-memory plus Kage folded in as ecosystem evidence below the admission bar.
- 2026-10-17 - Added the scaccogatto/okf-skills toolkit to the ecosystem caution and references as the OKF format's first delivery-side adoption, routed here from the skills category's entrant scan.

## See also

- [Memoryfields](../memoryfields/index.md) - the bespoke-spec sibling facing the same format-versus-tooling trade
- [File-based agent memory](../file-based-agent-memory/index.md) - the convention whose limits this design names and formalizes
- [Memanto](../memanto/index.md) - the member whose OKF markdown export makes this bundle format a migration target
- [Memory Feature Matrix](../memory-feature-matrix/index.md) - the shared-feature comparison this note joins

## References

- https://github.com/okf-memory/okf-agent-memory - repository, 814 stars, MIT, activity (GitHub API, as of 2026-10-17)
- https://raw.githubusercontent.com/okf-memory/okf-agent-memory/main/README.md - the DMAA two-layer architecture, AAG, highlights, and claims
- https://okf-memory.dev - the project docs site and landing page
- https://raw.githubusercontent.com/GoogleCloudPlatform/knowledge-catalog/main/okf/SPEC.md - the upstream Google OKF v0.2 specification this project implements
- https://raw.githubusercontent.com/okf-memory/okf-agent-memory/main/docs/spec/AGENT_ACTION_GRAMMAR_RFC.md - the Agent Action Grammar RFC behind the 400-token push layer
- https://api.github.com/repos/okf-memory/okf-agent-memory/releases/latest - v0.6.1 (2026-10-12), the latest tagged release
- https://news.ycombinator.com/item?id=49581240 - the launch thread (81 points, 32 comments, 2026-09-05) with the unanswered recall-benchmark and ripgrep-equivalence objections
- https://news.ycombinator.com/item?id=49945933 - the 392-point documentation-over-recall thread whose comments cite this repository three times, the independent coverage that fired the trigger
- https://api.github.com/repos/fellowgeek/mcp-memory - the second OKF implementation (218 stars, MIT, pushed 2026-08-30), the trigger's other arm, folded here as ecosystem evidence
- https://hn.algolia.com/api/v1/items/49286073 - the second implementation's own 70-point Show HN thread, the OKF family's other data point
- https://github.com/scaccogatto/okf-skills - the first delivery-side OKF adoption (417 stars, MIT, pushed 2026-10-13), routed here from the skills category's entrant scan
