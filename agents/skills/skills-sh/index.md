---
title: skills.sh
created: 2026-08-24
updated: 2026-10-22
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=x-preview-f-free, llm=glm-5.3-flash, skills, registries, vercel, agent-extensions]
readability: 3
audience_notes: >
  Engineers choosing where to discover and install SKILL.md packages across several agent harnesses.
  Assumes familiarity with the Agent Skills format and npm-style CLIs.
---

skills.sh is Vercel's directory and leaderboard for the open skills ecosystem: it ranks SKILL.md packages by install telemetry from its open-source CLI (`npx skills add <owner>/<repo>`), which installs into 79 agent harnesses as of 2026-10-22.

**It won the registry slot not through curation but by wrapping git: any repository is already a package, the CLI symlinks it into every harness, and the resulting install counts became the ecosystem's ranking, with security review still catching up.**

## What it is

Launched 2026-01-20 by Vercel's labs team; the CLI is MIT-licensed with 34.5k stars as of 2026-10-13, 3,088 forks and 582 commits as of 2026-10-22.
The CLI resolves GitHub shorthand and URLs, GitLab, any git URL, local paths, and direct archive URLs (downloads capped at 10 MiB by default), then symlinks or copies skills into per-agent directories.
The site adds the leaderboard, per-agent and per-topic pages, badges, and packs (one install command bundling public and private skills).
**Ranking comes from anonymous CLI telemetry (opt-out via `DISABLE_TELEMETRY`), not from vetting or ratings.**

## Status

**Active and dominant among third-party registries.**
Top of the all-time leaderboard as of 2026-10-22: find-skills (vercel-labs) at 4.0M installs, grill-me (mattpocock/skills) at 1.4M, then agent-browser (vercel-labs/agent-browser), grill-with-docs, and hyperframes-cli (heygen-com/hyperframes) at 1.2M each in third through fifth, improve-codebase-architecture sixth at 1.2M, hyperframes (heygen-com/hyperframes) seventh at 1.1M, tdd (mattpocock/skills) eighth at 1.1M, media-use (heygen-com/hyperframes) ninth at 1.0M, and reddit-automation (flowkit-labs/skills) tenth at 1.0M.
The reorder since 2026-10-13 is the widest yet: three heygen-com/hyperframes entries (hyperframes, media-use) plus reddit-automation entered the top ten, pushing frontend-design (anthropics/skills) to thirteenth and handoff and setup-matt-pocock-skills (mattpocock/skills) to eleventh and twelfth, so one video-tooling publisher now holds four of the top fourteen rows.
Official publisher entries include microsoft/azure-skills, supabase, prisma, and heygen-com/hyperframes.
The publisher mix has gone enterprise: open.feishu.cn (Lark) is the largest publisher (chips reading 4.4M and 11.8M on one page), larksuite/cli and microsoft/azure-skills both sit in the millions (7.3M and 5.5M), and prime-skills/runcomfy-agent-skills adds several million more (4.4M), all as of 2026-10-02.
**Treat those publisher totals with suspicion: the page showed prime-skills with two different totals (4.2M and 2.9M) at the same moment, and azure-skills swung from 7.1M to 2.4M to 7.7M across the three days after the downward recompute first seen 2026-09-20, so the chips are view-scoped sums of whatever rows the leaderboard currently renders, not stable per-publisher aggregates.**
The pattern held again on 2026-10-04: the azure-skills chip read 8.7M, open.feishu.cn a single 16.3M total, and larksuite/cli 5.9M.
On 2026-10-05 the azure-skills chip read 8.0M, open.feishu.cn still a single 16.3M total, and larksuite/cli was back to two totals on one page (4.6M and 2.3M), as was runcomfy (2.1M and 3.3M).
On 2026-10-06 the azure-skills chip read 8.1M, open.feishu.cn still a single 16.3M total, larksuite/cli again showed two totals on one page (4.1M and 3.2M), and runcomfy two totals again (4.7M and 4.4M).
On 2026-10-08 the azure-skills chip read 7.6M, open.feishu.cn a single 16.4M total, and larksuite/cli and runcomfy one total each (6.9M and 4.7M), so the two-totals render is intermittent rather than stable.
On 2026-10-09 azure-skills held at 7.6M, open.feishu.cn read a single 16.5M total, and the single totals swung again (larksuite/cli 8.7M, runcomfy 3.3M).
On 2026-10-10 azure-skills read 7.7M, open.feishu.cn was back to two totals on one page (11.3M and 5.3M), larksuite/cli held a single 8.7M total, and runcomfy showed two again (4.3M and 4.4M).
On 2026-10-11 azure-skills read 7.1M, open.feishu.cn a single 14.4M total, and larksuite/cli a single 7.3M total, with runcomfy showing two totals again (1.7M and 2.6M).
On 2026-10-13 the leaderboard's collapsed publisher rows read azure-skills 7.2M, open.feishu.cn 16.8M, larksuite/cli 3.3M, with runcomfy showing two totals again (2.2M and 2.6M).
On 2026-10-22 azure-skills read 8.4M, open.feishu.cn a single 17.5M total, larksuite/cli two totals again (1.9M and 4.2M), and runcomfy multiple totals on one page (1.5M, 3.0M, and 3.9M).
The nearest standalone competitor I had verified, skillregistry.io, listed 61 skills as of 2026-09-08, went dark by 2026-09-09, came back online by 2026-09-12 (last measured at 61 skills and 17,768 total downloads on 2026-10-05, still up 2026-10-10), and went dark again as of 2026-10-22, its second outage, with 18 contributors when last reachable and still orders of magnitude behind skills.sh on installs.

## Strengths

- **One command, every harness: the per-agent path table means a single install reaches Claude Code, Codex, Cursor, OpenCode, Copilot, Gemini, and dozens more.**
- Zero publishing step: the registry indexes git itself, including `.claude-plugin` manifests, so there is no upload surface to go stale.
- Per-skill security columns aggregate Gen Agent Trust Hub, Socket, and Snyk results directly on the page.

## Cautions

- **Install counts measure fashion, not fitness: telemetry counts CLI runs, anyone can drive their own numbers, and the docs state plainly that the quality and security of listed skills are not guaranteed.**
- The audit page shows the gap: as of 2026-10-22 the open.feishu.cn fleet still sat Pending across all three scanners (20 of the first 50 rows, 31 through 50) with no remediation history; the window's active warnings are Snyk Med Risk on find-skills, the leaderboard's all-time number one, and on agent-browser (row 3), hyperframes-cli (row 5), hyperframes (row 7), and reddit-automation (row 10), Snyk High Risk on design-mobile-apps (designed-by-ai/skills, now row 18), Gen Med Risk and Snyk Med Risk on improve-codebase-architecture (row 6) and triage (row 15), and one Socket alert each on media-use (row 9, its first flag since the 2026-10-10 pair cleared) and the four 101-skills entries at rows 25 through 28; mattpocock's code-review, the Gen Med Risk and Snyk High Risk flag first seen 2026-10-04, stays outside the window entirely (leaderboard row 53, 778.2K installs); the Snyk-Critical entry from September (genmedia-labs/skills' image-to-video, Safe on Gen and clean on Socket but Critical on Snyk) stays out of the window, while azure-validate, Snyk-flagged Critical in early September and remediated to Pass by 2026-09-18, remains below the window, its Pass status visible only on its own skill page (re-verified there 2026-10-22).
- Skills are instructions and scripts that agents execute, a risk Anthropic's engineering post calls out for skills generally, so a leaderboard install is a supply-chain decision.
- **PromptArmor's published research (fetched 2026-10-07) makes the risk concrete: backdoored skills passed Anthropic's own scanner and exfiltrated files in production, and the same report calls skill marketplaces minimally scanned and ranked by gameable metrics like install counts.**
- Telemetry is opt-out rather than opt-in, and one company controls the ranking surface of a nominally open ecosystem.

## Pricing

Free.
**The directory and CLI cost nothing, the CLI is MIT, and I found no paid placement or paid tier; skills carry their own licenses.**

## Compared to

- Vendor directories (Anthropic's partner directory, the ChatGPT/Codex plugin directory): curated and trusted, but single-ecosystem.
- skillregistry.io: a hosted upload registry pitched as "Dockerhub for Skill.md", 61 skills, two outages (2026-09-09 and again by 2026-10-22), still far smaller than skills.sh on every count I could verify.
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
- 2026-09-25 - Refreshed the leaderboard (find-skills 3.6M; agent-browser 933.7K rose past frontend-design 919.9K), the publisher chips (open.feishu.cn 16.0M, azure-skills swinging again to 8.4M, larksuite/cli and runcomfy each showing two totals on one page), skillregistry.io (still up with 61 skills and 16,503 downloads), and the audits window (feishu fleet still Pending, the genmedia-labs image-to-video Snyk-Critical entry now at row 48).
- 2026-09-27 - Refreshed the leaderboard (agent-browser 952.5K, frontend-design 926.8K, setup-matt-pocock-skills 897.1K; find-skills and grill-me unchanged), the publisher chips (azure-skills swinging again to 8.5M, larksuite/cli and runcomfy still showing two totals each), and the audits window (feishu fleet still Pending in 25 of the first 50 rows, the genmedia-labs image-to-video Snyk-Critical entry at row 44).
- 2026-10-03 - Refreshed the leaderboard (frontend-design 948.5K, setup-matt-pocock-skills 930.4K; the top six unchanged), the publisher chips (azure-skills swinging again to 8.6M, open.feishu.cn down to a single 15.6M total), and the audits window (feishu fleet Pending in 26 of the first 50 rows, the genmedia-labs image-to-video Snyk-Critical entry dropped out of the 50-row window).
- 2026-10-04 - A new audit flag entered the window: mattpocock's code-review (660.8K installs) sits at Gen Med Risk and Snyk High Risk at row 48, the feishu fleet's Pending count moved to 25 of the first 50 rows, and the leaderboard and publisher chips were refreshed (frontend-design 951.0K, setup-matt-pocock-skills 933.7K, azure-skills 8.7M, open.feishu.cn 16.3M single total, larksuite/cli 5.9M).
- 2026-10-06 - The code-review audit flag slipped out of the audits page's 50-row window (leaderboard row 54, 670.6K installs) while the feishu fleet held at Pending in 25 of 50, the window's active warnings moved to Gen Med Risk on improve-codebase-architecture and triage plus Socket single-alerts on media-use and the 101-skills pair, azure-validate re-verified Pass on its own page, and the leaderboard and publisher chips were refreshed (frontend-design 954.4K, setup-matt-pocock-skills 941.1K, azure-skills 8.1M).
- 2026-10-07 - Added PromptArmor's backdoored-skill research as the published instance of the supply-chain caution (scanner passed, files exfiltrated, marketplaces called minimally scanned and gameably ranked); the CLI's agent-target count moved to 80 and the repo figures refreshed.
- 2026-10-08 - The CLI's agent-target count moved back to 79 and the README's headline and table now agree (four named agents plus "75 more"); the leaderboard, publisher chips, and audits window were refreshed (frontend-design 962.1K and setup-matt-pocock-skills 960.7K at seventh and eighth, azure-skills chip down to 7.6M, the feishu fleet Pending in 23 of the first 50 rows, media-use at two Socket alerts, the 101-skills ai-image entry out of the window).
- 2026-10-09 - Leaderboard refresh: find-skills crossed to 3.8M and the seventh/eighth pair swapped (setup-matt-pocock-skills 968.3K now ahead of frontend-design 966.0K); the feishu fleet moved to Pending in 24 of the audits window's first 50 rows with code-review still outside at row 55 (697.5K installs); the publisher chips swung again (open.feishu.cn 16.5M single total, larksuite/cli 8.7M single, runcomfy 3.3M single, azure-skills holding 7.6M); the CLI moved to 33.5k stars and 563 commits with the 79-agent README count re-verified.
- 2026-10-10 - The audits window gained two flags: Snyk Med Risk on find-skills, the all-time number one, and Snyk High Risk on design-mobile-apps (row 48), while the 101-skills ai-video Socket entry slipped out with code-review still outside at row 56 (704.2K installs) and the feishu fleet steady at Pending in 24 of 50; the leaderboard's seventh/eighth order held (setup-matt-pocock-skills 974.2K, frontend-design 969.7K), the publisher chips swung again (azure-skills 7.7M, open.feishu.cn back to two totals, 11.3M and 5.3M, runcomfy two totals, 4.3M and 4.4M), and the CLI moved to 33.6k stars and 570 commits with the 79-agent README count re-verified.
- 2026-10-11 - The leaderboard record gained a ninth-place line, handoff (mattpocock/skills) at 959.0K installs, while the seventh/eighth order held; the audits window moved to the feishu fleet Pending in 23 of 50, the two 101-skills Socket entries back inside at rows 49 and 50, design-mobile-apps up to row 47 still Snyk High Risk, and tenth-place hyperframes-cli carrying Snyk Med Risk beside clean ninth-place handoff; the publisher chips read azure-skills 7.1M, open.feishu.cn 14.4M, and larksuite/cli 7.3M single totals with runcomfy back to two; the CLI moved to 33.7k stars with the 79-agent README count re-verified.
- 2026-10-13 - The leaderboard reordered behind the top three: hyperframes-cli climbed from tenth to eighth (990.7K), pushing frontend-design to ninth (983.3K) and handoff to tenth (976.5K) with setup-matt-pocock-skills holding seventh at 995.0K; the audits window moved to the feishu fleet Pending in 22 of the first 50 rows with media-use's two Socket alerts cleared, agent-browser newly carrying Snyk Med Risk beside find-skills, design-mobile-apps at row 22, and code-review outside at row 56 (727.0K installs); the publisher chips read azure-skills 7.2M, open.feishu.cn 16.8M, larksuite/cli 3.3M, and runcomfy two totals; the CLI moved to 34.5k stars with the 79-agent README count re-verified.
- 2026-10-22 - The widest top-ten reorder yet: hyperframes, media-use (both heygen-com/hyperframes), and reddit-automation (flowkit-labs/skills) entered at seventh, ninth, and tenth, pushing frontend-design to thirteenth and handoff and setup-matt-pocock-skills to eleventh and twelfth, with find-skills crossing to 4.0M; the audits window moved to the feishu fleet Pending in rows 31 through 50, Snyk Med Risk now also on hyperframes and reddit-automation, Snyk High on design-mobile-apps at row 18, one Socket alert back on media-use and the four 101-skills entries at rows 25 through 28, and code-review outside at row 53 (778.2K installs); the publisher chips read azure-skills 8.4M, open.feishu.cn 17.5M single, larksuite/cli two totals, runcomfy three; skillregistry.io went dark again (its second outage); the CLI moved to 3,088 forks and 582 commits with the 79-agent README count re-verified.

## See also

- [Agent Skills open standard](../agent-skills-open-standard/index.md) - the format this registry distributes
- [Anthropic Agent Skills](../anthropic-agent-skills/index.md) - the largest publisher on the leaderboard
- [OpenCode](../../harnesses/opencode/index.md) - one of the many harnesses the CLI installs into
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the distribution layer sitting over the harness map

## References

- https://vercel.com/blog/introducing-skills - launch announcement (2026-01-20)
- https://skills.sh/ - leaderboard, install counts, supported agents, as of 2026-10-22
- https://skills.sh/docs - ranking method (CLI telemetry) and the security disclaimer
- https://skills.sh/audits - Gen/Socket/Snyk audit columns, open.feishu.cn fleet Pending in rows 31 through 50, Snyk Med Risk on find-skills, agent-browser, hyperframes-cli, hyperframes, and reddit-automation and Snyk High Risk on design-mobile-apps (row 18) in the window, one Socket alert on media-use and the 101-skills quartet, code-review outside at leaderboard row 53 (778.2K installs), as of 2026-10-22
- https://www.skills.sh/microsoft/azure-skills/azure-validate - azure-validate still Pass on all three scanners via its detail page, as of 2026-10-22
- https://github.com/vercel-labs/skills - CLI source, agent path table, telemetry opt-out, 34,499 stars as of 2026-10-13, 3,088 forks and 582 commits as of 2026-10-22
- https://skillregistry.io/ - nearest standalone competitor, dark again as of 2026-10-22 (its second outage), last measured at 61 skills and 17,768 downloads on 2026-10-05, with 18 contributors
- https://github.com/Fcmam5/skilleton - lockfile-style, no-telemetry alternative
- https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills - the underlying untrusted-skill risk
- https://www.promptarmor.com/resources/anthropics-skill-scanner-defeated-by-backdoored-skills - the backdoored-skill bypass behind the new caution: skills that passed Anthropic's scanner by fetching payloads at runtime, and the marketplace criticism (fetched 2026-10-07)
