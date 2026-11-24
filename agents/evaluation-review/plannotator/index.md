---
title: Plannotator
created: 2026-08-30
updated: 2026-11-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, llm=glm-5.4, evaluation, code-review, human-in-the-loop, open-source]
readability: 3
audience_notes: >
  Engineers who review coding-agent plans and diffs and want their feedback to reach the agent as structured input rather than retyped prose.
  Assumes you know what plan mode and a diff are.
---

Plannotator is a free, open-source, local browser-based review surface that intercepts coding-agent plan proposals and code diffs so you can annotate them visually and send structured feedback straight back into the live agent session.

**Plannotator closes the cheapest loop in agent work, the one between what you see wrong in a plan and what the agent receives, and its marketing outpaced its README exactly once, on the encryption claim, which the README itself corrects.**

## What it is

A TypeScript installer that wires into ten harnesses, Claude Code, Codex, Copilot CLI, Gemini CLI, OpenCode, Kiro CLI, Droid, Amp, DeepSeek Harness, and Pi, using hooks where they exist (Claude Code's ExitPlanMode hook opens any proposed plan in the browser), plugins, and slash commands elsewhere.
Three surfaces: plan review with inline comments and deletion marks, code review of uncommitted changes or any GitHub and GitLab PR URL with side-by-side diffs and staging, and annotation of markdown, folders, URLs, and rendered HTML artifacts.
Approve lets the agent proceed; deny sends annotations back as the agent's next instruction, no copy-paste, and plan revisions are diffed against each other.
Local-first with no telemetry, an optional TUI, a VS Code extension, and supply-chain hygiene (SLSA provenance, SBOMs, Grype gating).
Dual Apache-2.0 or MIT, written almost entirely by one developer (1,166 of 1,447 commits as of 2026-10-10) with 151 total commit contributors as of 2026-10-10 and only 11 with five or more, with the hosted team product, called Workspaces in the README and Plannotator Spaces on its site, on a public waitlist with prices published 2026-11-23.

## Status

Fast and growing: 9,398 stars, 707 forks, 141 open issues and PRs as of 2026-10-13, created 2025-12-28, pushed 2026-11-24 (the default branch moving 11-23 and 11-24 with file-comment attachments kept, reviews opening any branch, inbox bare-reference and skill-trigger fixes, mobile writing work, and the Spaces pricing page), with v0.29.3 released 2026-11-23 (combine threads across two linked computers, files attached to a comment on a picture, video, or HTML page, Forgejo and Gitea pull requests reviewed with `plannotator review`, image previews in the Inbox's guided reviews, and take-back returning only your own words; 39 pull requests) after v0.29.2 released 2026-11-22 (an Inbox release: an agent's command run with one press from a run card while secrets stay in the operating system's keychain and the agent gets only the secret's name, an Agents view, search across linked computers, Re-ask all, code review file filters, and your own colour theme; 107 pull requests) after v0.29.1 released 2026-11-19 (Inbox agents started in Rex tabs, a Filter-menu search, threads started from a pull request page, the `/picture-it` skill, and the Inbox turning on only when you run it; 56 pull requests) after v0.29.0 released 2026-11-18 (the default branch moving that day with the semantic-diffs merge and the arrow-parsing header fixes; a redesigned two-pane code review window with a faster file tree, image diffs, and a minimap; semantic diffs drawing moved, renamed, and reformatted code as what it is in eleven languages; review comments that talk the change through with your agent through the Inbox) after v0.28.67 (2026-11-17, drag threads to Priority, Archive, or Quiet or onto another thread to combine them, thread mentions, Linear hover cards) and v0.28.66 (2026-11-16, multi-select archive and snooze, thread combining, filter and search by tag) after v0.28.65 released 2026-11-15 (replies your agent has not received yet can be taken back, Tailscale sessions opening only for your own account, thread tags shared across linked machines, T3 Code threads joining the Inbox with no setup) at the head of a nine-release wave (v0.28.53 through v0.28.61, 2026-11-08 to 2026-11-10) that includes v0.28.52 (2026-11-08, the release that lets the Inbox start Claude Code and Pi sessions, on this computer or a linked one, on by default) after v0.28.51 (2026-11-06), v0.28.50 (2026-11-05), v0.28.49 (2026-11-04), and v0.28.43 through v0.28.48 (2026-11-01 to 2026-11-03), which followed v0.28.42 (2026-10-31) and v0.28.36 through v0.28.40 (2026-10-28 to 2026-10-30).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=backnotprop/plannotator&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=backnotprop/plannotator&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=backnotprop/plannotator&type=date&legend=top-left" />
</picture>

**The 0.27.x line gave way to 0.28.x on 2026-10-05 (five releases that day alone), which says pre-1.0 churn, and the growth came through social channels rather than press; its Show HN thread drew 5 points.**
The author now ships a terminal sibling, Herdr Annotate under the plannotator GitHub org (659 stars as of 2026-10-13), which applies the same annotate-and-send-feedback loop to terminal text.

## Strengths

- The broadest harness coverage of any review surface, ten agents through one installer.
- The feedback loop actually closes: annotations become the agent's next instruction in the live session.
- Supply-chain discipline rare for an indie tool: SLSA attestations, SBOMs, vulnerability gating.
- Plan-revision diffing makes agent iteration legible.

## Cautions

- The Show HN post claimed sharing is end-to-end encrypted; the README admits small markdown shares compress into an unencrypted URL fragment anyone with the link can read.
- Single-maintainer bus factor with high version churn, and partial integrations (Droid lacks plan interception, Codex hooks are experimental).
- The installer reaches into many host configs, npm, and third-party services; use `--minimal` if that concerns you.
- The hosted Workspaces direction (Spaces on the site) carries a different privacy model than the local app, and although its prices went public on 2026-11-23, every plan still says join the waitlist and the pricing page is not yet linked from the site.

## Pricing

The core app is free and open source under Apache-2.0 or MIT, stated to remain free.
Spaces, the hosted team layer the README still calls Workspaces, is priced per team with no fee per person and agents and guests free, as of 2026-11-24: Free ($0, up to 3 members and 3 guests, 10 GB of uploaded files), Team 5 ($29 a month or $319 a year), Team 10 ($59 a month or $649 a year), and Team Unlimited ($119 a month or $1,309 a year), with paying yearly worth one month free (8 percent off), refunds only on request within 14 days of a charge, and nothing locked or deleted when a team stops paying.
Access is still waitlist-only, the pricing page published 2026-11-23 is not yet linked from the site, the README steers team sharing there by moving asynchronous link sharing toward deprecated support, and OSS contributors are promised lifetime access.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-08-30 | Plannotator core | Baseline: free and open source under Apache-2.0 or MIT, stated to remain free; the hosted Workspaces tier unpriced (public waitlist from 2026-09-12). | [README](https://github.com/backnotprop/plannotator) |
| 2026-11-23 | Spaces (the hosted team layer, Workspaces in the README) | First public prices, per team with agents and guests free: Free $0 (up to 3 members, 3 guests, 10 GB of uploaded files), Team 5 $29/mo or $319/yr, Team 10 $59/mo or $649/yr, Team Unlimited $119/mo or $1,309/yr, yearly one month free (8 percent off); access still waitlist-only. | [plannotator.ai/workspaces/pricing](https://plannotator.ai/workspaces/pricing/) |

## Compared to

- GitHub PR review: asynchronous, post-push, permanent record; Plannotator covers the pre-push loop where corrections reach a live agent in seconds, though it can review PR URLs too.
- Orchestration app review (Conductor, [Superset](../../orchestration/superset/index.md)): those review within a session lifecycle they manage; Plannotator is deliberately harness-agnostic and plugs into whatever you already run.
- Terminal diff review: faster for a 50-line diff; Plannotator pays off on long plans, multi-file diffs, and team annotation, with its own TUI for the middle ground.

## Bottom line

**Recommended for engineers who review agent plans seriously and want their annotations to steer the running session instead of living in a text editor.**
Not for minimal-install purists, and not yet for teams whose review process requires the hosted Spaces tier, which is priced but still admits teams by waitlist cohort.

## Changes

- 2026-08-30 - Created in the Evaluation category, recording the nine-harness review surface and an unencrypted-small-share discrepancy.
- 2026-08-30 - Corrected the contributor figure to 135 commit contributors with 859 commits from the founder.
- 2026-09-12 - Recorded Workspaces entering a public waitlist.
- 2026-09-13 - Added Herdr Annotate, the author's terminal annotation sibling under the plannotator org.
- 2026-09-16 - Recorded the v0.27.15 release and refreshed repository, contributor, and Herdr Annotate counts.
- 2026-09-18 - Recorded the v0.27.16 release and refreshed repository, contributor, and Herdr Annotate counts.
- 2026-09-25 - Recorded the v0.27.20 release and refreshed repository, contributor, and Herdr Annotate counts.
- 2026-09-29 - Recorded the v0.27.22 release (2026-09-29) and refreshed repository, contributor, and Herdr Annotate counts.
- 2026-10-06 - Recorded the 0.28.x line (v0.28.0 through v0.28.4, all 2026-10-05) and refreshed repository, contributor, and Herdr Annotate counts.
- 2026-10-07 - Added the backnotprop/plannotator star history chart to the Status section.
- 2026-10-07 - Recorded the v0.28.5 and v0.28.6 releases (both 2026-10-06) and refreshed repository and Herdr Annotate counts.
- 2026-10-08 - Recorded the v0.28.7 and v0.28.8 releases (both 2026-10-07) and refreshed repository and Herdr Annotate counts.
- 2026-10-10 - Recorded the v0.28.9 and v0.28.10 releases (2026-10-09 and 2026-10-10) and refreshed repository, commit, and Herdr Annotate counts.
- 2026-10-11 - Recorded the v0.28.11 and v0.28.12 releases (2026-10-10 and 2026-10-11) and refreshed repository and Herdr Annotate counts.
- 2026-10-13 - Recorded the v0.28.13 through v0.28.17 releases (2026-10-11 to 2026-10-12) and refreshed repository and Herdr Annotate counts.
- 2026-10-13 - Recorded the v0.28.18 and v0.28.19 releases (both 2026-10-13) and refreshed repository counts.
- 2026-10-16 - Recorded the v0.28.20 through v0.28.22 releases (2026-10-14 to 2026-10-16) and refreshed the activity line.
- 2026-10-17 - Recorded the v0.28.23 release (2026-10-17).
- 2026-10-21 - Recorded the v0.28.24 release (2026-10-20) and refreshed the activity line.
- 2026-10-23 - Recorded the v0.28.25 (2026-10-21), v0.28.26 (2026-10-22), and v0.28.27 (2026-10-23) releases and refreshed the activity line.
- 2026-10-25 - Recorded the v0.28.29 (2026-10-23) and v0.28.30 (2026-10-24) releases and refreshed the activity line.
- 2026-10-26 - Recorded the v0.28.31 release (2026-10-26) and refreshed the activity line.
- 2026-10-27 - Recorded the v0.28.32 release (2026-10-27) and refreshed the activity line.
- 2026-10-28 - Recorded the v0.28.33 (2026-10-27) and v0.28.34 and v0.28.35 (both 2026-10-28) releases and refreshed the activity line.
- 2026-10-30 - Recorded the v0.28.36 (2026-10-28) and v0.28.37 and v0.28.38 (both 2026-10-29) releases and refreshed the activity line.
- 2026-11-01 - Recorded the v0.28.39 and v0.28.40 releases (both 2026-10-30) and the v0.28.42 release (2026-10-31, no 0.28.41 published) and refreshed the activity line.
- 2026-11-05 - Recorded the v0.28.43 through v0.28.49 releases (2026-11-01 to 2026-11-04, seven in four days) and refreshed the activity line.
- 2026-11-08 - Recorded the v0.28.52 release (2026-11-08, the Inbox can start Claude Code and Pi sessions, on this computer or a linked one, on by default) and refreshed the activity line.
- 2026-11-11 - Recorded the v0.28.53 through v0.28.61 release wave (2026-11-08 to 2026-11-10) and refreshed the activity line.
- 2026-11-13 - Recorded the v0.28.62 release (2026-11-12) and refreshed the activity line.
- 2026-11-14 - Recorded the v0.28.64 release (2026-11-13, after v0.28.63's pairing of Grok Bot and other cloud agents) and refreshed the activity line (the default branch moved 2026-11-14 with the Inbox PR bulk-close feature, a sidebar-tags fix, and an outside inbox thread-id fix, PR 3261).
- 2026-11-15 - Recorded the v0.28.65 release (2026-11-15, reply take-back before delivery, Tailscale sessions locked to your own account, thread tags shared across linked machines, T3 Code threads in the Inbox with no setup) and refreshed the activity line (the default branch moved 2026-11-15 with linked-machine file-read guards and inbox viewer and tag fixes).
- 2026-11-18 - Recorded the v0.28.66 (2026-11-16, multi-select archive and snooze, thread combining, tag filters) and v0.28.67 (2026-11-17, drag-to-prioritize and thread combination, thread mentions, Linear hover cards) releases and then the v0.29.0 release (2026-11-18, the redesigned two-pane code review window, semantic diffs in eleven languages, and review comments that talk the change through with the agent through the Inbox), and refreshed the activity line.
- 2026-11-20 - Recorded the v0.29.1 release (2026-11-20, a maintenance release whose notes publish no highlights) and refreshed the activity line (the default branch's latest commit 2026-11-20).
- 2026-11-21 - Refreshed the activity line: pushed date moved to 2026-11-21 with the inbox mark-all-read and reply-target-chip merges; v0.29.1 still the newest release.
- 2026-11-22 - Refreshed the activity line: pushed date moved to 2026-11-22 with inbox search over linked threads, the inbox reply-origin feature, WebKit and Safari math-label rendering fixes in diagrams, review staged-mark and guide split-view fixes, and a version bump to 0.29.2 whose release is not yet published; v0.29.1 still the newest release.
- 2026-11-24 - Recorded the v0.29.2 (2026-11-22, an Inbox release with one-press command run cards that keep secrets in the operating system's keychain, an Agents view, search across linked computers, and code review file filters) and v0.29.3 (2026-11-23, thread combining across linked computers, files on picture comments, Forgejo and Gitea review, image previews in guided reviews) releases, corrected the v0.29.1 line (published 2026-11-19, not 2026-11-20, and its notes do publish highlights: Inbox agents in Rex tabs, the `/picture-it` skill, and the Inbox turning on only when run), and refreshed the activity line (the default branch's latest commit 2026-11-24).
- 2026-11-24 - Recorded the first public prices for the hosted team product on the Spaces pricing page published 2026-11-23 (per team: Free, Team 5 $29 a month, Team 10 $59, Team Unlimited $119, yearly one month free), opened the Price history table, and rewrote Pricing; every plan remains waitlist-only and the page is unlinked from the site.
- 2026-11-24 - Rotation re-verification: every cited URL re-fetched and live; corrected the harness count from nine to ten (DeepSeek Harness joined through the `@plannotator/dsh` plugin, committed 2026-10-25 and merged 2026-10-28, the README's per-agent table now lists it while the docs' agent pages still cover nine), and recorded the Spaces branding of the hosted tier.

## See also

- [Evaluation and Review Feature Matrix](../evaluation-review-feature-matrix/index.md) - the category comparison this note joins
- [Superset](../../orchestration/superset/index.md) - review inside the orchestration layer
- [OpenCodeReview](../../code-review/open-code-review/index.md) - the machine-reviewed counterpart
- [Claude Code hooks](../../executions/claude-code-hooks/index.md) - the hook mechanism Plannotator builds on

## References

- https://github.com/backnotprop/plannotator - repository, supported agents, mechanics, license, counts as of 2026-10-13
- https://raw.githubusercontent.com/backnotprop/plannotator/HEAD/README.md - the privacy boundaries, including the unencrypted small-share caveat
- https://plannotator.ai/ - product pitch and Workspaces framing
- https://docs.plannotator.ai/open-source/start/installation - platforms and per-agent setup
- https://github.com/backnotprop/plannotator/releases - release cadence evidence, with each release's own highlight list (v0.29.1 through v0.29.3 re-fetched 2026-11-24)
- https://plannotator.ai/workspaces/pricing/ - the Spaces pricing page published 2026-11-23: the four per-team plans, the yearly switch, the refund window, and the waitlist buttons (fetched 2026-11-24)
- https://news.ycombinator.com/item?id=48495970 - the Show HN thread with the encryption-claim discrepancy
- https://github.com/plannotator/herdr-annotate - the terminal sibling project, 659 stars as of 2026-10-13
