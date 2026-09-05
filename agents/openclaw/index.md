---
title: OpenClaw
created: 2026-08-27
updated: 2026-09-05
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, assistant-runtimes, personal-assistants, open-source, self-hosting]
readability: 3
audience_notes: >
  Engineers evaluating a self-hosted personal AI assistant, or anyone who has met the -claw variant family and wants the root profiled.
  Assumes you know what a daemon and a messaging-channel integration are.
---

OpenClaw is the self-hosted personal AI assistant (Node.js, MIT, from the OpenClaw Foundation): one Gateway process on your own device connects model providers, tools, and a few dozen messaging channels, and it is the root the entire -claw variant family reacts to.
Facts below verified as of 2026-09-05.

**OpenClaw won by being the first assistant you could actually own, and its 2026 saga, Google and Anthropic restricting subscriptions for running it, is the definitive evidence that owning the runtime does not mean owning the model access; the whole variant family exists to shrink what you must trust.**

## What it is

Install from npm or a curl script, run `openclaw onboard`, and a local Gateway becomes the control plane for sessions, tools, events, and channel connections, with a Control UI, CLI, and TUI on top.
Channels bring the assistant to WhatsApp, Telegram, Slack, Discord, Google Chat, Signal, iMessage, and more; companion apps add voice, Canvas, camera, and device-local actions.
It is designed for a single operator, works with hosted and local model providers, and extends through tools, skills, and plugins.
Security is pairing-based by default (unknown senders must be approved), and the README is blunt that tools run on the host unless you configure sandboxing.

## Status

The category's giant.
As of 2026-09-05: 388,904 stars and 81,701 forks since creation on 2025-11-24, pushed daily, 6,225 open issues, npm-published.
OpenClaw 2.0 shipped 2026-08-30 (v2026.8.1), by far the largest release in the project's history, roughly half of all pull requests ever merged in one drop from 933 contributors, rebuilding the browser app as a first-class surface and shortening the first-run install, and the cadence has held since with v2026.9.1 released 2026-09-03.
It was renamed twice in its first months (the 667-point "Moltbot Renamed Again" thread documents the path to the OpenClaw name).
**The 2026 provider saga is its defining record: Google restricting AI Pro/Ultra subscribers in February (802 points), Anthropic disallowing Claude Code subscriptions for it in April (1,099 points), a same-week privilege-escalation report (514 points), and Claude Code refusing commits that mention OpenClaw (1,349 points).**

## Strengths

- The Gateway architecture is the reference design every variant either copies or shrinks: one local control plane, many channels, pluggable providers.
- Channel breadth is unmatched, including Signal and iMessage paths the lighter tools still lack.
- An enormous ecosystem (skills, companion apps, clawsweeper triage robots, medical-skills libraries) that no variant approaches.
- Single-operator framing keeps the threat model explicit compared with multi-user platforms.

## Cautions

- Scale: the nanoclaw author's audit calls it nearly half a million lines, 53 config files, and 70+ dependencies, which is exactly the trust surface its variants reject.
- Tools run on the host by default; read the sandboxing guide before connecting anyone else.
- The provider saga shows subscription terms can be withdrawn from a popular open-source runtime at any time, budget for API keys, not just subscriptions.
- 6,225 open issues means the tracker is a weather report, not a queue.

## Pricing

Free and open source under MIT (OpenClaw Foundation).
No paid tier; you pay your model providers, and which providers will serve it is itself a moving question per the saga above.

## Compared to

- [NanoClaw](../nanoclaw/index.md): the auditable containerized rewrite; choose it when OpenClaw's size is the problem.
- [ZeroClaw](../zeroclaw/index.md): the Rust single binary; choose it when a Node process is the problem.
- [PicoClaw](../picoclaw/index.md): the Go firmware-grade build; choose it when the assistant should live on a $10 board.
- [Paperclip](../paperclip/index.md): not a variant but a manager; it hires OpenClaw instances as employees.

## Bottom line

**Recommended as the default if you want the ecosystem and accept the operational weight and the provider politics.**
Not for minimal-machine deployments or anyone unwilling to audit what they are giving full access to their life.
The disagreeable claim I will defend: the restrictions saga, not the code, is OpenClaw's real product lesson, and every engineer running agents on borrowed subscriptions learned it from OpenClaw's scars.

## See also

- [NanoClaw](../nanoclaw/index.md) - the audit-first variant
- [Assistant Runtimes Feature Matrix](../assistant-runtimes-feature-matrix/index.md) - the family compared
- [Read the Commits, Not the Manual](../../learnings-from-openclaw/index.md) - what maintaining at this scale takes
- [Paperclip](../paperclip/index.md) - the control plane that employs assistants like this

## References

- https://github.com/openclaw/openclaw - README: Gateway model, channels, security posture, install
- https://api.github.com/repos/openclaw/openclaw - stars, forks, issues, dates as of 2026-09-05
- https://openclaw.ai/blog/openclaw-2-accidentally - the OpenClaw 2.0 announcement (933 contributors, 16,000+ pull requests)
- https://docs.openclaw.ai - official documentation
- https://news.ycombinator.com/item?id=47633396 - Anthropic subscription restriction thread (1,099 points)
- https://news.ycombinator.com/item?id=47963204 - commits-mentioning-OpenClaw refusals (1,349 points)
- https://news.ycombinator.com/item?id=47628608 - the privilege-escalation report (514 points)
