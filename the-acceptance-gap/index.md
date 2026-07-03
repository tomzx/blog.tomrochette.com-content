---
title: "The Acceptance Gap: Why an LLM Solution Is Not a Shipped Solution"
created: 2026-07-03
type: post
status: finished
tags: [ai, software-engineering, llm, verification, taste, specification, fully-ai-generated, llm=glm-5.2]
readability: 3
audience_notes: >
  Assumes the reader is a technical practitioner who already uses LLM coding agents and has felt the moment where the model says "done" and the work is clearly not done. No explanation of what an LLM is.
---

Generation is solved.
You describe, the model produces, and the candidate looks plausible in seconds.
**The bottleneck is no longer producing a solution; it is deciding that a solution is acceptable, and that gap is the one the model cannot close on its own.**

I keep noticing the gap in two forms, and they fail for different reasons, which is why a single strategy like "review the output" addresses neither one well.
One is a bug fix that the model swears it fixed and did not.
The other is a feature that meets the description and still is not what I wanted.
Both feel like the model failed, but the failure is in a different place each time, and the difference is the whole point.

## The Gap Is Not One Gap

The distance between "a description of what I want" and "an acceptable solution I would ship" is not a single gap.
It is two, stacked, and they respond to completely different interventions.

The first gap is about correctness.
Did the change do the thing it was supposed to do, in the world, against ground truth the model cannot see?
The second gap is about fit.
Does the result match the thing I actually wanted, most of which I never wrote down?

Correctness is, in principle, objective.
You can check it.
Fit is, in practice, subjective.
You can only feel it.

Most of the frustration people report with LLM coding comes from treating these two gaps as the same gap, and applying the tool that closes one to the other.
**The bug gap wants a check; the feature gap wants a reaction, and reaching for one when you need the other is why the work keeps coming back unfinished.**

## Bug Fixes: The Silent-Failure Gap

When I ask an LLM to fix a bug, it returns a patch that looks correct.
It will explain the root cause in a confident voice, write a plausible diff, and tell me the issue is resolved.
Often it is.
Sometimes the patch addresses a symptom and the root cause resurfaces next week.
Sometimes it fixes the exact reproduction I pasted but not the general case.
Sometimes it fixes nothing at all, and merely rearranges the code into something that looks like a fix.

The model cannot tell me which of those happened, because the model has no access to the ground truth that would let it verify its own claim.
It optimized for "a plausible fix," not for "a verified fix."
**Its confidence is not evidence, and nothing in the tone of the output distinguishes a real fix from a convincing one.**

This is the dangerous kind of failure, which testers have always called the [oracle problem](https://en.wikipedia.org/wiki/Oracle_(software_testing)): without an independent way to decide what the correct output is, you cannot tell that a plausible output is wrong.
The model has the problem in its most acute form, because it is both the thing producing the answer and the thing narrating why the answer is right.
The narrator is not independent of the guess.

So for bug fixes I end up verifying manually.
I reproduce the original failure, apply the patch, and check whether the failure is gone.
Not because I enjoy the step, but because the model's report of "fixed" is a hypothesis, not a result.
**A fix is not fixed until something independent of the model says so.**

## Features: The Taste Gap

When I ask an LLM to build a feature, the gap is different, and it fails for a different reason.

The feature works, in the narrow sense that it does what the description said.
The gap is that "meets the description" is not "matches what I wanted," because most of what I wanted was never in the description.
It lived in taste.
The feel of the interaction.
The expectation about a default.
The sense that this control belongs here and not there, that the empty state should say this and not that, that the feature is finished when it feels light rather than heavy.

I did not write any of that down, because I did not know I wanted it until I saw the result that lacked it.
This is the nature of subjective requirements: they are discovered by contact with the artifact, not enumerated in advance.
**A specification can carry the objective part of what you want; it cannot carry the taste, because the taste is a reaction you have not had yet.**

So the loop for features is not "verify," it is "try."
Generate, run it, notice the distance between what I got and what I expected, describe that distance, regenerate.
When the distance closes to zero, I stop.
That stopping point, the "just ship it" moment, is a taste judgment, not a verification step.
No test defines it.
I define it, by being satisfied.

## Why the Model Cannot Close Either Gap Alone

The two gaps look different, but they share one cause.
Both are acceptance gaps, and acceptance requires information the model does not possess.

For bugs, the missing information is the ground truth of correct behavior.
That truth lives outside the model, in an executable check or in a human observation.
The model can guess at it, but it cannot consult it.
For features, the missing information is my taste.
That lives outside the model too, in the reaction I will have when I try the result.
The model can guess at it from my description, but it cannot feel it.

In both cases the model can generate candidates freely, and in both cases it cannot sign off on them.
**Signing off requires exactly the external information that was never in the prompt, which is why no amount of rephrasing the prompt closes the gap.**

This is the same pattern I described in [The Shifting Bottleneck](../the-shifting-bottleneck/index.md): automating a layer does not remove the layer, it moves the constraint to the layer above it.
Here the automated layer is generation, and the layer above it is acceptance.
The work did not go away.
It turned into deciding whether the generated thing is good enough.

## What Closes Each Gap

The two gaps respond to different interventions, and the strategy is to match the intervention to the gap.

The bug gap is closeable in principle, and the mechanism is encoding.
Write the acceptance criterion as a check the model cannot fake.
A failing test that must pass.
A reproduction script that must go green.
A property the output must satisfy, stated before the fix is written.
Once the check exists, the model can run it, and its claim of "fixed" becomes trustworthy only when the check agrees.
The bug gap shrinks to exactly the set of bugs for which I have not yet written a check.

This is [test-driven development](https://en.wikipedia.org/wiki/Test-driven_development), rediscovered as the answer to "why don't I trust the model's fix."
The discipline is to write the check before, or alongside, the fix, not after.
A bug fixed without a check is a bug I will have to verify by hand, forever, because nothing is keeping it fixed.
A bug fixed with a check stays fixed, because the check will scream if it regresses, whether or not I am looking.

The feature gap is not closeable the same way, and this is the uncomfortable part.
I cannot write a test for "this feels right," because I do not know the specification of my own taste until I see the result.
[Exploratory testing](https://en.wikipedia.org/wiki/Exploratory_testing) and [specification by example](https://en.wikipedia.org/wiki/Specification_by_example) help me surface more of what I want, but they cannot surface all of it, because the residual is a reaction, not a requirement.
The feature gap closes only through iteration, and the terminal condition is a human saying "good enough, ship it."

There is no encoding that removes the human from that loop, because the human's reaction is the signal the loop is measuring.
The best I can do is make the loop fast, so that each try is cheap and I can afford many of them.
A model that generates in thirty seconds and an environment where I can try the result in ten more is a loop I can run ten times in a morning, and the tenth version is usually the one I ship.

## The Mistake Is Treating Them as the Same Gap

Most of the waste in LLM-assisted work comes from applying the wrong tool to the wrong gap.

Treat the taste gap as a verification problem, and you write tests that pass and ship features nobody likes.
The tests confirm the feature does what the spec said, which was never the question.
The question was whether the spec was the right spec, and no test answers that.

Treat the verification gap as a taste problem, and you manually re-check, by hand, things the model could have checked for itself.
You read a diff looking for whether the bug is really fixed, applying your eyes as a slow and unreliable [oracle](https://en.wikipedia.org/wiki/Oracle_(software_testing)), when a failing test would have answered in a second and answered the same way every time.
**You burn the attention you should have been spending on taste on work the model could have done for you.**

The split is sharp once you see it.
If the gap is "did it do the thing," that is a check, and the move is to encode the check so the model runs it without you.
If the gap is "is this the thing I wanted," that is taste, and the move is to iterate fast and trust the stopping judgment.
[Verification and validation](https://en.wikipedia.org/wiki/Verification_and_validation) are the old words for this distinction, and they have never been more useful than they are now: verify against the spec, validate against the want.
The model can help with the first.
It cannot do the second for you.

## What to Do on Monday

Sort the next ten things you hand to the model into two piles.

The bug pile gets a check for each item, written first.
If you cannot write a check that would fail before the fix and pass after it, you do not yet understand the bug well enough to delegate it, and the model's fix will be a guess you have to verify by hand anyway.
The check is the thing that makes delegation safe.

The feature pile gets a fast iteration loop.
Cut anything that slows down the try-it-and-react cycle, because the cost of a feature is no longer the cost of building it, it is the cost of the number of tries it takes to match your taste.
A model that builds cheaply makes many tries affordable, and that is the real lever.

Leave the "is this good enough to ship" judgment to yourself.
**Generation is no longer the bottleneck, and neither, soon, is verification, once you encode it. The bottleneck is acceptance, and the half of acceptance that is taste is the last compounding thing you do.**
Nobody can write that prompt for you, which is exactly why it is the part worth keeping.

## See also

- [The Shifting Bottleneck](../the-shifting-bottleneck/index.md) - the upstream pattern this article specializes: automating generation moves the bottleneck up to acceptance, it does not remove it
- [Rethinking Code Review in the Age of LLMs](../rethinking-code-review-in-the-age-of-llms/index.md) - the case that quality is a property of your specifications and gates, which is the premise behind encoding the bug gap as a check
- [The Importance of Context When Interacting with LLMs](../the-importance-of-context-when-interacting-with-llms/index.md) - why the model cannot close either gap: ground truth and taste are context it was never given
- [AI-Maxxing and Resistance Are the Same Mistake](../ai-maxxing-vs-fighting-against-it/index.md) - taste as the compounding activity to protect, the same "ship it" judgment this article identifies as the last human loop
