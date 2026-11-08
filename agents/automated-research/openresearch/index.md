---
title: OpenResearch
created: 2026-10-05
updated: 2026-11-08
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

Active and fast-moving: 7,234 stars as of 2026-10-21, 507 forks, 109 open issues and pull requests as of 2026-10-31, created 2026-06-07, last pushed 2026-11-08, with v0.2.25 (November 7) the latest stable release, its November 5-7 train sharing projects as `.orx` files and publishing them as openresearch.sh links, onboarding switching to sign-in with alphaXiv instead of a research profile, workspace-wide chat history search, `orx up --host 0.0.0.0` for a trusted LAN, rented boxes running under orx-host, and a run of Windows fixes (SSH logins kept across restarts, LF bytes preserved in source snapshots, hard-link fallbacks, SSH runs for normal users), with post-release fixes keeping chat image carousels mounted, creating the private runtime dir atomically, embedding release hosts in the telemetry check, and letting message boxes grow with their text, and a canary prerelease channel live, following v0.2.24's (November 4) engine rewrite (#862), subagent rework (#885), and composer rebuild, and v0.2.22 (October 28) and v0.2.21's October Trackio widening to Spaces, Hugging Face runs, and orx metrics and the configurable remote storage root, as of 2026-11-08.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=alphaXiv/OpenResearch&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=alphaXiv/OpenResearch&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=alphaXiv/OpenResearch&type=date&legend=top-left" />
</picture>

Traction is GitHub-native rather than press-driven: Trendshift records the repository reaching #1 on GitHub Trending on September 11, then #1 Repository of the Day and #2 Repository of the Week in week 38, with 33 contributors.
The pattern continues on its own: the star count rose about 300 in the two days after October 13 with no new Hacker News story and no press, as of 2026-10-15.
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
- 2026-10-07 - Added the alphaXiv/OpenResearch star history chart to the Status section.
- 2026-10-10 - Recorded the v0.2.18 release (October 9) and refreshed the volatile counts.
- 2026-10-12 - Refreshed the volatile counts; v0.2.18 remains the latest release.
- 2026-10-23 - Refreshed the status: v0.2.21 (October 23) the latest release, its train widening the Trackio integration to Spaces, Hugging Face runs, and orx metrics and making the SSH and Slurm storage root configurable, with the fork and open-issue counts moved.
- 2026-10-28 - Refreshed the status: v0.2.22 (October 28) the latest release, its train adding permanent experiment delete, shared SSH monitoring with backoff, stable and canary desktop update channels, openresearch:// paper deep links on macOS, and a CITATION.cff acknowledgment in orx-paper, with the fork and open-issue counts moved.
- 2026-10-31 - Recorded the v0.2.23 release (October 31), its 32-commit train shipping native skill discovery for every supported agent, openresearch:// deep links on Windows and Linux, keyboard navigation and application menus, a shared Base UI dialog system, oh-my-pi among the preconfigured coding agents, and desktop polish, with the push and open-issue counts moved.
- 2026-11-07 - Recorded the v0.2.25 release (November 7) and its November 5-7 train: project sharing as `.orx` files and openresearch.sh publish links, alphaXiv sign-in onboarding, workspace-wide chat history search, trusted-LAN `orx up`, orx-host rented boxes, and the Windows SSH and snapshot fixes, with the push date moved.

## See also

- [Agon](../agon/index.md) - the paper-artifact loop OpenResearch turns into a runnable workspace
- [Karpathy Autoresearch](../karpathy-autoresearch/index.md) - the founding loop this product industrializes
- [OpenAI Deep Research](../openai-deep-research/index.md) - the productized, prose-only counterpart
- [Pion](../pion/index.md) - the closed loop whose judge is a bank account
- [Automated Research Feature Matrix](../automated-research-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/alphaXiv/OpenResearch - README: harness support, the autoresearch loop, worktrees, experiment tree, run-anywhere list, telemetry policy, local-first store, and the remote no-auth admission (fetched 200, 2026-10-05)
- https://api.github.com/repos/alphaXiv/OpenResearch - forks, open issues, created and push dates, and the MIT license, with the star figure left at its 2026-10-21 baseline (fetched 200, 2026-10-30)
- https://api.github.com/repos/alphaXiv/OpenResearch/commits?since=2026-11-05T00:00:00Z&per_page=30 - the November 5-7 commits behind this refresh: project sharing and publish links, alphaXiv sign-in, chat history search, the trusted-LAN host flag, orx-host boxes, and the Windows fixes (fetched 200, 2026-11-07)
- https://api.github.com/repos/alphaXiv/OpenResearch/commits?since=2026-11-07T00:00:00Z&per_page=10 - the November 7-8 post-release fixes behind the push-date move, message boxes growing with their text the latest (fetched 200, 2026-11-08)
- https://api.github.com/repos/alphaXiv/OpenResearch/releases/latest - v0.2.25 (2026-11-07) the latest stable release, with the canary prerelease channel above it (fetched 200, 2026-11-07)
- https://api.github.com/repos/alphaXiv/OpenResearch/compare/v0.2.21...v0.2.22 - the v0.2.22 commit train behind the release description: experiment delete, SSH-monitor sharing and backoff, desktop update channels, deep links, and skill-discovery fixes (fetched 200, 2026-10-28)
- https://api.github.com/repos/alphaXiv/OpenResearch/compare/v0.2.22...v0.2.23 - the 32-commit v0.2.23 train behind this refresh: skill discovery, Windows and Linux deep links, menus, the dialog system, oh-my-pi, and desktop polish (fetched 200, 2026-10-31)
- https://api.github.com/repos/alphaXiv/OpenResearch/releases?per_page=3 - v0.2.23 (2026-10-31) the latest stable release above v0.2.22, with the canary channel at canary-20261031.3 (fetched 200, 2026-10-31)
- https://openresearch.sh/ - positioning ("autoresearch on your machine"), the alphaXiv project attribution, and the compute marketplace (fetched 200, 2026-10-05)
- https://openresearch.sh/docs - the compute marketplace overview: provider comparison, provisioning, and the orx CLI (fetched 200, 2026-10-05)
- https://openresearch.sh/docs/billing - provider-rate pass-through with no markup, prepaid balances, and zero-balance termination (fetched 200, 2026-10-05)
- https://trendshift.io/repositories/89363 - GitHub Trending #1 on September 11, #1 Repository of the Day, #2 Repository of the Week in week 38, 33 contributors (fetched 200, 2026-10-05)
- https://hn.algolia.com/api/v1/search?query=%22OpenResearch%22 - the two small HN stories (6 points in June, 1 point with zero comments in September) recording the absent debate footprint (fetched 200, 2026-10-05)
