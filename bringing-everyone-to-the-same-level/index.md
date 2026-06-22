---
title: "Bringing Everyone to the Same Level: How Skills and LLMs Collapse Code Quality Variance"
created: 2026-06-17
type: post
status: finished
tags: [ai, software-engineering, llm, skills, productivity, fully-ai-generated, llm=glm-5.2]
readability: 3
audience_notes: >
  Assumes the reader is already using an LLM coding agent (opencode, Claude Code, Cursor) and has at least seen a "skill" or "rule" file. No explanation of what an LLM is.
---

Every team has the same shape.
A few engineers ship clean, well-tested, well-scoped work, and the rest ship work that mostly works.
The gap between them is not typing speed.
It is everything that happens before and after the typing: the steps they remember to run, the checks they know to perform, the conventions they have internalized through years of scar tissue.
**That knowledge has always been the real asset, and it has never scaled, because it lived inside a small number of heads.**

LLMs alone do not fix this.
They make everyone faster, which is a different thing from making everyone produce the same quality.
Done naively, they widen the variance, because an LLM is a multiplier on the quality of the instructions it receives.
The fix is to give every engineer, and every model, the same instructions.
That is what a skill is, and it is why skills are the mechanism that finally brings everyone to the same level.

## The Variance Problem Has Always Been a Knowledge Problem

Ask yourself what actually separates the output of your strongest engineer from your weakest.
It is rarely the language syntax.
Both of them can write a function.

The difference is that the strong engineer, before touching code, does a long list of invisible things.
They look for an existing solution before building a new one.
They write down what "done" means before they implement.
They check whether the change can be undone.
They name things the way the rest of the codebase names things.
They write the edge case the junior would have forgotten.
They run the linter, and they run it before opening the pull request, not after a reviewer asks.

Each of these is a step, and a step can be written down.
For most of the history of software, these steps were transmitted by osmosis.
You learned them by pairing with someone better, by getting review comments on your seventh PR, by breaking production once and remembering forever.
This is mentorship, and it works, but it is slow, expensive, and uneven.
It cannot keep up with a team that is hiring, and it cannot keep up with a codebase that is changing.
**The senior engineer's edge was always a process they ran in their head, and a process in a head does not scale.**

## LLMs Raise the Floor but Not the Ceiling

Drop an LLM into this situation and the naive expectation is that it levels the field.
It does not, at least not on its own.

What an LLM actually does is amplify whatever it is given.
Give it a vague one-line prompt and you get back plausible, generic code that does not match your conventions and forgets your edge cases.
Give it a precise specification, the relevant files, the patterns to reuse, and the checks to satisfy, and you get back code that is hard to distinguish from your best engineer's output.
The model is the same in both cases.
The difference is entirely in the context, which, as I argued in [The Importance of Context When Interacting with LLMs](../the-importance-of-context-when-interacting-with-llms/index.md), is the entire mechanism by which a frozen set of weights produces behavior relevant to your situation.

This has an uncomfortable implication.
**Before skills, the LLM made the senior engineer better and the junior engineer faster, and the gap between them stayed roughly the same.**
The senior engineer instinctively provides the context the model needs, because they know what good work requires.
The junior engineer does not know what they do not know, so they ask for less, and they get less back.
The tool that was supposed to democratize quality quietly reproduced the existing hierarchy, because it rewarded the same hidden knowledge that always did.

## A Skill Is the Senior Engineer's Process, Made Executable

A skill is a versioned file, usually markdown, that tells an LLM agent exactly how to perform a task.
Not a vague hint.
The steps, in order, the checks to run before declaring success, the gates the output must pass, and the format the output should take.
When the agent loads the skill, it stops improvising and follows the encoded process instead.

This is where the comparison to a human matters.
A junior engineer told to "go implement the feature" forgets half the steps, because they never fully learned them.
A junior engineer, or even an autonomous agent, told to implement the feature *through a skill* cannot forget the steps, because the steps are in the prompt the model reads on every run.
The skill is not advice the engineer might ignore.
It is part of the execution path.

Think of it as [the checklist idea](https://en.wikipedia.org/wiki/The_Checklist_Manifesto) from medicine and aviation, with one critical upgrade.
A surgical checklist still depends on a tired human choosing to read it and choosing to follow it.
A loaded skill does not depend on anyone's discipline.
**The model follows it because the skill is the instruction, and following instructions is what the model does.**

## Why This Collapses the Variance

Run the same task through two engineers with two different LLMs, but the same skill, and watch what happens to the output.
Both implementations start from the same specification step.
Both run the same "have you checked for an existing solution?" step.
Both end at the same verification step, with the same gates.
The code they produce is not identical, but it converges toward a common standard, because the process that produced it is identical.

The thing that used to vary, the invisible checklist inside each engineer's head, is now constant.
What varies is only the judgment applied at each step, and even that is bounded by the gates the skill enforces.
**Skills do not make everyone equally brilliant.
They make everyone equally unable to skip the steps that matter, and skipping the steps that matter is what produced most of the variance in the first place.**

This is the same logic I described, from the other direction, in [Developer Trust Profiles](../developer-trust-profiles/index.md).
There I argued the ideal end state is one where "every contributor, senior engineer or new hire, funnels their work through agents that enforce the same standards," so that authorship stops carrying signal and "the output converges into something homogeneous."
The trust profile was the bridge, and the point was to make itself obsolete.
**Skills are how you actually walk across that bridge.
They are the shared, enforced pipeline that makes the variance shrink in the first place.**

## The Leverage Moves Up, Again

If the junior engineer can now produce work that follows the senior engineer's process, what is left for the senior engineer to do?

The answer is the same one that keeps appearing everywhere AI touches the development pipeline.
The bottleneck moves up the decision chain, as in [The Shifting Bottleneck](../the-shifting-bottleneck/index.md), and the leverage moves with it.

The new seniority is not in running the skills.
Anyone, and any agent, can do that.
The new seniority is in writing them.
Deciding what the process should be in the first place.
Deciding which gate matters and which is theater.
Deciding what "done" means for this kind of task, precisely enough that a model can enforce it.
The judgment that used to be applied privately, one pull request at a time, is now applied once, at the skill level, where it benefits every future execution.

This is why a good skill library is one of the most valuable assets a team can hold.
It is the institutional memory of how the team does things well, written in a form that executes itself instead of sitting in a wiki nobody reads.
When a senior engineer leaves, the skills stay, and the standard stays with them.
When a new engineer joins, they do not spend a year absorbing the conventions through code review.
They load the skills on day one, and their first pull request already follows the team's process.

## What a Skill Has to Get Right to Actually Level the Field

Not every file labeled "skill" collapses the variance.
Most do not.
Writing a skill that genuinely raises everyone to the same level requires a few specific disciplines.

**Encode the steps that are actually forgotten, not the steps everyone already does.**
A skill that says "write clean code" is worthless, because nobody sets out to write dirty code and the phrase carries no executable instruction.
A skill that says "before implementing, run a search for existing solutions and list what you found" changes behavior, because that is exactly the step people skip when they are in a hurry.

**Make the gates concrete enough for a model to evaluate.**
"Make sure it is well tested" is an opinion.
"Write tests for the empty input, the maximum value, and the concurrent case, then run the suite and confirm it passes" is a gate.
The whole mechanism depends on the model being able to check its own work, and it can only do that against criteria it can test.
This is the same reason I argued, in [Rethinking Code Review in the Age of LLMs](../rethinking-code-review-in-the-age-of-llms/index.md), that quality is a property of your constraints, not of your reviewers.
The constraints in a skill are where the quality actually lives.

**Keep the skill shorter than the attention it will receive.**
As the "lost in the middle" work showed, [a model's reliability degrades when a context fills with noise](https://arxiv.org/abs/2307.03172).
A skill that tries to encode every possible consideration becomes a skill the model half-follows.
Prefer several focused skills over one omnibus document, and cut anything the model would do correctly without being told.

**Version and maintain it like the code it produces.**
A skill that encodes a convention from two years ago is worse than no skill, because it enforces a stale standard on every run.
Treat the skill library as part of the codebase, with owners, review, and the same "does this still earn its keep?" scrutiny you would give any dependency.

## The Honest Limits

This only works for the part of the job that is describable, and it is worth being clear about where it stops.

Skills cannot encode taste that the writer cannot articulate.
If your best engineer's advantage is a feel for when an abstraction is about to collapse, and they cannot explain the signals they are reading, that advantage does not survive the translation into a file.
It stays in their head, and the skill without it will produce work that is competent but not inspired.
For the routine majority of software, which is most of software, the describable process is enough.
For the genuinely hard design calls, it is not.

Skills can also ossify mediocrity.
A skill that encodes a mediocre process enforces that mediocrity on everyone, consistently, forever.
The mechanism is morally neutral.
It collapses the variance in whichever direction the skill points, so a careless skill library can quietly lower a strong team to a lower common standard instead of raising the rest.
The remedy is that the skills themselves have to be written by the people whose process you actually want to reproduce, and revisited when the process improves.

Finally, this raises the floor for producing code, but producing code was never the only bottleneck.
As [Software Engineering Teams in the Age of AI](../software-engineering-teams-in-the-age-of-ai/index.md) argues, deciding whether a feature should exist, and writing a precise specification for it, remain irreducibly human and irreducibly valuable.
Skills make the execution layer homogeneous.
They do not decide what to execute.

## What to Do on Monday

You do not need a grand migration to start closing the gap.

Pick the one task where your team's output varies the most, the one where the senior engineer's pull request looks nothing like the junior's.
Write down the steps your strongest engineer actually takes when they do it well, the steps they would never admit to because they seem obvious to them.
Turn that into a skill, and run the next instance of that task through it, regardless of who is doing it.

Watch the output converge.
Then do it again for the next task.
The variance does not close all at once.
It closes one encoded process at a time, and each skill you add is a piece of seniority that stops being a private habit and starts being a shared standard.

**The team that wins in this era is not the one with the most powerful model.
It is the one whose best engineer's process runs, unchanged and unskipped, in every other engineer's session.**

## See also

- [Developer Trust Profiles](../developer-trust-profiles/index.md) - names the end state this article describes how to reach, where authorship stops carrying signal because everyone ships the same quality
- [The Importance of Context When Interacting with LLMs](../the-importance-of-context-when-interacting-with-llms/index.md) - why context is the entire mechanism by which a frozen model produces good output, and why a skill is just well-engineered context
- [The Shifting Bottleneck](../the-shifting-bottleneck/index.md) - how each layer of automation pushes leverage, and seniority, one step up the decision chain
- [Rethinking Code Review in the Age of LLMs](../rethinking-code-review-in-the-age-of-llms/index.md) - the case that quality is a property of your constraints, not your reviewers, which is exactly what a skill encodes
- [Software Engineering Teams in the Age of AI](../software-engineering-teams-in-the-age-of-ai/index.md) - which processes to keep and which to eliminate once execution is cheap
- [When Engineers Disagree on Best Practices](../when-engineers-disagree-on-best-practices/index.md) - how teams settle the conventions that skills eventually enforce

## References

- [tomzx/agents](https://github.com/tomzx/agents) - a working library of the skills this article describes, including the create-implementation and quick-pr-review skills referenced throughout the blog
- [Brown et al., "Language Models are Few-Shot Learners"](https://arxiv.org/abs/2005.14165) - established in-context learning, the capability that lets a loaded skill reshape a model's behavior without retraining
- [Liu et al., "Lost in the Middle: How Language Models Use Long Contexts"](https://arxiv.org/abs/2307.03172) - why a skill must stay focused, since model reliability degrades as context fills with noise
- [Wikipedia, "The Checklist Manifesto"](https://en.wikipedia.org/wiki/The_Checklist_Manifesto) - Atul Gawande's case that disciplined checklists outperform expert memory, the human analogue to the skills mechanism
