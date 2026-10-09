---
title: "Executions Feature Matrix"
created: 2026-08-24
updated: 2026-10-08
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, comparison, executions, scheduling, workflow-automation]
readability: 3
audience_notes: >
  Engineers deciding where unattended agent execution should live, inside a harness, in Claude's cloud, in GitHub's cloud, in a compiled workflow, or on a self-hosted platform.
  Assumes you know what GitHub Actions, webhooks, and BYOK mean; each column links to a full note with sources.
---

This matrix compares the six execution mechanisms profiled in this section, the ways an agent runs without a person starting each task.

**What decides between these six is not agent quality but where the trigger definition lives and who can inspect it, and on that axis both hosted schedulers (Copilot automations and Claude routines) fail for any team today, a stronger verdict than their zero-setup convenience deserves.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified.
Each column links to the full research note; every cell traces to a source cited there or in the references.

## The matrix

| Feature                    | [Aeon](../aeon/index.md)                      | [Claude Code hooks](../claude-code-hooks/index.md)  | [Claude Code routines](../claude-code-routines/index.md)  | [GitHub Agentic Workflows](../github-agentic-workflows/index.md)  | [GitHub Copilot automations](../copilot-automations/index.md)  | [n8n](../n8n/index.md)                |
| -------------------------- | --------------------------------------------- | --------------------------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------- | -------------------------------------------------------------- | ------------------------------------- |
| Kind                       | framework, runs on Actions                    | harness feature                                     | hosted cloud service                                      | compiled framework                                                | cloud service                                                  | platform, self-host or cloud          |
| Trigger types              | cron (5-min), reactive triggers, chains, chat | lifecycle events (~33)                              | schedules, API POST, GitHub events                        | repo events, schedules                                            | repo events, schedules                                         | webhooks, schedules, chat, app events |
| Where execution runs       | your GitHub Actions runners                   | your machine, web sessions too                      | Anthropic cloud, self-hosted routable                     | Actions runners, self-host ok                                     | GitHub ephemeral runners                                       | self-host or n8n Cloud                |
| Open source                | ✓ MIT                                         | ✗ proprietary CLI                                   | ✗ hosted product                                          | ✓ MIT                                                             | ✗                                                              | ~ fair-code license                   |
| Agent lock-in              | 9 harnesses, 10 gateways                      | Claude Code only                                    | Claude Code sessions                                      | 5 engines, more imported                                          | Copilot agent only                                             | any provider, BYOK                    |
| Guardrails and permissions | capability hints, Fleet Watcher optional      | permission system, managed hooks                    | env network policy, connectors pruned, no approval gate   | safe outputs, firewall, threat scans                              | least-privilege tools, no self-approval                        | webhook auth, IP allowlists           |
| Versioned with the repo    | ✓ the repo is the deployment                  | ~ project-scope settings                            | ✗ saved in the cloud account                              | ✓ Markdown in repo                                                | ✗ not in git                                                   | ~ versioned publishes                 |
| Scheduled runs             | ✓ 5-minute tick, custom cron                  | ✗ (routines separate)                               | ✓ hourly minimum, cron, one-offs                          | ✓ Actions cron                                                    | ✓ hourly to weekly                                             | ✓ hourly to custom cron               |
| Pricing                    | free, minutes and inference                   | in plan, usage-metered handlers                     | in plan, subscription usage                               | free tool, minutes and inference                                  | paid plan, minutes and credits                                 | free self-host, per execution cloud   |

## Reading the matrix

**The Kind row is the table of contents: three of these are subscription features (hooks ship inside Claude Code, routines and automations ship inside paid Claude and Copilot plans) and three are ownable infrastructure (an MIT-licensed compiler, a self-hostable platform, an MIT framework that deploys as your own repo), and they answer different questions.**
The subscription trio presumes you already live in that ecosystem; the infrastructure trio is a decision about where agent work may run at all.

**Trigger types split the category into inside the session and outside it: only hooks see the agent's own lifecycle (tool calls, compaction, permission requests), n8n reaches furthest past the repository (webhooks, chat channels, 1,500+ integrations), and Aeon adds chat inbound and run-metric triggers on top of cron.**
The two GitHub offerings and routines share the middle ground of repository events and schedules, and routines' API trigger adds webhook-like starts, but the toolbox stays one harness, which is why the choice between them is governance rather than capability.

**The open-source row carries a correction the community keeps getting wrong: gh-aw and Aeon are both truly open (MIT), n8n is fair-code under the Sustainable Use License and says so itself, and the subscription trio is closed.**
Where execution runs compounds the difference: automations only ever run in GitHub's ephemeral environments, routines run on Anthropic's cloud or a routed self-hosted environment, gh-aw can move to self-hosted or ARC runners, Aeon runs on your own Actions runners, and n8n runs wherever you deploy it, including your own hardware.

**Guardrails differ in kind, not degree: gh-aw compiles a safe-outputs gate into the workflow itself, automations lean on attribution and write-access approvals, hooks lean on the permission system, routines lean on environment network policy and hand-pruned connectors, n8n leans on webhook authentication, and Aeon leans on self-declared capability hints with an optional run gate.**
The notes document fail-open behavior in two of the six (the hooks `if` filter and n8n's `Only Run If` conditional), routines invert the problem (green status reports infrastructure success while the task may have failed, and every account connector joins the run by default), and GitHub itself calls its approvals "a workflow convenience, not a security control", so none of these is a security boundary on its own.

**The versioned-with-the-repo row is where the two hosted schedulers lose me: an automation layer that neither admins nor teammates can audit and that is not committed to git is a governance hole, while gh-aw's compiled Markdown is exactly the review artifact a team needs.**
hooks sit in between, since project-scope settings can be committed and user scope cannot, n8n versions every publish as revertible snapshots without touching your git, and Aeon goes furthest because the deployed repo is the runtime, so every schedule, skill, and memory state is committed by construction.

## Choosing from the matrix

- Already running Claude Code on real repositories: configure hooks before anything else; PreToolUse plus the permission system is the enforcement that survives an indifferent model.
- Live in Claude subscriptions and want nightly or PR-event sessions without a machine awake: Claude Code routines, accepting the no-approval autonomy default, the creator-private storage, and research-preview churn.
- Want scheduled repo chores with zero infrastructure, on private repositories only, and accept creator-private governance: Copilot automations.
- Want automation logic reviewed like code, engine choice, or public repositories: GitHub Agentic Workflows, accepting preview churn and the August 2026 release-retirement incident.
- Want an always-on personal agent on your own Actions minutes and will read each skill first: Aeon, accepting the single maintainer and the token-adjacent project.
- Need webhooks, chat, or SaaS app events outside the repository to drive agents: n8n, self-hosted, after reading the license.
- Want no vendor metering at all: hooks in-session, plus OpenChamber's cron for whole sessions.

## Changes

- 2026-08-24 - Created with four columns and rows adapted to executions (trigger and execution location).
- 2026-09-24 - Removed the verification preamble line on owner request.
- 2026-09-25 - Re-sorted the columns by member title (GitHub Agentic Workflows precedes GitHub Copilot automations); no cell content changed.
- 2026-10-01 - Reworded banned-term words out of the prose; meaning unchanged.
- 2026-10-06 - Added the Claude Code routines column (four to five members, sorted alphabetically), rebuilt the table with a separator row matched to the header widths, moved the hooks trigger cell to 33 events, and extended the Kind, trigger, guardrail, versioning, and choosing prose for the fifth member.
- 2026-10-08 - Added the Aeon column (five to six members, sorted alphabetically), extended the Kind, trigger, guardrail, versioning, and choosing prose for the sixth member, corrected the open-source prose now that a second member is MIT, and re-counted the five-to-six references in the intro.

## See also

- [Harness Feature Matrix](../../harnesses/harness-feature-matrix/index.md) - the same treatment for terminal harnesses
- [Claude Code](../../harnesses/claude-code/index.md) - the harness that four of the six columns build on or drive
- [OpenChamber](../../surfaces/openchamber/index.md) - self-hosted cron scheduling for coding sessions, no per-run billing
- [Surface Feature Matrix](../../surfaces/surface-feature-matrix/index.md) - the sibling matrix for editors and environments
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the map these columns come from

## References

- https://code.claude.com/docs/en/hooks - event surface and handler types for the hooks column
- https://code.claude.com/docs/en/routines - trigger types, autonomy default, and cloud execution for the routines column
- https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations - triggers, visibility, and security model for the automations column
- https://github.github.com/gh-aw/ - frontmatter triggers, schedules, engines, guardrails, and runners for the gh-aw column
- https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent - Actions-powered sessions, the 59-minute cap, and billing
- https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/ - webhook trigger semantics for the n8n column
- https://docs.n8n.io/n8n-community-license/community-license.md - the not-open-source licensing cell
