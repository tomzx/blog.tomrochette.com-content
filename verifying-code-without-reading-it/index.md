---

title: "Verifying Code Without Reading It"
created: 2026-07-25
type: post
status: finished
tags: [software-engineering, code-review, pull-request, testing, llm, productivity, fully-ai-generated, llm=glm-5.2, llm=glm-5.3]
readability: 3
audience_notes: >
  Assumes the reader accepts that human line-by-line review of LLM-generated code is not scaling, and now wants the concrete system that replaces it. Familiarity with tests, linters, static analysis, and CI is assumed.
agent_sessions:
  - ses_06934dd48ffeox2IBEs9UprRKM
  - ses_06374508bffeM2tUUiojYK7ntr
---

It is a familiar observation by now that most code review happens without anyone reading the code ([the case is made in You Already Review Code Without Reading It](../code-review-without-reading-the-code/index.md)).
That observation leaves a question hanging.
If no human reads the diff, how do you still get correctness, maintainability, extensibility, and the rest of the things review was supposed to deliver?

The short answer is that you stop trying to read, and start trying to verify.
Reading is one tool doing many jobs poorly.
Verification is many tools, each doing one job well.
**Done right, the unread change is checked more thoroughly than the read one ever was.**

## Decompose What "Reading" Was Checking

When a reviewer reads code, they are not doing one thing.
They are running a dozen checks in their head at once, and doing each of them inconsistently.
Make those checks explicit, and a different picture appears.

Correctness: does the code do what the task actually asked for?
Tested: are the behaviors that matter covered by tests that would fail if the code were wrong?
Maintainable: is the complexity bounded, the duplication low, the naming consistent, the dead code absent?
Extensible: can the next change plug in without a rewrite, or has this change welded two things together that should stay apart?
Secure: does it cross a trust boundary, leak a secret, or open an injection path?
Reversible: if this is wrong, can we undo it in minutes, or does it mutate data we cannot get back?

A tired reviewer scans for all of these at once and catches each of them sometimes.
**The move is to give each property its own check, run on every change, without getting tired.**

## Match Each Property To Its Best Checker

Every property above has a checker that is cheaper and more reliable than a human reading a diff.

Correctness is checked by tests, and by an LLM judge that compares the diff against the acceptance criteria from the issue and asks: is there a case where the criteria hold but this code fails?
Tested is checked by coverage gates and by [mutation testing](https://en.wikipedia.org/wiki/Mutation_testing), which mutates the code and fails the build if the tests still pass, because that means the tests were not testing anything.
Maintainable is checked by complexity limits, duplication detectors, dead-code scans, and linters, all deterministic, all running every push.
Extensible is checked by dependency-direction rules, boundary tests, and an LLM critic that asks where the next feature would plug in and whether this change has made that harder.
Secure is checked by static analysis, secret scanning, and an adversarial LLM pass that tries to find the input the author did not think of.
Reversible is checked by a blast-radius classifier: did this touch the schema, the public API, an external commitment, or a trust boundary?

None of these requires a human to read the code.
**Together they cover everything a reader was supposed to cover, and they cover it on every change, not on the changes a reviewer happened to be alert for.**

## The LLM As Critic, Not Reader

The LLM's role in this system is not to read the code for you.
A summary of the diff is theater with a different font.
The LLM's role is to act as a critic against a single, stated property.

Give it the diff, the specification, and one question.
Does this change introduce a coupling that violates the intended dependency direction?
Is there an input that bypasses the authorization check the spec requires?
Does this function do something the acceptance criteria never asked for?
One question per critic, phrased so the answer is either a concrete failing case or a pass.

This is verification, not reading.
It is adversarial by construction: the critic is rewarded for finding a problem, not for approving.
And because each critic has one job, you can run many in parallel, each a different prompt, each looking for a different class of failure.
**A human reader tries to notice everything and notices some of it.
A battery of critics tries to notice one thing each and notices it every time.**

## Verification Is Not Validation

There is a distinction worth holding onto, because the system fails if you blur it.

[Verification](https://en.wikipedia.org/wiki/Verification_and_validation) asks: did we build the thing right, does the code meet its specification?
Validation asks: did we build the right thing, does the specification solve the real problem?

Reading a diff does verification badly and validation not at all.
No amount of staring at code tells you whether the feature should exist.
That judgment has to live somewhere, and the productive place for it is upstream, in the specification, and downstream, in production.

So split the work.
Put verification in the automated gates, where machines check the code against a precise spec on every change.
Put validation upstream, where humans decide which problems are worth solving and write the acceptance criteria that encode that judgment.
Put a third layer of validation downstream, in canaries, monitoring, and fast rollback, where production behavior is the ground truth no diff review can match.

**The human does not read the code.
The human writes what the code must satisfy, and then watches what the code does in production.**

## The Circularity Trap

There is one failure mode that will quietly ruin this system if you let it go unchecked.
Do not let the same model, or the same prompt, both write the code and approve it.

When the author and the verifier share a mind, the verifier inherits the author's blind spots.
A model that wrote a subtle bug will, asked to review its own work, tend to confirm that the work is fine.
This is not malice; it is the same statistical process producing both answers.

The defense is structural.
Use a different model for verification than for generation, or at minimum a different agent with a different prompt and different access to the specification.
Write the verification criteria before the code exists, so they describe the intended behavior rather than rationalizing whatever was built.
And run an adversarial pass whose only goal is to break the change, with no incentive to approve.

**Separation of concerns is not a nicety here; it is the whole reason the system can be trusted.**

## What The Human Does Instead

If the human is not reading diffs, what are they doing?

They write the specification and its acceptance criteria, because that is where validation lives and where the LLM's verification is anchored.
They review the rules the gates enforce, not the code the gates pass, because a bad rule approved once produces bad approvals forever, while a bad line of code is caught by a good rule.
They respond to gate failures, which is where their judgment adds value, instead of spending it on changes that passed cleanly.
And they read code only on the small, flagged minority of changes that carry real blast radius, where a deliberate read is still the best tool we have.

The new division of labor is more work at the top of the pipeline and less at the bottom, which is the right inversion.
**You are trading a low-leverage activity that scaled poorly (reading every diff) for a high-leverage one that compounds (writing the rules and specs that check every diff).**

## How You Know It Is Working

The objection that will come is simple: how do you know the unread code is good enough?

You do not answer it by pointing at how much code you read.
You answer it by measuring the outcomes reading was supposed to produce.

Track defect escape rate, the bugs that reach production per change.
Track rollback rate, how often a merged change has to be undone.
Track time-to-detect, how quickly a regression surfaces after it lands.
Track change failure rate, the fraction of deployments that cause an outage.

Run the new system on a slice of changes and compare these numbers to your old, human-read pipeline.
If the gates have a lower defect escape rate and a faster cycle time than your reviewers did, the unread code is provably better than the read code was.
If they do not, you have a concrete gap to close, by tightening a rule or adding a critic, not by urging reviewers to read harder.

**The standard is not "a human looked at it."
The standard is "the code behaves well in production, measurably, on every change."**
A human looking at it was always a proxy for that standard, and a weak one.
Replace the proxy with the thing it was standing in for.

## See also

- [You Already Review Code Without Reading It](../code-review-without-reading-the-code/index.md) - the diagnosis this article answers: review already does not involve reading, so build the system that makes that safe.
- [Rolling Out the Unread Review](../rolling-out-the-unread-review/index.md) - the team-side companion to this system: how to ship it to people who do not trust it yet.
- [Rethinking Code Review in the Age of LLMs](../rethinking-code-review-in-the-age-of-llms/index.md) - why reading LLM-written code is the wrong tool, and where human effort belongs instead.
- [The Merge Gate](../the-merge-gate/index.md) - which changes still deserve a human, selected by blast radius rather than by the existence of a pull request.
