---
title: OmO
created: 2026-10-13
updated: 2026-11-08
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

Massively starred and fast-moving: 70,047 stars, 5,763 forks, and 1,345 open issues and pull requests as of 2026-10-15, pushed 2026-11-08 (GitHub API, as of 2026-11-08), with release v5.1.64 published November 7, 2026 (desktop memory sync starting as soon as the engine boots instead of waiting for a session, concurrent same-line memory edits kept as whole lines on every device so they converge, a large memory-set push no longer peaking above 2 GiB through a journal index, and memory git no longer inheriting `core.hooksPath` or `GIT_DIR` redirects from the environment), after v5.1.63 the same day (a device listing answering unsupported devices immediately instead of waiting about ten seconds each, thread ops on another device spending fewer relay round trips, and a delegated child with no connected provider failing with one message naming every model in its chain and the Settings key that fixes it), after v5.1.62 published November 6, 2026 (OmO now verifies the device service it downloads against a pinned release key set of minted Ed25519 keys, refusing anything signed by neither key or with a malformed signature before anything is written, replacing what had been a placeholder pin), after v5.1.61 published November 5 (running senpi 2026.11.3-3: Claude Opus and Fable get their full pre-diet system prompt back, Anthropic Subscription no longer refuses a working Claude login as blocked when an older omo process still runs or the keychain is locked, a usage limit with an ISO reset time blocks that account until the reset instead of retrying every minute, and a goal waits for the first limited account to return), after v5.1.60 published November 3 (built-in reasoning defaults reverted to their pre-5.1.59 values, daily mode back to Claude Opus 5.5 at medium effort, and the `architect` task category now implementing as well as designing, its prompts naming broad debugging across code, logs, git history, issues, docs, configuration, and runtime evidence), after v5.1.59 published November 3 (a fix for new sessions' first message stalling for several seconds, refusal of agent kill/pkill/killall commands that would hit protected processes, and Windows memory sync refusing received items whose working paths git cannot stage), after v5.1.58 published November 2 (Claude subscription sign-in restored after the 5.1.57 routing change, and timed-out or cancelled browsing templates now giving their browser a graceful quit through process-group signals), after v5.1.57 published November 1 (Claude subscription sign-in routed through the Claude Code CLI, `/gpt-account unblock <id>` clearing usage-limit blocks after a provider-side reset, and refusal of Claude OAuth tokens handed to the plain `anthropic` provider), after v5.1.56 published November 1 (engine hosts started by the OmO desktop app or a self-started server no longer reading `SSL_CERT_FILE` or `SSL_CERT_DIR`, with certificates moved to the OS trust store or the app's extra-CA setting), after v5.1.55 published November 1, 2026 (the `programming` skill now ships two Bun scripts, `check-test-junk.ts` and `mutation-proof.ts`, that make its test rules mechanical, treating check-test findings as review candidates and naming the mutation-proof script as the command behind the serial apply/run/restore proof), after v5.1.54 published October 31 (5.1.52 and 5.1.53 went unpublished with their changes shipping inside v5.1.54: the `programming` skill's Go scaffolder writes LF files on every platform, so a Windows checkout with autocrlf no longer leaks CRLF into the project it generates), after v5.1.51 published 2026-10-28 (5.1.49 and 5.1.50 went unpublished with their changes shipping inside v5.1.51: session startup and task RPC attachment no longer wait for task-host liveness probes, recovery runs independently per host and stops claiming or reviving children after shutdown while preserving newer ownership claims, and DAG recovery and workpool reconciliation share one session-start reconcile gate without holding admission, so a paused DAG's revivable child is never judged orphaned and an orphaned worker's queued workpool item is redelivered rather than marked delivery_uncertain; before it, v5.1.48 published 2026-10-25 stopped OmO Native waiting on a stalled turn-end subscriber after two seconds with retryable memory recovery and named-component stall diagnostics, and cached warm memory prompts' HEAD and agreement reads by repository and revision to avoid repeated git processes; before that, v5.1.47 made a user Stop pause the workflow run it started instead of cancelling it, with DAG nodes, workpool workers, and task children holding until a Resume, fixed memory path-state recovery and commit hooks so literal Git lookups keep working under global glob and case-insensitive pathspec modes, and deduplicated project-memory nudges under concurrent file touches; before those, v5.1.45 made long-session reads incremental, 42 ms and 68 MB instead of 40 s and 1.8 GB on a 23,000-message session, by paging through OpenCode's message API instead of loading the whole session, and v5.1.46 fixed OmO Native's init-deep committed mode to finish through its own pull-request handoff instead of pointing at a skill that does not ship with OmO Native; before them, the train from v5.1.40 to v5.1.44, after v5.1.39's publish run stopped before npm, moved the engine to senpi 2026.10.21: long 1M-context conversations stop re-writing their cached prefix, Anthropic subscription context is counted once, engine hosts start faster and idle more quietly, Claude subscriptions use the native 1M context, memory sync reads each new keyring entry incrementally, and a session's first prompt no longer freezes a shared host while reading what changed in memory; earlier, v5.1.38 shipped the unpublished v5.1.36 and v5.1.37 content and raised the per-platform binary budget from 160 to 182 MiB after the Bun 1.4.3 runtime added about 9.5 MB per binary, v5.1.34 moved the oracle, momus, and plan-reviewer fallback chains to Argon ahead of the previous pro rung after a blind 16-judgment comparison, and v5.1.35 pinned omo-senpi's typecheck dependencies inside the checkout so results stop varying with the surrounding filesystem).
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
- 2026-10-25 - Recorded the train reaching v5.1.46 (October 25): v5.1.45 paging long-session reads through OpenCode's message API (42 ms and 68 MB instead of 40 s and 1.8 GB on a 23,000-message session), and v5.1.46 fixing OmO Native's init-deep committed mode to finish through its own pull-request handoff.
- 2026-10-26 - Extended the release train through v5.1.48 (October 25): Stop now pauses the workflow run it started instead of cancelling it (Resume continues it), stalled turn-end subscribers time out after two seconds, warm memory prompts cache Git HEAD and agreement reads, and literal Git lookups survive glob and case-insensitive pathspec modes.
- 2026-10-29 - Recorded the train reaching v5.1.51 (October 28), with 5.1.49 and 5.1.50 unpublished and their changes shipping inside it: session startup and task RPC attachment no longer wait for task-host liveness probes, recovery runs independently per host and stops after shutdown while preserving newer ownership claims, and DAG recovery and workpool reconciliation share one session-start gate that redelivers an orphaned worker's queued items instead of marking them delivery_uncertain; refreshed the push date to 2026-10-29.
- 2026-11-01 - Recorded the train reaching v5.1.55 (October 31 to November 1): the programming skill ships two Bun scripts (`check-test-junk.ts`, `mutation-proof.ts`) that make its test rules mechanical, and its Go scaffolder writes LF files on every platform (5.1.52 and 5.1.53 unpublished, their changes shipping in 5.1.54); refreshed the push date to 2026-11-01.
- 2026-11-04 - Recorded the train reaching v5.1.60 (November 1 to November 3): 5.1.56 stopped engine hosts reading `SSL_CERT_FILE` and `SSL_CERT_DIR`, 5.1.57 routed Claude sign-in through the Claude Code CLI and refused Claude OAuth tokens on the plain anthropic provider, 5.1.58 restored Claude subscription sign-in and gave timed-out browsing templates graceful quits, 5.1.59 fixed the first-message stall and refused kill commands hitting protected processes, and 5.1.60 reverted the reasoning defaults 5.1.59 raised and let the architect task category implement as well as design; refreshed the push date to 2026-11-04.
- 2026-11-06 - Recorded the train reaching v5.1.62 (November 5 to November 6): v5.1.61 moved to senpi 2026.11.3-3 with the full Claude Opus and Fable system prompt restored, Anthropic Subscription login-edge fixes, and reset-time-based account blocking, and v5.1.62 pinned the device service's release verification to minted Ed25519 keys, refusing unsigned or malformed releases before anything is written; refreshed the push date to 2026-11-06.
- 2026-11-08 - Recorded the train reaching v5.1.64 (both November 7): v5.1.63 answered unsupported devices in a listing immediately, cut relay round trips for cross-device thread ops, and gave delegated children with no connected provider a message naming every model in their chain, and v5.1.64 started desktop memory sync at engine boot, converged concurrent same-line memory edits as whole lines, indexed the push journal to cut multi-GiB peaks, and hardened memory git against inherited `core.hooksPath` and `GIT_DIR` redirects; refreshed the push date to 2026-11-08.

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
