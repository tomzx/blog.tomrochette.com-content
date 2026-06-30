---
title: "Defects Flow Downstream, Fixes Must Flow Upstream"
created: 2026-06-30
type: post
status: finished
tags: [ai, software-engineering, sdlc, llm, specification, fully-ai-generated, llm=glm-5.2]
readability: 3
audience_notes: >
  Assumes the reader is a senior engineer, architect, or engineering lead who already works with LLM-generated code and is deciding where across the software development lifecycle to spend effort. Comfortable with the basics of specification, review, and CI as distinct pipeline stages.
---

The further upstream a defect is born, the more code it contaminates, and the more expensive it becomes to remove.
This has been true for as long as software has had a lifecycle.
Two things have changed, and both point the same way.
The generation step is now automated, so upstream defects are materialized downstream at machine speed, and the old habit of patching them in place no longer buys what it used to.
**Once the pipeline executes itself, the only durable fix is the one made at the source, and every fix made downstream is a patch you will have to make again.**

## The Pipeline Has Always Run One Way

Software development is a cascade.
Each stage constrains the next: needs become requirements, requirements become a specification, the specification becomes an architecture, the architecture becomes code, the code is verified, shipped, and operated.
A decision at any stage narrows the space of what is possible at every stage below it, and an error at any stage is inherited by everything that descends from it.

This directionality is why the cost of removing a defect rises so steeply the later you find it.
[Boehm and Basili](https://doi.org/10.1109/2.962984) put a number on it more than two decades ago: finding and fixing a software problem after delivery is often a hundred times more expensive than finding and fixing it during requirements and design.
The exact multiplier is debatable, but the shape of the curve is not.
**Each stage a defect survives multiplies its removal cost, because each stage builds artifacts on top of it that all have to be reworked when the foundation moves.**

The industry already has a name for the obvious response.
It is called [shift-left testing](https://en.wikipedia.org/wiki/Shift-left_testing), and the move it prescribes, pushing verification earlier in the lifecycle, is correct as far as it goes.
But shift-left is a half-measure, because it moves the act of checking earlier without moving the act of fixing to where the defect was born.
The deeper move is not "test earlier."
It is "fix at the origin," and the two are not the same.
Testing earlier finds the symptom sooner; fixing at the origin ensures the symptom is never generated again.

## The Amplifier Got an Engine

Before LLMs, a human wrote the code, and the human was a lossy interpreter of the specification.
That lossiness was quietly load-bearing.
When the spec was ambiguous, the human made a judgment call, often a reasonable one, and that judgment absorbed some of the upstream defect before it could reach the running system.
The defect still propagated, but through a mind that could correct it on the way down.

The model does not absorb ambiguity.
It resolves it, once, in the direction of whatever is most probable, and then it materializes that resolution across every file it touches.
**The generation step stopped being a filter and became an amplifier, and it amplifies whatever it was given, including the gaps.**
One ambiguous line in a specification becomes a dozen consistent, plausible, uniformly wrong code paths, in seconds, and they all look correct because they all agree with each other.

This is the real intensification.
The cost curve was always steep, and it is now steep and fast.
The window in which a human used to catch an upstream defect by "just writing the code" has closed, because the code writes itself before the human has time to notice the spec was vague.
By the time anyone reads the output, the upstream defect has already been faithfully reproduced across the diff, and the reviewer is left arguing with the symptom instead of the cause.

## Why Consequences Fan Out

The reason early stages outrank late stages is not only that they are cheaper to fix.
It is that their defects multiply downstream while late-stage defects mostly do not.

A bug in code affects the code that contains it.
A gap in the architecture affects every component built on top of it.
A missing or wrong requirement affects every architecture that tries to satisfy it, every component that implements it, every test that verifies it.
**The earlier the stage, the larger the fan-out, because the larger the subtree of artifacts that descend from it.**

This is why a specification defect is not just "a bug, but earlier."
It is a different category of problem, one whose blast radius grows with the distance from the source.
A single ambiguity in a spec can be the common ancestor of a hundred production incidents, each of which looks like a separate bug to the engineer who responds to it, and each of which is, in fact, the same bug wearing different clothes.
Treat them as separate bugs and you will fix a hundred symptoms.
Treat them as one and you fix the spec once.

Nancy Leveson reached the same conclusion from the study of accidents in [Engineering a Safer World](https://direct.mit.edu/books/oa-monograph-pdf/2280500/book_9780262298247.pdf).
Serious failures are rarely caused by a single component breaking.
They are caused by flawed control structures upstream that set the components up to fail in concert, and the component failure is merely the place the upstream flaw became visible.
The component is the symptom.
The control structure is the cause.
Fixing the component prevents that one incident, and fixing the control structure prevents the class.
**A pipeline stage is a control structure, and in software the earliest stages are the ones with the widest reach.**

## The Fix Belongs Upstream

Here is the operational consequence, and it is the whole argument in a single rule.

When a defect appears in code, there are two places to fix it.
You can fix the code, which removes the symptom from this instance.
Or you can fix the upstream artifact that produced the code, which removes the cause from every instance.

These look similar and are not.
A code fix is a non-compounding fix.
It patches one occurrence, leaves the source intact, and guarantees that the same defect will be regenerated the next time the pipeline runs against the same upstream artifact.
A spec fix is a compounding fix.
It changes the source, and every future generation inherits the correction automatically, for as long as the artifact exists.

This is the same compounding-versus-one-time distinction that makes specification outrank review, as [Rethinking Code Review in the Age of LLMs](../rethinking-code-review-in-the-age-of-llms/index.md) argues: review catches a defect once, for the reviewer who happens to be reading, while a spec prevents the whole class from being generated.
The principle does not stop at review.
It runs the entire length of the pipeline.
**The defect you patch in code today is the defect the model writes again tomorrow from the same ambiguous spec, and the defect you fix in the spec today is the defect the model never writes again.**

The discipline this implies is uncomfortable for teams that grew up triaging bugs at the bottom of the pipeline.
It says that most "code bugs" in an AI-assisted codebase are not code bugs at all.
They are specification bugs, or architecture bugs, that happened to surface in code.
Treating them as code bugs, by fixing the code, is treating the symptom while leaving the disease in place to generate fresh symptoms next sprint.

A useful diagnostic comes straight from [the five whys](https://en.wikipedia.org/wiki/Five_whys) and the Toyota [andon](https://en.wikipedia.org/wiki/Andon_%28manufacturing%29) tradition: when the same class of bug appears more than once, stop the line, walk back up the pipeline asking why until you reach a process cause, and fix the process, not the product.
Fixing the product gets you a working unit today.
Fixing the process gets you a working line forever.
The two investments have almost nothing in common, and teams that confuse them spend their lives re-fixing the same bug in new files.

## What This Changes About Where You Spend Effort

If consequences amplify downstream and fixes compound upstream, then the allocation of engineering effort across the lifecycle is exactly inverted from where most teams spend it.

Most effort sits at the bottom of the pipeline.
Writing code, reviewing code, fixing code, fighting fires in production: these are the stages with the smallest blast radius and the least compounding return.
They feel urgent because they are where the pain is visible, but they are also where an hour of effort buys the least durable improvement, because the upstream artifacts that produced the pain are still in place, still generating.

The high-leverage stages are at the top.
Requirements, specification, and architecture are the stages whose defects fan out the widest and whose fixes compound the longest.
They feel less urgent because the pain they cause has not happened yet, and when it does happen it will be blamed on the code, not on the spec that produced the code.
**The trap is that the bottom of the pipeline is loud and the top of the pipeline is quiet, and most teams optimize for the noise rather than for the leverage.**

This is the same relocation [The Shifting Bottleneck](../the-shifting-bottleneck/index.md) describes from a different angle.
Once code writes itself, the bottleneck moves to verification, and the highest-leverage response is not to verify harder but to specify better, because specifying better reduces the volume of bad output that verification ever has to catch.
**The pipeline does not reward you for being good at a late stage.
It rewards you for making the late stage unnecessary by being good at an earlier one.**

## What to Do on Monday

A few concrete moves follow, and each is an inversion of the default.

Treat every repeated bug class as an upstream defect.
When the same kind of issue shows up a second or third time, stop fixing it in code.
Walk back up the pipeline until you find the artifact that allowed it, and fix that.
The rule is blunt and useful: fix at the source once, or fix at the symptom forever.

Invest disproportionately in specification.
The spec is now the highest-leverage artifact in the pipeline, because it is the stage whose defects fan out the widest and whose fixes compound the longest.
A team that under-invests here pays for it in every downstream stage, forever, at machine speed, and a team that over-invests here barely notices the downstream stages at all.

When you review, review the spec, not the code.
Code review catches symptoms once, on the diff that happens to be in front of the reviewer.
Spec review prevents classes of symptoms from being generated at all, across every future diff.
An hour on the spec outranks an hour on the code, because the code is downstream of the spec and the spec constrains every diff that will ever be written from it.

Keep an upstream ledger on incidents.
When something breaks in production, record not just the code-level cause but the pipeline stage where the defect was actually born.
Over a quarter the pattern will show which upstream stages are leaking the most, and that is where investment pays back the most, because a single fix there retires a whole family of incidents.

And when the model produces bad output in the same module twice, do not write a longer prompt.
Fix the module, or fix the spec that describes it, because as [The Importance of Context When Interacting with LLMs](../the-importance-of-context-when-interacting-with-llms/index.md) argues, the upstream artifacts are the model's context, and bad output is the most honest signal you will ever get about where that context is incoherent.
The model is showing you the leak.
The right response is to fix the pipe, not to mop the floor faster.

## The Lifecycle Runs One Way

Defects ride the pipeline downstream and multiply as they go.
Fixes can ride it upstream, and they multiply too, but in the opposite direction: one fix at the source prevents a thousand fixes at the symptom.

The team that understands this spends its best hours at the top of the pipeline, writing specifications and architectures that make most downstream defects impossible.
The team that does not spends its best hours at the bottom, fixing code that the pipeline keeps regenerating from sources it never touches.
Both teams are busy.
Only one of them is getting durable work done.
**In an era when the downstream stages execute themselves, the only engineering that compounds is the engineering done at the top of the pipeline. Everything below it is maintenance.**

## See also

- [The Shifting Bottleneck](../the-shifting-bottleneck/index.md) - why automating generation relocates the constraint first to verification and then to specification, the relocation this article turns into a rule about where to fix
- [The Foundation Predicts the House of Cards](../the-foundation-predicts-the-house-of-cards/index.md) - the upstream artifacts (specification, architecture, tests, written conventions) as the foundation whose defects decide whether generated code stands up
- [Rethinking Code Review in the Age of LLMs](../rethinking-code-review-in-the-age-of-llms/index.md) - the compounding-versus-one-time distinction between specification and review that this article generalizes across the entire pipeline
- [Software Engineering Teams in the Age of AI](../software-engineering-teams-in-the-age-of-ai/index.md) - specification named as the highest-leverage skill, which is the same conclusion reached from the team-process side
- [The Importance of Context When Interacting with LLMs](../the-importance-of-context-when-interacting-with-llms/index.md) - the upstream artifacts as the model's context, the mechanism by which an upstream defect becomes a downstream code bug
- [Learn the Foundation, Not the Syntax](../learn-the-foundation-not-the-syntax/index.md) - the durable mental models that let an engineer trace a code symptom back to its upstream cause instead of patching it in place

## References

- [Boehm and Basili, "Software Defect Reduction Top 10 List"](https://doi.org/10.1109/2.962984) - the finding that a defect fixed after delivery is often around a hundred times more expensive than one fixed at requirements, the original cost-of-fix curve
- [Leveson, "Engineering a Safer World"](https://direct.mit.edu/books/oa-monograph-pdf/2280500/book_9780262298247.pdf) - the argument that accidents trace to flawed upstream control structures rather than component failures, so the component is the symptom and the structure is the cause
- [Wikipedia, "Theory of Constraints"](https://en.wikipedia.org/wiki/Theory_of_constraints) - the pipeline framing in which improving one stage relocates the constraint rather than removing it
- [Wikipedia, "Shift-left testing"](https://en.wikipedia.org/wiki/Shift-left_testing) - the existing industry term for moving quality earlier, framed here as a partial move that checks sooner without fixing at the origin
- [Wikipedia, "Five whys"](https://en.wikipedia.org/wiki/Five_whys) - the practice of walking back from a symptom to its process cause before fixing, the root of the "fix the process, not the product" rule
- [Wikipedia, "Andon (manufacturing)"](https://en.wikipedia.org/wiki/Andon_%28manufacturing%29) - the Toyota practice of stopping the line to fix the source of a defect rather than passing it downstream
- [Wikipedia, "No Silver Bullet"](https://en.wikipedia.org/wiki/No_Silver_Bullet) - Brooks's split between accidental and essential complexity, where most late-stage fixing is accidental work that better upstream artifacts would eliminate
