---
title: CC Safety Net
created: 2026-10-07
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, control-planes, policy-enforcement, guardrails, security, open-source]
readability: 3
audience_notes: >
  Engineers who run AI coding agents on their own machine and want destructive commands and secret reads blocked before they execute.
  Assumes you know what a PreToolUse hook is and the difference between a policy gate and a sandbox.
---

CC Safety Net (Coding CLI Safety Net) is an MIT pre-execution guard that parses each command or file access an AI coding agent is about to make and blocks destructive git and filesystem operations plus secret-file reads before the tool call runs.

**Its design point is parse-then-decide: it reads what a command would actually do, so wrapping it or reordering flags does not sneak past, and it fails open on its own breakage (a broken config never blocks anything), the opposite trade from the sandboxes it explicitly says it is not.**

## What it is

A TypeScript CLI installed with `npx cc-safety-net install` into the hook surface of sixteen coding-agent CLIs, including Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot CLI, OpenCode, OpenClaw, Hermes Agent, Kimi Code, Pi, DeepSeek Harness, Amp Code, Antigravity CLI, Devin CLI, Factory Droid, and Grok Build, on Windows, macOS, and Linux.
Blocked by default are destructive commands (`git reset --hard`, `git push --force`, `rm -rf` on dangerous targets, including inside `bash -c` or `python -c`) and secret access (SSH keys, `.env` files, `~/.aws`, coding-CLI credentials) from both the shell and the agent's file tools.
Policy is tuned through a GUI (`npx cc-safety-net gui`) across Standard, Strict, and Paranoid presets, extended through official rulebooks (Terraform, AWS, gcloud, Azure) or your own JSON, and shared by committing the `.cc-safety-net/` directory so clones and cloud sessions inherit the same rules; a `checkCommand` library API embeds the engine in other tools.
It states plainly that it is not a sandbox: it contains no processes, sets no filesystem permissions, and watches no network egress.
MIT, single-repo open source, with full documentation at ccsafetynet.com.

## Status

Actively maintained with no Hacker News help: 1,579 stars, 84 forks, 9 open issues and PRs as of 2026-10-07, created 2025-12-25, pushed 2026-10-07.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=kenryu42/cc-safety-net&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=kenryu42/cc-safety-net&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=kenryu42/cc-safety-net&type=date&theme=dark&legend=top-left" />
</picture>

The npm package (`cc-safety-net`) is at 2.6.0 as of 2026-10-07, first published 2026-01-03 and last published 2026-10-05, so the release cadence is measured in days.
**A Hacker News search returns zero threads as of 2026-10-07, so ten months of growth came through npm and GitHub alone, and the missing community footprint means the security claims have no public adversarial review I could find.**

## Strengths

- Command parsing rather than pattern matching: reordering flags or hiding the payload in `bash -c` or `python -c` does not evade the check.
- Sixteen harness surfaces behind one install command, with policy distributable through the repo itself, which fits how teams already sync tool config.
- The GUI preset ladder (Standard, Strict, Paranoid) and rulebook packs make the policy approachable without reading YAML.
- The fail-open stance is stated up front, which is more candor than most guards offer about their own failure mode.

## Cautions

- It decides before execution and contains nothing after, so it complements rather than replaces an isolation boundary, and the README says so itself.
- Fail-open cuts both ways: a crashed or bypassed guard stops protecting silently, which is the wrong default for a threat model where the agent is adversarial rather than merely error-prone.
- Zero Hacker News footprint and no independent audit; the claims about parsing resistance are the project's own.
- The npm path has its own wrinkle the README warns about: a bare `cc-safety-net` spec can resolve a stale copy from the npx cache, so the `@latest` qualifier matters.

## Pricing

Free and open source under MIT, no paid tiers or hosted offering found as of 2026-10-07.

## Compared to

- [Veto](../veto/index.md): the same enforcement point (before the tool handler runs) with a different scope and audit depth, since Veto adds an allow/warn/require-approval ladder, approval routing, and offline-verifiable receipts for money-and-data actions, while CC Safety Net guards a workstation's git and secrets with none of that machinery.
- [OpenAPPA](../openappa/index.md): information-flow policy over what an agent reads, in-process or as a sidecar; CC Safety Net is a command-surface hook with secret-path denial, not a labeling engine.
- [Microsoft Agent Governance Toolkit](../microsoft-agent-governance-toolkit/index.md): the heavier multi-language program with policy engines, identity, and compliance; choose it for org-scale governance, CC Safety Net for a same-hour personal guardrail.

## Bottom line

**Recommended for developers who want destructive-command and secret-access guardrails across many agent CLIs on their own machine, installed in one command, accepting that the guard is a hook and not a boundary.**
Not for org-scale governance, audited enforcement, or anything where a silently crashed guard is unacceptable.

## Changes

- 2026-10-07 - Created from the daily-refresh entrant resolution, profiling the parse-then-decide pre-execution guard and its zero-HN footprint.

## See also

- [Control Planes Feature Matrix](../control-planes-feature-matrix/index.md) - the category comparison this note joins
- [Veto](../veto/index.md) - the same enforcement point with approval workflow and receipts
- [OpenAPPA](../openappa/index.md) - the information-flow alternative over what agents read
- [Sandboxing Feature Matrix](../../sandboxing/sandboxing-feature-matrix/index.md) - the boundaries this guard explicitly is not

## References

- https://github.com/kenryu42/cc-safety-net - repository: mechanism, supported CLIs, features, license
- https://raw.githubusercontent.com/kenryu42/cc-safety-net/main/README.md - the README whose mechanism and feature claims this note traces to
- https://ccsafetynet.com/docs - the documentation site (a client-rendered shell to fetchers, so linked rather than quoted)
- https://api.github.com/repos/kenryu42/cc-safety-net - stars, issues, creation and push dates as of 2026-10-07
- https://registry.npmjs.org/cc-safety-net - the 2.6.0 latest tag, first-publish and last-publish dates as of 2026-10-07
- https://hn.algolia.com/api/v1/search?query=%22cc-safety-net%22&tags=story - the zero-thread footprint check as of 2026-10-07
