---
title: Snyk Agent Scan
created: 2026-10-20
updated: 2026-11-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, llm=glm-5.4, skills, security, supply-chain]
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
Version 0.7.0 (2026-11-18) shipped the remote-discovery rollout: discovery can run off, shadow (backend-discovered components recorded with shadow-parity metadata but not scanned), or on, a coding-agent-discovery client feeds Snyk's backend the inventory, `discover_local_only` covers sources the backend cannot read, and a lost remote discovery session restarts from init, alongside optional machine-serial propagation from the guard hooks through scan metadata.
Snyk also ships it as the experimental `snyk agent-scan` command inside the main Snyk CLI (v1.1308.0), and an enterprise background mode (MDM-managed) reports results to the Snyk Evo platform.
The repo's README now documents a daily usage limit for free-tier SNYK_TOKEN users (a docs commit on 2026-11-16), worth knowing before scripted scans on the Free plan.

## Status

Active and vendor-backed: 3,154 stars and 292 forks as of 2026-10-20 (293 forks as of 2026-10-24, 298 as of 2026-11-17, 302 as of 2026-11-25), 802 commits on a repository created 2025-04-07, latest release v0.7.1 (2026-11-24, on PyPI the same day; its GitHub body is empty, the content reading from the 24 commits between the tags: the two 2026-11-18 commits recorded after v0.7.0's tag (the discovery-restart fix and scan-side machine-serial propagation), the 2026-11-19 Agent Guard install and uninstall fixes (guard config files written atomically, non-ASCII characters kept when rewriting agent config, no backup written on uninstall, Codex requirements.toml edited in place, the Guard-owned backup and the empty hooks directory removed on uninstall), a pydantic bump to >=2.14.2 for Snyk security vulnerabilities, and the 2026-11-23 discovery fixes (homes looked up once per shadow or on-mode scan, Windows profiles read from the registry, WSL keys and repeated clients compared like the backend, non-permission read errors reported as read_error, scanned home counts recorded in shadow metadata)), with the default branch's newest commit the 2026-11-23 release-prep merge and the repository's 2026-11-24 push landing off the default branch.
Skills scanning arrived with v0.4, published together with a technical report on the agent skill ecosystem: of 3,984 skills analyzed from the clawhub.ai hub, 13.4% carried at least one critical-level issue and 36.8% at least one other-severity issue, while 9% of the top legitimate skills.sh skills showed exploitable patterns such as insecure credential handling or third-party content processing.
Snyk Labs runs a companion Skill Inspector web experiment for scanning a single skill.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=snyk/agent-scan&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=snyk/agent-scan&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=snyk/agent-scan&type=date&legend=top-left" />
</picture>

The third-party footprint is thin against the vendor name: my searches found four Hacker News threads at 2, 7, 2, and 3 points (re-run 2026-11-25; the 2026-10-20 reading counted three and missed the 3-point Skill Inspector thread from 2026-09-12) and no independent review, so the 3.1k stars are Snyk's distribution, not a community.

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
The enterprise Evo platform (background fleet scanning, MDM mode) is not available on Free or Team and requires an enterprise platform subscription, figures as of 2026-10-20.
The pricing page was redesigned by 2026-11-07 and now leads with a credit-based enterprise platform (1 credit = $1, a per-capability rate card including Evo AI-SPM at 0.66 credits per active contributor per day) with the small-team flat rates behind a client-side pane, so the Free and Team figures above are no longer verifiable in a static fetch; as of 2026-11-25 the static fetch serves the page title "Try for Free or from $25/month" in its metadata, which corroborates the Team floor without restoring the pane.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-20 | Free, Team, Evo | First recorded: CLI free with a Snyk account (Free $0 per month), Team from $25 per month, Evo enterprise-only | https://snyk.io/pricing/ |
| 2026-11-07 | Enterprise/Evo | Pricing page redesigned to a credit-based platform model (1 credit = $1; Evo AI-SPM 0.66 credits per active contributor per day); the Free and Team flat-rate figures no longer render in a static fetch | https://snyk.io/pricing/ |

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
- 2026-10-24 - Volatile refresh: post-release pushes moved the default branch to 2026-10-22 (managed-mode hooks installation fixes and a certifi bump); v0.6.9 still the newest release.
- 2026-10-26 - Fixed the star-history chart markup carried since creation: the light-theme source had held the dark theme parameter, so the light fallback now requests the unthemed chart like every other note in the category.
- 2026-10-31 - The release train moved to v0.6.10 (published 2026-10-30, on PyPI the same day), which formalizes the managed-mode hooks fixes (skipping non-installed agents in managed mode) and the certifi vulnerability bump that had landed as post-v0.6.9 pushes; the Status release line moved to it.
- 2026-11-07 - The release train moved to v0.6.11 (published 2026-11-06, on PyPI the same day, with an empty GitHub body and the content read from the surrounding commits: Antigravity current-skill-path discovery, standalone-binary platform docs, hook-script version stamping at release time, and no-op agentic-fix parameter removal); the default branch pushed 2026-11-06, and Snyk's pricing page redesign moved the pricing section and price history to the credit-based enterprise model (figures no longer verifiable in a static fetch).
- 2026-11-12 - Volatile refresh: the default branch pushed 2026-11-09 (guard e2e install coverage for Copilot and guard-uninstall tests for all clients); v0.6.11 still the newest release.
- 2026-11-14 - Volatile refresh: the default branch pushed 2026-11-13 (retry hooks on transient errors, a certificate-error fix); v0.6.11 still the newest release.
- 2026-11-17 - Volatile refresh: the default branch pushed 2026-11-16 with a docs commit noting the daily usage limit for free-tier SNYK_TOKEN users (PR #541), the fact recorded in the What-it-is section; v0.6.11 still the newest release.
- 2026-11-19 - The release train moved to v0.7.0 (published 2026-11-18, on PyPI the same day, with an empty GitHub body and the content read from the surrounding commits: the remote-discovery rollout with off/shadow/on modes and shadow-parity metadata, backend-driven discovery through a coding-agent-discovery client, discover_local_only, a typed config model, transient-failure retries, and machine-serial propagation); the default branch pushed 2026-11-19 (scan-side machine-serial propagation, the discovery-restart fix), and the What-it-is section gained the 0.7 line.
- 2026-11-25 - The release train moved to v0.7.1 (published 2026-11-24, on PyPI the same day, with an empty GitHub body and the content read from the 24 commits between the tags: the Agent Guard install and uninstall fixes of 2026-11-19, a pydantic bump to >=2.14.2, and the 2026-11-23 discovery fixes, homes looked up once per scan, Windows profiles read from the registry, WSL keys and repeated clients compared like the backend, non-permission read errors as read_error, scanned home counts in shadow metadata); the default branch's newest commit is the 2026-11-23 release-prep merge, with the repository's 2026-11-24 push landing off the default branch; rotation re-verification with every cited URL re-fetched live, which corrected the HN footprint from three threads to four (2, 7, 2, and 3 points) and recorded the pricing page's static metadata now reading "Try for Free or from $25/month".

## See also

- [SkillSpector](../skillspector/index.md) - the per-artifact pre-install scanner this machine-wide auditor complements
- [skills.sh](../skills-sh/index.md) - the registry whose audit columns already carry Snyk verdicts
- [SkillMD](../skillmd/index.md) - the verification-first registry's published verdicts, the at-scale cousin of per-machine scans
- [Anthropic Agent Skills](../anthropic-agent-skills/index.md) - the vendor framing of skills as untrusted inputs that motivates scanning
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the map this audit layer sits under

## References

- https://github.com/snyk/agent-scan - repository, Apache-2.0, 3,154 stars and 292 forks as of 2026-10-20 (293 forks as of 2026-10-24), created 2025-04-07, default branch's newest commit 2026-11-23 with the repository pushed 2026-11-24 off the default branch (GitHub API, as of 2026-11-25)
- https://raw.githubusercontent.com/snyk/agent-scan/main/README.md - discovery matrix (14 agents, four scopes including the extension/plugin scope VS Code gained in v0.6.9), the two modes, the MCP consent flow and sandbox warning, and the API-sharing disclosure (fetched 2026-10-22; re-fetched 2026-11-25)
- https://pypi.org/pypi/snyk-agent-scan/json - snyk-agent-scan 0.7.1, Python 3.10+, Apache-2.0 (fetched 2026-11-25; 0.7.0 read there 2026-11-19)
- https://api.github.com/repos/snyk/agent-scan/releases/latest - v0.7.1 published 2026-11-24 (empty body; the compare endpoint's 24 commits between v0.7.0 and v0.7.1 name the Agent Guard install and uninstall fixes, a pydantic bump to >=2.14.2, and the discovery fixes: homes looked up once per scan, Windows profiles read from the registry, WSL keys and repeated clients compared like the backend, non-permission read errors as read_error, scanned home counts in shadow metadata), the newest release as of 2026-11-25 (fetched 2026-11-25; v0.7.0 read there 2026-11-19)
- https://raw.githubusercontent.com/snyk/agent-scan/main/.github/reports/skills-report.pdf - the skills-ecosystem threat report: 3,984 clawhub.ai skills, 13.4% with a critical issue, 36.8% with another-severity issues, the false-positive profile, and the clawhub/skills.sh comparison (fetched 2026-10-20; re-fetched 2026-11-25)
- https://labs.snyk.io/experiments/skill-scan/ - the Snyk Labs Skill Inspector companion experiment (fetched 2026-10-20; re-fetched 2026-11-25)
- https://docs.snyk.io/agent-security - the agent-security documentation home (fetched 2026-10-20; re-fetched 2026-11-25)
- https://updates.snyk.io/announcing-snyk-cli-v1-1308-0/ - the experimental `snyk agent-scan` command in Snyk CLI v1.1308.0, moved to risk-indicator output (fetched 2026-10-20; re-fetched 2026-11-25)
- https://snyk.io/pricing/ - the pricing page: Free $0, Team from $25 per month, Evo enterprise-only as of 2026-10-20; redesigned by 2026-11-07 to the credit-based enterprise model (1 credit = $1, Evo AI-SPM 0.66 credits per active contributor per day) with the flat-rate pane behind client-side rendering (re-fetched 2026-11-07); the page title "Try for Free or from $25/month" served in the static metadata (re-fetched 2026-11-25)
- https://hn.algolia.com/api/v1/search?query=agent-scan%20snyk&tags=story - the thin-footprint scan: four threads at 2, 7, 2, and 3 points (fetched 2026-10-20, when three were counted; re-fetched 2026-11-25)
