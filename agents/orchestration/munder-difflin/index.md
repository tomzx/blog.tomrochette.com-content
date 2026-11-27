---
title: Munder Difflin
created: 2026-11-27
updated: 2026-11-27
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.4, orchestration, multi-agent, agent-teams, desktop-app, open-source, telemetry]
readability: 3
audience_notes: >
  Engineers who already pay for two or more coding-agent CLIs and want one place to run them as a team with a lead agent, a shared memory, and a task board on their own machine.
  Assumes you know what a coding-agent CLI is, what a pseudoterminal is, and that an MIT source line and a vendor installer can be two different products.
---

Munder Difflin is an MIT-licensed Electron desktop app that runs a team of the coding-agent CLIs you already subscribe to as an office you can watch, with an orchestrator agent routing work through mailboxes, a shared memory, and a task board.

**It adds no model and no agent of its own: its bet is that the coordination layer (a lead agent, a file-based hive, and a token-free office simulation) is what a dozen separate CLI windows lack, and the open-source Classic line and the vendor's installer are now two products that differ on accounts, telemetry, and what is closed.**

## What it is

Each agent is a terminal process of its own (node-pty, drawn with xterm.js) running Claude Code, Codex, Gemini CLI, Antigravity, Grok, Kimi Code, Qwen, OpenCode, Crush, Pi, GitHub Copilot, or Cursor, plus any custom command, signed in with your own plan.
Twelve engines work side by side in one office, and API keys and local models (Ollama, LM Studio, vLLM) go in Settings.
Every agent has its own folder, memory, and mailbox, and agents talk through the hive, a local git repository of plain files where an agent writes to its outbox and only the app commits.
Michael, the orchestrator, takes your request, assigns and routes the work, and puts what needs you (spend, deletions, a change of scope) in an Ask me queue, while a circuit breaker watches every agent for loops, error storms, and runaway spend beside a token cap per agent.
The office is a deterministic simulation that uses no tokens once designed, schedules and webhooks start work on their own, Slack threads send work in, and a Sandbox Office runs agents on their own copy of a project inside a small Linux machine.
It is an Electron and TypeScript app for macOS 12+, Windows 10/11, and a modern Linux desktop, made by Chaitanya Giri, an individual developer based in India, who sells the paid editions through harnessmd.com (README fetched 2026-11-27; privacy policy effective 2026-11-11).
The site lists iOS and Android, but on a phone it offers only a link that sends the download to your computer (site, as of 2026-11-27).

## Status

Active and founder-dominated: 10,011 stars and 1,426 forks as of 2026-11-27, 230 open issues and pull requests (126 of them pull requests), created 2026-05-31, pushed 2026-11-27, and of 1,501 commits the founder carries 1,160 against 27 for the next human contributor (GitHub API and repository page, as of 2026-11-27).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=HarnessMD/munder-difflin&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=HarnessMD/munder-difflin&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=HarnessMD/munder-difflin&type=date&legend=top-left" />
</picture>

Two release lines run under one version number: the GitHub release list stops at v0.5.5 (2026-10-01), while the changelog carries 0.6.0 as unreleased with "the engine of 0.5.10" inside it, and from 0.6.0 releases ship as source code only (releases API and CHANGELOG.md, fetched 2026-11-27).
The footprint reaches outside the repository: a 312-point Hacker News thread of 2026-08-22 that the founder joined as a commenter (126 comments on the page, 131 in the Algolia tree from 89 distinct authors, as of 2026-11-27), a #5 Product of the Day badge, and third-party write-ups on dev.to (2026-09-28) and Rank Agents (2026-11-20), none of them a measured benchmark.
The Rank Agents review is a document review that states it did not install the app or run a task, and I found no independent hands-on benchmark either.

## Strengths

- Harness breadth: twelve coding CLIs mixed in one office on the plans you already pay for, with no model access sold.
- The hive is inspectable by design: plain files and a local git log you can open, back up, and diff, with the app as the only committer.
- The guard rails are first-class: an Ask me queue for spend, deletions, and scope changes, a circuit breaker, and a per-agent token cap.
- The office simulation costs no tokens and gives a spatial read on which agents are working and which are messaging each other.

## Cautions

- Two products under one name: the MIT repository is Munder Difflin Classic, released as source you build yourself, while the vendor's installers carry a Pro workspace the README says is not open source (README, fetched 2026-11-27).
- The installed app's data terms differ from the repository's telemetry document: from 0.5.2 the app needs an account, from 0.5.8 usage events and a monthly token count are required with no setting to turn them off and DO_NOT_TRACK ignored, and PostHog stores each event's IP address, while TELEMETRY.md in the repository still lists a settings switch and DO_NOT_TRACK as opt-outs (privacy policy effective 2026-11-11; TELEMETRY.md fetched 2026-11-27).
- On the free plan agents run only while the app can count their tokens, and the Rank Agents review reports a free-plan user whose Devin CLI engine could not start because its tokens could not be counted (privacy policy; Rank Agents, 2026-11-20).
- The same review relays a read-only source review (issue 873) that found the app writing Claude Code bypass-warning settings into the user's global settings file without asking, with Auto mode on by default; I did not trace that code path myself (Rank Agents, 2026-11-20).
- The launch thread's top comments split between delight and dismissal, and its one hands-on account lists settings that do not persist, broken macOS notifications, and work that bounces between agents instead of running a pipeline (Hacker News, 2026-08-22).
- The vendor's blog publishes daily (392 posts, many on unrelated topics given an agent-team angle), so its comparisons are marketing rather than coverage (munderdiffl.in/blog, as of 2026-11-27).
- The bundled pixel-art tileset is under LimeZu's license, which requires credit and sits outside the MIT grant (LICENSE-ASSETS, fetched 2026-11-27).

## Pricing

The Classic source is free under MIT, and you build it yourself.
The installed app's Free plan is $0 with Pro features free up to 200 million tokens a month and a $19 one-time top-up of 2 billion tokens (pricing page, as of 2026-11-27).
Pro is $39 a month or $350 a year at the launch price (list $49 and $490) with no token cap and one machine at a time.
Max is from $138 a month or $1,150 a year (list $148 and $1,480) for a Cloud Office at 2 vCPU, 4 GB memory, and 100 GB disk, with a bigger machine priced by the part ($2 a month per extra vCPU, $18 per extra GB of memory, $5 per extra 10 GB of disk).
Teams is $49 a seat a month or $490 a seat a year, with a Cloud Office add-on at $99 a seat a month.
Your model subscriptions and API usage bill separately.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-11-27 | Free, Pro, Max, Teams | Baseline at admission: Free $0 with Pro features up to 200 million tokens a month and a $19 one-time 2-billion-token top-up; Pro launch price $39/mo or $350/yr (list $49/$490); Max from $138/mo or $1,150/yr (list $148/$1,480) for a 2 vCPU, 4 GB, 100 GB Cloud Office; Teams $49/seat/mo or $490/seat/yr with the Cloud Office add-on at $99/seat/mo. | https://munderdiffl.in/pricing.html |

## Compared to

- [Agent Teams](../agent-teams/index.md): the AGPL boss-and-team desktop across nine CLIs with file- and hunk-level review controls; choose Agent Teams when code review inside the tool is the point, Munder Difflin when the team mixes engines and the work is broader than code.
- [Orkas](../orkas/index.md): the commander-and-specialist desktop whose nine specialists ship installed; choose Orkas for a ready roster, Munder Difflin for agents that are your own CLIs on your own plans.
- [OpenRig](../openrig/index.md): a YAML-defined team of Claude Code, Codex, and Pi sessions the daemon can snapshot and restore; choose OpenRig when the team should be declared as config, Munder Difflin when it should be hired and briefed through a UI.
- [Eigent](../../assistant-runtimes/eigent/index.md): the Cowork desktop with CAMEL-based workforces for knowledge work; the pitch overlaps, but Munder Difflin runs the coding CLIs you already pay for rather than its own workforce.

## Bottom line

**Recommended for engineers who already pay for several coding-agent CLIs and want one lead agent, one shared memory, and one task board over them, built from the MIT source.**
Not for anyone who needs an installer without an account and required usage events, a diff or pull-request review surface, or an independent benchmark.

## Changes

- 2026-11-27 - Created in the Orchestration category from a coverage sighting during the OpenComputer admission, recording the Classic-source-versus-installer split, the installed app's required usage events, and the 312-point launch thread.

## See also

- [Agent Teams](../agent-teams/index.md) - the boss-and-team desktop with the review controls it lacks
- [Orkas](../orkas/index.md) - the installed-specialist desktop on the same commander-and-worker line
- [OpenRig](../openrig/index.md) - the config-declared team over Claude Code, Codex, and Pi
- [OpenComputer](../opencomputer/index.md) - the Slack-driven cloud agent whose coverage search surfaced it
- [Eigent](../../assistant-runtimes/eigent/index.md) - the Cowork desktop whose knowledge-work pitch overlaps it
- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins

## References

- https://api.github.com/repos/HarnessMD/munder-difflin - stars, forks, open issues and pull requests, creation and push dates, and license, as of 2026-11-27
- https://github.com/HarnessMD/munder-difflin - the repository page: 1,501 commits, 126 open pull requests, MIT license, and the Classic README, as of 2026-11-27
- https://api.github.com/repos/HarnessMD/munder-difflin/contributors?per_page=6 - the founder's 1,160 commits against the next contributors' 31 (a bot), 27, 14, 13, and 11, as of 2026-11-27
- https://api.github.com/repos/HarnessMD/munder-difflin/releases?per_page=6 - the tagged releases v0.5.5 (2026-10-01) back to v0.4.7-rc.1 (2026-08-26), as of 2026-11-27
- https://raw.githubusercontent.com/HarnessMD/munder-difflin/main/README.md - the Classic README: the twelve engines, the hive, Michael, the guard rails, build from source, telemetry, and Pro not open source
- https://raw.githubusercontent.com/HarnessMD/munder-difflin/main/CHANGELOG.md - the unreleased 0.6.0 entry carrying "the engine of 0.5.10", and source-only releases from 0.6.0
- https://raw.githubusercontent.com/HarnessMD/munder-difflin/main/TELEMETRY.md - the repository's event allowlist, PostHog as the sink, and its three opt-outs
- https://raw.githubusercontent.com/HarnessMD/munder-difflin/main/LICENSE-ASSETS - the LimeZu tileset carve-out from the MIT grant
- https://munderdiffl.in - the site: the office, simulations, Sandbox Office, phone send-to-computer link, and the launch badges, as of 2026-11-27
- https://munderdiffl.in/pricing.html - the Free, Pro, Max, and Teams tiers, the token top-up, and the Cloud Office parts pricing, as of 2026-11-27
- https://munderdiffl.in/blog/ - the vendor's blog index: 392 posts with daily entries, as of 2026-11-27
- https://harnessmd.com/privacy - the privacy policy effective 2026-11-11: the account requirement from 0.5.2, required usage events and token counts from 0.5.8 with no opt-out, source builds sending nothing
- https://news.ycombinator.com/item?id=49398152 - the 312-point thread of 2026-08-22 with the founder's answers and the hands-on critique
- https://hn.algolia.com/api/v1/items/49398152 - the thread tree: 131 comments from 89 distinct authors, as of 2026-11-27
- https://dev.to/renolu/munder-difflin-runs-an-office-of-agents-on-the-coding-clis-you-already-pay-for-2jnc - the 2026-09-28 third-party walkthrough of the terminal, hive, and orchestrator design
- https://rankagents.app/blog/munder-difflin-review - the 2026-11-20 document review: the Classic-versus-installer split, the token-counting limit, and the issue 873 permission finding
