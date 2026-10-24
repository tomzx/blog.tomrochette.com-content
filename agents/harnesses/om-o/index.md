---
title: OmO
created: 2026-10-13
updated: 2026-10-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, harness, cli, pi-fork]
readability: 3
audience_notes: >
  Engineers evaluating very large CLI agent harnesses and their trust trade-offs.
  Assumes you know what a terminal coding agent is and what a source-available license does and does not let you do.
---

OmO is the working name of code-yeongyu/oh-my-openagent, a source-available CLI coding agent at roughly 70,000 stars that runs on senpi (its fork of the Pi harness) and bundles a memory system, CodeMode, multi-model ultracode, Anthropic subscription support, and a workflow-DAG side pane.

**It is the scale-versus-trust test case of the Pi-derivative family: twice the stars of any other member of that family, with a mascot listed as the maintainer, a sponsor in the README, and a custom license that assigns different terms to different portions of the code.**

## What it is

A terminal agent distributed through an install script (`get.omo.dev`), built on OmO 5.0's announced Pi base: the senpi fork contributes the harness core, and OmO layers a memory system, CodeMode execution, MCP support, multi-model ultracode (running several models on one task), and Anthropic subscription billing.
Workflow visualization comes through omo-herdr-dag, a companion project that renders live OmO workflow DAGs in a Herdr side pane.
The README is sponsor-supported (OpenGateway, an OpenAI-compatible gateway, is the backer) and states the project is maintained by Jobdori, an AI assistant persona.

## Status

Massively starred and fast-moving: 70,047 stars, 5,763 forks, and 1,345 open issues and pull requests as of 2026-10-15, pushed 2026-10-24 (GitHub API, as of 2026-10-24), with release v5.1.44 published 2026-10-23 (the train from v5.1.40 to v5.1.44, after v5.1.39's publish run stopped before npm, moved the engine to senpi 2026.10.21: long 1M-context conversations stop re-writing their cached prefix, Anthropic subscription context is counted once, engine hosts start faster and idle more quietly, Claude subscriptions use the native 1M context, memory sync reads each new keyring entry incrementally, and a session's first prompt no longer freezes a shared host while reading what changed in memory; earlier, v5.1.38 shipped the unpublished v5.1.36 and v5.1.37 content and raised the per-platform binary budget from 160 to 182 MiB after the Bun 1.4.3 runtime added about 9.5 MB per binary, v5.1.34 moved the oracle, momus, and plan-reviewer fallback chains to Argon ahead of the previous pro rung after a blind 16-judgment comparison, and v5.1.35 pinned omo-senpi's typecheck dependencies inside the checkout so results stop varying with the surrounding filesystem).
**The governance record is the caution: the repository moved from an organization that now 404s, the license is a custom per-portion document GitHub reports as NOASSERTION rather than any standard license, and the README names an AI assistant as the maintainer beside its sponsor, so the usual signals a 70,000-star project carries are absent or inverted.**
Independent discussion exists but is thin for the scale: two 4-point Hacker News threads (May and September 2026) and no sustained third-party coverage found.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=code-yeongyu/oh-my-openagent&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=code-yeongyu/oh-my-openagent&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=code-yeongyu/oh-my-openagent&type=date&legend=top-left" />
</picture>

## Strengths

- Capability breadth for a CLI agent: memory, CodeMode, MCP, multi-model execution, and subscription billing in one install script.
- The Pi lineage gives it a working harness core rather than a from-scratch framework, and Pi upstream ideas flow through the fork.
- Shipping velocity is genuine: a release published the day of verification and continuous pushes.
- The Herdr DAG side pane gives long-running work a visible workflow graph, which most terminal harnesses lack entirely.
- The size of the community is itself information: at this star count, breakage gets reported fast.

## Cautions

- The license is the headline risk: a custom per-portion document with no standard identifier, so redistribution and internal-use rights must be read term by term before adoption.
- Provenance is murky: the original organization 404s, the maintainer of record is an AI persona, and a sponsor's gateway product sits in the README funnel.
- The misspelled third-party reference inside the license ("oh-my-opencode") suggests the text was adapted rather than written for this project, which is the kind of detail a lawyer will care about.
- 1,272 open issues against a side-project maintenance story argues the issue tracker is a wish wall, not a backlog.
- Thin independent coverage for the star count keeps the stars-ahead-of-discussion flag this section applies to Cabinet-class records.

## Pricing

The code is free to install and the README advertises no paid plan; Anthropic subscription usage is billed by Anthropic under your own login, and the README's sponsor sells a separate gateway product.
The license file, not a pricing page, is what actually constrains use.

## Compared to

- [Pi](../pi/index.md): the upstream harness OmO forks; Pi is MIT, smaller, and explicit about its design, OmO is bigger and bundled.
- [Oh My Pi](../oh-my-pi/index.md): the other large Pi derivative at about half OmO's scale, with a cleaner licensing story; the like-for-like alternative inside the family.
- [OpenCode](../opencode/index.md): the vendor-neutral terminal harness with standard licensing; the safer default at any budget.

## Bottom line

**Recommended for tinkerers who want the most bundled terminal agent available and will read the custom license and pin the version they audit.**
Not for commercial use without legal review, for teams needing standard licensing and identifiable maintainers, or for anyone who wants upstream Pi rather than a fork.

## Changes

- 2026-10-13 - Created.
- 2026-10-13 - Corrected the star-history chart markup (the light source and fallback image dropped the dark-theme parameter to match the canonical chart block) and replaced the bare news.ycombinator.com reference with the fetched Algolia search URL grounding the two 4-point threads.
- 2026-10-17 - Recorded the train reaching v5.1.35 (October 17): v5.1.34 put Argon into the oracle, momus, and plan-reviewer fallback chains after a blind 16-judgment comparison, and v5.1.35 made the omo-senpi typecheck checkout-independent by pinning its own type packages.
- 2026-10-20 - Recorded v5.1.38 (October 19), which shipped the unpublished v5.1.36 and v5.1.37 content and raised the release-binary size budget from 160 to 182 MiB.
- 2026-10-24 - Recorded the train reaching v5.1.44 (October 23): the senpi 2026.10.21-3 engine (cached-prefix writes stopped on 1M-context conversations, Anthropic subscription context counted once, credential-slot fix), incremental memory-sync keyring reads, first-prompt memory reads no longer freezing shared hosts, and onboarding that saves only kept facts.

## See also

- [Harness Feature Matrix](../harness-feature-matrix/index.md) - the category comparison this note joins
- [Pi](../pi/index.md) - the upstream harness senpi forks
- [Oh My Pi](../oh-my-pi/index.md) - the cleaner-licensed Pi derivative at half the scale
- [OpenCode](../opencode/index.md) - the standard-licensed vendor-neutral default
- [The Agentic Development Environment Landscape](../../the-agentic-development-environment-landscape/index.md) - the tracker this section extends

## References

- https://github.com/code-yeongyu/oh-my-openagent - repository, custom license file, stars, fork count, push activity, and the OmO 5.0 Pi-base announcement as of 2026-10-13
- https://github.com/code-yeongyu/oh-my-openagent/blob/dev/README.md - the README: memory, CodeMode, Anthropic subscriptions, ultracode, sponsors, and the maintainer persona statement
- https://github.com/jc01rho/omo-herdr-dag - the companion workflow-DAG side-pane project
- https://get.omo.dev/install.sh - the install endpoint behind the curl one-liner
- https://hn.algolia.com/api/v1/search?query=oh-my-openagent&tags=story - the Algolia search returning the two 4-point threads (2026-05-04 and 2026-09-02) as the recorded thin independent footprint
