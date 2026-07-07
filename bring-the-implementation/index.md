---
title: "Bring the Implementation: An Issue Is No Longer a Contribution"
created: 2026-07-07
type: post
status: finished
tags: [ai, open-source, software-engineering, llm, issue-tracker, maintainership, contribution, fully-ai-generated, llm=claude]
readability: 3
audience_notes: >
  Assumes the reader files issues on or maintains open source projects, has used an LLM coding agent, and knows what a pull request and an issue tracker are. No introduction to open source etiquette from first principles.
---

Filing a good issue used to cost something.
You had to reproduce the problem, isolate it, read enough of the project to describe it in the maintainer's vocabulary, and write it up clearly.
That cost was a filter, and the filter was doing quiet work: an issue that existed at all was evidence that someone cared enough to spend an hour on it.

An AI agent now produces that artifact in seconds.
Point it at a repository, describe a vague desire, and it returns a polished issue with a plausible reproduction, a suggested root cause, and a respectful closing paragraph.
**The cost of filing a well-written issue has collapsed to nearly zero, and with it collapsed everything the cost used to signal.**
The tracker fills with hundreds of articulate issues, and the maintainer can no longer tell, by reading, which ones represent a real need backed by a real person willing to do real work.

So the bar has to move, and it is moving in a predictable direction.
**If you want a maintainer to act on your idea, stop filing the idea and start filing an implementation of it, because an implementation can be evaluated while an idea can only be discussed.**
Otherwise you are one of the many hundreds of issues slowly stacking in the tracker, sorted by nothing, waiting for attention that will likely never come.

## Cheap Artifacts Stop Being Signals

Economists have a name for messages that cost the sender nothing: [cheap talk](https://en.wikipedia.org/wiki/Cheap_talk).
The core result is uncomfortable and directly applicable here.
When sending a message is free, the message stops carrying information about the sender's commitment, because everyone can send it, including people with no commitment at all.
[Signalling](https://en.wikipedia.org/wiki/Signalling_(economics)) only works when the signal is expensive enough that only the serious can afford it.

A hand-written, carefully reproduced bug report was a costly signal.
An agent-generated issue is cheap talk.
It may be correct, it may even be valuable, but its existence no longer tells the maintainer anything, because producing it required no skin in the game.
The maintainer, staring at a tracker where every issue is equally articulate, has lost the ability to triage by quality of writing, which used to be the best cheap proxy for quality of thought.

Meanwhile the maintainer's side of the ledger did not change.
Reading an issue, understanding it, deciding whether it fits the project, designing a solution, implementing it, testing it, and shipping it costs exactly what it cost before.
**AI made the demand side of the tracker nearly free while leaving the supply side, maintainer attention, as scarce as it ever was**, and the [attention economy](https://en.wikipedia.org/wiki/Attention_economy) predicts exactly what happens next: the scarce resource gets rationed, and the rationing criterion changes.

## An Issue Is a Work Order; an Implementation Is a Candidate

Look at what each artifact actually asks of the maintainer.

An issue, however well written, is a work order.
It says: here is a problem or a desire, now you go design the solution, weigh the tradeoffs, write the code, write the tests, and maintain the result forever.
The issue transfers close to one hundred percent of the work to the person who did not ask for it.
Multiply by hundreds of issues and the tracker is not a to-do list, it is a queue of unfunded mandates.

An implementation is a candidate.
It says: here is a concrete, running answer to the problem, evaluate it.
The maintainer's job shrinks from "do everything" to "decide whether this specific artifact is acceptable," and deciding on a concrete artifact is a fundamentally cheaper operation than designing from a description.
You can run a patch.
You can read its tests.
You can measure its performance, try its edge cases, and feel whether the API is right.
None of that is possible with an idea, which is why discussions of ideas sprawl and evaluations of artifacts converge.

This is the oldest wisdom in open source, newly load-bearing.
"Talk is cheap. Show me the code" was [Linus Torvalds' answer](https://en.wikipedia.org/wiki/Linus_Torvalds) to grand proposals two decades ago, and "patches welcome" has always been the polite version of the same filter.
What changed is the excuse.
**The same agent that made your issue free to write makes the implementation nearly free to attempt, so declining to attempt it is now itself a signal, and not a flattering one.**
If the feature you want is genuinely a half-day of agent-assisted work and you did not spend the half-day, why should a stranger spend it for you?

## What "an Actual Implementation" Means

The word implementation is doing precise work here, and a low-effort AI-generated pull request does not qualify.
Maintainers are [already drowning in plausible, unprovenanced machine-generated patches](../triaging-open-source-pull-requests/index.md), and adding to that flood is worse than filing an issue, because a bad patch consumes more attention than a bad idea.
The point is not to move the cheap talk from the issue tab to the pull request tab.
The point is to bring something evaluable.

Evaluable means it runs.
A branch or a draft pull request that compiles, passes the existing suite, and can be checked out and exercised in minutes.

Evaluable means it demonstrates its own claim.
Tests that fail without the change and pass with it, a benchmark if the claim is performance, a screenshot or recording if the claim is behavior.
The [acceptance question is the expensive one now](../the-acceptance-gap/index.md), and your job as a contributor is to pre-pay as much of it as you can, because the model's confidence is not evidence and the maintainer knows it.

Evaluable means it is scoped.
The smallest diff that honestly makes the point, touching the fewest files, following the project's existing style, with the tradeoffs you considered written down in the description.
A three-hundred-line focused patch is a candidate.
A three-thousand-line refactor that arrived unannounced is a hostage situation.

And evaluable means you read it before the maintainer did.
An implementation you generated but never reviewed is not your implementation, it is a forwarded lottery ticket, and forwarding it transfers the verification cost to exactly the person you were trying to spare.
**You are asking for an evaluation, so the artifact must be worth evaluating, and only a human who checked it can promise that.**

## When Discussion Still Comes First

The rule is not "never file issues," and pretending otherwise produces its own pathology.

Some changes genuinely need design agreement before code: breaking API changes, architectural shifts, anything that commits the project to a maintenance burden regardless of how it is implemented.
For those, an unsolicited implementation is presumptuous, and many projects rightly ask for a proposal first.
But notice that even there, the artifact beats the abstraction.
A spike, a prototype in a fork, a proof of concept linked from the proposal turns the design discussion from a debate about imagined systems into an evaluation of a visible one, and starves the [bikeshedding](https://en.wikipedia.org/wiki/Law_of_triviality) that pure idea threads feed on.

Bug reports with reliable reproductions also remain valuable on their own, because a minimal reproduction is already an evaluable artifact: it runs, it demonstrates its claim, and it is scoped.
The dividing line is not "issue versus pull request."
**The dividing line is whether you handed the maintainer something they can evaluate or something they must do.**

And read the contributing guide before doing any of this, because a growing number of projects now specify exactly how they want AI-assisted contributions declared and structured, and violating that is the fastest way to have your carefully prepared candidate closed unread.

## The New Etiquette

For contributors, the checklist is short.
Before filing, ask whether you could attempt the implementation with the tools you already have, and if the answer is yes, attempt it.
Bring the smallest running, tested, self-demonstrating version of what you want, reviewed by your own eyes, with tradeoffs stated.
If the change needs design agreement first, file the issue, but attach the prototype.
If you are not willing to do any of that, be honest about what your issue is: a wish, filed into a queue of wishes, with the priority a wish deserves.

For maintainers, the move is to make the bar explicit rather than resenting its absence.
State in the contributing guide that feature requests accompanied by a working, tested implementation get evaluated first, and that idea-only issues are triaged as suggestions, not commitments.
This is not gatekeeping, it is honest pricing.
The tracker was always an economy of your attention.
**AI did not break that economy, it just removed the last cheap proxy for seriousness, and the only signal left that cannot be faked by a model in thirty seconds is the artifact that survives evaluation.**

Generation is free now.
Evaluation is the scarce good.
Bring something worth evaluating.

## See also

- [The Pull Request Queue Outgrew You](../triaging-open-source-pull-requests/index.md) - the maintainer's side of the same collapse: when artifacts are cheap to produce, triage must come before review
- [The Acceptance Gap](../the-acceptance-gap/index.md) - why "the model produced it" is not "it is acceptable," which is exactly the gap a good contribution pre-pays
- [The Shifting Bottleneck](../the-shifting-bottleneck/index.md) - the general pattern: automating production of an artifact moves the constraint to deciding whether the artifact is any good
- [The Backlog Is Not a Dumping Ground](../backlog-management-best-practices/index.md) - the internal-team version of a tracker filling faster than anyone can honestly triage it
