---
title: Operator Memory
created: 2026-10-17
updated: 2026-10-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, agent-memory, documentation, markdown, context-engineering]
readability: 3
audience_notes: >
  Engineers running Claude Code, Codex, OpenCode, or Pi who want session knowledge to persist
  as documentation their agent maintains itself, not as a retrieval database.
  Assumes you know what a harness is and how CLAUDE.md-style files work.
---

Operator Memory is a BSD-3-Clause, harness-agnostic documentation brain for coding agents: the working agent stores project knowledge as markdown documents in git-tracked partitions and consults and updates them as structural phases of every task, instead of capturing session snippets for retrieval.

**Its bet is that memory should be a maintained workspace, not a database: the agent writes specs, decisions, and lessons while the full picture is in context, and rewrites them where they live when truth changes.**

## What it is

A TypeScript system installed through the @aerovato/operator-helper npm package (20 releases from 1.0.0 on 2026-08-16 to 1.9.0 on 2026-10-27), with adapter plugins for Claude Code, Codex, OpenCode (V2 the default install since 2026-10-20, V1 kept as legacy), Pi, DeepSeek Harness, and Kiro.
Knowledge lives in three markdown partitions: ~/.operator/user/ for personal rules across projects, .operator/ for private project knowledge, and .operator-shared/ for knowledge published with the repository, with conflicts resolving private over user over shared.
Every session starts from a deterministic preamble: fixed framework rules, each partition's operator.md, a catalog mapping each Brain document, and a project index whose entries carry read_if conditions, so the agent deliberately opens deeper material instead of receiving similarity-ranked injections.
There is no vector database, no embedding model, no background maintenance agent, and no retrieval step; the author's comparison doc argues every capture-replay memory plugin shares one broken architecture.
It came out of the author's August 2025 internal/ folder convention and ships with the essay Agents Don't Need Memory. They Need Documentation. as its public argument.

## Status

**Young, single-author, and carried by one viral essay.**
461 stars with the repository pushed 2026-10-12, created 2026-08-16, BSD-3-Clause, as of 2026-10-17 (GitHub API).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=aerovato/operator-memory&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=aerovato/operator-memory&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=aerovato/operator-memory&type=date&legend=top-left" />
</picture>

The liao.gg essay (2026-10-03, updated 2026-10-05) reached 392 points and 312 comments on Hacker News, and the repository is the essay's grounded implementation, so the adoption and the argument share one author.
Development is active: the helper shipped 20 npm releases in two and a half months, and the roadmap names an observation engine, reliable brain updates, and cache-aware preamble rendering as unfinished work.

## Strengths

- **Deterministic loading is the design's core honesty mechanism**: the same session start produces the same orientation, and a stale brain fails in ordinary files you can open and fix, not in ranking weights you cannot inspect.
- The three-partition split (personal, project private, project shared) maps to how teams actually share knowledge, and the shared partition travels through the repo to every teammate and cloud agent.
- Harness-agnostic by construction: adapters are deliberately lean (the Claude Code adapter is under 100 lines, per the essay), so knowledge follows you across harnesses instead of binding to one.
- Zero infrastructure: markdown and git only, no embeddings bill, no daemon, no server.

## Cautions

- **There are no benchmarks, and the project argues benchmarks cannot apply**: its own issues thread hosts the position that LoCoMo, LongMemEval, and peers only test RAG wrappers, which is a fair critique of rivals and simultaneously a confession that this design has zero retrieval-quality evidence of its own.
- Freshness depends on the working agent's discipline, and the author admits manually intervening to create, rewrite, split, or consolidate documents, which is the same statistical-adherence problem the file conventions have with a bigger writing surface.
- Single-author project with a pseudonymous persona (liao.gg, rejected as a profiled voice on the thin-record test), so bus factor and support expectations are solo.
- The no-RAG pitch still trusts the agent to open the right document; the catalog routes, but nothing forces the read, and the essay's own comment section raises docs-rot and the-code-is-the-documentation objections the author answers in prose, not measurements.

## Pricing

Free and open: BSD-3-Clause, no hosted tier, no paid component of any kind.

## Compared to

- [File-based agent memory](../file-based-agent-memory/index.md): the convention Operator formalizes; the convention costs nothing and asks the agent nothing structured, Operator adds catalogs, partitions, and an update discipline on top.
- [OKF Agent Memory](../okf-agent-memory/index.md): the same documentation-over-recall thesis on a published standard, Google's OKF v0.2, with search tooling; Operator has no format spec and leans entirely on agent judgment and catalogs.
- [Cabinet](../cabinet/index.md): both keep memory as markdown files on disk; Cabinet brings its own scheduled agent team, Operator wires the harness you already run.

## Bottom line

**Recommended for solo developers and small teams on Claude Code, Codex, or OpenCode who want agent-maintained documentation instead of a memory database, and who will actually read the brain it writes.**
Not for teams needing measured retrieval quality (none exists here), enterprise support, or memory that spans applications rather than repos.

## Changes

- 2026-10-17 - Created from the coordinator-flagged entrant candidate (surfaced by the 2026-10-16 people-and-publications scan of the liao.gg essay), with nine fetched sources, the no-benchmarks-plus-single-author combination recorded as the critical angle, and the standing rejections consulted before admission.
- 2026-10-25 - The OpenCode adapter's V2 became the default install with V1 frozen to legacy (helper commit, 2026-10-20); recorded in the adapter list.
- 2026-10-27 - Recorded the helper@v1.9.0 release (October 27, the first since 1.8.0): the OpenCode V2-default install shipped in a release rather than only on main, with Antigravity harness guides, a benchmark-discussion link in the README, and portable test fixtures.
- 2026-10-30 - Rotation re-verification: every cited URL re-fetched live, no facts changed (the repository still pushed 2026-10-27, BSD-3-Clause, the helper still at 1.9.0 with twenty npm releases, the essay thread steady at 392 points and 312 comments, the README's partitions, harness table, and comparison links unchanged, the benchmark-exchange issue comment intact).

## See also

- [File-based agent memory](../file-based-agent-memory/index.md) - the convention this productizes, and the thesis's cheapest form
- [OKF Agent Memory](../okf-agent-memory/index.md) - the standard-track sibling implementing the same thesis on Google's OKF
- [Cabinet](../cabinet/index.md) - the other markdown-brain knowledge base, with its own agent team
- [Memory Feature Matrix](../memory-feature-matrix/index.md) - the shared-feature comparison this note joins

## References

- https://github.com/aerovato/operator-memory - repository, 461 stars, BSD-3-Clause, activity (GitHub API, as of 2026-10-17)
- https://raw.githubusercontent.com/aerovato/operator-memory/main/README.md - the loop, partitions, harness table, roadmap, and the VS-other-memory-plugins positioning
- https://raw.githubusercontent.com/aerovato/operator-memory/main/docs/architecture.md - the deterministic preamble, catalogs and read_if indexes, the no-RAG argument, and the partition authority order
- https://raw.githubusercontent.com/aerovato/operator-memory/main/docs/comparison.md - the anti-replay comparison and the five failure modes of capture-based memory
- https://raw.githubusercontent.com/aerovato/operator-memory/main/LICENSE - the BSD-3-Clause license text
- https://registry.npmjs.org/@aerovato%2Foperator-helper - publish history: 20 releases, 1.0.0 (2026-08-16) to 1.9.0 (2026-10-27)
- https://liao.gg/blog/agents-dont-need-memory - the author's essay (2026-10-03, updated 2026-10-05), the project's public argument
- https://news.ycombinator.com/item?id=49945933 - the essay's thread (392 points, 312 comments, 2026-10-03), the critical engagement with the documentation-over-recall position
- https://api.github.com/repos/aerovato/operator-memory/issues/comments/5979061413 - the benchmark exchange in issue #48: the counterparty's position that current memory benchmarks test RAG wrappers, not memory systems
