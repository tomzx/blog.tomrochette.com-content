---
title: "Machinist"
created: 2026-09-05
updated: 2026-11-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, llm=glm-5.4, software-factory, orchestration, go]
readability: 3
audience_notes: >
  Engineers wiring coding agents into repeatable pipelines who want the control plane local and the agents swappable.
  Assumes you know what a worktree, a runner, and a pull request gate are.
---

**Machinist is an open-source software factory whose whole design keeps the controller out of the agent loop: a control plane that holds jobs and never starts an agent, runner daemons that dial out for work, and nothing arbitrary crossing the boundary.**

## What it is

A MIT-licensed Go control plane for coding-agent work on machines you own: the control plane holds jobs and presets and never starts an agent, while any number of runner daemons on Macs, VMs, or Kubernetes dial out, ask for work, and run it, per the README and configuration docs as of 2026-11-22.
A job runs a preset, a list of steps (clone, plan, build, test, review, open a pull request), where a step runs an agent (Claude Code, Codex, Pi, or Antigravity, each with its own model and prompt) or any shell command, and a test step is a gate an agent cannot skip; an agent is a folder of plain files (a playbook, a model, and the subagents and skills it can use), with a runner offering only the harnesses it holds credentials for.
Work arrives from the web app's New job form, through the run API from `curl`, from a tracker, a webhook, or an automation, or by assigning a Linear issue to the Machinist app (Linear off unless `linear.teams` is set); jobs run headless from start to finish and never stop to ask a question, guesses land under Assumptions in the pull request, and change requests or CI failures continue the same job on the same pull request per the redesign design document.
Defaults stay explicit: `run_timeout` defaults to sixty minutes, and the merge rule is code: the default preset ends in a `machinist merge` step that merges once the repository's checks pass and the review accepted the change, `github.auto_merge` on by default with `false` leaving every pull request open for a person, and branch protection still deciding what can merge.
The 2026-11-14 redesign replaced the vocabulary this note previously recorded from the 2026-10-15 app release (named commands over named repositories, a native-agents default run mode, a Codex-only gVisor runner target); the docs map now carries runners, credentials, factory files, a generic-runner design, and the redesign design document, and machinist.sh caught up on 2026-11-22 with Home, How it works, and Get started pages selling the same model, a four-harness roster, and docs pointed at the repository.

## Status

Active and early: created 2026-07-16, 502 stars and 96 forks as of 2026-10-13, releases v0.1.0 through v0.5.0 (v0.4.0 from 2026-08-31, v0.5.0 on 2026-11-22, v0.5.1 nightlies from 2026-11-24), and the README labeling it early-access software, per the GitHub API as of 2026-11-25.
**The 2026-11-14 redesign is the second step change and it kept moving: main, quiet since 2026-10-29 with the 2026-11-02 and 2026-11-09 pushes on side branches, took the tickets-runners-jobs merge (PR #585) on 2026-11-14, a setup-check fix (PR #589) on 2026-11-15, a PR-tracking merge (PR #614) on 2026-11-21, and then 394 commits past v0.4.0 by 2026-11-22 (true job figures in PR #644, the site split into Home, How it works, and Get started pages in PR #645), with no release past v0.4.0 at that reading; the README and docs now describe presets of steps, a four-harness roster (Claude Code, Codex, Antigravity, and Pi), headless runs that never stop to ask, a default-on `github.auto_merge` merge step with an opt-out, and Linear, tracker, webhook, and run-API intake, and machinist.sh caught up on 2026-11-22 after three weeks of serving the pre-redesign app description.**
**v0.5.0 (2026-11-22, published after that day's reading) is the first release past v0.4.0 and it ships the redesign: task workflows, review gates, and shared artifacts, the run API, the coding and hello presets, jobs shown as pipelines that run again, a Setup page, and Antigravity as a harness, with v0.5.1 nightlies from 2026-11-24 and main at 523 commits past v0.4.0 by 2026-11-25; main after them (unreleased) adds an LLM merge-gate step for risk-based auto-merge and a default merge policy refined for reversibility, per the release notes and commit history.**
The repository also ships an evals directory with a deterministic GitHub-issue-lifecycle evaluation, with broader outcome scoring documented as planned rather than shipped.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=owainlewis/machinist&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=owainlewis/machinist&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=owainlewis/machinist&type=date&legend=top-left" />
</picture>

**There is no Hacker News thread or independent coverage as of 2026-11-22, so the missing community footprint is itself the signal, and the repository plus the docs site at machinist.sh are the whole evidence base.**
The velocity (five releases in eight weeks) says maintained; the single-author commit history says bus-factor one.

## Strengths

- **The merge rule is code, not an agent**: the default preset's `machinist merge` step merges once the repository's checks pass and the review accepted the change, no agent decides what merges, and branch protection still gates the merge; the human gate is now an opt-out (`github.auto_merge: false`).
- **The control plane never starts an agent**: runner daemons dial out from machines you own, so work runs where the credentials and compute live, and the controller stays an observer.
- Candid about failure: a lost runner's ten-minute lease, the overlap window, and unpushed-work loss are documented, and the run timeout and the merge opt-out are plain settings rather than hidden behavior.

## Cautions

- **Headless by default and auto-merge on by default**: jobs never stop to ask a question (guesses land under Assumptions in the pull request) and the default preset merges its own pull requests once checks pass and review accepts, so a team that wants a human merge gate must set `github.auto_merge: false`; none of the redesign or its 2026-11-22 follow-ons is release-documented, with v0.4.0 predating all of it.
- Solo-maintainer risk on an early-access product, with no independent evaluation of the execution model yet.
- **Isolation rides the runners**: Kubernetes runners start one gVisor Job per run behind a gvisor RuntimeClass and NetworkPolicy CNI with an egress allowlist, local runners give each run a private home and an allowlisted environment, and the run's Job reads its GitHub and harness credentials from a Secret.
- The missing HN footprint cuts both ways: no drama, but also no second opinion.

## Pricing

Free and open source under MIT; you supply the machine and the model tokens.

## Compared to

- [Super Simple Software Factory](../super-simple-software-factory/index.md): the other code-owns-the-loop minimalism, but SSSF packages as a skill and binds to pi, while Machinist is a standalone Go control plane whose runners carry Claude Code, Codex, Antigravity, or Pi credentials.
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
- 2026-11-21 - Volatile re-verification: recorded the PR-tracking merge (PR #614) reaching 290 commits past v0.4.0 with v0.4.0 still the newest release, machinist.sh re-fetched and still serving the pre-redesign app description, and the zero-coverage claim re-run and holding to 2026-11-21; no material change.
- 2026-11-22 - Volatile re-verification on the push signal, and the model moved again: main reached 394 commits past v0.4.0 (PR #644's true job figures and PR #645's site split into Home, How it works, and Get started pages, with v0.4.0 still the newest release), the README now names a four-harness roster (Claude Code, Codex, Antigravity, and Pi), presets of steps, headless runs that never stop to ask (guesses under Assumptions in the pull request), a default-on `github.auto_merge` merge step the default preset ends in with `false` the opt-out, and Linear, tracker, webhook, and run-API intake (the `max_turns_without_human` cap and the GitHub bot-mention and MCP intake lines gone from the docs), and machinist.sh caught up, ending the two-surfaces disagreement recorded since the redesign; the What-it-is, Strengths, and Cautions rewritten to the current model and the configuration-doc reference updated; the zero-coverage claim re-run and holding to 2026-11-22.
- 2026-11-25 - Recorded v0.5.0 (2026-11-22, published after the 2026-11-22 reading) as the first release past v0.4.0, carrying the redesign (task workflows, review gates, shared artifacts, the run API, the coding and hello presets, Antigravity as a harness) with v0.5.1 nightlies from 2026-11-24, and the unreleased 2026-11-24 merge gate on main (an LLM merge-gate step for risk-based auto-merge, the default merge policy refined for reversibility); pushed date refreshed to 2026-11-24.

## See also

- [Software Factory Feature Matrix](../software-factory-feature-matrix/index.md) - where the control-plane-and-runners column sits among the factories
- [HAR](../har/index.md) - the isolation-first factory comparison
- [Super Simple Software Factory](../super-simple-software-factory/index.md) - the skill-packaged minimalism comparison
- [Executions Feature Matrix](../../executions/executions-feature-matrix/index.md) - scheduled triggers versus invoked factory runs

## References

- https://github.com/owainlewis/machinist - repository facts and license (GitHub API, as of 2026-11-15)
- https://raw.githubusercontent.com/owainlewis/machinist/main/README.md - the redesigned README: the control plane that never starts agents, runner daemons, presets of steps, the four-harness roster, headless runs and the Assumptions convention, the intake surfaces, and the `machinist merge` rule
- https://raw.githubusercontent.com/owainlewis/machinist/main/docs/runners.md - local and Kubernetes runners, the gVisor Job-per-run model with its RuntimeClass, NetworkPolicy, and egress allowlist, run leases, and credential Secrets
- https://raw.githubusercontent.com/owainlewis/machinist/main/docs/configuration.md - control plane and runner settings: the ticket database, `run_timeout`, the default-on `github.auto_merge` merge setting, and `linear.teams`
- https://machinist.sh - the docs site, caught up to the redesigned model on 2026-11-22 (Home, How it works, and Get started pages, the four-harness roster, docs pointed at the repository)
- https://api.github.com/repos/owainlewis/machinist/releases - the release list, v0.4.0 (2026-08-31) still the newest as of 2026-11-22
- https://api.github.com/repos/owainlewis/machinist/compare/v0.4.0...main - 394 commits past v0.4.0 as of 2026-11-22, the site-pages merge (PR #645) newest
- https://hn.algolia.com/api/v1/search?query=machinist&tags=story - the footprint scan finding no story about the repository (2026-11-22)
