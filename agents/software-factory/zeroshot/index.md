---
title: Zeroshot
created: 2026-10-10
updated: 2026-10-23
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, software-factory, review-loop, multi-agent]
readability: 3
audience_notes: >
  Engineers who want coding-agent runs gated by review the implementing agent cannot perform on itself.
  Assumes you know what a worktree, a graph node, and a harness CLI are.
---

Zeroshot is an MIT-licensed CLI that runs a coding task as an explicit graph: a worker agent implements the change, two independent reviewer agents must both accept, and rejected work returns through a bounded repair loop before anything is delivered.

## What it is

The Open Engine's Zeroshot is a native Rust binary installed from npm that also drops one skill into Codex, Claude Code, GitHub Copilot, and Pi, then runs one of those harness CLIs as both the worker and the reviewers with your existing logins.
A GraphSpec file defines control flow and typed state, a RuntimePlan binds each node to a harness, provider, model, and named connections, and the run input is validated before execution opens a durable SQLite ledger.
The built-in software-change template routes worker output to parallel acceptance and code review, sends rejected work to a dedicated repair worker with both reviews' feedback, and re-runs both reviews until a retry cap stops the loop.
Delivery is a ladder you opt into, from keep-it-local through --push, --pr, and --ship through PR, CI, and merge, and runs execute locally, on a self-hosted Docker target, or on Zeroshot Cloud's managed capacity.

## Status

Active and shipping: 1,969 stars since creation on 2025-12-25, per the GitHub API as of 2026-10-13.
Pushed 2026-10-23, with the train at v10.16.0 (2026-10-22), npm in sync at 10.16.0, and the Python SDK release train (zeroshot-python tags) riding each release, per the GitHub API and the npm registry as of 2026-10-23.
v10.14.0 adds Pi as a fourth harness beside Claude Code, Codex, and GitHub Copilot CLI, and v10.13.0 guards merges with renewable delivery credentials that stay out of agent environments, profiles, and history.
v10.16.0 extends that credential line with human-managed machine delegations and expiring API keys for unattended runs (delegation management requires a human login, and machine keys stay out of run inputs and subprocesses), and local PR delivery now rejects a target branch absent from the selected remote before agents start.
v10.15.0's README repositions the tool around user-configured workflows, with the built-in review loop moved below them, and strips the Zeroshot Cloud section, its pricing pointer, and the Cloud docs links, with the maintainers stating plainly that they are not advertising Cloud yet.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=the-open-engine/zeroshot&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=the-open-engine/zeroshot&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=the-open-engine/zeroshot&type=date&theme=dark&legend=top-left" />
</picture>

**The independent footprint is thin: one 2-point Hacker News thread from June 2026 and a young curated list, so the README's "starred by engineers at Google, Meta, Shopify" badge is a self-published claim.**
v8 was a hard interface cutover that replaced a Node.js runtime with the native binary, and the README still warns of breaking changes and rough edges while declining issues and external contributions.

## Strengths

- **The acceptance rule is architectural**: reviewer nodes return comments and never edit, the implementing agent cannot approve its own output, and required checks re-run after every repair.
- The graph defines sequence, parallel steps, retry caps, and exit conditions before execution, so a run's behavior is inspectable in advance.
- RuntimePlan hands credentials to one node at a time, and reviewers do not inherit the worker's keys.
- Profiles save a graph plus its per-node model bindings for reuse, and custom topologies are a documented extension path.

## Cautions

- **Acceptance is LLM judgment, not a deterministic gate**: the README states coverage depends on the requirements, reviewers, tests, and environment you provide, a weaker guarantee than Fluent's final Tester or Ouroboros' mechanical first stage.
- Local runs edit the current git worktree with no isolation, so isolation means standing up the Docker target.
- Thin independent evaluation, and the v8 cutover shows interface stability is not a promise.
- Zeroshot Cloud has no published prices, and the v10.15.0 README stopped advertising Cloud entirely, so the managed path is unknown until it returns with a price.

## Pricing

The core is MIT, free, and self-hosted on your harness logins and keys.
Zeroshot Cloud is a managed target whose docs cover accounts, organization policy, and queue behavior, without published prices as of 2026-10-11.
The v10.15.0 README (2026-10-19) removed the Cloud section and its pricing pointer, so the managed path is currently unadvertised rather than sold.

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

## See also

- [Ouroboros](../ouroboros/index.md) - the other anti-self-grading member, hidden grading versus independent reviewers
- [Fluent](../fluent/index.md) - the deterministic final gate comparison
- [Fabro](../fabro/index.md) - the graph-authoring alternative
- [Software Factory Feature Matrix](../software-factory-feature-matrix/index.md) - where the review-loop column sits among the factories

## References

- https://github.com/the-open-engine/zeroshot - repository, the built-in workflow, delivery ladder, install methods, and license
- https://zeroshot.sh/docs/ - the graph, runtime plan, and ledger model, and the three run targets
- https://cloud.zeroshot.sh/docs - Zeroshot Cloud's managed target, the reviewers-never-edit model, and the absence of published prices
- https://registry.npmjs.org/@the-open-engine-company%2Fzeroshot - the npm package, 10.16.0 latest as of 2026-10-23
- https://api.github.com/repos/the-open-engine/zeroshot/releases - the release train, v10.16.0 newest as of 2026-10-23, the Pi harness in the v10.14.0 notes, and the Cloud de-advertising in the v10.15.0 notes
- https://news.ycombinator.com/item?id=48599820 - the 2-point June 2026 thread, the thin independent footprint this note records
- https://github.com/varun1505/awesome-software-factories - the third-party curated list that surfaced this note
