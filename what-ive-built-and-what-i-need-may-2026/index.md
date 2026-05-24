---
title: "What I've built and what I need: May 2026"
created: 2026-05-24
type: post
status: finished
tags: [personal-update, skills, ai, automation, fully-ai-generated, llm=glm-5.1]
readability: 3
---

The past month has been about turning repetitive workflows into reusable skills, and the gaps that remain are mostly about making those skills smarter, not more numerous.

## What I Have Been Working On

**Built a full SDLC skill pipeline.** I shipped a comprehensive software development lifecycle orchestrator in [dot-claude](https://github.com/tomzx/dot-claude/blob/main/skills/sdlc/SKILL.md) that chains over 20 sub-skills, from issue creation through learnings capture. It handles phase contracts, backtracking when upstream artifacts are incomplete, and fast paths for small work like bug fixes and config changes. The pipeline tracks artifact status via YAML frontmatter and stores everything under `.sdlc/` with a consistent directory structure.

**Made issue tracking actually useful.** I have been using [create-issue](https://github.com/tomzx/dot-claude/blob/main/skills/create-issue/SKILL.md) heavily over the past month to track gaps in the software I am building. It is not perfect, but it beats not tracking the work, and it captures more context than I would take the time to write by hand.

**Automated PR descriptions.** I use [create-pr-description](https://github.com/tomzx/dot-claude/blob/main/skills/create-pr-description/SKILL.md) to generate PR descriptions based on code changes and intent. Writing those manually was slow and inconsistent; now the descriptions reflect what actually changed without the manual effort.

## What I Currently Need

**Battle test the SDLC pipeline.** The [SDLC skill](https://github.com/tomzx/dot-claude/blob/main/skills/sdlc/SKILL.md) is built but has not been stress-tested end to end on real feature work. I need to run it through enough real scenarios to surface the gaps between the design and practical use.

**Scheduled issue-to-PR automation in openchamber.** Openchamber can already create a worktree per directory and execute a prompt, but it does not run on a regular schedule. I need it to pick up new issues, execute the full pipeline, and open PRs without manual triggering.

**Automated issue triaging in open source projects.** I built a [triage-issues](https://github.com/tomzx/dot-claude/blob/main/skills/triage-issues/SKILL.md) skill but have not used it on my own repositories. The goal is to reduce the burden of going through issues to identify duplicates and decide whether they should be acted on.

**Memory that agents manage automatically.** Right now memory requires explicit reads and writes. I need agents to store, retrieve, and decay knowledge across sessions without me prompting them to do it.

**Contextual Slack support.** I need a way for users asking for help on Slack to receive contextually relevant information, and for the system to learn from human-to-human interactions and the answers people give each other.

**Automatic context clearing between execution and review.** Running implementation and review in the same context introduces bias. I need a mechanism, likely using forked subagents, to `/clear` between execution and review automatically so the reviewer starts fresh.

**Accuracy pass on daily summaries.** I have accumulated daily summaries that contain inaccuracies. I need something to go through them and correct what is wrong, rather than letting bad data compound over time.

**Incremental PR description updates.** When I update a PR after the description is written, I need [create-pr-description](https://github.com/tomzx/dot-claude/blob/main/skills/create-pr-description/SKILL.md) to adjust minimally, appending or amending what changed, rather than regenerating the whole thing from scratch.

**Skill usage tracking.** I need to know how often each skill is invoked and when. Without that data, I cannot tell which skills are earning their keep and which are dead weight.
