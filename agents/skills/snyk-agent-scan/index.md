---
title: Snyk Agent Scan
created: 2026-10-20
updated: 2026-10-22
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, skills, security, supply-chain]
readability: 3
audience_notes: >
  Engineers who want to know what agent components are already installed on their machines
  and which of those carry prompt-injection or malware risk. Assumes familiarity with SKILL.md
  and MCP configurations.
---

Snyk Agent Scan is Apache-2.0 security tooling from Snyk that discovers every agent harness, MCP server, and skill installed on a machine and scans them for prompt injection, malicious code, credential handling, and data-handling risks, reporting scored risk indicators per component.

**Its difference from the per-artifact scanner beside it is direction: SkillSpector grades one skill before you install it, Agent Scan inventories everything already installed, which is the audit half of the supply-chain problem most teams skip.**

## What it is

A Python 3.10+ CLI (`uvx snyk-agent-scan`, or a GPG-signed standalone binary with SBOM and checksums; no npm package) that auto-discovers agent configurations across Claude Code and Claude Desktop, Cursor, VS Code, GitHub Copilot, Gemini CLI, Windsurf, OpenCode, Codex, Amp, Kiro, Antigravity, Amazon Q, and OpenClaw, at system, user, project, and extension scopes.
Analysis runs two ways: local checks, and Snyk's analysis API, to which skill contents, agent applications, tool names, and descriptions are shared under Snyk's Agent Scan terms.
Version 0.6 (August 2026) moved from issue-code output to scored risk indicators against a 2026-07-10 analysis API, and the 0.5.x line is planned for deprecation.
Snyk also ships it as the experimental `snyk agent-scan` command inside the main Snyk CLI (v1.1308.0), and an enterprise background mode (MDM-managed) reports results to the Snyk Evo platform.

## Status

Active and vendor-backed: 3,154 stars and 292 forks as of 2026-10-20 (293 forks as of 2026-10-22), 778 commits on a repository created 2025-04-07, latest release v0.6.9 (2026-10-20) with the default branch pushed 2026-10-21.
Skills scanning arrived with v0.4, published together with a technical report on the agent skill ecosystem: of 3,984 skills analyzed from the clawhub.ai hub, 13.4% carried at least one critical-level issue and 36.8% at least one other-severity issue, while 9% of the top legitimate skills.sh skills showed exploitable patterns such as insecure credential handling or third-party content processing.
Snyk Labs runs a companion Skill Inspector web experiment for scanning a single skill.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=snyk/agent-scan&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=snyk/agent-scan&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=snyk/agent-scan&type=date&legend=top-left" />
</picture>

The third-party footprint is thin against the vendor name: my searches found three Hacker News threads at 2, 7, and 2 points and no independent review, so the 3.1k stars are Snyk's distribution, not a community.

## Strengths

- **Discovery is the product: it inventories what is actually installed across every harness, scope, and operating system, which no per-artifact scanner does.**
- Detection targets the attack classes that actually hit the skill supply chain: prompt injection, malicious code, suspicious downloads, credential handling, secret detection, and untrusted content, with skills skippable via `--no-skills`.
- The release engineering is enterprise-grade: GPG-signed checksums, SBOMs per release, and a stated enterprise support channel.
- The vendor publishes its own research base rates (the skills report) instead of marketing only.

## Cautions

- **Analysis is hybrid cloud: skill contents, tool names, and descriptions leave your machine for Snyk's API, so the tool that guards your supply chain also asks you to trust Snyk with your skill inventory.**
- Scanning MCP configurations still executes what it audits, but the README now gates part of it: since at least the 2026-10-22 README, foreground interactive scans ask explicit consent (y/n) before contacting each discovered MCP server and background or push-key scans start no stdio servers without `--dangerously-run-mcp-servers`, yet those fleet scans still inspect remote MCP URLs automatically, and the README still says to run untrusted scans inside a sandbox.
- The CLI output contract is experimental and explicitly may change without notice, and the entire 0.5.x line is planned for deprecation, so scripts built on it churn.
- Their own report shows the detector tiers behave differently: critical-level detectors hit 0% false positives on the top 100 legitimate skills.sh skills, but high- and medium-level detectors fire on up to 9% of those same legitimate skills.
- The community footprint is one vendor's voice: no independent benchmark of its detection quality was found as of 2026-10-20.

## Pricing

Free and open source under Apache-2.0; the CLI requires a Snyk account token, and Snyk's Free plan is $0 per month.
Snyk Team starts at $25 per month.
The enterprise Evo platform (background fleet scanning, MDM mode) is not available on Free or Team and requires an enterprise platform subscription, as of 2026-10-20.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-20 | Free, Team, Evo | First recorded: CLI free with a Snyk account (Free $0 per month), Team from $25 per month, Evo enterprise-only | https://snyk.io/pricing/ |

## Compared to

- [SkillSpector](../skillspector/index.md): NVIDIA's pre-install scanner grades one artifact with a 0-100 score and a DO NOT INSTALL verdict, locally or on your own LLM tokens; Agent Scan inventories and audits everything already installed, with analysis shared with Snyk. Pre-install gate versus fleet audit.
- [skills.sh](../skills-sh/index.md): its audit columns aggregate Snyk results per listed skill after the fact; Agent Scan is the same vendor scanning your machine instead of a registry.
- [SkillMD](../skillmd/index.md): the registry that publishes scanner verdicts per indexed skill; neither registry sees what you actually installed, which is Agent Scan's vantage.

## Bottom line

**Recommended for anyone who has been installing skills and MCP servers for months without an inventory, especially on shared or enterprise machines where the installed set is unknown.**
Not as a pre-install gate for a single unfamiliar skill (that is SkillSpector's job), and not for machines whose skill inventory cannot leave the environment, because the analysis shares contents with Snyk's API.
My disagreeable claim: the audit direction is the more valuable half of this market, the pre-install scanners are arguing about a door while most machines are already full, and discovery-first tooling will matter more than one more verdict badge.

## Changes

- 2026-10-20 - Created from the skills entrant scan (the mapped awesome-list source), with the hybrid-cloud analysis and the execute-what-you-scan warning recorded as the critical angles.
- 2026-10-22 - v0.6.9 (published 2026-10-20) added VS Code extension MCP-server discovery (servers registered by installed extensions) alongside dependency upgrades; the Status release line moved to it.
- 2026-10-22 - The MCP-execution caution corrected against the current README: foreground interactive scans now ask consent before contacting each discovered server and background scans start no stdio servers without --dangerously-run-mcp-servers, while fleet scans still auto-inspect remote MCP URLs and the sandbox advice stands.

## See also

- [SkillSpector](../skillspector/index.md) - the per-artifact pre-install scanner this machine-wide auditor complements
- [skills.sh](../skills-sh/index.md) - the registry whose audit columns already carry Snyk verdicts
- [SkillMD](../skillmd/index.md) - the verification-first registry's published verdicts, the at-scale cousin of per-machine scans
- [Anthropic Agent Skills](../anthropic-agent-skills/index.md) - the vendor framing of skills as untrusted inputs that motivates scanning
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the map this audit layer sits under

## References

- https://github.com/snyk/agent-scan - repository, Apache-2.0, 3,154 stars and 292 forks as of 2026-10-20 (293 forks as of 2026-10-22), created 2025-04-07, pushed 2026-10-21 (GitHub API)
- https://raw.githubusercontent.com/snyk/agent-scan/main/README.md - discovery matrix (14 agents, four scopes including the extension/plugin scope VS Code gained in v0.6.9), the two modes, the MCP consent flow and sandbox warning, and the API-sharing disclosure (fetched 2026-10-22)
- https://pypi.org/pypi/snyk-agent-scan/json - snyk-agent-scan 0.6.9, Python 3.10+, Apache-2.0 (fetched 2026-10-22)
- https://api.github.com/repos/snyk/agent-scan/releases/latest - v0.6.9 published 2026-10-20 (VS Code extension MCP discovery, dependency upgrades), the newest release as of 2026-10-22
- https://raw.githubusercontent.com/snyk/agent-scan/main/.github/reports/skills-report.pdf - the skills-ecosystem threat report: 3,984 clawhub.ai skills, 13.4% with a critical issue, 36.8% with another-severity issues, the false-positive profile, and the clawhub/skills.sh comparison (fetched 2026-10-20)
- https://labs.snyk.io/experiments/skill-scan/ - the Snyk Labs Skill Inspector companion experiment (fetched 2026-10-20)
- https://docs.snyk.io/agent-security - the agent-security documentation home (fetched 2026-10-20)
- https://updates.snyk.io/announcing-snyk-cli-v1-1308-0/ - the experimental `snyk agent-scan` command in Snyk CLI v1.1308.0, moved to risk-indicator output (fetched 2026-10-20)
- https://snyk.io/pricing/ - Free $0, Team from $25 per month, Evo enterprise-only (fetched 2026-10-20)
- https://hn.algolia.com/api/v1/search?query=agent-scan%20snyk&tags=story - the thin-footprint scan: three threads at 2, 7, and 2 points (fetched 2026-10-20)
