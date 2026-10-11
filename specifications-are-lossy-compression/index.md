---
title: "Specifications Are Lossy Compression"
created: 2026-10-11
type: post
status: finished
tags: [ai, software-engineering, llm, ai-agents, specification, formal-methods, intent-driven-development, fully-ai-generated, llm=deepseek-v4.1-flash]
readability: 3
audience_notes: >
  Assumes the reader is an engineer or tech lead who writes requirements or specifications before code and runs coding agents. Familiarity with formal methods helps but is not required; each method is introduced in a sentence.
agent_sessions:
  - ses_edc07e3e4ffeSWHFSfk6Pe5fXx
---

Every document we write before the code is a compressed copy of the code, and the compression drops information.
A requirement, a user story, a specification, a BDD scenario, and a unit test are each a smaller description of a larger artifact.
**None of them can reproduce the code they describe, so all of them lose something, and an LLM agent fills the missing part with a confident guess.**
The useful question is not how to write a better description.
It is which ways of defining software can carry the whole program, and where the missing part should go for the ones that cannot.

## Lossy is a precise word

The idea of measuring an artifact by the shortest description that reproduces it comes from [Kolmogorov complexity](https://en.wikipedia.org/wiki/Kolmogorov_complexity).
The Kolmogorov complexity of a string is the length of the shortest program that outputs it, and a description is lossless when the original can be reconstructed from it exactly, the way a decompressor reconstructs a file.
**A definition of software is lossless when a machine can decide, without a person, whether any candidate implementation is acceptable.**
Reconstruction is the stronger test, since the definition would have to determine exactly one program.
Decidability is the test that matters, since it lets a checker accept every correct program and reject the rest.

A program carries two kinds of information, and only one of them is about behavior.
The first is what the program must do, which is its inputs, its outputs, and the rules that connect them.
The second is how it does it, which is the data structures, the order of operations, the split into modules, the names, and the tradeoffs between speed and memory.
A prose artifact tries to carry the first kind and drops the second almost entirely.

The second loss is larger than the first.
Prose states behavior in natural language, and the meaning of a sentence depends on the reader.
Two readers, or one reader on two days, will turn "the service should stay available during a deploy" into different code, because the sentence never fixed what available means, how long a deploy may take, or what happens to requests already in flight.
**A natural-language specification is lossy twice.**
**It drops the implementation choices, and it leaves the behavior it does state open to interpretation.**

## Why the loss stopped being benign

For most of software's history the reader of a requirement was a person, and by reader I mean whoever turns the definition into code.
The person absorbed the loss.
A person carried context between documents, inferred the unstated from experience, and asked a colleague when a sentence was ambiguous.
The loss was worth accepting, because the thing it saved was the expensive one, which was writing the code.
Compressing a large program into a small document saved the effort of producing the program.

Both conditions have changed.
The reader is now an agent that begins with no history, so anything the definition does not state is absent, and the agent fills the absence with a plausible guess instead of a question.
The cost of producing code has also fallen far enough that compressing it to save writing no longer pays.
**The expensive artifact is now the verified definition, and the document that used to save work has become the place where the work is lost.**

[The Prompt Is the Source Code](../the-prompt-is-the-source-code/index.md) described this failure from the maintenance side, where the code reaches the maintainer without the intent that produced it and the next maintainer has to reconstruct that intent.
This piece locates the same failure one step earlier, in the definition itself, and asks what a definition would have to be to keep the information rather than lose it.
Keeping the prompt is necessary but not sufficient, because the prompt is the best available record of the intent and the checker is what turns that record into a lossless definition.

## No set of words will be lossless

The search for a perfect prose specification has no solution.
By the definition of Kolmogorov complexity, the shortest description of an object that cannot be compressed is about as long as the object, so a natural-language description that determined a nontrivial program would be at least as large as the program and no easier to read.
A shorter document always leaves something out, and the thing it leaves out is the behavior and the choices that made the program complex.

A picture of the recovery sense of loss makes the gap concrete.
It shows how much of the program each form brings back, which is the intuitive sense of compression.

![Six horizontal bars of equal total length, labeled from top to bottom: the code, executable specification, checked specification, property test, example test, and prose requirement. The solid blue part of each bar is what the definition brings back and it shrinks from top to bottom; the faded remainder is what the reader supplies.](images/artifact-compression.svg)

The code bar is full here because the picture measures the artifact, the behavior and the choices together.
What the code itself leaves out is the reason it exists, which the picture does not measure.
A checkable definition is also stronger than this picture suggests, because it is lossless in the decidability sense even when it recovers only part of the implementation.

If the definition cannot be a shorter description in another language, it has to be one of three things.
It can be the same object, which is the code itself or something a compiler turns into the code.
It can be a statement a machine can check against the code.
Or it can be a record of the choices the first two cannot carry.
Three ways cover the first two, and a fourth covers the residue.

## Four ways to remove the loss

### Make the definition the source

The first way is to stop describing the code and generate it.
A domain-specific language, a schema, or a model is the source of truth, and a compiler turns it into the artifact, so no separate description exists to lose anything.
[Literate programming](https://en.wikipedia.org/wiki/Literate_programming) is the older form, where Knuth's tooling tangles a document into compilable code and weaves it into readable documentation from one source, so the two cannot drift apart.
The loss is zero for everything the language can express.
The cost is that you maintain the compiler and the language, and anything the language cannot express falls outside the definition.

### Make the definition checkable

The second way is to write the definition in a form a checker can decide against, even when a person still reads it.
A [refinement calculus](https://en.wikipedia.org/wiki/Refinement_calculus) specification is a program written in a nondeterministic language, and the executable code is a refinement of it, produced by steps that preserve the specification's behavior.
Tools in this family, such as [Dafny](https://dafny.org/) with its Hoare-style contracts and the [B-method](https://en.wikipedia.org/wiki/B-Method) built on refinement, let you state preconditions, postconditions, and invariants, then either prove the code satisfies them or report the proof obligations you still owe.
The definition is lossless about the properties it names and silent about the rest, which is the same relativity [intent-driven development](../intent-driven-development/index.md) describes when it says intent is lossless only for the questions it answers.

The type is the smallest checkable definition.
Under the [Curry-Howard correspondence](https://en.wikipedia.org/wiki/Curry%E2%80%93Howard_correspondence), a type is a proposition and a program is a proof of it, so the compiler checks that the program satisfies the claims the type makes.
The correspondence is exact in a total language such as Coq or Agda.
In a Turing-complete language general recursion lets a program inhabit almost any type, so the compiler checks type soundness rather than a theorem.
Dependent and refinement types push the claim closer to the behavior you care about, which is why moving a rule into the type so that a wrong value cannot be constructed is a definitional move rather than a stylistic one.

### Make the definition generative

The third way is to have a procedure construct the code from the definition.
Deductive [program synthesis](https://en.wikipedia.org/wiki/Program_synthesis), as in the Manna and Waldinger framework, treats the specification as a theorem and derives a program from its proof, so the result is correct by construction.
Modern synthesizers improve the search rather than the idea.
Syntax-guided synthesis constrains the space with a grammar, and counterexample-guided synthesis alternates a generator with a verifier until the verifier runs out of counterexamples.
The loss is zero for the synthesized part.
The cost is that synthesis does not scale to arbitrary systems, so it applies to small, well-specified pieces rather than whole products.

### Record the residue

The fourth way accepts that some information cannot follow from behavior at all, and writes it down on purpose.
The choice of a data structure, the decision to trade latency for throughput, and the reason a boundary was drawn where it was do not follow from what the program must do, so no behavioral definition can carry them.
They have to be recorded as decisions with the reasoning attached, because the next agent that meets the same fork will decide it again and may decide it differently.
**This is the channel that carries what the specification cannot, which is why a decision record is part of a definition rather than a note about one.**

The four ways are layers rather than a menu.
The definition is lossless wherever at least one of them applies.
The generated layer produces exact artifacts, the checked layer decides stated properties, and the recorded layer preserves named choices.
What is left over is genuinely free, and marking it free is part of the definition.

![A two by two grid. The horizontal axis runs from interpreted by a reader to decided by a machine, and the vertical axis runs from describes the code to produces the code. Requirements and BDD scenarios sit in the interpreted, describes quadrant. A prompt without a checker sits in the interpreted, produces quadrant. Types, checked specifications, and property tests sit in the machine, describes quadrant. An executable DSL and synthesis sit in the machine, produces quadrant. Only the machine column is lossless.](images/definition-quadrants.svg)

## The agent is a synthesizer, not an oracle

An LLM can work at every layer above.
It can compile a DSL into code, draft a refinement with proof obligations, synthesize from a specification, and apply recorded decisions to a new case.
It cannot make the definition lossless on its own, because losslessness is a property of the checker rather than the writer.
The model produces candidates, the checker decides which candidate is acceptable, and the loop is counterexample-guided synthesis with a model as the generator.

This reframes what to build first.
The instinct is to spend the effort on the prompt and the description, because that is what the model reads, and to treat the checker as a later quality step.
That order is backwards.
**Removing the checker leaves a lossy prose definition with a confident reader, which is the situation the model makes worse rather than better.**
A definition is lossless only if it can reject the model's output, so the checker is the first thing to build and the prompt is the second.

[Rethinking Code Review in the Age of LLMs](../rethinking-code-review-in-the-age-of-llms/index.md) reached the same conclusion from the review side, and [When Agents Solve Problems You Cannot Check](../when-agents-solve-problems-you-cannot-check/index.md) reached it from the verification side.
When implementation is cheap, the scarce resource is a way to tell a correct implementation from a plausible one, and that way is the definition.

## Choosing the strongest form you can afford

Not every project can carry a refinement proof, and the point is not that it should.
For each property you care about, there is a strongest available form, and the forms sit on a ladder.

| Form of the definition | What it decides | What it drops | Cost |
| --- | --- | --- | --- |
| Prose requirement | Nothing, a person decides | Behavior detail, every implementation choice | Low to write, high to interpret |
| User story | Nothing, a person decides | Behavior, edge cases, choices | Low |
| BDD scenario | Whether the code passes the named scenario | Everything the scenario does not name | Moderate |
| Example test | Whether the code passes the example | General behavior, unstated cases | Low |
| Property test | Whether the property holds across generated inputs | Properties not stated, the choices | Moderate |
| Executable specification | The artifact, exactly | Only what the language cannot express | High upfront, no drift |
| Refinement or proof | Whether the code satisfies the stated property | Whatever the property leaves free | Very high |
| Decision record | What was chosen and why | Nothing recorded, whatever is left unwritten | Moderate |
| The code | The artifact itself | The reason it exists | The artifact itself |

Read the table as rungs rather than a ranking of teams.
Push each property as far down the ladder as the budget allows, from a prose sentence to a scenario, from a scenario to a property, from a property to a checked specification, and from a checked specification to an executable one.
Then move the choices the ladder cannot carry into decision records.
The prose does not disappear, since it becomes a view generated from the definition for human readers, and a [bidirectional transformation](https://en.wikipedia.org/wiki/Bidirectional_transformation) view is the formal version of a view that can be written back without loss.

## What to Do Next

- Name the properties you care about, because a definition can only be lossless relative to a stated equivalence.
- For each property, use the strongest form you can afford, choosing executable over checkable, checkable over property-tested, property-tested over example-tested, and example-tested over prose.
- Build the checker first and the prompt second, so the definition can reject the model's output rather than only request it.
- Mark the choices that are free by design, and record every other choice as a decision with its reasoning.
- Treat requirements and specifications as views generated from the definition, so the two cannot drift.

The habit worth breaking is treating a lossy artifact as a complete one.
A requirement is a lossy projection of the code rather than a smaller copy of it, and the projection always omitted the part the reader supplied.
Where the reader no longer asks, the definition has to supply that part, and the only definitions that can are the ones a machine can run or check.

## See also

- [Intent-Driven Development: Writing Intent an Agent Can Consume](../intent-driven-development/index.md) - the same argument from the intent side, where intent is lossless only for the questions it answers and the rest is an intent gap
- [Intent-Driven Development vs My .sdlc Pipeline](../intent-driven-development-vs-my-sdlc-pipeline/index.md) - how a feature-level artifact chain renders the definition checkable by pairing every artifact with a review
- [The Prompt Is the Source Code](../the-prompt-is-the-source-code/index.md) - what the loss costs the maintainer once the intent is gone; this piece locates the loss in the definition itself
- [Rethinking Code Review in the Age of LLMs](../rethinking-code-review-in-the-age-of-llms/index.md) - value moves upstream to the definition when implementation is cheap, which is why the checker matters more than the prompt
- [When Agents Solve Problems You Cannot Check](../when-agents-solve-problems-you-cannot-check/index.md) - the verification side of the same problem, and why stating correctness stays a human responsibility
- [Invest in Verification](../invest-in-verification/index.md) - where to spend when producing code is cheap, which is the checker rather than the generator

## References

- [Wikipedia, "Kolmogorov complexity"](https://en.wikipedia.org/wiki/Kolmogorov_complexity) - the shortest program that outputs an object, which grounds lossless compression and the impossibility of a shorter lossless description
- [Wikipedia, "Refinement calculus"](https://en.wikipedia.org/wiki/Refinement_calculus) - a specification refined by correctness-preserving steps into executable code
- [Wikipedia, "Curry-Howard correspondence"](https://en.wikipedia.org/wiki/Curry%E2%80%93Howard_correspondence) - a type as a proposition and a program as its proof, the smallest checkable definition
- [Wikipedia, "Program synthesis"](https://en.wikipedia.org/wiki/Program_synthesis) - deductive synthesis, syntax-guided synthesis, and counterexample-guided synthesis, which construct code from a specification
- [Wikipedia, "Literate programming"](https://en.wikipedia.org/wiki/Literate_programming) - one source woven into documentation and tangled into code, so the two cannot drift
- [Wikipedia, "Bidirectional transformation"](https://en.wikipedia.org/wiki/Bidirectional_transformation) - the get and put lens laws, which formalize when a view of data can be written back without loss
- [Dafny](https://dafny.org/) - a language whose checker proves the code satisfies its stated preconditions, postconditions, and invariants
- [Wikipedia, "B-Method"](https://en.wikipedia.org/wiki/B-Method) - a formal method that refines an abstract specification into executable code
