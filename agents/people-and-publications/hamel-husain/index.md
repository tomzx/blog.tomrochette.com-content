---
title: Hamel Husain
created: 2026-08-29
updated: 2026-09-22
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=big-pickle, llm=glm-5.3-flash, people, publications, evals, applied-ai, llm-practitioner]
readability: 3
audience_notes: >
  Engineers shipping AI products who want a grounded, data-first method for deciding whether their agent actually works and for improving it.
  Assumes you have built an AI feature or agent and have hit the wall of not knowing whether changes help or hurt.
---

Hamel Husain is the independent consultant and writer who turned AI evaluation, "evals", from an afterthought into the disciplined practice teams use to decide whether their agent works.

**His core argument is that most AI teams focus on architecture when what decides success is measurement and iteration: the teams that win "obsess over measurement and iteration" rather than the vector database or framework.**

## What it is

A personal blog plus a substack, a newsletter, and a paid course, written by Hamel Husain, a machine learning engineer who worked at Airbnb and GitHub and does early LLM research used by OpenAI for code understanding.
He is currently an independent AI consultant through Parlance Labs.
The [A Field Guide to Rapidly Improving AI Products](https://hamel.dev/blog/posts/field-guide/) post, which distills process from 30+ production implementations, is the canonical entry point.

## Status

Active and influential as of 2026-09-22.
The blog posts through mid-2026, most recently "AI Evals: Everything You Need to Know" (2026-09-18), "AI Product Engineering Notes" (2026-08-12), and "Do Automated Evals Work?" (2026-07-11).
He co-teaches the [AI Evals for Engineers and PMs](https://maven.com/parlance-labs/evals) course with Shreya Shankar, reporting over 5,000 engineers and PMs from teams like OpenAI, Google, Meta, Amazon, and Microsoft as of 2026-09-22, with an Oct 10 cohort advertised at 25% off.
He is co-author of the forthcoming O'Reilly book [Evals for AI Engineers](https://www.oreilly.com/library/view/evals-for-ai/9798341660717/).

## Strengths

- His error-analysis-first method is unglamorous and reproducible: find failures in production data, write tests for them, then automate an LLM judge you have calibrated against a domain expert.
- He is explicitly skeptical of off-the-shelf evaluation metrics and of outsourced annotation, arguing that the value comes from building product intuition, not from buying a tool.
- He grounds recommendations in real client cases rather than frameworks, which makes the advice transferable.
- The Field Guide is widely endorsed, including by Simon Willison, who calls it "packed with hard-won actionable advice".

## Cautions

- The core value sits increasingly behind a $4,200 course and consulting work, so the free blog is the teaser, not the full method.
- "Evals" is a crowded, hype-prone corner: the recommendation to invest heavily in evaluation can read as self-serving from someone who sells evals services.
- His binary pass/fail and critique-shadowing method is opinionated and does not suit every product, even though he argues it well.
- Automated evals have known failure modes: a judge that rubber-stamps PASS can score ~90% agreement while catching nothing, so the discipline is exactly what makes them trustworthy.

## Pricing

Free to read on the blog and substack.
The course is paid ($4,200 on Maven as of 2026-09-13), and Parlance Labs sells consulting and the O'Reilly book is forthcoming.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-13 | Maven course | Baseline: blog and substack free; the evals course $4,200 on Maven; Parlance Labs sells consulting. | [maven.com/parlance-labs/evals](https://maven.com/parlance-labs/evals) |

## Compared to

- [Andrej Karpathy](../andrej-karpathy/index.md): the vocabulary-setter versus the practitioner; Karpathy names the concepts, Husain gives you the working method for verifying them.
- [Simon Willison](../simon-willison/index.md): both are hands-on practitioners, but Willison chronicles the tool churn while Husain focuses narrowly on the evaluation loop.
- [Chip Huyen](../chip-huyen/index.md): the systems-design surveyor versus the error-analysis specialist; Huyen covers the whole AI application lifecycle, Husain goes deep on one part.

## Bottom line

**Recommended for any engineer whose agent produces outputs nobody can verify, because the data-first evaluation loop is the highest-leverage improvement available.**
Not for someone looking for survey-level breadth or for a tool recommendation; it is a process, not a product.

## Top 5 recommended reading

- [A Field Guide to Rapidly Improving AI Products](https://hamel.dev/blog/posts/field-guide/) - The canonical entry point, distilling the error-analysis-first method from 30+ production implementations.
- [Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/) - The framing post that argues evaluation is the highest-leverage investment in any AI product.
- [Using LLM-as-a-Judge For Evaluation: A Complete Guide](https://hamel.dev/blog/posts/llm-judge/) - The step-by-step critique shadowing method for building an LLM judge you can actually trust.
- [AI Evals: Everything You Need to Know](https://hamel.dev/blog/posts/evals-faq/) - The comprehensive FAQ co-written with Shreya Shankar, curating answers from teaching 5,000+ engineers and PMs.
- [Evals Skills for Coding Agents](https://hamel.dev/blog/posts/evals-skills/) - Shows how to give coding agents the eval workflow itself, from error discovery to judge validation.

## Changes

- 2026-08-29 - Created in the People and publications expansion as the evaluation-and-verification note.
- 2026-08-30 - Aligned the course claim to the current page wording.
- 2026-09-20 - Added the Price history section tracking price changes in a table, per the new owner rule.
- 2026-09-22 - New post "AI Evals: Everything You Need to Know" (2026-09-18) now leads the blog; the course page advertises an Oct 10 cohort at 25% off.
- 2026-09-24 - Added the Top 5 recommended reading section.

## See also

- [Context Management Patterns](../../context-management-patterns/index.md) - the feed-side discipline that evals then verify
- [Model Selection for Coding Tasks](../../model-selection-for-coding-tasks/index.md) - evaluation data is what makes model selection a measurement, not a guess
- [Rethinking Code Review in the Age of LLMs](../../../rethinking-code-review-in-the-age-of-llms/index.md) - how verification of generated output changes the human review role
- [The Codebase Gardener](../../../the-codebase-gardener/index.md) - the domain-expert role his eval method depends on

## References

- https://hamel.dev/ - the blog and the evals focus, background and current posts
- https://hamel.dev/blog/posts/field-guide/ - the Field Guide, the canonical error-analysis-driven method
- https://hamel.dev/blog/posts/evals/ - "Your AI Product Needs Evals", the framing post
- https://maven.com/parlance-labs/evals - the course with subscriber and student counts
- https://arize.com/blog/rise-of-the-ai-engineer-why-ai-evals-fail-before-the-evaluation-begins/ - a critical look at why evals fail, featuring his views
