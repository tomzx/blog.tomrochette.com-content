---
title: OpenReview
created: 2026-10-11
updated: 2026-10-11
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, code-review, ai-review, developer-tools]
readability: 3
audience_notes: >
  Engineers tempted by vendor-labs demos who want the record on a review bot that
  drew a crowd and then went silent, including its missing license.
---

OpenReview is Vercel Labs' beta, self-hosted AI code review bot: deploy it on Vercel, connect a GitHub App, and mention @openreview on a pull request to get a Claude-powered review from a Vercel Sandbox.

## What it is

**It is the vendor-labs demo pattern in miniature: four days of commits, 1,696 stars, then silence.**
The bot triggers on an @openreview mention, runs Claude inside an isolated Vercel Sandbox (a Firecracker microVM product that has since gone generally available) with full repository access, and posts line-level comments with GitHub suggestion blocks for one-click fixes.
It can fix formatting, lint errors, and simple bugs itself, then commit and push to the PR branch.
The README states it was "built as an internal project to help the Vercel team test their technologies together", warns of rough edges and breaking changes, and ships as a one-click deploy wired to Upstash KV storage.

## Status

**Dormant.**
The repo (vercel-labs/openreview) was created March 2, 2026, was pushed to last on March 6, 2026, and shows 1,696 stars and 121 forks as of 2026-10-11, with zero releases.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=vercel-labs/openreview&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=vercel-labs/openreview&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=vercel-labs/openreview&type=date&legend=top-left" />
</picture>

Its Show HN (March 17, 2026) drew 4 points and one comment, so the star count came from visibility elsewhere, and nothing on the repo has moved since March.
No shutdown notice exists; the repository simply stopped.

## Strengths

- **The feature set still reads well: on-demand reviews, sandboxed execution that can run linters, formatters, and tests, inline suggestion blocks, and direct commits for mechanical fixes.**
- It demonstrates the sandbox pattern, running review inside an isolated microVM with repo access instead of a thin API call.
- Self-hosted by construction: your Vercel account, your Anthropic keys, your GitHub App.

## Cautions

- **No license file exists: the GitHub API reports none, so the code is publicly viewable but all rights are reserved by default, and "open-source" in the tagline overstates it.**
- Dormant since March 6, 2026, with the beta warning still standing and nobody maintaining it.
- Vercel-dependent by design (Sandbox, Upstash KV, the deploy flow), so forking it means porting off Vercel's own primitives.
- Quality evidence is absent: no benchmark, no independent assessment, and a four-point launch thread.

## Pricing

Does not apply: OpenReview is free to deploy, with costs sitting in your Vercel account (Sandbox bills active CPU time) and your Anthropic usage.

## Compared to

- [roborev](../roborev/index.md): the maintained way to self-host review on your own machine; roborev is MIT, active, and agent-agnostic, OpenReview is unlicensed, dormant, and Claude-bound.
- [Graphite Diamond](../graphite-diamond/index.md): the other vendor-absorbed review story; Diamond was bought, OpenReview was abandoned.
- [Kodus](../kodus/index.md): what a maintained open-source reviewer looks like by contrast, AGPL with an active roadmap.

## Bottom line

**Recommended for nobody as a dependency, and for anyone studying what vendor-labs review bots look like when the lab moves on.**
Not for teams that need a license, updates, or support.
My disagreeable take: an unlicensed repo tagged open-source is a trap for exactly the adopters stars attract, and shipping it without a LICENSE file is the cautionary fact here, more than the dormancy.

## Changes

- 2026-10-11 - Created after the entrant scan resolved the vercel-labs/openreview candidate from the GitHub topic search; six sources fetched this run, including the no-license API check.
- 2026-10-11 - Added the star history chart.

## See also

- [roborev](../roborev/index.md) - the maintained, licensed self-hosted counterpart
- [Graphite Diamond](../graphite-diamond/index.md) - the acquisition route out of independence, versus this abandonment route
- [Kodus](../kodus/index.md) - the maintained open-source reviewer this is not
- [Code Review Feature Matrix](../code-review-feature-matrix/index.md) - where OpenReview now sits among the category's members
- [Code Review Without Reading the Code](../../../code-review-without-reading-the-code/index.md) - the corpus case for machine-scale review

## References

- https://github.com/vercel-labs/openreview - repo facts: 1,696 stars, 121 forks, created 2026-03-02, pushed 2026-03-06, no license detected (GitHub API, as of 2026-10-11)
- https://raw.githubusercontent.com/vercel-labs/openreview/HEAD/README.md - the beta warning ("internal project to help the Vercel team test their technologies together"), the mention trigger, and the sandbox feature set
- https://api.github.com/repos/vercel-labs/openreview/license - returns 404, the no-license check (fetched 2026-10-11)
- https://api.github.com/repos/vercel-labs/openreview/releases - zero releases (fetched 2026-10-11)
- https://vercel.com/docs/sandbox - the Vercel Sandbox execution model: isolated Linux microVMs, active-CPU billing (fetched 2026-10-11)
- https://hn.algolia.com/api/v1/items/47413785 - the Show HN thread, 4 points and one comment, March 17, 2026, the thin-footprint signal
