---
title: "Issues Are Free Now: Send the Implementation, Not the Idea"
created: 2026-07-06
type: post
status: finished
tags: [open-source, software-engineering, llm, pull-request, issues, ai, contribution, fully-ai-generated, llm=glm-5.2]
readability: 3
audience_notes: >
  Assumes the reader files issues or pull requests against open source or internal projects, has watched an issue tracker fill up faster than it can be cleared, and uses AI coding agents well enough to produce a draft implementation. No introduction to what an issue tracker or a pull request is.
---

For most of software's history, filing an issue took real work.
You had to reproduce the bug, narrow it down, write a clear description, and decide whether the request was worth the maintainer's time.
That filter is gone.
**An AI agent can read a README, a changelog, or spend ten minutes with the tool, and produce a polished, well-formatted issue in seconds, and it can do it a hundred times before lunch.**
The cost of creating an issue fell to almost nothing, the cost of clearing one did not, and every issue tracker on the internet is now overflowing.

If you are the one filing those issues, the result is hard to hear but clear.
The issue you just opened is no longer a contribution in any real sense.
It is a request for someone else's work, and it is sitting in a queue next to nine hundred other requests for someone else's work, most of them produced just as cheaply as yours.
**The only thing that still moves the needle is the implementation attached to the request, because the implementation is the one input whose cost has not fallen.**

## The Issue Tracker Was Always a Wish List

It is worth being clear about what an issue tracker actually was, even before AI.
A well-written bug report was a real gift, because it gave the maintainer a reproduction and a starting point.
A feature request was almost always a wish.
Someone else should do this.
Someone else should want this.
Someone else should spend their Saturday on the thing I would like to have.

Maintainers cleared the gifts and let the wishes pile up, and that was fine, because the wishes cost the filer enough effort to write that only the motivated ones made it through.
The friction was the filter.
**The issue tracker was tolerable only because filing an issue was mildly annoying, and the mildly annoyed filer self-selected for "I actually care."**

Remove the friction and the wish list becomes the whole tracker.
That is where we are.

## The Cost Imbalance Is the Whole Problem

The math that kills the tracker is simple.
It costs a filer roughly zero seconds and zero cents to open an issue with an AI agent.
It costs a maintainer anywhere from five minutes to an afternoon to triage it: read the request, check whether it duplicates something, decide whether the project wants it, find the relevant code, and either close it, schedule it, or do it.
**One side of that exchange is free; the other side is unpaid, and the unpaid side is the one you are asking to work.**

Multiply that imbalance by a few hundred issues a week and you get the current state of every popular open source repository on the planet.
The triage queue grows faster than any single human can read it, the maintainer starts ignoring the tab, the contributor waits six months for a reply, and the project slowly gains a reputation for being unresponsive.
Nobody is at fault.
**The system is just balanced so that the cheap side produces faster than the expensive side can consume, and the buffer between them is a person.**

This is the same dynamic I described for pull requests in [The Pull Request Queue Outgrew You](../triaging-open-source-pull-requests/index.md): the cost to create a change fell below the cost to review it, and the maintainer became the bottleneck in their own queue.
What is true for code changes is now true for ideas, and ideas are even cheaper to produce.

## An Implementation Rewrites the Ask

Here is the move that fixes the imbalance, and it is the only move that fixes it.
Stop sending the description.
Send the code.

A pull request with a working implementation changes the maintainer's job from "do this work" to "evaluate this work," and those are not the same task.
Doing the work is open-ended, expensive, and unpaid.
Evaluating the work is limited, fast, and something a maintainer can actually fit into a Saturday morning.
The difference between "you should add a dark mode" and "here is a dark mode, here are the tests, here is the screenshot, merge or reject" is the difference between a request for a favor and an offer to work together.
**The implementation is what converts your issue from a cost imposed on the maintainer into an option extended to them.**

This is also why the maintainer is so much more likely to act on a pull request than on an issue.
A PR gives them a simple choice they can make in minutes.
An issue gives them an open-ended commitment that will eat an afternoon if they engage with it at all.
If you wonder why your feature request has sat untouched for two years while a stranger's twenty-line PR landed in a week, that is the entire explanation.
**The PR was cheap to say yes to. Your issue was expensive to say yes to, and expensive to say no to, so it got neither, which is what happens to expensive things in a full queue.**

## The Cost of Implementing Fell Too

The obvious pushback is that not everyone can write the implementation, and that used to be true.
It is not true anymore.

The same AI agent that filed the issue can write the pull request.
You describe what you want, the agent reads the codebase, produces a diff, writes the tests, and opens the PR.
The skill floor for "I can send a working implementation" dropped from senior engineer to motivated user with a coding agent and an afternoon.
**The reason to keep sending descriptions instead of implementations is no longer that you cannot produce the implementation.
It is that you have not updated your habits to match the new cost structure.**

This is the same shift [The Shifting Bottleneck](../the-shifting-bottleneck/index.md) keeps arriving at.
Producing code is no longer the constraint.
Deciding what to produce, and accepting what got produced, is the constraint.
In an issue tracker, that means the scarce resource is no longer "someone willing to file the issue" or even "someone willing to write the code."
The scarce resource is the maintainer's attention, and the only way to earn a slice of it is to bring the work to a state where saying yes costs them almost nothing.

## But I Am Not Sure My Implementation Is Good

This is the second pushback, and it is more serious than the first.
You worry that sending an AI-generated PR is dumping low-quality work on an already overloaded maintainer, and that is a real risk.
The answer is not to hold back the PR.
The answer is to do the work that makes the PR cheap to evaluate.

Run the tests.
Write a new one for the behavior you added.
Reproduce the bug you claim to fix, and show the test going red before your patch and green after.
Keep the change small and focused on one thing.
Link the issue you are closing.
Write a PR description that lets the maintainer evaluate the change in thirty seconds.
**Every one of these is an attempt to lower the cost of saying yes, and lowering the cost of saying yes is the entire game.**

A small, tested, well-described PR is a gift.
A large, untested, AI-generated diff with a one-line description is just a different kind of issue, and it will be treated like one.
The discipline is not "send code instead of an issue."
The discipline is "send code that is cheaper to merge than to discuss, and if you cannot produce that, the issue tracker will not save you either."

## What the Maintainer Actually Wants

It helps to look at this from the maintainer's chair for a moment, because the request they are implicitly making is not unreasonable.
They want to spend their scarce attention on decisions only they can make: the architecture, the direction, the boundary between what the project is and is not.
They do not want to spend it turning a feature description into code, because that is the part the LLM can do now.
**The highest-value contribution you can make is one that arrives with every reversible decision already made and every test already green, so that the maintainer's job is reduced to a judgment call they were going to have to make anyway.**

This is the open source version of the argument in [Rethinking Code Review in the Age of LLMs](../rethinking-code-review-in-the-age-of-llms/index.md).
When the implementation is cheap to produce, the value concentrates upstream, at the point where someone decides what the implementation should be.
A good contributor in this era is not someone who writes clean code.
A good contributor is someone who arrives with a concrete proposal, already implemented, already tested, already de-risked, leaving the maintainer nothing to do but approve, redirect, or reject.

## What About Bugs You Cannot Reproduce

There is a real exception, and it should be named so the argument does not go too far.
Some issues are genuine bug reports where the value is in the reproduction, not in the fix.
A crash that happens on a specific kernel version, a regression that only shows up under load, a data corruption bug that requires a particular sequence of inputs.
These are gifts, when written carefully, because the maintainer could not have produced the reproduction themselves.

But notice what makes them gifts.
They carry information the maintainer did not have and could not get cheaply.
**The test for whether your issue is a contribution or noise is exactly this: does it contain information the maintainer could not have produced on their own in fifteen minutes with an AI agent?
If yes, file it.
If no, the issue is a request for someone else to do work you could have done yourself, and the queue is full of those already.**

The same test separates a useful feature request from noise.
"Add dark mode" is noise.
"Add dark mode, here is the design, here is why it does not conflict with the theming system, here is the PR, here are the screenshots, here are the tests" is a contribution.
The information that converts noise into contribution is exactly the information that comes from having tried to build the thing.

## What to Do on Monday

If you file issues against projects you depend on, change one habit.
Before you open the issue, try to open the PR instead.
Point an agent at the codebase, describe the change you want, and let it produce a draft.
Spend the time you would have spent polishing the issue description on getting the PR to a state where merging it is the obvious move: tests passing, scope small, description clear.
**File the issue only if the PR attempt really failed, and when you do, include what you learned from the attempt, because that is the information the maintainer actually needs.**

If you maintain a project, change the default you invite.
Rewrite your contributing guide to say, plainly, that feature requests without an accompanying PR will be closed, and that bug reports without a reproduction will be closed faster.
Be clear that this is not hostility.
It is the only way the queue stays a queue instead of a landfill.
Make the pull request template the front door, and the issue template the side door for the narrow set of things only an issue can carry.
**Raising the floor on contributions is, in this era, an act of respect for the contributors who are willing to meet it, because they are the ones whose work will otherwise be buried under the noise.**

And for everyone, learn the new cost structure.
Ideas are free.
Descriptions are free.
Issues are free.
Implementations are the only currency left that buys maintainer attention, and the reason is not that maintainers are picky.
It is that implementations are the one input whose cost has not fallen to zero, which makes them the one input that still signals you meant it.
**If you want a maintainer to take your request seriously, prove it the only way that still costs you something: by sending the code.**

## See also

- [The Pull Request Queue Outgrew You](../triaging-open-source-pull-requests/index.md) - the companion argument from the maintainer's side: the cost to create a change fell below the cost to review it, and triage has to replace review
- [The Shifting Bottleneck](../the-shifting-bottleneck/index.md) - the upstream pattern: producing code is no longer the constraint, deciding and accepting are, which relocates where contribution lives
- [Rethinking Code Review in the Age of LLMs](../rethinking-code-review-in-the-age-of-llms/index.md) - why value concentrates upstream at the decision point when implementation becomes cheap
- [The Acceptance Gap](../the-acceptance-gap/index.md) - the maintainer's remaining job is acceptance, and an implementation is what lets them do that job in minutes instead of afternoons
- [Feature Parity Is Not a Moat](../feature-parity-is-not-a-moat/index.md) - the parallel collapse of copy-time, which made features cheap to clone the same way AI made issues cheap to file
