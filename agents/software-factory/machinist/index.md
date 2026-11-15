---
title: "Machinist"
created: 2026-09-05
updated: 2026-11-15
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, software-factory, orchestration, go]
readability: 3
audience_notes: >
  Engineers wiring coding agents into repeatable pipelines who want the control plane local and the agents swappable.
  Assumes you know what a worktree, a runner, and a pull request gate are.
---

**Machinist is an open-source software factory whose whole design keeps the controller out of the agent loop: a control plane that holds tickets and never starts an agent, runner daemons that dial out for work, and nothing arbitrary crossing the boundary.**

## What it is

A MIT-licensed Go control plane for coding-agent work on machines you own: the control plane holds tickets, talks to GitHub, and never starts an agent, while any number of runner daemons on Macs, VMs, or Kubernetes dial out, ask for work, and run it, per the README and configuration docs as of 2026-11-15.
A job is a list of stages, an agent, another agent, or a script, and a script stage is a gate an agent cannot skip; an agent is a folder of plain files (a playbook, a model, and the subagents and skills it can use) that runs on Claude Code or Codex, with a runner offering only the harnesses it holds credentials for.
Work arrives by mentioning the bot on a GitHub issue, typing it into the web UI's one assignment box, or sending it from a coding session over MCP; the agent works on its own branch, opens one pull request, a fresh reviewer comments, and change requests or CI failures continue the same job on the same pull request, with the agent asking and waiting when it needs a decision.
Defaults stay explicit: `max_turns_without_human` caps agent runs since a person last said something at five, `run_timeout` defaults to sixty minutes, and the merge rule is that Machinist never merges unless an automation using an allowed agent does it (repository maintenance remains the opt-in exception that auto-merges only qualifying, independently reviewed Machinist documentation PRs under enforced branch protections).
The 2026-11-14 redesign replaced the vocabulary this note previously recorded from the 2026-10-15 app release (named commands over named repositories, a native-agents default run mode, a Codex-only gVisor runner target); the docs map now carries runners, credentials, factory files, and a redesign design document, while machinist.sh still served the pre-redesign app description as of 2026-11-15.

## Status

Active and early: created 2026-07-16, 502 stars and 96 forks as of 2026-10-13, releases v0.1.0 through v0.4.0 with v0.4.0 (2026-08-31) still the newest, and the README labeling it early-access software, per the GitHub API as of 2026-11-15.
**The 2026-11-14 redesign is the second step change: main, quiet since 2026-10-29 with the 2026-11-02 and 2026-11-09 pushes on side branches, took the tickets-runners-jobs merge (PR #585, a new UI among them) on 2026-11-14 and an agent-runner setup-check fix (PR #589) on 2026-11-15, reaching 201 commits past v0.4.0 with still no release past v0.4.0; the README and docs now describe a control plane that never starts agents, dial-in runner daemons, and jobs of agent and script stages, while machinist.sh still served the pre-redesign app description as of 2026-11-15.**
The repository also ships an evals directory with a deterministic GitHub-issue-lifecycle evaluation, with broader outcome scoring documented as planned rather than shipped.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=owainlewis/machinist&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=owainlewis/machinist&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=owainlewis/machinist&type=date&legend=top-left" />
</picture>

**There is no Hacker News thread or independent coverage as of 2026-11-15, so the missing community footprint is itself the signal, and the repository plus the docs site at machinist.sh are the whole evidence base.**
The velocity (five releases in eight weeks) says maintained; the single-author commit history says bus-factor one.

## Strengths

- **The merge rule is a hard gate**: Machinist never merges a pull request unless an automation using an allowed agent does it, and a script stage is a gate an agent cannot skip, a boundary that survived the redesign.
- **The control plane never starts an agent**: runner daemons dial out from machines you own, so work runs where the credentials and compute live, and the controller stays an observer.
- Candid about failure: a lost runner's ten-minute lease, the overlap window, and unpushed-work loss are documented, and a capped turn budget plus a run timeout are plain defaults rather than hidden behavior.

## Cautions

- Solo-maintainer risk on an early-access product, with no independent evaluation of the execution model yet.
- **Isolation rides the runners**: Kubernetes runners start one gVisor Job per run behind a gvisor RuntimeClass and NetworkPolicy CNI with an egress allowlist, local runners give each run a private home and an allowlisted environment, and the run's Job reads its GitHub and harness credentials from a Secret (the docs site still carries the older GitHub-publication-outside-Pods wording).
- **The redesign is one day old in the docs**: the README, docs map, and configuration guide describe the new model, while machinist.sh still sells the pre-redesign app (standard pipeline, executors TOML), so the two surfaces disagree until the site catches up.
- The missing HN footprint cuts both ways: no drama, but also no second opinion.

## Pricing

Free and open source under MIT; you supply the machine and the model tokens.

## Compared to

- [Super Simple Software Factory](../super-simple-software-factory/index.md): the other code-owns-the-loop minimalism, but SSSF packages as a skill and binds to pi, while Machinist is a standalone Go control plane whose runners carry Claude Code or Codex credentials.
- [HAR](../har/index.md): the fleet harness with per-agent worktree slots and a shared .har contract; HAR isolates more, Machinist gates the entrypoint more.
- [Fluent](../fluent/index.md): the self-improving alternative, when you want the factory to learn rather than just record.

## Bottom line

Recommended for engineers who want a local, auditable runner around agent CLIs and are comfortable being close to the only users.
Not for teams needing proven scale, resumable pipelines, or a community to escalate to.

## Changes

- 2026-09-05 - Created when the entrant-resolution run accepted it into Software factory for its named-command boundary.
- 2026-09-09 - Corrected the releases line to read v0.1.0 through v0.4.0.
- 2026-09-16 - Re-verified the zero-coverage claim and recorded growth to 418 stars with no new release.
- 2026-09-25 - Re-verified the zero-coverage claim and refreshed counts (458 stars, pushed 2026-09-24, 53 commits past v0.4.0, no new release).
- 2026-09-27 - Re-verified the zero-coverage claim and refreshed counts (463 stars, no new release).
- 2026-10-07 - Added the owainlewis/machinist star history chart to the Status section.
- 2026-10-16 - Recorded the 2026-10-15 step-change push (GitHub App onboarding, the local app's standard pipeline with triage, spec approval, independent review, and up to three repair rounds before human merge, scheduled automations, multi-repository projects, and the gVisor Kubernetes runner target) with 80 commits past v0.4.0 and still no release past v0.4.0; the isolation caution corrected and the zero-coverage claim re-verified to 2026-10-16.
- 2026-10-23 - Rotation re-verification: every cited URL re-fetched (repository README, machinist.sh, configuration.md, the workflows examples, the gVisor Kubernetes doc, the releases API, and the HN search) and all claims confirmed, with the zero-coverage claim holding to 2026-10-23; recorded 176 commits past v0.4.0 (still no release past v0.4.0), the native-agents default run mode with advisory child reviews, the evals directory's deterministic issue-lifecycle evaluation, and the opt-in repository-maintenance auto-merge limited to qualifying documentation PRs.
- 2026-10-28 - Rotation re-verification: every cited URL re-fetched (repository README, machinist.sh, configuration.md, the workflows examples, the gVisor Kubernetes doc, the releases API, and the HN search) and all claims confirmed, including v0.4.0 still the newest release, 176 commits past v0.4.0 with main's newest commit still 2026-10-21, and the zero-coverage claim holding to 2026-10-28; no material change.
- 2026-11-08 - Rotation re-verification: every cited URL re-fetched (repository via the API, machinist.sh, configuration.md, the workflows examples, the gVisor Kubernetes doc, the releases API, and the HN search) and all claims confirmed, including v0.4.0 still the newest release, 179 commits past v0.4.0 with main's newest commit still 2026-10-29 (the 2026-11-02 push a side branch), and the zero-coverage claim holding to 2026-11-08; no material change.
- 2026-11-14 - Volatile re-verification: v0.4.0 still the newest release and still 179 commits past it, main's newest commit still 2026-10-29 with the 2026-11-09 push another side branch, and the zero-coverage claim re-run and holding to 2026-11-14; no material change.
- 2026-11-15 - Out-of-rotation re-verification on the redesign signal: recorded the 2026-11-14 tickets-runners-jobs redesign (PR #585) and the 2026-11-15 agent-runner setup-check fix (PR #589), main at 201 commits past v0.4.0 with v0.4.0 still the newest release; the What-it-is and Status rewritten to the redesign model (a control plane that never starts agents, dial-in runners on Macs, VMs, or Kubernetes, jobs of agent and script stages, bot-mention, web-box, and MCP intake, same-job-same-pull-request repair, the `max_turns_without_human` cap and `run_timeout` default, merge only through automations using an allowed agent); the isolation caution moved to the gVisor Job-per-run model with the run's Secret-held credentials and the docs-site disagreement added as a caution; two dead source paths replaced (the gVisor doc moved to docs/runners.md, the workflows examples removed by the redesign) and the redesigned README, runners doc, configuration doc, and commit-range compare added to references; the zero-coverage claim re-run and holding to 2026-11-15.

## See also

- [Software Factory Feature Matrix](../software-factory-feature-matrix/index.md) - where the control-plane-and-runners column sits among the factories
- [HAR](../har/index.md) - the isolation-first factory comparison
- [Super Simple Software Factory](../super-simple-software-factory/index.md) - the skill-packaged minimalism comparison
- [Executions Feature Matrix](../../executions/executions-feature-matrix/index.md) - scheduled triggers versus invoked factory runs

## References

- https://github.com/owainlewis/machinist - repository facts and license (GitHub API, as of 2026-11-15)
- https://raw.githubusercontent.com/owainlewis/machinist/main/README.md - the redesigned README: the control plane that never starts agents, runner daemons, jobs and stages, the intake surfaces, and the merge rule
- https://raw.githubusercontent.com/owainlewis/machinist/main/docs/runners.md - local and Kubernetes runners, the gVisor Job-per-run model with its RuntimeClass, NetworkPolicy, and egress allowlist, run leases, and credential Secrets
- https://raw.githubusercontent.com/owainlewis/machinist/main/docs/configuration.md - control plane and runner settings: the ticket database, `max_turns_without_human`, and `run_timeout`
- https://machinist.sh - the docs site, still serving the pre-redesign app description (standard pipeline, executors TOML) as of 2026-11-15
- https://api.github.com/repos/owainlewis/machinist/releases - the release list, v0.4.0 (2026-08-31) still the newest as of 2026-11-15
- https://api.github.com/repos/owainlewis/machinist/compare/v0.4.0...main - 201 commits past v0.4.0 as of 2026-11-15, the redesign merge and the setup-check fix newest
- https://hn.algolia.com/api/v1/search?query=machinist&tags=story - the footprint scan finding no story about the repository (2026-11-15)
