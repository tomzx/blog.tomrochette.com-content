---
title: "Context Management Patterns"
created: 2026-08-24
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, context-management, coding-agents, context-engineering]
readability: 3
audience_notes: >
  Engineers who drive terminal coding agents daily and want sessions that stay sharp on large codebases and long tasks.
  Assumes you know what a token budget is and have watched an agent degrade after its window filled.
---

This is a maintained guide to the patterns that fit large codebases and long tasks into agent context windows: selective loading, packing, retrieval, compaction, and memory files.
Everything below was verified against harness documentation and primary sources on 2026-08-24; when the tools move, this page moves with them.

**Every working pattern does one thing, it keeps the window small and fresh, and in 2026 the harness-native features (compaction, subagents, memory files) deliver more of that value than any retrieval pipeline you can buy.**
My disagreeable claim: below a few hundred thousand lines of code, a short memory file plus automatic compaction beats a bespoke RAG stack, and teams buying context engines before learning their harness's `/compact` are paying money to avoid learning a skill.
The corpus has long argued that [context quality dominates model choice](../../the-importance-of-context-when-interacting-with-llms/index.md); this page is the operational version of that argument.

## The problem is attention, not tokens

**The window is finite, but the binding constraint is attention: recall drops as context grows, and it drops worst in the middle.**
The [lost in the middle](https://arxiv.org/abs/2307.03172) result showed models recall information best at the beginning or end of long inputs and significantly worse in the middle, even for explicitly long-context models.
Anthropic's own engineering post names the phenomenon context rot and treats every token as drawing down a finite attention budget.
[Claude Code](../claude-code/index.md)'s documentation states it plainly: performance degrades as the window fills, and "the context window is the most important resource to manage".
The window also fills before you say anything: the [model selection guide](../model-selection-for-coding-tasks/index.md) records harness baselines of about 33k input tokens (Claude Code) versus about 7k (OpenCode) on a minimal task, so a heavy harness taxes every pattern below.
A bigger window does not escape this, it spreads the same attention over more tokens, which is why the patterns exist at every window size.

## Load identifiers, not contents

**The strongest pattern keeps lightweight pointers in context (paths, symbols, queries) and pulls contents just in time.**
Anthropic calls this just-in-time context: agents hold references and load data at runtime through tools, the way Claude Code analyzes large data with `head` and `tail` instead of loading whole files.
Every harness ships the manual version: `@` file references in [Claude Code](../claude-code/index.md) and [OpenCode](../opencode/index.md) inject one named file on demand, and OpenCode's `!` prefix injects a shell command's output into the prompt.
[aider](../aider/index.md) is the purest expression of the family: its tree-sitter repo map ranks symbols by graph references into a roughly 1k-token budget, so the model sees the codebase's skeleton and fetches bodies only when needed (see the [tree-sitter chunking](../tree-sitter-chunking/index.md) note).
The field is consolidating here: the [semantic code search](../semantic-code-search/index.md) note records pioneers replacing local embeddings indexes with agentic grep loops, because grep is always current and an index is not.

## Firewall noisy work into subagents

**Exploration is the biggest context consumer, so run it in a window you throw away.**
Claude Code's docs recommend delegating investigation to subagents, which read files in their own context window and return only a summary; OpenCode does the same with custom commands that force `subtask: true` so output never pollutes the primary session.
Anthropic quantifies the pattern: a subagent may burn tens of thousands of tokens exploring but returns a 1,000 to 2,000 token distilled summary.
This is also how you keep retrieval cheap: an Explore-style subagent can grep aggressively because the misses cost its own window, not yours.
The failure mode to avoid is unscoped investigation in the main session, which Claude Code's own docs list as a named anti-pattern ("the infinite exploration").

## Packing and chunking: measure dumb before buying clever

**Whole-repo packing is legitimate but linear, so it is a budget decision, not a default.**
[Repomix](../repomix/index.md) packs a repo into one file with exact token counts and a `--token-budget` flag that fails CI, which makes "just give it everything" a measured choice rather than an accident.
Its limits are recorded in the note: spend grows linearly, attention is weakest exactly in the middle regions where the pack puts most content, and the tree-sitter `--compress` mode is experimental and lossy by design.
If you chunk for a vector store instead, the [tree-sitter chunking](../tree-sitter-chunking/index.md) note records practitioners ranking truncation and fixed-length splits above AST chunking, because 16k-token embedding models fit most whole files.
Framework machinery exists (LlamaIndex's `CodeSplitter`, see the [LlamaIndex](../llamaindex/index.md) note) but its own makers pivoted elsewhere, and the tools that shipped code retrieval built it by hand or stripped it back out.

## Indexed retrieval pays only past a threshold

**Retrieval infrastructure is an enterprise-scale pattern, and the strongest evidence for that comes from the vendors selling it.**
The [Sourcegraph](../sourcegraph-code-context/index.md) note records their CodeScaleBench data: a +0.259 reward delta for code intelligence in the 400K to 2M LOC range, but a -0.080 delta below 400K, meaning their own tools slightly hurt agents on most repositories, behind a $16K floor.
[Augment Code](../augment-code/index.md) makes the strongest counter-case, retrieval-first agents at 33% lower token spend at matched quality, and every number is vendor-run, which the note flags as the missing replication.
[Greptile](../greptile/index.md) applies the same graph-index idea to review, with the caveat that its index is post-commit and never sees your working tree.
When you do cross the threshold, delivery is settled: an MCP server (Sourcegraph's works with Claude Code, Codex, Cursor, and Amp) feeds the index to whichever harness you already run.

## Compaction is a default you should steer

**Summarize-and-restart has shipped as a harness default, and its lossiness is steerable if you bother steering it.**
Claude Code auto-compacts as you approach the limit, and Anthropic documents what survives: architectural decisions, unresolved bugs, key implementation details, and the five most recently accessed files.
All three major harnesses expose it manually: `/compact <instructions>` in Claude Code (for example, "focus on the API changes"), `/compact` in [Codex](../codex/index.md) (with `/status` showing context usage), and `/compact`, aliased `/summarize`, in [OpenCode](../opencode/index.md).
Claude Code goes further than most: the rewind menu summarizes from or up to a chosen checkpoint, and `/btw` answers side questions that never enter history at all, the same idea as Codex's `/side`.
The steering mechanism most engineers miss: put compaction directives in the memory file ("when compacting, always preserve the modified-file list and test commands"), which turns a lossy default into a controlled one.
Augment's rebuild, recorded in its note, runs proactive compaction on a cheaper model and measured 53% lower cost per task, so compaction is also a cost lever, not only a capacity lever.
The caution is real: Anthropic warns overly aggressive compaction loses subtle context whose importance shows up later, which is the argument for files.

## Files outlive sessions

**Anything you need after a compaction should already be on disk, because files are the only layer that survives restarts, compactions, and vendor switches.**
Anthropic calls this structured note-taking: the agent writes NOTES.md-style files outside the window and reads them back later, which is how agents maintain coherence across hours.
The shipped version is the memory file: CLAUDE.md, AGENTS.md, and GEMINI.md load every session, and Claude Code's `/init` and OpenCode's `/init` scaffold them.
Their documentation also carries the warning worth repeating: bloated memory files cause the model to ignore your actual instructions, so prune ruthlessly and move rarely-needed knowledge into on-demand skills.
The frontier is automating the capture: Gemini CLI's Auto Memory (experimental) mines idle past sessions for durable facts and proposes memory patches and skill drafts into a review inbox, applying nothing without approval (see the [Gemini CLI](../gemini-cli/index.md) note for that harness's status).
I treat review-gated capture as the correct design: unreviewed auto-memory is how a wrong summary becomes a permanent fact.

## A workflow that composes the patterns

**Compose by phase: files for what persists, search for what changes, subagents for what is noisy, compaction for what is finished.**

- Keep a short memory file (under a page) with commands, conventions, and landmines; everything else loads on demand.
- Start a fresh session per task (`/clear` or OpenCode's `/new`), because a clean window with a better prompt beats a long one full of corrections.
- Let subagents do the exploration and `@`-reference the few files you already know matter.
- Compact at phase boundaries (after exploration, before implementation) with explicit instructions, instead of waiting for the auto-trigger mid-edit.
- Have the agent write durable facts (decisions, found constraints) to a notes file during long tasks, so the next compaction cannot erase them.
- Add an MCP context engine only when you pass the few-hundred-thousand-line threshold, and re-run its benchmark on your own repos first.
- Measure: watch context usage (`/status`, `/context`), and track tokens per merged PR the way the [model selection guide](../model-selection-for-coding-tasks/index.md) argues.

## What changes fast and how to re-verify

**Compaction defaults and memory features are the fastest-moving surfaces in every harness, so every claim here carries a date.**
Gemini CLI's Auto Memory is explicitly experimental and off by default; Claude Code's compaction behavior has changed repeatedly across releases; Augment's efficiency numbers await independent replication.
On each refresh I re-fetch the four harness pages cited below plus the context-engine notes, and I update this page and its date together.
A pattern claim that no longer matches the docs gets deleted, not hedged.

## What to Do Next

- Learn your harness's compact, clear, and subagent commands this week; they are free and you already pay for their absence.
- Add one compaction directive to your memory file naming what must survive summarization, then verify it survives on your next long session.
- Delete half of your memory file today; if behavior does not degrade, it was padding.
- Before buying any context engine, measure your current tokens per task and check your repo against the 400K LOC threshold with your own numbers.
- Try Repomix with `--token-budget` as a CI guard on the whole-repo habits you already have, so at least the dumb pattern is bounded.

## See also

- [Model Selection for Coding Tasks](../model-selection-for-coding-tasks/index.md) - the other half of the economics: why harness overhead moves your bill as much as model choice
- [Repomix](../repomix/index.md) - the packing pattern measured, budgeted, and bounded
- [Augment Code](../augment-code/index.md) - the strongest vendor case that retrieval beats exploration
- [Sourcegraph code context platform](../sourcegraph-code-context/index.md) - the size threshold below which indexed retrieval hurts
- [Semantic code search in coding tools](../semantic-code-search/index.md) - why tools are retreating from indexes toward agentic search

## References

- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents - context rot, attention budgets, compaction mechanics, structured note-taking, sub-agent summaries, just-in-time retrieval
- https://code.claude.com/docs/en/best-practices - Claude Code auto-compaction, /compact with instructions, /clear, /btw, memory-file pruning, compaction directives
- https://developers.openai.com/codex/reference/slash-commands - Codex /compact, /status context usage, and /side
- https://opencode.ai/docs/tui - OpenCode /compact (alias /summarize), /new (alias /clear), and @ file references
- https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/auto-memory.md - Gemini CLI Auto Memory: review-gated extraction of memory patches and skills from past sessions
- https://arxiv.org/abs/2307.03172 - Lost in the Middle: recall degrades for information in the middle of long contexts
