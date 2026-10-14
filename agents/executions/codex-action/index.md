---
title: Codex Action
created: 2026-10-11
updated: 2026-10-11
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, executions, github-actions, codex, security]
readability: 3
audience_notes: >
  Engineers wiring OpenAI's Codex into GitHub Actions workflows who care about what the agent can reach.
  Assumes you know Actions jobs, permission scopes, and what a filesystem sandbox does.
---

Codex Action is OpenAI's official GitHub Action that installs the Codex CLI and runs it inside an Actions workflow behind a local proxy that holds the provider key, so the agent never sees your credentials.

**It is the best-engineered guardrail stack of the three official vendor Actions and the worst product, because there is no mention dispatch and no workflow suite: every trigger is YAML you write, in exchange for privilege reduction the other two make you assemble yourself.**

## What it is

A workflow step (`openai/codex-action@v1`) that installs the Codex CLI, starts a proxy to the Responses API that keeps `OPENAI_API_KEY` out of the agent's process, and runs `codex exec` with your prompt.
Safety strategies control runner privileges: `drop-sudo` (the default) removes sudo and Docker-socket access and starts Codex under `no_new_privs` with empty capability sets, `unprivileged-user` runs a dedicated account, `read-only` sandboxes filesystem and network, and `unsafe` (the only Windows option) removes all reduction.
Codex permission profiles (`:workspace`, `:read-only`, or named profiles, beta, CLI 0.138.0 and later) scope filesystem and network access per workflow.
Write-access checks gate who can trigger a run, with explicit `allow-users` and `allow-bots` lists, and the final Codex message surfaces as a step output you route wherever you want.
It is Apache-2.0, built by OpenAI, and tag-versioned (v1.13 the newest) rather than release-published.

## Status

**Active and current, with a small footprint.**
1,266 stars, 180 forks, and 82 open issues and pull requests as of 2026-10-13 (GitHub API), created 2025-10-01 and pushed 2026-10-09.
The tag train is at v1.13 with changelog commits the same week, so maintenance is steady, but the distribution choice (tags, no GitHub releases) keeps the version history low-visibility.
Hacker News has no dedicated thread as of 2026-10-11 searches; the README, the security guide, and the Codex permissions docs are the whole record.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=openai/codex-action&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=openai/codex-action&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=openai/codex-action&type=date&theme=dark&legend=top-left" />
</picture>

## Strengths

- **The key proxy is a guardrail none of the other official Actions offer**: the provider credential stays in a separate process, so a prompt-injected agent cannot read your OpenAI key directly.
- `drop-sudo` is a kernel-enforced default, not a request: `no_new_privs`, empty capability sets, and socket ACL denial on Linux, with the action verifying the kernel cooperates before launching Codex.
- Permission profiles give per-workflow filesystem and network policy, and protected runs reject argument overrides that change permissions, trust, or providers.
- The docs are the most security-literate in this category, down to which self-hosted-runner states fail closed and why re-running after the sudo drop refuses to proceed.

## Cautions

- **The trigger surface is empty by design**: no GitHub App, no mention routing, no prebuilt triage or review suite, just one example workflow you copy and adapt.
- `unsafe` is the only supported strategy on Windows runners, so heterogeneous runner fleets have a hole.
- The account and socket changes on self-hosted runners can outlive the job; the docs direct you to disposable runners and fresh jobs, which is a hard operational constraint.
- The permission-profile system is beta and version-pinned (Codex CLI 0.138.0 and later), and the legacy sandbox it replaces does not compose with it, so mid-migration workflows carry two security models at once.

## Pricing

The action is free and Apache-2.0.
Runs cost GitHub Actions minutes plus OpenAI API usage (Azure OpenAI supported through an endpoint override); the key you provision is billed normally, only stored where the agent cannot read it.

## Compared to

- [Claude Code Action](../claude-code-action/index.md): the mention-driven sibling; choose it for the issue-and-PR conversation flow, accept that its guardrails are workflow flags rather than process isolation.
- [Run Gemini CLI](../run-gemini-cli/index.md): the suite-shipping sibling, with auth hygiene but no runtime privilege reduction.
- [GitHub Agentic Workflows](../github-agentic-workflows/index.md): the multi-engine compiler whose safe-outputs gate is the write-path equivalent of this action's read-path key proxy.

## Bottom line

**Recommended for OpenAI-API teams that want Codex in CI with privilege reduction handled by the vendor, and who will write their own triggers.**
Not for anyone wanting a zero-configuration mention bot, and not for Windows-first runner fleets.
My disagreeable claim: OpenAI shipped the security model the other vendors should copy and forgot to ship the product around it, and most adopters will pick their action by onboarding friction, not by threat model.

## Changes

- 2026-10-11 - Created from the 2026-10-11 official-Actions family admission, with the key-proxy design recorded as the differentiator.

## See also

- [Codex](../../harnesses/codex/index.md) - the CLI this action installs and runs
- [Claude Code Action](../claude-code-action/index.md) - the mention-driven official sibling
- [Run Gemini CLI](../run-gemini-cli/index.md) - the suite-shipping official sibling
- [GitHub Agentic Workflows](../github-agentic-workflows/index.md) - the multi-engine compiled alternative

## References

- https://github.com/openai/codex-action - repository, 1,266 stars, Apache-2.0 license, as of 2026-10-13
- https://api.github.com/repos/openai/codex-action - exact counters (1,266 stars, 180 forks, 82 open issues and pull requests, pushed 2026-10-09, created 2025-10-01)
- https://raw.githubusercontent.com/openai/codex-action/main/README.md - the proxy architecture, safety strategies, permission profiles, trigger allowlists, and Azure setup
- https://api.github.com/repos/openai/codex-action/commits?per_page=3 - the v1.13 changelog commits (2026-10-05 and 2026-10-09)
- https://api.github.com/repos/openai/codex-action/tags?per_page=5 - the tag-versioning scheme, v1.13 newest
- https://developers.openai.com/codex/permissions - the permission-profile schema and enforcement this action configures
- https://hn.algolia.com/api/v1/search?query=codex-action - the coverage scan finding no dedicated thread (2026-10-11), the missing-footprint record
