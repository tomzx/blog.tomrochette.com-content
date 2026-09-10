---
title: Engrim
created: 2026-09-10
updated: 2026-09-10
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, memory, sqlite, local-first]
readability: 3
audience_notes: >
  Engineers running AI coding CLIs (Claude Code, Cursor, Codex, Antigravity, Windsurf) who want
  session memory to survive /clear and follow a project across model switches.
  Assumes familiarity with MCP, lifecycle hooks, and at least one hosted memory service.
---

Engrim is a local-first, project-scoped episodic memory engine for AI coding CLIs: one MIT-licensed Python package that keeps decisions, constraints, and session state in a single SQLite file on your machine and re-injects a 4,000-character memory pack into whichever CLI (Antigravity, Claude Code, Cursor, Windsurf, Codex) you open next.
Facts below verified as of 2026-09-10.

**Its bet is that the unit of memory should be the project, not the model or the harness: one curated store that every agent CLI on your machine reads and writes, so switching models mid-project costs nothing.**

## What it is

Engrim is a Python package by Tim Gordon (pip install engrim, Python 3.10+) that stores episodic records (decision, fact, feedback, state, user, reference) in ~/.engrim/memory.db.
Retrieval is hybrid: SQLite FTS5 with bm25 and a porter stemmer, plus model2vec static embeddings, fused by reciprocal rank, all on CPU with a pure-lexical fallback (ENGRIM_EMBED=off).
`engrim setup` auto-detects installed environments and wires lifecycle hooks (SessionStart, Stop, UserPromptSubmit), MCP servers, and skills for Google Antigravity, Claude Code, Cursor, Windsurf, and Codex CLI.
Every record carries an origin_agent field (antigravity, claude-code, cursor, cli, user), and a flight-recorder log of turns powers `engrim review`, a heuristic "safe to clear" check run before wiping a session.

## Status

**A fast mover, and one this section's own pass initially rejected.**
The Show HN thread (2026-09-07) reached 92 points and 64 comments as of 2026-09-10, and the repo grew from 27 stars to 220 in the same three days.
I passed on it at launch at 19 points and 27 stars, and the category pass that surfaced it again on 2026-09-10 reversed that call.
The cadence is unusual: 42 commits and 15 PyPI releases since 2026-06-23, with three releases in the 72 hours around verification (1.3.0 on 2026-09-07, then 1.3.1 and 1.3.2 on 2026-09-10).
Several of those releases fold in same-day fixes requested in the thread, including an uninstall command, Codex auto-detection, stop-hook handling, and a multi-store `engrim merge`.
Single maintainer, no funding, no institutional backing.

## Strengths

- **Cross-model memory is the actual differentiator**: claude-mem and the other local plugins bind memory to one harness, while engrim's single SQLite file is shared by five CLIs, which is the only design in this category built for people who switch models mid-project.
- Provenance is built in, not gated: origin_agent tags every record and supersede chains retire conflicting decisions, a capability the hosted services mostly reserve for enterprise tiers.
- The capture story is realistic: automatic engrim_add via MCP plus a manual `engrim add`, with `engrim review` and resume-pointer records making /clear recoverable.
- Hygiene details show care: 0600 file permissions, *.db gitignored by default, an idempotent content-keyed merge for multi-machine stores, and pruning that is opt-in rather than automatic.

## Cautions

- **The flagship evidence is a self-reported case study, not a benchmark**: the 105-session, 50,000-line trading-system numbers ship without a methodology, and the thread's sharpest question (benchmark it against other memory plugins) went unanswered.
- The launch drew an AI-generated-content flag from a HN moderator, and the author acknowledged drafting replies with LLM help, which is worth knowing when reading the thread's uniformly positive tone.
- The 4,000-character pack is a compaction policy as much as a memory system, since what survives is whatever the agent chose to log, and the thread's in-repo-docs counterpoint covers most solo-developer needs with no new store.
- Bus factor of one, a five-platform wiring surface, and hooks that rewrite settings files add moving parts the "it's just a SQLite file" pitch hides, so inspect the setup diff (there is a --dry-run) before trusting it.

## Pricing

Free and open: MIT package, MIT repo, no hosted tier, no cloud component at all.
The cost is a disk file and your attention.

## Compared to

- [mem0](../mem0/index.md): the hosted API solves multi-user, cross-application memory and charges monthly for it; engrim is single-user, machine-local, and free, and refuses to become a service.
- [Memoryfields](../memoryfields/index.md): both bet on portable local data, but Memoryfields makes the files canonical and the index disposable, while engrim makes the SQLite store canonical and only mirrors markdown in one way via `engrim sync`.
- [File-based agent memory](../file-based-agent-memory/index.md): the strongest counterposition and the HN thread's best objection, since memory that lives in the repo travels to every environment for free; engrim's answer (a scratchpad that never clutters commit history) wins only if you actually switch CLIs mid-project.

## Bottom line

Recommended for solo developers who run two or more agent CLIs against the same repo and want decisions and provenance to survive model switches and /clear.
Not for teams needing shared or cross-user memory, and probably not for single-CLI users, where the in-repo docs convention does the job with zero new infrastructure.
My disagreeable claim: the provenance tracking, not the local-first storage, is the real product, and engrim would still be worth running if it did nothing but tag which agent made which decision.

## See also

- [Memory Feature Matrix](../memory-feature-matrix/index.md) - where this column lands against the seven other memory approaches
- [Memoryfields](../memoryfields/index.md) - the files-canonical sibling, the opposite resolution of the same portability bet
- [mem0](../mem0/index.md) - the hosted, multi-user counterpoint engrim refuses to become
- [claude-mem](../claude-mem/index.md) - the closest architectural cousin: hooks plus SQLite, but bound to one harness
- [File-based agent memory](../file-based-agent-memory/index.md) - the convention the HN counterpoint defends

## References

- https://github.com/timgordontg/engrim - the repo: description, 220 stars, 12 forks, 42 commits, MIT, pushed 2026-09-10, as of 2026-09-10
- https://hn.algolia.com/api/v1/items/49594008 - the Show HN thread (92 points, 64 comments): launch claims, the in-repo-docs counterpoint, the moderator AI-content flag, and same-day fixes
- https://news.ycombinator.com/item?id=49594008 - the thread's canonical page confirming 92 points and 64 comments as of 2026-09-10
- https://raw.githubusercontent.com/timgordontg/engrim/main/README.md - architecture (FTS5 plus model2vec), provenance, CLI surface, security notes, and the 105-session case study
- https://pypi.org/pypi/engrim/json - 15 releases from 0.7.0 (2026-06-23) to 1.3.2 (2026-09-10), MIT classifier, Python 3.10+
- https://api.github.com/repos/timgordontg/engrim/releases/latest - v1.3.2 notes: multi-store merge, negation checks, 0-session review state, 197 passing tests
- https://api.github.com/repos/timgordontg/engrim/license - the MIT LICENSE file, verified through the GitHub API
