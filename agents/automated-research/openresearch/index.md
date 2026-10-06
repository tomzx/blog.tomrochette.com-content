---
title: OpenResearch
created: 2026-10-05
updated: 2026-10-06
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, automated-research, open-source, autoresearch, multi-agent, alphaXiv]
readability: 3
audience_notes: >
  Engineers who want to run autonomous research loops on their own coding agents, repositories, and compute.
  Assumes you know what a git worktree, an experiment harness, and a coding agent are.
---

OpenResearch is alphaXiv's MIT-licensed, local-first workspace that turns Claude Code, Codex, OpenCode, Cursor, or Google Antigravity into research agents with isolated worktrees, a git-native experiment tree, and an autonomous mode that proposes, runs, and selects its own next experiments.

**OpenResearch is the first entry in this category an engineer can run end to end today: the loop, the lineage, and the compute all live on your machine, which makes it the engineering-grade implementation of the Agon lineage rather than a paper artifact.**

## What it is

A desktop app (macOS, Windows beta, Linux AppImage) plus the `orx` CLI, built by alphaXiv, the company behind the arXiv discussion layer.
Each research direction gets its own agent session in an isolated git worktree, and every run archives an immutable snapshot of its recorded commit, so experiments form a lineage tree instead of a scrollback buffer.
The autonomous mode runs the full loop: propose an idea, change the code, launch an experiment, inspect the evidence, and decide what to try next, with multiple agents exploring directions in parallel.
Runs execute locally, over SSH, or on Slurm, Kubernetes, Ray, Hugging Face Jobs, Modal, or Tinker, or on OpenResearch's own compute marketplace, which aggregates provider offers and bills at provider rates.
The agent-facing surface is first-class: `orx install-skills` installs a skill into supported agents, and the repository ships SKILL.md, SYSTEM_PROMPT.md, AGENTS.md, and CLAUDE.md in-tree.

## Status

Active and fast-moving: 6,642 stars, 420 forks, 66 open issues and pull requests, created 2026-06-07, last push 2026-10-06, with releases v0.2.13 through v0.2.16 landing between September 29 and October 5, as of 2026-10-06.
Traction is GitHub-native rather than press-driven: Trendshift records the repository reaching #1 on GitHub Trending on September 11, then #1 Repository of the Day and #2 Repository of the Week in week 38, with 33 contributors.
**The Hacker News footprint is nearly absent, and that is itself the signal: a 6-point June story and a 1-point September 30 story with zero comments, as of 2026-10-05, so adoption is spreading through GitHub without any critical public debate yet.**

## Strengths

- The loop is inspectable end to end: worktrees, experiment lineage, and archived commits are all plain git a human can diff.
- Harness-agnostic (five agents) and compute-agnostic (laptop to Slurm to a provider marketplace), so the loop is not locked to one vendor.
- Local by default: a SQLite store on 127.0.0.1, coarse opt-out telemetry tied to a random installation ID, and no telemetry from source builds.
- It treats evidence as a first-class artifact, keeping logs, diffs, files, and results tied to the run that produced them.

## Cautions

- The README's own security note is the sharpest critique available: the remote mode's service binds to loopback with no application-level authentication, so other users on that host can reach it.
- No independent evaluation of the autonomous loop exists; with zero HN comments there is no third-party read on how often the loop's decide-what-to-try-next step is actually good.
- Young and churny: a 0.2.x codebase releasing every few days, a beta Windows installer that is still unsigned, and a CLI that is not yet code-signed on macOS.
- The compute marketplace adds an account, a prepaid organization balance, and a billing relationship on top of the local-first story, and a non-positive balance terminates running hosted instances.

## Pricing

Free and open source under MIT.
The optional compute marketplace and managed compute bill at the underlying provider rate with no OpenResearch markup, prepaid through an organization balance, so no OpenResearch prices are stated.

## Compared to

- [Agon](../agon/index.md): both run producer loops toward experiments and papers; Agon is a Claude Code plugin surface meant to run unattended, OpenResearch is an app-grade workspace with experiment lineage where you steer per direction. Choose Agon to study loop failure modes, OpenResearch to run loops on your own repos and GPUs.
- [OpenAI Deep Research](../openai-deep-research/index.md): the productized prose loop with no code execution; OpenResearch runs experiments and produces artifacts, and costs compute instead of a subscription.
- [Pion](../pion/index.md): the other loop judged by outcomes, closed and operator-run; OpenResearch is the open mirror whose operator is you, with an evidence tree instead of a bank account as the judge.

## Bottom line

**Recommended for engineers and researchers who want the autonomous-research loop running on their own agents, repositories, and compute today, with every intermediate artifact inspectable in git.**
Not for anyone who needs a supported product, a security-reviewed remote deployment, or independently validated autoresearch results, none of which exist yet as of 2026-10-05.

## Changes

- 2026-10-05 - Created.

## See also

- [Agon](../agon/index.md) - the paper-artifact loop OpenResearch turns into a runnable workspace
- [OpenAI Deep Research](../openai-deep-research/index.md) - the productized, prose-only counterpart
- [Pion](../pion/index.md) - the closed loop whose judge is a bank account
- [Automated Research Feature Matrix](../automated-research-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/alphaXiv/OpenResearch - README: harness support, the autoresearch loop, worktrees, experiment tree, run-anywhere list, telemetry policy, local-first store, and the remote no-auth admission (fetched 200, 2026-10-05)
- https://api.github.com/repos/alphaXiv/OpenResearch - stars, forks, open issues, created and push dates, and the MIT license (fetched 200, 2026-10-05)
- https://api.github.com/repos/alphaXiv/OpenResearch/releases - v0.2.15 (2026-10-02) and the release cadence across late September (fetched 200, 2026-10-05)
- https://openresearch.sh/ - positioning ("autoresearch on your machine"), the alphaXiv project attribution, and the compute marketplace (fetched 200, 2026-10-05)
- https://openresearch.sh/docs - the compute marketplace overview: provider comparison, provisioning, and the orx CLI (fetched 200, 2026-10-05)
- https://openresearch.sh/docs/billing - provider-rate pass-through with no markup, prepaid balances, and zero-balance termination (fetched 200, 2026-10-05)
- https://trendshift.io/repositories/89363 - GitHub Trending #1 on September 11, #1 Repository of the Day, #2 Repository of the Week in week 38, 33 contributors (fetched 200, 2026-10-05)
- https://hn.algolia.com/api/v1/search?query=%22OpenResearch%22 - the two small HN stories (6 points in June, 1 point with zero comments in September) recording the absent debate footprint (fetched 200, 2026-10-05)
