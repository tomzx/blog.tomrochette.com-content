---

title: "What I've built and what I need: September 2026"
created: 2026-10-04
type: post
status: finished
tags: [what-ive-built-and-what-i-need, personal-update, llm, ai-agents, automation, sdlc, workflows, fully-ai-generated, llm=deepseek-v4.1-flash]
readability: 3
audience_notes: >
  A monthly status update for anyone following my work on LLM-driven software development pipelines. Assumes familiarity with the SDLC skills from prior updates; September focuses on the PR review loop, measuring where session time goes, and the move toward hands-off runs.
agent_sessions:
  - ses_ef956eeabffeP9qTkKILuMqi0B
---

The headline this month was **turning the review skills into a scheduled, mostly unattended loop, and building the first instrument for where my session time actually goes**.
September came to 58 commits, over 180 files changed, and 14 new skills.
The measurement points straight at what I need next: to stop babysitting sessions.

## What I Have Been Working On

**Turned reviewing others' PRs into a scheduled, mostly unattended loop.**
[review-requested-prs](https://github.com/tomzx/agents/blob/main/skills/review-requested-prs/SKILL.md) now fetches every PR waiting on me in one GraphQL query, runs discovery in parallel, sorts the queue by blocking depth, and skips any step already done for the current commit.
It also recovers dropped team review requests from notifications, and a readiness light beside each PR marks when it can be auto-approved.
The new [assess-pr-risk](https://github.com/tomzx/agents/blob/main/skills/assess-pr-risk/SKILL.md) scores a PR's risk and confidence to decide how deep the review goes, using only evidence it gathers itself.
The reverse direction, handling feedback on my own PRs, is [triage-pr-feedback](https://github.com/tomzx/agents/blob/main/skills/triage-pr-feedback/SKILL.md) plus a FastAPI dashboard that groups and sorts incoming comments so I can mark each one implement, decline, or defer.
[handle-pr-reviewer-feedback](https://github.com/tomzx/agents/blob/main/skills/handle-pr-reviewer-feedback/SKILL.md) owns that contract and triage just delegates.
[handle-failing-pr-ci](https://github.com/tomzx/agents/blob/main/skills/handle-failing-pr-ci/SKILL.md) lists my PRs' CI status and fixes failures in parallel.
[review-pr-full](https://github.com/tomzx/agents/blob/main/skills/review-pr-full/SKILL.md) chains the whole review, now starting with test-coverage analysis and committing its assets alongside the report.

**Pushed verification earlier, into implementation.**
[refactor-implementation](https://github.com/tomzx/agents/blob/main/skills/refactor-implementation/SKILL.md) runs between implementation and review to introduce only the abstractions the change needs.
[create-implementation](https://github.com/tomzx/agents/blob/main/skills/create-implementation/SKILL.md) now checks coverage and adds characterization tests before it modifies code.
[propagate-changes](https://github.com/tomzx/agents/blob/main/skills/propagate-changes/SKILL.md) replaced backpropagate-sdlc and stopped being one-directional: it rewrites dependents and questions the premises they rely on.
The repo's own rules now say to get a working feature first, before any lint or type check.

**Built an instrument for where session time goes.**
[llm-sessions-analyzer](https://github.com/TomzxCode/llm-sessions-analyzer) reads the [agentsview](https://github.com/kenn-io/agentsview) `sessions.db` archive read-only and attributes the wall-clock span between consecutive messages to a category: coding, testing, linting, formatting, build, exploration, research, git, delegation.
It reports a stacked bar, a per-category table, and a timeline in the terminal or as a self-contained, sortable HTML report.
The point is to find where the time actually goes: whether I am waiting on a specific tool most of the day (test suites run too widely or too often, lint and type checks that cost more than they save, builds whose artifacts never get used), or simply waiting on the model to generate.

**Added visualization and writing skills.**
[create-svg-image](https://github.com/tomzx/agents/blob/main/skills/create-svg-image/SKILL.md) and [create-mermaid-visualization](https://github.com/tomzx/agents/blob/main/skills/create-mermaid-visualization/SKILL.md) split diagram work out of [create-article](https://github.com/tomzx/agents/blob/main/skills/create-article/SKILL.md), which now delegates to them, records the agent sessions that contributed to a piece, and requires direct statements over loose prose.

**Grew the general-purpose skill set.**
[setup-agent-machine](https://github.com/tomzx/agents/blob/main/skills/setup-agent-machine/SKILL.md)/[sync-agent-machine](https://github.com/tomzx/agents/blob/main/skills/sync-agent-machine/SKILL.md) turn a directory into an indexed machine context.
[search-existing-issues](https://github.com/tomzx/agents/blob/main/skills/search-existing-issues/SKILL.md), [select-issue](https://github.com/tomzx/agents/blob/main/skills/select-issue/SKILL.md), [trace-issues](https://github.com/tomzx/agents/blob/main/skills/trace-issues/SKILL.md), [create-discussion](https://github.com/tomzx/agents/blob/main/skills/create-discussion/SKILL.md), and [prune-merged-worktrees](https://github.com/tomzx/agents/blob/main/skills/prune-merged-worktrees/SKILL.md) cover the issue lifecycle.
[slack-resolve-threads](https://github.com/tomzx/agents/blob/main/skills/slack-resolve-threads/SKILL.md) and [improve-sessions](https://github.com/tomzx/agents/blob/main/skills/improve-sessions/SKILL.md) mine Slack threads and past sessions for follow-ups and reusable lessons.
[create-skill](https://github.com/tomzx/agents/blob/main/skills/create-skill/SKILL.md) authors a new skill from the best existing examples.

**Made concise communication a shared rule instead of a per-skill habit.**
[communication-guidelines](https://github.com/tomzx/agents/blob/main/skills/communication-guidelines/SKILL.md) is the single place every skill reads before it writes text on my behalf, from GitHub comments to Slack messages and email.
It sets one principle (lead with the point, cut every sentence that does not change what the reader knows or does) and concrete length ceilings per surface.
**This matters more as more of the output is machine-written**, since a language model's natural failure mode is padding and repetition.

**Taught an agent to read a day of Slack and report what was decided.**
[extract-colleague-decisions](https://github.com/tomzx/agents/blob/main/skills/extract-colleague-decisions/SKILL.md) searches Slack for the messages a set of colleagues authored in a day, reads the full threads behind them, and pulls out the decisions each person made, plus who supported them, citing a permalink for each and filtering out the chatter.
The judgment is the point: telling a decision from an acknowledgement is a reading task, not a keyword match, and a small Jev classifier buckets each message to speed that judgment up.

**Added a memory file so sessions stop relearning the same lessons.**
`AGENTS.md` carries the durable rules, but not the decisions, conventions, and gotchas discovered mid-session that the next one should inherit.
`MEMORY.md` holds those, a global one for cross-project lessons and one per project for repository facts.
Every session reads both at the start and writes back what it learns.
It stays narrow on purpose: only what a future session cannot cheaply rediscover from the repo, kept concise and nothing a near-term commit would invalidate.

**Tightened conventions and tooling.**
[banned-terms.txt](https://github.com/tomzx/agents/blob/main/banned-terms.txt) is now the single source of truth for banned terms, and report file naming was normalized across the review skills.
The library was cleaned of Claude Code and `.claude` references and the old `slack-cached` name.
`create-pr` gained reviewer context comments via [ghx](https://github.com/TomzxCode/ghx) and design decisions in the description, and `create-pr-description` now diffs against the PR base with `gh` instead of Graphite.

## What I Currently Need

**I need to stop babysitting sessions.**
Most of my supervision time goes to steering a running agent and catching when the original prompt or context was wrong.
That is the wrong place for my attention to be.
What I want is a run that goes from prompt to end-to-end tested and verified on its own, and I do not have it yet.

**I need proof that is easy to consume and that proves real behavior.**
The verification I need at the end is not the model asserting success.
It is evidence a human can skim quickly that the thing we expected to work actually works, not that the agent hallucinated it working.
Closing this gap is what makes the first one possible: I can walk away only when I trust the proof.

**I need to go from one session at a time to many.**
I want to explore solving problems at scale as a learning exercise, mostly in software engineering projects, on the hunch that a generic framework is hiding there.
The tooling (loops, the scheduler, the gates), the trust (relying on CI and review), and the process (how work is scoped and handed off) all feel like part of the blocker, and the sessions analyzer is my first attempt to see which one to attack first.

**I need the review pipeline to stay fast as I lean on it more.**
`review-requested-prs` and the other review skills call the GitHub API directly, and I want to route them through [ghx](https://github.com/TomzxCode/ghx) as a caching layer so repeated runs reuse cached issues, PRs, and comments instead of refetching them.
That should cut API calls, raise the cache hit rate, and keep the hourly loop cheap enough to run without thinking about it.

## See also

- [What I've built and what I need: August 2026](../2026-08/index.md) - the previous entry; September turns the review skills it described into a scheduled loop.
- [Managing Many LLM Agent Sessions](../../managing-many-llm-agent-sessions/index.md) - the one-to-many problem this month's need names.
- [Verifying Code Without Reading It](../../verifying-code-without-reading-it/index.md) - the proof a human can skim without reading every line.
- [Loops as Files](../../loops-as-files/index.md) - the scheduling layer that makes unattended runs possible.
- [You Are the Bottleneck](../../you-are-the-bottleneck/index.md) - why session babysitting is the thing to remove next.

## References

- [agents](https://github.com/tomzx/agents) - the skill library where the review, implementation, and machine-context skills landed.
- [llm-sessions-analyzer](https://github.com/TomzxCode/llm-sessions-analyzer) - the tool built this month to measure where session time goes.
- [agentsview](https://github.com/kenn-io/agentsview) - the session archive llm-sessions-analyzer reads.
- [ghx](https://github.com/TomzxCode/ghx) - the GitHub CLI used across the review and feedback skills.
