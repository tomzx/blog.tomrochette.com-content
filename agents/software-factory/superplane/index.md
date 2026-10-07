---
title: SuperPlane
created: 2026-10-07
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, software-factory, orchestration, self-hosted]
readability: 3
audience_notes: >
  Engineers comparing end-to-end factories that turn backlog issues into verified pull requests.
  Assumes you know what a work item, a pipeline stage, and a human review gate are.
---

SuperPlane is an open-source software factory that turns high-confidence backlog issues into verified, review-ready pull requests by coordinating coding agents, source control, CI, review, and approvals in one visible system.

## What it is

**A self-hosted factory platform from the Semaphore CI cofounder's team, where a work order moves through automation lines instead of an agent freelancing through a task.**
SuperPlaneHQ builds it as a Go engine with a React surface: a Factory holds work orders, automation lines, and policies, a work order records one delegated task from intake to outcome, and an automation runs an agent, calls a tool, waits for an event, or requires approval.
Every step records a durable Run with inputs, outputs, retries, and cost, and the factory continuously evaluates which backlog issues agents can handle with high confidence while ambiguous work stays with the team.
The core is Apache-2.0 with integrations across source control, CI, cloud, observability, incident, and chat tools; an /ee directory ships under a separate Enterprise Edition license.

## Status

Active and the category's largest member: 7,711 stars, 650 forks, and 439 open issues, pushed 2026-10-07, per the GitHub API as of 2026-10-07.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=superplanehq/superplane&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=superplanehq/superplane&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=superplanehq/superplane&type=date&legend=top-left" />
</picture>

**The positioning pivoted and the tags lag main: the January 2026 Show HN launched it as an open source DevOps control plane (21 points), and the newest tag v0.30.0 dates to 2026-07-27 while main is pushed daily.**
The repository now carries the software-factory topic and the website and docs sell one-shot routine engineering, which is the frame this note reads it under.

## Strengths

- **The work order is a durable operational record**: event history, execution state, and artifacts survive retries, so a failed run resumes without custom glue or lost context.
- **Confidence-gated intake**: it evaluates which issues agents can handle and leaves ambiguous work with humans, the boundary most factory pitches skip.
- **Uniform guardrails**: the same workflow-level rules apply to every run rather than living in per-agent prompts.
- **It meets the team where work already lives**: source control, CI, observability, incidents, and chat are integrations, not afterthoughts.

## Cautions

- **Release tags lag main by months**: v0.30.0 on 2026-07-27 against daily main pushes as of 2026-10-07, so tag-tracking self-hosters run old code.
- **Open-core split**: the /ee directory sits under a separate Enterprise Edition license, and GitHub cannot classify the result.
- **Young platform surface**: 439 open issues and a January control-plane-to-factory pivot mean the docs story is still settling.
- **It is broader than a factory**: workflow automation across observability and incidents puts it in workflow-platform territory too, which dilutes the factory comparison.

## Pricing

The engine is open source and free to self-host; the website offers cloud and on-prem options without published prices as of 2026-10-07.
There is no public per-seat tier to track yet.

## Compared to

- [HAR](../har/index.md) isolates a fleet around a repo contract you already own; SuperPlane is a platform that owns the intake-to-PR line and the policies around it.
- [Fluent](../fluent/index.md) is a single-author binary whose loop learns from accepted work; SuperPlane is a company-backed platform whose loop is configured, not learned.
- [Ouroboros](../ouroboros/index.md) verifies locally with grading hidden from the worker; SuperPlane verifies at the workflow level and hands humans the review decision.

## Bottom line

**Recommended for teams that want backlog issues turned into review-ready pull requests under uniform guardrails, with the run history and cost of every step on record.**
Not for local-first, single-repo loops, and not for anyone who needs tagged releases rather than main.

## Changes

- 2026-10-07 - Created from the category's entrant scan as the largest member.

## See also

- [HAR](../har/index.md) - the fleet-harness alternative that keeps your repo as the contract
- [Fluent](../fluent/index.md) - the self-improving factory comparison
- [Ouroboros](../ouroboros/index.md) - the hidden-grading verification comparison
- [Software Factory Feature Matrix](../software-factory-feature-matrix/index.md) - where the platform column sits among the factories
- [Code Factories: Wow](../../../code-factories-wow/index.md) - the corpus metaphor this platform scales toward

## References

- https://github.com/superplanehq/superplane - repository, the Factory/Work order/Line/Automation/Run model, integrations, and topics
- https://superplane.com - positioning as one-shot routine engineering work
- https://docs.superplane.com/get-started/overview - the factory docs overview
- https://github.com/superplanehq/superplane/blob/main/LICENSE - Apache-2.0 core with the /ee Enterprise Edition license
- https://news.ycombinator.com/item?id=46793814 - the January 2026 Show HN as an open source DevOps control plane, 21 points
- https://api.github.com/repos/superplanehq/superplane/releases - the release tags, v0.30.0 newest as of 2026-10-07
- https://github.com/markoa - Marko Anastasov, SuperPlaneHQ and Semaphore cofounder
