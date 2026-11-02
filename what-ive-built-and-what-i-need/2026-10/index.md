---
title: "What I've built and what I need: October 2026"
created: 2026-10-29
type: post
status: finished
tags: [what-ive-built-and-what-i-need, personal-update, llm, ai-agents, automation, sdlc, workflows, fully-ai-generated, llm=deepseek-v4.1-flash]
readability: 3
audience_notes: >
  A monthly status update for anyone following my work on LLM-driven software development pipelines. Assumes familiarity with the SDLC skills from prior updates; October covers consolidating one-off tools into a single app, moving recurring work onto schedules, and reviewing intent instead of code.
agent_sessions:
  - ses_e7a6a863fffeYo7OmzIS8ZGGmI
---

The headline this month was **consolidating a set of one-off tools into a single app, and moving more of the work onto schedules that run without me**.
Agentic took 351 commits, the skills library took 70, and most of what landed there exists to make the next session start from a prepared decision instead of a blank prompt.

## What I Have Been Working On

**Built Agentic, one place for the tools I kept writing separately.**
[Agentic](https://github.com/TomzxCode/agentic) tracks work as tasks, links the Slack threads, GitHub issues and pull requests, documents, and notes that feed each task, creates a git worktree per task, and runs a coding agent against it.
An agent keeps a current summary and a next-steps list per task, so resuming costs a read instead of a re-derivation.
The backend is FastAPI with SQLModel, the frontend is a Vue PWA, and a CLI drives the same API, which is what makes the app usable by an agent and by me.
The reasoning is compounding: each one-off tool solved a problem and then sat mostly unused, while one app everything feeds into gets better the more I use it, and it tracks the work better than I did.
It is also far from the state I want, which is why it is first in my needs below.
[A separate article covers what Agentic is for and how it works](../../agentic/index.md).

**Moved recurring work onto schedules.**
The skills that trigger on a schedule (review requests, PR feedback, failing CI, the daily refresh of this blog's agents section) mean I stop starting the same session by hand.
The saving is not the keystrokes.
It is that I arrive at a prepared request for a decision instead of prompting, waiting, and then deciding.
That changes what my attention is for: deciding rather than waiting.
Most of the work below follows from that shift.

**Started looking at my own work as a production line.**
The [sessions analyzer](https://github.com/TomzxCode/llm-sessions-analyzer) from September measures where wall-clock time goes.
This month the view became more literal: [ghx](https://github.com/TomzxCode/ghx) grew a local web UI with a graph of the PR pipeline (waiting on a reviewer, on the author, on merge), and Agentic records changes per task so it can compute an autonomy rate and a yield.
I wrote about the [metrics I want for a software factory](../../metrics-for-a-software-factory/index.md).
The point of measuring is to pick the next bottleneck instead of the next interesting thing.

**Moved review from reading code to checking intent.**
[adversarial-pr-review](https://github.com/tomzx/agents/blob/main/skills/adversarial-pr-review/SKILL.md) assumes a change is broken and works to make it fail, and only reports a failure it executed or reproduced.
Four surface reviews cover CLI, SDK, API, and database contracts, [summarize-behavior-changes](https://github.com/tomzx/agents/blob/main/skills/summarize-behavior-changes/SKILL.md) states what behaves differently after merge, and `review-pr` and `assess-pr-risk` now ask whether a change is proportional to the problem it solves.
The reason for the shift is that deep line reading was my most expensive review activity and the least decisive.
**What I want to review is the intent document and the behavior delta.**
If the intent is right and the diff of behaviors is what I asked for, reading every line adds little.

**Made test runs auditable.**
[create-test-skill](https://github.com/tomzx/agents/blob/main/skills/create-test-skill/SKILL.md) generates a per-project skill that lists every test level the project supports, how each one is set up, and the exact command that runs it.
Every run also writes a trace of the commands called and any temporary change made to get the suite to pass.
An agent can make a suite look green by running one narrow test or relaxing an assertion, and the trace is what makes those moves visible.
This is the piece that makes walking away from a session plausible.

**Pushed the review loop into research on a nearly unsolvable problem.**
[p-np](https://github.com/TomzxCode/p-np) was an exploratory exercise in using my z.ai subscription to guide agents against the P vs NP problem.
It holds a corpus of route maps, claim forensics, and experiments, plus a Lean 4 formalization of the p=2 core of the Krajicek program, with review loops that downgrade a claim whenever the proof does not survive.
The loop ran as a teacher/student pair: DeepSeek v4.1 Flash read what GLM 5.3 Flash had produced every few hours and sent back feedback for the working agent to address.
It ran for two days and about thirty commits, then the reviews started finding contradictions faster than the work could resolve them, so I stopped it.
The lesson was that a research loop without a mechanical gate for the word "proved" turns into reviewing its own reviews.

**Tightened how the skills write.**
October was mostly subtraction: plain language with figurative language banned, tighter [communication guidelines](https://github.com/tomzx/agents/blob/main/skills/communication-guidelines/SKILL.md), article plans written before drafting, and credibility ratings for sources.
When the text is machine-written, the cheapest quality gain is removing what the model adds for no reason.

## What I Currently Need

**I need the pull request caching in Agentic to stop being slow.**
Caching PRs through ghx is not efficient right now.
It is the most used data in the app and the most expensive to load, and I need it fixed before it becomes the reason I stop opening the app.
Fixing it also improves ghx, which everything else reads from.

**I need the sidebar to reflect what I actually do.**
It reached 20 items, which means the app has no model of my work and offers everything at once.
I need to cut it down to what I reach for daily and move the rest behind something I open on purpose.

**I need to decide which views are worth keeping.**
Several views in the app went unused after I built them.
I need to use each one deliberately, then either improve it or delete it, rather than leaving a shelf of half-used pages.
Deleting is the outcome I expect for most of them.

**I need to improve what exists before adding more.**
I expect November to go into Agentic and the skill library fitting each other, not into new surface area.
The risk is that I keep adding views because adding is easier than deciding, and end up with the same problem one level up.

## See also

- [What I've built and what I need: September 2026](../2026-09/index.md) - the previous entry; October turns the scheduled review loop it described into a habit and consolidates the tooling around it.
- [Agentic: a work tracker for coding agents](../../agentic/index.md) - the longer write-up of the app that consolidated the one-off tools.
- [Metrics for a Software Factory](../../metrics-for-a-software-factory/index.md) - the measurements behind the production line view of my own work.
- [Specifications Are Lossy Compression](../../specifications-are-lossy-compression/index.md) - why the intent document, not the diff, is where review should land.
- [Intent-Driven Development](../../intent-driven-development/index.md) - the review approach this month moved toward.
- [Coordinating Multiple Agents from Messages to a Shared Work Ledger](../../coordinating-multiple-agents-from-messages-to-a-shared-work-ledger/index.md) - the task ledger idea Agentic implements.

## References

- [agents](https://github.com/tomzx/agents) - the skill library, including the review, test, and discovery skills added this month.
- [agentic](https://github.com/TomzxCode/agentic) - the task app that consolidates the one-off tools.
- [ghx](https://github.com/TomzxCode/ghx) - the GitHub cache and CLI that agentic reads PRs from.
- [llm-sessions-analyzer](https://github.com/TomzxCode/llm-sessions-analyzer) - the session time measurement from September.
- [p-np](https://github.com/TomzxCode/p-np) - the research exercise described above.
