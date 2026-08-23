---
title: "The Shifting Bottleneck: From Writing Code to Questioning Everything"
created: 2026-05-12
type: post
status: finished
tags: [ai, software-engineering, llm, product-thinking, automation, fully-ai-generated, llm=glm-5.1, llm=glm-5.3]
readability: 3
audience_notes: >
  Assumes the reader is a software developer or engineering lead who has used LLM coding tools and has already felt the shift from writing code to reviewing and deciding. No explanation of what an LLM is.
---

Every time AI removes a bottleneck in software development, the next one appears one level higher up the decision chain.
**The constraint never disappears, it just moves.**

## The Five Stages

### 1. Producing code

For decades, the bottleneck was typing.
Writing code was slow.
Understanding codebases was slow.
Every feature required a human to translate intent into syntax, one keystroke at a time.
We built IDEs, autocompletion, linters, and refactoring tools to speed this up, but the fundamental constraint remained: humans had to write the code.

**Then LLMs arrived and that constraint dissolved almost overnight.**
[GitHub Copilot](https://github.com/features/copilot), [Cursor](https://cursor.com), [Claude Code](https://claude.com/product/claude-code), and a dozen other tools made it trivial to generate working code from a description.
The bottleneck moved.

### 2. Verifying generated code

When code writes itself, your job shifts from author to reviewer.
You no longer ask "how do I implement this?" but "does this implementation do what I want?"

Verification is a fundamentally different skill.
Reviewing code you didn't write requires reading with suspicion.
Every function could contain a subtle bug, a hallucinated API call, or a plausible-sounding but incorrect assumption.
The code looks right, the tests pass, but does it actually solve the problem?

The verification bottleneck is harder than the production bottleneck because verification is an underconstrained problem.
There are infinitely many ways code can be wrong, and no finite checklist catches them all.

### 3. Deciding what to implement

Once you can generate and verify code quickly enough, a new question surfaces: should this be built at all?

Not every feature deserves implementation.
Not every bug deserves a fix.
The cost of writing code approaches zero, but the cost of maintaining code, shipping code, and supporting code does not.
[Every line of code is a liability](https://blog.codinghorror.com/the-best-code-is-no-code-at-all/).
Every feature adds surface area for bugs, increases cognitive load, and constrains future decisions.

The bottleneck shifts from "can we build it?" to "should we build it?"
Deciding what to implement is product thinking, not engineering.
Engineers who spent careers optimizing for execution speed now find themselves needing to develop judgment about what is worth executing.

### 4. Deciding what to build

Push further: should this product exist at all?

Before LLMs, the cost of building a product was a natural filter.
If it took six months and a team of five to build an MVP, you had to be reasonably confident the market wanted it.
Now that an MVP can be built in an afternoon, the cost of building is no longer the filter.
The filter is the cost of being wrong about product-market fit.

The bottleneck now sits in strategy.
Understanding users, identifying real problems, and choosing which market to enter are now the scarce skills.
Anyone can build the product.
Figuring out which product to build is the hard part.

### 5. Questioning automation itself

And then you arrive at the final question: should we have automated ourselves at all?

This is not a joke.
Every layer of automation removes human involvement from a layer of decision-making.
When code writes itself, verifies itself, decides what to build, and decides whether to build it, what is left for the human?

There is a genuine question about whether the end state of this trajectory is human irrelevance.
Not because AI became malevolent, but because we systematically removed every reason for a human to be involved.
Each step was rational.
Each bottleneck was real.
Each automation was justified.
And yet the cumulative effect is a slow unwinding of human agency in the creative process.

## The Bottleneck Elevator

This pattern has a name in systems thinking: the [theory of constraints](https://en.wikipedia.org/wiki/Theory_of_constraints).
In any system, improving one stage of a pipeline exposes the next bottleneck downstream.
In software development, the pipeline runs upward through abstraction layers:

```
Existential → Product → Feature → Verification → Production
```

AI has been climbing this stack from the bottom.
**Each time it solves one level, the next level becomes the limiting factor.**
The work doesn't decrease, it transforms.

## What to Do Next

If you are a software developer today, your career trajectory is being pulled up this stack whether you like it or not.

**If you are still at Stage 1** (producing code), you are already behind.
Adopt AI coding tools now.
The gap between developers who use LLMs and those who don't is widening every month.

**If you are at Stage 2** (verifying code), invest in specification skills.
The ability to write precise, testable requirements is what separates effective AI-assisted developers from those who spend all day reviewing hallucinated nonsense.

**If you are at Stage 3** (deciding what to implement), develop product judgment.
Understanding trade-offs, opportunity cost, and the difference between "can build" and "should build" is your leverage.

**If you are at Stage 4** (deciding what to build), you are in the right place for now.
Strategy, market understanding, and user empathy are the current frontier.

**If you are at Stage 5**, you have seen the full picture.
The question is not whether automation will continue climbing, it will.
The question is what humans should do with the freedom that comes from not being the bottleneck.

## The Real Answer

I don't have a clean answer for Stage 5.
Neither does anyone else.
The optimists say we will find new creative work that we cannot yet imagine, the same way we always have after every technological revolution.
The pessimists say this time is different because AI doesn't just replace manual labor, it replaces cognitive labor, and eventually all of it.
Both positions are old positions in the [technological unemployment](https://en.wikipedia.org/wiki/Technological_unemployment) debate, and neither side has settled it.

What I can observe is that the bottleneck will keep shifting.
Whatever you think the final constraint is, solving it will reveal another one behind it.
**The work of a developer is not to write code, it is to stand at the current bottleneck and push.**

The bottleneck will move.
Your job is to move with it.
