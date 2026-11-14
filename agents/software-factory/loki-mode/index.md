---
title: Loki Mode
created: 2026-10-07
updated: 2026-11-13
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, software-factory, autonomous-agents, verification]
readability: 3
audience_notes: >
  Engineers who want an autonomous issue-to-pull-request factory that proves what it delivered.
  Assumes you know what an acceptance contract, an MCP server, and a source-available license are.
---

Loki Mode is Autonomi's source-available autonomous software factory: hand it a PRD, a GitHub issue, an OpenAPI doc, or a one-line brief, and it derives a delivery contract, builds against it, and ends with a signed Evidence Receipt stating what was proven and what was not.

## What it is

**A local CLI factory whose acceptance artifact is a receipt you can re-check offline, not an agent's claim of done.**
It installs from npm, Bun, Homebrew, or Docker and runs on your machine with your own keys against Claude by default, with Cline, Codex, Aider, and OpenCode supported as experimental providers; a bundled MCP server exposes 39 tools including run, status, and verify for background runs.
Before a build counts as done, a review council selects reviewers from a scored specialist pool, and if the contract cannot be derived the run blocks and asks one question instead of guessing.
Autonomi publishes it under BUSL-1.1, and the README documents outcomes and exit codes, a workspace command, and a doctor that names setup blockers.

## Status

Active and shipping fast: 1,093 stars and 206 forks since creation on 2025-12-26 (as of 2026-10-13), 326,335 Docker pulls as of 2026-11-13, per GitHub and Docker Hub.
Pushed 2026-11-13, and the train is at v11.139.0 (2026-11-12), with npm `latest` and `next` in sync at 11.139.0, per the GitHub API and the npm registry as of 2026-11-13.
**The burst since v11.18.0 (2026-10-20) has covered about one hundred twenty minors in under a month, and its newest entries keep reshaping the acceptance story and then pulling it back: the never-stop policy shipped in v11.138.0 (a run that meets an ambiguous or conflicting spec implements its best reading, discloses the choice, and caps at PARTIAL, with one tool-less Opus consult fired at a would-be stop or a red verify), and v11.138.1 (2026-11-12) reversed it one day later, turning the consult and never-stop off by default again so a conflicting spec ends BLOCKED as before, after the author's own bench measured two false VERIFIED verdicts with the consult on against zero with it off; v11.139.0 (2026-11-12) then trimmed the default call budget, folding the separate coverage turn into the implement brief and turning the executable-spec call off by default, at a measured cost of about one third of v11.138.1's per-task price on Haiku; the Wall (Loki writing acceptance tests before implementing) stays off by default with VERIFIED requiring the repository's own suite green plus a test the harness itself runs failing on the base commit and passing on the change (v11.130.0), the Project Model is answered from manifests with zero model sessions and twenty-seven dead commands were removed (v11.130.0), PR titles now name the work instead of the run id (v11.125.0), .NET repos reach a verified result with no configuration (v11.103.0), and every signed receipt carries a measured Seal accuracy line read from seeded-defect results (v11.90.0).**
The release process itself changed mid-train: v11.17.99 reduced CI to a single release workflow that publishes npm, Homebrew, the SDKs, and signed Docker images with no test gate in front, removing the Tests, nightly, security-audit, and SBOM workflows.
The catch-up release run changed the acceptance story: seal VERIFIED now requires at least one agent-independent (exogenous) proof by default, `loki verify --explain` classifies each gate as exogenous or agent-influenced, and the burst shipped a deploy path (`loki deploy` with Fly, Netlify, and Cloudflare verbs, custom-domain TLS proof, and a rollback command), per the v11.17.33 through v11.17.40 release notes.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=asklokesh/loki-mode&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=asklokesh/loki-mode&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=asklokesh/loki-mode&type=date&legend=top-left" />
</picture>

**Its Hacker News footprint is self-submitted threads in the single digits, and the 99.67 percent SWE-Bench claim in one of them is self-reported, so no independent evaluation exists as of 2026-10-07.**
The version line moves faster still: eight published releases in the two days to 2026-10-09, after the five that closed 2026-10-08, with v11.3.3 never published because its release run failed.
The 11.4-to-11.15 burst added a publish pattern the release notes state plainly: most tagged versions in the run (v11.4.0 through v11.14.0) failed required CI and reached npm only through fix-forward patches, and v11.6.0 was a consolidation release that merged or deleted every duplicate module under an "extend existing code, never duplicate" rule.
v11.3.1 shipped the 11.3 program's ten v1 features (cost preview, mutation proof, intent card, reviewer brief, scored worktree attempts, memory with proof, overnight queue, before/after proof, provider failover, and a supply-chain guard), the router escalation chain and plan-time routing from v11.3.0 stay off by default, and the v11.3.4 through v11.3.9 security arc hardened credential reach, with the release notes now stating plainly that this is default-path hardening, not a sandbox.

## Strengths

- **The receipt is the acceptance artifact**: it states what was proven and what was not, and anyone can re-check it offline.
- **It refuses to guess**: an underivable contract blocks the run with one question, a rarer safety move than another retry.
- **The review council is pulled, not prompted**: reviewers are selected from a scored specialist pool per run.
- **Distribution is finished**: npm, Homebrew, and Docker installs, a doctor for setup, and an MCP server for programmatic runs.

## Cautions

- **BUSL-1.1 is source-available, not open source**: the code is readable but not OSI-licensed, and GitHub cannot classify the license.
- **The README's Documentation link dead-ends**: the wiki it points to does not exist, so docs live in scattered repo files.
- **Benchmark claims are self-reported** and the HN threads are self-submitted; treat the SWE-Bench number as marketing until a third party repeats it.
- **Version churn is fast**, with a v10 engine already superseded by an 11.x line.

## Pricing

Free as a source-available CLI: the BUSL-1.1 grant covers personal, internal, academic, and non-commercial use, converts the code to Apache-2.0 on 2030-03-19, and names founder@autonomi.dev for other arrangements.
You bring your own model keys, and Autonomi's site describes a live control plane without published prices as of 2026-10-09, a page this run could not re-fetch (empty on both 2026-10-11 attempts).
There is no public tier to track yet.

## Compared to

- [Super Simple Software Factory](../super-simple-software-factory/index.md) is the MIT stamped-skill minimalist; Loki Mode is a packaged CLI with a receipt gate under a BUSL license.
- [Ouroboros](../ouroboros/index.md) hides the grading from the worker; Loki Mode signs what was proven and lets you verify the receipt yourself.
- [SuperPlane](../superplane/index.md) runs the intake-to-PR line as a shared platform; Loki Mode runs it locally with your keys.

## Bottom line

**Recommended for engineers who want an autonomous issue-to-PR loop with an offline-checkable receipt and accept a source-available license and self-reported benchmarks.**
Not for teams that require OSI licensing, and not for anyone who needs independent evaluation first.

## Changes

- 2026-10-07 - Created from the category's entrant scan as the receipt-gated member.
- 2026-10-08 - Recorded the npm train's jump from 11.0.3 to 11.3.0 (five releases in the two days to 2026-10-08, led by the router escalation chain shipped off by default) and refreshed counts.
- 2026-10-09 - Recorded the train to 11.3.9 (eight published releases since 11.3.0, v11.3.3 never published after a failed release run), the v11.3.1 ship of the 11.3 program's ten v1 features, the v11.3.4-v11.3.9 credential-hardening arc with its "hardening, not a sandbox" wording, the provider roster's Cline and Aider additions as experimental, and refreshed counts.
- 2026-10-11 - Added the BUSL-1.1 use grant and its 2030-03-19 Apache-2.0 conversion date to Pricing, recorded the autonomi.dev fetch failure (empty on two attempts), and refreshed counts.
- 2026-10-16 - Recorded the train from 11.3.9 to v11.15.0 (2026-10-16, `next` tag while `latest` holds 11.10.1), the fix-forward publish pattern where CI-failed tags reached npm only through patches, and the v11.6.0 consolidation release.
- 2026-10-17 - Recorded the npm `latest` tag catching up to the train at 11.17.39 (GitHub train at v11.17.40 after eight stable-tagged releases on 2026-10-17) and the acceptance change behind it: seal VERIFIED requires one agent-independent proof by default, with `loki verify --explain` naming each gate's class; the deploy path (Fly, Netlify, and Cloudflare verbs, custom-domain TLS proof, rollback) landed in the same burst.
- 2026-10-19 - Recorded the train passing v11.17.58 to reach v11.17.81 (2026-10-19), with npm `latest` and `next` both in sync at 11.17.81.
- 2026-10-21 - Recorded the train reaching v11.18.0 (2026-10-20, a no-engine-change checkpoint release, npm in sync) and the v11.17.99 CI reduction to a single release workflow with no test gate in front (Tests, nightly, security-audit, and SBOM workflows removed).
- 2026-10-23 - Recorded the burst from v11.18.0 to v11.60.17 (about forty minors in three days, releases minutes apart with single-fix notes quoting the review verdict), npm `latest` at 11.60.15 ahead of `next` at 11.60.10, and Docker pulls refreshed to 225,945 (2026-10-23).
- 2026-10-25 - Recorded the train passing v11.60.17 to reach v11.77.0 (2026-10-24, about sixty minors in five days), npm `latest` and `next` back in sync at 11.77.0, the newest entries shipping feature lists again (live `loki status` following, stuck-run alerts, `loki github protect` requiring the receipt status check on the default branch), and Docker pulls refreshed to 265,042 (2026-10-24).
- 2026-10-31 - Recorded the train passing v11.77.0 to reach v11.94.0 (2026-10-31, seventeen minors in seven days, npm `latest` and `next` in sync): measured Seal accuracy lines on every signed receipt (v11.90.0, printed in pull-request bodies and verify output by v11.91.0), resume for interrupted runs (v11.81.0, v11.87.0), `loki try` on a public repository in a temporary clone (v11.79.0), an independent Java acceptance test (v11.83.0), acceptance checks written by a separate walled provider call (v11.85.0), and Docker pulls refreshed to 296,635 (2026-10-31).
- 2026-11-01 - Recorded the train passing v11.94.0 to reach v11.103.0 (2026-11-01, nine minors since v11.94.0, npm `latest` and `next` in sync): .NET support with xUnit, NUnit, and MSTest acceptance tests (v11.103.0), the package slimmed to 789 npm files with the Docker image now running the quality gates (v11.102.0), run-branch cleanup with bundle saves and Bash secret-read denies (v11.101.0), whole-issue runs up to four in parallel with splitting only after a failed whole attempt (v11.99.0, v11.100.0), labelled draft PRs for PARTIAL results (v11.98.0), in-place answers to blocked runs and arbitrated Wall tests capping the Seal at PARTIAL (v11.95.0, v11.96.0), and Docker pulls refreshed to 306,269 (2026-11-01).
- 2026-11-07 - Recorded the train passing v11.103.0 to reach v11.138.0 (2026-11-06, about thirty-five minors in five days, npm `latest` and `next` in sync): the Wall now off by default with VERIFIED requiring the repository's own suite green plus a harness-run test failing on the base commit and passing on the change, the Project Model answered from manifests with zero model sessions, and twenty-seven dead commands removed (v11.130.0), a never-stop policy with one Opus consult implementing its best reading and capping at PARTIAL (v11.138.0), and PR titles naming the work (v11.125.0); Docker pulls refreshed to 324,934 (2026-11-07).
- 2026-11-13 - Recorded the train reaching v11.139.0 (2026-11-12, npm `latest` and `next` in sync) and the acceptance-policy reversal behind it: v11.138.1 turned the v11.138.0 never-stop default and its Opus consult back off after the author's 20-task Haiku bench measured two false VERIFIED verdicts with the consult on against zero with it off (a conflicting spec ends BLOCKED again, LOKI_E10_OPUS_CONSULT=1 opts back in), and v11.139.0 folded the coverage turn into the implement brief and turned the executable-spec call off by default at a measured cost of about a third of v11.138.1's per-task price on Haiku (LOKI_E10_LEAN_CALLS=0 restores the old defaults); Docker pulls refreshed to 326,335 (2026-11-13).

## See also

- [Ouroboros](../ouroboros/index.md) - the other verification-first member, hidden grading versus signed receipts
- [Super Simple Software Factory](../super-simple-software-factory/index.md) - the MIT stamped-loop alternative
- [SuperPlane](../superplane/index.md) - the platform factory alternative
- [Software Factory Feature Matrix](../software-factory-feature-matrix/index.md) - where the receipt column sits among the factories

## References

- https://github.com/asklokesh/loki-mode - repository, delivery contract, review council, MCP server, and install methods
- https://www.autonomi.dev - Autonomi's site and the issue-to-PR-with-signed-receipt positioning
- https://www.npmjs.com/package/loki-mode - the npm package, 11.138.0 latest as of 2026-11-07
- https://github.com/asklokesh/loki-mode/releases - the release train, v11.139.0 newest as of 2026-11-13, the consult-off reversal and its false-VERIFIED bench numbers in the v11.138.1 notes, the lean-default cost cuts in the v11.139.0 notes, the never-stop Opus consult in the v11.138.0 notes, the Wall default flip, the manifest-read Project Model, and the removed commands in the v11.130.0 notes, the PR-title change in the v11.125.0 notes, the .NET acceptance path in the v11.103.0 notes, the package slim and Docker quality gates in the v11.102.0 notes, the run-branch cleanup and secret-read denies in the v11.101.0 notes, the whole-issue and split-run entries in the v11.99.0 and v11.100.0 notes, the draft-PR, arbitration, and in-place-answer entries in the v11.95.0 through v11.98.0 notes, the Seal accuracy receipt line in the v11.90.0 notes, the seal VERIFIED exogenous-proof default in the v11.17.33 notes, and the v11.17.99 CI reduction
- https://github.com/asklokesh/loki-mode/releases/tag/v11.3.1 - the v11.3.1 release notes, the 11.3 program's ten v1 features including scored attempts and memory with proof
- https://github.com/asklokesh/loki-mode/releases/tag/v11.3.9 - the v11.3.9 release notes, credential-isolation follow-ups and backstop-triggered promotion
- https://hub.docker.com/r/asklokesh/loki-mode - the Docker image and its pull count
- https://github.com/asklokesh/loki-mode/blob/main/LICENSE - Business Source License 1.1
- https://news.ycombinator.com/item?id=46393705 - the Show HN thread, 4 points
- https://news.ycombinator.com/item?id=46528155 - the self-reported 99.67 percent SWE-Bench thread, 2 points
