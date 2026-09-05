---
title: NanoClaw
created: 2026-08-27
updated: 2026-08-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, assistant-runtimes, personal-assistants, containers, open-source]
readability: 3
audience_notes: >
  Engineers who want a chat-channel personal agent they can fully read and containerize, at the cost of the big sibling's ecosystem.
  Assumes you know what a Linux container is and run at least one model provider.
---

NanoClaw is a MIT-licensed Node.js personal agent (nanocoai) that runs each agent in its own Linux container, born as a 500-line rewrite of the OpenClaw idea that now stands at about 30.6k stars.
Facts below verified as of 2026-09-05.

**NanoClaw's product is auditability: a codebase small enough to hold in your head and a container wall between the agent and your life, a direct rebuttal of the half-million-line root it responds to.**

## What it is

One process and a handful of files; its author built it because giving "complex software I didn't understand full access to my life" was not acceptable, and the README keeps that argument on page one.
**Agents are sandboxed in Linux containers (Docker on macOS, Linux, WSL2) where bash runs inside the container, not on your host**, and channels arrive as skills (`/add-telegram`, `/add-slack`) copied into your own fork rather than compiled in: WhatsApp, Telegram, Discord, Slack, Teams, iMessage, Matrix, Google Chat, Webex, Linear, GitHub, WeChat, email.
It uses Claude Code natively through the Claude Agent SDK, with `/add-codex`, `/add-opencode`, and `/add-ollama-provider` as drop-in providers, and credentials never sit in the agent: outbound calls route through OneCLI's Agent Vault, which injects keys at request time under per-agent policies.
Each agent group gets its own container, workspace, memory, and mounts; Slack provisioning gives every agent its own app; scheduled tasks, templates, and a Claude-Code-assisted installer round it out.

## Status

Active and independently credible.
As of 2026-09-02: 30,682 stars and 12,855 forks since creation on 2026-01-31, pushed the day of verification, 1,076 open issues.
The [533-point launch thread](https://news.ycombinator.com/item?id=46850205) pitched it as "Clawdbot in 500 lines of TS with Apple container isolation", followed by a 169-point thread on the move from Apple Containers to Docker and a 112-point thread on adopting the OneCLI Agent Vault.
The family is real: microclaw (731 stars) describes itself as inspired by NanoClaw, and the prompt-security clawsec suite explicitly covers it.

## Strengths

- The security argument is structural (container isolation) instead of permission-based, the correct default for chat-driven agents.
- Small enough to fork and rework; the README tells you to have Claude Code walk you through the codebase.
- Credential vaulting via OneCLI is a better key model than most of the family.
- Real HN discussion footprint with author follow-through across the container and vault transitions.

## Cautions

- Container requirement means no native Windows and a Docker dependency the single-binary variants skip.
- The fork-and-modify philosophy means your install drifts from trunk by design; updates become your problem.
- The 12.8k forks against a small core team is a lot of divergence for one codebase to carry.
- It inherits the family's provider politics (see the OpenClaw saga) while standardizing on Anthropic's SDK.

## Pricing

Free and open source under MIT.
No paid tier; bring your own provider keys or subscriptions.

## Compared to

- [OpenClaw](../openclaw/index.md): the full ecosystem at 13x the code; choose OpenClaw for channels and companions, NanoClaw for trust.
- [ZeroClaw](../zeroclaw/index.md): the Rust single binary; same suspicion of sprawl, different runtime bet.
- [PicoClaw](../picoclaw/index.md): smaller still, but hardware-first rather than isolation-first.

## Bottom line

**Recommended for engineers whose blocker is trusting the software, not lacking features: read it in an afternoon, run it in containers, sleep at night.**
Not for maximum channel breadth or anyone allergic to maintaining a fork.
My disagreeable claim: the container wall matters more than every permission system in the category, and in five years it will be the default all of them converged to.

## See also

- [OpenClaw](../openclaw/index.md) - the root it shrinks
- [Assistant Runtimes Feature Matrix](../assistant-runtimes-feature-matrix/index.md) - the family compared
- [ZeroClaw](../zeroclaw/index.md) - the compile-time alternative
- [Paperclip](../paperclip/index.md) - hiring runtimes like this into a company

## References

- https://github.com/nanocoai/nanoclaw - README: philosophy, channels, vault, isolation model
- https://api.github.com/repos/nanocoai/nanoclaw - stars, forks, issues as of 2026-09-02
- https://docs.nanoclaw.dev - official documentation
- https://news.ycombinator.com/item?id=46850205 - the 533-point launch thread
- https://news.ycombinator.com/item?id=47113731 - the Apple-Containers-to-Docker move (169 points)
- https://github.com/prompt-security/clawsec - third-party security suite naming the variant family
