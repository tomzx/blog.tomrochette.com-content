---
title: multi
created: 2026-10-16
updated: 2026-10-22
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, code-review, multi-model, open-source, developer-tools]
readability: 3
audience_notes: >
  Developers who already pay for several coding models and want their disagreement
  used as a review signal, and who can weigh a three-month-old solo project with no
  independent quality replication.
---

multi is an MIT-licensed CLI and Claude Code/Codex plugin from a solo maintainer that runs one review through several model backends in parallel over a frozen snapshot, then merges their findings into a single report sorted by how many model families corroborated each one.

## What it is

**The bet is that the most informative output of several reviewers is where they disagree, so the report buckets findings instead of flattening them.**
Every backend in your profile reads the same snapshot of the change (not the live tree), in parallel, and the merged report marks each finding corroborated (two model families saw it), single-source (one saw it, checked against the code), disagreed (the part the README tells you to read), or dropped with a reason.
Backends are Claude sub-agents, Codex, OpenCode, Kilo Code, Gemini, GitHub Copilot, the Google Antigravity CLI (an opt-in `agy` backend since v1.19.0, no effort setting), or headless Claude Code pointed at any Anthropic-compatible endpoint (OpenRouter, z.ai, DeepSeek), composed in a TOML profile, with a depth knob (lite, normal, ultra) separate from who reviews.
It ships as a Claude Code and Codex plugin (marketplace install), reviews a diff, branch, files, a function, or a whole repository, and refuses to run at all with only one model configured, because a one-model review wearing a multi-model label is worse than none.
The only mode that edits your tree is the opt-in loop (fix, re-review, repeat until clean or three rounds); everything else is read-only over the snapshot.
It is Shell and Python from szarkans, first published July 5, 2026, with 127 commits and 26 tagged releases (v1.19.0 latest).

## Status

**Active, small, and solo: 23 stars and 2 forks as of 2026-10-16, pushed October 21, 2026.**

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=szarkans/multi&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=szarkans/multi&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=szarkans/multi&type=date&legend=top-left" />
</picture>

Independent coverage exists but is thin, and I state that as a finding: OpenAgentSkill, a third-party skill registry, published a review of it on August 28, 2026 ("disagreement as signal", conclusion: track it, it is unproven), then removed the post from its blog (the URL 404s as of 2026-10-22), while its audit page remains, flagging the shell and credential surface and now blocking auto-install pending source review, and a Hacker News search re-run on 2026-10-22 still returns zero threads.
The repo was renamed from szarkans/multi-code-review to szarkans/multi (the old URL redirects), so third-party citations under either name resolve to one project.

## Strengths

- **Disagreement becomes an interface, not noise: the corroborated/single-source/disagreed buckets answer the question single-report reviewers never pose, which findings would a second model contest.**
- The vendor ships measurements with the protocol in the open: a 13-bug corpus gated red-green (revert the fix, watch its own test fail), blind majority grading, and a published list of the ways its own numbers could mislead.
- Its measured claim is specific and falsifiable: on 12 cases, the multi-model review found 29 findings against the built-in single-model review's 14, at roughly equal Claude cost but roughly double the wall time.
- A per-backend training-use disclosure table (yes, no, or unknown per endpoint) and a no-train switch that drops every uncertain backend from the roster, a privacy knob no other reviewer in this category exposes.
- Budget profiles compose free tiers (OpenCode free models, OpenRouter free endpoints) into a working zero-cost review team.

## Cautions

- **The eval is vendor-run on the author's own bugs: the corpus stays private because it is client code, so no independent replication of the 29-versus-14 claim exists as of 2026-10-16.**
- Reviews take roughly twice as long as a single-model pass (about 19 versus 10 minutes per case in the author's own table) and produce roughly twice the findings to read, which is the cost of the signal.
- No forge integration: nothing posts to a pull request, so it is a pre-merge instrument you run, not a reviewer your repository hosts.
- The name is unsearchable ("multi" collides with everything), and third-party citations split across the old multi-code-review name and the new one.
- 23 stars and zero Hacker News threads mean the community footprint is a registry listing whose review post has since been removed, and the registry's own audit flags the plugin's shell-execution and credential surface and blocks auto-install pending source review.

## Pricing

Does not apply: multi is free under MIT and bills nothing itself; costs are your own model subscriptions and API keys (the author's table puts a normal-depth review at about $3.50 of Claude usage per case plus cents for the external backends).

## Compared to

- [roborev](../roborev/index.md): the other bring-your-own-agents reviewer; roborev is a resident daemon reviewing every commit with panel synthesis on pull requests, multi is an on-demand consensus pass over one target.
- [OpenQodex](../openqodex/index.md): the other local pre-push gate; OpenQodex pairs scanners with one isolated reviewer under a completeness contract, multi pairs several reviewers with a convergence contract and no scanners.
- [Greptile](../greptile/index.md): the hosted swarm with learned rules; multi has no memory between runs, which is the point when you want opinions that did not learn your team's habits.

## Bottom line

**Recommended for developers who already pay for two or more model families and want a second-opinion instrument for risky changes, priced in their existing subscriptions.**
Not for teams that want PR-inbox automation, learned rules, or an independently validated defect-finding rate.
My disagreeable claim: the corroborated-versus-disagreed split is the correct interface for multi-model review, and every single-report reviewer in this category is discarding the one signal their parallel models produce that a human reviewer cannot.

## Changes

- 2026-10-16 - Created after the entrant scan resolved the szarkans/multi candidate (a skills-worker flag resolved to this category on kind); nine sources fetched this run, including the zero-HN-threads search as the coverage signal.
- 2026-10-22 - Rotation re-verification: recorded v1.18.1 and v1.19.0 (OpenCode 2.0 support and the agy Google Antigravity CLI backend, taking the roster to six backend types and 26 releases), and recorded that OpenAgentSkill removed its August review post while its audit page now blocks auto-install; every cited URL re-fetched, the eval page and zero-HN footprint unchanged.

## See also

- [roborev](../roborev/index.md) - the other review-with-your-own-models tool, daemon versus on-demand
- [OpenQodex](../openqodex/index.md) - the other local pre-merge gate, scanner-plus-one-reviewer versus many reviewers
- [Greptile](../greptile/index.md) - the hosted agent-swarm rival whose reviews multi deliberately does not learn from
- [Code Review Feature Matrix](../code-review-feature-matrix/index.md) - where multi now sits among the category's members
- [Rethinking Code Review in the Age of LLMs](../../../rethinking-code-review-in-the-age-of-llms/index.md) - the corpus essay on what review means when agents write the code

## References

- https://github.com/szarkans/multi - repo facts: 23 stars, 2 forks, MIT, created 2026-07-05, 127 commits, renamed from multi-code-review (GitHub API, as of 2026-10-16, re-queried 2026-10-22: pushed 2026-10-21)
- https://raw.githubusercontent.com/szarkans/multi/main/README.md - the bucketed report, backends, profiles, depth knob, loop mode, refusal to run single-model, and the training-use table, re-fetched 2026-10-22
- https://raw.githubusercontent.com/szarkans/multi/main/evals/RESULTS.md - the eval protocol: red-green bug corpus, blind majority grading, the fix-revert exam discarded as broken, and the limitations list, re-fetched 2026-10-22 (unchanged, last update still 2026-09-24)
- https://raw.githubusercontent.com/szarkans/multi/main/config.example.toml - the backend and profile configuration surface, now documenting the sixth backend type, agy (Google Antigravity CLI), re-fetched 2026-10-22
- https://raw.githubusercontent.com/szarkans/multi/main/INSTALL.md - the non-marketplace install path for other hosts, re-fetched 2026-10-22 (unchanged)
- https://api.github.com/repos/szarkans/multi/tags - 26 tagged releases, v1.19.0 latest (GitHub API, as of 2026-10-16 with 24 tags, re-fetched 2026-10-22)
- https://www.openagentskill.com/blog/introducing-szarkans-multi-code-review - the August 28, 2026 review: disagreement as signal, track-don't-adopt conclusion, fetched 2026-10-16; the post has since been removed from the registry's blog (404, re-checked 2026-10-22)
- https://www.openagentskill.com/skills/szarkans-multi-code-review - the registry's audit page: shell and credential surface flagged, low-adoption signals stated, fetched 2026-10-16, re-fetched 2026-10-22 (now also blocking auto-install pending source review)
- https://hn.algolia.com/api/v1/search?query=szarkans%20multi&tags=story - the coverage search that returned zero threads (queried 2026-10-16, re-queried 2026-10-22, still zero)
