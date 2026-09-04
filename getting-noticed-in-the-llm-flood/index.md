---

title: "Getting Noticed in the LLM Flood: Compete on What Cannot Be Generated"
created: 2026-08-14
type: post
status: finished
tags: [ai, llm, attention-economy, information-overload, self-promotion, content, fully-ai-generated, llm=glm-5.2, llm=glm-5.3]
readability: 3
audience_notes: >
  Assumes the reader makes things online (writing, software, videos, small products) and wants that work to be found in feeds that are increasingly filled with LLM-generated content. No technical background required.
agent_sessions:
  - ses_0593f1fb4ffekcvYC4VrUXxKzV
  - ses_033986bc9ffe2HUO2Hk5fdLWSK
  - ses_033922873ffe5mOotG2G03zZJl
---

For most of the internet's life, the rule was simple: make something good, put it somewhere findable, and the channels would carry the rest.
That rule assumed a scarcity that no longer holds.
**When a model can draft a competent essay, tutorial, landing page, or thread in seconds, the supply of "good enough" writing goes effectively infinite, and good stops being the thing that gets you noticed.**
The scarce thing has moved upstream, from content to the trust that lets any single reader pick your work out of the flood.

## The Flood Has Two Sides

A flood that is impossible to read is also a flood that is impossible to be read in.
These are the same problem seen from opposite ends.

The reader's version is a filtering problem: too much coming at you, too little time to sort it (see [Keeping Up With AI Is a Losing Strategy](../keeping-up-with-ai/index.md)).
The maker's version is a discovery problem: your work is one drop in a self-replenishing ocean, and the ocean refills faster than anyone can drink.

The root cause is identical.
As [Herbert Simon](https://en.wikipedia.org/wiki/Attention_economy) put it half a century before LLMs, "a wealth of information creates a poverty of attention."
**What changed is that the wealth of information stopped requiring people to produce it, so the supply curve bent from steep to vertical.**
Attention did not scale with it.
That leaves every creator competing for a fixed resource against a supply that has no ceiling.

## "Good" Is Now the Floor

It used to mean something to publish clear, well-structured, useful writing, because producing it took time, skill, and effort, and that effort was itself a signal.
When the median post can be generated in seconds and is, on the surface, as clean as anything a careful human would ship, clarity and structure stop signaling much.
They become the default, the price of entry, the thing readers expect and immediately forget.

This is [Sturgeon's law](https://en.wikipedia.org/wiki/Sturgeon%27s_law) ("ninety percent of everything is crud") with the dial turned up: not only is most content mediocre, but the mediocre is now polished enough to pass for good, which forces readers to assume everything is mediocre until proven otherwise.
**The practical effect is that competence no longer earns attention; it merely avoids an immediate bounce.**
You cannot out-write the flood, because the flood is now competently written.

## Compete on What Cannot Be Generated

If the surface layer is commoditized, the advantage moves to the layers a model cannot generate, and almost all of them are slow, specific, and human.
Kevin Kelly named these the "generatives" in [Better Than Free](https://kk.org/thetechnium/better-than-fre/): the qualities that stay valuable precisely because copies are free.
His list, written in 2008 about an earlier wave of abundance, maps almost perfectly onto the problem of being noticed now.
Four of them do most of the work.

**Authenticity** is the sense that a real, specific person made this for a reason they will stand behind.
A model can imitate a voice, and even the surface texture of the life behind it: a recorded mistake, a hard-won opinion, a detail only someone who was there would notice.
What it cannot provide is the underlying record that makes those details checkable, which is why authenticity has to be backed by proof rather than merely asserted (see Proof of Work, below).

**Embodiment** is the version of the work that lives in the physical, social world: a live talk, a conversation, a workshop, a thing you can point to in a room.
It cannot be copied at all because it is not made of text, and it is where the strongest trust gets built.

**Personalization** is work tuned to a specific reader or community rather than aimed at everyone.
The flood is generic by construction; anything that clearly was not, anything that names a particular reader's problem in a particular context, stands out against it by contrast alone.

**Findability** is the quality most creators neglect, and the focus of this whole article.
As Kelly wrote, "when there are millions of free things requesting our attention, being found is valuable."
**In a flood, distribution is not the layer you add after the work is good; it is the work.**

## Proof of Work Is the Signal That Survives

If readers now assume competence is fake by default, the only thing that reliably breaks through is evidence that a real person actually did the thing behind the writing.
Call it proof of work, borrowing a term from systems where trust is established by demonstrating costly effort rather than by asserting it ([proof of work](https://en.wikipedia.org/wiki/Proof_of_work)).

The tempting version of this claim is that the right story reads as authentic and therefore cannot be faked.
It does not survive contact with the models.
A fabricated postmortem with specific-sounding numbers, a plausible failure chain, and the right tonal markers passes most readers' filters, because few will check whether the project existed, whether the numbers are real, or whether the author lived it.
The cost asymmetry the argument depends on, expensive to produce but cheap to verify, inverts: the story is now nearly free to generate, verification still costs real effort, and readers rarely pay it.

What cannot be faked at scale is not the story but the record it claims to sit on.
A real project leaves a wide trail, commits, issues, deployed systems, other people who remember it, a history you can point to.
The postmortem itself is cheap to hallucinate; the artifacts it references are not.
The durable signal is not "does this read like lived experience" but "can I trace it to something independent of the author's word," and that is a harder bar than most writing clears.

That bar is why the familiar examples carry weight only when they are traceable.
A postmortem of a project that failed, with real numbers and real reasons, matters if you can link the project, the commit that introduced the bug, the incident report.
An experiment you actually ran, with setup and outcome, matters if the setup is reproducible and the data is there.
A thing you built and genuinely use matters if the repository exists, has a history, and other people can run it.
Strip the traceability and the same sentences are indistinguishable from hallucination.
**Proof of work is not a quality you can write into a paragraph; it is a verification surface you either leave behind or do not, and the cost that makes it trustworthy is paid in building that record, not in describing it.**

Proof of work is the producer's version of the moat argument elsewhere on this blog: when the easy-to-copy layer is free, the advantage relocates to the layers that compound through time and cannot be cloned (see [Feature Parity Is Not a Moat](../feature-parity-is-not-a-moat/index.md)).
For a creator, those layers are a track record, a body of specific work, and the relationships built around it.

## Be a Source, Not an Echo

Most generated content restates things other people already said, which means most of the flood is echo.
The way to stop being part of the flood is to be the thing it is restating.

A source is someone who produces a fact, an observation, a measurement, an argument, or a story that did not exist in that form before they wrote it.
An echo is everyone, human or machine, who restates it.
**The flood is almost entirely echo, which means even a small amount of genuine source material stands out clearly against it.**

The lever is to bias every piece toward the thing only you could have written: the result you observed, the mistake you made, the opinion you hold and can defend, the specific reader you are addressing.
Narrow beats broad here, because narrow is where specificity lives and specificity is what an echo cannot manufacture.
A durable body of narrow work also compounds: ten pieces on the same corner of a problem make you the address for that problem, where ten unrelated pieces make you another drop.

## Relationships Are the Distribution Layer That Does Not Saturate

Every algorithmic channel is now full, and getting fuller, and the curve points one way.
The one channel that does not saturate the same way is direct human relationship, the small set of people who know you, trust your work, and pass it on because they want to.

These are not "followers" in the metric sense; they are the thin layer of real acquaintance, [parasocial](https://en.wikipedia.org/wiki/Parasocial_interaction) or otherwise, that turns "I made a thing" into "someone I trust made a thing."
**Trust is the only distribution medium that the flood dilutes more slowly than it dilutes everything else, because trust cannot be manufactured by a model either.**
This is why the unglamorous work of replying, citing, collaborating, and showing up over years outperforms any broadcast tactic in a saturated feed.
It is also the version of distribution that compounds, while a clever hook compounds for about a day.

## The Bottleneck Moved to Trust

The uncomfortable reading of all this is that "make good things" was never the whole strategy; it was a strategy that worked while good things were scarce.
They are not scarce anymore, and they will not be again.

What is scarce, and getting scarcer, is the trust that lets a reader choose one piece out of a million.
**Trust is built only from the inputs a model cannot generate: your time, your experience, your track record, and your relationships.**
Getting noticed in the flood is not a louder version of the old playbook; it is the decision to stop competing on the layer that went free, and to put everything onto the layers that never will.

## What to Do Next

**Stop optimizing for volume.**
Posting more into an infinite stream makes you more of the stream, not more visible inside it, and the marginal post now competes with machines that post faster, for free.

**Bias every piece toward proof of work.**
If a reader cannot tell whether a real person did the thing behind the writing, they will assume not, so leave a verification surface they can actually check: link the repository, the data, the incident report, the commit, so the claim rests on something independent of your word rather than on how lived the prose sounds.

**Write what only you can write, and narrow until that is true.**
Specificity is the cheapest signal that survives generation, and a narrow, durable body of work is what makes you the address for a problem instead of a drop in the flood.

**Treat distribution as the work, not the afterthought.**
Findability is a generative in its own right, and in a flood it is the generative that decides whether any of the rest gets read.

**Build the channels that do not saturate.**
A small set of real relationships, maintained over years, will carry your work further than any algorithmic tactic, and it is the one distribution layer a model cannot generate.

## See also

- [Keeping Up With AI Is a Losing Strategy](../keeping-up-with-ai/index.md) - the reader's side of the same flood; this article is the producer's mirror image
- [Feature Parity Is Not a Moat](../feature-parity-is-not-a-moat/index.md) - when the copyable layer is free, advantage moves to layers that compound and cannot be cloned, the same relocation trust depends on
- [The Shifting Bottleneck](../the-shifting-bottleneck/index.md) - the pattern of the constraint moving one level up whenever a lower one is automated, here from content production to trust

## References

- [Attention economy (Wikipedia)](https://en.wikipedia.org/wiki/Attention_economy) - Simon's "a wealth of information creates a poverty of attention," the root framing for why a content flood is a trust problem
- [Kevin Kelly, "Better Than Free"](https://kk.org/thetechnium/better-than-fre/) - the "generatives" that stay valuable when copies are free, including authenticity, embodiment, personalization, and findability
- [Sturgeon's law (Wikipedia)](https://en.wikipedia.org/wiki/Sturgeon%27s_law) - "ninety percent of everything is crud," sharpened here by the fact that the crud is now polished enough to pass for good
- [Information overload (Wikipedia)](https://en.wikipedia.org/wiki/Information_overload) - the long-standing name for the reader's condition this article takes as its starting point
- [Proof of work (Wikipedia)](https://en.wikipedia.org/wiki/Proof_of_work) - trust established by demonstrating costly effort rather than by assertion, the property that lets real work stand out against generated content
- [Parasocial interaction (Wikipedia)](https://en.wikipedia.org/wiki/Parasocial_interaction) - the one-to-many relationship layer that distributes work without saturating the way algorithmic feeds do
