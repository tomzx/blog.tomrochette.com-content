---
title: git-ai
created: 2026-10-11
updated: 2026-10-11
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, session-analytics, provenance, git, open-source]
readability: 3
audience_notes: >
  Engineers who want to know which agent, model, and prompt wrote which line of their code, and anyone comparing provenance mechanisms across session analytics.
  Assumes you know what git blame and git notes are.
---

git-ai is an Apache-2.0 Rust git extension that records which lines of code were written by which AI agent, model, and prompt, stores that attribution in Git Notes, and reads it back as AI blame, commit stats, and IDE gutter annotations.

**git-ai fills the provenance slot this category left nearly empty: ctx blames from the transcript side, while git-ai records authorship inside the repository itself, so the answer lives next to the code, syncs through ordinary push and fetch, and survives every rebase that would orphan an external database.**

## What it is

A single Rust CLI (installed by curl or PowerShell script on macOS, Linux, and Windows) built by Aidan Cunniffe and Sasha Varlamov, now maintained under the git-ai-project organization after moving from Cunniffe's personal account.
Fourteen named agents (Claude Code, Codex, Cursor, GitHub Copilot, OpenCode, Pi, Windsurf, Droid, Amp, Gemini, Continue, Junie, Rovo Dev, and Firebender) follow the project's open attribution standard, plus a documented add-your-agent path, and the CLI manages their pre and post tool-call hooks centrally.
Each Edit, Write, or Bash call triggers a `git ai checkpoint` that marks the touched lines as AI-authored, and on commit the checkpoints consolidate into a note on refs/notes/ai that maps files and line ranges to agent, model, session, and a pointer to the full transcript.
Git operations rewrite the notes to match: rebase, merge, squash, cherry-pick, stash, reset, and amend are all handled, eventually consistent within 5 to 100 milliseconds, while git mv, filter-branch, and git replace are named gaps.
`git ai blame` replaces git blame with agent-aware output, `git ai stats` reports percent AI, accepted rates, and per-tool and per-model breakdowns for any commit range, and VS Code, Cursor, Windsurf, and Antigravity plugins plus a magit port color the gutter by authoring session.
A vendor product, the Git AI Platform from Next Element, Inc., adds team rollout through MDM, a prompt store, and percent-AI analytics per PR, repo, and team.

## Status

Acquired and active: the founders announced Git AI joining OpenAI's Codex team on 2026-09-11, with continued investment in the open-source CLI and the standard.
2,829 stars, 312 forks, 261 open issues, created 2025-07-02, pushed 2026-10-07, newest tag v1.7.5 with no GitHub releases (distribution is the install script), as of 2026-10-11.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=git-ai-project/git-ai&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=git-ai-project/git-ai&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=git-ai-project/git-ai&type=date&legend=top-left" />
</picture>

The vendors claim hundreds of thousands of developer machines and Fortune 100 deployments.
Independent discussion is thinner than those numbers: a 6-point, 4-comment Show HN from 2025-11-10, and peer citations in other tools' threads (the Selvedge launch names it as the incumbent that gets checked in) rather than public debate of its own.

## Strengths

- The only member of this category that stores session attribution inside the repository, where it travels with the code and outlives any local database.
- Attribution is explicit, not inferred: agents report exactly which lines they wrote, which avoids the false positives every detection heuristic carries.
- The hard part of provenance, surviving history rewrites, is handled as a first-class feature rather than a caveat.
- Stats turn authorship into management signal: accepted rates per tool and model, and generated-versus-committed ratios that show how much agent output survived review.

## Cautions

- Coverage is a cooperation list, not a parsing feat: an agent that never runs checkpoints gets no attribution at all, so unsupported harnesses are invisible rather than miscounted.
- The teams platform is demo-gated with no published prices, and the install-base claims are the vendor's own.
- 261 open issues against 312 forks suggests a large installed base hitting edges quickly, and the project's future now follows an acquirer's roadmap.
- Web-UI squash and rebase merges need the CI Actions or the paid platform, so attribution can silently stop at the merge queue.

## Pricing

The CLI is free and open source under Apache-2.0.
The Git AI Platform for teams (prompt store, PR analytics, MDM rollout, self-hosted or cloud) is sold through demo bookings with no published prices, so pricing does not apply.

## Compared to

- [ctx](../ctx/index.md): the transcript-side blame, mapping a line, file, commit, or PR back to the session that produced it from your session store, while git-ai answers the same question from the repo permanently.
- [AgentTrace](../agenttrace/index.md): the local audit of what sessions cost and where they failed, with no authorship record; git-ai covers who wrote what, AgentTrace covers what it cost.
- [claude-devtools](../claude-devtools/index.md): the per-turn reconstruction of one Claude Code session on your machine, where git-ai keeps only the authorship thread but keeps it everywhere the repo goes.

## Bottom line

**Recommended for anyone who needs to know which agent, model, and prompt produced a line of code after the fact, and for teams measuring how much AI-written code survives review into production.**
Not for live observation, cost dashboards, or transcript search, and not for agents outside the checkpoint standard.

## Changes

- 2026-10-11 - Created from the 2026-10-11 re-evaluation of the 2026-10-10 control-planes rejection on the session-analytics provenance basis, with the OpenAI acquisition (announced 2026-09-11) recorded in Status.

## See also

- [ctx](../ctx/index.md) - the other provenance answer in this category, blaming from the transcript side instead of the repo side
- [AgentTrace](../agenttrace/index.md) - the cost and failure audit for the same sessions git-ai attributes
- [Session Analytics Feature Matrix](../session-analytics-feature-matrix/index.md) - the category comparison this note joins

## References

- https://api.github.com/repos/git-ai-project/git-ai - 2,829 stars, 312 forks, 261 open issues, Apache-2.0 license, Rust, created 2025-07-02, pushed 2026-10-07, as of 2026-10-11
- https://raw.githubusercontent.com/git-ai-project/git-ai/main/README.md - the mechanism, the 14-agent standard table, the capability and rewrite matrices, stats and blame commands, IDE plugins, and the FAQ
- https://usegitai.com/docs/cli/how-git-ai-works - the checkpoint, note-attachment, and rewrite mechanics, including the 5 to 100 millisecond consistency claim and the refs/notes/ai design
- https://usegitai.com/blog/git-ai-is-joining-openai - the OpenAI Codex team acquisition announced 2026-09-11 and the hundreds-of-thousands-of-machines claim
- https://usegitai.com - the enterprise surface: MDM rollout, PR-level percent-AI and cost views, the Fortune 100 claim, and Next Element, Inc. as the company
- https://api.github.com/repos/git-ai-project/git-ai/tags?per_page=5 - v1.7.5 as the newest tag behind the no-releases, install-script distribution
- https://api.github.com/repos/acunniffe/git-ai - the original owner's URL now resolving to git-ai-project/git-ai, grounding the repository transfer
- https://hn.algolia.com/api/v1/search?query=git-ai - the 6-point Show HN (2025-11-10) and the peer citations behind the thinner-than-adoption footprint claim, fetched 2026-10-11
