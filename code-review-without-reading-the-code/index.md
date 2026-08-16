---
title: "You Already Review Code Without Reading It"
created: 2026-07-25
type: post
status: finished
tags: [software-engineering, code-review, pull-request, productivity, fully-ai-generated, llm=glm-5.2]
readability: 3
audience_notes: >
  Assumes the reader participates in pull request review on a software team and has a gut sense that approvals are decided quickly. No particular tooling or stack required.
---

**Most code review does not involve reading code.**
The decision to approve is made before the diff opens.
We keep the ritual, and quietly drop the part that is supposed to justify it.

The gap between the ritual and the reading has a mirror on the other side of the pull request.
An LLM cannot vouch for its own output, because accepting a solution as done needs information the model does not have ([the acceptance gap](../the-acceptance-gap/index.md)).
The reviewer has the same problem in reverse: vouching for code that was never read.

## What I Mean By Reading

There is a difference between opening a pull request and reading one.
Reading means reconstructing what the code does, tracing each branch, checking every assumption against the rest of the system, and forming an independent opinion about whether it is correct.
That takes time, and sustained focus, and the kind of attention that does not survive a fifteen-item review queue.

Opening is something else.
You open the PR, your eye catches the file list, the green check from CI, the test count, the description the author wrote, and within a few seconds a feeling forms: this is fine, or this is not.
The code itself sits downstream of all of that.
Most of the time, you never reach it.

This is not a failure of discipline.
It is how the tool presents work to you, and how a busy engineer responds to that presentation.
The diff is the last tab you look at, and often the one you look at least.

## The Signals That Actually Decide Approval

If you watch what an approver actually responds to, the code is rarely the first thing.

CI passed.
That carries more weight than any line you might have read.
The tests are green, the build is green, the linter is quiet, and that cluster of signals has already done the safety work before you arrived.

Then the author.
A pull request from someone you trust gets a lighter read than one from a new hire.
You will deny this in a meeting and do it anyway in practice.
Trust is a real signal, and a useful one, but it is not "reading the code".

Then the size of the change.
A two-line diff to a README merges in seconds.
A four-hundred-line refactor to the auth module stalls.
You are reacting to blast radius, not to semantics, and you are right to, but again, that is not reading.

Then the description and the linked issue.
These tell you what the author intended.
For a lot of pull requests, the intent is all you ever verify, because the code is too long to verify against it in the time you have.

**The code is the alibi.
The signals are the verdict.**

## Why We Pretend To Read

If the code is not really what we are checking, why the ceremony around it?

Because reading code is the thing code review is supposed to be for.
Admit that you are not doing it, and you admit that the central activity of the gate is not happening.
That is an uncomfortable admission, so it does not get made.
Instead we keep the form, the comments, the approving review, and let the substance slide.

There is also a blame function.
When something breaks, we want to point at a name on the pull request and say "they signed off".
The signature has to mean "I read this and vouched for it", or it cannot carry that blame.
So we maintain the fiction that the signature means what it says, even though everyone, on both sides, knows it often does not.

This is accountability theater: the approve click certifies that a person was present, but rarely certifies that the code was read.
The signature allocates blame after the fact.
It does not prevent harm before it.

## The Self-Test

Here is a test you can run on yourself.
Approve your next five pull requests the way you normally would.
The next day, try to recall a single line of code from each one.

If you cannot, be precise about what that means.
It means you approved metadata.
You were responding to CI, to the author, to the description, to the size of the diff, to your sense of the person.
Those are signals, and some of them are good signals.
But none of them are "I read this code and understood it".

Run the same test on your team.
Ask a recent approver to explain, from memory, one function that changed in the pull request they approved.
The silence you get back is the most truthful data you will collect about how code review actually works in your organization.

I am not mocking reviewers here.
I have failed this test more often than I have passed it.
The point is that the gap between what review is supposed to be and what it is, is large, and we never measure it because measuring it would force a conclusion we have already decided not to reach.

## Two Real Paths

Once you accept that most review does not involve reading, you have two defensible directions, and only two.

The first is to actually read the code, on the changes that warrant it.
Not every change.
The ones with real blast radius: irreversible changes, trust-boundary changes, changes to the gating system itself.
On those, slow down, read deliberately, trace the logic, and form an independent opinion.
This is high-leverage work, and it is rare, and it deserves the time it takes.

The second is to drop the pretense, and let the changes you were never going to read merge on the strength of the signals you were actually using.
Green CI, a passing test suite, a trusted author, a small reversible diff.
These already decided the outcome.
Let them decide it without a human in the middle adding latency and taking credit.

**What is not defensible is the current default.**
The default is the second path, with the theater of the first layered on top.
You approve without reading, but you still require a human to approve without reading, and you call the combination a quality gate.

## When The Code Was Written By A Machine

This was already true when humans wrote the code.
It is sharper now that machines do.

When an LLM generates the diff, reading it line by line is even less useful, for reasons explored in [the case against reading LLM-written code](../rethinking-code-review-in-the-age-of-llms/index.md).
The reviewer becomes the only mind in the loop, reconstructing intent from output, and that reconstruction is harder and slower than reviewing a human who can at least be asked what they meant.

So the metadata review does not get more rigorous by being relabeled a code review.
It gets more exhausting, and less effective, for the same rubber stamp at the end.

If you were not reading human-written code, you are not going to start reading machine-written code.
You are going to keep approving signals, with a worse feeling about it.
The productive move is to put the effort where it was always worth more: upstream, in the specification, the tests, and the gates.

## What to Do Next

You do not need permission to start.
Pick the low-blast-radius path and let it merge on green.
Then be plain with your team about what the rest of the approvals were already doing.

When a change is large, irreversible, or crosses a trust boundary, read it for real.
Budget the time.
Treat it as the exception it is, not as the default dressed up as diligence.

And measure the gap.
Ask your approvers what they remember from the pull requests they approved.
The number will embarrass you, and that embarrassment is the beginning of a review process that is actually worth its cost.

## See also

- [Verifying Code Without Reading It](../verifying-code-without-reading-it/index.md) - the system that makes unread review safe: the checks, critics, and gates that replace the reading.
- [Rolling Out the Unread Review](../rolling-out-the-unread-review/index.md) - how to ship that system to a team that does not trust it yet.
- [The Acceptance Gap](../the-acceptance-gap/index.md) - the root insight this article shares, seen from the model's side: acceptance is the gate the model cannot close on its own, and reading is its reviewer-side mirror.
- [Rethinking Code Review in the Age of LLMs](../rethinking-code-review-in-the-age-of-llms/index.md) - makes the case that reading LLM-written code is the wrong tool for the job.
- [The Merge Gate](../the-merge-gate/index.md) - separates the approve-click from the reading, and shows where a human gate genuinely adds value.
- [The Future of Code Review](../the-future-of-code-review/index.md) - the more aggressive claim that human review is being replaced by verification systems.
- [Who Resolves the Merge Conflict?](../who-resolves-the-merge-conflict/index.md) - a companion question about which decisions need a human who holds real intent.
