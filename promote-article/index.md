---

title: Promote article
created: 2021-03-07
type: post
readability: 3
status: finished
tags: [self-promotion]
agent_sessions:
  - ses_130ad8b9cffeXe0hzXcBOHkDkf
  - ses_0a63424b6ffe1wuysOohhZVAnS
---

## Context
Writing an article is only half the work. If nobody knows it exists, it does not matter how good it is. This is a reusable checklist of where and how to share an article once it is published, ordered roughly by expected return per unit of effort.

The goal is to post broadly (since posting is cheap when automated) while keeping each post native to its platform.

# Automation
Run `python3 promote-article.py <slug>` to generate platform-native copy for every fitting platform at once. The script reads the article's front matter and content, extracts the thesis, picks platforms by tag fit, and writes `promote-<slug>.md` with ready-to-paste drafts and pre-filled submit links.

```
python3 promote-article.py the-acceptance-gap
python3 promote-article.py the-acceptance-gap --platforms=hn,reddit,mastodon
```

Supported platforms: hn, lobsters, reddit, devto, mastodon, bluesky, x, linkedin.

# Selecting channels by fit
The script auto-selects platforms from article tags. The mapping mirrors this manual guidance:

* **Deep technical / tooling I built**: Hacker News, Lobsters, relevant subreddit.
* **AI / LLM / ML**: Hacker News, r/LocalLLaMA, r/MachineLearning, X, LinkedIn.
* **Opinion / career / process**: X, LinkedIn, dev.to cross-post.
* **Niche tutorial / fix**: the specific subreddit, Stack Overflow (as a link in an answer), the relevant tag on dev.to / Hashnode.

# Primary channels (highest signal)
* **Hacker News** (news.ycombinator.com): one of the biggest single sources of traffic for technical writing. Use a neutral, descriptive title. Avoid clickbait, it gets flagged. Only submit to "Show HN" if it is something you built.
* **Lobsters** (lobste.rs): smaller and higher signal than HN. Invite-only; ask for an invite in their invite thread. Strong fit for deep technical posts.
* **Reddit**: pick the single best subreddit for the topic. Each subreddit has its own self-promotion rules (commonly the 10% rule), so participate beyond just posting your links.
  * r/programming, r/MachineLearning, r/LocalLLaMA, r/artificial, r/Productivity, r/devops, r/php, r/kubernetes.
* **Direct outreach**: email or message the author of a post I referenced, with my related article. Reply substantively in existing HN / Reddit threads where my article is the answer, only when genuinely relevant. Highest conversion per effort.

# Secondary channels (cross-posting)
* **dev.to / Hashnode / Medium**: republish with a canonical URL pointing to the original post so I capture their distribution without losing SEO.
* **X / Twitter**: short hook plus link, pin it to my profile. Engage with the AI / dev community accounts, do not just broadcast.
* **LinkedIn**: surprisingly strong for career-flavored and "software engineering teams in the age of AI" type posts. Cross-post there too.
* **Bluesky**: growing dev / AI audience, lower noise than X right now.
* **Mastodon** (fosstodon.org, hachyderm.io): tech-friendly, good for longer-form takes.

# Targeted channels
* **Slack / Discord communities** I already participate in (LLM tooling, local AI, alumni channels). Only share when the article is genuinely relevant to that group.
* **IRC**: for the old-school communities I still frequent.
* **Newsletters**: pitch myself as a source to newsletters that cover my niches (TLDR AI, Latent Space, Hacker Newsletter, Changelog). Commenting substantively on their posts is the on-ramp.

# Building a durable audience
Traffic from a single share is ephemeral. A few habits compound over time:

* **Follow relevant people** on X / Bluesky / Mastodon to increase potential followers (bidirectional relationships still work).
* **Internal-link** related posts (I have clusters like `code-factories-*`, `code-review-*`, `*-wsl`) to keep readers on site and boost ranking.
* **Update older popular posts** with links to newer related ones.
* **SEO basics**: clear title and meta description per post, descriptive slug. The front matter already controls this.
* **Get the opinion of specific people** I respect on the topic. Their feedback often leads to a second round of sharing.

# Cadence
* One primary post per article: HN or the single best subreddit, not both at once.
* Wait 1 to 2 days, then cross-post to secondary channels if it gained traction.
* Keep a per-article promotion log so I can learn which channels actually drove traffic.

# Per-article checklist
* [ ] Picked the single best primary channel for the topic.
* [ ] Wrote a neutral, descriptive title for submission.
* [ ] Checked the channel's self-promotion rules.
* [ ] Scheduled secondary cross-posts 1 to 2 days later.
* [ ] Notified / referenced authors of related work.
* [ ] Set the canonical URL if cross-posting.
* [ ] Internal-linked related articles on my own blog.
* [ ] Logged which channels were used and the resulting traffic.

# See also
* [Reusable writing](../reusable-writing/index.md)

# References
* https://news.ycombinator.com
* https://lobste.rs
