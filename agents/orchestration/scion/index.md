---
title: Scion
created: 2026-10-06
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, containers, isolation, control-plane, google]
readability: 3
audience_notes: >
  Engineers deciding where agent isolation should live, who can weigh a corporate testbed against a supported product.
  Assumes you know what containers, git worktrees, and a control plane are.
---

Scion is GoogleCloudPlatform's Apache-2.0 "hypervisor for agents": a Hub control plane over runtime brokers that runs coding agents in containers with per-agent worktrees and credentials, scaling from a laptop to highly available hosted deployments.

**Scion is the only hyperscaler-backed column in this category, and the most credible thing about it is Google's own label: an experimental testbed that is not an officially supported product, which makes it a public architecture lab rather than something to standardize on.**

## What it is

A container-first orchestration platform that runs each agent in its own container with its own git worktree, configuration, and credentials, so parallel agents cannot corrupt each other's work.
The control plane is the Hub; the execution layer is runtime brokers managing containerized agents over Docker, Podman, Apple Container, Kubernetes, or Cloud Run.
Run modes ladder from Local (CLI only, no server) through Workstation (a combo server on your own machine) to Single-node and HA hosted (Cloud Run plus GKE), and the same `scion` CLI drives all of them.
It ships Gemini CLI and Claude Code harnesses by default, with Codex, OpenCode, and Antigravity available as opt-in bundles, the first two only partially supported.

## Status

Active and early: 1,730 stars and 272 forks as of 2026-10-06, created 2026-03-10, with 32 contributors and nightly releases.

<a href="https://www.star-history.com/?repos=GoogleCloudPlatform%2Fscion&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=GoogleCloudPlatform/scion&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=GoogleCloudPlatform/scion&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=GoogleCloudPlatform/scion&type=date&legend=top-left" />
 </picture>
</a>

The README states plainly that Scion is not an officially supported Google product and is not eligible for Google's support programs.
InfoQ's April 2026 coverage framed it as an experimental testbed with partial Codex and OpenCode support and documented its idiosyncratic lexicon (grove, hub, runtime broker).
The 230-point, 62-comment Hacker News thread from April 2026 is the largest practitioner debate in this category.

## Strengths

- The strongest isolation story in the matrix: container plus worktree plus credentials per agent, where most columns offer a worktree alone and OpenRig shares the host.
- A run-mode ladder no other column has: the identical CLI from a laptop with no server to HA on GCP.
- Google engineering and nightly releases behind an Apache-2.0 codebase, with harnesses swapped through configuration rather than baked in.
- Attach and detach through tmux sessions, so agents keep working while you are away and you can rejoin interactively.

## Cautions

- It is a testbed by its own description: Google names no support commitment and no plan for production integration.
- Partial Codex and OpenCode support means the two CLIs most of this category drives are second-class here today.
- The idiosyncratic lexicon (grove, hub, runtime broker) adds learning cost that the documentation only partly pays down.
- The documentation favors running agents in permissive mode behind infrastructure isolation, a trade some reviewers will reject on principle: policy enforced at the container boundary instead of the prompt.
- 1,730 stars is a small number for a Google project, which reads as low adoption rather than low quality.

## Pricing

Free and open source under Apache-2.0, self-hosted on infrastructure you already pay for.
No paid tiers exist; the hosted modes run on your own GCP bill.

## Compared to

- [AX](../ax/index.md): Google's other orchestration entrant, Kubernetes-first and fleet-scale; choose AX for declarative cluster manifests, Scion for the laptop-to-HA team with per-agent containers.
- [OpenRig](../openrig/index.md): the local control plane with no isolation at all; choose Scion when sandboxing is the requirement, OpenRig when you want terminal sessions rather than containers.
- [Emdash](../emdash/index.md): the SSH-first desktop environment; choose Emdash for a GUI over remote machines, Scion for container isolation with a hosted path.

## Bottom line

**Recommended for teams whose first requirement is per-agent isolation and who accept testbed churn plus Google's explicit non-support.**
Not for anyone who needs a supported product with a roadmap commitment, or whose daily drivers are Codex and OpenCode today.

## Changes

- 2026-10-06 - Created.
- 2026-10-07 - Added the GoogleCloudPlatform/scion star history chart to the Status section.

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [AX](../ax/index.md) - Google's cluster-scale sibling in this category
- [OpenRig](../openrig/index.md) - the control-plane contrast: sessions without isolation
- [Emdash](../emdash/index.md) - the SSH-first desktop alternative
- [The Agentic Development Environment Landscape](../../the-agentic-development-environment-landscape/index.md) - the tracker this category extends

## References

- https://api.github.com/repos/GoogleCloudPlatform/scion - stars, forks, Apache-2.0 license, creation date, and push date as of 2026-10-06
- https://raw.githubusercontent.com/GoogleCloudPlatform/scion/main/README.md - the isolation model, Hub and Runtime Broker definitions, harness list, and the non-support disclaimer
- https://googlecloudplatform.github.io/scion/overview/ - control plane versus execution layer, the four run modes, and the Managed Agent path
- https://www.infoq.com/news/2026/04/google-agent-testbed-scion/ - the hypervisor framing, partial Codex and OpenCode support, the lexicon, and the experimental-testbed caveat
- https://hn.algolia.com/api/v1/search?query=scion%20agents&tags=story - the launch thread's 230 points and 62 comments
- https://news.ycombinator.com/item?id=47675213 - the April 2026 launch discussion
