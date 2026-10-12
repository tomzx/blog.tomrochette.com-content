---
title: "Executions Feature Matrix"
created: 2026-08-24
updated: 2026-10-11
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, comparison, executions, scheduling, workflow-automation]
readability: 3
audience_notes: >
  Engineers deciding where unattended agent execution should live, inside a harness, in Claude's cloud, in GitHub's cloud, in a compiled workflow, in a vendor Action, on your own inbox, or on a self-hosted platform.
  Assumes you know what GitHub Actions, webhooks, and BYOK mean; each column links to a full note with sources.
---

This matrix compares the eleven execution mechanisms profiled in this section, the ways an agent runs without a person starting each task.

**What decides between these eleven is not agent quality but where the trigger definition lives and who can inspect it, and on that axis both hosted schedulers (Copilot automations and Claude routines) fail for any team today, a stronger verdict than their zero-setup convenience deserves.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified.
Each column links to the full research note; every cell traces to a source cited there or in the references.

## The matrix

| Feature                    | [Aeon](../aeon/index.md)                      | [Airut](../airut/index.md)                          | [Claude Code Action](../claude-code-action/index.md)   | [Claude Code hooks](../claude-code-hooks/index.md)  | [Claude Code routines](../claude-code-routines/index.md)  | [Codex Action](../codex-action/index.md)     | [GitHub Agentic Workflows](../github-agentic-workflows/index.md)  | [GitHub Copilot automations](../copilot-automations/index.md)  | [n8n](../n8n/index.md)                | [Run Gemini CLI](../run-gemini-cli/index.md)     | [Trigger.dev](../trigger-dev/index.md)              |
| -------------------------- | --------------------------------------------- | --------------------------------------------------- | ------------------------------------------------------ | --------------------------------------------------- | --------------------------------------------------------- | -------------------------------------------- | ----------------------------------------------------------------- | -------------------------------------------------------------- | ------------------------------------- | ------------------------------------------------ | --------------------------------------------------- |
| Kind                       | framework, runs on Actions                    | self-hosted gateway                                 | official GitHub Action                                 | harness feature                                     | hosted cloud service                                      | official GitHub Action                       | compiled framework                                                | cloud service                                                  | platform, self-host or cloud          | official Action, workflow suite                  | platform, code-first tasks, cloud or self-host      |
| Trigger types              | cron (5-min), reactive triggers, chains, chat | email, Slack, cron, reply-to-continue               | @claude mentions, labels, assignments, schedules       | lifecycle events (~33)                              | schedules, API POST, GitHub events                        | any Actions event, wired by you              | repo events, schedules                                            | repo events, schedules                                         | webhooks, schedules, chat, app events | @gemini-cli mentions, repo events, schedules     | cron, SDK and API calls, batches, delays, debounce  |
| Where execution runs       | your GitHub Actions runners                   | your VM, rootless Podman container per task         | your Actions runners                                   | your machine, web sessions too                      | Anthropic cloud, self-hosted routable                     | your Actions runners                         | Actions runners, self-host ok                                     | GitHub ephemeral runners                                       | self-host or n8n Cloud                | your Actions runners                             | Trigger.dev cloud workers or self-hosted containers |
| Open source                | ✓ MIT                                         | ✓ MIT                                               | ✓ MIT                                                  | ✗ proprietary CLI                                   | ✗ hosted product                                          | ✓ Apache-2.0                                 | ✓ MIT                                                             | ✗                                                              | ~ fair-code license                   | ✓ Apache-2.0                                     | ✓ Apache-2.0                                        |
| Agent lock-in              | 9 harnesses, 10 gateways                      | Claude Code only                                    | Claude Code only                                       | Claude Code only                                    | Claude Code sessions                                      | Codex CLI only                               | 6 engines, more imported                                          | Copilot agent only                                             | any provider, BYOK                    | Gemini CLI only                                  | any provider in code, SDK guides                    |
| Guardrails and permissions | capability hints, Fleet Watcher optional      | rootless containers, egress allowlist, surrogate credentials | write-access checks, secret scrubbing, RISKY flags documented | permission system, managed hooks | env network policy, connectors pruned, no approval gate   | key-holding proxy, drop-sudo default, permission profiles | safe outputs, firewall, threat scans                              | least-privilege tools, no self-approval                        | webhook auth, IP allowlists           | auth hygiene (WIF, app tokens), no runtime sandbox | retries, queues, idempotency, TTLs, HITL waitpoints |
| Versioned with the repo    | ✓ the repo is the deployment                  | ~ .airut/ in repo, server config on the host        | ✓ workflows in repo                                    | ~ project-scope settings                            | ✗ saved in the cloud account                              | ✓ workflows in repo                          | ✓ Markdown in repo                                                | ✗ not in git                                                   | ~ versioned publishes                 | ✓ workflows in repo                              | ✓ tasks are code in the repo                        |
| Scheduled runs             | ✓ 5-minute tick, custom cron                  | ✓ cron tasks, email delivery                        | ✓ Actions cron                                         | ✗ (routines separate)                               | ✓ hourly minimum, cron, one-offs                          | ✓ Actions cron, wired by you                 | ✓ Actions cron                                                    | ✓ hourly to weekly                                             | ✓ hourly to custom cron               | ✓ nightly workflows in the suite                 | ✓ cron, timezones, windows, free plan hourly floor  |
| Pricing                    | free, minutes and inference                   | free self-host, VM plus Claude usage                | free, minutes plus Claude usage                        | in plan, usage-metered handlers                     | in plan, subscription usage                               | free, minutes plus OpenAI usage              | free tool, minutes and inference                                  | paid plan, minutes and credits                                 | free self-host, per execution cloud   | free, minutes plus Gemini usage (free-tier quotas) | free tier, usage compute plus per-run fee           |

## Reading the matrix

**The Kind row is the table of contents: three of these are subscription features (hooks ship inside Claude Code, routines and automations ship inside paid Claude and Copilot plans) and eight are ownable infrastructure (the three official vendor Actions plus the Airut gateway that run on hardware you control, the gh-aw compiler, the Aeon framework, the n8n canvas, and the Trigger.dev platform), and they answer different questions.**
The subscription trio presumes you already live in that ecosystem; the infrastructure eight is a decision about where agent work may run at all.

**Trigger types split the category into inside the session, on the repository, and off the platform: only hooks see the agent's own lifecycle (tool calls, compaction, permission requests), the repository middle holds the two hosted schedulers and all three official Actions (mention phrases, labels, comment slash commands, and hand-wired events on one side, schedules on the other), and the exits belong to n8n (webhooks, chat channels, 1,500+ integrations), Aeon (chat inbound and run-metric triggers), and Airut (email and Slack threads with reply-to-continue).**
Trigger.dev covers the application side the others leave open: durable cron with per-user schedules, SDK and API calls, batches, delays, and debounce, but no repository events and no incoming-webhook node, since you expose your own endpoint.
The three official Actions divide the middle by ergonomics: Claude Code Action owns the mention workflow, Run Gemini CLI ships the copyable triage-and-review suite, and Codex Action runs whatever you wire yourself.
The two GitHub offerings and routines share the middle ground of repository events and schedules, and routines' API trigger adds webhook-like starts, but the toolbox stays one harness, which is why the choice between them is governance rather than capability.

**The open-source row carries a correction the community keeps getting wrong: seven of the eleven are truly open (gh-aw, Aeon, Trigger.dev, Airut, Claude Code Action, Codex Action, and Run Gemini CLI, under MIT or Apache-2.0, though Trigger.dev's checkpointing machinery is cloud-only), n8n is fair-code under the Sustainable Use License and says so itself, and the subscription trio is closed.**
Where execution runs compounds the difference: automations only ever run in GitHub's ephemeral environments, routines run on Anthropic's cloud or a routed self-hosted environment, gh-aw can move to self-hosted or ARC runners, Aeon runs on your own Actions runners, n8n runs wherever you deploy it, including your own hardware, Trigger.dev splits into its managed cloud or a self-hosted container set that lacks the checkpoints, the three official Actions all run on your own Actions runners, and Airut runs each task in a rootless container on a VM you operate.

**Guardrails differ in kind, not degree, and the official Actions split three ways: Codex Action is the only member that keeps the provider key out of the agent's process and drops sudo by default, Claude Code Action leans on write-access trigger checks and secret scrubbing with the risky bypass flags documented in capitals, Run Gemini CLI leans on auth hygiene with no runtime sandbox, and Airut is the only member whose guardrail is architecture, a rootless container with an egress allowlist proxy and surrogate credentials per task.**
The incumbent rows still differ in kind: gh-aw compiles a safe-outputs gate into the workflow itself, automations lean on attribution and write-access approvals, hooks lean on the permission system, routines lean on environment network policy and hand-pruned connectors, n8n leans on webhook authentication, Aeon leans on self-declared capability hints with an optional run gate, and Trigger.dev leans on the reliability primitives (retries, queues, idempotency keys, TTLs) plus code-level human-in-the-loop waitpoints rather than a platform approval gate.
The notes document fail-open behavior in two of the eleven (the hooks `if` filter and n8n's `Only Run If` conditional), routines invert the problem (green status reports infrastructure success while the task may have failed, and every account connector joins the run by default), and GitHub itself calls its approvals "a workflow convenience, not a security control", so none of these is a security boundary on its own.

**The versioned-with-the-repo row is where the two hosted schedulers lose me: an automation layer that neither admins nor teammates can audit and that is not committed to git is a governance hole, while gh-aw's compiled Markdown is exactly the review artifact a team needs.**
hooks sit in between, since project-scope settings can be committed and user scope cannot, n8n versions every publish as revertible snapshots without touching your git, Aeon goes furthest because the deployed repo is the runtime, so every schedule, skill, and memory state is committed by construction, Trigger.dev keeps tasks in your repo with deploys that are versioned and rollback-able from the dashboard, the three official Actions keep their workflows in your repo by definition, and Airut splits the difference, with the container recipe and allowlist in `.airut/` and the server, channels, and credentials on the host.

## Choosing from the matrix

- Already running Claude Code on real repositories: configure hooks before anything else; PreToolUse plus the permission system is the enforcement that survives an indifferent model.
- Live in Claude subscriptions and want nightly or PR-event sessions without a machine awake: Claude Code routines, accepting the no-approval autonomy default, the creator-private storage, and research-preview churn.
- Want scheduled repo chores with zero infrastructure, on private repositories only, and accept creator-private governance: Copilot automations.
- Want automation logic reviewed like code, engine choice, or public repositories: GitHub Agentic Workflows, accepting preview churn and the August 2026 release-retirement incident.
- Want @claude in your issues and pull requests today, on your own runners: Claude Code Action, after reading the RISKY flags.
- Want Codex in Actions with the API key unreachable from the agent: Codex Action, writing your own triggers.
- Want Gemini triage and review from copyable workflows: Run Gemini CLI, accepting the stalled action repo.
- Want to start tasks by email or Slack with the sandbox included: Airut, self-hosted, single maintainer.
- Want an always-on personal agent on your own Actions minutes and will read each skill first: Aeon, accepting the single maintainer and the token-adjacent project.
- Need scheduled or event-triggered agent workloads inside an application you are building, in TypeScript: Trigger.dev, paying for cloud durability or accepting that self-hosted drops the checkpoints.
- Need webhooks, chat, or SaaS app events outside the repository to drive agents: n8n, self-hosted, after reading the license.
- Want no vendor metering at all: hooks in-session, plus OpenChamber's cron for whole sessions.

## The long tail

Keesan12's MartinLoop stays out on the Ralph-loop family rejection recorded 2026-10-07 (410 stars, 68 forks, Apache-2.0, pushed 2026-10-08, 2,809 npm downloads in the trailing month, as of 2026-10-11): a governed loop runner around the same agent CLIs (Claude Code, Codex, Gemini CLI, plus OpenAI-compatible endpoints) that adds budget caps, iteration limits, verifier gates, and verifiable run receipts to the unattended-loop technique documented in the geoffrey-huntley note, but the kind is unchanged, a technique script around existing harnesses rather than a trigger surface or an execution layer, and its footprint (one self-posted 2-point Hacker News story on 2026-05-11, a product site at martinloop.com, an NVIDIA Inception badge) does not separate it from the rejected family; re-review if it ships a hosted trigger surface or adoption moves an order of magnitude.

## Changes

- 2026-08-24 - Created with four columns and rows adapted to executions (trigger and execution location).
- 2026-09-24 - Removed the verification preamble line on owner request.
- 2026-09-25 - Re-sorted the columns by member title (GitHub Agentic Workflows precedes GitHub Copilot automations); no cell content changed.
- 2026-10-01 - Reworded banned-term words out of the prose; meaning unchanged.
- 2026-10-06 - Added the Claude Code routines column (four to five members, sorted alphabetically), rebuilt the table with a separator row matched to the header widths, moved the hooks trigger cell to 33 events, and extended the Kind, trigger, guardrail, versioning, and choosing prose for the fifth member.
- 2026-10-08 - Added the Aeon column (five to six members, sorted alphabetically), extended the Kind, trigger, guardrail, versioning, and choosing prose for the sixth member, corrected the open-source prose now that a second member is MIT, and re-counted the five-to-six references in the intro.
- 2026-10-10 - Added the Trigger.dev column (six to seven members, sorted alphabetically), extended the Kind, trigger, open-source, guardrail, versioning, and choosing prose for the seventh member, and added its pricing, self-hosting, and site references.
- 2026-10-11 - Updated the gh-aw Agent lock-in cell to six engines after the experimental Agy engine joined the built-in list (Gemini deprecated in its favor); no membership change.
- 2026-10-11 - Added the Claude Code Action, Codex Action, Run Gemini CLI, and Airut columns (seven to eleven members, sorted alphabetically), rebuilt the table with a separator row matched to the header widths, extended the Kind, trigger, open-source, guardrails, versioning, and choosing prose for the four new members, and added this long-tail section with the MartinLoop rejection on the Ralph-loop family rule.

## See also

- [Harness Feature Matrix](../../harnesses/harness-feature-matrix/index.md) - the same treatment for terminal harnesses
- [Claude Code](../../harnesses/claude-code/index.md) - the harness that six of the eleven columns build on or drive
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
- https://trigger.dev/ - the product surface and deployment model for the Trigger.dev column, as of 2026-10-11
- https://trigger.dev/pricing - the plan tiers and usage meters for the Trigger.dev pricing cell, as of 2026-10-11
- https://trigger.dev/docs/self-hosting/overview - the cloud-only checkpoints, warm starts, and auto-scaling behind the Trigger.dev open-source and execution cells
- https://github.com/anthropics/claude-code-action - the trigger, execution, license, and pricing cells of the Claude Code Action column, as of 2026-10-11
- https://raw.githubusercontent.com/anthropics/claude-code-action/main/docs/security.md - the guardrails cell (write-access checks, secret scrubbing, RISKY flags)
- https://github.com/openai/codex-action - the kind, execution, license, and pricing cells of the Codex Action column, as of 2026-10-11
- https://raw.githubusercontent.com/openai/codex-action/main/README.md - the guardrails and lock-in cells (key proxy, drop-sudo, permission profiles)
- https://github.com/google-github-actions/run-gemini-cli - the kind, trigger, execution, and license cells of the Run Gemini CLI column, as of 2026-10-11
- https://api.github.com/repos/google-github-actions/run-gemini-cli/releases?per_page=5 - the stalled-release context behind the Run Gemini CLI column, as of 2026-10-11
- https://raw.githubusercontent.com/airutorg/airut/main/README.md - the trigger, execution, guardrails, scheduling, and pricing cells of the Airut column, as of 2026-10-11
- https://api.github.com/repos/Keesan12/martin-loop - the long-tail rejection record (counters, license, activity, as of 2026-10-11)
