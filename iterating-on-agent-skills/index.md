---
title: "Iterating on Agent Skills: The Loop That Keeps Them Improving"
created: 2026-08-16
type: post
status: draft
tags: [ai, llm, agent-skills, workflow, skills, software-engineering, fully-ai-generated, llm=glm-5.2]
readability: 3
audience_notes: >
  Assumes the reader already writes or maintains agent skills (a SKILL.md or similar) inside a coding agent like OpenCode, Cursor, or Claude Code, and has shipped at least one skill they no longer touch. No introduction to what an LLM is or what a skill is.
---

A skill file is not done when it ships.
The first version of a `SKILL.md` is a hypothesis: that this sequence of steps, sent to a model, will produce the result you want.
Hypotheses get tested every time the agent runs, and most hypotheses fail in small ways you only notice on the fifth or tenth run.
**A skill is a depreciating asset, and the only thing that keeps it paying off is a deliberate loop you run on it after it ships: notice the failure, explain what happened to a fresh agent session, iterate with the agent on a patch, verify the patch, and periodically shrink the whole library back down.**

The rest of this piece is that loop, in the order I run it.

## Why skills decay

Three forces pull at a skill from the day you write it, and any one of them is enough to make a good skill go stale.

The model changes underneath it.
A skill that was necessary to spell out every step for last year's model is over-specified for this year's model, and the over-specification starts to fight the model instead of helping it.

The task drifts.
The repo layout moves, the tool's CLI changes, the team's convention evolves, and the skill keeps calling the old path.

And your own understanding improves.
Six months after writing the skill, you know a shorter, cleaner way to express the same instruction, but the file still holds the first, clunkier version.

**A skill that nobody touches is a skill that is quietly getting worse, because the world around it is not standing still.**

[Keeping Up With AI Is a Losing Strategy](../keeping-up-with-ai/index.md) makes the same argument about filters: the asset you built at the last model generation may be miscalibrated for the current generation, and you will not notice because the failure is silent.
Skills fail silently the same way.
The agent still produces output.
The output is just a little more wrong, a little more verbose, a little more off, and you compensate for the drift in your head without ever feeding the fix back into the file.

## The loop

I run the same five-step loop on every skill, whether I noticed a failure today or I am doing a monthly sweep.
The order matters, because each step is cheap only if the previous step ran.

My part of the loop is the noticing and the judgment.
The diagnosing and the patching belong to the agent, and the split is the point: I explain, the agent analyzes, and the skill gets fixed without me becoming the bottleneck the loop exists to remove.

### 1. Notice the failure

A skill only improves when one of its failures gets explained, and most failures never get explained.

The default behavior after a bad run is to fix the output by hand, move on, and forget the skill was ever wrong.
The hand fix is the failure mode, because the next run will produce the same bad output the same way, and you will apply another hand fix.

I do not keep failure notes, and I do not stop to work out what went wrong.
When the agent produces something I have to correct, I open a new agent session and explain what happened: the bad output, what I expected instead, and which skill produced the run.
The explanation is the whole capture.
Explaining takes a minute, needs no template, and the session holds the failure so my head does not have to.

**The rule is simple: if I had to correct the output, the skill has to hear about the correction.**

The rule is the encoding loop from [My AI Workflow](../my-ai-workflow/index.md) turned outward.
There, the rule was that every time I caught myself remembering to do something, the reminder became a skill.
Here, the rule is that every time I catch myself correcting the agent, the correction becomes a session about the skill that produced the output.
Both rules turn a private, forgettable moment into a durable, improvable artifact.

### 2. Explain it to a fresh session

The session has to be new, and the newness is doing real work.
The session that produced the bad output is the worst investigator of the bad output, because the agent in that session is attached to the reasoning that went wrong.
A fresh session reads the skill the way a new maintainer would, with no stake in the run that failed.

My message states what happened, not why.
The bad output, what I expected instead, and anything about the run that surprised me.
Then I let the session read the skill and tell me what went wrong, and the diagnosis lands on one of a handful of causes.

The skill was missing context the model needed.
It referenced a file that was not in scope, or assumed a convention that was never stated.

The skill was over-specified.
It pinned a step-by-step recipe that the current model does better on its own, and the pin is now producing worse output than letting go.

The skill was ambiguous.
Two reasonable readings of the same instruction exist, and the model picked the wrong reading.

The skill called the wrong tool, or called the right tool the wrong way.

Or the failure was not the skill at all.
The model was weaker than the skill assumed, the input was bad, or I asked for the wrong thing.

The diagnosis matters because each cause gets a different patch.
Missing context gets added.
Over-specification gets cut.
Ambiguity gets rewritten with one clear reading.
A wrong tool call gets corrected.
And a failure that is not the skill's fault gets parked, not patched, because editing a skill to compensate for a bad input is how skills accumulate defensive cruft they do not need.

**Most skill decay is over-specification, not under-specification, and the instinct to add more instructions is usually wrong.**
The model is almost always more capable than the day the skill was written, and the smallest patch that fixes the failure class is very often a deletion.

### 3. Iterate to a patch

The agent writes the patch, and I iterate with the agent until the patch is right.
My job in the session is judgment, not authorship: keep the patch aimed at the failure class, and keep the patch small.

The patch edits the `SKILL.md`, not the output.

The discipline is to patch the failure class, not the failing instance.
A patch that fixes one bad run without addressing the kind of bad run is a patch that will be re-applied, in a different form, to the next bad run, and to the bad run after that.
The skill accumulates special cases and never gets cleaner.

Each iteration should end with a smaller diff, not a bigger one.
Add the one missing piece of context.
Rewrite the one ambiguous sentence.
Delete the step the model now does on its own.
A small patch is easy to review and easy to revert if the patch makes things worse; a large patch that tries to fix the skill end to end is almost always a sign the diagnosis was incomplete.

**The patch is also where the skill gets shorter, not just longer.**
If the session cannot make the failing skill better without also making the skill longer, the session is probably patching a symptom.

### 4. Verify

A patched skill is another hypothesis, and a hypothesis that is not tested is a guess.

The cheapest verification is to re-run the skill against the run that failed, and to read the new output for the specific problem the session was asked to fix.
If the explanation captured the failure well, the check takes a minute.

For skills whose output can render, the pattern from [Teach Your Agent Skills to Use Tools That Render](../agent-skills-that-render/index.md) pays for itself here.
A skill that emits a diagram, a table, or a diff is a skill I can verify by looking, and looking stays cheap when reading the prose would bury me.
A skill that emits only paragraphs is a skill I can only verify by reading, and reading is the bottleneck that started the whole problem.

For skills that touch code, the verification runs the project's own checks.
The linter, the type checker, the test suite.
The skill does not need its own separate verification when the repository already runs these checks, the same way [The Codebase Gardener](../the-codebase-gardener/index.md) leans on objective signals from the tools rather than on a human re-reading every diff.

**A skill without a verification step is a skill that drifts back to broken the moment you stop looking.**

### 5. Shrink or delete

Shrink-or-delete is the step most people skip, and also the step that matters most over the long run.

Every skill is a bet that the model cannot do the task reliably on its own.
The models keep getting better.
The bet that was correct when the skill was written is incorrect now for some percentage of the library, and that percentage grows every model generation.

When a skill's failures have stopped, and the agent produces the right output from a prompt alone, the skill is no longer carrying its weight.
The skill is scaffolding around a capability the model now holds on its own, and the right move is to take the scaffolding down, not maintain the skill.

[My AI Workflow](../my-ai-workflow/index.md) makes the same argument: the skills are a temporary scaffold for the gap between what the model can do today and what the model will do on its own tomorrow, and a good chunk of the work is knowing which scaffold to take down next.

Shrinking applies within a single skill too.
A step that the model now does reliably on its own is a step that should leave.
An instruction that only existed to work around an old model limitation is an instruction whose time is up.
A skill that has not been shortened in six months is almost certainly carrying dead weight from a weaker model generation.

**Deletion is not loss.
Deletion is the most positive outcome a skill can have, because deletion means the model grew into the capability the skill was propping up.**

## The review sweep

One failure at a time is too slow a pace to keep a library healthy, the same way one pull request at a time is too slow a pace to keep a codebase clean.

I run a periodic sweep over the whole library, the same way [The Codebase Gardener](../the-codebase-gardener/index.md) describes raking a codebase instead of chasing every leaf.
**The sweep is a small set of questions asked of every skill, not the deep rewrite of any one skill.**

Which skills have I not edited in three months?
Skills untouched for three months are the most likely to have decayed, because the world moved and the skill did not.

Which skills reference files, tools, or paths that no longer exist?
Broken references are the cheapest bug to find and fix.

Which skills overlap with each other?
Two skills that do almost the same thing should become one, because the duplication will drift and one will go stale while the other gets maintained.

Which skills did I not run at all this month?
A skill that is never invoked is either redundant or forgotten, and both states are reasons to consider deletion.

Which skills did I run but correct every time?
Skills that need correcting every run are the candidates for the next session.

A sweep takes an hour and pays for a quarter, because each finding is an iteration the per-failure loop would have taken months to surface.

## Skills about skills

The loop has a recursive quality worth naming, because the recursion is where the compounding really lives.

The act of iterating on a skill is itself a repeatable task, and repeatable tasks become skills.
I run a `review-skills` pass that does the sweep described above.
I run an `improve-skill` pass that takes a single skill and proposes high-value, low-risk patches to the skill.
The failure session from step 2 is the same move, held by hand: I supply the failure and the judgment, the agent supplies the analysis and the patch.

The recursion is the real multiplier.
**Once the iteration loop is itself a skill, the library improves itself at the pace the agent can run, not the pace I can read.**
I still make the calls, because deciding which patch lands and which skill gets deleted is a judgment the model does not yet make well.
But the surface I have to hold in my head shrinks every time an iteration step is encoded, and the part I do myself narrows to the genuinely judgment-laden calls.

The end state matches what [The Self-Evolving Repository](../the-self-evolving-repository/index.md) describes for codebases, applied one layer up: a library of skills that observes its own failures, proposes its own patches, and shrinks itself as the model grows, with the human left only at the checkpoint that needs taste.

## What to Do Next

Pick one skill you have already run more than five times.
Find the last run where you corrected the output.
Open a new agent session, paste the bad output, and explain what you expected instead.
You have just run steps 1 and 2 of the loop.

Then let the session read the skill and propose the diagnosis: missing context, over-specification, ambiguity, or the wrong tool call.
Push the session until the patch is small and makes the skill shorter, and re-run the skill against the run that failed.
You have just run steps 3 and 4.

If you cannot remember the last time a skill failed, you are either very lucky or, more likely, you have stopped noticing.
Run a sweep instead.
Open every skill, ask when the skill was last edited, and assume anything over three months old has decayed.
You will be right more often than not.

And every quarter, ask which skills you can delete.
The library that only grows is the library that is losing, because the library is carrying scaffolding for problems the model has already solved.

**The goal is not a large library.
The goal is a small library that is exactly the size of the gap between the model and the work, and a library that shrinks every time the model catches up.**

## See also

- [My AI Workflow: The Skills Are the Part That Compounds](../my-ai-workflow/index.md) - the case that skills are the durable asset, and the encoding loop this piece turns outward onto the skills themselves
- [Teach Your Agent Skills to Use Tools That Render](../agent-skills-that-render/index.md) - the verification step of the loop, made cheap by rendering output instead of writing more prose
- [The Codebase Gardener](../the-codebase-gardener/index.md) - the sweep pattern, applied there to a codebase and here to the skill library
- [The Self-Evolving Repository](../the-self-evolving-repository/index.md) - the end state when the iteration loop on skills is itself automated
- [Keeping Up With AI Is a Losing Strategy](../keeping-up-with-ai/index.md) - the argument that any filter built at one model generation must be re-audited, which is exactly what the skill sweep does

## References

- [tomzx/agents](https://github.com/tomzx/agents) - the skills library this loop is run against, including the `review-skills` and `improve-skill` passes that operationalize the sweep and the patch
- [Agent Skills format](https://agentskills.io) - the open skill format that makes each skill small enough to iterate on independently
