---

title: Spending Your Unused Tokens to Make the World a Better Place
created: 2026-08-21
type: post
status: draft
tags: [ai, llm, tokens, altruism, fully-ai-generated, llm=glm-5.3]
readability: 3
audience_notes: >
  Assumes the reader pays for an LLM subscription or API budget and knows
  what tokens, rate limits, and reset windows are; no ML background needed.
agent_sessions:
  - ses_fddb6ddfbffeG6VqaS2gIwA6bk
---

**Every week, part of the token allowance I pay for expires unused, and the same is true for almost everyone with an AI subscription.**
The surplus is a small philanthropy budget on a reset schedule, and almost nobody spends that budget on purpose.
The tokens evaporate either way; the only open question is whether the tokens do useful work before hitting zero.

## A budget that melts

Subscription pricing is flat, but my usage is not.
On a heavy week I hit the limits by Tuesday; on a week of meetings and code review, most of my allowance dies quietly when the window resets.
Prepaid API credits are just as perishable in practice, because per-token prices keep falling and hoarded credit loses value while the credit sits.
The money is spent either way, so unused capacity is not savings; unused capacity is waste.

Donating surplus capacity is an old idea.
In 1999, [SETI@home](https://en.wikipedia.org/wiki/SETI@home) persuaded millions of people to hand over idle CPU cycles through a screensaver, and [BOINC](https://boinc.berkeley.edu), the platform that grew out of SETI@home, still routes volunteer compute to science projects today.
[Folding@home](https://foldingathome.org) ran donated GPUs hot for pandemic-era protein research.
**Tokens are simply the newest surplus that ordinary people own and never fully spend.**

## Triage the backlog of open source

Every healthy open source project has a pile of work nobody wants: stale bugs without reproduction steps, long issues without summaries, undocumented flags, untested edge cases.
Surplus tokens are well matched to the pile.
A spare hour can reproduce five stale bugs and post minimal test cases, or distill a ninety-comment thread into a summary a maintainer can act on in one minute.
The bar does not move because a model helped: every patch clears the same review a human patch would.
**The unglamorous backlog is exactly the work that a few spare million tokens can erase.**

## Translate free knowledge

Free software documentation, open textbooks, and nonprofit guides are dramatically thinner in most languages than in English.
Translation is the cleanest surplus-token job I know: mechanical enough to automate, important enough to matter, and cheap for a native speaker to verify compared with translating by hand.
Offer the work where a project already wants translations, follow the project's process, and review every line before the line ships.
A hundred good pages of translated documentation will outlive any chat session I have ever had.

## Make archives accessible

Image-heavy archives, oral history collections, and long recordings sit unusable by screen readers, search engines, and non-experts.
Alt text at scale, transcripts, and plain-language rewrites of dense public documents are generation-heavy and review-light, which is precisely the profile of a good surplus job.
The pattern is proven on the human side: [Distributed Proofreaders](https://www.pgdp.net) has turned volunteer attention into proofread Project Gutenberg texts for decades by splitting big jobs into small reviewed steps.
Machine drafts slot into the same pipeline as a first pass, with a human reviewer at the end, and the reviewer is you.

## Summarize the public record

City council meetings, court opinions, budgets, and regulatory filings are public and mostly unread.
Somewhere near you, a journalist or civic volunteer is compressing the material by hand tonight.
A surplus budget can turn three hours of meeting transcript into a skimmable brief with the decisions extracted, ready for the volunteer to verify.
The work is not glamorous, and that is the point: nobody else will do the work.

## Feed the model commons

Open models improve through public goods: evaluation data, adversarial test cases, and preference labels.
Volunteers have donated such material before; the [Open Assistant](https://huggingface.co/datasets/OpenAssistant/oasst1) project collected prompts, replies, and rankings from thousands of contributors into an open corpus anyone can train on.
Surplus tokens can generate candidate test cases, probe open-weight models for failure modes, and write the findings up for the teams building the next round of models.
Red-teaming an open model with published findings beats red-teaming a closed product with discarded findings.

## Run a batch for one nonprofit

No marketplace exists for donating leftover subscription capacity, and most providers' terms would frown on transferring credits anyway.
The workaround is to spend the tokens yourself on a specific organization's problems.
A food bank needs grant drafts cleaned up; a housing nonprofit needs a decade of messy spreadsheets normalized; a community clinic needs patient-facing text simplified.
One relationship, one standing weekly batch job, and the surplus has a destination.

## Guardrails

**Spending tokens still costs energy, even when the tokens feel free.**
The subscription fee is sunk, but inference has a real footprint, an argument [Green AI](https://arxiv.org/abs/1907.10597) made about research compute years before chat subscriptions existed.
Aim the surplus at work with lasting value rather than volume for the sake of volume.
The other rule is never to dump unreviewed output into a shared commons; [Wikipedia restricts LLM-generated content](https://en.wikipedia.org/wiki/Wikipedia:Large_language_models) precisely because unreviewed machine text taxes everyone who maintains the commons.
Every idea above keeps a human in the loop, and the human is the person holding the subscription.
Review capacity is the scarce resource, so fewer and better artifacts beat a flood of drafts.

## What to do next

Pick one destination for the quarter: one repository, one archive, or one nonprofit.
Reserve the last thirty minutes before the reset window and run one surplus job against the destination.
Keep a log of what the expiring allowance bought for other people, because the log turns an invisible habit into a visible one.
Start smaller than feels meaningful; a single proofread translation per week still clears the zero baseline.
**The tokens expire on the provider's schedule regardless; what the tokens buy before expiring is the only part you control.**

## See also

- [GlobaLLM: Automated Open Source Contribution at Scale](../agi/globallm-automated-open-source-contribution-at-scale/index.md) - a design for pointing large token budgets at open source maintenance automatically.
- [My AI Workflow: The Skills Are the Part That Compounds](../my-ai-workflow/index.md) - the spend-a-token-save-an-hour mindset that makes surplus capacity feel free.
- [You Are the Bottleneck: What to Do When Your Coworker's LLMs Outproduce Your Review](../you-are-the-bottleneck/index.md) - why review capacity, not generation capacity, is the limit when you add more agents.
- [The Future of Code Review: How AI Makes Human Review Obsolete](../the-future-of-code-review/index.md) - what engineering looks like once every engineer commands a large token allocation.
- [Six Months with OpenChamber](../six-months-with-openchamber/index.md) - measured evidence of how much capacity a subscription-style setup actually moves.

## References

- [SETI@home](https://en.wikipedia.org/wiki/SETI@home) - the screensaver-era precedent for donating idle personal compute.
- [BOINC](https://boinc.berkeley.edu) - the volunteer computing platform that outlived SETI@home.
- [Folding@home](https://foldingathome.org) - distributed disease research on donated home hardware.
- [Distributed Proofreaders](https://www.pgdp.net) - the human proofreading pipeline that machine drafts can feed into.
- [Open Assistant (OASST-1)](https://huggingface.co/datasets/OpenAssistant/oasst1) - an open corpus built from donated prompts and rankings.
- [Green AI](https://arxiv.org/abs/1907.10597) - the case for counting compute as a real cost.
- [Wikipedia: Large language models](https://en.wikipedia.org/wiki/Wikipedia:Large_language_models) - the encyclopedia's policy on LLM-generated content.
