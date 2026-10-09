---
title: Cabinet
created: 2026-10-02
updated: 2026-10-08
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, memory, knowledge-base, file-based, self-hosted]
readability: 3
audience_notes: >
  Engineers and operators who want an agent team that works out of a markdown knowledge base on their own disk instead of a SaaS brain.
  Assumes you know what an agent harness is and are comfortable running a local server.
---

Cabinet is an MIT-licensed, self-hosted knowledge base where every artifact is a markdown file on disk and an onboarded team of AI agents works over that knowledge base on a schedule.

**Its bet is that an agent team is only as durable as the files underneath it: no database, no vendor lock-in, and the knowledge base doubles as the memory the agents read and write.**

## What it is

A local web workspace (bootstrapped with `npx create-cabinet`, then `npm run dev:all` on http://localhost:4000) built in public by Hila Shmuel, a former Apple engineering manager.
An onboarding wizard asks five questions and assembles a custom AI team; ready-made teams cover roles like SDR, marketing expert, and researcher doing scheduled work such as competitor watches and inbox triage.
Everything lives as markdown files and plain folders on your disk, connected sources include Google Drive, Gmail, Slack, and Notion, and dashboards render live operating views over that knowledge.
Desktop downloads exist for Mac and Windows (Linux coming soon), with hosted Cabinet Cloud tiers on a waitlist.

## Status

Popular but quiet: 2,879 stars as of 2026-10-08 (302 forks as of 2026-10-03), created 2026-04-03, with the last release v0.6.0 on 2026-08-25 and no push since August 25.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=cabinetai/cabinet&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=cabinetai/cabinet&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=cabinetai/cabinet&type=date&legend=top-left" />
</picture>

The repository has moved from the founder's personal account to the cabinetai organization (the old hilash/cabinet URL redirects).
**The star count outruns the community record: one founder-posted Show HN thread from April 2026 (16 points, 6 comments), which makes this one of the larger repos in the category whose adoption story rests on GitHub stars alone.**
Cloud Pro and Cloud Max are waitlist stage, so the product today is the self-hosted free tier.

## Strengths

- Files on disk are the whole memory model: git-versionable, greppable, portable, and readable by any other agent or tool you run.
- The onboarding wizard makes team setup a five-question exercise instead of a configuration project.
- Scheduled agent work (boards, digests, triage) turns the knowledge base into an operating surface, not just storage.
- Self-hosted is genuinely free with bring-your-own AI accounts, and the FAQ promises a data download path back off paid hosting.
- Built in public by a named maintainer with a tracked roadmap, which keeps the project's claims checkable.

## Cautions

- Development has been quiet for about six weeks as of 2026-10-08 with no release since v0.6.0, and the broad "startup OS" scope ages badly if the pace stays flat.
- No independent community footprint: one founder-posted Show HN thread at 16 points, no third-party writeups I could find, so the 2,879 stars are the entire social proof.
- Hosted tiers are waitlist only, so teams wanting managed backups today must build their own.
- Platform coverage is Mac and Windows, with Linux still "coming soon" despite a web UI that suggests otherwise.
- The agent team runs on your connected accounts (Drive, Gmail, Slack), which concentrates real access in a young codebase.

## Pricing

Self-Hosted: free, the complete product on your own machines, bring your own AI accounts.
Cabinet Cloud Pro: $20/month billed monthly, managed hosting for one always-on Cabinet, daily backups with 7-day retention (waitlist).
Cabinet Cloud Max: $49/month billed monthly, larger container, encrypted 30-day backups, point-in-time restore (waitlist).
Enterprise: custom pricing with SSO, data residency, and a 99.9% SLA.
A Cabinet AI add-on sells model access starting at $10/month if you do not bring your own accounts.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-02 | Self-Hosted, Cloud Pro, Cloud Max | Self-Hosted free, Cloud Pro $20/mo, Cloud Max $49/mo, Cabinet AI add-on from $10/mo observed (cloud tiers waitlist) | https://runcabinet.com/pricing |

## Compared to

- [File-based agent memory](../file-based-agent-memory/index.md): the plain-files pattern Cabinet productizes; use the pattern when you want zero new software, Cabinet when you want scheduled agents on top of it.
- [claude-mem](../claude-mem/index.md): claude-mem compresses Claude Code session memory for one harness; Cabinet is a whole-workspace knowledge base with its own agent team.
- [Cognee](../cognee/index.md): Cognee builds knowledge-graph memory pipelines for other applications; Cabinet keeps memory as files and pairs it with ready-made agent roles.

## Bottom line

**Recommended for solo operators and small teams who want scheduled agent work over a file-based knowledge base they fully own.**
Not for Linux-first teams, or anyone who needs an actively shipping dependency, a managed tier today, or memory that other harnesses can query directly.

## Changes

- 2026-10-02 - Created.
- 2026-10-03 - Corrected the community record: a founder-posted Show HN thread (April 2026, 16 points, 6 comments) exists, so the no-HN-discussion claim was wrong; recorded the repository's move from the hilash account to the cabinetai organization; refreshed stars to 2,879.
- 2026-10-07 - Added the cabinetai/cabinet star history chart to the Status section.

## See also

- [Memory Feature Matrix](../memory-feature-matrix/index.md) - the category comparison this note joins
- [File-based agent memory](../file-based-agent-memory/index.md) - the plain-files pattern this product builds on
- [claude-mem](../claude-mem/index.md) - the session-memory alternative for Claude Code users
- [Cognee](../cognee/index.md) - the knowledge-graph pipeline alternative
- [The Agentic Development Environment Landscape](../../the-agentic-development-environment-landscape/index.md) - the tracker this section extends

## References

- https://github.com/cabinetai/cabinet - repository, MIT license, stars, forks, release history, and the quiet-since-August push record as of 2026-10-03 (the hilash/cabinet URL redirects here)
- https://runcabinet.com/ - product positioning, the ready-made AI team roles, the scheduled-work surface, and the download platforms
- https://runcabinet.com/pricing - the four plans, the waitlist status of the cloud tiers, and the bring-your-own-AI FAQ, re-verified unchanged 2026-10-03
- https://www.npmjs.com/package/create-cabinet - the create-cabinet bootstrap package, version 0.5.0 verified through the npm registry API (the npm site itself 403s to curl)
- https://news.ycombinator.com/item?id=47649336 - the founder's Show HN thread (2026-04-05, 16 points, 6 comments), the one piece of independent-community record found on re-verification
