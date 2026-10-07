---
title: OpenClaw
created: 2026-08-27
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, assistant-runtimes, personal-assistants, open-source, self-hosting]
readability: 3
audience_notes: >
  Engineers evaluating a self-hosted personal AI assistant, or anyone who has met the -claw variant family and wants the root profiled.
  Assumes you know what a daemon and a messaging-channel integration are.
---

OpenClaw is the self-hosted personal AI assistant (Node.js, MIT, from the OpenClaw Foundation): one Gateway process on your own device connects model providers, tools, and a few dozen messaging channels, and it is the root the entire -claw variant family reacts to.

**OpenClaw won by being the first assistant you could actually own, and its 2026 saga, Google and Anthropic restricting subscriptions for running it, is the definitive evidence that owning the runtime does not mean owning the model access; the whole variant family exists to shrink what you must trust.**

## What it is

Install from npm or a curl script, run `openclaw onboard`, and a local Gateway becomes the control plane for sessions, tools, events, and channel connections, with a Control UI, CLI, and TUI on top.
Channels bring the assistant to WhatsApp, Telegram, Slack, Discord, Google Chat, Signal, iMessage, and more; companion apps add voice, Canvas, camera, and device-local actions.
It is designed for a single operator, works with hosted and local model providers, and extends through tools, skills, and plugins.
Security is pairing-based by default (unknown senders must be approved), and the README is blunt that tools run on the host unless you configure sandboxing.

## Status

The category's giant.
As of 2026-10-06: 391,475 stars and 82,292 forks since creation on 2025-11-24, pushed daily, 9,408 open issues, npm-published.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=openclaw/openclaw&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=openclaw/openclaw&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=openclaw/openclaw&type=date&legend=top-left" />
</picture>

OpenClaw 2.0 shipped 2026-08-30 (v2026.8.1), by far the largest release in the project's history, roughly half of all pull requests ever merged in one drop from 933 contributors, rebuilding the browser app as a first-class surface and shortening the first-run install, and the cadence has held since, with v2026.9.1 released 2026-09-03, v2026.9.2 on 2026-09-05, v2026.9.3 on 2026-09-08, v2026.9.4 on 2026-09-11, v2026.9.5 on 2026-09-19, and v2026.9.6 on 2026-09-23 (its crashing macOS build was rebuilt and notarized on 2026-09-24), plus patches on the older lines, v2026.6.35 released 2026-09-10, v2026.7.33 on 2026-09-18, and v2026.7.35 on 2026-09-21, and on 2026-09-29 the project shipped v2026.8.33, a gateway-only extended-stable release it describes as its LTS equivalent, OpenClaw as of the end of August 2026 plus critical security updates, reliability and performance fixes, and new model support; the cadence has continued with v2026.9.7 released 2026-09-30 (518 direct commits, 334 contributors), a second extended-stable patch, v2026.8.34, released 2026-10-02, and v2026.9.8 released 2026-10-03 (58 commits, 43 pull requests, 21 contributors) as the current latest alongside a third extended-stable patch, v2026.8.35, released 2026-10-02, the same day as the second.
The October line has opened as a prerelease: v2026.10.1-beta.1 shipped 2026-10-05 while stable remains v2026.9.8.
The v2026.9.2 notes turned Swarm on by default: concurrent sub-agent orchestration with structured results and live progress, with explicit opt-outs preserved.
On 2026-09-21 the project announced a completed Trail of Bits security audit run through OpenAI's Patch the Planet initiative: 27 private advisories plus 3 hardening pull requests, 23 confirmed vulnerabilities (0 critical, 2 high, 16 medium, 6 low), every actionable issue repaired and shipped in the v2026.8.1 and v2026.7.33 releases, with permission-carryover and check-what-you-use as the recurring finding classes.
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
- 9,408 open issues means the tracker is a weather report, not a queue.

## Pricing

Free and open source under MIT (OpenClaw Foundation).
No paid tier; you pay your model providers, and which providers will serve it is itself a moving question per the saga above.

## Compared to

- [NanoClaw](../nanoclaw/index.md): the auditable containerized rewrite; choose it when OpenClaw's size is the problem.
- [ZeroClaw](../zeroclaw/index.md): the Rust single binary; choose it when a Node process is the problem.
- [PicoClaw](../picoclaw/index.md): the Go firmware-grade build; choose it when the assistant should live on a $10 board.
- [Paperclip](../../control-planes/paperclip/index.md): not a variant but a manager; it hires OpenClaw instances as employees.

## Bottom line

**Recommended as the default if you want the ecosystem and accept the operational weight and the provider politics.**
Not for minimal-machine deployments or anyone unwilling to audit what they are giving full access to their life.
The disagreeable claim I will defend: the restrictions saga, not the code, is OpenClaw's real product lesson, and every engineer running agents on borrowed subscriptions learned it from OpenClaw's scars.

## Changes

- 2026-08-27 - Created as the root anchor of the four OpenClaw-variant notes, recording the Gateway architecture and the provider-restriction saga.
- 2026-09-02 - Recorded the 2.0 release (v2026.8.1, 933 contributors), the project's largest.
- 2026-09-06 - Added the v2026.9.2 Swarm default-on sentence and the releases reference.
- 2026-09-10 - Recorded the v2026.6.35 patch to the June line, released while no v2026.9.4 existed.
- 2026-09-18 - Recorded the v2026.7.33 patch to the July line, released 2026-09-18, extending the old-line patch pattern.
- 2026-09-20 - Recorded v2026.9.5 (released 2026-09-19), the fifth September-line release in the watch window, with refreshed adoption numbers.
- 2026-09-22 - Recorded the v2026.7.35 July-line patch (released 2026-09-21), the completed Trail of Bits audit announced 2026-09-21 (23 confirmed vulnerabilities, all repaired, shipped in v2026.8.1 and v2026.7.33), and refreshed adoption numbers.
- 2026-09-24 - Recorded v2026.9.6 (released 2026-09-23, macOS build rebuilt and notarized 2026-09-24), the sixth September-line release in the watch window, with refreshed adoption numbers.
- 2026-09-29 - Recorded v2026.8.33 (2026-09-29), the first gateway-only extended-stable release (the project's stated LTS equivalent: end-of-August state plus critical security, reliability, and new-model fixes), with refreshed adoption numbers.
- 2026-10-02 - Recorded v2026.9.7 (released 2026-09-30, 518 direct commits, 334 contributors), now the current latest, and the second extended-stable patch v2026.8.34 (released 2026-10-02), with refreshed adoption numbers.
- 2026-10-03 - Recorded v2026.9.8 (released 2026-10-03, 58 commits, 43 pull requests, 21 contributors), now the current latest, and the third extended-stable patch v2026.8.35 (released the same day), with refreshed adoption numbers.
- 2026-10-04 - Corrected the v2026.8.35 release date to 2026-10-02 per the releases API (it shipped the same day as v2026.8.34, not alongside v2026.9.8), and refreshed adoption numbers.
- 2026-10-06 - Recorded v2026.10.1-beta.1 (2026-10-05), the October line's first tag, a prerelease while stable stays v2026.9.8, with refreshed adoption numbers.
- 2026-10-07 - Added the openclaw/openclaw star history chart to the Status section.

## See also

- [NanoClaw](../nanoclaw/index.md) - the audit-first variant
- [Assistant Runtimes Feature Matrix](../assistant-runtimes-feature-matrix/index.md) - the family compared
- [Read the Commits, Not the Manual](../../../learnings-from-openclaw/index.md) - what maintaining at this scale takes
- [Paperclip](../../control-planes/paperclip/index.md) - the control plane that employs assistants like this

## References

- https://github.com/openclaw/openclaw - README: Gateway model, channels, security posture, install
- https://api.github.com/repos/openclaw/openclaw - stars, forks, issues, dates as of 2026-10-04
- https://api.github.com/repos/openclaw/openclaw/releases - v2026.9.2 release notes, Swarm enabled by default (2026-09-05), through v2026.9.5 (2026-09-19), the v2026.7.33 July-line patch (2026-09-18), v2026.7.35 (2026-09-21), v2026.9.6 (2026-09-23), and v2026.8.33 (2026-09-29), the first gateway-only extended-stable release, plus v2026.9.7 (2026-09-30), the v2026.8.34 extended-stable patch (2026-10-02), v2026.9.8 (2026-10-03, current latest), the v2026.8.35 extended-stable patch (2026-10-02), and the v2026.10.1-beta.1 prerelease (2026-10-05), the October line's first tag
- https://openclaw.ai/blog/openclaw-trail-of-bits-engagement-recap - the Trail of Bits audit recap (27 advisories, 23 confirmed vulnerabilities, all repaired)
- https://openclaw.ai/blog/openclaw-2-accidentally - the OpenClaw 2.0 announcement (933 contributors, 16,000+ pull requests)
- https://docs.openclaw.ai - official documentation
- https://news.ycombinator.com/item?id=47633396 - Anthropic subscription restriction thread (1,099 points)
- https://news.ycombinator.com/item?id=47963204 - commits-mentioning-OpenClaw refusals (1,349 points)
- https://news.ycombinator.com/item?id=47628608 - the privilege-escalation report (514 points)
