---
title: roborev
created: 2026-10-06
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, code-review, ai-review, open-source, developer-tools]
readability: 3
audience_notes: >
  Engineers running coding agents who want review inside the loop, at commit time,
  on their own model subscriptions, and who can weigh a young tool whose quality
  evidence lives mostly in its famous author's channels.
---

roborev is an MIT-licensed background code review daemon from Kenn Software that reviews every commit with the coding agents you already run, keeps findings in a ledger until they are addressed, and now also reviews GitHub and GitLab pull requests with multi-agent panels.

## What it is

**It moves the review loop from the pull request to the commit, where agent-written code is still cheap to fix.**
A post-commit git hook (installed with `roborev init`) reviews each commit in the background using auto-detected local agents, with eleven named in the docs from Codex and Claude Code through Grok Build.
Findings land in a terminal or browser UI ledger, persist until they are addressed, and flow back into active agent sessions through the agent hook.
The PR layer arrived with 0.57: a daemon CI poller reviews open GitHub pull requests through subagent review panels with a synthesis parent review, and GitLab merge requests get the same treatment.
It is a Go binary from Kenn Software LLC, the company led by Wes McKinney (the creator of pandas), free under MIT with Homebrew, script, and `go install` installs.

## Status

**Active and unusually fast-moving, with adoption concentrated around its author's reputation.**
The repo (kenn-io/roborev) was created January 5, 2026 and shows 1,745 stars, 165 forks, and 30 contributors as of 2026-10-06, pushed the same day.

[![Star History Chart](https://api.star-history.com/chart?repos=kenn-io/roborev&type=date&legend=top-left)](https://www.star-history.com/?repos=kenn-io%2Froborev&type=date&legend=top-left)

The release train ran from v0.33 (2026-02-17) to v0.71.0 (2026-10-03), 120 releases in nine months.
The project moved twice: both wesm/roborev and roborev-dev/roborev now redirect to kenn-io/roborev, and Kenn's site pairs it with the sibling tools AgentsView and msgvault.
The HN record is thin, and I state that as a finding: a 4-point, zero-comment launch thread (46515428, January 2026) and two 1-point resubmits since, so the visible validation lives in the author's blog, a Posit profile, and podcast appearances rather than in independent discussion.

## Strengths

- **Commit-time review with a persistent ledger is accountability infrastructure, not a notification stream: findings stay open until addressed, and `roborev compact` consolidates them.**
- Harness-agnostic by construction: it reviews with the agents you already pay for, so there is no vendor judge and no token markup.
- The PR panels synthesize multiple reviewer agents into one response and can include discussion from trusted collaborators as context.
- Team surfaces are present and growing: PostgreSQL sync for multi-machine history, an ACP adapter layer, GitHub App auth, and a gh-action workflow generator.

## Cautions

- **The independent quality record is thin and partly negative: a user reported it hallucinating findings (flagging changes that do not exist) too often for job use, and the changelog itself records false-positive fixes in 0.33 and later.**
- Coverage concentrates in the author's own channels (his engineering blog, Posit's flattering profile, podcast appearances), which is evidence of reach, not of review quality.
- Reviews bill to your own agents' tokens on every commit, so high-frequency committers carry a genuine cost with no included quota.
- Kenn Software's plan for monetizing a free MIT tool is undeclared: no pricing page and no funding announcement found as of 2026-10-06.

## Pricing

Does not apply: roborev is free and open source under MIT, run locally against your own agent subscriptions, with no paid tier found as of 2026-10-06.

## Compared to

- [CodeRabbit](../coderabbit/index.md): the hosted incumbent judges your code from a vendor cloud with learned rules and an exploit history; roborev keeps review local, on your agents, at commit granularity.
- [OpenCodeReview](../open-code-review/index.md): the other license-zero self-hosted path; `ocr` is a deterministic pipeline plus one agent over PRs and diffs, roborev is a resident daemon loop over commits with panels on PRs.
- [Greptile](../greptile/index.md): hosted whole-repo graph review; choose Greptile for zero-operations depth, roborev when review must sit inside the agentic loop itself.

## Bottom line

**Recommended for developers running coding agents at high commit volume who want findings captured while context is fresh, on their own models, without a vendor holding write access to their repositories.**
Not for teams that need an independently validated reviewer today, or a zero-maintenance hosted bot.
My disagreeable take: the PR is a legacy interface for agent-written code, and commit-ledger review is where the category should have gone when agents became the main authors; whether roborev wins that argument depends on whether the hallucination reports age out.

## Changes

- 2026-10-06 - Created after the entrant scan resolved the owner's 2026-09-20 star of kenn-io/roborev, which no earlier run had resolved; twelve sources fetched this run, including the critical LinkedIn hallucination report.
- 2026-10-07 - Added the kenn-io/roborev star history chart to the Status section.

## See also

- [CodeRabbit](../coderabbit/index.md) - the hosted incumbent whose vendor-cloud trade roborev refuses
- [OpenCodeReview](../open-code-review/index.md) - the other self-hosted, bring-your-own-agent reviewer
- [Greptile](../greptile/index.md) - hosted whole-repo context as the opposite answer to the same problem
- [Code Review Feature Matrix](../code-review-feature-matrix/index.md) - where roborev now sits in the category
- [Code Review Without Reading the Code](../../../code-review-without-reading-the-code/index.md) - the corpus case for machine-scale review

## References

- https://github.com/kenn-io/roborev - repo facts: 1,745 stars, 165 forks, 30 contributors, MIT, created 2026-01-05, pushed 2026-10-06 (GitHub API, as of 2026-10-06)
- https://raw.githubusercontent.com/kenn-io/roborev/HEAD/README.md - the two automation layers, the refine skill, and install paths
- https://roborev.io/docs/ - the ledger model, the agent hook, panels, PostgreSQL sync, and the ACP surface
- https://roborev.io/docs/agents.md - the eleven supported agents and the auto-detection fallback order
- https://roborev.io/docs/integrations/github.md - the CI poller, subagent panels with synthesis (0.57+), and trusted-collaborator context
- https://roborev.io/docs/changelog/ - the release train, the 0.33 false-positive work, and the gh-action generator
- https://github.com/kenn-io/roborev/releases - v0.71.0 (2026-10-03), latest of 120 releases (GitHub API, as of 2026-10-06)
- https://hn.algolia.com/api/v1/items/46515428 - the 4-point, zero-comment launch thread, the thin-footprint signal
- https://wesmckinney.com/blog/agentic-engineering-aug-2026/ - the author's workflow grounding the design, roborev as the verification layer beside Superpowers
- https://posit.co/blog/the-prolific-output-of-wes-mckinney-in-the-age-of-agentic-engineering/ - the independent profile of author and tool, and the source linking the pre-transfer roborev-dev org
- https://kenn.io/ - Kenn Software LLC, the author, and the sibling AgentsView and msgvault projects
- https://www.linkedin.com/posts/semyon-a-sinchenko_why-i-still-use-aider-in-2026-code-ownership-activity-7437170160362340352--SNB - the critical user report of hallucinated findings
