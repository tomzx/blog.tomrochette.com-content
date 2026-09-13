---
title: "What a Senior Engineer Owes Their Reviewer"
created: 2026-09-13
type: post
status: finished
tags: [software-engineering, code-review, pull-requests, processes, fully-ai-generated, llm=glm-5.3-flash]
readability: 3
audience_notes: >
  Assumes the reader works on a team that uses pull request review and has both authored and reviewed PRs. No explanation of what a PR or CI is.
---

When a senior engineer opens a pull request, the reviewer should be able to start judging the change, not excavating it.
**The standard is that everything which did not require a second brain is already done before the review request goes out.**
CI is green, the diff is small and single-purpose, the description explains the change, the author has already read their own diff, and the proof that it works is in the PR.
Anything less quietly converts review time into discovery time, and discovery is the most expensive way to use a reviewer.

## The Standard Expectations

Stripped of argument, here is what a reviewer can assume when a senior engineer opens a PR:

- CI is green on the latest commit.
- The diff does one thing; refactors and behavior changes live in their own PRs.
- Stray logs, commented-out code, and unrelated reformatting are gone.
- The author has read the full diff as a stranger would and annotated the lines that need context.
- The description answers what changed, why, and how it was tested, and points at where to look closely and what is out of scope.
- Proof that it works is in the PR: tests for new behavior, plus written manual verification when tests are impractical.
- The requested reviewers own the subsystem you are touching, not whoever is idle.

**Each of these assumptions a reviewer has to re-verify by hand is attention taken away from judging the change.**
When one of them breaks, the reasonable response is not a comment, it is returning the PR to draft.

## The Cost of a Round Trip

The unit of waste in review is the round trip: the author requests review, the reviewer finds a gap, comments, and the change then sits in a queue until both people are free at the same time again.
One round trip costs four context switches, two per side, plus a wait for the other person's next open slot.
The reviewer switches out of their own work to read the diff and back into it after commenting, and the author later switches out of their work to address the comment and back into it after pushing the fix.
Because each switch means rebuilding the mental state you had before the interruption, a gap the author could have closed in minutes costs days of calendar time.
**Every expectation in the standard above exists to delete one class of round trip.**
A green build deletes the "your build is broken" loop, a single-purpose diff deletes the "split this up" loop, an annotated self-review deletes the "what is this line for" loop, and real proof deletes the most expensive loop of all, "your tests do not cover this", which costs a test rewrite plus a full second pass.
Research on real reviews backs the self-review half of the deal: in industrial code review, most comments ask for improvements and clarifications rather than catching real defects ([Bacchelli and Bird, 2013](https://www.microsoft.com/en-us/research/publication/expectations-outcomes-and-challenges-of-modern-code-review/)), and Google's study of its own process treats small, fast changes as the mechanism that keeps review load sustainable ([Sadowski et al., 2018](https://research.google/pubs/modern-code-review-a-case-study-at-google/)).
**Review latency is mostly queueing, not judging, and the standard is how you stop feeding the queue.**

## The Handoff Contract

Review is a handoff, and a handoff has two sides.
The author's side is logistics: prove the change works, make it easy to read, explain why it exists.
The reviewer's side is judgment: design, correctness, and whether the code will still make sense in a year.
When the author skips their half, the reviewer inherits it.
**A PR that forces the reviewer to reconstruct the intent is a PR that was opened too early.**

The division of work looks like this:

```mermaid
flowchart LR
    subgraph Author["Author, before opening"]
        A1[CI green]
        A2[Self-review done]
        A3[Description written]
        A4[Proof of testing]
        A5[Small single-purpose diff]
    end
    A1 --> O[Open PR]
    A2 --> O
    A3 --> O
    A4 --> O
    A5 --> O
    O --> R["Reviewer: judgment only<br/>design, correctness, maintainability"]
```

## Small, Single-Purpose Diffs

The highest-leverage habit is also the dullest one: keep the diff small.
[Google's engineering practices](https://google.github.io/eng-practices/review/developer/small-cls.html) make the case from experience, small changes get reviewed faster and more thoroughly, and reviewers miss fewer defects.
Size is not the only variable though, purpose is.
**A senior engineer separates refactoring from behavior changes, because a diff that does two things forces the reviewer to review both at once and catch neither.**
If a PR needs a live walkthrough before anyone can understand it, that is usually a sign the PR is several PRs wearing a trench coat.

There are legitimate exceptions, a generated-code migration or a mechanical rename can be large and still easy to review.
The mark of a senior engineer is knowing which kind of large diff they have, and saying so in the description.

## Self-Review Before Anyone Else Reviews

Before requesting review, the author reads their own diff on the same screen the reviewer will use, the Files Changed tab, end to end.
This pass has two jobs.
The first is debris removal: stray logs, commented-out code, leftover debugging, unrelated reformatting that inflates the diff.
The second is annotation: leaving comments on the lines that need context, "this mirrors the logic above", "this limit matches the upstream API", so the reviewer does not have to ask.

**Self-review is also where a senior engineer catches the embarrassing stuff, and catching it yourself is the whole point of being senior.**
Every defect the author removes before the review is a round trip that never happened.

## A Description That Answers the Obvious Questions

The description exists so the reviewer never has to ask questions the author could have answered in writing.
The questions are predictable:

- What does this change do, and why is it needed?
- How was it tested?
- What should the reviewer look at most closely?
- What is deliberately out of scope?

Screenshots for UI changes, before-and-after output for behavior changes, and a link to the ticket all belong here.
**The ticket link is a pointer, not a description.**
A reviewer who has to read the ticket to know what the PR does has been given homework instead of a review request.

## Proof That It Works

The author's job is to demonstrate the change works, not to believe it works.
That means tests for new behavior, updated tests for changed behavior, and a written note on manual verification when tests are impractical ("ran the migration against a copy of staging, 4.2M rows, 90 seconds").
I put this in the description under "How I tested this".
The reviewer's job is then to audit the proof: are the tests real assertions or tautologies, do they cover the failure modes, is the manual claim plausible.
**An author who ships "seems to work" is asking the reviewer to do QA on a hunch, and most reviewers will price that in with a request for changes.**

## After You Open It

**The standard does not end when the PR is opened.**
Watch CI and fix failures immediately; a PR with a red build is blocking a reviewer for nothing.
Respond to comments within a day, even if the answer is "I'll get to this Thursday".
Push fixes as commits so the reviewer can see what changed since their last pass, and say when the PR is ready for a re-review.
When a comment thread passes about twenty back-and-forths, take it to a call and write the conclusion back into the PR.
And when you disagree with a reviewer, either convince them, accept the change, or escalate; a senior engineer does not let a PR rot in a stalemate.

## When You Cannot Meet the Standard Yet

The standard has legitimate exceptions, and seniority shows in running the exception protocol instead of quietly lowering the bar.
Sometimes the approach is still unsettled, sometimes a change cannot be split cleanly, and sometimes you need early eyes to avoid building the wrong thing for a week.
Each case has a protocol that keeps discovery on the author's side of the handoff:

- **The approach is unsettled:** settle it in a short design note or issue before writing code; a paragraph of prose resolves an approach faster than three rounds of review comments on code headed for the trash.
- **You need early feedback:** open the PR as a draft and name the exact question and the lines that answer it, for example "design feedback on the cache interface only, ignore the internals".
- **The diff is unavoidably large:** stack it, base each PR on the previous one, and keep every PR in the stack single-purpose so the reviewer can approve them in order.

```mermaid
flowchart TD
    Q{"Cannot meet the<br/>standard yet?"} -->|"Approach unsettled"| D["Design note or issue<br/>settle the approach first"]
    Q -->|"Early feedback needed"| E["Draft PR<br/>name the question and the lines to read"]
    Q -->|"Diff too large"| S["Stacked PRs<br/>each one single-purpose"]
    D --> R["Then open a PR<br/>that meets the standard"]
    E --> R
    S --> R
```

**The difference between a draft and a premature PR is that the draft tells the reviewer what to look at, and what to ignore.**
"Is this the right approach?" is a question a reviewer can answer in five minutes.
"What is this PR doing?" is homework.

## Make the Standard the Default

None of the seven expectations should depend on memory, because memory fails on exactly the days the standard matters most, the rushed ones.
Encode it once and let the system carry it:

- A PR template with the four description questions already written out.
- Format and lint gates in CI, so reformatting noise never reaches a human-reviewed diff.
- A draft-first habit: every PR is born as a draft and only flips to ready when the checklist passes.
- Reviewer assignment by code ownership, so requests route to the subsystem's owners instead of whoever is idle.

There is a quieter reason a senior engineer holds this line.
**A senior engineer's PRs are the template the rest of the team copies, because people calibrate to what actually gets merged, not to what a wiki says.**
The first time the team watches its most senior member ship a rushed PR to quick approvals, the written standard is dead.
If you want to change how a team reviews, change what its most visible engineers ship.

## What to Do Next

Before you click "Request review" next time, walk the seven expectations in the list above one last time, in order.
Then go a step further and audit your last three merged PRs: find the expectation you break most often under deadline pressure, and encode it once, as a template line, a CI gate, or a personal checklist item.
A standard you re-derive from memory every time will erode; a standard encoded in the system survives your worst week.
None of this requires talent.
**It is the difference between treating review as a service you consume and a contract you enter, and seniority is mostly showing up on the right side of that contract.**

## See also

- [Reviewing code](../processes/reviewing-code/index.md) - the reviewer-side counterpart of this piece