---
title: skills.sh
created: 2026-08-24
updated: 2026-09-12
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=x-preview-f-free, llm=glm-5.3-flash, skills, registries, vercel, agent-extensions]
readability: 3
audience_notes: >
  Engineers choosing where to discover and install SKILL.md packages across several agent harnesses.
  Assumes familiarity with the Agent Skills format and npm-style CLIs.
---

skills.sh is Vercel's directory and leaderboard for the open skills ecosystem: it ranks SKILL.md packages by install telemetry from its open-source CLI (`npx skills add <owner>/<repo>`), which installs into 79 agent harnesses as of 2026-09-12.
Facts below verified as of 2026-09-12.

**It won the registry slot not through curation but by wrapping git: any repository is already a package, the CLI symlinks it into every harness, and the resulting install counts became the ecosystem's ranking, with security review still catching up.**

## What it is

Launched 2026-01-20 by Vercel's labs team; the CLI is MIT-licensed with 31.5k stars, 2.7k forks, and 509 commits as of 2026-09-12.
The CLI resolves GitHub shorthand and URLs, GitLab, any git URL, local paths, and direct archive URLs (downloads capped at 10 MiB by default), then symlinks or copies skills into per-agent directories.
The site adds the leaderboard, per-agent and per-topic pages, badges, and packs (one install command bundling public and private skills).
**Ranking comes from anonymous CLI telemetry (opt-out via `DISABLE_TELEMETRY`), not from vetting or ratings.**

## Status

**Active and dominant among third-party registries.**
Top of the all-time leaderboard as of 2026-09-12: find-skills (vercel-labs) at 3.4M installs, grill-me (mattpocock/skills) at 1.1M, with the next three slots still held by mattpocock/skills entries (grill-with-docs, improve-codebase-architecture, and tdd, last read at 943.0K, 902.7K, and 874.6K on 2026-09-10), while frontend-design (anthropics/skills) now shows 880.2K in sixth and the newest top-ten entrant is agent-browser (vercel-labs/agent-browser) at 838.7K in seventh.
Official publisher entries include microsoft/azure-skills, supabase, prisma, and heygen-com/hyperframes.
The publisher mix has gone enterprise: open.feishu.cn (Lark) is the largest publisher at 14.8M aggregate installs across 22 skills, larksuite/cli entries add 6.1M across 14, and prime-skills/runcomfy-agent-skills holds 4.6M across 11, all as of 2026-09-09.
The nearest standalone competitor I had verified, skillregistry.io, listed 61 skills as of 2026-09-08, went dark by 2026-09-09, and is back online as of 2026-09-12 with 61 skills, 15,746 total downloads, and 18 contributors, still orders of magnitude behind skills.sh on installs.

## Strengths

- **One command, every harness: the per-agent path table means a single install reaches Claude Code, Codex, Cursor, OpenCode, Copilot, Gemini, and dozens more.**
- Zero publishing step: the registry indexes git itself, including `.claude-plugin` manifests, so there is no upload surface to go stale.
- Per-skill security columns aggregate Gen Agent Trust Hub, Socket, and Snyk results directly on the page.

## Cautions

- **Install counts measure fashion, not fitness: telemetry counts CLI runs, anyone can drive their own numbers, and the docs state plainly that the quality and security of listed skills are not guaranteed.**
- The audit page shows the gap: as of 2026-09-10 it listed 78 Pending and 24 Safe entries with no remediation history, and the microsoft/azure-skills azure-validate entry Snyk flagged Critical in early September still shows Snyk Critical as of 2026-09-12, alongside a Safe Gen rating and zero Socket alerts.
- Skills are instructions and scripts that agents execute, a risk Anthropic's engineering post calls out for skills generally, so a leaderboard install is a supply-chain decision.
- Telemetry is opt-out rather than opt-in, and one company controls the ranking surface of a nominally open ecosystem.

## Pricing

Free.
**The directory and CLI cost nothing, the CLI is MIT, and I found no paid placement or paid tier; skills carry their own licenses.**

## Compared to

- Vendor directories (Anthropic's partner directory, the ChatGPT/Codex plugin directory): curated and trusted, but single-ecosystem.
- skillregistry.io: a hosted upload registry pitched as "Dockerhub for Skill.md", 61 skills before it went dark on 2026-09-09 and back online by 2026-09-12, still far smaller than skills.sh on every count I could verify.
- Skilleton: lockfile-based, telemetry-free skill management that pins skills to commits, built explicitly as a critique of install-count culture.

## Bottom line

**Recommended as the discovery layer for cross-harness teams, provided you pin commits and read the SKILL.md before it touches a repo with production secrets.**
Not for air-gapped or compliance-bound environments, where an opt-out-telemetry installer needs review before it ever runs.
My disagreeable claim: marketplaces are the least interesting part of this ecosystem, the ten skills your team writes itself will beat the leaderboard's top ten, and I would not let an agent auto-install from it.

## See also

- [Agent Skills open standard](../agent-skills-open-standard/index.md) - the format this registry distributes
- [Anthropic Agent Skills](../anthropic-agent-skills/index.md) - the largest publisher on the leaderboard
- [OpenCode](../opencode/index.md) - one of the many harnesses the CLI installs into
- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - the distribution layer sitting over the harness map

## References

- https://vercel.com/blog/introducing-skills - launch announcement (2026-01-20)
- https://skills.sh/ - leaderboard, install counts, supported agents, as of 2026-09-12
- https://skills.sh/docs - ranking method (CLI telemetry) and the security disclaimer
- https://skills.sh/audits - Gen/Socket/Snyk audit columns, azure-validate still Snyk-Critical, as of 2026-09-12
- https://github.com/vercel-labs/skills - CLI source, agent path table, telemetry opt-out, 31.5k stars as of 2026-09-12
- https://skillregistry.io/ - nearest standalone competitor, back online as of 2026-09-12 with 61 skills and 15,746 total downloads
- https://github.com/Fcmam5/skilleton - lockfile-style, no-telemetry alternative
- https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills - the underlying untrusted-skill risk
