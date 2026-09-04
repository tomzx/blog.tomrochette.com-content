---

title: "Every Decision You Change Pays Once Per File"
created: 2026-08-12
type: post
status: draft
tags: [ai, software-engineering, llm, code-quality, decision-making, scope, productivity, fully-ai-generated, llm=glm-5.2]
readability: 3
audience_notes: >
  Assumes the reader is an engineer or tech lead who uses LLM coding agents and has watched a small project balloon into many generated files whose assumptions drift apart as requirements change. Builds on "When a Closed Decision Reopens" and "The Prompt Is the Source Code" but can be read on its own.
agent_sessions:
  - ses_00aa72b23ffeXhCs4E3aTIxKrP
  - ses_005ec6e29ffeREI2bLD97m5Tfn
---

I was building a project whose requirements were unclear, and the only way to make them clearer was to iterate with my principal.
Each round of conversation produced a slightly sharper version of the vision, and I let an LLM agent turn each version into files.
By the time the vision was finally stable, I had a directory full of files that each encoded a different snapshot of a decision that had since moved.
**The hard part was never generating the files. The hard part was keeping them consistent with each other every time the vision changed, and the agent that made the files cheap to create was the same agent that made them cheap to make inconsistent.**

## The Problem Is Not the File Count, It Is the Surface That Count Creates

It is worth being precise about what actually hurts here, because the obvious diagnosis, "I have too many files," points at the wrong fix.
A large, stable codebase is not a problem.
A large codebase that must all agree on a vision that is still moving is the problem, and the pain is proportional to how many places a single decision is encoded.

Every file the agent produced carried assumptions: the name of the core entity, the contract's fields, which behavior was in scope and which was out, what the principal meant by a word he used loosely in one meeting and differently in the next.
Each of those assumptions was a tiny copy of a decision, pasted into another file, and each copy was a place a future reversal would have to be found and re-applied.
When the principal changed his mind, I did not have one thing to fix.
I had a list, and I did not even know how long the list was, because the copies were scattered through files I had not written and did not fully remember.
**The number of files is not a storage cost, it is a multiplier on the cost of every decision you are still making, and the multiplier is paid in the currency of "find every place the old decision lives and rewrite it."**

This is the classic code smell the industry calls [shotgun surgery](https://en.wikipedia.org/wiki/Shotgun_surgery), one change that forces you to touch many files, except that LLM agents have industrialized the setup.
A human writing carefully tends to centralize a decision before they are willing to repeat it.
An agent happily reproduces the decision, slightly differently, across every file it generates, because it has no memory of having written it anywhere else and no incentive to avoid the duplication.

## Creation Being Cheap Baited Me Into the Expensive Configuration

Here is the part that is easy to miss in the moment, and that I missed.
The agent made file creation nearly free, and free creation felt like progress.
Every file was evidence that the project was getting more real, and it is genuinely pleasant to watch a vision turn into a file tree in an afternoon.

But creation being free does not make change free, and the requirements being unclear guaranteed that change was coming.
I was generating broadly during the one phase of the project where decisions were most likely to reverse, and each broad file I generated was a bet that the decision it encoded would survive the next conversation with the principal.
Most of those bets lost.
**Cheap creation is the trap, because it tempts you to encode a volatile vision into many files before it has settled, and the file count you build during the volatile phase is exactly the surface you will be re-editing for the rest of the project.**

The tools are not malicious here.
They are doing exactly what they are good at, producing files fast.
The mismatch is between what the tool rewards (more files, more surface, more apparent progress) and what the situation rewards (as few encodings of a still-moving decision as possible).
When the requirements are unclear, the situation rewards restraint, and the tool rewards the opposite, and the engineer is the only one in the loop who can notice.

## The Vision Has to Have Somewhere Canonical to Live

The deeper failure underneath all of this is that the vision itself had no home.
It lived in my conversation with the principal, which is to say it lived nowhere durable, and so every file became its own private copy of a thing that had never been written down once, correctly, in one place.

As I argued in [When a Closed Decision Reopens](../when-a-closed-decision-reopens/index.md), a decision that exists only in the heads of the people who were in the room has a half-life, and the half-life is exactly as long as it takes for the next conversation to start.
My files were not inconsistent because the agent was careless.
They were inconsistent because they were all trying to reconstruct a vision from memory, and memory drifts between files the same way it drifts between people.
**You cannot keep many files consistent with a vision that has no canonical form, because there is nothing for them to be consistent with, so the first move is always to give the vision one.**

## A Few Ways to Deal With It

None of these remove the underlying fact that unclear requirements mean changing decisions.
They change the cost of a change from "hunt through every file" to something bounded and mechanical, and most of the relief comes from the first two.

### Shrink the surface with a single source of truth

The highest-leverage move is to ensure that each fact about the vision lives in exactly one canonical place, and that every file either references that place or is derived from it.
A decision that is encoded once costs one edit to change.
A decision that is copied into twenty files costs up to twenty edits, plus the search to find the twenty, plus the risk that you miss the twenty-first.
**The multiplier on change cost is literally the number of independent copies, so driving that number toward one is the thing that matters.**

In practice this means a specification, a set of decision records, a domain model, whatever container holds the statements the rest of the project depends on, and the discipline to stop re-stating those statements inline wherever they are used.
[Don't repeat yourself](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) is an old principle for exactly this reason, and [single source of truth](https://en.wikipedia.org/wiki/Single_source_of_truth) is its organizational form: the duplication is not a style problem, it is a change-cost problem, and the change cost is what is hurting you.

### Write every decision down the moment it changes, with the principal

You cannot propagate a change from a decision you cannot pin down, and a verbal decision in a moving conversation is a decision you cannot pin down.
Each iteration with the principal should produce a dated, written record: what we decided, what we ruled out, what it depends on, and what would have to become true for it to change again.
This is the [Architecture Decision Record](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) discipline applied to scope, and it turns the principal's shifting enthusiasm into an artifact you can actually align files to.

This is the upstream fix for the consistency problem.
If the canonical decision exists and is current, then keeping the files consistent is a matter of pointing them at it.
If it does not exist, you are reconciling files against a memory of a conversation, and no amount of tooling will make that reliable, because the source of truth is decaying in your head between meetings.

### Generate as little as possible while the vision is still volatile

The counterintuitive move, given that the agent makes it so easy to generate, is to generate the least you can get away with during the phase where decisions are still moving.
Build the thinnest thing that lets the principal react, a prototype, a single file, a sketch on a page, and resist encoding the vision into a broad file tree until the decisions behind it have started to hold.
As [The Shifting Bottleneck](../the-shifting-bottleneck/index.md) argues, once implementation becomes cheap, the hard work moves upstream into deciding what to implement, and during unclear requirements that upstream work is nowhere near done.

The goal is not to avoid files forever.
It is to defer the broad generation until the decision it encodes is stable, so that the file count multiplies a decision you will keep rather than one you are about to throw away.
Every file you do not generate during the volatile phase is a file you do not have to hunt down and rewrite when the next conversation moves the target.

### Separate what is stable from what is volatile, and concentrate the volatile

Not every part of the vision moves at the same speed.
The domain entities, the invariants, the core nouns, these tend to settle early and stay settled.
The scope, the API details, the behavior at the edges, these are what the principal keeps renegotiating.
If you can tell the two apart, put the volatile facts in as few files as possible and let the stable facts be the broad part of the codebase.

Then a change touches the small set of volatile files instead of rippling through the large set of stable ones, and the cost of a reversal shrinks to the size of the thing that actually changed.
This is the same insight as [connascence](https://en.wikipedia.org/wiki/Connascence), the idea that the cost of a change is a function of how many things must change with it and how tightly they are coupled: you are deliberately arranging the project so that the things that change together live together, and the things that change often are few.

### Make the propagation mechanical, not something you remember

Once a decision has a canonical home, a human should not be the thing that remembers which files depend on it.
Humans miss files, and missing one is precisely how the vision goes inconsistent without anyone noticing.

What actually worked for me was making the agent track its own dependencies.
I asked it to maintain a file that recorded, for every file it generated, which other files that file was built on.
When a canonical file changed, the agent did not have to guess what to re-check; it read the manifest, found every file that depended on the one that moved, and walked through them in turn to re-establish consistency.
The job of "find every place the old decision lives" turned from a memory task into a [dependency graph](https://en.wikipedia.org/wiki/Dependency_graph) traversal, and the graph was written down instead of living in my head.
This is the file-count multiplier from earlier, but turned to my advantage: the same surface that made change expensive when I had to hunt it by memory made change cheap once the edges between files were recorded.

**The principle is that the correction should be automatic or at least alarmed, never remembered.**
A dependency manifest is one form of it; a script that regenerates derived files from the source of truth is another, and either works as long as the list of dependents is recorded rather than recalled.
If keeping the files consistent depends on me remembering the full list of places a decision lives, then the project is one tired afternoon away from quiet inconsistency, and the whole point was to stop depending on my memory.

## What I Would Do Differently

If I ran this project again, I would change the order of operations, and most of the pain would not happen.
I would write the vision down in one place before I generated a broad file tree, and I would treat every conversation with the principal as producing a written decision record rather than a vibe to carry forward.
I would keep the representation small and rough-edged while the decisions were still moving, and I would not let the agent spin out a full project structure until the decisions behind it had stopped reversing.
And I would, from the first generated file, have the agent record what each file was built on, so that a change started in one place and propagated along recorded edges rather than by me hunting through a tree I could not fully remember.

The lesson I take from it is narrow and specific.
**When the requirements are unclear and the decisions are still being negotiated, the cheapest file to maintain is the one you did not generate yet, and the most expensive thing you can do is let a fast agent encode a moving vision into many files before it has settled.**
The agent makes creation nearly free, and that is real, but change is not free, and unclear requirements guarantee that change is coming.
Treat the file count during the volatile phase as a liability, not a trophy, because every file you generate then is a place you will pay the next time the principal changes his mind.

## See also

- [When a Closed Decision Reopens](../when-a-closed-decision-reopens/index.md) - the same decision-durability argument (a verbal decision has a short half-life) applied to scope negotiations, and the case for writing every decision down the moment it is made
- [The Prompt Is the Source Code](../the-prompt-is-the-source-code/index.md) - why intent must travel with the files that encode it; here the point is that without a canonical intent, every file drifts toward its own private version of the vision
- [The Shifting Bottleneck](../the-shifting-bottleneck/index.md) - once implementation is cheap, the hard work moves upstream into deciding what to build, which is exactly the phase where broad generation is most dangerous
- [The Foundation Predicts the House of Cards](../the-foundation-predicts-the-house-of-cards/index.md) - specification discipline as the highest-leverage capability, and why generating broadly on an unstable foundation multiplies the cards
- [The Importance of Context When Interacting with LLMs](../the-importance-of-context-when-interacting-with-llms/index.md) - the codebase as the model's context; inconsistent files are bad context, and the agent faithfully extends the inconsistency

## References

- [Wikipedia, "Shotgun surgery"](https://en.wikipedia.org/wiki/Shotgun_surgery) - the code smell this article describes: one change that forces you to touch many scattered files, which LLM agents industrialize by default
- [Wikipedia, "Single source of truth"](https://en.wikipedia.org/wiki/Single_source_of_truth) - the structural remedy of giving each fact about the vision exactly one canonical home, so a change costs one edit instead of many
- [Wikipedia, "Don't repeat yourself"](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) - the older name for the same principle, framed here as a change-cost argument rather than a style preference
- [Michael Nygard, "Documenting Architecture Decisions"](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) - the Architecture Decision Record format, applied here to the decisions negotiated with the principal so they become durable artifacts instead of memories
- [Wikipedia, "Connascence"](https://en.wikipedia.org/wiki/Connascence) - the framework for why change propagates and at what cost, which underlies the advice to concentrate the volatile parts of the vision in as few files as possible
- [Wikipedia, "Dependency graph"](https://en.wikipedia.org/wiki/Dependency_graph) - the structure behind the manifest approach, turning "which files must I re-check" from a memory task into a recorded graph the agent can walk
