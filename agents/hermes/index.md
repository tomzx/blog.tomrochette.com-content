---
title: Hermes Agent
created: 2026-08-27
updated: 2026-08-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, assistant-runtimes, personal-assistants, nous-research, open-source]
readability: 3
audience_notes: >
  Engineers choosing a self-hosted personal agent runtime and weighing Nous Research's learning-loop pitch against the -claw family.
  Assumes you know what a cron scheduler and a model provider are.
---

Hermes Agent is Nous Research's MIT-licensed self-improving personal agent: a Python gateway process that lives in your chat channels, builds skills from its own experience, and runs on everything from a $5 VPS to serverless sandboxes, at about 238k stars the biggest runtime launch since OpenClaw.
Facts below verified as of 2026-08-30.

**Hermes' bet is that the runtime winner is decided by the learning loop, not the channel list: an agent that curates its own memory, writes its own skills, and models you across sessions compounds while the others merely answer.**

## What it is

Install with a curl script (the installer bundles uv, Python 3.11, Node.js, ripgrep, ffmpeg, and an isolated Git Bash on Windows), and one gateway process serves Telegram, Discord, Slack, WhatsApp, Signal, and a CLI, with voice-memo transcription and conversation continuity across platforms.
**The learning loop is the differentiator: it creates skills autonomously after complex tasks, improves them during use, nudges itself to persist knowledge, searches its own past sessions (FTS5 with LLM summarization), and builds a user model through Honcho, compatible with the agentskills.io open standard.**
Any model goes in (Nous Portal, OpenRouter, OpenAI, custom endpoints) and switching is a `hermes model` command with no code changes.
Execution spans seven backends (local, Docker, SSH, Singularity, Modal, Daytona, Vercel Sandbox), with serverless persistence that hibernates when idle, and a built-in cron scheduler delivers reports to any platform.

## Status

Massive and fast-moving.
As of 2026-08-30: 238,457 stars and 48,547 forks since creation on 2025-07-22, pushed today, MIT, and 37,824 open issues, a support surface bigger than most projects' users.
The [52-point launch thread](https://news.ycombinator.com/item?id=48419000) landed June 2026, and a real tool ecosystem followed (a 28-point Grafana observability integration, a Fleet console for managing Dockerized Hermes agents, XMPP interop with OpenClaw).
**The governance record is the caution: a May 2026 thread documents Nous editing a GitHub issue to remove plagiarism claims about Hermes Agent ([issue 10232](https://github.com/NousResearch/hermes-agent/issues/10232)), so origin claims around this project deserve independent reading.**

## Strengths

- The learning loop (skills that write and improve themselves) is the most complete self-improvement story in the category.
- Seven execution backends with serverless idle pricing solves the always-on cost problem that keeps personal agents expensive.
- Model-agnostic to the point of indifference, with a one-command switch.
- Nous Research's model portfolio gives it a first-party provider path the -claw tools lack.

## Cautions

- 37,824 open issues is triage weather, not a queue; expect to read code when things break.
- The plagiarism-claim edit is a stewardship red flag worth weighing before making it your memory keeper.
- A self-curating memory compounds errors as efficiently as insights; the loop needs supervision, not just trust.
- Windows installs bundle a lot of machinery (uv, Node, Git Bash), which is surface area to audit.

## Pricing

Free and open source under MIT.
No paid tier; usage is your provider keys or Nous Portal, with serverless backends billed by the platform when idle-cheap.

## Compared to

- [OpenClaw](../openclaw/index.md): the other giant, ecosystem-first; choose OpenClaw for channels and companions, Hermes for the learning loop and model freedom.
- [NanoClaw](../nanoclaw/index.md): the auditable minimalists' pick; Hermes is the opposite trade, a lot of machinery you must trust.
- [Paperclip](../paperclip/index.md): if Hermes is an employee, Paperclip is the company that would manage several of them.

## Bottom line

**Recommended for engineers who want their assistant to get measurably better at their job and will supervise the loop.**
Not for minimal-footprint deployments or anyone uncomfortable with an agent that edits its own memory.
The disagreeable claim I will defend: the channel-list era of this category is over and the memory-loop era decides the winner, and Hermes is a year ahead of the -claw family on exactly that axis.

## See also

- [OpenClaw](../openclaw/index.md) - the ecosystem giant it chases
- [Assistant Runtimes Feature Matrix](../assistant-runtimes-feature-matrix/index.md) - the category compared
- [File-based agent memory](../file-based-agent-memory/index.md) - the memory conventions its loop automates
- [Agent Skills open standard](../agent-skills-open-standard/index.md) - the standard its self-written skills follow

## References

- https://github.com/NousResearch/hermes-agent - README: learning loop, backends, channels, install
- https://api.github.com/repos/NousResearch/hermes-agent - stars, forks, issues as of 2026-08-30
- https://hermes-agent.nousresearch.com - official site and docs
- https://news.ycombinator.com/item?id=48419000 - the 52-point launch thread
- https://github.com/NousResearch/hermes-agent/issues/10232 - the edited plagiarism-claims issue
- https://news.ycombinator.com/item?id=49318128 - the 28-point Grafana observability integration
