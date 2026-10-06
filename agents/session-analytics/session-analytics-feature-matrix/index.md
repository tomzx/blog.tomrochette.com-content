---
title: "Session Analytics Feature Matrix"
created: 2026-08-30
updated: 2026-10-05
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3-flash, llm=deepseek-v4.1-flash, comparison, session-analytics, observability, token-usage]
readability: 3
audience_notes: >
  Engineers choosing how to observe and audit their coding-agent sessions across tools.
  Assumes you know what a session transcript and token accounting are; each column links to a full note with sources.
---

This matrix compares the nine members of the Session analytics category: tools that turn what your coding agents record (or are recording right now) into live views, searchable history, cost reports, and audits, plus one that borrows the same agent-readable interface for product analytics.
The category now spans three arrangements: the local retrospective archive and report tools (agentsview, ctx, Memex, AgentTrace, ccusage, CodeBurn), the live view (agents-observe, ClawTrace, and the real-time half of Agent Analytics), and the edge case, Agent Analytics, which measures your product's users rather than your agents.

**The category's founding question, retrospective archive versus live observation, now has both answers several times over: agentsview indexes what every agent already did and cost across 60-plus formats, ctx answers where did this line of code come from, AgentTrace answers what did this run cost and why was it slow, ccusage prints what every agent cost by day, week, month, and session, CodeBurn cuts the same dollars by task and branch and proposes what to stop paying for, agents-observe answers what is my agent doing right now (Claude Code and Codex only), ClawTrace answers the same question for OpenClaw by uploading the run, Memex answers where did I already do this and drops you back into the session, and Agent Analytics answers a different question entirely, how are my product's users behaving, with the same agent-readable stance.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified.
Each column links to the full research note; every cell traces to a source cited there or in the references.

## The matrix

| Feature | [Agent Analytics](../agent-analytics/index.md) | [agents-observe](../agents-observe/index.md) | [agentsview](../agentsview/index.md) | [AgentTrace](../agenttrace/index.md) | [ccusage](../ccusage/index.md) | [ClawTrace](../clawtrace/index.md) | [CodeBurn](../codeburn/index.md) | [ctx](../ctx/index.md) | [Memex](../memex/index.md) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kind | agent-readable web product analytics, tracker.js events served to agents through CLI, MCP, and API | real-time observability dashboard for live and replayed sessions | local session indexer, web UI + CLI + desktop | local-first TUI/CLI audit of coding-agent session history (cost, tokens, latency, failures, health) | local cost-report CLI over the session files coding agents already wrote | hosted trace and cost-attribution platform for OpenClaw runs, with an AI analyst | local spend-analysis desktop app plus CLI with task and branch attribution, plan quota, and spend guards | local session search CLI with built-in blame attribution | local session search CLI and TUI with resume-in-place and an MCP server |
| Deployment | self-hosted OSS server (Cloudflare Workers + D1, Docker/Kubernetes + SQLite, plain Node) or hosted cloud at app.agentanalytics.sh | Claude Code plugin, hooks feeding a Dockerized local API server, dashboard on localhost:4981 | local daemon, Docker, optional PostgreSQL push for teams | single Rust binary, TUI plus CLI reports, Homebrew/npm/curl/cargo installs (winget dropped in v0.10.0) | zero-install CLI (npx/bunx, or npm global) with JSON config; no daemon, no server | OpenClaw plugin streaming to a hosted cloud pipeline (Azure Blob, Databricks, PuppyGraph, Vercel UI), no documented self-host path | CLI (npx, npm, brew) plus a signed desktop app (macOS, Windows Store, Linux deb/rpm/AppImage) with menu bar, tray, and GNOME plugins; no daemon | single-binary CLI install, agent-callable skill | single-binary CLI install (brew, AUR, Nix, cargo-binstall), TUI, local web UI, native desktop apps, MCP server |
| Open source | ~ README claims MIT, no LICENSE file on the default branch as of 2026-09-27, sibling repos are MIT | ✓ MIT | ✓ MIT | ✓ MIT | ✓ MIT (license file at apps/ccusage/LICENSE in the monorepo) | ~ Apache-2.0 repository, hosted cloud is the product and no self-host path is documented | ✓ MIT | ✓ Apache-2.0, blame included since 2.0 | ✓ MIT |
| Agents covered | any agent that can run commands or call HTTP, with documented installs for Claude Code, Codex, Cursor, OpenClaw, Paperclip, Hermes, Instinct, and OpenWork | ~ Claude Code and Codex, with the plugin install Claude Code-native | 60+ formats auto-discovered (Claude Code, Codex, Gemini CLI, Copilot, Cursor, Zed, OpenCode, and more) | ~ about 15 named formats plus generic JSON/JSONL (Claude Code, Codex, Gemini CLI, Qwen Code, OpenCode, OpenClaw, Cursor exports, and more) | 18 named sources in the unified report (Claude Code, Codex, OpenCode, Amp, Droid, Codebuff, Hermes Agent, pi, Goose, OpenClaw, Kilo, Kimi, Qwen, Copilot CLI, Gemini CLI, Antigravity, Grok Build CLI, ZCode) | ~ OpenClaw only, through its eight-hook plugin | ~ 41 integrations claimed (Claude Code, Codex, Cursor, Gemini, and more); Cursor coverage reads the IDE database only, so Cursor Agent CLI transcripts are missed | ~ about 40 agent harnesses documented (Claude Code, Codex, Cursor, Pi, OpenCode, and more) | ~ 17 engines graded per capability (Claude Code, Codex, Cursor, OpenCode, Pi, GitHub Copilot CLI, Grok, Hermes, KiloCode CLI, and more), support uneven |
| Token cost reporting | ✗ product events, not agent token cost | ✓ per-session token usage and cost breakdowns (since v0.9.7) | ✓ per-model pricing catalog, seconds over months of sessions | ✓ per-session tokens and estimated USD cost across sources, with pricing overrides and confidence levels | ✓ daily, weekly, monthly, and session reports plus Claude 5-hour blocks and a beta statusline, with per-model breakdowns; pricing-catalog estimates | ✓ per-step tokens and USD cost, 80+ models with cache-aware pricing | ✓ by tool, model, project, git branch, and task, with plan-quota tracking; API-equivalent estimates | ✗ | ~ per-engine token usage, off by default |
| Search | ~ flexible analytics queries (metrics, group_by, filters), funnels, paths, retention, not transcript search | ✓ filtering and search across live and stored events | ✓ FTS5 full text, semantic search opt-in | ✓ sort and filter sessions by cost, duration, health, failures, anomalies, model, source, or text | ✗ report tables and JSON output, no transcript search | ~ trace tree, call graph, timeline browse, and natural-language Ask Tracy queries over the trace graph, not transcript search | ~ sessions drill down to turns and periods compare side by side, no full-text search | ✓ cross-agent message and tool-call search, subagent and fork aware | ✓ BM25 default, opt-in local or remote (OpenAI-compatible) embeddings for semantic and hybrid queries, saved memories searchable, SSH federation |
| Provenance | ✗ | ✗ | ✗ | ~ heuristic Git delivery correlation only, no line-level attribution | ✗ | ✗ | ~ spend matched to pull requests and git branches, not line-level attribution | ✓ blame maps a line, file, commit, or PR to the session that produced it | ✗ |
| Live observation | ✓ real-time terminal dashboard across projects, plus opt-in web session replay | ✓ hook events stream to the dashboard over websockets as agents run | ✗ retrospective only, parses files already written | ✗ retrospective only, reads logs already written | ~ live Claude 5-hour block monitoring and a beta statusline, not a session dashboard | ✓ runs stream to the hosted dashboard through the eight-hook plugin | ~ menu bar, tray, and Capacity Dock show current spend and what is running now, not agent actions | ✗ retrospective only | ✗ retrospective only |
| Team features | ~ multi-agent access and cross-project portfolios, no team roles or SSO documented | ✗ single-user local setup | ✓ PostgreSQL push, machine-labeled sync, S3 roots, versioned exports | ~ CI reports and shared baseline artifacts, no hosted team sync | ✗ | ~ multi-tenant accounts (Tenant to Agent to Trace to Span) with referrals, no team roles documented | ✗ | ~ beta history sharing through a self-hosted ctx server with collection permissions and revocable access since v2.2.0, no hosted team product | ✗ single-user, SSH federation to your own machines, object-storage sync announced |
| Privacy posture | self-host keeps events in your D1 or SQLite, hosted cloud stores them in the vendor database, replay is opt-in and PII-masked | local-first, events stay in a local SQLite store behind a local Docker server | local-first, one anonymous ping by default, disableable | local-first, prompt and result bodies are not stored in tool steps, history of derived metrics is opt-in | local reads only, no accounts; fetches the model-pricing catalog unless run with --offline | hosted, trace payloads including LLM inputs and outputs are uploaded to the vendor's data lake | local reads, no account; guard and optimize edit local config with backups, and the MCP server pseudonymizes project names | local-first, attribution refuses data not on the machine | local-first, no cloud service in the default path, embeddings local by default (the opt-in remote path sends transcript text to that API) |
| Pricing | free cloud tier (100k events/month, 2 projects), metered cloud at $1 per 10k events, self-host free | free, MIT, no paid tiers published | free, MIT, no accounts | free, MIT, no paid tiers published | free, MIT, sponsor-funded, no paid tier | consumption credits; 100 free, packages $10 to $400, storage 1.35 credits/MB/day | free, MIT, no paid tiers published | free, Apache-2.0, the former $20/month pro add-on withdrawn from the site | free, MIT, no paid tier published |

## Reading the matrix

**The live-observation row is the row this matrix existed to name, and it now has two hosted and local answers**: agents-observe streams hook events into its dashboard while the agents run, ClawTrace fills the same row for OpenClaw by uploading the run, and Agent Analytics offers a real-time terminal dashboard for its own product events, though the coding-agent cells still cover only Claude Code, Codex, and OpenClaw, so the remaining empty cells belong to the harnesses none of them hook.
The second row worth reading is provenance: ctx's blame attribution is the only cell in the category that answers "which session wrote this", which agentsview deliberately leaves to cost and history questions.

**Token cost reporting is the row that pays for the tool**: harness-native cost views reset and see only their own sessions, while a pre-indexed store answers multi-tool, multi-month questions in seconds.
An earlier version of the agentsview docs benchmarked its reports at 84 to 223 times faster than ad-hoc parsing (calling that an upper bound); the current docs have dropped that benchmark entirely, so the row should be read as "fast because pre-indexed", with no vendor number left to lean on.
The docs' token-usage page is back to documenting schema version 5 as of 2026-09-27, with no version 6 mention left anywhere on the docs site, so scripts consuming those reports should expect churn either way.
AgentTrace adds a cost cell the archive tools do not, with explicit estimate labeling and pricing overrides, while ClawTrace adds per-step cost inside a hosted trace, which is more granular than anything local but only for OpenClaw.
ccusage and CodeBurn make cost the whole product: ccusage is the zero-install incumbent the other tools benchmark against, CodeBurn adds task and branch cuts plus an optimize loop that proposes config fixes, and both print estimates computed from pricing catalogs rather than bills.

**Memex adds the closing move the other archive tools lack: resume-in-place, where finding a session and re-entering it are one action in the TUI, plus the category's only semantic search (BM25 by default, opt-in embeddings that run locally or, since 2026-10-03, against an OpenAI-compatible API that receives your transcript text, so the headline requires setup either way).**
Its 17-engine support table is graded per capability and unevenly at that (some engines have no resume at all, token counting is missing for at least one), and its launch footprint is as thin as ctx's was, so read the column as promising and unproven.

**The 2026-09-27 columns split the category's remaining questions**: AgentTrace is the local cost, latency, and failure auditor that adds slow-run diagnosis the archive tools skip, ClawTrace is the hosted answer that trades privacy for full LLM payloads and an AI analyst, and Agent Analytics tests where the category's boundary sits by serving product analytics to agents instead of session data.

**Breadth of coverage is agentsview's moat**: roughly 60 supported sources against CodeBurn's claimed 41, ctx's 40, ccusage's 18, AgentTrace's 15, Memex's 17, and the two harnesses agents-observe covers or the one ClawTrace hooks, which matters because most practitioners now run two or three harnesses at once.
Agent Analytics is agent-agnostic by design, since any agent that can call HTTP is a client.
ctx's moat is different: agent-facing retrieval, where the consumer of the search is your next session rather than you.

## Choosing from the matrix

- Running three or more different coding agents and wanting one private history and cost view: agentsview.
- Wanting your agents to recall why code exists, from the session that wrote it: ctx, with its self-reported numbers accepted.
- Living in the terminal and wanting semantic recall plus one action back into the session: Memex, accepting a few hundred stars and thin verification.
- Auditing what a run cost and why it was slow, locally and with CI gates: AgentTrace.
- Wanting the quickest terminal answer to what did my agents cost this week, without installing anything: ccusage.
- Wanting spend cut by task and branch, plan-quota tracking, and a guard that stops a runaway session: CodeBurn.
- Running OpenClaw and wanting full-payload traces plus an AI analyst, hosted: ClawTrace, accepting that the traces leave your machine.
- Instrumenting a product your agents are building and reading its traffic through an agent: Agent Analytics.
- Needing to see what an agent is doing right now: agents-observe for Claude Code or Codex, or ClawTrace if you run OpenClaw and can upload the run; otherwise a harness-native view is still the fallback.
- Single-agent users: your harness's built-in usage views are probably enough.

## Changes

- 2026-08-30 - Created as the Session analytics category's companion matrix, a single-column scaffold with the live-observation gap named in prose.
- 2026-09-05 - Extended from one to two columns with ctx.
- 2026-09-06 - Updated the ctx cell for its published pro pricing.
- 2026-09-08 - Dropped the agentsview benchmark claim from the prose after the tool's docs removed it entirely.
- 2026-09-13 - Added the agentsview usage-output schema version 6 churn note to the reading prose.
- 2026-09-16 - Extended to three columns with agents-observe, filling the live-observation gap the prose used to name.
- 2026-09-18 - ctx agents-covered cell updated after the docs began listing about 40 supported agent harnesses.
- 2026-09-20 - Extended from three to four columns with Memex, inserted last alphabetically, every row gaining a cell traced to the new note, with the reading and choosing prose extended.
- 2026-09-20 - Corrected the schema caution in the reading prose: the docs' usage JSON contract is at schema version 5, version 6 is the session-export schema.
- 2026-09-24 - Removed the verification preamble line on owner request.
- 2026-09-25 - Retired the ctx pro cells: the Kind, Open source, Team features, and Pricing cells now describe blame as built in, after v2.0.0 shipped it inside the single open-source executable and the site dropped every paid-tier listing.
- 2026-09-27 - Re-verified all four columns: repository counts refreshed (agents-observe 684, agentsview 6,001, ctx 1,135, Memex 231 stars), the reading prose's schema line revised after the agentsview docs returned to version 5, and the Memex star count in the choosing prose generalized; no table cells moved.
- 2026-09-27 - Extended from four to seven columns with Agent Analytics, AgentTrace, and ClawTrace, re-sorted all columns alphabetically, updated the intro member count and framing, and extended the reading and choosing prose.
- 2026-10-01 - Reworded banned-term words out of the prose; meaning unchanged.
- 2026-10-02 - Moved the ctx Team features cell after v2.2.0 shipped opt-in history backup plus beta sharing through a self-hosted ctx server; the other six columns re-verified unchanged.
- 2026-10-03 - Updated the Memex agents-covered cell and the prose engine counts to 17 engines after v0.25.0 (2026-10-02) added Hermes and KiloCode CLI; the other six columns re-verified unchanged.
- 2026-10-04 - Updated the Memex Search and Privacy posture cells and the reading prose after v0.26.0 (2026-10-03) added opt-in OpenAI-compatible remote embeddings alongside the local path; the other six columns re-verified unchanged.
- 2026-10-05 - Extended from seven to nine columns with ccusage (the zero-install cost-report incumbent, inserted in sorted position between AgentTrace and ClawTrace) and CodeBurn (the desktop spend-analysis app with task attribution and spend guards, between ClawTrace and ctx), every row gaining two cells traced to the new notes; the AgentTrace Deployment cell dropped winget after v0.10.0 removed it, the intro count and reading and choosing prose updated.

## See also

- [Executions Feature Matrix](../../executions/executions-feature-matrix/index.md) - the trigger-and-run layer whose runs these tools observe
- [Model Selection for Coding Tasks](../../model-selection-for-coding-tasks/index.md) - the per-token economics these reports feed
- [Context Management Patterns](../../context-management-patterns/index.md) - the context costs the token reports make visible

## References

- https://github.com/kenn-io/agentsview - the repository, supported agents, architecture, and license for the agentsview column
- https://www.agentsview.io/docs/token-usage/ - the cost computation, benchmark caveats, and undercount disclosures
- https://www.agentsview.io - the deployment surfaces and team features
- https://github.com/ctxrs/ctx - the ctx column: repository, license, and no-compaction positioning
- https://ctx.rs/pro - the ctx column: blame attribution and its citation model
- https://code.claude.com/docs/en/costs - the harness-native cost views that define the category's baseline
- https://github.com/simple10/agents-observe - the agents-observe column: repository, license, and adoption numbers
- https://raw.githubusercontent.com/simple10/agents-observe/main/README.md - the agents-observe column: plugin install, Docker server, websockets dashboard, and token and cost breakdowns
- https://news.ycombinator.com/item?id=47602986 - the agents-observe launch thread behind the live-observation claim's community context
- https://github.com/nicosuave/memex - the Memex column: repository, surfaces, engine support table, and license
- https://raw.githubusercontent.com/nicosuave/memex/main/README.md - the Memex column: BM25 and local-embedding search, resume-in-place, MCP server, and install paths
- https://github.com/luoyuctl/agenttrace - the agenttrace column: repository, MIT license, and coverage
- https://raw.githubusercontent.com/luoyuctl/agenttrace/master/README.md - the agenttrace column: source formats, governance reports, CI gates, and privacy posture
- https://github.com/epsilla-cloud/clawtrace - the ClawTrace column: repository, Apache-2.0 license, and adoption numbers
- https://raw.githubusercontent.com/epsilla-cloud/clawtrace/main/README.md - the ClawTrace column: eight hooks, cloud pipeline, per-step cost, and self-evolve skill
- https://www.clawtrace.ai/docs/billing/credits - the ClawTrace column: credit packages and consumption rates
- https://github.com/Agent-Analytics/agent-analytics - the Agent Analytics column: repository, self-host routes, and license status
- https://agentanalytics.sh/ - the Agent Analytics column: tracker, access surfaces, and cloud pricing tiers
- https://github.com/ccusage/ccusage - the ccusage column: repository, eighteen-source coverage, and license
- https://raw.githubusercontent.com/ccusage/ccusage/main/apps/ccusage/README.md - the ccusage column: report types, blocks and statusline features, offline mode, and pricing overrides
- https://api.npmjs.org/downloads/point/last-month/ccusage - the ccusage column: 544,542 trailing-month downloads (as of 2026-10-05)
- https://github.com/getagentseal/codeburn - the CodeBurn column: repository, surfaces, and the 41-integration claim
- https://raw.githubusercontent.com/getagentseal/codeburn/main/README.md - the CodeBurn column: spend cuts, optimize/quota/guard behavior, and desktop install matrix
- https://api.npmjs.org/downloads/point/last-month/codeburn - the CodeBurn column: 38,725 trailing-month downloads (as of 2026-10-05)
