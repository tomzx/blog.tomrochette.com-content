---
title: Airut
created: 2026-10-11
updated: 2026-10-31
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, executions, email, slack, claude-code, self-hosted]
readability: 3
audience_notes: >
  Engineers who want to start coding-agent tasks from their inbox or Slack and will run a small server themselves.
  Assumes you know what DMARC, rootless containers, and egress allowlists do.
---

Airut is a self-hosted MIT gateway that starts sandboxed Claude Code tasks from email or Slack messages and returns results as thread replies and pull requests, with each task running in a container behind a network allowlist.

**It is the first execution layer in this category whose trigger is your inbox, and its guardrail is architecture rather than configuration: per-task rootless containers, an egress allowlist proxy, and surrogate credentials, which is the stack every other member asks you to assemble yourself.**

## What it is

You send a message (email or Slack) describing a task; Airut authenticates the sender (DMARC for email, workspace membership for Slack, with per-repo sender authorization), provisions an isolated container with the repository cloned, runs Claude Code, pushes a pull request, and replies in the same thread.
Replying to the thread continues the session, so conversation state, not a terminal, carries the task across days; a cron scheduler runs periodic tasks (daily reviews, nightly checks) and delivers results to email, where a reply re-opens the conversation.
The gateway is Python, installed from PyPI with `uv tool install airut` onto a Linux host with rootless Podman, configured through a web dashboard with live network-activity logs.
It is built by Pyry Haulos, MIT-licensed, and developed through its own workflow: the README states all development since the first working version happened by sending instructions to Airut and reviewing the PRs.
A companion `airut-sandbox` CLI and `airutorg/sandbox-action` extend the same container and allowlist isolation to CI, covering the code an agent's PR triggers on the runner side.

## Status

**Young, active, and nearly invisible.**
84 stars, 3 forks, and 1 open issue as of 2026-10-31 (GitHub API), created 2026-02-03 and pushed 2026-10-31.
PyPI carries 0.27.1, with 287 downloads in the trailing month (2026-10-01 to 2026-10-31).
The community footprint is three self-posted Show HN threads (2, 1, and 2 points, zero comments, February through March 2026), so there is no independent coverage or adoption evidence, and that absence is itself the signal for a project with this much documentation depth.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=airutorg/airut&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=airutorg/airut&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=airutorg/airut&type=date&legend=top-left" />
</picture>

## Strengths

- **The trigger is a message thread, and reply-to-continue persistence means an agent task survives across days with no terminal, app, or workflow file in the loop.**
- Defense-in-depth is architecture: each task gets a rootless Podman container, egress restricted through an allowlisting proxy, and credential masking with surrogate keys, so the sandbox is not a permission setting someone can flip.
- Scheduled tasks deliver results into email, and replies continue the conversation, the rare scheduler in this category with a human channel built in.
- The web dashboard exposes live network-activity logs per task, making the allowlist auditable rather than documented.
- The CI sandbox action closes the gap most agent workflows leave open: your own CI running the agent's code outside the agent's sandbox.

## Cautions

- **One maintainer and no visible adoption**: 84 stars, single-digit forks, and a self-reported community footprint of three zero-comment Show HN threads as of 2026-10-31.
- Self-hosting is the only mode, and the prerequisites (Linux, rootless Podman, a dedicated IMAP/SMTP account or Slack app per repository) put the operations burden on you.
- Claude Code only, and the autonomy pitch (a full-permission agent inside the container) presumes the boundary holds; the security-model documentation is the audit artifact you must read yourself.
- The email channel inherits email's failure modes: DMARC-verified senders plus per-repo authorization are all that stands between a stranger and an agent task on your code.

## Pricing

Free and MIT-licensed, self-hosted only.
The costs are your VM, your Claude subscription or API key, and the email or Slack infrastructure the channels ride on.

## Compared to

- [n8n](../n8n/index.md): the general trigger canvas with chat nodes and 1,500+ integrations; Airut is a purpose-built coding-agent gateway where the sandbox is included rather than assembled.
- [Claude Code routines](../claude-code-routines/index.md): scheduled sessions in Anthropic's cloud with no messaging channel; Airut is self-hosted, thread-driven, and runs on your hardware.
- [Aeon](../aeon/index.md): the Actions-based unattended framework with Telegram inbound; Airut keeps execution off Actions entirely, inside containers on your own VM.

## Bottom line

**Recommended for solo engineers or small teams who want to drive Claude Code from their inbox with credible isolation and will operate a small server.**
Not for anyone needing a supported product, multi-harness execution, or evidence of adoption beyond the author.
My disagreeable claim: at 84 stars this is the least proven member of the category, and it still has the best default security architecture in it, because container, allowlist, and surrogate credentials are what every other member's guardrails row describes piecewise.

## Changes

- 2026-10-11 - Created from the 2026-10-11 entrant scan, with the thin community footprint recorded as the critical signal.
- 2026-10-18 - Fully re-verified in rotation with every cited URL re-fetched: the README architecture claims (rootless Podman, allowlist proxy, surrogate credentials, CI sandbox action, dogfooding), the airut.org site, the 0.27.0 PyPI version, the 287 trailing-month downloads, and the three-thread community footprint all re-confirmed unchanged after the 2026-10-18 push.
- 2026-10-24 - Recorded the v0.27.1 release (2026-10-24), the first since v0.27.0; the README architecture claims and the counters (84 stars, 3 forks, 1 open issue) re-verified unchanged around it.
- 2026-10-25 - Corrected the star-history chart fallback markup (the img fallback carried the dark-theme parameter; it now points at the default chart).
- 2026-10-31 - Fully re-verified in rotation with every cited URL re-fetched: the README architecture claims (rootless Podman, allowlist proxy, surrogate credentials, scheduled tasks, dashboard, CI sandbox action, dogfooding), the airut.org site, the PyPI package (still 0.27.1), the 287 trailing-month downloads, and the three-thread community footprint (2, 1, and 2 points, zero comments) all re-confirmed unchanged after the 2026-10-31 push; the counters re-verified unchanged (84 stars, 3 forks, 1 open issue).

## See also

- [Sandboxing](../../sandboxing/_index.md) - the category holding the boundary tools Airut builds in
- [n8n](../n8n/index.md) - the general trigger canvas Airut specializes against
- [Claude Code routines](../claude-code-routines/index.md) - the hosted scheduled-session alternative
- [Claude Code](../../harnesses/claude-code/index.md) - the harness every Airut task runs

## References

- https://github.com/airutorg/airut - repository, 84 stars, MIT license, description, as of 2026-10-11 (re-fetched 2026-10-31)
- https://api.github.com/repos/airutorg/airut - exact counters (84 stars, 3 forks, 1 open issue, pushed 2026-10-31, created 2026-02-03; re-verified 2026-10-31)
- https://raw.githubusercontent.com/airutorg/airut/main/README.md - the channel model, sandbox architecture, scheduled tasks, dashboard, CI sandbox action, and the dogfooding claim (re-fetched 2026-10-31)
- https://pypi.org/pypi/airut/json - the PyPI package at 0.27.1, "Sandboxed Claude Code over email and Slack" (re-fetched 2026-10-31)
- https://pypistats.org/api/packages/airut/recent - 287 trailing-month downloads (2026-10-01 to 2026-10-31)
- https://airut.org - the project site: the message-to-deploy pitch and the surrogate-credential walkthrough (re-fetched 2026-10-31)
- https://hn.algolia.com/api/v1/search?query=airut&tags=story - the three self-posted Show HN threads (2, 1, and 2 points, zero comments), the footprint record as of 2026-10-31
- https://news.ycombinator.com/item?id=46947714 - the first Show HN thread, "Sandboxed Claude Code sessions over email" (2026-02-09, 2 points, zero comments)
