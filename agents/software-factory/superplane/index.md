---
title: SuperPlane
created: 2026-10-07
updated: 2026-11-14
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

Active: 7,709 stars as of 2026-10-14, 707 forks and 240 open issues as of 2026-11-14, pushed 2026-11-14, per the GitHub API.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=superplanehq/superplane&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=superplanehq/superplane&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=superplanehq/superplane&type=date&legend=top-left" />
</picture>

**The positioning pivoted and the release story closed its loop: the January 2026 Show HN launched it as an open source DevOps control plane (21 points), the component train began as prereleases on 2026-10-13 and 2026-10-14 and moved past RC to stable runner tags at v0.2.1 beside fleet-manager v0.1.2 through v0.1.6, all published as container images, and v1.0.0 shipped 2026-10-27 as the first stable release, after an RC train that ran from v1.0.0-rc1 (2026-10-16) through rc9 in eleven days with a first CLI component at cli/v1.0.0-rc1 (2026-10-19).**
Its notes frame the loop this note reads it under: a task starts in Backlog, Implement runs the agent, Verify addresses pull request comments and status checks and re-runs failed checks with agent feedback, and the task reaches Done when the pull request merges.
The repository now carries the software-factory topic and the website and docs sell one-shot routine engineering, which is the frame this note reads it under.

## Strengths

- **The work order is a durable operational record**: event history, execution state, and artifacts survive retries, so a failed run resumes without custom glue or lost context.
- **Confidence-gated intake**: it evaluates which issues agents can handle and leaves ambiguous work with humans, the boundary most factory pitches skip.
- **Uniform guardrails**: the same workflow-level rules apply to every run rather than living in per-agent prompts.
- **It meets the team where work already lives**: source control, CI, observability, incidents, and chat are integrations, not afterthoughts.

## Cautions

- **v1.0.0 is still the only stable platform tag eighteen days later**: the first stable platform tag landed 2026-10-27 against daily main pushes (the newest main commit, a merge-confidence running check of 2026-11-13, is unreleased), so tag-tracking self-hosters jump three months of main at once, and the stable train's own track record is one release; the component train holds at runner v0.2.1 and fleet-manager v0.1.7.
- **Open-core split**: the /ee directory sits under a separate Enterprise Edition license, and GitHub cannot classify the result.
- **Young platform surface**: 463 open issues and a January control-plane-to-factory pivot mean the docs story is still settling.
- **It is broader than a factory**: workflow automation across observability and incidents puts it in workflow-platform territory too, which dilutes the factory comparison.

## Pricing

The engine is open source and free to self-host with community support.
The website's plans (repriced between 2026-10-10 and 2026-11-13, as fetched 2026-11-13): Pay-as-you-go at $0 per month plus usage with 10 seats and up to 5 tasks in parallel, Starter at $20 per organization per month plus usage with unlimited parallel tasks, Team at $50 per user per month plus usage with up to 50 seats and bring-your-own API keys, and Enterprise custom with enterprise integrations, access controls, and priority support.
The former Business plan at $199 per organization per month with $50 shared monthly usage and the free OSS Projects tier no longer appear on the page.
Usage bills through prepaid credits: provider rate plus 10 percent on SuperPlane-provided tokens, with no markup when you connect your own subscriptions or API keys.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-10 | Business | First published pricing: Business $199 per organization per month with $50 shared monthly usage and unlimited team members, OSS Projects free, Enterprise custom. | [superplane.com/pricing](https://superplane.com/pricing/) |
| 2026-11-13 | All plans | Business $199 per organization per month replaced by Pay-as-you-go ($0 plus usage, 10 seats, 5 parallel tasks), Starter ($20 per organization per month), and Team ($50 per user per month, up to 50 seats, BYO keys); the OSS Projects free tier no longer appears; usage bills at provider rate plus 10 percent on SuperPlane-provided tokens, no markup on your own keys. | [superplane.com/pricing](https://superplane.com/pricing/) |

## Compared to

- [HAR](../har/index.md) isolates a fleet around a repo contract you already own; SuperPlane is a platform that owns the intake-to-PR line and the policies around it.
- [Fluent](../fluent/index.md) is a single-author binary whose loop learns from accepted work; SuperPlane is a company-backed platform whose loop is configured, not learned.
- [Ouroboros](../ouroboros/index.md) verifies locally with grading hidden from the worker; SuperPlane verifies at the workflow level and hands humans the review decision.

## Bottom line

**Recommended for teams that want backlog issues turned into review-ready pull requests under uniform guardrails, with the run history and cost of every step on record.**
Not for local-first, single-repo loops, and not for anyone who needs a stable release with a track record: v1.0.0 shipped on 2026-10-27.

## Changes

- 2026-10-07 - Created from the category's entrant scan as the largest member.
- 2026-10-10 - Recorded the website's first published pricing (Business $199 per organization per month with $50 shared monthly usage, OSS Projects free, Enterprise custom, machine and model usage rates), adding the Price history section; counts refreshed.
- 2026-10-13 - Recorded the first releases since the July stable tag: a component prerelease train (runner v0.1.0-rc.1 through rc.4, fleet-manager v0.1.0-rc.4 and rc.5, published as container images) on 2026-10-13 and 2026-10-14, which softens the release-lag caution while v0.30.0 remains the newest stable tag; counts refreshed.
- 2026-10-16 - Recorded the component train advancing past prerelease: runner v0.2.0 (the first stable runner tag) and fleet-manager v0.1.2 through v0.1.4 (2026-10-15), while v0.30.0 remains the newest stable platform tag.
- 2026-10-17 - Recorded the platform's first release candidate since July, v1.0.0-rc1 (2026-10-16, container image); v0.30.0 remains the newest stable tag; pushed date refreshed.
- 2026-10-21 - Recorded the RC train advancing to v1.0.0-rc2 (2026-10-19) and v1.0.0-rc3 (2026-10-20) and the first CLI component tag, cli/v1.0.0-rc1 (2026-10-19); v0.30.0 remains the newest stable platform tag; pushed date refreshed.
- 2026-10-23 - Recorded the RC train advancing to v1.0.0-rc4 (2026-10-22) and v1.0.0-rc5 (2026-10-23) and the component tags moving to runner v0.2.1 (2026-10-23) and fleet-manager v0.1.5 (2026-10-22); v0.30.0 remains the newest stable platform tag; pushed date refreshed.
- 2026-10-25 - Recorded the RC train advancing to v1.0.0-rc6 (2026-10-23) and v1.0.0-rc7 (2026-10-24) and fleet-manager reaching v0.1.6 (2026-10-24); v0.30.0 remains the newest stable platform tag; pushed date refreshed.
- 2026-10-28 - Recorded the v1.0.0 stable release (2026-10-27, the first stable platform tag, after rc8 and rc9 the same morning closed the rc1-through-rc9 train) and its Backlog-Implement-Verify-Done framing from the release notes, ending the stable-tags-lag-main caution; pushed date refreshed.
- 2026-10-31 - Recorded fleet-manager v0.1.7 (2026-10-28, a container image and chart digest bump with no feature notes) advancing the component train; pushed date refreshed.
- 2026-11-13 - Rotation re-verification: every cited URL re-fetched (repository and releases via the API, the site, the docs overview, the LICENSE files, the pricing page, the Show HN thread, and the founder profile) and all claims confirmed except pricing; recorded the repricing (Business $199 per organization per month replaced by Pay-as-you-go $0 plus usage, Starter $20 per organization per month, and Team $50 per user per month, the OSS Projects free tier gone, usage at provider rate plus 10 percent on SuperPlane-provided tokens), with the Price history row appended; pushed and counts refreshed, no release past fleet-manager v0.1.7.
- 2026-11-14 - Volatile re-verification: pushed date and open-issue count refreshed, the newest main commit now a merge-confidence running check (2026-11-13, unreleased), and no release past fleet-manager v0.1.7; no material change.

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
- https://api.github.com/repos/superplanehq/superplane/releases - the release train: v1.0.0 (2026-10-27) the first stable platform tag, fleet-manager v0.1.7 (2026-10-28) the newest component tag, after the rc1-through-rc9 train and the v0.30.0 July tag (as of 2026-11-01)
- https://github.com/markoa - Marko Anastasov, SuperPlaneHQ and Semaphore cofounder
