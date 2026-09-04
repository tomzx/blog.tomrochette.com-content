---

title: "Attention Engineering: Your Attention Is the Bottleneck"
created: 2026-08-08
type: post
status: finished
tags: [ai, llm, attention-engineering, productivity, cognitive-load, fully-ai-generated, llm=glm-5.2, llm=glm-5.3]
readability: 4
audience_notes: >
  Assumes the reader already delegates work to LLM coding agents and has felt the difference between spawning a task and actually judging its output. No introduction to LLMs; builds on the acceptance and bottleneck pieces already on this blog.
agent_sessions:
  - ses_05e63b4f7ffelX4pKs3x9Xh5dN
---

Generation stopped being the expensive part of working with LLMs.
You describe, the model produces, and a plausible answer arrives in seconds.
**The expensive part is now your attention, and almost nobody has updated how they spend it.**

We kept the habits from when writing the code was the hard part.
We hover over the agent while it works, we read every diff it produces, we re-check by hand what a check could check for us, and we call the exhaustion that follows "using AI well."
It is not.
It is attention spent on the half of the problem that is already solved, while the half that still needs a human mind gets the leftovers.

Attention engineering is the deliberate practice of treating your own attention as the scarce resource, and allocating it to the parts of an agent workflow where a mind is actually required.

## Attention Is Not Time

The first mistake is to confuse attention with time.
Time expands to fit the work; attention does not.
You can run eight agent sessions in parallel in the same number of hours, but you cannot read, judge, and decide on eight outputs in parallel.
The part that parallelizes is generation, which is the part that no longer needs you.
The part that needs you, deciding what is good enough, is strictly serial and strictly finite.

This is why [spawning more sessions](../managing-many-llm-agent-sessions/index.md) often makes you slower, not faster.
Each open session is a claim on working memory, and working memory is small and slow to refill after a switch.
The literature on [cognitive load](https://en.wikipedia.org/wiki/Cognitive_load) has been clear about this for decades: heavy switching fragments attention and produces shallow processing, and the cost is paid by the task you switched into, not the one you left.
**Parallel agents widen the generation pipe and narrow the decision pipe at the same time, and the decision pipe is the one that matters.**

## Where Attention Leaks

**Most of the fatigue people blame on AI is really misallocated attention.**
It leaks in four predictable places.

Watching the agent generate.
The stream of tokens is mesmerizing and almost useless.
You cannot usefully steer a model at token speed, and the sense of "supervising" it is a feeling of productivity, not productivity itself.
You are attending to a process you cannot improve by attending to it.

Re-verifying what a check could verify.
The model says the bug is fixed, and instead of trusting a test, you re-read the diff looking for the fix with your own eyes.
This is [the acceptance gap](../the-acceptance-gap/index.md) run backwards: you spend scarce, taste-grade attention on correctness, the one thing that can be encoded and handed off.
A minute of writing the check would have saved an hour of reading, forever.

Context-switching between sessions mid-judgment.
You decide on session A until a notification pulls you to session B, and back.
Each switch leaves a residue of the previous task in your head, and the decision you return to is made with half your mind still elsewhere.
The work feels continuous and is actually being done in shallow fragments.

Signing off without attending.
The pull request opens, CI is green, the description looks right, and a feeling forms before the code is read.
We have known for a long time that [most review works this way](../code-review-without-reading-the-code/index.md), and the arrival of machines writing the diff has not made the reading more rigorous, only the ritual more exhausting.
And attention collapses fastest on the work you had no investment in to begin with: it defends itself on what you care about and quietly gives up on what you do not ([The Cost of Work You Did Not Choose](../the-cost-of-work-you-did-not-choose/index.md)).

## The Leverage Ranking

Not every part of an agent workflow needs your attention equally, and the error is treating them the same.
Rank them by how much they need a human mind.

Generation needs none.
Stop attending to it.
Hand over a finished intent and walk away.

Verification, the question of whether it did the thing, needs very little, once you encode it as a check.
A failing test that must pass is attention that pays itself forever, for free, whether or not you are watching.
The residual cost is exactly the set of things you have not yet bothered to encode.

Specification, the question of what you actually want, needs a great deal, and it is upstream.
Attention spent writing the spec pays a higher dividend than attention spent editing the output it produced, because a good spec prevents the wrong output from existing at all.

Judgment, the question of whether the result is the thing you wanted, needs all of it, and it cannot be delegated.
This is the taste decision, the "good enough, ship it" moment, and it is the last compounding thing you do.

**The skill is to starve the first two and feed the last two.**

## Attention Engineering, In Practice

A few rules hold up.

**Spend attention upstream, not downstream.**
The hour you invest in the specification is worth ten hours of fixing the generated output, because the output is downstream of the spec and inherits all of its omissions.
If you keep editing what the agent produced, the problem is usually the prompt you did not write, not the model.

Encode correctness until it costs you nothing.
**Every check you write is attention you never have to spend again.**
The goal is to shrink the "verify by hand" pile to the set of things that genuinely cannot be expressed as a check, which is smaller than most people think.

Parallelize generation, serialize judgment.
Let many sessions run at once, but do all your deciding in one focused pass, one session at a time, with the others closed or paused.
The model is the part that benefits from parallelism.
Your judgment does not, and pretending otherwise is how you ship work you never actually read.

Refuse to supervise.
If you find yourself watching the agent work, you have either failed to specify the task well enough to walk away, or you have not built the check that would let you trust the result without watching.
Both are fixable, and fixing them is a better use of attention than the watching.

Protect the taste decision.
It is small in duration and enormous in leverage, and it is the one thing no tool will ever do for you, which is exactly why it is worth protecting from the noise of everything else.

## The Implication

The constraint has done what it always does when a layer gets automated: it moved up the chain, from generating the work to deciding whether it is good enough ([The Shifting Bottleneck](../the-shifting-bottleneck/index.md)).
What is new is that the new constraint is not another task you can delegate.
It is your own attention.

The ceiling on what you produce with agents is not the model, not the tooling, and not how many sessions you can spawn at once.
**It is how much focused attention you can bring to the few decisions that require a mind, and how ruthlessly you keep that attention off the many that do not.**

The people who get the most out of LLMs are not the ones with the cleverest prompts.
They are the ones who learned to walk away from generation, to encode everything checkable, and to save their finite attention for the specification and the taste that only they can supply.

Working with agents is not a prompting skill.
It is an attention skill, and the sooner you treat your attention as the bottleneck it has become, the more of it you will have for the work that is actually yours to do.

## See also

- [The Acceptance Gap](../the-acceptance-gap/index.md) - the core insight this article builds on: generation is solved, acceptance is the bottleneck, and the taste half of acceptance is the last human loop
- [The Shifting Bottleneck](../the-shifting-bottleneck/index.md) - the upstream pattern: automating a layer moves the constraint to the layer above it, here from generation to deciding
- [Managing Many Concurrent LLM Agent Sessions](../managing-many-llm-agent-sessions/index.md) - where parallel sessions make the attention bottleneck acute and turn it into human cognitive load
- [You Already Review Code Without Reading It](../code-review-without-reading-the-code/index.md) - the failure mode this article warns against: signing off on output you never actually attended to
- [The Cost of Work You Did Not Choose](../the-cost-of-work-you-did-not-choose/index.md) - why attention defends itself on work you care about and collapses on work you do not
## References

- [Cognitive load](https://en.wikipedia.org/wiki/Cognitive_load) - grounds why attention is finite: working memory is small, and heavy context switching fragments it into shallow processing

