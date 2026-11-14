---
title: Open-Inspect
created: 2026-11-07
updated: 2026-11-14
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, software-factory, background-agents, self-hosted, multi-agent]
readability: 3
audience_notes: >
  Engineers who want Ramp's Inspect pattern self-hosted: background sessions from Slack, GitHub, and
  Linear that return attributed pull requests. Assumes you know what a sandbox, a GitHub App, and a team are.
---

Open-Inspect is an MIT-licensed, self-hosted background coding agent inspired by Ramp's Inspect: sessions take work from a web UI, Slack, GitHub pull requests, Linear issues, or webhooks, and return pull requests with commit attribution to the person who prompted them.

## What it is

**The Ramp-Inspect pattern published as an open system: Modal-style sandboxed sessions, multiplayer editing, per-prompt attribution, and your existing model subscriptions.**
A deployment is single-tenant by design (a Terraform guide for full infrastructure, a separate guide for local development), with each session running in a sandboxed environment carrying Node.js, Python, git, browser automation, and VS Code.
Sessions support live multiplayer collaboration, parallel sub-tasks in separate sandboxes, cron automations, and event-driven automations for GitHub events, Sentry alerts, and webhooks.
Model access rides subscriptions as well as keys: Claude by API key or a connected Claude subscription, Codex through a ChatGPT subscription, Grok through SuperGrok, or OpenCode Zen.
The project has 55 contributors and bilingual English and Chinese documentation.

## Status

Young but growing: 3,467 stars since creation on 2026-01-25, pushed 2026-11-14, MIT, per the GitHub API as of 2026-11-14.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=open-inspect/background-agents&type=date&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=open-inspect/background-agents&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=open-inspect/background-agents&type=date&legend=top-left" />
</picture>

**There is no release train and no independent coverage: the repository publishes no GitHub release tags, so deployments track main, and a Hacker News search returns no story about it (2026-11-14).**
The missing community footprint is itself the signal this note states, and the documentation is the counterweight: the security model, getting-started, and setup guides read as production runbooks, down to credential scoping, enforcement modes, and break-glass read paths.

## Strengths

- **Sandbox credentials are scoped per session**, covering the session's granted repositories and failing closed when grants cannot be resolved, a tighter default than the installation-wide credentials most platform factories hand out.
- Per-prompt commit attribution means the pull request names the human who asked, so review authority stays with people, not the app.
- Candid single-tenant trust documentation: the guides state plainly that all users share the deployment's GitHub App installation and that teams add internal access controls, not tenant isolation.
- Automations cover the operational edges: cron jobs, GitHub events, Sentry alerts, and webhooks, which most members of this category leave to external schedulers.

## Cautions

- **No release tags exist**: a deployment tracks main, so there is no pinned, upgradeable version line.
- Single-tenant only by design, and GitLab deployments fall back to one deployment-wide PAT, a weaker credential boundary the docs admit.
- Zero independent coverage as of 2026-11-08; the evidence base is the repository and its documentation.
- The infrastructure burden is heavy: full deployments go through Terraform, GitHub Apps, and sandbox images, closer to platform engineering than to installing a CLI.
- Acceptance is human review of the attributed pull request; no built-in acceptance gate exists.

## Pricing

MIT, free, and self-hosted on your own cloud, with your model subscriptions or API keys as the running cost.
There is no hosted tier and no published prices as of 2026-11-07.

## Compared to

- [Open SWE](../open-swe/index.md) is the closest peer: LangChain's Robin needs LangSmith's Managed Deep Agents to run as-is, while Open-Inspect runs its own harness and routes your existing Claude, Codex, and Grok subscriptions.
- [SuperPlane](../superplane/index.md) owns the intake-to-PR line as a platform with confidence-gated backlog intake and durable run records; Open-Inspect is session-first and leaves confidence scoring out.
- [Fusion](../fusion/index.md) is board-first and local-node-first with per-step gates; Open-Inspect is chat-and-tracker-first and sandbox-first, with no local mode.

## Bottom line

**Recommended for a team that wants the Ramp-Inspect loop, background sessions to attributed pull requests, on its own infrastructure with per-session scoped credentials, and accepts tracking main with no release train.**
Not for multi-tenant use, which the design excludes, and not for anyone who needs third-party validation or pinned releases first.
My disagreeable claim: per-session credential scoping makes Open-Inspect the safest default in this category's platform tier, and it deserves coverage proportional to its stars.

## Changes

- 2026-11-07 - Created from the awesome-software-factories 2026-11-05 weekly sweep, clearing the bar on the Open SWE intake-to-PR line with the zero-coverage footprint recorded.
- 2026-11-08 - Corrected the HN footprint reference, which cited the search at a news.ycombinator.com API host that returns 404 (the canonical Algolia host replaces it); the pushed date refreshed to 2026-11-08 and the empty release train and zero-coverage claims re-verified.
- 2026-11-14 - Volatile re-verification: pushed date refreshed to 2026-11-14, the release list still empty, and the zero-coverage search re-run and holding; no material change.

## See also

- [Open SWE](../open-swe/index.md) - the LangChain platform peer this note's subscription-routed model is measured against
- [SuperPlane](../superplane/index.md) - the confidence-gated platform factory comparison
- [Fusion](../fusion/index.md) - the board-first, local-node comparison
- [Software Factory Feature Matrix](../software-factory-feature-matrix/index.md) - where the background-session column sits among the factories

## References

- https://github.com/open-inspect/background-agents - the README: the loop, intake surfaces, model routing, and the single-tenant security model
- https://github.com/open-inspect/background-agents/blob/main/docs/GETTING_STARTED.md - the deployment runbook: Terraform, scoped sandbox credentials, fail-closed resolution, and the GitLab PAT caveat
- https://api.github.com/repos/open-inspect/background-agents/releases - the empty release list grounding the no-release-train caution
- https://hn.algolia.com/api/v1/search?query=open-inspect&tags=story - the footprint scan finding no story (2026-11-14)
- https://builders.ramp.com/post/why-we-built-our-background-agent - Ramp's Inspect post, the pattern this project replicates, with its sandbox, attribution, and multiplayer design
