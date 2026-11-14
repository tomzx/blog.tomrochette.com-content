---
title: Hermes Agent
created: 2026-08-27
updated: 2026-11-14
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, assistant-runtimes, personal-assistants, nous-research, open-source]
readability: 3
audience_notes: >
  Engineers choosing a self-hosted personal agent runtime and weighing Nous Research's learning-loop pitch against the -claw family.
  Assumes you know what a cron scheduler and a model provider are.
---

Hermes Agent is Nous Research's MIT-licensed self-improving personal agent: a Python gateway process that lives in your chat channels, builds skills from its own experience, and runs on everything from a $5 VPS to serverless sandboxes, at about 253k stars the biggest runtime launch since OpenClaw.

**Hermes' bet is that the runtime winner is decided by the learning loop, not the channel list: an agent that curates its own memory, writes its own skills, and models you across sessions compounds while the others merely answer.**

## What it is

Install with a curl script (the installer bundles uv, Python 3.14, Node.js, ripgrep, and ffmpeg, and stages a verified Git for Windows archive when Git is absent; the official site also ships desktop installers for macOS 12+ and Windows 10/11), and one gateway process serves Telegram, Discord, Slack, WhatsApp, Signal, Email, and a CLI, with voice-memo transcription and conversation continuity across platforms.
**The learning loop is the differentiator: it creates skills autonomously after complex tasks, improves them during use, nudges itself to persist knowledge, searches its own past sessions (FTS5 with LLM summarization), and builds a user model through Honcho, compatible with the agentskills.io open standard.**
Any model goes in (Nous Portal, OpenRouter, OpenAI, custom endpoints) and switching is a `hermes model` command with no code changes.
Execution spans six built-in terminal backends (local, Docker, SSH, Modal, Daytona, Vercel Sandbox) plus plugin backends such as Singularity and Apptainer, with serverless persistence that hibernates when idle, and a built-in cron scheduler delivers reports to any platform.

## Status

Massive and fast-moving.
253,488 stars and 54,982 forks as of 2026-10-14 since creation on 2025-07-22, MIT, and as of 2026-11-14 pushed that day with 53,388 open issues, a support surface bigger than most projects' users.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=NousResearch/hermes-agent&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=NousResearch/hermes-agent&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=NousResearch/hermes-agent&type=date&legend=top-left" />
</picture>

Releases shipped as date-stamped tags through v2026.9.24 (2026-09-24), with September alone seeing five tags, and on 2026-10-08 the project cut v0.21.6, the first semver tag and the first release of a new stable release pipeline (one attempt ref, a tested Docker image, and a receipt tag at publish), rolling up about 2,100 pull requests since v0.21.5 with the curated notes deferred to v0.22.0, and v0.21.7 followed on 2026-10-12 as the line's second tag, with v0.22.0, "The Threshold Release", landing 2026-10-14 (about 6,080 merged pull requests since v0.21.0, a guided first-run setup chat on a free trial model) and v0.22.1 and v0.22.2 following the same day and on 2026-10-15, with v0.22.3 and v0.22.4 following on 2026-10-21 and v0.22.5 landing 2026-10-23 (about 81 pull requests since v0.22.4, curated notes again deferred to v0.23.0), and v0.22.6 rolling up about 776 pull requests since v0.22.5 on 2026-11-02, curated notes again deferred to v0.23.0, and v0.22.7 rolling up about 174 pull requests since v0.22.6 on 2026-11-03, curated notes again deferred to v0.23.0, and v0.23.0, "The Hearth Release", landing 2026-11-05 (about 1,950 merged pull requests since v0.22.0 from 666 contributors: the headline a gateway-served Webapp that opens the whole Desktop workspace in a browser tab, with a single gateway owning each session so the CLI, TUI, Desktop, editors, bots, and cron sit on one agent, plugins that keep themselves updated, price tags and spend limits on paid MCP tools, pluggable delegation, and the plugin catalog grown from about 600 to over 1,050 entries), the release that finally delivered the deferred curated notes by rolling up and fully documenting the v0.22.1 through v0.22.7 patches, and v0.23.1 following on 2026-11-10 (about 618 pull requests since v0.23.0: the plugin catalog's published JSON had outgrown the 2 MiB cap clients accept since the November 9 catalog site deploy, so every install silently fell back to the catalog it shipped with, now fixed), with curated notes again deferred, this time to v0.24.0.
The [52-point launch thread](https://news.ycombinator.com/item?id=48419000) landed June 2026, and a real tool ecosystem followed (a 28-point Grafana observability integration, a Fleet console for managing Dockerized Hermes agents, XMPP interop with OpenClaw, and a community gadget SDK building ESP32 voice and text devices, 302 stars as of 2026-10-07).
**The governance record is the caution: a May 2026 thread documents Nous editing a GitHub issue to remove plagiarism claims about Hermes Agent ([issue 10232](https://github.com/NousResearch/hermes-agent/issues/10232)), so origin claims around this project deserve independent reading.**

## Strengths

- The learning loop (skills that write and improve themselves) is the most complete self-improvement story in the category.
- Six built-in execution backends plus plugin backends, with serverless idle pricing, solve the always-on cost problem that keeps personal agents expensive.
- Model-agnostic to the point of indifference, with a one-command switch.
- Nous Research's model portfolio gives it a first-party provider path the -claw tools lack.

## Cautions

- Roughly 54,000 open issues is triage weather, not a queue; expect to read code when things break.
- The plagiarism-claim edit is a stewardship red flag worth weighing before making it your memory keeper.
- A self-curating memory compounds errors as efficiently as insights; the loop needs supervision, not just trust.
- Windows installs bundle a lot of machinery (uv, Node, Git Bash), which is surface area to audit.

## Pricing

The runtime is free and open source under MIT.
Paid plans now exist through Nous Portal, and as of 2026-09-22 the prices are public on the official site: Free at $0, Plus at $20/month, Super at $100/month, and Ultra at $200/month, where each paid tier bundles monthly credits with a 10 percent bonus ($22, $110, and $220 respectively), 200+ models, and hosted tool use.
Or bring your own provider keys, with serverless backends billed by the platform when idle-cheap.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-18 | Nous Portal | Paid plans introduced: Free $0, Plus $20/mo, Super $100/mo, Ultra $200/mo, each paid tier bundling monthly credits with a 10 percent bonus; the runtime stays MIT free. | [hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com) |

## Compared to

- [OpenClaw](../openclaw/index.md): the other giant, ecosystem-first; choose OpenClaw for channels and companions, Hermes for the learning loop and model freedom.
- [NanoClaw](../nanoclaw/index.md): the auditable minimalists' pick; Hermes is the opposite trade, a lot of machinery you must trust.
- [Paperclip](../../control-planes/paperclip/index.md): if Hermes is an employee, Paperclip is the company that would manage several of them.

## Bottom line

**Recommended for engineers who want their assistant to get measurably better at their job and will supervise the loop.**
Not for minimal-footprint deployments or anyone uncomfortable with an agent that edits its own memory.
The disagreeable claim I will defend: the channel-list era of this category is over and the memory-loop era decides the winner, and Hermes is a year ahead of the -claw family on exactly that axis.

## Changes

- 2026-08-27 - Created as an Assistant runtimes note after the control-planes alternatives scan.
- 2026-09-09 - Added paid tiers (Free, Plus, Super, Ultra via Nous Portal), retiring the no-paid-tier claim.
- 2026-09-12 - Paid tier prices went public on the official site, retiring the bot-wall claim.
- 2026-09-20 - Added the Price history section tracking price changes in a table, per the new owner rule.
- 2026-09-22 - Recorded the near-daily release-tag cadence (v2026.9.7 through v2026.9.21 in September), with refreshed adoption numbers and portal tiers re-checked unchanged.
- 2026-09-24 - Recorded v2026.9.24, the fifth September tag, with refreshed adoption numbers and the Portal tiers (Free, Plus $20, Super $100, Ultra $200) re-checked unchanged on the official site.
- 2026-10-07 - Added the NousResearch/hermes-agent star history chart to the Status section.
- 2026-10-07 - Added the community hermes-gadget-sdk (ESP32 voice and text devices for the agent, 302 stars) to the ecosystem record, with refreshed adoption numbers.
- 2026-10-10 - Recorded the release-scheme change: v0.21.6 (2026-10-08) is the first semver tag and the first cut of a new stable release pipeline, ending the date-stamped scheme and the early-October tag gap, with refreshed adoption numbers and the Portal tiers re-checked unchanged.
- 2026-10-11 - Recorded the official desktop installers (macOS 12+, Windows 10/11) joining the curl install path and Email joining the official channel list, with refreshed adoption numbers and the Portal tiers (Free $0, Plus $20, Super $100, Ultra $200) re-checked unchanged on the official site.
- 2026-10-13 - Recorded v0.21.7 (2026-10-12), the second tag on the new stable release line, with refreshed adoption numbers and the Portal tiers re-checked unchanged on the official site.
- 2026-10-16 - Recorded the v0.22 line: v0.22.0, "The Threshold Release" (2026-10-14, about 6,080 merged pull requests since v0.21.0), v0.22.1 (2026-10-14), and v0.22.2 (2026-10-15), with refreshed adoption numbers.
- 2026-10-21 - Rotation re-verification: every cited URL re-fetched live (repo and releases APIs, the v0.21.6 release notes, the official site, both HN threads, the plagiarism-edit issue, the gadget SDK repo), v0.22.2 (2026-10-15) confirmed still the latest release, the seven-backend list and the Portal tiers (Free $0, Plus $20, Super $100, Ultra $200) unchanged, and the issue-10232 edit record intact.
- 2026-10-23 - Recorded the v0.22 line continuing: v0.22.3 and v0.22.4 (both 2026-10-21) and v0.22.5 (2026-10-23, about 81 pull requests since v0.22.4, curated notes again deferred to v0.23.0), with refreshed adoption numbers.
- 2026-10-25 - Corrected the backend list to the README's current framing: six built-in terminal backends (local, Docker, SSH, Modal, Daytona, Vercel Sandbox), with Singularity and Apptainer now plugin backends; the README and the official site re-fetched live and the Portal tiers (Free $0, Plus $20, Super $100, Ultra $200) unchanged, with refreshed adoption numbers.
- 2026-10-31 - Rotation re-verification: every cited URL re-fetched live (repo and releases APIs, the v0.21.6 release notes, the official site, both HN threads, the plagiarism-edit issue, the gadget SDK repo), v0.22.5 (2026-10-23) confirmed still the latest release, the Portal tiers (Free $0, Plus $20, Super $100, Ultra $200) unchanged, and the installer stack corrected to the README's current framing (Python 3.14 delegated to its package manager, a verified Git for Windows archive staged when Git is absent).
- 2026-11-03 - Recorded v0.22.6 (2026-11-02, about 776 pull requests since v0.22.5, curated notes again deferred to v0.23.0; the window's gateway-served Webapp, per-skill locks against autonomous writes, and opt-in OS-keychain vault storage disclosed only in the release notes), with refreshed adoption numbers.
- 2026-11-04 - Recorded v0.22.7 (2026-11-03, about 174 pull requests since v0.22.6, curated notes again deferred to v0.23.0; the window's opt-in Group Chats lead routing, cron jobs posting into group chats, pinned Kanban boards, TeX and mermaid rendering, Telegram team-gateway account linking, an opt-in Slack thread_followup_silence, and a Daybreak switch for catalog-listed ChatGPT subscription models disclosed only in the release notes), with refreshed adoption numbers.
- 2026-11-07 - Recorded v0.23.0, "The Hearth Release" (2026-11-05, about 1,950 merged pull requests since v0.22.0 from 666 contributors: the gateway-served browser-tab Webapp, a single gateway owning each session across every surface, self-updating plugins, price tags and spend limits on paid MCP tools, pluggable delegation, and the plugin catalog grown to over 1,050 entries), which delivered the curated notes the v0.22.x patches had been deferring, with refreshed adoption numbers.
- 2026-11-11 - Recorded v0.23.1 (2026-11-10, about 618 pull requests since v0.23.0: the fix for the plugin catalog's published JSON outgrowing the 2 MiB cap clients accept since the November 9 catalog site deploy, which had left every install silently falling back to its shipped catalog), with curated notes again deferred to v0.24.0 and refreshed adoption numbers.

## See also

- [OpenClaw](../openclaw/index.md) - the ecosystem giant it chases
- [Assistant Runtimes Feature Matrix](../assistant-runtimes-feature-matrix/index.md) - the category compared
- [File-based agent memory](../../memory/file-based-agent-memory/index.md) - the memory conventions its loop automates
- [Agent Skills open standard](../../skills/agent-skills-open-standard/index.md) - the standard its self-written skills follow

## References

- https://github.com/NousResearch/hermes-agent - README: learning loop, backends, channels, install
- https://api.github.com/repos/NousResearch/hermes-agent - stars, forks, issues as of 2026-10-10
- https://api.github.com/repos/NousResearch/hermes-agent/releases - the date-stamped tags through v2026.9.24 (2026-09-24), then the semver line: v0.21.6 (2026-10-08, the first tag under the new stable release pipeline) through v0.23.1 (2026-11-10), including v0.22.0, "The Threshold Release", and v0.23.0, "The Hearth Release"
- https://api.github.com/repos/NousResearch/hermes-agent/releases/tags/v0.21.6 - the v0.21.6 release notes describing the new stable release pipeline (fetched 2026-10-10)
- https://hermes-agent.nousresearch.com - official site and docs, including the Hermes Free/Plus/Super/Ultra plan tiers
- https://news.ycombinator.com/item?id=48419000 - the 52-point launch thread
- https://github.com/NousResearch/hermes-agent/issues/10232 - the edited plagiarism-claims issue
- https://news.ycombinator.com/item?id=49318128 - the 28-point Grafana observability integration
- https://github.com/Adolanium/hermes-gadget-sdk - the community ESP32 voice-and-text gadget SDK (302 stars as of 2026-10-07)
