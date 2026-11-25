---
title: Cloudroom
created: 2026-11-24
updated: 2026-11-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.4, orchestration, cloud-agents, desktop-app, rust, apache-2.0]
readability: 3
audience_notes: >
  Engineers who already pay for Claude Code, Codex, or another coding-agent subscription and want
  agents to keep running with the laptop closed. Assumes you know what a coding-agent CLI, a Docker
  sandbox, and a reverse proxy are, and that you can judge a ten-week-old solo project's security page.
---

Cloudroom is David Ondrej's Apache-2.0 desktop app and Rust service that run coding-agent harnesses in one cloud sandbox per thread on the subscriptions you already pay for, and move a running session between your Mac and the cloud.

**Its bet is that the harness should keep its agent loop, tools, and login while a separate core owns the sandbox, the process queue, and the recorded history, which is what lets a live session teleport between your laptop and the cloud without losing its conversation.**

## What it is

The repository holds three parts: a desktop app built on bb (the surfaces member), the Rust core that runs agents in the cloud and saves their history, and the skills every Cloudroom agent ships with.
Each cloud thread gets its own sandbox with a copy of your repository and its own Git branch, and the app talks to that sandbox's core directly.
The README says 7 harnesses run this way over 4 native protocols; the harness adapters document Codex and Pi over their own protocols, Claude Code over stream JSON, and a shared ACP adapter for several others.
The docs list twelve harnesses that run in cloud threads (Claude Code, Codex, Pi Agent, OpenCode, fx, Hermes, Devin, Droid, OpenClaw, Antigravity, Kimi Code, and Agent Zero), with Cursor and Grok local only, so the README count lags the docs.
Teleport moves a parent thread between Local and Cloud with its conversation, queued messages, and work, for five harnesses (Claude Code, Codex, Pi Agent, OpenCode, and Antigravity); ignored files, running processes, terminal sessions, and browser sessions stay behind.
The app ships for Apple Silicon Macs (macOS 13 and later), Linux x64, and Windows 11, and updates itself.
You can host the core yourself on Ubuntu 24.04 with one install script, or let cloudroom.dev host the same core for you.
Model calls go from the harness straight to your own provider, so Cloudroom does not bill for tokens.

## Status

Active on a near-daily release train: gui-v167 and core-v0.1.124 both published 2026-11-25 (subagents nesting six levels deep), after gui-v166 and core-v0.1.123 on 2026-11-24 (side chats picking their own agent and model, and the Cloudroom Agent plugin keeping a plan-limited Claude Code or Codex thread going on open source models), gui-v165 and core-v0.1.122 also on 2026-11-24 (cloud agents reach Windows PCs), after v164 on 2026-11-23, v163 on 2026-11-22, v161 and v162 on 2026-11-21, v159 and v160 on 2026-11-19, and v158 on 2026-11-18, with the default branch pushed 2026-11-25 (GitHub API, as of 2026-11-25).
The repository was created 2026-09-17 and stands at 1,841 stars with 318 forks and 82 open issues as of 2026-11-24.
It is a solo project with help: the owner accounts for 210 of the top contributors' commits against 3 for the next (GitHub API, as of 2026-11-24).
The site says Cloudroom is built by David Ondrej and a small team who previously built DeepAPI and the open-source Immortal Agents project, and that he runs a YouTube channel about AI with over 400,000 subscribers, so the launch audience is the founder's own.
The repository was first published as `davidondrej/cloudroom-core`, the path the launch comment linked, and that path now resolves to `davidondrej/cloudroom`.
**The independent record is one 2-point Hacker News story with a single comment (the submitter's own launch video link, 2026-10-17) and one third-party review that stress-tests the founder's claims and found no outside test of them.**
The home page's own headline metric, that the typical user makes 84 percent more GitHub contributions in their four weeks with Cloudroom, is the vendor's measurement.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=davidondrej/cloudroom&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=davidondrej/cloudroom&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=davidondrej/cloudroom&type=date&legend=top-left" />
</picture>

## Strengths

- **Teleport is the feature no peer in this category has**: a thread starts on your Mac, moves to a cloud sandbox before you close the lid, and comes back, keeping its chat, model, and reasoning level.
- The harness keeps its own login and calls its provider directly, so there is no model markup and no second inference bill.
- The core is self-hostable from the same open-source images, with history stored on your own machine and no database to run.
- The security page states its limits plainly: agents run without approval prompts, Mac access lets cloud agents act as you, and Command Guard catches only a few known commands.

## Cautions

- **Cloud agents run with full admin rights inside their sandbox and without approval prompts**, and with Mac access on they can read files and run commands on your Mac as you, so the self-host guide assumes one trusted user per machine.
- Command Guard, the only pre-execution guard, is on by default, catches a few catastrophic commands, and can be turned off.
- The project is ten weeks old, solo-authored, and releases a new build almost every day (v161 merged 69 pull requests alone), so the surface you evaluate will not be the surface you run next week.
- Subagents can share their thread's sandbox and change each other's files, and Teleport keeps your Mac's copy of a file changed on both sides, discarding the cloud copy to a side folder rather than merging.
- Phone access still runs through `getbb.app`, which belongs to bb and not to Cloudroom, until the move to `cloudroom.run` is done.
- The documentation disagrees with itself (7 harnesses in the README against 12 cloud-capable in the docs), and the pricing moved from per-agent quotas to credits with a new Super tier within one month.

## Pricing

The app is free and open source under Apache-2.0, local threads are free, and model usage stays on your own Claude, Codex, or other provider plans with no markup (cloudroom.dev pricing page, as of 2026-11-24).
Hosted cloud compute is sold in Cloud Credits, where a typical hour of agent work uses about 100.
Free costs $0 and includes 3,000 Cloud Credits a month (about 30 hours of agent work) with 7 day storage.
Pro costs $50 a month for 50,000 credits (about 500 hours) with no queue, H100 and B200 GPUs on demand, agents awake 4 times longer, and 1 year storage.
Super costs $150 a month for 150,000 credits (about 1,500 hours) with 2 year storage and priority support.
Ultra costs $500 a month for 500,000 credits (about 5,000 hours) with 5 year storage and a Slack channel with the founder.
Yearly billing takes 17 percent off, is paid once for 12 months, and is not refunded for unused months.
Self-hosting the core has no fee.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-15 | Free, Pro, Ultra | per-agent quotas read by a third-party review: Free 100 cloud agents and 25 hours every 30 days, Pro $50 a month with 1,000 agents and 300-plus hours, Ultra $500 a month with 10,000 agents and 3,000-plus hours | https://wkndagency.com/blog/cloudroom-review/ |
| 2026-11-24 | Free, Pro, Super, Ultra | baseline: Cloud Credits replace the agent quotas and the Super tier is added, Free 3,000 credits a month, Pro $50 a month for 50,000, Super $150 a month for 150,000, Ultra $500 a month for 500,000 | https://www.cloudroom.dev/pricing |

## Compared to

**[Conductor](../conductor/index.md)** is the closed-source macOS app for parallel sessions with its own paid cloud; Cloudroom is open source, runs on three desktop operating systems and any harness, and gives its cloud a free tier.
**[Emdash](../emdash/index.md)** goes SSH-first to run agents next to remote code on machines you reach; Cloudroom sells and open-sources the sandbox itself and adds the live local-to-cloud handoff.
**[Paseo](../paseo/index.md)** is the self-hosted daemon driving agents from desktop, web, and mobile clients; Cloudroom's nearest open-source peer on reach, but Paseo has no hosted cloud and no teleporting session.
Choose Cloudroom for one sandbox per agent with a live handoff between laptop and cloud, Conductor for a polished Mac-only review flow, and Paseo for a relay to machines you already own.

## Bottom line

Recommended for developers who already pay for two or more coding-agent subscriptions and want agents to keep working on their own branch with the laptop closed, and who will keep Mac access off and keys scoped.
Not for teams that need approval prompts on cloud agents, several users on one self-hosted machine, or independent performance evidence before adopting.

## Changes

- 2026-11-24 - Created, landing the admission the cross-category scan routed to orchestration on 2026-11-03 on the standalone-ADE line.
- 2026-11-25 - Volatile refresh: recorded gui-v166 and core-v0.1.123 (2026-11-24, side chats picking their own agent and model) and gui-v167 and core-v0.1.124 (2026-11-25, subagents nesting six levels deep) on the two-line train, the push date refreshed to 2026-11-25.

## See also

- [Conductor](../conductor/index.md) - the closed Mac app Cloudroom's own comparison table names first, with cloud agents on a paid plan
- [Emdash](../emdash/index.md) - the cross-platform ADE that reaches remote code over SSH instead of selling sandboxes
- [Paseo](../paseo/index.md) - the self-hosted daemon with desktop, web, and mobile clients and no vendor cloud
- [OpenHarness](../openharness/index.md) - the command center linking machines you own over an encrypted relay, where Cloudroom hosts the machines
- [Agent Zero](../agent-zero/index.md) - the general-purpose agent whose `a0` bridge Cloudroom's adapters can run in a cloud thread
- [bb](../../surfaces/bb/index.md) - the agentic IDE whose code the Cloudroom desktop app is built on

## References

- https://api.github.com/repos/davidondrej/cloudroom - repository metadata: created 2026-09-17, pushed 2026-11-24, 1,841 stars, 318 forks, 82 open issues, Apache-2.0, as of 2026-11-24.
- https://raw.githubusercontent.com/davidondrej/cloudroom/main/README.md - the harness-plus-core split, the 7-harnesses-over-4-protocols count, Teleport, the three desktop platforms, self-hosting, and the security section.
- https://raw.githubusercontent.com/davidondrej/cloudroom/main/core/docs/setup.md - the self-host guide: one trusted user per fresh Ubuntu 24.04 VM, agents without approval prompts, a loopback HTTP API behind Tailscale or an HTTPS proxy.
- https://raw.githubusercontent.com/davidondrej/cloudroom/main/core/docs/harnesses.md - the harness adapters: Codex and Pi on native protocols, Claude Code over stream JSON, the shared ACP adapter, and the Agent Zero bridge.
- https://raw.githubusercontent.com/davidondrej/cloudroom/main/LICENSE - the Apache-2.0 license; the NOTICE file carries bb's MIT notice.
- https://api.github.com/repos/davidondrej/cloudroom/releases?per_page=10 - the two-line release train, gui-v167 and core-v0.1.124 (2026-11-25) back to gui-v164 and core-v0.1.121 (2026-11-23); re-fetched 2026-11-25.
- https://api.github.com/repos/davidondrej/cloudroom/contributors?per_page=10 - the solo-author split (davidondrej 210 commits against 3 for the next contributor).
- https://api.github.com/repos/davidondrej/cloudroom-core - the earlier repository path, which resolves to davidondrej/cloudroom.
- https://www.cloudroom.dev/ - the home page: the vendor-measured 84 percent contribution claim, the live agent counters, and the comparison table against Conductor, OpenHands, Warp, Codex, and Claude Code dated 2026-10-26.
- https://www.cloudroom.dev/pricing - the Free, Pro, Super, and Ultra plans with Cloud Credits and the yearly terms, as of 2026-11-24.
- https://www.cloudroom.dev/security - the limits page: agents without approval prompts, full admin inside the sandbox, Mac access, Command Guard's scope, and the domains the project owns.
- https://www.cloudroom.dev/docs/teleport - what Teleport moves (five harnesses, parent threads), what stays behind, and the both-sides-changed rule.
- https://www.cloudroom.dev/docs/harnesses - the twelve cloud-capable harnesses, the local-only Cursor and Grok, and the Teleport subset.
- https://www.cloudroom.dev/docs/faq - the credit pricing restated, self-hosting without a database, and the Cloud-only features (GPUs, Cloud loops, computer use).
- https://www.cloudroom.dev/about - the team paragraph (David Ondrej, DeepAPI, Immortal Agents, the 400,000-subscriber channel) and the vendor's first-free-cloud-agents claim.
- https://www.cloudroom.dev/changelog - the per-version notes, v165 (2026-11-24) back to v160 (2026-11-19), with the pull request counts.
- https://hn.algolia.com/api/v1/search?query=Cloudroom&hitsPerPage=30 - the single Hacker News story (2 points, 1 comment, 2026-10-17) and its comment linking the launch video and the cloudroom-core path.
- https://wkndagency.com/blog/cloudroom-review/ - the 2026-10-29 third-party review: the founder's launch claim, the 2026-10-15 pricing snapshot, the security-page reading, and the finding of no outside test.
