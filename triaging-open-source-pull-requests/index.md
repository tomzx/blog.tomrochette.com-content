---
title: "The Pull Request Queue Outgrew You: A Triage Layer for Open Source Maintainers"
created: 2026-06-30
type: post
status: finished
tags: [open-source, software-engineering, code-review, pull-request, llm, automation, github-actions, productivity, fully-ai-generated, llm=glm-5.2]
readability: 3
audience_notes: >
  Assumes the reader maintains or co-maintains an open source repository, has dealt with a pull request backlog, and is comfortable with GitHub Actions, branch protection, and the basics of prompting an LLM. No introduction to what a pull request or an LLM is.
---

Open source always had a queue problem.
For most of its history the threat was volume: more pull requests than a maintainer could read, arriving faster than one unpaid person could clear.
**The pull request queue scales with the project's popularity, and a single maintainer's attention does not scale with anything at all.**

That is still true, and it is no longer the worst of it.
The character of the queue changed.
The median pull request is now machine-generated, and a machine-generated pull request is a different kind of problem than a human one.
It looks correct, because plausibility is exactly what a language model optimizes for, and it may be subtly, uniformly wrong in ways that read as confident and clean.
There is usually no author who thought about each line, so there is no intent for you to leverage as context, only output you have to verify from scratch.
And almost never does the contributor tell you which model produced the code, what prompt generated it, or whether a human ever read it before it landed in your queue.
**The flood is not just bigger now.
It is full of plausible code with no provenance, and plausible, unprovenanced code is the hardest thing in the world to triage by reading it.**

The instinct of a responsible maintainer is to read every pull request, carefully, and reply thoughtfully.
That instinct is exactly what kills the project.
Every half-hour spent reverse-engineering an AI-generated PR that looks reasonable until the third function is a half-hour not spent on the architectural change that keeps the library alive.
The queue grows while you sleep, and while you are polite, and while you are giving a stranger's model the benefit of the doubt.

You cannot review your way out of this, for the same reason a team engineer cannot: [per-unit review scales linearly with your hours, and the entropy is produced faster than you can read it](../the-codebase-gardener/index.md).
The difference is that on a team you can hire.
In open source, you are usually alone, unpaid, and tired, and the code you are being asked to vet no longer carries the reasoning of the person who submitted it.
**The only way out is to stop reviewing everything and start triaging everything, so that your scarce attention lands only on the pull requests that deserve it.**

## Triage Before Review

Review answers the question, "is this code correct?"
Triage answers a cheaper question that comes first: "does this pull request deserve my attention at all, and if so, how much?"

Most maintainers fuse the two.
They open a pull request, start reading the diff, and only then discover that it is stale, that it conflicts with main, that it has no tests, that it touches a file nobody asked it to touch, or that it is the fourth duplicate of a request they already declined.
Every one of those discoveries was free to make before reading a single line of code, and making them up front is the entire difference between a queue you manage and a queue that manages you.

A triage layer is the set of automated signals that answer the cheap questions before you ever open the diff.
Does it still apply?
Does it still merge?
Is it small or sprawling?
Is it risky or routine?
Who is it from?
Does it match the conventions the project already requires?
**Each of these is a machine-checkable property, and a property a machine can check is attention you never have to spend again.**
This is the same move [The Codebase Gardener](../the-codebase-gardener/index.md) makes for a team codebase: encode the standard where every change is forced to pass through it, instead of carrying it in your head as a review habit.

The goal of the triage layer is not to merge everything automatically.
It is to make the queue sortable, so that when you sit down with your limited hour, you are looking at the five pull requests that matter, ranked, instead of the fifty that arrived in the order they happened to come in.

## Plausibility Is the Danger, Provenance Is the Missing Signal

Understanding why the modern queue is dangerous is what shapes the triage layer, because AI-generated code breaks the assumptions review used to rest on.

When a human wrote the pull request, you and the author shared a mental model.
You could trust that the choices in the diff were deliberate, even imperfect ones, and a gap between your expectation and the code was an interesting signal, because it represented two human understandings of the same problem meeting.
**When a model wrote the code, there is no shared mental model, and there is no author who deliberated.**
The code is the output of a pattern-matching process, internally coherent, consistent with nothing around it, and wrong about the domain in ways that look exactly like correctness.
This is the argument from [Rethinking Code Review in the Age of LLMs](../rethinking-code-review-in-the-age-of-llms/index.md), and it lands hardest in open source, where the reviewer and the "author" have never spoken.

What makes this crisis specific is the provenance gap.
Contributors almost never disclose that the code is generated, let alone which model generated it, what prompt produced it, or whether a human checked the output before opening the pull request.
Without provenance, you cannot assess risk.
A fifty-line patch from a contributor who tested it by hand and a fifty-line patch a model hallucinated in three seconds look identical in the diff, and the diff is all you have.
**Plausible code with no origin story is the default input now, and it forces a worst-case assumption on every pull request: treat it as unverified until something proves otherwise.**

The implication for triage is concrete.
First, the durable defense against plausible code is not a sharper opinion but a machine-checkable gate, because opinion-based review loses against code that was designed to look right.
Tests, static analysis, type checking, reproducible builds: these operate on what the code does, not on how it reads, and they do not get fooled by confident prose.
Second, the absence of provenance is itself a routing signal.
A large, high-churn, undocumented pull request from an unknown contributor should default to high-risk, not because the contributor is malicious but because you have no evidence to assign it anything lower.
Third, the one piece of information that would most improve your triage, which model and what prompt, is the one nobody is giving you, which means the cheapest high-leverage intervention available is to start asking for it.

## Let Automation Carry the Logistics

The first tier of triage is pure logistics, and all of it is solved.
You should not be tracking any of this by hand.

**Mark and close the stale.**
A pull request that has had no activity for sixty days is not waiting for you.
It is rotting, and rot is contagious, because a queue full of stale PRs signals to new contributors that nobody is home.
[actions/stale](https://github.com/actions/stale) marks a pull request stale after a window you define, posts a warning, and closes it if the contributor does not respond.
This is not cruelty.
Letting a contributor's work sit unread for a year is cruelty.
A fast, automatic close with a clear "reopen if you are still interested" is a kindness, and it is a kindness that costs you nothing.

**Surface the conflicting.**
A pull request that no longer merges cleanly is a pull request that is wasting your attention, because until the contributor rebases, your review is provisional.
[eps1lon/actions-label-merge-conflict](https://github.com/eps1lon/actions-label-merge-conflict) adds a `merge-conflict` label the moment a PR falls behind main, and removes it the moment it merges again.
Now you can filter `label:-merge-conflict` and only review work that is actually ready.
The contributor also gets a clear, automated nudge that rebase is needed, without you having to be the one to say it.

**Label by size.**
The blast radius of a change is the single best predictor of how much attention it deserves, a point I made in [The Merge Gate](../the-merge-gate/index.md): a README typo and a schema migration are both pull requests, and they do not need the same gate.
A size action tags every PR with `size/S` through `size/XL` based on diffstat.
Small changes become candidates for fast-track; large ones become candidates for "please split this."

**Label by area.**
[actions/labeler](https://github.com/actions/labeler) tags a pull request based on which files it touches, so you can route `area/ci`, `area/docs`, `area/security` to the right context, or skip the areas you are not the expert in.

**Flag the first-timers.**
Label first-time contributors explicitly.
Not so you can be suspicious of them, but so you can be generous with them, because a good first review is how a first-time contributor becomes a second-time contributor, and a second-time contributor is how a project outlives its original maintainer.

**Enforce the conventions you already require.**
If your project requires a linked issue, a semantic title, a signed commit, a test for every new function, enforce each one with a check that runs on open.
[amannn/action-semantic-pull-request](https://github.com/amannn/action-semantic-pull-request) is one example, but the specific tool matters less than the principle: anything you find yourself typing in review comments repeatedly belongs in a check that fails the build.
A review comment is a standard you enforce only when you are awake.
A failing check is a standard that runs forever.

Each of these is a small automation, and none of them review code.
Together they collapse the queue from "everything that arrived" to "everything that is ready, relevant, and sized."
That is most of the battle, and it cost you zero hours of reading diffs.

## Demand Provenance

The single most valuable triage signal is the one the current ecosystem refuses to provide, which means the maintainer has to require it.

Add two fields to your pull request template, and make them hard to skip.
Was this change generated or significantly assisted by an AI tool?
If so, which model, and what was the prompt or task description?
A checkbox and a free-text line are enough.
You do not need a policy on whether AI contributions are welcome; you need the data to triage them on their actual risk rather than on a guess.

Label from the answer.
`human-authored`, `ai-assisted`, `ai-generated`, and a tag for the model when it is disclosed.
Now provenance becomes a filter and a routing input instead of a mystery.
A `human-authored` patch from a known contributor with passing tests can travel the fast lane.
An `ai-generated` patch with no model disclosed and no linked issue starts one gate further back, by default, because it carries the provenance risk this era is defined by.

Be explicit that disclosure is not a penalty.
The penalty is discovery, when you eventually realize a PR was generated and the contributor hid it, because at that point the trust that makes open source work is gone and the PR is closed on principle.
Disclosure is what lets a generated contribution compete for your attention on its merits.
Concealment is what makes every generated contribution read as an attempt to slip something past you.
**A maintainer cannot triage what they cannot see, and in a queue full of plausible code, the origin of the code is the first thing they need to see.**

## Let the LLM Do the First Pass

Once the logistics are handled, the remaining question is the one automation traditionally could not answer: is the code itself any good.
That used to require a human, because reading a diff and reasoning about its consequences was exactly the task machines could not do.
It is not anymore.
**An LLM will not review a pull request as well as you would, but it will review it in seconds, on every pull request, at three in the morning, and it will produce a structured signal you can sort and filter on.**
That is a different value than correctness, and for triage it is the value that matters.

Run an LLM review on every pull request when it opens and on every push that updates it.
Give it your evaluation criteria, explicitly, the same checklist you would walk through mentally if you opened the diff yourself.
Does it add a new dependency?
Does it change a public interface?
Does it touch security-sensitive code paths?
Does it introduce backward/forward-incompatible behavior?
Are there tests for the new behavior?
Does it match the naming and structural conventions of the surrounding code?

Ask for the output as structured data, not prose.
A risk score, a confidence score, a one-line summary, and a short list of specific findings.
Then parse those fields and turn them into labels.
`risk:low`, `risk:medium`, `risk:high`.
`confidence:high`, `confidence:low`.
`needs-human-review` when the model is unsure or when the risk is high.
`auto-merge-candidate` when the risk is low, the confidence is high, the size is small, the tests pass, and the contributor is trusted.

Now your queue is sorted by signal instead of by arrival time.
The pull requests that are low-risk and high-confidence can be merged on green, or queued for a single glance, because the LLM has already done the scanning work you would have done anyway.
The pull requests that are high-risk, or where the model is uncertain, rise to the top of your attention with the findings already attached.
**You are no longer choosing what to read.
You are confirming or rejecting a hypothesis the triage layer has already formed.**

A few cautions, because this is the part people get wrong.

The LLM review is advisory, not authoritative.
It hallucinates, it misses subtle bugs, and it is confidently wrong in exactly the register that makes you want to trust it.
Never wire it to merge on its own verdict for anything that crosses a trust boundary, changes a public contract, or is hard to undo.
Use it to route attention, not to replace it, and reserve the replaced attention for the small, reversible, low-risk changes where being wrong is cheap to fix.
This is the same risk-based gating [The Merge Gate](../the-merge-gate/index.md) argues for: the unit of gating is the blast radius of the change, not the existence of the pull request.

The deepest caution is specific to this era, and you have to internalize it before trusting any automated score.
**When an LLM reviews code that an LLM wrote, the reviewer shares the generator's blind spots.**
Both are statistical models trained on overlapping corpora, and a mistake plausible enough for one model to make is often plausible enough for the other to overlook.
Two models agreeing that "this looks fine" is a weaker signal than either model issuing that verdict alone, and if the reviewer and the generator come from the same model family the agreement proves almost nothing.
This is why provenance matters at the review layer as well: feed the disclosed model and prompt into the reviewer's context so it can target the failure modes that model is known for, rather than re-reading the diff through the same lens that produced it.
And it is why, for `ai-generated` pull requests, you must discount the confidence score and default toward `needs-human-review` unless the change is independently verified by something that does not share the blind spot: a passing test, a type checker, a reproducible build, a specification the code is checked against.
**The LLM review is one signal in the triage layer, never the only one, and against generated code its job is to surface hypotheses for a human or a gate to confirm, not to pronounce the code correct.**

Calibrate by reviewing the reviewer.
For your first month, read the LLM's review on every pull request you also review yourself, and keep a tally of where it was right, where it was wrong, and where it missed something you caught.
That tally tells you which criteria to strengthen in the prompt and which labels to distrust.
An uncalibrated LLM gate is a liability.
A calibrated one is a second pair of eyes that never gets tired, and that gets more accurate every time you adjust the criteria.

Post the rationale, not just the label.
Have the action leave the summary and findings as a comment on the pull request.
The contributor sees what was flagged, the maintainer sees why a label was applied, and the verdict is auditable rather than a black box.
Transparency is what keeps an automated review from feeling like a gatekeeping robot, and it is what lets a contributor fix the problem before you ever have to look.

## Route by Risk, Not by Arrival

Once the triage layer is producing labels, the routing writes itself, and it should match the risk profile of each change rather than the order it was submitted.

Low risk, high confidence, small, passing tests: auto-merge on green, or batch them into a single weekly pass where you glance and click.
High risk, or low confidence, or large, or crossing a security boundary: hold for human review, and review those first.
AI-generated with no model disclosed, or no linked issue, or no tests: default to the human queue until a test or a specification proves it, regardless of how small it looks, because small and plausible is exactly the shape of a subtle bug.
First-time contributor: prioritize the response, because the speed of your first reply decides whether they come back.
Conflicting: invisible until rebased.
Stale: closed.

This is the open source version of the argument from [The Merge Gate](../the-merge-gate/index.md): treating every pull request as needing the same gate is a failure to think about risk, and most pull requests do not need a human at all.
**The maintainer who wins is not the one who reads the most diffs.
The maintainer who wins is the one whose queue has been pre-sorted so that the diffs they do read are the only ones that ever needed a human.**

## The Contributor Relationship Is the Hidden Triage

There is a layer underneath all of this, and it is the one maintainers most often neglect, because it is not technical.
Most of the pain of an overflowing queue is not the code.
It is the guilt of unanswered contributors, the dread of opening the tab, and the slow resentment of work that is supposed to be voluntary but has started to feel like a debt.

Automation is part of the answer, but so is setting expectations, because a contributor who knows what to expect does not require a personal reply to stay patient.

Write a `CONTRIBUTING.md` that says what you will and will not accept, what a good pull request looks like, and how long response takes.
Use a pull request template that asks for the linked issue, the motivation, and the test.
Publish a response-time norm, even an honest one: "I review pull requests on Thursdays."
State it, link it in every template, and let the automation reinforce it.
**Predictability is a contribution, and a maintainer who responds every Thursday is more sustainable than one who responds in a burst and then disappears for three months.**

And learn to close fast.
A fast, clear "no, and here is why" is a gift.
It respects the contributor's time, it keeps the queue honest, and it is almost always kinder than a silence that stretches into a year.
The maintainer's fear of seeming ungrateful is what swells the queue past recoverability.
A no is not ungrateful.
A no is an answer, and an answer is all a contributor is waiting for.

## What to Do on Monday

You do not need to build the whole layer at once, and you should not try.
Pick the single thing that is costing you the most attention right now and automate that one.

Add [actions/stale](https://github.com/actions/stale) and let it start closing the pull requests you were never going to get to.
Add [eps1lon/actions-label-merge-conflict](https://github.com/eps1lon/actions-label-merge-conflict) and stop looking at diffs that are not ready to merge.
Add a size labeler and a path-based labeler and make the queue sortable.
Write the `CONTRIBUTING.md` you have been meaning to write, and add the two provenance fields, AI-assisted yes or no, and which model, to the pull request template, so every contribution arrives with the one piece of context this era hides by default.

Then, and only then, wire in the LLM first-pass review.
Start it in shadow mode, posting its summary as a comment without applying any labels, and read along with it for a month.
When you trust its risk and confidence calls, turn the labels on.
When you trust the labels, let the lowest-risk, highest-confidence, smallest changes merge on green.
Each step is a slice of attention you stop spending by hand and start spending on the pull requests that actually need a human.

A sustainable open source project is not one where the maintainer reads everything.
It is one where the maintainer has built a triage layer good enough that almost nothing needs to reach them unread, and what does reach them is exactly what was worth their time.
Build that, one automation at a time, and the queue stops being the thing that owns you.

## See also

- [The Codebase Gardener](../the-codebase-gardener/index.md) - the team-codebase version of the same argument: encode the standard where work is forced to pass through it, instead of carrying it as a per-PR review habit
- [The Merge Gate](../the-merge-gate/index.md) - the case for gating on the blast radius of the change rather than on the existence of a pull request, which is the principle behind risk-based triage routing
- [Rethinking Code Review in the Age of LLMs](../rethinking-code-review-in-the-age-of-llms/index.md) - why an automated first pass plus a precise specification outperforms a tired human scanning a diff, the premise the LLM review layer stands on
- [Defects Flow Downstream, Fixes Must Flow Upstream](../defects-flow-downstream/index.md) - why repeated review comments signal a missing check rather than a missing reviewer, the root of "encode it, do not retype it"

## References

- [actions/stale](https://github.com/actions/stale) - the official GitHub Action for marking inactive pull requests and issues stale and closing them after a configurable window
- [eps1lon/actions-label-merge-conflict](https://github.com/eps1lon/actions-label-merge-conflict) - labels pull requests that no longer merge cleanly and unlabels them once the conflict is resolved
- [actions/labeler](https://github.com/actions/labeler) - the official GitHub Action for applying labels based on the files a pull request touches
- [amannn/action-semantic-pull-request](https://github.com/amannn/actions-semantic-pull-request) - enforces conventional-commit-style pull request titles as a required check
- [Wikipedia, "Theory of Constraints"](https://en.wikipedia.org/wiki/Theory_of_constraints) - Goldratt's framing for why you change the bottleneck station rather than adding effort at it, the basis for moving the maintainer out of the triage station
- [Wikipedia, "Paved road"](https://en.wikipedia.org/wiki/Paved_road) - the principle of making the compliant path the easiest path, applied here to contributor conventions and templates
