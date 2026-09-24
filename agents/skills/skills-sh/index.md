---
title: skills.sh
created: 2026-08-24
updated: 2026-09-22
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=x-preview-f-free, llm=glm-5.3-flash, skills, registries, vercel, agent-extensions]
readability: 3
audience_notes: >
  Engineers choosing where to discover and install SKILL.md packages across several agent harnesses.
  Assumes familiarity with the Agent Skills format and npm-style CLIs.
---

skills.sh is Vercel's directory and leaderboard for the open skills ecosystem: it ranks SKILL.md packages by install telemetry from its open-source CLI (`npx skills add <owner>/<repo>`), which installs into 79 agent harnesses as of 2026-09-22.
Facts below verified as of 2026-09-22.

**It won the registry slot not through curation but by wrapping git: any repository is already a package, the CLI symlinks it into every harness, and the resulting install counts became the ecosystem's ranking, with security review still catching up.**

## What it is

Launched 2026-01-20 by Vercel's labs team; the CLI is MIT-licensed with 32.3k stars, 2.7k forks, and 520 commits as of 2026-09-22.
The CLI resolves GitHub shorthand and URLs, GitLab, any git URL, local paths, and direct archive URLs (downloads capped at 10 MiB by default), then symlinks or copies skills into per-agent directories.
The site adds the leaderboard, per-agent and per-topic pages, badges, and packs (one install command bundling public and private skills).
**Ranking comes from anonymous CLI telemetry (opt-out via `DISABLE_TELEMETRY`), not from vetting or ratings.**

## Status

**Active and dominant among third-party registries.**
Top of the all-time leaderboard as of 2026-09-22: find-skills (vercel-labs) at 3.5M installs, grill-me (mattpocock/skills) at 1.2M, with the next three slots still held by mattpocock/skills entries (grill-with-docs, improve-codebase-architecture, and tdd), while frontend-design (anthropics/skills) shows 913.6K in sixth, agent-browser (vercel-labs/agent-browser) 911.6K in seventh, and setup-matt-pocock-skills (mattpocock/skills) rounds out the top eight at 878.1K.
Official publisher entries include microsoft/azure-skills, supabase, prisma, and heygen-com/hyperframes.
The publisher mix has gone enterprise: open.feishu.cn (Lark) is the largest publisher at 16.6M aggregate installs, larksuite/cli adds 5.8M, prime-skills/runcomfy-agent-skills and microsoft/azure-skills both sit in the millions, all as of 2026-09-22.
**Treat those publisher totals with suspicion: the page showed prime-skills with two different totals (4.2M and 2.9M) at the same moment, and azure-skills swung from 7.1M to 2.4M to 7.7M across the three days after the downward recompute first seen 2026-09-20, so the chips are view-scoped sums of whatever rows the leaderboard currently renders, not stable per-publisher aggregates.**
The nearest standalone competitor I had verified, skillregistry.io, listed 61 skills as of 2026-09-08, went dark by 2026-09-09, and is back online as of 2026-09-12 with 61 skills (still up as of 2026-09-22), 16,353 total downloads, and 18 contributors, still orders of magnitude behind skills.sh on installs.

## Strengths

- **One command, every harness: the per-agent path table means a single install reaches Claude Code, Codex, Cursor, OpenCode, Copilot, Gemini, and dozens more.**
- Zero publishing step: the registry indexes git itself, including `.claude-plugin` manifests, so there is no upload surface to go stale.
- Per-skill security columns aggregate Gen Agent Trust Hub, Socket, and Snyk results directly on the page.

## Cautions

- **Install counts measure fashion, not fitness: telemetry counts CLI runs, anyone can drive their own numbers, and the docs state plainly that the quality and security of listed skills are not guaranteed.**
- The audit page shows the gap: as of 2026-09-22 the open.feishu.cn fleet still sat Pending across all three scanners (26 of the first 50 rows), with no remediation history, a new Snyk-Critical entry appeared in the same window (genmedia-labs/skills' image-to-video, Safe on Gen and clean on Socket but Critical on Snyk at row 49), and azure-validate, Snyk-flagged Critical in early September and remediated to Pass by 2026-09-18, has since slipped below the audits page's 50-row window, its Pass status now visible only on its own skill page.
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

## Changes

- 2026-08-24 - Created in the Skills category seed.
- 2026-08-26 - Restored the mandatory Not-for-Y bottom-line clause.
- 2026-09-05 - Rewrote the audits caution after the Snyk-Critical azure-validate entry stopped appearing.
- 2026-09-06 - Added the enterprise publisher mix with aggregate install figures.
- 2026-09-07 - Updated the audits caution as azure-validate returned to the page marked Safe.
- 2026-09-16 - azure-validate's Snyk rating cleared from Critical to Low Risk; the audits caution was rewritten around the still-Pending open.feishu.cn fleet.
- 2026-09-18 - Refreshed leaderboard and publisher figures; azure-validate completed its remediation to Pass across all three scanners.
- 2026-09-20 - Refreshed the publisher mix after skills.sh recomputed cumulative install totals downward (open.feishu.cn 17.8M to 16.3M, larksuite/cli 11.3M to 5.3M, runcomfy 11.2M to 4.6M) and moved the azure-validate Pass status to its skill page after it slipped below the audits page's 50-row window.
- 2026-09-21 - The downward recompute extended to microsoft/azure-skills (7.1M to 2.4M aggregate installs), open.feishu.cn ticked back up to 16.4M, and the leaderboard and skillregistry.io figures were refreshed.
- 2026-09-22 - Refreshed the leaderboard (frontend-design 913.6K, agent-browser 911.6K, setup-matt-pocock-skills 878.1K), reinterpreted the publisher chips as view-scoped sums after azure-skills swung back to 7.7M and prime-skills showed two totals on one page, and flagged a new Snyk-Critical skill (genmedia-labs image-to-video) in the audits window while the feishu fleet stays Pending.

## See also

- [Agent Skills open standard](../agent-skills-open-standard/index.md) - the format this registry distributes
- [Anthropic Agent Skills](../anthropic-agent-skills/index.md) - the largest publisher on the leaderboard
- [OpenCode](../../harnesses/opencode/index.md) - one of the many harnesses the CLI installs into
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the distribution layer sitting over the harness map

## References

- https://vercel.com/blog/introducing-skills - launch announcement (2026-01-20)
- https://skills.sh/ - leaderboard, install counts, supported agents, as of 2026-09-22
- https://skills.sh/docs - ranking method (CLI telemetry) and the security disclaimer
- https://skills.sh/audits - Gen/Socket/Snyk audit columns, open.feishu.cn fleet still Pending in 26 of the first 50 rows and genmedia-labs image-to-video Snyk-Critical at row 49, as of 2026-09-22
- https://www.skills.sh/microsoft/azure-skills/azure-validate - azure-validate still Pass on all three scanners via its detail page, as of 2026-09-22
- https://github.com/vercel-labs/skills - CLI source, agent path table, telemetry opt-out, 32.3k stars as of 2026-09-22
- https://skillregistry.io/ - nearest standalone competitor, back online 2026-09-12 and still up with 61 skills and 16,353 downloads as of 2026-09-22
- https://github.com/Fcmam5/skilleton - lockfile-style, no-telemetry alternative
- https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills - the underlying untrusted-skill risk
