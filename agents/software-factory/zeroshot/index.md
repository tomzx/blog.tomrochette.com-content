---
title: Zeroshot
created: 2026-10-10
updated: 2026-11-13
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, software-factory, review-loop, multi-agent]
readability: 3
audience_notes: >
  Engineers who want coding-agent runs gated by review the implementing agent cannot perform on itself.
  Assumes you know what a worktree, a graph node, and a harness CLI are.
---

Zeroshot is an MIT-licensed CLI that runs a coding task as an explicit graph: a worker agent implements the change, two independent reviewer agents must both accept, and rejected work returns through a bounded repair loop before anything is delivered.

## What it is

The Open Engine's Zeroshot is a native Rust binary installed from npm that also drops one skill into Codex, Claude Code, GitHub Copilot CLI, and Pi, with contributor-maintained OpenCode and Hermes adapters beside the core four in local builds, then runs one of those harness CLIs as both the worker and the reviewers with your existing logins.
A GraphSpec file defines control flow and typed state, a RuntimePlan binds each node to a harness, provider, model, and named connections, and the run input is validated before execution opens a durable SQLite ledger.
The built-in software-change template routes worker output to parallel acceptance and code review, sends rejected work to a dedicated repair worker with both reviews' feedback, and re-runs both reviews until a retry cap stops the loop.
Delivery is a ladder you opt into, from keep-it-local through --push, --pr, and --ship through PR, CI, and merge, and runs execute locally, on a self-hosted Docker target, or on Zeroshot Platform's managed capacity (Zeroshot Cloud until the v10.18.0 rebrand).

## Status

Active and shipping: 1,969 stars since creation on 2025-12-25, per the GitHub API as of 2026-10-13.
Pushed 2026-11-12, with the train at v15.0.0 (2026-11-10, npm `latest` in sync at 15.0.0), per the GitHub API and the npm registry as of 2026-11-13.
**The v11.0.0 major (2026-11-02) broke interface again, splitting delivery evidence out of graph output so a successful native Git delivery no longer depends on the graph echoing a receipt (the Python SDK exposes `RunResult.delivery_receipt`), and v11.1.0 (2026-11-05) added a second built-in template, code-review, whose triage partitions a pull request into units for four per-unit reviewers beside five whole-change specialists without installing dependencies or starting the app, plus local script bindings that let a typed graph step run a plain executable exchanging validated JSON over stdin, a `workspaceCheckpoints` opt-out, and host-chosen commit identity for delivered commits.**
**The train then ran four majors in two days: v12.0.0 made machine-size identifiers target-owned with a `zeroshot target sizes` catalog command, v13.0.0 stopped sending the shell's GH_TOKEN to named targets unless you opt in (an ambient token silently replaced the target's stored GitHub connection), v14.0.0 published the forge-adapter target-reconciliation contract, v14.1.0 added trusted delivery validation for hosted runs, including independently verified no-change outcomes, and v15.0.0 gave Active Memory independent per-injection limits (16,000 approximate tokens for node guidance, 8,000 for repository hooks) and expanded postmortem authority (all between 2026-11-09 and 2026-11-10, npm in sync).**
The same release cycle rewrote the README across eleven documentation pull requests, now positioning zeroshot as a multi-agent orchestration framework for autonomous software development with the tagline "Independent, adversarial review with mechanically enforced execution."
v10.17.0 added Active Memory for local and Docker runs, and v10.18.0 (2026-10-24) rebrands Zeroshot Cloud as Zeroshot Platform across the CLI, docs, and SDKs, its notes stating the old $100 Cloud pricing is no longer stated anywhere.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=the-open-engine/zeroshot&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=the-open-engine/zeroshot&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=the-open-engine/zeroshot&type=date&legend=top-left" />
</picture>

**The independent footprint is thin: two June 2026 Hacker News threads at 2 points each, both pointing at the repository, plus a young curated list, and the maintainers removed the README's "starred by engineers at Google, Meta, Shopify" badge in the v11.1.0 cycle after this note recorded it as a self-published claim.**
v8 was a hard interface cutover that replaced a Node.js runtime with the native binary, v11.0.0 repeated it at the delivery-evidence seam, and the README now routes reproducible bugs and feature requests to GitHub Issues and runs contributions through a CONTRIBUTING.md with a Discord claim process, though contributed adapters stay outside the product-maintained core.

## Strengths

- **The acceptance rule is architectural**: reviewer nodes return comments and never edit, the implementing agent cannot approve its own output, and required checks re-run after every repair.
- The graph defines sequence, parallel steps, retry caps, and exit conditions before execution, so a run's behavior is inspectable in advance.
- RuntimePlan hands credentials to one node at a time, and reviewers do not inherit the worker's keys.
- Profiles save a graph plus its per-node model bindings for reuse, and custom topologies are a documented extension path.

## Cautions

- **Acceptance is LLM judgment, not a deterministic gate**: the README states coverage depends on the requirements, reviewers, tests, and environment you provide, a weaker guarantee than Fluent's final Tester or Ouroboros' mechanical first stage.
- Local runs edit the current git worktree with no isolation, so isolation means standing up the Docker target.
- Thin independent evaluation, and the v8 and v11.0.0 cutovers show interface stability is not a promise; v12.0.0 through v15.0.0 broke interface four more times in the two days after v11.1.0.
- Zeroshot Platform (Cloud until the v10.18.0 rebrand) has no published prices, the v10.15.0 README stopped advertising it entirely, and the v10.18.0 notes confirm the old $100 price is no longer stated anywhere.

## Pricing

The core is MIT, free, and self-hosted on your harness logins and keys.
Zeroshot Platform, the managed target (Zeroshot Cloud until the v10.18.0 rebrand), covers accounts, organization policy, and queue behavior in its docs, without published prices as of 2026-10-25.
The v10.15.0 README (2026-10-19) removed the Cloud section and its pricing pointer, and the v10.18.0 release notes state the old $100 price is no longer stated anywhere, so the managed path is currently unadvertised rather than sold.

## Compared to

- [Ouroboros](../ouroboros/index.md) hides the grading command and expected result from the worker and gates mechanically first; Zeroshot shows reviewers the code but separates who judges from who wrote.
- [Fluent](../fluent/index.md) ends in a deterministic Tester bound to the reviewed commit; Zeroshot ends in independent reviewer agents plus your configured checks.
- [Fabro](../fabro/index.md) makes you author any DOT graph with human gates; Zeroshot ships the review loop built in and treats custom topology as the extension path.

## Bottom line

**Recommended for engineers who want issue-to-PR runs where review is structurally independent from implementation, on harnesses they already pay for.**
Not for teams that require a deterministic final gate, third-party validation first, or interface stability guarantees.

## Changes

- 2026-10-10 - Created from the awesome-software-factories scan as the independent-review-loop member.
- 2026-10-16 - Recorded the train to v10.12.0 (2026-10-15, npm in sync), the new Python SDK release train, and the two features (planner-led archived exploration with three independent scouts in v10.11.0, local-folder and generic-Git-transport runs in v10.12.0).
- 2026-10-21 - Recorded the train to v10.15.0 (2026-10-19, npm in sync): Pi added as a fourth harness in v10.14.0, renewable delivery credentials kept out of agent environments in v10.13.0, and the v10.15.0 README repositioning that leads with user-configured workflows and stops advertising Zeroshot Cloud; the What-it-is harness roster and the Pricing and caution lines updated.
- 2026-10-23 - Recorded the train to v10.16.0 (2026-10-22, npm in sync): machine delegations with expiring API keys for unattended runs, human-gated delegation management, keys kept out of run inputs and subprocesses, and a remote-base preflight before local PR delivery.
- 2026-10-25 - Recorded the train to v10.18.0 (2026-10-24, npm in sync): Active Memory in v10.17.0 (lessons recalled from costly repository mistakes on local and Docker runs, enabled by default) and the Zeroshot Cloud to Zeroshot Platform rebrand in v10.18.0, whose notes state the old $100 Cloud pricing is no longer stated anywhere; the What-it-is run-target line and the Pricing and caution lines updated.
- 2026-10-25 - Corrected the star-history chart fallback markup (the img fallback carried the dark-theme parameter; it now points at the default chart).
- 2026-10-26 - Corrected the star-history chart's light source, which wrongly carried the dark-theme parameter.
- 2026-10-28 - Recorded the train to v10.19.1 (2026-10-26, npm in sync): the guided zeroshot-graph-design interview skill and the Platform endpoint move to app.zeroshot.sh in v10.19.0, and Python SDK publishing fixes plus bundled-harness updates in v10.19.1.
- 2026-10-31 - Recorded the train to v10.24.0 (2026-10-31, npm in sync): host context with Git and checkpoint hardening (v10.20.0), caller-declared model context and output limits (v10.21.0), adapter isolation with contributed OpenCode and Hermes harnesses (v10.22.0, contributors maintain them, Platform admits core only), template-graph terminal trees (v10.23.0), and Active Memory lesson reconciliation extended to hosted runs (v10.24.0); the README now links GitHub Issues and a CONTRIBUTING.md, replacing the declining-contributions claim, and the What-it-is harness roster updated.
- 2026-11-07 - Recorded the v11.0.0 major (2026-11-02, delivery evidence separated from graph output, the Python SDK's `delivery_receipt`) and v11.1.0 (2026-11-05, npm in sync): the code-review built-in template (four per-unit reviewers beside five whole-change specialists, no dependency install or app start), local script bindings on typed graph steps, a workspaceCheckpoints opt-out, and host-chosen commit identity; the README's eleven-PR rewrite repositions zeroshot as a multi-agent orchestration framework and removes the starred-by badge, and the footprint line corrected to two 2-point June threads.
- 2026-11-13 - Recorded the train passing v11.1.0 to reach v15.0.0 (2026-11-10, npm `latest` in sync): four majors in two days, v12.0.0's target-owned machine-size identifiers, v13.0.0's opt-in GH_TOKEN forwarding to named targets (closing the ambient-token override), v14.0.0's forge-adapter target-reconciliation contract, v14.1.0's trusted delivery validation with verified no-change outcomes, and v15.0.0's Active Memory per-injection limits and expanded postmortem authority; pushed date refreshed.

## See also

- [Ouroboros](../ouroboros/index.md) - the other anti-self-grading member, hidden grading versus independent reviewers
- [Fluent](../fluent/index.md) - the deterministic final gate comparison
- [Fabro](../fabro/index.md) - the graph-authoring alternative
- [Software Factory Feature Matrix](../software-factory-feature-matrix/index.md) - where the review-loop column sits among the factories

## References

- https://github.com/the-open-engine/zeroshot - repository, the built-in workflow, delivery ladder, install methods, and license
- https://zeroshot.sh/docs/ - the graph, runtime plan, and ledger model, and the three run targets
- https://cloud.zeroshot.sh/docs - Zeroshot Platform's managed target (Cloud before the v10.18.0 rebrand), the reviewers-never-edit model, and the absence of published prices
- https://registry.npmjs.org/@the-open-engine-company%2Fzeroshot - the npm package, 15.0.0 latest as of 2026-11-13
- https://api.github.com/repos/the-open-engine/zeroshot/releases - the release train, v15.0.0 newest as of 2026-11-13, the delivery-evidence split in the v11.0.0 notes, the code-review template, script bindings, checkpoint opt-out, and commit identity in the v11.1.0 notes, the target-owned machine sizes in the v12.0.0 notes, the opt-in GH_TOKEN forwarding in the v13.0.0 notes, the forge reconciliation contract in the v14.0.0 notes, trusted delivery validation in the v14.1.0 notes, and the Active Memory limits and postmortem authority in the v15.0.0 notes, the README rewrite and badge removal across the v11.1.0 documentation pull requests, the contributed-harness and adapter-isolation features in the v10.20.0 through v10.24.0 notes, the Pi harness in the v10.14.0 notes, the Cloud de-advertising in the v10.15.0 notes, and the Active Memory and Platform rebrand in the v10.17.0 and v10.18.0 notes
- https://raw.githubusercontent.com/the-open-engine/zeroshot/main/docs/project/harness-adapters.md - the harness registry: four core adapters product-maintained, contributor-maintained OpenCode and Hermes adapters, and Platform's core-only admission
- https://news.ycombinator.com/item?id=48599820 - the 2-point June 2026 thread, the thin independent footprint this note records
- https://github.com/varun1505/awesome-software-factories - the third-party curated list that surfaced this note
