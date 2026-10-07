---
title: AgentTrace
created: 2026-09-27
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=deepseek-v4.1-flash, llm=glm-5.3-flash, session-analytics, cost-tracking, cli, tui, open-source]
readability: 3
audience_notes: >
  Engineers running several coding agents who want a local, terminal-first audit of session cost, latency, failures, and health.
  Assumes you know where harnesses store session logs and what token accounting is.
---

AgentTrace is an MIT-licensed local-first Rust TUI and CLI that reads the session logs your coding agents already wrote and reports their cost, tokens, latency, failures, and health.

**AgentTrace's bet is the narrow one this category keeps proving out: the useful telemetry is already on disk, and the product is a fast local query over it, with governance reports and CI gates bolted on top.**

## What it is

One Rust binary gives both interfaces: run `agenttrace` with no action to open the TUI, or pass flags such as `--overview`, `--audit`, `--recommend`, `--mcp-governance`, `--context-trends`, and `--delivery-evidence` for CLI and JSON output.
It parses about 13 named coding-agent formats (Claude Code, Codex CLI, Qwen Code, Cline, Aider, Cursor exports, Hermes Agent, OpenCode, OpenClaw, Pi, Oh My Pi, Kimi CLI, Copilot-style logs) plus generic JSON and JSONL traces; v0.10.1 removed Gemini CLI (discontinued upstream), and Antigravity sessions under `~/.gemini/antigravity-cli` are still read.
Install paths are Homebrew, npm, curl, and cargo; v0.10.0 dropped winget, added checksum-verified installers, and added an `agenttrace update` self-updater.
Everything runs locally: no hosted backend is required, and tool steps keep metadata and duration without storing prompt, response, result, or tool-argument bodies.
Reports render as JSON, Markdown, or self-contained HTML, and `--overview` can gate a CI job on session health, critical sessions, and tool-failure rate.
Made by an independent developer (luoyuctl) under MIT.

## Status

Young and active: 139 stars, 9 forks, 5 open issues, created 2026-05-01, last pushed 2026-10-06, latest release v0.10.1 on 2026-10-05 after v0.10.0 and v0.9.1 on 2026-10-04, as of 2026-10-06.

<a href="https://www.star-history.com/?repos=luoyuctl%2Fagenttrace&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=luoyuctl/agenttrace&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=luoyuctl/agenttrace&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=luoyuctl/agenttrace&type=date&legend=top-left" />
 </picture>
</a>

It is effectively a one-person project: the v0.9.0 and v0.10.0 changelists credit every feature pull request to the owner, with the one outside contributor's commit merged in v0.9.0.
The community footprint is nearly empty: a Hacker News search for the author returns nothing, and I found no Reddit discussion.
v0.9.1 and v0.10.0 (both 2026-10-04) rebuilt the session cache (schema v24, so the first launch after upgrading re-parses history), fixed Claude Code transcripts being misclassified as Qwen Code, attributed Claude Code subagent cost and tokens to the parent session, added --daily/--weekly/--monthly reports with a --timezone flag and 5-hour --blocks, and shipped the self-updater.
v0.10.1 (2026-10-05) corrected token accounting across agents (Claude Code and Codex totals move down, WorkBuddy up), rebuilt the cache again at schema v26, and removed Gemini CLI support because Gemini CLI was discontinued upstream.
**A pre-1.0 single-maintainer tool with serious packaging but no independent verification, so read its roadmap and issue tracker rather than its README for what actually ships.**

## Strengths

- Breadth of local parsing is unusually wide for its age: about 15 named harness formats plus generic JSON and JSONL behind one binary.
- Slow-run diagnosis is the differentiator: it surfaces long gaps, hanging sessions, retry loops, slow tool calls, large parameters, and context pressure, which the cost-first tools in this category do not.
- Governance reports are deliberate about evidence quality, labeling cost and delivery numbers as estimates or heuristics and reporting parse and pricing confidence instead of hiding gaps.
- CI integration is first class: `--overview` exits with code 2 on a failed health, critical-session, or tool-failure gate, and it can keep JSON on stdout while writing a Markdown or HTML artifact.
- Distribution punches above its size: Homebrew tap, npm, winget, curl, and cargo, with a documented parser contribution flow.

## Cautions

- Cost and delivery evidence is self-labeled as estimated: unknown models fall back to pricing, and the README says outright these are not provider billing or proof a commit reached main.
- Pre-1.0 with a fast-moving report schema, so scripts consuming the governance JSON should expect churn.
- One maintainer and no third-party benchmark or discussion, so reliability claims rest on the README, the CI workflow, and the maintainer's own tests.
- It reads logs, so coverage is only as complete as each harness writes, and unsupported formats degrade to `Limited` capability levels rather than a full trace.
- There is no live view and no provenance: it answers what a run cost and why it was slow after the fact, not what an agent is doing now or which session wrote a line.

## Pricing

Free and open source under MIT.
No paid tiers are published, and everything runs locally with no hosted service.

## Compared to

- [agentsview](../agentsview/index.md): the broader archive with more than 60 formats and a web and desktop UI; AgentTrace is narrower but terminal-first and adds latency and anomaly diagnosis plus CI gates, so choose AgentTrace for slow-run triage and agentsview for cross-harness history at scale.
- [agents-observe](../agents-observe/index.md): the live hook-fed dashboard for Claude Code and Codex; AgentTrace is retrospective, so they answer different moments.
- [ctx](../ctx/index.md): the search-and-blame CLI; AgentTrace does not do provenance, and ctx does not do cost or latency, so a cost-conscious engineer may run both.

## Bottom line

**Recommended for terminal-first engineers running several harnesses who want a local audit of session cost, latency, and failures with CI gates, and who value a private, no-backend setup.**
Not for live observation, transcript search, or line-level provenance.

## Changes

- 2026-09-27 - Created.
- 2026-10-02 - Recorded the v0.9.0 release (an Oh My Pi parser fix from the project's first outside contributor, static CRT linking on Windows, and a Codex cost double-counting fix) and refreshed repository counts.
- 2026-10-05 - Recorded v0.9.1 and v0.10.0 (2026-10-04): the schema-v24 cache rebuild, the Qwen-misclassification fix, subagent cost attribution to parent sessions, timezone-aware period reports and 5-hour blocks, and the self-updater with winget dropped; refreshed repository counts.
- 2026-10-06 - Recorded v0.10.1 (2026-10-05): cross-agent token-accounting corrections (lower Claude Code and Codex totals), the schema-v26 cache rebuild, and Gemini CLI support removed as discontinued upstream, with Antigravity sessions still read; the format count and the matrix's agents-covered cell updated, repository counts refreshed, and the ROADMAP reference repointed to docs/ROADMAP.md after the file moved from the repository root.
- 2026-10-07 - Added the luoyuctl/agenttrace star history chart to the Status section.

## See also

- [Session Analytics Feature Matrix](../session-analytics-feature-matrix/index.md) - the category comparison this note joins
- [agentsview](../agentsview/index.md) - the wider local archive for cross-harness history and cost
- [agents-observe](../agents-observe/index.md) - the live dashboard that answers the question AgentTrace answers only after the run
- [ctx](../ctx/index.md) - the provenance sibling that maps code back to the session that wrote it

## References

- https://github.com/luoyuctl/agenttrace - the repository, MIT license, description, and topics
- https://raw.githubusercontent.com/luoyuctl/agenttrace/master/README.md - the coverage list, governance flags, install paths, privacy posture, and report formats
- https://raw.githubusercontent.com/luoyuctl/agenttrace/master/docs/guides/ci-integration.md - the CI gate flags, exit code 2, and report artifacts
- https://raw.githubusercontent.com/luoyuctl/agenttrace/master/docs/ROADMAP.md - the local-first scope and explicit non-goals (moved from the repository root)
- https://api.github.com/repos/luoyuctl/agenttrace - stars, forks, dates, and license as of 2026-10-06
- https://api.github.com/repos/luoyuctl/agenttrace/releases - the v0.9.0 release date, v0.9.1 and v0.10.0 on 2026-10-04, and v0.10.1 on 2026-10-05
- https://registry.npmjs.org/@zack78/agenttrace - the npm package, latest 0.10.1
- https://hn.algolia.com/api/v1/search?query=luoyuctl - the empty Hacker News footprint behind the thin-community claim
