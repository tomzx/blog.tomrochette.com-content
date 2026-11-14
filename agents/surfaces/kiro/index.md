---
title: Kiro
created: 2026-08-24
updated: 2026-11-14
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, surfaces, ai-editors, aws]
readability: 3
audience_notes: >
  Engineers in the AWS orbit evaluating the spec-driven agentic IDE.
  Assumes you know what a spec is and what subscription credits meter.
---

Kiro is AWS's agentic IDE: spec-driven by default, with a CLI, web, mobile, and a multi-agent Crew, metered in credits from a 50-credit free tier to a $200/month Power plan.

**Kiro is the only major IDE vendor that treats specs, requirements, and design documents as the primary artifact rather than chat, and that bet either matches how your team already works or will feel like bureaucracy.**

## What it is

**Two modes organize everything: vibe mode for direct iteration and spec mode, where Kiro generates requirements and design docs you edit before implementation proceeds.**
Agent hooks trigger on file changes or schedules, and a subscription covers the IDE, the CLI, Kiro on the web, mobile, Crew (parallel agents), and ACP-compatible IDEs, an unusually wide surface list.
The default model router is Auto, mixing frontier and specialist models, with explicit choices spanning GPT-5.6, Claude Opus 5 and Sonnet 5, DeepSeek, MiniMax, GLM-5, and Qwen3 Coder Next.

## Status

**Active and enterprise-ready.**
The vendor changelog shows weekly releases, with the November 10 to 12 entries (Kiro Mobile for Android on Google Play running cloud sessions from the phone on Pro and up, IDE 1.4.178's workflow-run following and post-compaction skill reloads, CLI 3.3.0's `/copy N` history commands and configurable compaction threshold, CloudTrail audit logging of Kiro service MCP tool calls in us-east-1 and eu-central-1, CLI 3.2.1 and 3.2.0's tool-output detail control, full-screen Mermaid viewer, and OAuth-free MCP sign-in, IDE 1.4.154's Approve for me permission modes, the Grok 4.7 experimental model with a 500K context window at 2.7x and 5.4x credit multipliers, Enterprise Management in preview with the Kiro Crew LTS edition, and credit pooling extended to Okta and Microsoft Entra ID) above the November 4 entries (Claude Haiku 5.5 and Kimi K3 reaching general availability with full support, the Excluded Models indemnity exception lifted for Haiku 5.5 but remaining on Kimi K3, and enterprise credit pooling at $20 per seat per month for 500 pooled monthly credits, the only option for new Kiro profiles) above CLI 3.0.0 (November 3, 2026, V3 by default with the Classic interface, the desktop app, and inline autocomplete retired, leaving a single standalone `kiro-cli` binary and cloud sessions, Memory, Approve for me, the sandbox, and Workflows as V3-native) above CLI 2.37.0 (October 30, automatic V2 agent upgrades by default when a V3 session starts, and terminal sign-in from ACP clients) above CLI 2.36.0 (October 29, the Approve for me policy preset that settles routine actions in interactive V3 sessions) above the Web release of October 28 (per-session recaps, workflows that ask for input during planning, and Schedule replacing Automations) above IDE 1.4.62 and 1.4.51 (October 28 and 27, Windows system-wide installers and Shift-free drag-and-drop chat attachments, then faster reconnect after session expiry and keyboard comments in Markdown Review) above CLI 2.35.0 (October 27, the elevated-privilege warning and organization MCP and web-tools controls in V3) above CLI 2.34.0 (October 23, MCP elicitation, workflow controls, and memory deletion from `/memories`) above the Claude Haiku 5.5 experimental model addition (October 23, a 1M-token context window at 0.06x up to 100K tokens and 0.3x beyond) above CLI 2.33.1 (October 21, 2026, workflows starting only when you ask) above CLI 2.33.0 (October 20, a workspace-trust screen that gates a cloned repository's hooks, agents, MCP servers, and workflows behind an explicit trust choice, and model fallback saved per session) above IDE 1.4.10 (October 20, the new IDE Memory defaulting to off) and IDE 1.4.0 (October 19, Memory carrying repository conventions and corrections across sessions in the IDE, with a Memory view and use-only modes) above Crew 0.9.0 (October 16, crewmate profile cards, per-crewmate dynamic dashboards and remote crews as live windows, both previews, plus usage estimates that project when credits run out) above CLI 2.32.0 (October 15, folder-level write approvals, non-interactive V3 cloud sessions, and workflow plan previews) above the CLI at 2.31.1 (October 14, 2026, Mermaid diagrams drawn directly in chat) above 2.31.0 of October 13 (the local command sandbox and local autonomous mode for every V3 user, MCP tools loaded on demand, and KIRO_HOME extended across V3 configuration) and the IDE at 1.3.11 (October 15, 2026, Markdown Review with batched comments on rendered files, a What's New announcement browser, and workflow step notifications) above 1.3.0 of October 13 (the local command sandbox, starting saved Workflows from chat, and live session status on editor tabs), above the CLI at 2.30.0 (October 12, 2026, a gradually rolling startup prompt inviting a V3 switch ahead of CLI 3.0 becoming the default harness at the end of October, plus V3 model-fallback notices that show when a turn moved to another model) above the 2.29.1 patch of October 10 above the 2.29.0 release of October 9, 2026 (Memory for local V3 sessions that carries repository commands and conventions into later chats, with read-write, read-only, and off controls and automatic memory updates) above the 2.28.0 release of October 5, 2026 (an interactive offer to switch Classic sessions to 3.0 with upgraded agent configs, category-based matching for V3 hooks across shell, read, write, or a specific MCP server or tool, and steadier long V3 sessions) above the 2.27.0 release of October 1, 2026 (control over how V3 delegates when Workflows are enabled, live file and folder context in Steering, and saved prompts exposed as slash commands) above the 2.26.0 release of September 30 (opt-in Workflows for reusable multi-step tasks in V3, Classic migration guidance, and stricter V3 approval safeguards) above the 2.25.0 release of September 28 (Powers management from chat or the command line, V3 output styles, fullscreen scroll tuning, and a SessionEnd Hook) and the 2.24.0 release of September 23 (session-wide tool approval in V3, combined session dashboard controls, and environment isolation that stops project .env files auto-loading, after the 2.23.0 and 2.23.1 pair of September 21 to 23 with reasoning controls in /model and V3 cloud sessions that start before connecting a repository, and the 2.22.0 to 2.22.1 line of September 16 to 17, which added fullscreen chat and a streamlined session dashboard) and the IDE at 1.2.56 since October 8, 2026 (a Workflows feedback link, fixes across chat, terminal, and source control, and improved workflow reliability, spec-only commands, and Hook matching), up from the 1.2.4 release of September 30, 2026 (IDE Workflows, safeguards for untrusted workspaces, and enterprise sign-in controls), up from the 1.1.70 release of September 24 (configurable terminal timeouts, clickable file links, and Agent Focus session restore, continuing the 1.1 line that began September 14 with durable agent artifacts and native ARM64 builds, up from the 1.0.437 line of September 1, the same day Kiro Web reached general availability and Kiro came under AWS ISO/IEC 27001:2022 certification), while Crew 0.7.0 landed September 24, 2026 with live settings, durable queued work that survives Gateway restarts, pull request watches beyond GitHub (GitLab, Bitbucket Cloud, and Azure DevOps), OpenCode and goose agent backends, and AWS Fargate remote crews, building on Crew 0.6.0's September 5 session harness selection (Claude Code, Codex, or KAS); pricing, GovCloud availability, and enterprise billing through AWS are all shipped.
On October 12, 2026 Kiro came in scope for FedRAMP Class C in AWS US East (N. Virginia), opening the government-workload market.
The same day, Kiro Web added a per-model fallback choice, a model picker on workflow steps, and session-reopen previews that show the saved conversation while the sandbox restarts.
On October 14, 2026 Claude Sonnet 4 reached end of life in Kiro, leaving Sonnet 5.5 as the line's latest.
On October 15, 2026 Kimi K3 joined the model list with experimental support across IDE, CLI, Crew, and Web (Moonshot's open-weight model, text and images, a 1M-token context window, a 2.4x credit multiplier, Pro tiers and up, US geography).
On October 30, 2026 Claude Opus 5.5 and GPT-5.6 Sol reached general availability with full support, their Experimental labels dropped and the excluded-models indemnity exception lifted.
On November 4, 2026 Claude Haiku 5.5 and Kimi K3 followed the same path out of experimental, though Kimi K3 remains a Kiro Excluded Model.
The same day, credit pooling arrived for enterprise administrators: seats at $20 per month each add 500 monthly credits to one shared pool with per-user, per-group, and per-profile limits, existing customers can switch through a one-way wizard, and credit pooling is the only option for new Kiro profiles.
On September 30, 2026 Workflows reached Kiro Web: opt-in reusable multi-step agent plans running in cloud sessions, with investigate, feature-pipeline, and publish-pr bundled recipes.
On October 2, 2026 Claude Sonnet 5.5 joined the model list across the IDE, CLI, Crew, and Web for paid tiers in us-east-1 and eu-central-1, a 1M-token context window at a 1.3x credit multiplier, two days after CLI 2.27.0.
The September 14 changelog also raised the GPT-5.6 family to a 1M context window, billed at double the short-context rate above 272K tokens.
On September 16, 2026 the Claude Fable 5.1 Preview began rolling out to Kiro Enterprise clients: a 1M-context model billing at a 6x credit multiplier, with US-East-only inference and traffic retained up to 30 days for abuse detection.
On September 28, 2026 Claude Opus 5.5 joined the model list across the IDE, CLI, Crew, and Web at a 2.0x credit multiplier, down from Opus 5's 2.2x.
On October 9, 2026 both Claude Sonnet 5.5 (1.3x) and Opus 5.5 (2.0x) reached AWS GovCloud (US) East and West regions for the IDE and CLI at their existing multipliers.
The public issue tracker (kirodotdev/Kiro, about 4.4k stars (4,367) as of 2026-10-16) saw only README docs and Dependabot dependency commits on August 26-27, 2026, with no feature commits since June 22, 2026, so release evidence still lives on kiro.dev, not the repository.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=kirodotdev/Kiro&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=kirodotdev/Kiro&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=kirodotdev/Kiro&type=date&legend=top-left" />
</picture>

Its spec workflow has been influential enough that community projects port it to other harnesses.

## Strengths

- **Specs as first-class artifacts** turn agent work into reviewable documents, the same pull-based review pattern this blog argues for elsewhere.
- One subscription spans IDE, CLI, web, mobile, Crew, and ACP-compatible editors.
- Free tier includes Claude Sonnet 4.5 and open-weight models, a genuine trial rather than a teaser.
- Enterprise identity, billing, and GovCloud come from AWS machinery that orgs already run.

## Cautions

- **Credits are the trap**: 1,000 credits on Pro sounds large until spec tasks, refinements, and agent hooks each meter fractions of a credit at model-specific multipliers, and add-ons cost $0.04 per credit.
- Terms explicitly forbid routing subscription usage through third-party automation harnesses, so your Kiro credits stay in Kiro surfaces.
- An August 2025 writeup documented arbitrary code execution via indirect prompt injection in the IDE.
- The client is closed; the GitHub repository is feedback and docs, not source.

## Pricing

Free: $0 with 50 credits, open-weight models plus Claude Sonnet 4.5.
Pro $20 (1,000 credits), Pro+ $40 (2,000), Pro Max $100 (5,000), Power $200 (10,000), add-on credits at $0.04 each, enterprise via AWS with SSO and overage controls, with credit pooling at $20 per seat per month for 500 pooled credits as the only option for new profiles, GovCloud priced about 20% higher, as of 2026-11-14 (re-verified, tier prices unchanged).

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-18 | All tiers | Baseline: Free $0 (50 credits), Pro $20 (1,000), Pro+ $40 (2,000), Pro Max $100 (5,000), Power $200 (10,000), add-on credits $0.04 each, GovCloud about 20% higher. | [kiro.dev/pricing](https://kiro.dev/pricing/) |
| 2026-11-04 | Credit sharing (enterprise) | Introduced: $20/month per seat adds 500 monthly credits to one shared pool, with per-user, per-group, and per-profile limits and credits purchased separately good for one year; the only option for new Kiro profiles. | [kiro.dev/changelog](https://kiro.dev/changelog/) |

## Compared to

- [Cursor](../cursor/index.md): chat-first versus spec-first; pick Kiro when requirements artifacts matter to your team.
- [JetBrains IDEs](../jetbrains/index.md): deep analysis versus spec workflow; both sell credits.
- [VS Code + Copilot](../vscode-copilot/index.md): the neutral host; Kiro is an opinionated environment with AWS gravity.

## Bottom line

**Recommended for spec-disciplined teams, especially those already buying through AWS.**
Not for credit-averse solo engineers or anyone who wants an open client.

## Changes

- 2026-08-24 - Created in the owner-requested Surfaces expansion with credit tiers and the incident record.
- 2026-08-25 - Corrected the status attribution, moving release-cadence evidence to the vendor changelog and adding it as a reference.
- 2026-09-02 - Added Kiro Web general availability and the ISO 27001 certification.
- 2026-09-12 - Recorded Crew 0.6.0 session-harness selection alongside CLI patch updates.
- 2026-09-16 - Recorded IDE 1.1 (agent artifacts, native ARM64) and the GPT-5.6 1M-context upgrade, both September 14.
- 2026-09-18 - Recorded CLI 2.22.0 (fullscreen chat, streamlined session dashboard) and the Claude Fable 5.1 Enterprise Preview (1M context, 6x multiplier), both September 16.
- 2026-09-20 - Added the Price history section tracking price changes in a table, per the new owner rule.
- 2026-09-24 - Recorded CLI 2.23.1 (reasoning controls, V3 cloud sessions before repo connection) and IDE 1.1.70 (terminal timeouts, clickable file links, Focus session restore), September 21 through 24; prices unchanged.
- 2026-09-26 - Recorded CLI 2.24.0 (September 23, session-wide tool approval, dashboard controls, environment isolation) and Crew 0.7.0 (September 24, live settings, durable work, PR watches beyond GitHub, OpenCode and goose backends, Fargate remote crews) as the new latest releases.
- 2026-10-02 - Recorded CLI 2.26.0 (September 30, opt-in Workflows for reusable multi-step tasks in V3, Classic migration guidance, stricter V3 approval safeguards) as the new latest CLI release.
- 2026-10-02 - Recorded the releases the 2.26.0 pass missed: CLI 2.25.0 (September 28, Powers management, V3 output styles, SessionEnd Hook), IDE 1.2.4 (September 30, IDE Workflows, untrusted-workspace safeguards, enterprise sign-in controls) as the new latest IDE, and the Claude Opus 5.5 model addition (September 28, 2.0x multiplier); prices unchanged.
- 2026-10-03 - Recorded CLI 2.27.0 (October 1, control over how V3 delegates when Workflows are enabled, live file and folder context in Steering, saved prompts as slash commands) as the new latest CLI release; prices unchanged.
- 2026-10-04 - Recorded Kiro Web Workflows (September 30, opt-in multi-step plans in cloud sessions with three bundled recipes) and the Claude Sonnet 5.5 model addition (October 2, 1M context, 1.3x multiplier, paid tiers, us-east-1 and eu-central-1); prices unchanged.
- 2026-10-07 - Added the kirodotdev/Kiro star history chart to the Status section.
- 2026-10-08 - Recorded CLI 2.28.0 (October 5, interactive Classic-to-3.0 switching, category-based V3 hook matching, steadier long V3 sessions) as the new latest CLI release; prices unchanged.
- 2026-10-10 - Recorded CLI 2.29.0 (October 9, Memory across chat sessions for local V3 sessions with read-write, read-only, and off controls) and the IDE 1.2.56 patch (October 8, Workflows feedback link, chat, terminal, and source-control fixes) as the new latest releases; prices re-verified unchanged.
- 2026-10-13 - Recorded CLI 2.30.0 (October 12, the gradual V3-switch startup prompt and V3 model-fallback notices, ahead of CLI 3.0 becoming the default harness at the end of October) as the new latest CLI release, the 2.29.1 patch (October 10), and the Claude Sonnet 5.5 and Opus 5.5 additions to AWS GovCloud (US) regions (October 9); prices re-verified unchanged.
- 2026-10-16 - Recorded CLI 2.31.0 (October 13, the local command sandbox and local autonomous mode for V3, on-demand MCP loading) and 2.31.1 (October 14, Mermaid diagrams in chat), IDE 1.3.0 (October 13, sandbox, Workflows from chat, live tab status) and 1.3.11 (October 15, Markdown Review), the FedRAMP Class C scope addition (October 12), Claude Sonnet 4's end of life (October 14), and the Kimi K3 experimental model addition (October 15, 2.4x multiplier, 1M context); prices re-verified unchanged.
- 2026-10-18 - Recorded the October 12 Kiro Web update the release chain had skipped (per-model fallback choice, workflow-step model pickers, session-reopen previews); the changelog shows nothing newer than October 15, and prices stand unchanged.
- 2026-10-23 - Rotation re-verification (kiro.dev, changelog, pricing, repository, and both HN threads re-fetched live): recorded CLI 2.32.0 (October 15), Crew 0.9.0 (October 16), IDE 1.4.0 (October 19, Memory in the IDE) and 1.4.10 (October 20, Memory defaulting to off), CLI 2.33.0 (October 20, workspace trust) and 2.33.1 (October 21), and re-verified prices unchanged.
- 2026-11-04 - Rotation re-verification, all cited URLs re-fetched live: recorded CLI 3.0.0 (November 3, V3 by default with Classic, the desktop app, and inline autocomplete retired, delivering the promised end-of-October switch), CLI 2.34.0 through 2.37.0 (October 23 to 30, MCP elicitation, the elevated-privilege warning, Approve for me, and automatic V2 agent upgrades with ACP terminal sign-in), IDE 1.4.51 and 1.4.62, the Web recaps-and-Schedule release (October 28), the Claude Haiku 5.5 experimental addition (October 23), and the October 30 general availability of Claude Opus 5.5 and GPT-5.6 Sol; prices re-verified unchanged.
- 2026-11-06 - Volatile re-verification on the pushed signal (the default branch's November 5 commits are Dependabot merges), recorded the November 4 changelog entries: Claude Haiku 5.5 and Kimi K3 reaching general availability (the Excluded Models indemnity exception lifted for Haiku 5.5, remaining on Kimi K3) and enterprise credit pooling at $20 per seat per month for 500 pooled credits, the only option for new Kiro profiles (Price history row); individual tier prices unchanged.
- 2026-11-14 - Rotation re-verification, all cited URLs re-fetched live: recorded the November 10 to 12 changelog wave (Kiro Mobile for Android, IDE 1.4.178 and 1.4.154, CLI 3.3.0, 3.2.1, and 3.2.0, the Grok 4.7 experimental model, Enterprise Management preview with Kiro Crew LTS, CloudTrail audit logging, and credit pooling with Okta and Entra ID); tier prices and the credit-pooling terms re-verified unchanged; the repository stands pushed November 5 and both HN threads live.

## See also

- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the surface layer this note belongs to
- [Send Implementation, Not Issue](../../../send-implementation-not-issue/index.md) - why generated specs plus implementation beats bare tickets
- [OpenCode](../../harnesses/opencode/index.md) - the open harness alternative, also ACP-reachable

## References

- https://kiro.dev/ - product surfaces, modes, hooks
- https://kiro.dev/pricing/ - tiers, credits, model multipliers, enterprise and GovCloud terms, as of 2026-11-04 (unchanged from the 2026-09-24 baseline); re-verified 2026-11-06 with tier prices unchanged and credit pooling now surfaced on the page (teams of 2 or more, $20 per seat per month, 500 included credits per seat, $0.04 per additional credit, no free tier in Enterprise or GovCloud); re-verified again 2026-11-14 with the ladder unchanged
- https://kiro.dev/changelog/ - the weekly release cadence, CLI 2.21.0 and Web GA and ISO certification on September 1, 2026, Crew 0.6.0 on September 5, IDE 1.1 with the GPT-5.6 1M-context upgrade on September 14, CLI 2.22.0 with the Claude Fable 5.1 Enterprise Preview on September 16, CLI 2.23.0 on September 21, the Web reasoning-effort update on September 22, CLI 2.23.1 and 2.24.0 on September 23, IDE 1.1.70 and Crew 0.7.0 on September 24, Crew patches 0.7.1 and 0.7.2 plus CLI 2.25.0 and the Claude Opus 5.5 model addition on September 28, IDE 1.2.4, CLI 2.26.0, and Web Workflows on September 30, CLI 2.27.0 on October 1, the Claude Sonnet 5.5 model addition on October 2, the CLI 2.27.1 and IDE 1.2.37 patches on October 2 and 5, CLI 2.28.0 on October 5, the IDE 1.2.56 patch on October 8, CLI 2.29.0 (Memory across chat sessions) on October 9, the CLI 2.29.1 patch on October 10, the Claude Sonnet 5.5 and Opus 5.5 AWS GovCloud (US) additions on October 9, CLI 2.30.0 (the gradual V3-switch startup prompt and model-fallback notices) on October 12, the FedRAMP Class C scope addition and the Web model-fallback and workflow-step-model update on October 12, IDE 1.3.0 and CLI 2.31.0 (the local command sandbox and autonomous mode) on October 13, Claude Sonnet 4's end of life and CLI 2.31.1 (Mermaid in chat) on October 14, and IDE 1.3.11 (Markdown Review) plus the Kimi K3 experimental model addition on October 15, CLI 2.32.0 (folder write approvals, non-interactive cloud sessions) on October 15, Crew 0.9.0 (crewmate profiles, dynamic dashboards, remote crews as live windows) on October 16, IDE 1.4.0 (Memory in the IDE) on October 19, CLI 2.33.0 (workspace trust) and IDE 1.4.10 (Memory default off) on October 20, and CLI 2.33.1 on October 21, then CLI 2.34.0 (MCP elicitation, workflow controls, memory deletion) on October 23 with the Claude Haiku 5.5 experimental addition the same day, CLI 2.35.0 (elevated-privilege warning, organization controls) on October 27, IDE 1.4.51 and 1.4.62 on October 27 and 28, the Web session-recaps and Schedule release on October 28, CLI 2.36.0 (Approve for me) on October 29, CLI 2.37.0 (automatic V2 agent upgrades, ACP terminal sign-in) on October 30 with the Claude Opus 5.5 and GPT-5.6 Sol general-availability announcement the same day, and CLI 3.0.0 (V3 by default, Classic and desktop app retired) on November 3, then the November 4 entries (Claude Haiku 5.5 and Kimi K3 generally available, and enterprise credit pooling at $20 per seat per month for 500 pooled credits), then the November 10 to 12 entries (credit pooling with Okta and Microsoft Entra ID, CLI 3.2.0, IDE 1.4.154, the Grok 4.7 experimental model, Enterprise Management preview with Kiro Crew LTS, CLI 3.2.1, and the CloudTrail audit logging, Kiro Mobile for Android, IDE 1.4.178, and CLI 3.3.0 wave), as of 2026-11-14
- https://github.com/kirodotdev/Kiro - issue tracker, no feature commits since June 22, 2026, the default branch's latest commits Dependabot dependency merges (November 5, 2026, re-verified 2026-11-06, re-fetched 2026-11-14 with the push date unchanged), about 4.4k stars as of 2026-10-16
- https://news.ycombinator.com/item?id=45044061 - the prompt-injection code execution writeup
- https://news.ycombinator.com/item?id=44654560 - the spec-workflow port that shows Kiro's influence
