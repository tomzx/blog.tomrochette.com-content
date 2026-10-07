---
title: llms.txt
created: 2026-10-07
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, protocols, conventions, context-files, web]
readability: 3
audience_notes: >
  Engineers who publish documentation or websites that agents read and who must decide whether an
  llms.txt file and its v2 link machinery are worth maintaining.
  Assumes you know what robots.txt, sitemaps, and Markdown are.

---

llms.txt is an open convention, proposed by Jeremy Howard of Answer.AI in September 2024, for a Markdown file at a site's root that indexes the site's content for language models, revised to v2 in August 2026 with standard link relations that let an agent discover the file and each page's Markdown version mechanically.

**The convention split its adoption down the middle: the docs-and-coding-agent side adopted it, with thousands of sites publishing one and documentation platforms generating one automatically, while the search side rejected it, with Google's John Mueller calling it purely speculative, and the v2 revision is the docs side winning.**

## What it is

A Markdown file served at `/llms.txt` (or, since v2, at any path root, covering the pages under that path) with an H1 carrying the project name, a blockquote summary, and sections of links with one-line descriptions, plus an optional companion full-content file.
Pages that agents may need are asked to serve a clean Markdown version at their own URL, either by appending `.md` or replacing the extension, both blessed in v2.
**V2 (August 2026) added the discoverability machinery: `rel="alternate" type="text/markdown"` points to a page's Markdown version and `rel="describedby"` points to the covering llms.txt file, expressible as HTML `<link>` elements or an HTTP `Link:` header, so agents can find the files without guessing URLs.**
It is a convention, not a foundation standard: no required fields, no registry, no versioning beyond the spec site's own v1 and v2.

## Status

**Active and adopted exactly where it aimed, and ignored exactly where it did not.**
The spec site reports that thousands of sites publish an llms.txt file, that documentation platforms generate one automatically, and that coding agents use them reliably, and this run fetched live files from Anthropic's developer docs (825 lines) and OpenAI's developer docs to confirm the served reality (2026-10-07).

The community footprint is substantial for a file convention: the launch thread drew 206 points and 175 comments on Hacker News (2024-09-03), a directory-of-files thread drew 106 points (2024-12-23), and generator tools have shipped steadily since.
The skeptical record is equally firm: Google's John Mueller called the file "purely speculative for now" in June 2026 and pointed to WebMCP as the Google-backed alternative, and a 2025 industry piece reported that major AI platforms do not even request the file in their crawls.
Search-engine adoption, the hope that pulled in the SEO crowd, never arrived.

## Strengths

- **Zero tooling to adopt: a Markdown file any site can ship, which is why docs platforms could make it default-on for new documentation.**
- The v2 link relations make discovery mechanical: an HTTP `Link:` header added in server or CDN configuration works without touching any page, and works for non-HTML resources too.
- The `.md` companion convention gives agents a clean page mirror that parses reliably, unlike scraped HTML.
- Coding agents are the consumer that actually showed up, so a docs site that serves llms.txt is directly improving the tooling this corpus covers.

## Cautions

- **The search payoff the convention was often sold on does not exist: Google ignores the file, and Mueller's server-logs point (AI crawlers do not request it) is the sharpest form of that criticism.**
- Governance is author-driven (Answer.AI), with no foundation, working group, or implementer conformance process, so v2's blessing of divergent practice is consensus by declaration.
- Adjacent conventions fragment the space: ai.txt permissions files, robots.txt AI directives, and commerce variants all compete for the same well-known-file slot.
- V2 is two months old as of this run, so tooling support for the link relations is still uneven.

## Pricing

Does not apply: it is a free file convention with nothing to buy.
The cost is authoring and maintaining the index (or checking that the docs platform's auto-generation stays accurate) plus adding the v2 headers.

## Compared to

- [AGENTS.md](../agents-md/index.md): the repo-scope instruction file versus the site-scope content index; both are plain-Markdown conventions agents read, and a docs site can carry both.
- [WebMCP](../webmcp/index.md): the capability bet versus the content bet; a site that wants agents to act exposes tools through WebMCP, while llms.txt helps agents that want to read, and Mueller's own dismissal of the one in favor of the other is the clearest statement of that split.
- robots.txt and ai.txt: permissions files that say what agents may not do; llms.txt is the opposite sign, a helpfulness file saying what agents should read.

## Bottom line

**Recommended for any documentation surface agents read: the file is cheap, v2's headers make it discoverable without touching pages, and the coding agents in this index are the audience that actually fetches it.**
Not worth adopting as an SEO play, since search ignores it entirely.
My disagreeable claim: llms.txt succeeded by failing at its original goal, because the search-discovery framing died and the convention survived as a docs-surface convention for coding agents, which is a better market than the one it was proposed for.

## Changes

- 2026-10-07 - Created from the 2026-10-07 entrant scan (the site-content-discovery slot), with the docs-side adoption versus search-side rejection split recorded as the central tension.

## See also

- [AGENTS.md](../agents-md/index.md) - the repo-level sibling convention, and the precedent for file conventions in this category
- [WebMCP](../webmcp/index.md) - the browser capability lane that Google's critique of llms.txt points to instead
- [Model Context Protocol (MCP)](../mcp/index.md) - the tool layer a site can add once agents are reading its content
- [Protocols Feature Matrix](../protocols-feature-matrix/index.md) - the category comparison this note joins as the eleventh column

## References

- https://llmstxt.org/ - the spec site: author (Jeremy Howard), published 2024-09-03, modified 2026-08-10, the v2 format and link relations
- https://llmstxt.org/changes.html - the v2 changelog (August 2026): link relations, both `.md` URL forms, subpath scoping, and the adoption summary
- https://docs.anthropic.com/llms.txt - Anthropic's served llms.txt, 825 lines, fetched 200 this run
- https://developers.openai.com/llms.txt - OpenAI's served llms.txt, fetched 200 this run
- https://www.searchenginejournal.com/google-says-llms-txt-is-purely-speculative-for-now/577576/ - Google's John Mueller calling the file purely speculative (June 2, 2026) and favoring WebMCP
- https://ppc.land/llms-txt-adoption-stalls-as-major-ai-platforms-ignore-proposed-standard/ - the adoption-stalls record: major AI platforms not requesting the file
- https://hn.algolia.com/api/v1/search?query=%22llms.txt%22&tags=story - the footprint scan: launch thread 206 points and 175 comments (2024-09-03), directory thread 106 points (2024-12-23), generator tools since
