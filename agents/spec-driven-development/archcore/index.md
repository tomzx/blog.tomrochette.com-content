---
title: Archcore
created: 2026-10-21
updated: 2026-11-08
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, spec-driven-development, context-engineering, decision-records, open-source]
readability: 3
audience_notes: >
  Engineers who want a project's specs, decisions, and rules enforced on coding agents across several harnesses,
  without adopting a whole method's vocabulary.
  Assumes you know what a decision record and a review gate are.
---

Archcore is the archcore-ai org's Apache-2.0 Go CLI plus per-agent TypeScript plugins that keep a project's specs, plans, decisions, and rules as typed Markdown files under `.archcore/` in Git, and drive coding agents through plan, document, and review commands that read and enforce them.

**Its distinctive move is the two-sided review verdict: `/archcore:review` compares the branch against the documents and returns `code-wrong` when the code broke a standing document, or `spec-wrong` when the document is the one out of date, so the tool names the guilty side instead of handing a human a pile of findings.**

## What it is

An install script plus `archcore init` that adds the CLI and connects the agents you choose through MCP and hooks: plugins for Claude Code, Codex CLI, and GitHub Copilot CLI, native support for Gemini CLI, OpenCode, Roo Code, and Cline, and one extra setup step for Cursor.
The workflow is four skills: `/archcore:init` reads the repository and proposes the first documents (or imports existing CLAUDE.md, AGENTS.md, and rule files), `/archcore:plan` writes the spec, examples, and tasks a change needs, `/archcore:document` turns one sentence into a linked, typed decision or rule, and `/archcore:review` checks the branch against all of it before merge.
The package sizes itself to the change: a small fix gets no documents, a settled choice gets a decision record, a migration gets a plan, a multi-capability initiative gets a PRD and one spec per capability.
Documents carry their type in the filename (`rate-limiting.spec.md`, `token-bucket-in-redis.adr.md`), link to related documents, and version with the code, and the project's own `.archcore/` tree is the published example.

## Status

Active and young: 71 stars and 13 forks since creation on 2026-04-05, pushed 2026-11-07, Apache-2.0, with v0.15.5 (2026-11-07) the newest of a six-release train that ran v0.15.0 through v0.15.5 on November 2 to 7 (v0.15.0 made global sources a read policy written through their project and gave every MCP tool and hook an explicit per-call project target, v0.15.1 removes hung plans in one batch on every review, v0.15.2 planned the Antigravity, Pi, Hermes, OpenClaw, and JetBrains host integrations and fixed OpenCode 2.x plugin-update authorization, v0.15.3 moved the CLI to Go 1.26.10 with Charm v2 and validates a post-tool-use write in the project the server served, v0.15.4 hardened the CLI's write paths and synced the Copilot and Codex agent copies with the list_relations wording, and v0.15.5 fixed the document-search path limit, rejecting a negative limit under search_documents for_path and stating that for_path ignores limit), following the v0.14.x line that landed the OpenCode plugin package and the spec body-cap fix, as of 2026-11-08 (GitHub API).
The CLI is written in Go, per the project's own v0.15.3 release notes, README Go 1.26+ badge, and dev-branch source tree (328 Go files); the default main branch carries the TypeScript plugins and docs, which is what its earlier language stats alone showed.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=archcore-ai/archcore&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=archcore-ai/archcore&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=archcore-ai/archcore&type=date&legend=top-left" />
</picture>

**The independent footprint is empty: a Hacker News search returns no thread about it (the query only matches unrelated ARM chipset posts), so adoption rests on its own site, docs, and Discord/Telegram channels, and the bilingual English and Russian docs say the early community is regional.**
It entered this category's scan as the skills worker's 2026-10-20 cross-category flag.

## Strengths

- The review verdict names the side that is wrong, which is the decision every other convergence mechanism in this category leaves to a human.
- Ceremony sizing is built into the packaging logic, not chosen by the user, the same answer BMad and cc-sdd give but applied per document package.
- The context is plain typed Markdown in Git, readable without the tool, and any MCP-speaking agent can read and write it, so the artifacts outlive the harness choice.
- The import path (`/archcore:init import`) turns an existing CLAUDE.md or AGENTS.md setup into the document model instead of starting from zero.

## Cautions

- 71 stars, a pre-1.0 v0.15 line, and zero independent coverage mean nothing here is validated by anyone but its steward.
- The steward is a young company org (8 public repositories, site, docs, and community channels of its own) with no stated business model, so the free tool's durability is an open question.
- Review only checks what the documents cover; a branch touching undocumented behavior gets checked against decisions and rules alone, and the tool's answer is to offer recording, not to guarantee coverage.
- The four-skill flow assumes the human keeps recording decisions as they happen; nothing schedules the re-check of an accepted decision that later went stale.

## Pricing

Free and open source under Apache-2.0.
No paid tier is published anywhere in the repo, site, or docs, as of 2026-10-21.

## Compared to

- [OpenSpec](../openspec/index.md): both keep living specs in the repo; OpenSpec versions change as delta proposals archived into a ledger, Archcore versions typed documents beside plans and decision records and checks the branch against them.
- [GitHub Spec Kit](../spec-kit/index.md): Spec Kit scaffolds per-change conventions for any agent, Archcore builds standing per-project context plus a review gate, so they compose more than they compete.
- [AGENTS.md](../../protocols/agents-md/index.md): the rules file is the convention Archcore imports and extends with typed, linked, review-enforced documents.

## Bottom line

**Recommended for multi-agent teams that want decisions and specs enforced at review time and that accept a young, unvalidated steward.**
Not for anyone who needs a proven adoption record, and not for solo prototype work where no document package would be produced at all.
The disagreeable claim I will defend: naming the guilty side (code-wrong or spec-wrong) is the convergence answer this category has been missing, because every other tool hands you findings and hopes you adjudicate, which is exactly where review fatigue eats the gate.

## Changes

- 2026-10-21 - Created from the skills worker's cross-category flag, resolving archcore-ai/archcore into this category as the typed-document context layer with the two-sided review verdict.

- 2026-10-25 - Corrected the star-history chart fallback markup (the img fallback carried the dark-theme parameter; it now points at the default chart).
- 2026-10-26 - Corrected the star-history chart light-source markup (the light source carried the dark-theme parameter; it now points at the default chart).
- 2026-10-27 - Recorded the v0.14.0 through v0.14.3 release train (all 2026-10-26): an OpenCode plugin package delivered from `archcore init` with OpenCode 2.x support, and the spec body-cap fix that stops verification and revisit sections from forcing a spec split.
- 2026-10-27 - Corrected the implementation language from Go to TypeScript, per the repository's own language stats (TypeScript and Shell, no Go); meaning otherwise unchanged.
- 2026-11-07 - Out-of-rotation re-verification triggered by the v0.15.3 release signal (every cited source re-fetched, all alive): corrected the implementation language back to Go, because the project's own v0.15.3 release moved the CLI to Go 1.26.10 with Charm v2, the README carries a Go 1.26+ badge, and the dev-branch source tree holds 328 Go files, while the default branch the 10-27 correction read carries only the plugins and docs; recorded the v0.15.0 through v0.15.3 release train (2026-11-02 to 06: global sources as a read policy with per-call project targets, hung-plan cleanup on review, plans for five new host integrations, and the Go 1.26.10 toolchain move).
- 2026-11-08 - Recorded the v0.15.4 and v0.15.5 releases (both 2026-11-07: hardened CLI write paths with the Copilot and Codex agent copies synced to the list_relations wording, and the search_documents for_path limit fix).

## See also

- [OpenSpec](../openspec/index.md) - the delta-ledger neighbor on the living-specs axis
- [GitHub Spec Kit](../spec-kit/index.md) - the scaffolding alternative it composes with
- [AGENTS.md](../../protocols/agents-md/index.md) - the convention its import path starts from
- [Spec Driven Development Feature Matrix](../spec-driven-development-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/archcore-ai/archcore - repository: counts, dates, license, the four-command README (71 stars as of 2026-10-21)
- https://raw.githubusercontent.com/archcore-ai/archcore/main/README.md - the plan/document/review workflow, the document tree, install surfaces, and the change-to-package table
- https://archcore.ai/ - the project site: positioning, install script, integrations list, and the code-wrong/spec-wrong framing
- https://docs.archcore.ai/guides/commands/ - the command reference: typed documents, plugin hosts, MCP access, CLI split
- https://archcore.ai/how-to-use/ - the MCP-plus-hooks connection model and the CLAUDE.md/AGENTS.md import path
- https://api.github.com/repos/archcore-ai/archcore/releases - the release train through v0.15.3 (2026-11-06), fetched 2026-11-07
- https://hn.algolia.com/api/v1/search?query=archcore&hitsPerPage=5 - the footprint check: no thread about the product, only unrelated ARM hits
