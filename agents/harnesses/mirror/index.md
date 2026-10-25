---
title: "Mirror"
created: 2026-10-21
updated: 2026-10-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=deepseek-v4.1-flash, cli, coding-agent, reflection, open-weights, byok]
readability: 3
audience_notes: >
  Engineers shortlisting a terminal coding agent, especially ones who want a vendor harness whose default model they can also download and serve themselves.
  Assumes you know what a git worktree, MCP, AGENTS.md, and a per-token API bill are.
---

**Mirror is Reflection's entrant into the vendor-harness pattern, and its bet is the workspace rather than the conversation: one session holds several agents, each with its own model, reasoning effort, and approval mode, in its own worktree or microVM.**
Like DeepSeek Harness, Kimi Code, Qwen Code, and ZCode, it pairs an open harness with a vendor whose default model ships as open weights, so openness alone does not distinguish it; the multi-workspace session does.

## What it is

Mirror is a terminal coding agent that reads code, edits files, and runs commands, installed with `uv tool install reflection-mirror` and started with `mirror`.
The CLI is Python (3.12 or later) and drives a native Rust agent plus ripgrep that ship inside the release wheels, on macOS 15 or later for Apple Silicon and on Linux with glibc 2.28 or later; native Windows is not supported.
It defaults to Reflection's API and `Beam-1.0-501B-A23B`, and can be pointed at OpenRouter, the OpenAI and Anthropic APIs, a ChatGPT plan sign-in, any OpenAI-compatible Chat Completions endpoint, or a local server.
One session holds several workspaces, each with its own directory, conversation, model, reasoning effort, and approval mode, and switching workspaces never pauses the agent you left.
`/worktree <name>` creates a checkout under `~/.mirror/worktrees` on a `mirror/<name>` branch, `/sandbox` creates one whose file and shell tools run in a microVM, and `/folder` opens a directory you already have; Jujutsu repositories are supported alongside Git.
The code is Apache-2.0 at `reflection-oss/mirror`, and much of the product surface is a bundled Python extension layer you can turn off, replace, or extend.

## Status

Early beta and moving: `reflection-oss/mirror` was created on 2026-10-12, stood at 196 stars and 13 forks as of 2026-10-21, and was last pushed on 2026-10-22 (GitHub API, as of 2026-10-25).
The version line is still 0.1.x: one tagged release on GitHub (`mirror-agent-v0.1.8`, 2026-10-19) and the PyPI package `reflection-mirror` at 0.1.1 since 2026-10-22 (0.1.0 shipped 2026-10-16), with Reflection's own docs stating that commands and behavior may change between releases and that the extension API is in early beta.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=reflection-oss/mirror&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=reflection-oss/mirror&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=reflection-oss/mirror&type=date&legend=top-left" />
</picture>

**The community footprint so far belongs to the model, not the harness:** Reflection's Beam launch post drew 556 points on Hacker News on 2026-10-05, while searches for the harness itself return no thread, which I read as distribution through the model release rather than developers picking up a new terminal agent on its own merits.

## Strengths

- The default model is open: Beam 1.0 ships under Apache 2.0 on Hugging Face with SGLang, vLLM, TokenSpeed, and Kubernetes recipes, so pointing Mirror at your own serving endpoint is a supported path, which the closed big-vendor harnesses cannot offer for their default models, and the same `--api` switch reaches Reflection, OpenRouter, OpenAI, Anthropic, a ChatGPT plan, or a local server without changing tools.
- Workspaces are the parallelism primitive rather than a separate product: `/worktree` and `/sandbox` create independent checkouts, each tab carries the agent's status, and a message typed mid-turn is queued instead of dropped.
- Extensions are the product: the model picker, connections, repository line, context meter, and memory are all bundled extensions, so the surface is inspectable and the agent can write its own tools once `user_extensions` is on.
- Experiments are cheap to reverse: `/rewind` edits an earlier prompt and branches the conversation, and each workspace keeps its own model, effort, and approval mode, so a controller session and an auto-approving one can coexist.
- Blast radius is considered: MCP server definitions are read only from `~/.mirror/mcp` and never from a project, unknown extensions ask before they load with disable preselected, and provider keys such as `REFLECTION_API_KEY` are kept out of the environment of commands the agent runs.

## Cautions

- It is 0.1.x software in early beta, with one tagged release and a documented promise that commands and behavior change between releases.
- Approval mode decides what you review, not what the agent can reach: the docs say plainly that approved commands, extensions, and local MCP servers run with your account's full permissions, and only `/sandbox` workspaces get a microVM, which needs Apple Silicon or access to `/dev/kvm`.
- `/rewind` rewinds the conversation only, so files the agent edited after that turn stay edited; undoing those is your version-control problem.
- There is no independent evaluation: no FrontierHarness, SWE-bench, or other third-party pass-rate and cost run exists for the harness as of 2026-10-21, and the vendor's own default provider publishes no price list.
- The platform floor is narrow: macOS 15 on Apple Silicon or Linux on glibc 2.28 or later, with no native Windows support.
- Memory is off by default, but `/memory import` pulls in what Claude Code and Codex keep on the same machine, so enabling it concentrates transcripts from several tools into one store.

## Pricing

The harness is free and open source under Apache-2.0.
Usage is metered: the default path bills through Reflection's API, which publishes no price list on reflection.ai or in the developer docs as of 2026-10-21, while OpenRouter lists Beam 1.0 at $0.30/$1.00 per million tokens with cache reads at $0.04 as of 2026-10-21.
The OpenAI, Anthropic, ChatGPT plan, and generic OpenAI-compatible paths bill through those vendors at their own rates, and a local or self-hosted endpoint costs only your hardware.
Web search and page reading need a separate Firecrawl API key, priced by Firecrawl rather than by Reflection.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-21 | OpenRouter (Beam 1.0) | Baseline: `reflection/beam-1.0-501b-a23b` at $0.30/$1.00 per million tokens, cache reads $0.04; the harness itself free under Apache-2.0, and Reflection's own API price list unpublished. | [OpenRouter model list](https://openrouter.ai/api/v1/models) |

## Compared to

- [Pi](../pi/index.md): the closest philosophical match, both betting that the harness should be extended in code rather than configured through flags; Pi has the frozen core plus TypeScript extensions and a longer track record, while Mirror has the early-beta Python extension API and a vendor model you can download.
- [OpenCode](../opencode/index.md): the provider-neutral option with the leanest measured token baseline; choose OpenCode when the model roster matters more than any one vendor's tuning, and Mirror when you want Reflection's agent paired with Reflection's open weights.
- [Codex](../codex/index.md): the other vendor-owned terminal agent, bundled into a ChatGPT plan and far better tested; Mirror is 0.1.x with metered API billing and no subscription to inherit.
- [DeepSeek Harness](../deepseek-harness/index.md): the same open-harness-over-open-weights pattern pushed to its limit, MIT and everything-a-plugin but prerelease-only; Mirror trades that plugin depth for per-workspace agents, a sandbox option, and ACP.

## Bottom line

Recommended for engineers who want a vendor-maintained harness over an open-weights model, and for anyone who wants agent parallelism in worktrees with per-workspace models and approval modes without leaving the terminal.
Not for teams that need a mature, independently benchmarked agent, native Windows, or a bundled subscription price.

## Changes

- 2026-10-21 - Created from the owner's entrant question: repository, model defaults, workspaces, extensions, instructions and skills, MCP, CLI reference, and pricing sources all fetched the same day.
- 2026-10-21 - Corrected the opening claim: DeepSeek Harness, Kimi Code, Qwen Code, and ZCode are also vendor harnesses whose makers publish open weights, so openness does not distinguish Mirror; the thesis now names the multi-workspace session and the vendor-entrant pattern instead.
- 2026-10-25 - Recorded the push moving to 2026-10-22 and the PyPI package reaching 0.1.1 (October 22, after 0.1.0 on October 16); the single GitHub tag mirror-agent-v0.1.8 stands.

## See also

- [Pi](../pi/index.md) - the other minimal core with user-supplied extensions, and the sharper comparison on extension design
- [OpenCode](../opencode/index.md) - the provider-neutral baseline Mirror's model roster is measured against
- [Model Selection for Coding Tasks](../../model-selection-for-coding-tasks/index.md) - where Beam's per-token economics and capability tier sit
- [Model Provider Feature Matrix](../../model-provider-feature-matrix/index.md) - the provider-bundle view that Reflection is not yet part of
- [OpenRouter](../../model-access/openrouter/index.md) - the price and endpoint host behind Mirror's cheapest documented token path

## References

- https://developers.reflection.ai/mirror-overview - the session model, screen layout, approval modes, and conversation handling
- https://developers.reflection.ai/mirror-workspaces - `/worktree`, `/sandbox`, `/folder`, workspace status indicators, and the Jujutsu path
- https://developers.reflection.ai/mirror-models - the provider table, reasoning effort levels, `models.json`, and local endpoints
- https://developers.reflection.ai/mirror-instructions-and-skills - the `AGENTS.md` read order, the 32 KiB instruction cap, skills, and memory
- https://developers.reflection.ai/mirror-extensions - the bundled extension list, the Python extension API, and the trust prompt
- https://developers.reflection.ai/mirror-mcp - the Notion, Datadog, Linear, and Slack connections, and the home-directory-only server definitions
- https://developers.reflection.ai/mirror-cli-reference - every slash command, shortcut, launch option, `mirror exec`, and `mirror acp`
- https://developers.reflection.ai/coding-agents-quickstart - install path, platform requirements, the Firecrawl web search key, and the Reflection provider settings
- https://github.com/reflection-oss/mirror - repository, Apache-2.0 license, and the Rust agent plus Python CLI build layout
- https://pypi.org/project/reflection-mirror/ - package version 0.1.0, published 2026-10-16, Python 3.12 or later
- https://reflection.ai/blog/beam-is-available - Beam's Apache 2.0 weights release and the Mirror CLI section of the announcement, published 2026-10-16
- https://news.ycombinator.com/item?id=49969183 - the 556-point Beam launch thread, cited as the model-side footprint while the harness itself has no thread
- https://openrouter.ai/api/v1/models - the live Beam 1.0 per-token price and cache-read rate, as of 2026-10-21
