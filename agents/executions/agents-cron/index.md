---
title: agents-cron
created: 2026-11-08
updated: 2026-11-08
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, executions, cron, scheduling, self-hosted, local-first]
readability: 3
audience_notes: >
  Engineers who already run a coding agent CLI in a terminal and want scheduled prompt tasks to run unattended on their own machine, without a hosted service or a workflow platform.
  Assumes you know what a crontab, a headless CLI run, and an npm package are.
---

agents-cron is a local-first, AGPL-3.0 npm package that lets your existing crontab run due prompt tasks through a coding agent CLI (Pi built in, plus Claude Code and Codex adapters), giving every run its own isolated headless session instead of touching your interactive one.

## What it is

You write a task once (a prompt plus a time rule, never a shell command), and one global crontab line periodically invokes `agents-cron run-due`, which takes a run lock, filters due tasks, and drives each through an **Agent Adapter** that spawns the real binary: `pi --print`, `claude --print`, or `codex exec`.
The design rule the README leads with is "time is not ours": the scheduler never wakes itself, no daemon or timer exists, and the external cron decides when to look.
Task definitions live in a machine-wide registry at `~/.agents/cron/` (ADR 0007 since 0.9.0), bound to their project, while run records, reports, and session transcripts stay in each project's `.agents/cron/`; every scheduler file is written `0600`.
Management happens from three surfaces that never call each other: Pi slash commands (`/loop`, `/remind`, `/schedule`) and a deferred `schedule_task` tool, the CLI, and a read-only local web dashboard bound to 127.0.0.1.
Runs can announce themselves on webhook, email, or desktop-notification channels, error-only by default, and the extension is deliberately inert inside a task session so a scheduled run cannot schedule more work.
It is a single-maintainer TypeScript project by fookhsu, first published on npm as `@fookhsu/pi-scheduler` and renamed to `agents-cron` on 2026-10-18, with a stub package keeping old installs working.

## Status

**Active and shipping on a weekly release train, with a small but measurable install footprint.**
3 stars as of 2026-11-08 (GitHub API), 0 forks, 1 open issue, created 2026-09-10 and pushed 2026-11-05, with the default branch's head a same-day PR merge.
The npm package counts 4,185 downloads from 2026-10-08 to 2026-11-08 (dated-range query), and Pi's official package registry page reports 3,825/mo and 932/wk as of 2026-11-08, at version 0.16.1 published 2026-11-04.
The store has been migrated twice in a month of releases (`.pi/scheduler/` to `.agents/cron/` at 0.7.0, project files to the global registry at 0.9.0), both migrations are documented and automatic.
The default branch's latest work adds a "hybrid ask" that hands work over to an agents-pod pod, an early sign of a multi-agent direction.
The independent footprint is zero: no Hacker News thread as of 2026-11-08 searches (one incidental match in an unrelated Show HN), no blog write-ups, and the third-party listings that exist (omppackages, which marks it untested on omp) are directory automation, not coverage.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=fookhsu/agents-cron&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=fookhsu/agents-cron&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=fookhsu/agents-cron&type=date&legend=top-left" />
</picture>

## Strengths

- **Borrow the runtime instead of rebuilding it**: a task run is your already-configured `pi`, `claude`, or `codex` binary, so model, credentials, and project-trust rules are the ones you tuned, not a second SDK copy that drifts.
- One isolated session per run, never merged into your interactive session, and the no-fan-out rule (a scheduled run cannot schedule more work) closes the recursion failure mode most schedulers never name.
- State discipline is unusually careful for a one-person tool: run locks, stale-run reclaim, crash recovery, missed recurring windows collapsing into one catch-up run, per-run records plus Markdown reports, and idempotent exit codes.
- The adapter layer keeps the core agent-agnostic; adding a harness is one adapter directory and one `registerAgent` line, and the built-in adapters document their per-harness permission quirks (Claude Code denies un-allowlisted tools, Codex decides by sandbox).
- Notification routing is practical: per-task channels and levels, `chmod 600` config with secrets from the environment, a 10-second best-effort budget that never fails the run it reports on.

## Cautions

- **One maintainer, three stars, and no independent coverage as of 2026-11-08**; the npm install count is the only adoption evidence, and the repo-centric signals read near-zero.
- AGPL-3.0 is fine for a CLI you run but a real consideration for anyone embedding the scheduler core in a hosted product.
- Local-first means you own the crontab, Node >= 22.19.0, and the minimal-PATH footgun (cron strips PATH, so the docs make `AGENTS_CRON_PI_BIN` and friends a required ritual), with no managed service to fall back on.
- Imported or agent-created tasks run prompts with your credentials; import defaults to disabled and deletion asks for confirmation, but the review burden stays yours.
- The package moves fast and has relocated its store twice inside a month; the migrations are automatic and rollback-documented, but expect churn if you adopt early.

## Pricing

Free and open source under AGPL-3.0.
There is no hosted tier and no paid plan; your costs are the machine that runs cron, the model inference behind whichever harness adapter you pin, and any SMTP or webhook endpoint you wire for notifications.

## Compared to

- [Claude Code routines](../claude-code-routines/index.md): the hosted sibling; routines need no machine awake but keep schedules creator-private in Anthropic's cloud and lock you to Claude sessions, while agents-cron keeps everything on your machine and harness-agnostic.
- [Aeon](../aeon/index.md): the other cron-driven unattended agent, hosted in GitHub Actions with the repo as the deployment; Aeon suits repo-scoped chores you want in CI, agents-cron suits machine-local tasks that need your local files and CLIs.
- [Trigger.dev](../trigger-dev/index.md): the code-first durable platform for scheduling TypeScript functions inside applications; agents-cron schedules prompts rather than code and carries no platform of its own.

## Bottom line

**Recommended for engineers who already live in Pi, Claude Code, or Codex and want scheduled prompt tasks running on their own machine, isolated per run, without adopting a platform.**
Not for teams that need the schedule itself reviewed in git (GitHub Agentic Workflows and Aeon compile theirs into the repo), not for anyone unwilling to run a single-maintainer AGPL package, and not for machine-less setups.
My disagreeable claim: the borrow-the-runtime pattern here (spawn the CLI you already configured instead of wrapping an SDK) is the right default for every local agent scheduler, and schedulers that embed an SDK copy are maintaining a drifting shadow of a harness you already tuned.

## Changes

- 2026-11-08 - Created from the dedicated-list check's three-candidate resolution; admitted on the Airut small-maintainer precedent, with npm install telemetry as the adoption evidence the octopool ruling asks for.

## See also

- [Aeon](../aeon/index.md) - the Actions-hosted cron cousin, repo-as-deployment instead of local crontab
- [Claude Code routines](../claude-code-routines/index.md) - the hosted scheduled-session sibling, cloud convenience against local control
- [Airut](../airut/index.md) - the other single-operator self-hosted member, message-triggered instead of time-triggered
- [Trigger.dev](../trigger-dev/index.md) - the code-first durable alternative when schedules belong inside an application
- [Claude Code](../../harnesses/claude-code/index.md) - the most-attached harness behind this category's tools

## References

- https://api.github.com/repos/fookhsu/agents-cron - counters (3 stars, 0 forks, 1 open issue, created 2026-09-10, pushed 2026-11-05), TypeScript, AGPL-3.0, as of 2026-11-08
- https://raw.githubusercontent.com/fookhsu/agents-cron/main/README.md - the design rules, adapter layer, cron setup, storage layout, notifications, and rename history
- https://raw.githubusercontent.com/fookhsu/agents-cron/main/LICENSE - the AGPL-3.0 license text
- https://api.github.com/repos/fookhsu/agents-cron/commits?per_page=3 - default-branch activity, head at the 2026-11-05 agents-pod handover merge
- https://api.github.com/repos/fookhsu/agents-cron/tags?per_page=5 - the tag train, v0.16.1 down to v0.13.2
- https://registry.npmjs.org/agents-cron - the package record: latest 0.16.1, created 2026-10-18, last modified 2026-11-04
- https://api.npmjs.org/downloads/point/2026-10-08:2026-11-08/agents-cron - 4,185 downloads in the trailing month, dated-range query
- https://pi.dev/packages/agents-cron - Pi's official package page: version, 3,825/mo and 932/wk downloads as of 2026-11-08, extension and skill types, the rename note
- https://omppackages.com/packages/agents-cron - third-party directory listing, marked untested on omp
- https://hn.algolia.com/api/v1/search?query=%22agents-cron%22&tags=story - the coverage search finding no dedicated thread as of 2026-11-08
