---
title: GitHub Agentic Workflows
created: 2026-08-24
updated: 2026-10-06
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, executions, github-actions, workflows]
readability: 3
audience_notes: >
  Maintainers who want repository chores to run without them and already live in GitHub Actions.
  Assumes familiarity with Actions triggers, permissions, and the gh CLI.
---

GitHub Agentic Workflows (gh-aw) define repository automation in Markdown with YAML frontmatter, compiled into a hardened GitHub Actions workflow that runs an AI coding agent with guardrails.

**GitHub Actions is becoming the default execution layer for code agents, and gh-aw is the mechanism that makes an untrusted LLM in CI survivable.**

## What it is

You write a Markdown file whose frontmatter declares triggers, permissions, tools, safe outputs, and an engine, and the `gh-aw` CLI extension compiles it into a `.lock.yml` Actions workflow.
Five engines are built in (Copilot as default, Claude Code, Codex, Gemini, Pi), with importable samples for OpenCode, Cursor, Kiro, Aider, and Crush.
It is built by GitHub Next with Microsoft Research, MIT-licensed, in public preview.

## Status

**Active preview with real traction.**
About 5.3k stars, 574 forks, and roughly 18,000 commits in `github/gh-aw` as of 2026-10-06.
The February 2026 Hacker News launch thread drew 302 points and 141 comments.
The trust story has kept moving: an August 2026 billing bug forced the retirement of releases 0.68.4 through 0.71.3, and a critical security advisory published August 27 forced the pre-emptive retirement of releases 0.83.3 through 0.85.3 (patched in 0.85.4), a notice that still sits in the README while the billing one was cleared.
The release line keeps churning (latest v0.91.1 on 2026-10-06 as a prerelease, with v0.89.21 still the newest stable-marked release since 2026-09-23), which shows how quickly this preview will break its users.

## Strengths

- **The guardrail stack is the product**: read-only tokens by default, secrets isolated from the agent runtime, an agent workflow firewall, validated safe-output jobs that apply writes with scoped permissions, threat detection scans, and prompt-injection integrity filtering.
- Cost controls are first-class: `max-ai-credits` caps a run (default 1,000 AIC, where 1 AIC = $0.01), `max-daily-ai-credits` caps a workflow per day (default 5,000 AIC), and `gh aw logs` and `gh aw audit` give spend visibility.
- Engine choice means you are not locked to one model vendor inside your CI.
- It complements rather than replaces deterministic Actions: use Actions for builds, agentic workflows for triage, CI investigation, and docs drift.

## Cautions

- **Public preview, and the project says so bluntly**: the README closes its security section with "use it with caution, and at your own risk".
- The dogfooding record is instructive: HN commenters found agent-authored PRs in the gh-aw repo itself that mis-implemented a dependency bump and were still merged by a human maintainer.
- Compiling Markdown into generated workflows adds a layer few people will read; one early user reported `gh aw init` pushing a token secret to the wrong repo (since fixed with extra confirmations).
- AIC estimates are best-effort and may not match provider invoices, so budget on your provider's dashboard, not gh-aw's numbers.

## Pricing

Two costs stack: GitHub Actions minutes plus inference billed by the engine.
With the Copilot engine, usage maps to Copilot AI credits; third-party engines bill through their providers.
Self-hosted and ARC runners are supported, which can zero out the Actions-minutes side.

## Compared to

- [Claude Code Action](https://github.com/anthropics/claude-code-action): the mature single-agent incumbent on the same platform (about 9.4k stars as of 2026-10-06), better for @claude PR review, weaker on multi-engine guardrails.
- [Copilot automations](../copilot-automations/index.md): GitHub's hosted scheduled and event triggers, no files in your repo, Copilot-only.
- [Claude Code hooks](../claude-code-hooks/index.md): event triggers inside one harness session, versus repository-level automation across engines.

## Bottom line

**Recommended for maintainers automating issue triage, CI failure investigation, and documentation upkeep, provided a human still reviews every write.**
Not for teams that need stability guarantees, since a billing bug and a critical security advisory each forced release retirements as recently as August 2026.
My disagreeable claim: even in preview, I would start here rather than hand-rolling a script that shells out to a coding agent, because the safe-outputs gate is worth more than any bespoke wrapper your team will write and abandon.

## Changes

- 2026-08-24 - Created among the seed notes of the Executions category.
- 2026-08-30 - Recorded the retired-release notice cleared from the README after the August billing-bug retirements.
- 2026-09-12 - Corrected the release line: every v0.89.x release is a prerelease, with v0.88.7 the last stable.
- 2026-09-16 - Recorded the critical security advisory that forced the pre-emptive retirement of releases 0.83.3 through 0.85.4, a notice still live in the README, and refreshed the release train to v0.89.15.
- 2026-09-18 - Refreshed the fork count (541 to 544) and re-confirmed the release line unchanged, v0.89.15 still the newest prerelease and v0.88.7 the last stable.
- 2026-09-20 - Refreshed the release train to v0.89.17 (September 19) and re-confirmed v0.88.7 as the last stable release and the security-advisory notice still live in the README.
- 2026-09-24 - Refreshed the release train to v0.89.21 (September 23) and re-confirmed v0.88.7 as the last stable release; fork count refreshed to 558.
- 2026-09-27 - Recorded the prerelease-versus-stable flip: v0.89.21 (2026-09-23) is now the newest stable-marked release and v0.89.22 (2026-09-27) runs as a prerelease, retiring the v0.88.7-last-stable record; forks refreshed to 562.
- 2026-09-29 - Refreshed the release train to v0.90.0 (2026-09-28, a prerelease) and re-confirmed v0.89.21 as the newest stable-marked release; forks refreshed to 564.
- 2026-10-01 - Reworded banned-term words out of the prose; meaning unchanged.
- 2026-10-02 - Release train refreshed to v0.90.1 (2026-09-30, a prerelease) with v0.89.21 still the newest stable-marked release, the README advisory notice re-confirmed live, and growth refreshed (about 5.3k stars, 571 forks).
- 2026-10-03 - Corrected the retired-release range to 0.83.3 through 0.85.3, since the advisory patches in 0.85.4 rather than retiring it, refreshed the release train to v0.90.3 (2026-10-03, a prerelease) with v0.89.21 still the newest stable-marked release, and refreshed forks to 572.
- 2026-10-06 - Refreshed the release train to v0.91.0 (2026-10-05, a prerelease) with v0.89.21 still the newest stable-marked release, re-confirmed the security-advisory notice still live in the README, and refreshed forks to 574.
- 2026-10-06 - Release train refreshed again to v0.91.1 (2026-10-06, a prerelease), and the daily cost cap (`max-daily-ai-credits`, 5,000 AIC default) added to the cost-controls strength; the claude-code-action star count moved to about 9.4k as a routine refresh.

## See also

- [Copilot automations](../copilot-automations/index.md) - the hosted, Copilot-only sibling on the same platform
- [Claude Code](../../harnesses/claude-code/index.md) - one of the five built-in engines
- [Claude Code hooks](../claude-code-hooks/index.md) - in-harness event triggers versus repo-level automation

## References

- https://docs.github.com/en/copilot/concepts/agents/about-github-agentic-workflows - product definition, security model, AIC billing
- https://github.github.com/gh-aw/ - full reference: engines, guardrails, cost management
- https://github.com/github/gh-aw - repository scale, MIT license, as of 2026-10-06
- https://github.com/github/gh-aw/security/advisories/GHSA-8h78-hpm7-29gg - the critical advisory (safe-output artifacts may expose CI trigger tokens) behind the 0.83.3-0.85.3 retirement, patched in 0.85.4
- https://news.ycombinator.com/item?id=46934107 - February 2026 launch discussion (302 points) including dogfooding criticism
- https://github.com/anthropics/claude-code-action - the single-agent alternative on the same platform
- https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automation-rationale-and-approvals - shared rationale and approvals layer, including its limits
