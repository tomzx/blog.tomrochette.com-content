---
title: LongHorizon-Harness
created: 2026-10-13
updated: 2026-10-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, harness, computer-use, long-horizon, meta-harness]
readability: 3
audience_notes: >
  Engineers running agents on hours-long desktop and terminal work who want to know whether an audited outer loop is worth its token cost.
  Assumes you know what Claude Code, Codex CLI, and computer-use benchmarks are.
---

LongHorizon-Harness is MIT-licensed research code from Alibaba's DreamX team (the Amap ML organization) that turns existing agents into long-running computer-use systems through a Manage-Execute-Audit loop: a manager plans one bounded subtask at a time, a fresh-context executor performs it, and a read-only auditor certifies what actually changed before anything counts as progress.

**It is the meta-harness with an audit gate: four members of this very category (Claude Code, Codex, OpenCode, DeepSeek Harness) serve as its interchangeable backends, and only auditor-verified facts may enter the task state that survives between rounds.**

## What it is

A Python package (`uv tool install lh-harness`) that wraps existing agent CLIs through a lightweight AgentAdapter, preserving each backend's native loop while the harness controls context, permissions, budgets, and reporting.
The three roles can each use a different model or backend by configuration alone, with per-round budgets (1,800 seconds for the executor, 300 for manager and auditor) and a 25-round cap per task.
Execution spans desktop GUI (click, type, scroll) and terminal (code, commands, dependencies) in one continuous task, with a React/FastAPI web dashboard (`lh-harness web`) and per-run audit trails under runs/.
The accompanying paper (arXiv 2608.01964, submitted 2026-08-03) formalizes the loop as independently audited state transitions and reached #1 on the Hugging Face Daily Papers weekly ranking for 2026-W32.

## Status

Published, quiet for two months, then revived: 1,729 stars, 188 forks, and 43 open issues as of 2026-10-13, created 2026-08-04, with v0.1.7 on 2026-08-20 ending in an eight-week commit silence that v0.1.8 (published 2026-10-21) broke, the default branch pushed the same day (GitHub API, as of 2026-10-24).
The release train ran daily-to-weekly through August (v0.1.4 dashboard, v0.1.5 DeepSeek Harness support, v0.1.6 OpenCode support, v0.1.7 conversational follow-ups), stopped, and resumed on 2026-10-21 with v0.1.8, which fixed approvals after resuming historical runs (a resumed run no longer rejects approvals with HTTP 409, preserving its workspace, run ID, and round ledger), added Markdown-formatted Manager routes, Claude Code MCP isolation, non-UTF-8 CLI and DeepSeek output handling, and a configurable `--final-response-timeout` for slower closing replies.
Self-reported results: on WeaveBench, Qwen 3.7-Plus through Claude Code moves from 51.8 to 80.7 percent PassRate; Terminal-Bench 2.1 from 69.7 to 77.2 percent with 24 percent fewer tokens; OSWorld 2.0 binary completion from 2.8 to 8.3 percent, with gains carrying to Claude Opus 4.7.
PyPI downloads run about 1,000 per month as of 2026-10-13, and independent discussion is one 1-point Hacker News story.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=AMAP-ML/LongHorizon-Harness&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=AMAP-ML/LongHorizon-Harness&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=AMAP-ML/LongHorizon-Harness&type=date&legend=top-left" />
</picture>

## Strengths

- The audit gate is a real design contribution: the read-only auditor never sees the executor's reasoning, its reports are the only cross-round memory, and detected mutation is recorded as an integrity violation that cannot support completion.
- Fresh-context execution attacks context rot directly: each round starts clean, and only compact audit reports persist, so long-run degradation is bounded by design rather than by prompt tricks.
- Backend independence is genuine and current: Claude Code, Codex CLI, OpenCode, and DeepSeek Harness are all wired, each role assignable to a different model.
- The evaluation is unusually self-critical for a vendor report: the paper discloses that its WeaveBench runs use root privileges while official baselines use a regular user, and reports where the harness costs more tokens than it saves.
- Corporate provenance with a paper trail: an arXiv manuscript, a #1 weekly papers ranking, and a named team give the eight-week-old project unusual provenance for its size.

## Cautions

- A two-month commit and release silence (2026-08-20 to 2026-10-21) ended with a single patch release; one revival release is evidence of life, not of a restored cadence, so the archive-or-revive question stays live.
- The headline WeaveBench gain is against same-backbone baselines; the comparison with official leaderboard numbers crosses a privilege setting the paper itself flags as unmatched.
- Absolute computer-use numbers stay low (8.3 percent binary completion on OSWorld 2.0), so the loop multiplies a backbone's capability rather than replacing it.
- Token cost is backbone-dependent: 2.3 times baseline on WeaveBench and 3.6 times on OSWorld 2.0 output for Qwen 3.7-Plus, against a 24 percent saving on Terminal-Bench 2.1.
- Provenance concentration: one corporate lab, one paper, no external reproduction, and a community footprint of one 1-point Hacker News story.

## Pricing

Free and open source under MIT.
No hosted tier; cost is your own model bills, with the paper's token-share analysis (manager about 2 to 8 percent, auditor 19 to 38 percent) as the published cost expectation.

## Compared to

- [Omnigent](../omnigent/index.md): the other meta-harness, wrapping the same class of CLIs behind one API for governance and session sharing; Omnigent adds policy and sandboxes, LongHorizon-Harness adds the audited long-horizon loop.
- [Claude Code](../claude-code/index.md): the wrapped incumbent; use it directly for interactive work, and LongHorizon-Harness when tasks outlast context windows and unverified self-assessment is the failure mode.
- [Mini-SWE-agent](../mini-swe-agent/index.md): the minimal-loop contrast; Mini-SWE-agent is the baseline this category measures against, and LongHorizon-Harness is the argument that the loop, not the model, is what the baseline lacks.

## Bottom line

**Recommended for research and evaluation workloads with hours-long computer-use tasks, a strong wrapped backend, and tolerance for a self-reported evidence base.**
Not for production daily driving while the cadence question stays open after the two-month gap, and not for tasks whose bottleneck is model capability the loop cannot add.

## Changes

- 2026-10-13 - Created.
- 2026-10-24 - Rotation re-verification, re-fetching every cited reference (all live): recorded v0.1.8 (published 2026-10-21) ending the eight-week release silence with resumed-run approval fixes, Markdown Manager routes, Claude Code MCP isolation, and --final-response-timeout, and rewrote the Status, caution, and bottom line that had treated the project as silent.

## See also

- [Harness Feature Matrix](../harness-feature-matrix/index.md) - the category comparison this note joins
- [Omnigent](../omnigent/index.md) - the other harness-around-harnesses member, governance instead of auditing
- [Claude Code](../claude-code/index.md) - the primary executor backend it wraps
- [DeepSeek Harness](../deepseek-harness/index.md) - the phase-1 CLI backend it added in v0.1.5
- [The Agentic Development Environment Landscape](../../the-agentic-development-environment-landscape/index.md) - the tracker this section extends

## References

- https://api.github.com/repos/AMAP-ML/LongHorizon-Harness - repository metadata: MIT license, 1,729 stars, 188 forks, push and creation dates (as of 2026-10-13)
- https://api.github.com/repos/AMAP-ML/LongHorizon-Harness/readme - the README: MEA loop, backend table, benchmark table, news timeline, and install model
- https://api.github.com/repos/AMAP-ML/LongHorizon-Harness/releases?per_page=3 - the release record through v0.1.8 (published 2026-10-21, re-verified via GitHub API 2026-10-24)
- https://lh-harness.pages.dev - the project website: loop principles, benchmark detail, token-cost analysis, and the DreamX Team footer
- https://arxiv.org/abs/2608.01964 - the paper abstract: MEA formalization, headline benchmark numbers, and submission date
- https://huggingface.co/papers/2608.01964 - the paper full text (served via Hugging Face Daily Papers): the DreamX Team, Alibaba Group affiliation, per-role budgets, and the disclosed root-privilege caveat
- https://api.github.com/orgs/AMAP-ML - the publishing organization: display name DreamX, 51 public repositories
- https://pypistats.org/api/packages/lh-harness/recent - the 1,048 downloads in the last month as of 2026-10-13
- https://hn.algolia.com/api/v1/search?query=%22long-horizon%22%20harness&hitsPerPage=8 - the thin independent-discussion record: one 1-point story, no comment thread
