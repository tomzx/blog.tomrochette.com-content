---
title: "Continuous Research: Deep Research on a Loop"
created: 2026-08-22
type: post
status: finished
tags: [ai, llm, deep-research, ai-agents, research, knowledge-management, automation, fully-ai-generated, llm=glm-5.3]
readability: 3
audience_notes: >
  Assumes the reader has used a deep research feature (ChatGPT Deep Research, Claude Research, or an equivalent) and is comfortable with scheduled jobs and git. No ML background needed.
---

Deep research agents changed who does the reading, not how often it happens.
You type a question, the agent browses for up to half an hour, you receive a cited report.
Then the world moves, and the report starts decaying on the day it was written.
Ask the same question next month and the agent starts from zero, with no memory of what it already told you.
**The report was never the product. The product is a knowledge base that stays current, and the way to get one is to put research on a loop.**

I call this continuous research: declare the topics you care about, schedule an agent to re-research them on a cadence, and let it maintain a versioned knowledge base whose updates you read like diffs.
The human stops being the researcher and becomes the editor of a small research department that never sleeps.

## The Report Is a Snapshot

The current wave of research agents is genuinely good at the finding part.
ChatGPT's [Deep Research](https://en.wikipedia.org/wiki/Deep_research) autonomously browses the web for five to thirty minutes per query and returns a structured, cited report.
Claude's [Research](https://www.anthropic.com/news/research) runs multiple searches that build on each other and explores angles you did not ask for.
A recent [survey of deep research systems](https://arxiv.org/abs/2512.02038) formalizes what these tools do into four components: query planning, information acquisition, memory management, and answer generation.

What the survey's framing makes visible is where the continuity breaks.
Query planning, acquisition, and generation all live and die inside a single run.
The only component that could span runs, memory management, is scoped to the session.
These products treat memory as scratch space for finishing one answer, not as the durable asset.

So the structure of the interaction is: one question in, one report out, everything forgotten.
The run lengths are capped in minutes and the queries are metered by the month, because a long autonomous browse is expensive.
The output is a document, and a document is a snapshot.

None of this is a flaw in the tools.
It is a flaw in the unit of work.
A report answers a question once, but most questions that matter to your work are recurring, and recurring questions deserve a maintained answer, not a fresh one every time.

## What Continuous Research Is

The definition I use: **continuous research is a scheduled agent loop that incrementally maintains a versioned knowledge base about topics you have declared, so that your current understanding is a system property rather than an activity.**

Four pieces, each of which already exists on its own.

The first is the topic file.
One markdown file per topic stating the scope, the questions worth answering, the canonical sources, and what a meaningful change would look like.
This is an editorial artifact, written by you, and it is the part that encodes taste.
It is the same move as a skill file: the judgment goes in a file, versioned, rather than in a prompt you retype.

The second is the loop.
A schedule, a budget, and a skill that knows how to research one topic, in the format [Loops as Files](../loops-as-files/index.md) describes.
The scheduling primitive is no longer exotic: coding agents can already be [run on a schedule](https://code.claude.com/docs/en/scheduled-tasks), and a GitHub Actions cron or an agent runtime does the rest.

The third is the incremental update.
Each run advances a checkpoint, the last date the topic was researched, and the agent reads only what is new since that date.
arXiv monitoring works exactly this way: fetch what appeared since the last processed date, summarize, advance the checkpoint.
This is what separates continuous research from naively re-running a deep research query every week: the run is a delta against a base, not a rebuild from scratch.

The fourth is the knowledge base itself, which is the product the other three pieces serve.

## The Knowledge Base Is the Product

A continuous research knowledge base is a directory per topic, in git, containing three kinds of files.
A brief, rewritten each run, holding the current state of understanding.
A log of dated updates, so the history of the topic is readable as a timeline.
Snapshots of the sources, so every claim in the brief can be traced to the page it came from, even if that page moves or dies.

The properties fall out of the format.
The brief answers "what is true now", the log answers "what changed", and the diff between the last two versions of the brief is your weekly digest, generated as a byproduct rather than assembled by hand.
**The git log of the knowledge base becomes the changelog of your own understanding.**

I keep the research directories of this blog in this form, agent-written briefs with per-topic folders and source snapshots, and the pattern is the same one behind my public [specification workspace](https://github.com/TomzxCode/sdlc), where a weekly drift check re-derives specifications for open-source projects I depend on from their upstream code and commits the diff.
That workspace is a continuous research system pointed at code repositories instead of the web, and it has held up well enough to recommend the pattern in general.

The comparison worth making is to continuous integration.
A one-shot research report is a local build: correct at a moment, unverified the next day.
Continuous research is CI for knowledge: the build runs on every tick, and breakage, meaning drift between your knowledge base and the world, shows up as a diff instead of as a surprise in a meeting.

## The Wiki Half Already Exists

The LLM-maintained knowledge base now has a name and a following.
Andrej Karpathy's [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) idea file, published in April 2026, describes the same shift from deriving to maintaining: instead of a retrieval layer that reassembles knowledge from raw chunks on every question, the agent incrementally builds and maintains a persistent wiki of interlinked markdown pages.
His architecture has three layers: immutable raw sources, an LLM-owned wiki, and a schema file that tells the agent the conventions to follow.
The schema is my topic file under another name, and his append-only log matches the update log my knowledge base layout uses, which suggests these choices are convergent rather than arbitrary.
**The part of his framing worth keeping is the economics: humans abandon wikis because the maintenance burden grows faster than the value, and the LLM is the first maintainer that does not get bored.**
He traces the pattern back to [Vannevar Bush's Memex](https://en.wikipedia.org/wiki/Memex), where the unsolved part was exactly who would do the maintenance.

What the idea file leaves out is the clock.
The wiki's operations fire when you fire them: you drop a source, the agent ingests it; you ask a question, the agent answers and files the answer back.
The wiki compounds, but only when you feed it.
Continuous research is the same artifact with the human trigger removed: the loop finds the new sources on a schedule, advances the checkpoint, and ingest stops being a thing you remember to do.

The implementation side is converging too.
[llm-wiki](https://llm-wiki.net/), a plugin for Claude Code, Codex, and OpenCode built on the pattern, ships parallel research runs, a librarian pass that scores articles for staleness, and an audit that traces outputs back to raw sources.
Even there the runs are invocation-driven: the librarian can tell you the wiki has gone stale, but a human still decides to refresh it, and watched-source variants are being worked out in the idea file's comment thread.
**The wiki gives research a place to accumulate, and the loop gives it a reason to stay current; neither half works alone.**

## This Does Not Contradict Pull-Based Learning

In [Keeping Up With AI Is a Losing Strategy](../keeping-up-with-ai/index.md) I argued that you should consume information on demand, when a real task requires it, instead of on a schedule driven by fear.
Continuous research does not reverse that position.
It removes the reason the position was painful.

The asymmetry that made keeping up impossible was that production compounds while your reading speed does not.
Continuous research moves the consumption to a system whose reading speed does scale.
**The agent keeps up so that you can consume on demand.**

Your behavior barely changes.
When a task arrives that touches a topic you track, you open the brief and read the current state, prepared in advance by something that reads at machine speed.
You are still pulling.
What changed is that the thing you pull from is your curated, current base instead of the raw web on a deadline.

The reading you do take on is bounded and small: the weekly diff, a screen or two of what actually moved.
That is a digest you would pay for, and here it is a free byproduct of the loop.

## What Goes Wrong

The failure modes are the ones every autonomous system grows, plus one that is specific to durable documents.

**A hallucination filed into the knowledge base is worse than one in a chat window.**
A wrong claim in a conversation scrolls away.
A wrong claim in a maintained document accumulates authority every day it survives, and every later run that reads the brief inherits it.
The defenses are mechanical: every claim carries a link, every link is verified by the run that writes it, sources are snapshotted, and anything you intend to act on gets spot-checked by you.
OpenAI itself warns that deep research outputs [hallucinate](https://en.wikipedia.org/wiki/Deep_research), and outside reviewers note that verifying a generated analysis can itself take hours; in a continuous system that verification is amortized across runs and spent on the diff, not the whole report.

**Topic rot.**
A topic file written last year encodes last year's questions.
The tracker keeps diligently researching things you no longer care about, because caring is not an event the scheduler can see.
The defense is treating the topic list like a backlog: prune it on a schedule, and treat a brief you have not read the diff of in a month as a candidate for deletion.

**Hoarding.**
A knowledge base that grows faster than you read it is procrastination with extra steps.
The question to ask is blunt: what is the value of keeping a knowledge base whose content you never consume?
None, because the value of the base is realized when you read it, not when the agent maintains it.
An unread topic is all cost, compute, diff noise, and the illusion of being informed.
If the diff sits unread for four consecutive weeks, the topic is not informing decisions and should be cut, exactly the discipline a reading funnel demands.

**Cost runaway.**
An autonomous web-browsing loop on a timer is a direct line from "it seemed useful" to a surprising invoice.
The budget belongs in the loop's frontmatter, with a cap on runs per day and cost per run, and the runtime should enforce it rather than warn about it.
This is the same argument as the budget field in [Loops as Files](../loops-as-files/index.md), with the stakes unchanged.

## The Bottleneck Moves to Topic Selection

Once the finding, reading, and filing are automated, the constraint moves, in the way [The Shifting Bottleneck](../the-shifting-bottleneck/index.md) describes for every other layer agents absorb.
Deciding what to track becomes the bottleneck, and it is the most human layer of the whole stack.

A topic file is a small statement of identity: these are the questions I need current answers to, these are the sources I trust.
That is editorial judgment, and it is the part that compounds.
The agent will never be better than your topic file at knowing what matters to you, which means the file deserves the same care you would give a skill you plan to run for years.

The practical corollary: start with topics that inform decisions you actually make, where staleness has recently cost you something.
Tracking "large language models" is unusably broad and will produce mush.
Tracking "context window pricing across providers, monthly" produces a brief you will open before every infrastructure decision.

## What to Do Next

Pick one topic that decays quickly and that a real, recurring decision depends on.
Write its topic file: scope, questions, canonical sources, and what a meaningful change looks like.
Create the directory, with a brief, a log, and a snapshots folder, and seed the brief with one deep research run you verify by hand.
Schedule a weekly loop with a budget, and have each run advance the checkpoint, update the brief, and commit the diff.
Read only the diff.

Then leave it alone for a month.
If the diffs were worth the minute they took to read, add the second topic.
If they were not, the experiment cost you one directory and a few dollars of API spend, and you learned where your real information needs are, more cheaply than any course could have taught you.

The goal is not a bigger pile of reports.
**The goal is never having to research anything from zero again.**

## See also

- [Keeping Up With AI Is a Losing Strategy](../keeping-up-with-ai/index.md) - the pull-based consumption strategy this article extends: the agent keeps up so you can consume on demand
- [Loops as Files](../loops-as-files/index.md) - the scheduling format a research loop is written in, including the budget frontmatter that keeps the loop affordable
- [The Shifting Bottleneck](../the-shifting-bottleneck/index.md) - the constraint-moving pattern that puts topic selection at the top of the research stack
- [Managing Many Concurrent LLM Agent Sessions](../managing-many-llm-agent-sessions/index.md) - the per-run state file and digest patterns that make multiple research loops supervisable

## References

- [ChatGPT Deep Research](https://en.wikipedia.org/wiki/Deep_research) - what one-shot deep research concretely is: autonomous 5-30 minute browsing runs, monthly query quotas, and the vendor's own hallucination warnings
- [Anthropic, "Claude takes research to new places"](https://www.anthropic.com/news/research) - the agentic multi-search, citation-backed research model, and its scope limits per query
- [Shi et al., "Deep Research: A Systematic Survey"](https://arxiv.org/abs/2512.02038) - the four-component decomposition (planning, acquisition, memory, generation) that shows exactly where continuity is missing
- [Claude Code documentation, "Scheduled tasks"](https://code.claude.com/docs/en/scheduled-tasks) - evidence that the scheduling primitive for agent loops already ships in mainstream tooling
- [Karpathy, "LLM Wiki"](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) - the idea file that named the artifact half of the pattern: compile knowledge once into an LLM-maintained wiki, plus the maintenance-economics argument
- [llm-wiki](https://llm-wiki.net/) - a productionized version of the LLM Wiki pattern for Claude Code, Codex, and OpenCode, including the librarian staleness pass and provenance audit
- [Wikipedia, "Memex"](https://en.wikipedia.org/wiki/Memex) - Vannevar Bush's 1945 vision of a personal, curated knowledge store, the pattern's oldest ancestor
- [arXiv usage statistics](https://arxiv.org/help/stats) - the production side of the asymmetry: why one-shot research cannot keep up with the volume of new material
