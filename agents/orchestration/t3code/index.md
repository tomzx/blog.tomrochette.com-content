---
title: T3 Code
created: 2026-10-07
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, mobile-client, control-surface]
readability: 3
audience_notes: >
  Engineers supervising coding agents from phones or a second machine, and anyone comparing session multiplexers.
  Assumes you already run at least one coding CLI on your own subscription.
---

T3 Code is Ping.gg's MIT-licensed control surface for agent harnesses: one server drives Claude Code, Codex, Cursor, Grok Build, OpenCode, and Antigravity on your machine, from iOS, Android, web, and Electron desktop clients.

**T3 Code is the mobile-client family's bet-the-company entrant, the first with native apps on every surface and a 400,000-developer reach claim, built on the same bring-your-own-subscription rule Happy Coder established and priced at zero because it resells no tokens.**

## What it is

A local server plus four client surfaces (an iOS app, an Android app, the app.t3.codes web app, and an Electron desktop build) by T3 Tools Inc, Theo Browne's company, MIT licensed with a fork-first policy (25,979 stars, pushed 2026-10-07, as of 2026-10-07).
The server controls whichever harnesses are installed and authenticated on your machine, across your existing subscriptions, with no key resale and no quota caps, and it can switch models mid-thread.
Every agent thread writes to its own branch, and one button turns a finished thread into a GitHub pull request with a generated title, body, and changelog, with inline diff review and draft, stack, and amend flows.
Install is a curl script or brew cask, with nightly releases (v0.0.46-nightly line, multiple builds a day) and an explicit "very early, expect bugs" notice that also says contributions are mostly not accepted yet.

## Status

Active and shipping daily: created 2026-02-08, 25,979 stars in eight months, nightly releases, as of 2026-10-07.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=pingdotgg/t3code&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=pingdotgg/t3code&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=pingdotgg/t3code&type=date&legend=top-left" />
</picture>

The site claims more than 400,000 developers tolerated it, a marketing number with no published denominator.
Its Hacker News footprint is small (three submissions in March 2026, the largest at 6 points), so adoption evidence is the star curve and the vendor's own counter, not independent measurement.

## Strengths

- The widest harness coverage in the mobile-client family: six harnesses today, with new ones described as shipping weekly.
- Native clients on all four surfaces, where the family's incumbents are web-app-in-a-shell or Telegram bots.
- The thread-to-branch-to-PR flow makes the phone a review surface, not just a prompt screen.
- MIT and fork-forward: the README's stated exit is that you keep everything needed to build your own editor if they go astray.

## Cautions

- Self-described as very early with nightly-only releases and a closed-to-contributors main repo, so the bus factor is one company.
- The 400,000-developer claim is unaudited marketing.
- Nothing in the model is exclusive: every harness here ships or partners toward its own remote surface, so the moat is UX and harness breadth, both copyable.
- Remote access to a machine that runs authenticated agents is a high-value target; the security policy exists but the surface is young.

## Pricing

Free and open source under MIT; the clients, server, and updates cost nothing because T3 Code resells no tokens, so pricing does not apply.
Your only spend is the harness subscriptions you already pay for.

## Compared to

- [Happy Coder](../happy-coder/index.md): the family's incumbent mobile client, encrypted and Claude Code plus Codex focused; choose T3 Code for six-harness breadth and native apps, Happy Coder for its longer mobile track record.
- [Omnara](../omnara/index.md): the YC control plane that supervises agents from dashboard, phone, CLI, API, and Slack with YAML-defined agents; T3 Code is the consumer-polished client for harnesses you already run.
- [Conductor](../conductor/index.md): the macOS-only parallel-session workspace; T3 Code is what you reach for when the session has to be supervised away from the desk.

## Bottom line

**Recommended for engineers who supervise agent sessions from a phone or a second machine and want one client across every harness they pay for, accepting nightly-grade software from a single company.**
Not for teams needing audited remote access today, and not for anyone who wants to contribute patches, because the project is not taking them yet.

## Changes

- 2026-10-07 - Created.

## See also

- [Happy Coder](../happy-coder/index.md) - the mobile-client family member T3 Code's launch chased
- [Omnara](../omnara/index.md) - the control-plane sibling with the same supervise-from-anywhere goal
- [Conductor](../conductor/index.md) - the desktop-bound parallel-session incumbent
- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/pingdotgg/t3code - repository, MIT license, harness list, install paths, and the early-stage and no-contributions notices (fetched 200, 2026-10-07)
- https://api.github.com/repos/pingdotgg/t3code - stars, created date, and push date for the as-of status (fetched 200, 2026-10-07)
- https://t3.codes - the four client surfaces, the bring-your-own-subscription rule, the thread-to-PR flow, and the 400,000-developer claim (fetched 200, 2026-10-07)
- https://api.github.com/repos/pingdotgg/t3code/releases - the nightly v0.0.46 release line and cadence (fetched 200, 2026-10-07)
- https://hn.algolia.com/api/v1/items/47283489 - the largest T3 Code thread, 6 points, March 2026, grounding the small-HN-footprint observation (fetched 200, 2026-10-07)
