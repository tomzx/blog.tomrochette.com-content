---
title: "The Tells Are Structural"
created: 2026-09-02
updated: 2026-09-02
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3-flash, ai, llm, writing, evaluation]
readability: 3
audience_notes: >
  Assumes the reader is an engineer who regularly ships LLM-assisted writing (documentation, pull request replies, postmortems, design docs) and has watched readers discount such text as AI slop. No NLP background required; every study cited is summarized in plain terms.
---

I generate drafts with LLMs every day, and so does almost every engineer I know.
Somewhere along the way a reader can tell, and the text starts getting discounted before its content gets read.
**The popular fixes are word swaps, and word swaps fail because the tell is not the words, it is the structure.**
A 2026 study put numbers on this, and the numbers should change how you edit anything AI-assisted that other engineers will read.

## The humanizer trap

The market is full of humanizers that promise to scrub the AI out of a draft.
They do what you would expect: replace "delve" with "examine", break up em-dashes, vary sentence length, swap vocabulary.
The problem is that detection does not live on that layer.
StoryScope, a study from UMD and Google DeepMind (arXiv 2604.03136), built a dataset of about 61,600 stories written by humans and five frontier LLMs, then induced 304 interpretable narrative features like character agency, causal chain continuity, and how themes get handled.
A classifier using those narrative features alone, with no access to word choice at all, detected AI fiction at 93.2 percent macro-F1.
**On samples where surface style had been rewritten away, detection barely moved, holding at 93.9 percent.**
The vocabulary police are treating the one layer the signal demonstrably survives.

## What the structure layer actually is

So what gives it away, if not the words?
The features with the largest human-AI gaps are architectural.
A narrator steps out to explain the theme in 77 percent of AI stories versus 52 percent of human ones.
Emotions get rendered only as bodily sensation (a tight throat, a heavy chest) in 81 percent versus 38 percent.
There are no subplots in 79 percent versus 57 percent, and the ending arrives through the protagonist's internal acceptance in 47 percent versus 27 percent.
Human stories do the opposite of tidy: they name real books, places, and brands explicitly (47 percent versus 24 percent), and they wander.
The deepest finding in the paper is distributional: human stories sit in rarer, more spread-out regions of the feature space, with a median rarity percentile of 0.71 versus 0.49, and the human-to-AI centroid distance is 1.6 times the AI-to-AI distance.
**Human writing is detectable as an absence of clustering, which means applying every anti-AI rule at once just builds a new, equally clustered fingerprint.**
The sepia skill (about 1,444 stars on GitHub as of 2026-09-02, five days after release) turns this research into a working protocol, and its governing principle is the right one: calibrate to the human distribution, do not invert the AI one, and pick three to five structural moves per document rather than all of them.

## Your readers are the detectors that work

Maybe you think detection is a platform-moderation problem, some classifier somewhere, not your problem.
The evidence points the other way.
In a study of human detection (arXiv 2501.15654), five annotators who frequently use LLMs for writing tasks reached a majority vote that misclassified exactly 1 of 300 articles, which beat most commercial and open-source detectors even when the text had been paraphrased or humanized.
**Engineering audiences are precisely the heavy-LLM-users population, so your documentation is being read by the best detectors in existence.**
The practical threat is not an automated ban, and automated detectors remain weaker and more subjective than these humans (the slop-measurement study, arXiv 2509.19163, found binary slop judgments are somewhat subjective even between experts).
It is quieter than that: a skilled reader notices, and the trust discount starts before your argument does.
That is the prose twin of the code asymmetry in Who Maintains the Slop?, where generated work costs the reader more than it cost its producer.

## Engineering prose has its own structural layer

Fiction findings do not transfer one to one, and I do not want to pretend they do.
Professional writing legitimately rewards an explicit thesis, and this blog bolds its theses on purpose.
The nonfiction tells live one level up from vocabulary too, but they are different tells.
The LAMP study (arXiv 2409.14509) hired 18 professional writers to edit 1,057 LLM paragraphs, and the writers independently agreed on a seven-category taxonomy of LLM idiosyncrasies: cliches, unnecessary exposition, and their siblings.
Wikipedia maintains a field guide of signs of AI writing for its own editors, and it is mostly structural: promotional tone, filler that carries no information, hedging where a judgment was required, passages that acknowledge the reader nobody wrote for.
sepia's professional-pass rules match what good engineering style already demands: release notes lead with user impact, pull request replies answer first and cite file and line, postmortems are blameless toward people and merciless toward mechanisms, numbers come with conditions.
**The de-AI pass and the ordinary editing pass are the same pass, as long as you do it at the structure layer instead of the vocabulary layer.**
A draft that answers first, names real things, commits to judgments, and leaves slack in the rhythm is not a disguised AI draft; it is just a good draft.

## What to Do Next

Stop paying for word-level humanizers; the evidence says the money buys nothing that survives contact with a skilled reader.
Instead, budget one structural revision pass per AI-assisted document.
Run these checks: does every paragraph serve one announced theme, is every emotion or claim rendered as a bodily or formulaic placeholder, does the piece resolve too neatly through acceptance, where would a human have named a specific real thing, where did I hedge instead of judging.
Fix three to five of those per document and leave the rest alone.
If you review other people's writing, read structure rather than vocabulary; a draft with tidy causal chains and no subplots deserves your suspicion more than one that uses "delve".

## See also

- [Who Maintains the Slop?](../../who-maintains-the-slop/index.md) - the code-side twin of the trust asymmetry this essay describes for prose.
- [Rethinking Code Review in the Age of LLMs](../../rethinking-code-review-in-the-age-of-llms/index.md) - reviewing generated output, the code counterpart of the structural read proposed here.
- [Defects Flow Downstream, Fixes Must Flow Upstream](../../defects-flow-downstream/index.md) - the humanizer industry patches at the word layer; the same argument for fixing defects at the source applies to prose.

## References

- <https://arxiv.org/abs/2604.03136> - StoryScope: the 61,608-story dataset, 304 narrative features, 93.2 percent narrative-only detection, and the rarity and clustering findings.
- <https://arxiv.org/abs/2501.15654> - the expert-detector study: five frequent LLM users' majority vote misclassified 1 of 300 articles and beat most automated detectors.
- <https://arxiv.org/abs/2409.14509> - LAMP: 18 professional writers, 1,057 edited paragraphs, and the seven-category taxonomy of LLM writing idiosyncrasies.
- <https://arxiv.org/abs/2509.19163> - Measuring AI "Slop" in Text: the expert-derived slop dimensions and the subjectivity of binary slop judgments.
- <https://github.com/Nanako0129/sepia> - the open-source skill that operationalizes this research (write, review, refactor, recreate) with the calibrate-not-invert principle; about 1,444 stars as of 2026-09-02.
- <https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing> - Wikipedia's editorial field guide of structural AI-writing signs for nonfiction.
