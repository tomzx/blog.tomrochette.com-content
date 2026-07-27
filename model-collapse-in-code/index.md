---
title: "Model Collapse: When Code Models Train on Their Own Output"
created: 2026-07-26
type: post
status: finished
tags: [ai, software-engineering, llm, code-quality, training-data, fully-ai-generated, llm=glm-5.2]
readability: 3
audience_notes: >
  Assumes the reader already uses LLM coding tools and is familiar with the trend toward automated, human-light code review. No machine learning background required; model collapse is explained from first principles.
---

Every code-generating LLM in production today was trained on code written by humans.
That fact is easy to forget, because the same models are now writing most of the code.
**If humans stop reading, reviewing, and refining that code, the next generation of models will have to train on the output of this one, and the research on what happens then is not reassuring.**

## Models Were Trained on Human Code

The large code models learned from enormous corpora of human-written code: public repositories, Stack Overflow answers, patches, and documentation.
None of that code was perfect.
Much of it was buggy, redundant, or obsolete.
But it carried something that model output cannot manufacture: the accumulated signal of millions of programmers solving real problems under real constraints, correcting each other in public, and converging over decades on patterns that actually work.

That signal is the fuel.
When you prompt a model and it produces a working function, it is not reasoning from first principles.
It is predicting the next token from patterns absorbed out of human code, and those patterns were selected by reality, not by another model's preferences.

## The Trend Is Pulling Humans Out of the Loop

I have spent the last year arguing that human code review should shrink, that we should verify code instead of reading it ([Verifying Code Without Reading It](../verifying-code-without-reading-it/index.md)), and that the specification, not the diff, is where human judgment belongs ([Rethinking Code Review in the Age of LLMs](../rethinking-code-review-in-the-age-of-llms/index.md)).
I still believe that, at the level of a single team shipping a single product.

But there is a consequence I have been slow to take seriously, because it does not show up in any one team's metrics.
It shows up in the corpus.
As review becomes automated and engineers read less of what the model writes, the public record of code becomes a record of model output, lightly curated by machines.
**The very thing the next models need to train on, human-written and human-corrected code, is becoming a smaller and smaller fraction of what exists.**

## What Model Collapse Is

This feedback loop has a name.
Researchers call it model collapse, and the clearest statement of it is Shumailov et al.'s 2024 paper, ["AI models collapse when trained on recursively generated data"](https://www.nature.com/articles/s41586-024-07566-y).

The finding is stark.
When you train a model on data produced by another model, and then train the next model on the first model's output, and repeat, the model degrades.
It does not degrade the way a person gets tired.
It loses information about the tails of the distribution first, the rare cases, the minority examples, the edge behavior, while its performance on the average case can look fine for a surprisingly long time.
**Model collapse is hard to notice precisely because the headline metrics keep going up while the long tail quietly disappears.**

The mechanism is statistical, not mysterious.
A model that fits another model's output is fitting a smoothed, averaged version of reality.
Each generation of training rounds off a little more of the texture, the weird inputs, the unusual-but-correct solutions, until what remains is a narrow, over-represented center.

The preprint that introduced the term, ["The Curse of Recursion"](https://arxiv.org/abs/2310.07450), works through the mathematics, and the [Wikipedia article on model collapse](https://en.wikipedia.org/wiki/Model_collapse) lays out the two stages, early and late, and the open disagreement among researchers about how severe the real-world impact will be.

## Why Code Is Especially Exposed

General model collapse is a concern for text and images.
Code is a sharper case, for three reasons that compound.

First, the useful part of code lives in the tails.
The happy path is easy.
The value is in error handling, concurrency, boundary conditions, security, the obscure API, and the input that should never arrive but does.
These are exactly the minority examples that collapse erodes first.
**A model that handles the common case and breaks on the edge case is the literal definition of early model collapse, and it is also the definition of code that passes review and fails in production.**

Second, code that looks correct is easy to generate and hard to filter out.
A plausible-looking function that contains a subtle bug is not obviously wrong the way a garbled sentence is.
If nobody reads it, and the tests do not cover the edge case, it merges into the corpus and becomes training data for the next model, carrying its bug forward as if it were a pattern worth repeating.

Third, the volume is exploding.
When a model can draft a feature in minutes, the amount of model-written code committed every day is growing faster than anyone's ability to curate it.
Public repositories are filling with generated code, and that code is the raw material for the next training run.
The [dead internet theory](https://en.wikipedia.org/wiki/Dead_Internet_theory), originally a half-joke about the web filling with bots, is becoming literal for code.

## What Might Happen Next

No one knows exactly how this plays out, because the loop has not completed a full generation at scale yet.
But a few hypotheses are worth stating plainly, because they are testable and they point at where to look.

### The quality plateau

Models keep improving on benchmarks for a while, then flatten.
The plateau will not look like running out of compute.
It will look like running out of signal.
**The bottleneck moves from the size of the model to the quality of the data, and the data has stopped improving because it is no longer being written by anyone who understands it.**
This is the same pattern I described in [The Shifting Bottleneck](../the-shifting-bottleneck/index.md): each constraint you remove reveals the next one, one level up.

### The long-tail erosion

While the common case improves, the edge cases get quietly worse.
Security vulnerabilities, race conditions, and incorrect handling of unusual inputs become more frequent, not less, because the training distribution has thinned exactly where those lessons lived.
Benchmarks that measure average correctness will miss this.
Benchmarks that measure adversarial or edge-case correctness will catch it, and they will be the ones to watch.

### The grounding premium

Code with verifiable grounding becomes valuable.
What matters is not who typed it but whether it was selected by reality: it ran in production, it passed tests against inputs no one hand-picked, it survived real failures and was corrected by them.
A human-written snippet that never ran carries no signal a model could not invent.
A model-generated snippet that ran under real load and survived carries signal that no amount of recursive training can synthesize.
Labels like "ran in production without rollback" or "verified against a fuzz corpus" start to mean something, the way "organic" became a label worth paying for in food.
Grounding begins to matter as much as data volume, and the organizations that can prove their code carried a real outcome get better models.
**Eventually the most valuable training corpus is the one you can prove was selected by reality, not merely produced by a model.**

### The verification-as-data loop

The only new ground-truth signal that does not depend on model output is execution.
The most valuable training data stops being code at all, and becomes (specification, implementation, test result) triples, where the test result is measured by reality, not inferred by another model.
Reinforcement learning from execution, where the reward comes from actually running the code, replaces scraping repositories as the dominant way to improve code models.
A model is, at inference time, a function of its context, as I argued in [The Importance of Context When Interacting with LLMs](../the-importance-of-context-when-interacting-with-llms/index.md); at training time it is a function of its corpus, and the corpus is the part that is degrading.

### The bifurcation

A gap opens between organizations that keep humans in the loop and those that do not.
The fully automated shops gain short-term velocity but slowly poison their own tooling, because their internal corpus drifts toward generic, model-flavored code.
The shops that keep humans reading, correcting, and rewriting code retain a source of fresh signal, and their models, or at least their use of models, stays sharper over time.
**The competitive advantage flips from speed to the quality of the signal you feed back into the system**, which is the same conclusion the foundation argument reaches in [The Foundation Predicts the House of Cards](../the-foundation-predicts-the-house-of-cards/index.md).

## The Case That Code Improves Instead

Everything above assumes the only training signal is "imitate the previous generation."
For text and images that is roughly true, which is why model collapse is a real worry there.
Code is different in one decisive respect: it has an oracle.

Code runs.
It passes tests or fails them, type-checks or does not, compiles or crashes, and a fuzzer can generate inputs no human would think to test.
That execution result is a ground-truth signal that does not come from any model, and it is the one thing the self-consumption loop cannot synthesize.
**Where collapse assumes the model learns only from its own output, execution lets it learn from reality, and reality does not degrade between generations.**

This changes the arithmetic in several ways that point upward rather than down.

First, reinforcement learning from execution replaces imitation as the engine of improvement.
The training unit stops being "a file someone committed" and becomes a (specification, implementation, test result) triple, where the reward is measured by running the code.
A model rewarded for passing tests it has never seen is being pushed toward correct behavior, not toward the average of prior outputs, and that pressure does not loop back on itself.

Second, selection effects push the surviving corpus upward, not toward the mean.
When generation is best-of-N, or when an adversarial verifier tries to break each candidate, the code that survives into the corpus is the code that passed real checks.
A repository built from verified survivors can be cleaner than the human corpus ever was, because GitHub and Stack Overflow were always full of bugs that nobody ran.
Filtering is the antidote to unfiltered collapse, and code is the one modality where filtering is automatic.

Third, the long tail can get better represented, not worse.
Humans are lazy about edge cases.
Fuzzers, property-based tests, and generated edge-case suites are not.
If the training signal includes execution across millions of rare inputs, the model sees more of the tail than human-written code ever covered, and the long-tail erosion hypothesis inverts into long-tail reinforcement.

So the optimistic thesis is precise: **code is the modality least susceptible to model collapse, because it alone carries an objective, automatic, infinite ground truth.**
The thing that makes code hard, that it has to actually work, is also the thing that protects it.

The catch is that the oracle only checks what you ask it to check.
A passing test suite proves the code does what the tests cover, not that the tests cover what matters.
Let the same model write the tests and the code, or let the test suite stay shallow, and execution stops being an oracle and becomes a rubber stamp.
**The virtuous loop holds only while the verification is sound, separate from generation, and broader than the happy path.**

## What Breaks the Loop

Even the imitation-only loop has an escape hatch, if real data keeps accumulating.
Gerstgrasser et al. showed in ["Is Model Collapse Inevitable?"](https://arxiv.org/abs/2404.01413) that collapse is avoided when synthetic data accumulates alongside real data instead of replacing it.
Their result is the weaker version of the optimistic case: as long as we keep adding fresh human code to the corpus, the model does not have to train only on its own output.

The catch is the word "fresh."
The mitigation only works if real human code keeps flowing into the training set in meaningful quantities.
**And that is exactly the input the current trend is starving.**
Every hour engineers spend prompting instead of writing, every diff that ships unread, every answer on Stack Overflow that goes unposted because a model answered it privately, shrinks the stream of new human signal.

So the practical question is not whether model collapse is possible.
The research says it is.
The question is whether we keep enough humans writing, reading, and correcting code, in public, to keep the real data flowing.

## The Verdict Hinges on the Oracle

I have argued, and still believe, that a single team should not force a human to read every diff if its verification system is strong enough.
What I no longer believe is that this is automatically a tragedy of the commons.
It is a tragedy only if the only signal the field feeds back into its models is imitation of prior output.
Execution is a second signal, and for code it is the stronger one.

The two futures run on the same variable: the soundness of verification.
If verification stays grounded in real execution, adversarial, and separate from generation, the loop improves on its own, and humans reading code matters less every year.
If verification is captured, shallow, or graded by the same model that wrote the code, the loop degrades, and no amount of human reading at the end will save it.

So the instruction is narrower than "keep humans writing code in public."
It is: keep the oracle trustworthy.
Run the tests, fuzz the inputs, separate the verifier from the author, and treat every passing suite as a claim about coverage rather than proof of correctness.
Do that, and generated code can keep getting better long after humans stop writing most of it.
Fail to do it, and the degradation arrives on schedule.

## See also

- [Verifying Code Without Reading It](../verifying-code-without-reading-it/index.md) - the local practice this article complicates: stop reading diffs, start verifying them, and the global cost that practice imposes when everyone adopts it
- [Rethinking Code Review in the Age of LLMs](../rethinking-code-review-in-the-age-of-llms/index.md) - the case for moving human effort from the diff to the spec, which is correct per-team and worth re-examining at the corpus level
- [The Importance of Context When Interacting with LLMs](../the-importance-of-context-when-interacting-with-llms/index.md) - the inference-time version of the same claim: a frozen model reflects its context, just as a trained model reflects its corpus
- [The Shifting Bottleneck](../the-shifting-bottleneck/index.md) - why removing the production constraint relocates it, which predicts the data-quality plateau
- [The Foundation Predicts the House of Cards](../the-foundation-predicts-the-house-of-cards/index.md) - why codebase health outranks tooling, and why the teams that keep human signal win over time

## References

- [Shumailov et al., "AI models collapse when trained on recursively generated data" (Nature, 2024)](https://www.nature.com/articles/s41586-024-07566-y) - the definitive empirical demonstration that training on model output degrades models across generations
- [Shumailov et al., "The Curse of Recursion: Training on Generated Data Makes Models Forget"](https://arxiv.org/abs/2310.07450) - the preprint that introduced model collapse and its mathematical treatment
- [Gerstgrasser et al., "Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data"](https://arxiv.org/abs/2404.01413) - the counterpoint showing collapse is avoided when real data accumulates alongside synthetic data
- [Wikipedia, "Model collapse"](https://en.wikipedia.org/wiki/Model_collapse) - overview of the two stages of collapse and the disagreement over real-world impact
- [Wikipedia, "Dead Internet theory"](https://en.wikipedia.org/wiki/Dead_Internet_theory) - the analogy for code repositories filling with generated content
