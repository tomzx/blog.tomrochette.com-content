---
title: Kent Beck
created: 2026-09-24
updated: 2026-09-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, people, publications, extreme-programming, tdd, augmented-coding, methodology]
readability: 3
audience_notes: >
  Engineers and leads who are reworking their team process, tests, and design habits for coding agents and want that guidance from the source rather than from commentary.
  Assumes you know what Extreme Programming, TDD, and coding agents are, and that you have used at least one agent on real code.
---

Kent Beck, creator of Extreme Programming and test-driven development, publishes his current thinking on software design and AI-era practice on the Software Design: Tidy First? newsletter.
Facts below verified as of 2026-09-24.

**He is the most credible methodology voice on which parts of classic software craft survive when agents write the code, and his boundary is process and economics: he tells you how to work, not which tool or model to buy.**

## What it is

A weekly newsletter (over 126,000 subscribers as of 2026-09-24) backed by a forty-year methodology portfolio: Extreme Programming Explained, Test-Driven Development by Example, Implementation Patterns, the 2023 book Tidy First?, and co-creating JUnit with Erich Gamma.
His AI arc runs from the April 2023 essay "90% of My Skills Are Now Worth $0" (the repricing thesis: "the value of 90% of my skills just dropped to $0. The leverage for the remaining 10% went up 1000x") to June 2025's "Augmented Coding: Beyond the Vibes", which separates augmented coding, where you still care about code, tests, and design, from vibe coding, where you only care about behavior.
He grounds that distinction in a real project, a B+ tree library in Rust and Python built with agents over about four weeks, with his full system prompt and intervention habits published in the post.
Around the newsletter sit consulting, speaking (topics like "Beyond Vibes: What Augmented Coding Actually Requires"), a Still Burning podcast, and Tidy Together, the in-progress third book of his Empirical Software Design series.

## Status

Active, and newly central to the process debate.
Cadence is weekly per his own site, and the newsletter's top-posts archive shows entries dated December 12 2025 and January 16, April 16, and May 15 (Substack omits the year on current-year posts, so those are 2026).
He is independent: Wikipedia records his Facebook years (2011-2019) and a 2019 software fellow role at Gusto, but kentbeck.com now presents him as consultant, writer, artist, and speaker, with draft chapters of Tidy Together going to paid subscribers.
The AI-era posts themselves drew modest Hacker News traction (his own submission of the augmented-coding essay sat at 5 points as of 2026-09-24), yet the framing keeps resurfacing in threads asking whether XP should be revisited for the agent era, which is the slower, stickier kind of influence.

## Strengths

- Authority with receipts: the person who defined TDD and XP re-deriving his own methodology for agents carries weight no commentator can match.
- He experiments on real code and shows his work: the B+ tree build came with the system prompt, the time logs, and a candid verdict, correct and fast but with more accidental complexity than he likes.
- He names the distinctions the industry now argues with: augmented versus vibe coding, and the three warning signs of an agent going off track (loops, unrequested features, cheating on tests).
- The economics essays give leaders a decision frame instead of a prediction: Programming Deflation's substitution-versus-Jevons pairing ends with capabilities to build that pay off under either future.
- Short, quotable essays, one idea each, with no tool churn to wade through.

## Cautions

- This is a process feed, not a tracking feed: expect near zero coverage of specific tools, models, and prices, so pair it with a practitioner blog for that layer.
- His evidence is personal and he says so: "I'm extrapolating wildly from a couple of experiences, which is what I do."
- Even his own commenters push back on the emotional cost: one writes that LLM-generated code "feels to me like having no soul", a tension he does not resolve.
- The best material (draft book chapters, weekly Thinkies) sits behind the paid tier.

## Compared to

- [Simon Willison](../simon-willison/index.md): the daily tool-level chronicler versus Beck's weekly process level; use Willison to learn what changed this week, Beck to decide what it means for how your team works.
- [Andrej Karpathy](../andrej-karpathy/index.md): the model-and-training-level view, and the coiner of the "vibe coding" term Beck argues against, versus Beck's working discipline of tests and tidiness under agents.
- [Steve Yegge](../steve-yegge/index.md): manifesto-scale provocations versus small falsifiable essays; read Yegge for the argument, Beck for the practice.

## Bottom line

Recommended for senior engineers and leads who need to rework team process, review habits, and design discipline for agent-heavy development.
Not for readers who want tool comparisons, model benchmarks, or news.

## Top 5 recommended reading

- [Augmented Coding: Beyond the Vibes](https://tidyfirst.substack.com/p/augmented-coding-beyond-the-vibes) - the essay that defines the discipline, with the full system prompt and his three warning signs that an agent is going off track.
- [90% of My Skills Are Now Worth $0](https://tidyfirst.substack.com/p/90-of-my-skills-are-now-worth-0) - the April 2023 repricing thesis that started his AI arc, including his own admission that he was extrapolating wildly.
- [Programming Deflation](https://tidyfirst.substack.com/p/programming-deflation) - substitution versus Jevons paradox applied to software, ending in skills that hold up whether employment shrinks or grows.
- [Canon TDD](https://tidyfirst.substack.com/p/canon-tdd) - the five steps of TDD from the person who named it, written to stop strawman critiques and now the foundation agents are being pointed at.
- [Tidy First? and the Empirical Software Design series](https://www.kentbeck.com/) - his own summary of the book series and the design-as-optionality economics behind his augmented-coding principles.

## Changes

- 2026-09-24 - Created.

## See also

- [Simon Willison](../simon-willison/index.md) - the daily counterpart feed: what tools and models did this week.
- [Andrej Karpathy](../andrej-karpathy/index.md) - where the "vibe coding" framing Beck argues against came from.
- [Steve Yegge](../steve-yegge/index.md) - the other veteran rethinking the profession, louder and less systematic.
- [GitHub Spec Kit](../../spec-driven-development/spec-kit/index.md) - spec-first tooling that mechanizes the planning discipline Beck does by hand with plan.md.
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the tooling his essays deliberately abstract away.

## References

- https://tidyfirst.substack.com/p/augmented-coding-beyond-the-vibes - the augmented versus vibe coding essay, the B+ tree case study, and the published system prompt
- https://tidyfirst.substack.com/p/90-of-my-skills-are-now-worth-0 - the 2023 repricing thesis and the 3X Explore/Expand/Extract framing
- https://tidyfirst.substack.com/p/programming-deflation - the substitution versus Jevons economics essay (2025-09-15)
- https://tidyfirst.substack.com/p/canon-tdd - his definitive TDD workflow essay (2023-12-11)
- https://tidyfirst.substack.com/ - the newsletter home: over 126,000 subscribers as of 2026-09-24
- https://tidyfirst.substack.com/archive?sort=top - posting cadence evidence with dated entries into 2026
- https://www.kentbeck.com/ - current projects (Tidy Together, augmented-coding research and speaking), subscriber and open-rate figures, consulting and podcast
- https://en.wikipedia.org/wiki/Kent_Beck - the methodology record: XP, TDD, JUnit, the Agile Manifesto, Facebook and Gusto years, book list
- https://hn.algolia.com/api/v1/search?query=%22augmented%20coding%22%20kent%20beck&hitsPerPage=8 - third-party HN evidence, including his own submission at 5 points and citations in XP-revision threads (as of 2026-09-24)
