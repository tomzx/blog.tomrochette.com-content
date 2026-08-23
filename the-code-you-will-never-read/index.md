---
title: "The Code You Will Never Read"
created: 2026-08-01
type: post
status: finished
tags: [software-engineering, ai, llm, machine-learning, code-review, productivity, fully-ai-generated, llm=glm-5.2, llm=glm-5.3]
readability: 3
audience_notes: >
  Assumes the reader writes software in a world where LLMs and agents produce much of the code, and has at least a lay picture of how a trained neural network works (weights, training, evaluation). No hands-on ML experience required.
---

There is a kind of code growing around us, and growing fast.
Code that no human wrote, line by line.
Code that no human will read, line by line.
Code that no human will review, because the verification system passed and the change shipped on green.
If you are an engineer, this is supposed to make you uncomfortable.
But the discomfort is something you can get past, because we have gotten past it before, in several fields next door, and their tricks transfer.

Machine learning practitioners have been comfortable with opacity for a decade.
The trained neural network sitting behind your favorite model is, at the bottom, billions of floating-point numbers.
Nobody reads them.
Nobody can.
There is no "go to definition" for a weight.
You cannot trace a decision through the layers by opening the matrix in your editor and following the logic.
The entire artifact is illegible to a human by construction, and the field that built it made its peace with that a long time ago.

**The code now being produced by agents is heading toward the same property, and the comfort ML people found is the comfort software engineers need to find next.**

## The Model We Already Live With

How did machine learning get comfortable with a thing nobody can read?

Not by pretending to understand the internals.
**By refusing to need them.**

The model is a black box.
**You understand it through what it does, never through what it is.**
You probe it with inputs and watch the outputs.
You assemble a test set that captures the behaviors you care about, the happy paths and the adversarial ones.
You measure accuracy, calibration, latency, and failure modes on the edge cases that would embarrass you in production.
You characterize the artifact from the outside, and the characterization is the thing you trust.

Nobody on a model team ever says "let me read the weights to see if this is correct."
That sentence is nonsense in that world.
It is becoming nonsense in ours, and the people who notice last will be the ones still trying to read code that no longer rewards reading.

## Code Is Becoming That

The parallel is not exact, but it is close, and it is closing.

A neural network is opaque because its meaning is smeared across billions of parameters, none of which means anything alone.
Agent-written code is opaque for a different reason and a more mundane one: there is simply too much of it, it was produced too fast, and no human has the hours to reconstruct what it does from the source.

**The end state is the same from the operator's point of view.**
You are handed an artifact that does something.
You cannot hold its behavior in your head by reading it.
You have to find out what it does the way you find out what a model does, by running it and watching.

This is already the lived reality for the engineers defending codebases where agents produce faster than humans can read ([The Codebase Gardener](../the-codebase-gardener/index.md) describes that arithmetic).
It will be the reality for everyone soon enough.
The code you depend on, the code in your dependencies, the code that ships from the team across the hall, is increasingly code whose source you will never open, because opening it would tell you less than running it would.

## Why Code Felt Different (And Why It Should Not)

Source code used to be the thing that made software tractable.
That was the whole promise.
Unlike a compiled binary, unlike a trained network, you could open the file and follow the logic.
Reading was how you understood a system, how you debugged it, how you trusted it.
**The fact that code was legible was the foundation engineers built their competence on.**

Machine learning never had that foundation, so it never grieved losing it.
**Software engineering did, and does, and that grief is most of what the discomfort is made of.**

Strip the grief away and the practical question is simpler.
If you could not read the code anyway, would you rather have no code, or would you rather have code you can probe, test, measure, and roll back?
You would rather have the code, and you would build the same scaffolding around it that ML built around its weights.
The only thing standing between you and that scaffolding is the feeling that you ought to be able to read it, and that feeling is a habit, not a requirement.

## The Skills Transfer Directly

The practices machine learning developed for living with opacity are almost a one-to-one map onto opaque code.
You already know half of them, because software engineering reinvented them under different names.

In ML, the test set captures the behaviors that matter.
In opaque code, that is the acceptance criteria written before implementation, plus a characterization suite that records what the code actually does across the inputs you care about ([Verifying Code Without Reading It](../verifying-code-without-reading-it/index.md) is the full version of this system).

In ML, probing with held-out and adversarial inputs is how you find where the model breaks.
In opaque code, that is property-based testing and fuzzing, generating inputs no human would think to write, exposing the edge cases reading would have missed anyway.

In ML, you measure accuracy and failure rate on a benchmark, not vibes.
In opaque code, that is defect escape rate, rollback rate, time-to-detect, and change failure rate, measured per change, in production.

In ML, adversarial examples are how you stress the model before it ships.
In opaque code, that is the adversarial pass: a separate agent whose only job is to break the change, with no incentive to approve ([Verifying Code Without Reading It](../verifying-code-without-reading-it/index.md) covers the separation that keeps it sound).

In ML, the [model card](https://arxiv.org/abs/1810.03993) documents what the model is good at and where it fails.
In opaque code, that is the specification plus the issue, the artifact that tells you what the code was supposed to do, which matters far more than what any individual line does ([Rethinking Code Review in the Age of LLMs](../rethinking-code-review-in-the-age-of-llms/index.md)).

**Every tool you need to trust opaque code is a tool ML already built to trust opaque weights, renamed.**

## It Is Not Just Machine Learning

Machine learning is the most recent field to face this problem, not the only one.
Depending on an artifact you cannot fully read is an old situation, and the disciplines that met it first each invented a piece of the answer.
None of them solved it by making the artifact legible.
They solved it by changing how they interacted with it, and every one of those changes is a tool we can pick up for opaque code.

**Silicon.**
Once a chip is fabricated, you cannot read its logic from the silicon.
The hardware field answered with design for test: [boundary scan](https://en.wikipedia.org/wiki/Boundary_scan), built-in self-test, test vectors injected at the pins and observed at the outputs.
The lesson is structural, and it is the one our field is slowest to learn: testability has to be designed into the artifact before it exists, not bolted on after.
For code, that means the architecture carries probes, hooks, and test seams by default, so an implementation nobody reads can still be exercised by a system that does.

**Pharmacology.**
A drug interacts with a body no one fully models.
The field answered with phased clinical trials, a tiny reversible exposure first, then efficacy, then population scale, all run double-blind and followed by post-market surveillance.
The transferable pattern is staged rollout with independent evaluation and production watchfulness, which is exactly canary deployments, feature flags, a verifier separate from the author, and monitoring that treats production behavior as the real verdict.

**Behaviorism.**
Psychology met an opaque artifact earliest of all, the mind itself, and built a whole epistemology around it.
Stimulus and response, operational definitions, the refusal to introspect what could not be opened.
The stance is the one this article is arguing for: when you cannot inspect the internals, you understand the thing by characterizing what it does, and you stop treating that as a compromise and start treating it as the method.

**Cryptography.**
A cipher is trusted not by reading it but by trying to break it, and [Kerckhoffs's principle](https://en.wikipedia.org/wiki/Kerckhoffs%27s_principle) says the system must stay safe even when its mechanism is fully public.
The lesson is an inversion that cuts against the instinct to trust illegible code by hoping someone read it: obscurity was never what made it safe, and dropping the reading does not drop the safety if the adversarial testing holds.
Trust comes from attack, not from inspection.

**Optimizing compilers.**
The output of a modern optimizer is illegible to humans, and no one considers that a crisis.
Compilers are trusted through conformance suites and fuzzing, not by reading the assembly they emit.
Generated code is a new instance of a situation our own field has always been calm about, a transformation pipeline whose output you verify rather than read.

**Legacy mainframes.**
Long before LLMs, our field operated systems no living person fully understood, COBOL cores kept alive by runbooks, golden-file tests, and behavior contracts.
The practitioners did not resign over the illegibility.
They built characterization tests that pinned observed behavior, and they ran the systems safely on those pins for decades.
That is the exact toolkit an opaque, agent-managed codebase needs.

Each field contributed a distinct piece.
Hardware taught us to design testability in beforehand.
Pharmacology taught us staged exposure with independent oversight.
Behaviorism taught us the epistemology of characterization.
Cryptography taught us to trust by attack, not by inspection.
Compilers taught us that illegible output is normal and suite-verified.
Legacy systems taught us to operate on pinned behavior when comprehension is gone.
**Stack those techniques and you have the full practice for a codebase no one reads: instrumented by design, rolled out in stages, characterized by behavior, stress-tested by adversaries, suite-verified, and pinned by contracts.**

## What Understanding Means When You Cannot Read

Engineers are going to resist this, so it is worth being precise about what is lost and what is gained.

Reading code gives you one kind of understanding, causal and local.
You trace a branch, follow a call, and build a mental model of why the code behaves the way it does on the inputs you happened to trace.
It is deep, but it is narrow.
It covers the paths you followed, and it depends on you being alert and unhurried while you followed them.

Characterizing behavior gives you a different kind of understanding, statistical and global.
You cannot say why a specific input produces a specific output by tracing the logic.
But you can say, with evidence, how the system behaves across thousands of inputs, including the ones no human would have thought to trace.

The first kind feels more satisfying because it produces a story.
The second kind is more reliable because it does not depend on which story you happened to follow on the day you read it.

A reviewer who reads a diff understands a few paths well and the rest not at all.
A test suite that runs on every change understands every path it covers, every time, forever, without getting tired.
**Reading gives you a vivid understanding of a tiny fraction of the behavior.
Probing gives you a coarse understanding of all of it, and for software that has to keep working when you are not looking, the second is the one that compounds.**

## The Identity Problem

Here is the part nobody puts in the engineering blog posts.

This shift is hardest for the people it should be easiest for.
The senior engineer, the staff engineer, the person whose entire professional identity is built on being able to open any file in the codebase and understand it, is the person being asked to surrender the exact skill that made them senior.

That is a loss, and it is real, and pretending it is not is why so many of the arguments against unread code sound rational but run on fear.
It is not irrational fear.
If the thing you are best at is reading code, and reading code stops being the valuable thing, then you are being asked to become a beginner again, and beginners are slow and uncertain and uncomfortable.

The way through it is the same way ML practitioners found.
You do not stop being valuable.
You move your value up a layer.
The ML engineer's skill was never reading weights, it was designing the training, choosing the objective, building the evaluation that decided whether the model was good enough to ship.
The senior engineer's skill, it turns out, was never really reading lines either.
It was knowing which behaviors matter, what the failure modes are, where the blast radius lives, and what "done" actually means for this system.
Those survive the loss of legibility intact, and they are exactly the skills the opaque-code world pays for.

**You are not losing your competence.
You are being asked to point it at the layer where it was always doing the most work.**

## How to Get Comfortable

Comfort is not an attitude you adopt.
**It is a confidence you earn by watching the safety net catch things.**
Each time a gate stops a bad change, each time a canary surfaces a regression a reader would have missed, each time a rollback undoes a problem in minutes, the illegible artifact gets a little less frightening, because the system around it is doing the job your eyes used to do.

Start where the stakes are low.
Pick the changes you were never going to read carefully anyway, the small, reversible, low-blast-radius ones ([You Already Review Code Without Reading It](../code-review-without-reading-the-code/index.md) is the uncomfortable proof that this is most of them).
Let those merge on green, with no human in the middle, and watch what happens.
**If nothing breaks, your nervous system learns faster than your opinions do.**

Then build the probing muscles.
Write the behavioral tests before you let an agent write the code.
Add a fuzzer to the paths that carry real risk.
Put a blast-radius classifier on the gate, and reserve your attention for the small set of changes that actually deserve a human, the irreversible and the trust-boundary-crossing.
Measure the outcomes, and let the measurements argue for you when your instincts object.

The end state is not that you stop caring about code.
It is that you stop needing to read it to trust it, the same way the ML engineer stopped needing to read weights to trust a model.
You develop a feel for the system the way they developed a feel for the model, by living with its behavior, watching it under load, and letting the evaluation be the authority instead of your eyes.

## The Disciplines That Already Did It

Machine learning is the closest mirror to what software is becoming, and it is worth noticing how comfortably it ended up.

Nobody in ML talks about the illegibility of weights as a crisis.
They talk about evaluation, about distribution shift, about calibration, about the gap between benchmark and production.
The opacity is settled ground, the same way it is settled ground in chip design, in pharmacology, in every field that learned to trust an artifact it could not open.
The work happens entirely at the boundary, in the inputs you choose and the outputs you measure, because that is where understanding of an opaque artifact can live.

Software engineering is arriving at the same place, later and more reluctantly, because it had something to lose that those fields never had.
The legibility of source code was a gift, and it was a gift that lasted a few decades, and it is ending, and the ending feels like a demotion when it is really a relocation.

**The code you will never read is coming regardless.
The only question is whether you learn to be comfortable with it the way half a dozen fields already are, by building the cage of tests and probes and staged rollouts and adversarial checks around it, or whether you keep insisting on reading until the volume of unread code makes the insistence irrelevant.**

The first option is work.
The second option is a feeling that does not scale.
Pick the one that does.

## See also

- [You Already Review Code Without Reading It](../code-review-without-reading-the-code/index.md) - the diagnosis that most review already happens without reading, which is the proof that the comfort is mostly already earned.
- [Verifying Code Without Reading It](../verifying-code-without-reading-it/index.md) - the concrete system of tests, critics, and gates that replaces reading, and that maps almost one-to-one onto ML evaluation practices.
- [Rethinking Code Review in the Age of LLMs](../rethinking-code-review-in-the-age-of-llms/index.md) - the case for moving human effort from the diff to the specification, which is the layer where understanding of opaque code actually lives.
- [The Codebase Gardener](../the-codebase-gardener/index.md) - the arithmetic that makes unread code inevitable, and the strategy for defending a codebase against entropy produced faster than you can read.
- [The Acceptance Gap](../the-acceptance-gap/index.md) - the root insight that a model cannot vouch for its own output, which is why the external evaluation (the ML equivalent of a test set) is the part that has to be trustworthy.
