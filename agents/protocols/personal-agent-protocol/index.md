---
title: Personal Agent Protocol (Poppy)
created: 2026-11-07
updated: 2026-11-08
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, protocols, interoperability, oauth, agentic-commerce]
readability: 3
audience_notes: >
  Engineers deciding whether their company should publish a Poppy discovery file or their
  agent should speak the protocol, and who want the draft's actual maturity and adoption state
  before betting an integration on it.
  Assumes you know what OAuth scopes and MCP servers are.
---

The Personal Agent Protocol, nicknamed Poppy, is an open draft standard from Sierra and Meta for how a consumer's personal agent discovers a company, signs its user in over OAuth, and works within limits both sides set, across the company's website, its APIs, and its own agent.

**Poppy is the consumer front door of the protocol stack this category tracks, and its first month pairs unusually formal specification discipline with an adoption record that is still a placeholder: 43 named design partners, and exactly one partner serving a discovery file, a three-field stub with no sign-in.**

## What it is

Announced 2026-10-06 by Sierra's Bret Taylor and Clay Bavor with Meta, naming Genesys, Instinct, Rocket, Shopify, Stripe, and Walmart as partners, while Meta's same-day post named NiCE and Decagon instead of Instinct, and Decagon shipped its own competing PACT protocol that day.
Draft 0.1 followed on 2026-10-09 under the Poppy nickname with 35 more design partners, OpenAI among them.
A company publishes one discovery file at `/.well-known/poppy.json` saying how agents may interact, how customers sign in, and what agents can do; the agent identifies itself, starts a session as a guest or signs the user in, and works through the company's website, its OpenAPI or MCP interfaces, or its conversational company agent, in one session across all three.
The draft builds on OAuth, JWTs, DPoP token binding, HTTPS, OpenAPI, and MCP, and positions itself as complementary to shopping protocols such as Google and Shopify's UCP.
Apache-2.0, hosted at personalagentprotocol.org with feedback through issues on the spec repository.

## Status

**Active, fast-moving, and pre-1.0 by explicit policy: until 1.0, a revision can break compatibility with earlier drafts.**
The v0.1 the announcement promised for October shipped on schedule as draft 0.1 (2026-10-09), frozen at its own URL; 0.2 published 2026-10-24; 0.3 published and frozen 2026-11-04, the version that removed the protocol-defined `poppy:read` and `poppy:write` scopes in favor of company-defined scopes with reversible and irreversible consequence hints; draft 0.4 is open, mostly additions.
The path-to-1.0 page, updated 2026-11-04, lists 43 design partners who agreed to be named: three personal agents (Instinct, Meta, OpenAI), 21 companies (Walmart, Bank of America, Target, Rocket, PayPal/Venmo among them), and 19 technology providers (Stripe, Visa, Mastercard, Cloudflare, Okta, Shopify, Sierra among them), with payments, push notifications, signed approvals, attachments, and self-hosted agents declared open topics.
Repository created 2026-10-14, pushed 2026-11-08, 77 stars, 14 forks, 25 open issues, TypeScript (GitHub API, as of 2026-11-08).
The reference implementation Sierra promised on 2026-10-09 for the following month had not appeared on the spec site as of 2026-11-08 (the site's Demos page now says first-party demos are in development, with community demos listed meanwhile).
Meta named the protocol on its 2026-10-21 earnings call, with its CFO expecting uneven adoption (per the poppy.md coverage inventory).
The Hacker News footprint is thin for the partner count: one 9-point launch thread (2026-10-06) and a 4-point follow-up (2026-10-22).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=personal-agent-protocol/personal-agent-protocol&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=personal-agent-protocol/personal-agent-protocol&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=personal-agent-protocol/personal-agent-protocol&type=date&legend=top-left" />
</picture>

The deployment record is the gap: a third-party scan requesting the discovery file from 49 domains belonging to the 44 named partners on 2026-10-27 found one file, DIRECTV's, valid but a placeholder with no sign-in and an empty `web` object (Personal Agent Bench), and an earlier scan of 24,577 API-provider domains found five valid files, none from launch partners (API Evangelist, 2026-10-19).
Implementations do exist outside the partner list: a vendor-hosted signed-out-only integration (Salespeak for Panaya), a personal site running draft 0.2 read-only (movahedi.ca), and demo stores on the spec site.

## Strengths

- **Specification discipline no same-age protocol in this category matches**: frozen published drafts at per-version URLs, a dated changelog tagging every breaking change, and design moving issue by issue in public (the 0.4 changelog cites issues 66, 67, and 75 by number).
- Built almost entirely on standards engineers already run: the 0.3 restructuring makes the spec read as standard OAuth plus a signed session header, so a team can reuse its OAuth issuer, DPoP stack, and MCP servers.
- The 0.3 scope redesign is the draft's best idea: companies define their own scopes and carry machine-readable consequence hints (`changes`: reversible or irreversible, `personal_data`), so an agent can decide before sign-in which scopes need the user's approval.
- Secrets hygiene is written into the spec, not left to guidance: access tokens, session JWTs, private keys, and authorization codes must stay out of model context, following the IETF agent-identity draft.
- The coalition spans both sides of the door, consumer agent builders and the businesses those agents knock on, which neither UCP, Visa's TAP, nor Decagon's PACT assembled in one list.

## Cautions

- **Draft churn is structural, not incidental: four versions in four weeks, several carrying breaking changes, with pre-1.0 compatibility promised to nobody.** Early implementers lag quickly; three of the four non-partner implementations in the October scan still served 0.2 files defining scopes 0.3 had removed.
- Approval is the part the protocol cannot police, and its own Operations extension says so: `approved_by` works on trust because the company cannot see the agent's interface, so an agent that misreports its user's consent stays inside the protocol.
- Governance is steward-run: no foundation, no independent conformance suite, no neutral body, with feedback landing in the Sierra and Meta controlled repository, and Sierra also selling the customer-service implementation path to its own market.
- Mediated Sign-In, the credential pass-through the draft itself compares to OAuth's password grant, remains an extension until 1.0 sets its removal date; privacy reviewers flag it, with allowlists and stable per-company identifiers, as the design's sharpest edges.
- Partner overlap dilutes the coalition: Stripe, Shopify, Visa, Mastercard, Walmart, and Meta also sit in UCP, ACP, or TAP lanes, and Walmart's own 2026-10-21 agent program (Agent Profiles, an MCP gateway, agent terms) does not mention Poppy.
- Payments are not in the spec, and Anthropic and Amazon remain outside it.

## Pricing

Pricing does not apply: the specification, its site, and the repository are Apache-2.0 and free, with no certification or hosted component announced.

## Compared to

- [MCP](../mcp/index.md): the tool-connection layer Poppy deliberately rides on; Poppy adds what MCP leaves out for this use, the agent's identity, a pseudonymous user, account sign-in, and one session across channels.
- [A2A](../a2a/index.md): agent-to-agent interop between platforms; Poppy is the consumer-agent-to-company lane, and its per-company pseudonymous user ID answers a question A2A never asks.
- [PIC Standard](../pic-standard/index.md): the other permission contract in this category; PIC gates one tool call pre-execution on provenance evidence, Poppy grants standing account access over OAuth scopes, and one deployment could reasonably carry both.
- Visa's Trusted Agent Protocol and Google's UCP cover adjacent lanes, signed agent identity from the card networks and shopping checkout, with overlapping partners, and beri.net's four-standard comparison is the grounded read on how they stack.

## Bottom line

**Recommended for tracking and policy work now, implementation later: write your guest, read, and write permission tiers and OAuth scope design this quarter, because that work transfers to Poppy, UCP, or TAP whichever wins, and publish a discovery file only when a 1.0 or a design-partner implementation path makes the churn someone else's problem.**
Not for betting customer-facing flows on a draft that promises incompatibility between revisions, and not as an MCP or A2A substitute in engineering stacks.
My disagreeable claim: the adoption test that matters is beri.net's bar, whether by early 2027 an agent with no Sierra and no Meta inside it completes authorized transactions at companies that are not Sierra customers, and on today's evidence, one stub file among 44 partners, the front door is drawn but not yet built.

## Changes

- 2026-11-07 - Created from the coordinator's 2026-11-03 admission handoff, with the published-draft record (0.1 through 0.4) replacing the unshipped-v0.1 fact the handoff carried, the one-of-44-partners deployment scan as the adoption gap, and beri.net's pre-spec comparison as the standing critical source.

## See also

- [Model Context Protocol (MCP)](../mcp/index.md) - the tool layer Poppy lists as one of its API lanes
- [Agent Network Protocol (ANP)](../anp/index.md) - the open-web discovery bet; Poppy's per-company pseudonymous IDs are the platform-mediated opposite
- [PIC Standard](../pic-standard/index.md) - the pre-execution gating contract at the tool boundary Poppy's standing scopes sit above
- [Protocols Feature Matrix](../protocols-feature-matrix/index.md) - the category comparison this note joins as the fourteenth column

## References

- https://sierra.ai/blog/introducing-personal-agent-protocol - the 2026-10-06 announcement: the OAuth session design, launch partners, the promised v0.1, workshops, and reference implementation (fetched 2026-11-07)
- https://sierra.ai/blog/poppy - the 2026-10-09 draft post: the Poppy name, the five building blocks, and the 35 additional design partners including OpenAI (fetched 2026-11-07)
- https://personalagentprotocol.org/docs/changelog - the version train: 0.1 published 2026-10-09, 0.2 on 2026-10-24, 0.3 frozen 2026-11-04, draft 0.4 in progress with per-change breaking tags (fetched 2026-11-07)
- https://personalagentprotocol.org/docs/path-to-1 - the status line updated 2026-11-04, the open topics, and the 43 named design partners (fetched 2026-11-07)
- https://personalagentprotocol.org/docs/introduction - the principles (existing standards, controls not policy, progressive adoption) and the Apache-2.0 license (fetched 2026-11-07)
- https://api.github.com/repos/personal-agent-protocol/personal-agent-protocol - repository facts: 77 stars, 14 forks, 30 open issues, created 2026-10-14, pushed 2026-11-06, Apache-2.0, TypeScript (GitHub API, as of 2026-11-07)
- https://www.beri.net/article/meta-sierra-personal-agent-protocol-oauth-guest-read-write-access-vs-ucp-acp-trusted-agent-protocol-retail-banks - the standing critical source, dated pre-spec (2026-10-07): the four-standard comparison with UCP, ACP, and TAP, the partner-hedging record, the permission-tier advice, and the adoption test
- https://personalagentbench.com/personal-agent-protocol/ - the independent partner scan (one file among 44 partners on 2026-10-27), the scope-history read (poppy:read and poppy:write removed in 0.3), and the approval-trust gap (fetched 2026-11-07)
- https://apievangelist.com/2026/10/19/the-first-poppy-files-and-the-one-a-vendor-wrote/ - five valid poppy.json files across 24,577 API providers, none from launch partners, and the vendor-hosted file the 0.2 redirect rule closed (fetched 2026-11-07)
- https://hn.algolia.com/api/v1/search?query=%22Personal%20Agent%20Protocol%22&tags=story - the footprint scan: one 9-point launch thread (2026-10-06) and a 4-point follow-up (2026-10-22)
- https://poppy.md/press.html - the independent coverage inventory: Meta's Q3-earnings naming, the Meta-versus-Sierra partner-list difference, and the community scan links (fetched 2026-11-07)
