---
title: Run Gemini CLI
created: 2026-10-11
updated: 2026-10-18
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, executions, github-actions, gemini, scheduling]
readability: 3
audience_notes: >
  Maintainers considering Google's Gemini for automated issue triage and pull request review on GitHub.
  Assumes you know Actions workflows, API keys versus workload identity federation, and what a slash command is.
---

Run Gemini CLI is Google's official GitHub Action that runs Gemini CLI inside repository workflows, shipped with a copyable suite of dispatch, issue-triage, pull-request-review, and assistant workflows triggered by mentions, repository events, and schedules.

**It is the batteries-included one of the three official vendor Actions, and also the neglected one: the workflow suite is the product, while the action repository has been quiet since August and its release train stopped in April.**

## What it is

An action (`google-github-actions/run-gemini-cli`) plus a set of prebuilt workflows you copy into `.github/workflows`, with `gemini-dispatch.yml` routing events and comment commands to the right one.
Mentioning @gemini-cli in an issue or pull request starts a conversational assistant, with slash commands such as `/review` and `/triage`; issues and pull requests also fire automated triage and review workflows, and schedules cover nightly runs.
A `GEMINI.md` file in the repository carries project instructions, and Gemini CLI extensions and tool calling (including the `gh` CLI) extend what a run can do.
Authentication is the deepest of the trio: a free-tier Gemini API key from AI Studio, Vertex AI, workload identity federation, or Gemini Code Assist, and observability ships OpenTelemetry traces, metrics, and logs to your own Google Cloud project.
It is Apache-2.0, published by the google-github-actions organization, and set up from Gemini CLI with `/setup-github`.

## Status

**Shipped and widely starred, with a stalled action repo and a fast product behind it.**
2,105 stars as of 2026-10-13, 288 forks and 85 open issues and pull requests as of 2026-10-18 (GitHub API), created 2025-07-11, but the last push was 2026-08-21, fifty-eight days before this check.
The release train stopped at v0.1.22 (2026-04-24), nearly six months before this check, after monthly releases through the winter.
The wrapped product, google-gemini/gemini-cli, is enormous and active (about 107.3k stars as of 2026-10-13, pushed 2026-10-18 UTC), so the CLI keeps moving while the action layer it powers on GitHub has gone quiet, and no dedicated Hacker News thread exists as of 2026-10-18 searches.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=google-github-actions/run-gemini-cli&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=google-github-actions/run-gemini-cli&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=google-github-actions/run-gemini-cli&type=date&theme=dark&legend=top-left" />
</picture>

## Strengths

- **The only one of the three official Actions shipping a full workflow suite**: dispatch router, issue triage, pull request review, and a conversational assistant, all copyable and meant to be customized.
- The @gemini-cli mention flow gives it the conversational feel of Claude Code Action without any app install.
- Auth flexibility is the trio's deepest, from a free AI Studio key to Vertex AI and workload identity federation, so the same workflow moves from hobby to enterprise credentials.
- OpenTelemetry observability into your own Google Cloud project is unique among the official Actions.

## Cautions

- **The action layer is going stale in public**: last push 2026-08-21, no release since v0.1.22 on 2026-04-24, as of 2026-10-18.
- There is no runtime sandbox; the workflow token's declared permissions are the boundary, and the best-practices doc leans on version pinning, branch protection, and restricted approvers.
- Google's own agentic-workflows product (GitHub Agentic Workflows) deprecated its built-in Gemini engine in favor of its Agy engine, so Google's bet inside the compiler layer has moved off the CLI this action runs.
- The settings JSON, extensions, and CLI-version inputs inherit Gemini CLI's fast churn, and a stalled action repo is a slow responder to that churn.

## Pricing

The action is free and Apache-2.0.
Runs cost GitHub Actions minutes plus Gemini usage: the AI Studio API key carries free-of-charge quotas, while Vertex AI and Code Assist routes bill normally, so scheduled triage at scale is a billing decision.

## Compared to

- [Claude Code Action](../claude-code-action/index.md): the mention-driven sibling with app-based scoping; this one copies plain workflows and asks no app install, but ships no injection-specific mitigations.
- [Codex Action](../codex-action/index.md): the security-first sibling with no suite; pick it when the key proxy matters more than ready-made triage.
- [GitHub Agentic Workflows](../github-agentic-workflows/index.md): the compiler layer, whose safe outputs and cost caps this suite lacks, and whose Gemini engine is now deprecated.

## Bottom line

**Recommended for Google-stack teams that want issue triage and PR review running on Gemini, on their own runners, and will own the workflow files afterward.**
Not for anyone needing an actively shipping action layer or runtime sandboxing.
My disagreeable claim: this is the README I would copy from among the three official Actions, and the action I would least want to pin unattended automation to, because nearly six months without a release is how drift starts.

## Changes

- 2026-10-11 - Created from the 2026-10-11 official-Actions family admission, with the stalled action repo recorded as the critical angle.
- 2026-10-18 - Fully re-verified in rotation with every cited URL re-fetched: the stalled-repo status (last push still 2026-08-21, releases still stopping at v0.1.22), the README claims (workflow suite, mention commands, auth options, observability), the wrapped CLI's activity, and the still-missing dedicated HN thread all re-confirmed; refreshed the as-of dates, the fork count (287 to 288), and the stale-duration figures.

## See also

- [Gemini CLI](../../harnesses/gemini-cli/index.md) - the harness this action runs
- [GitHub Agentic Workflows](../github-agentic-workflows/index.md) - the compiler layer that deprecated its Gemini engine
- [Claude Code Action](../claude-code-action/index.md) - the Anthropic sibling
- [Codex Action](../codex-action/index.md) - the OpenAI sibling

## References

- https://github.com/google-github-actions/run-gemini-cli - repository, 2,105 stars, Apache-2.0 license, as of 2026-10-13
- https://api.github.com/repos/google-github-actions/run-gemini-cli - exact counters (2,105 stars as of 2026-10-13, 288 forks, 85 open issues and pull requests, pushed 2026-08-21, created 2025-07-11)
- https://raw.githubusercontent.com/google-github-actions/run-gemini-cli/main/README.md - the workflow suite, mention commands, GEMINI.md context, auth options, and observability (re-fetched 2026-10-18)
- https://api.github.com/repos/google-github-actions/run-gemini-cli/releases?per_page=5 - the release train stopping at v0.1.22 (2026-04-24, re-verified 2026-10-18)
- https://api.github.com/repos/google-gemini/gemini-cli - the wrapped product's scale and activity (about 107.3k stars as of 2026-10-13, pushed 2026-10-18 UTC)
- https://hn.algolia.com/api/v1/search?query=run-gemini-cli - the coverage scan finding no dedicated thread (2026-10-18), the missing-footprint record
