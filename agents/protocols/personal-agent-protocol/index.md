---
title: Personal Agent Protocol (Poppy)
created: 2026-11-07
updated: 2026-11-15
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, protocols, interoperability, oauth, agentic-commerce]
readability: 3
audience_notes: >
  Engineers deciding whether their company should publish a Poppy discovery file or their
  agent should speak the protocol, and who want the draft's actual maturity and adoption state
  before betting an integration on it.
  Assumes you know what OAuth scopes and MCP servers are.
---

The Personal Agent Protocol, nicknamed Poppy, is an open standard from Sierra and Meta for how a consumer's personal agent discovers a company, signs its user in over OAuth, and works within limits both sides set, across the company's website, its APIs, and its own agent.

**Poppy is the consumer front door of the protocol stack this category tracks, and it went from first draft to frozen 1.0 in five weeks with a deployment record no protocol here matched at that age: 1.0 published and frozen on 2026-11-14, Shopify auto-publishing a Poppy file for every merchant storefront, Meta's Muse checking Poppy first on every site it visits, and 103 named design partners after the 2026-11-13 roster expansion.**

## What it is

Announced 2026-10-06 by Sierra's Bret Taylor and Clay Bavor with Meta, naming Genesys, Instinct, Rocket, Shopify, Stripe, and Walmart as partners, while Meta's same-day post named NiCE and Decagon instead of Instinct, and Decagon shipped its own competing PACT protocol that day.
Draft 0.1 followed on 2026-10-09 under the Poppy nickname with 35 more design partners, OpenAI among them.
A company publishes one discovery file at `/.well-known/poppy.json` saying how agents may interact, how customers sign in, and what agents can do; the agent identifies itself, starts a session as a guest or signs the user in, and works through the company's website, its OpenAPI or MCP interfaces, or its conversational company agent, in one session across all three.
The draft builds on OAuth, JWTs, DPoP token binding, HTTPS, OpenAPI, and MCP, and positions itself as complementary to shopping protocols such as Google and Shopify's UCP, with Shopify co-authoring the commerce extension that links the two.
Apache-2.0, hosted at personalagentprotocol.org with feedback through issues on the spec repository.

## Status

**Active and past 1.0: the train ran 0.1 (2026-10-09), 0.2 (2026-10-24), 0.3 (2026-11-04, the version that removed the protocol-defined `poppy:read` and `poppy:write` scopes in favor of company-defined scopes with reversible and irreversible consequence hints), and 0.4 (2026-11-10, the 1.0 release candidate, which made Direct Sign-In the preferred sign-in type and accepted the cross-device sign-in-started-by-someone-else risk with mitigations in section 10.8), and 1.0 was published and frozen on 2026-11-14, five weeks after the first draft.**
1.0 is 0.4 with implementer fixes: the six breaking majors the draft carried shipped as recorded (conversation protocol descriptions, Pushed Authorization Requests, PS384 required for client assertions and delegations, consent pages listing every scope granted before, the same DPoP key required at refresh, and UCP scope requests naming every scope), joined by three breaking minors (a five-minute client-assertion lifetime, one sign-in covering every resource with each later token request naming one resource, and `working` narrowed to mean only that a reply is in progress), the fixes-not-features policy retired, and 1.x versions now adding features without breaking 1.0 implementations through per-request version negotiation.
**1.0 also set the Mediated Sign-In retirement date every pre-1.0 draft had deferred: the extension is planned to retire on March 17, 2027.**
The path-to-1.0 page's status line now reads "Version 1.0 is published" (updated 2026-11-14), over the roster the 2026-11-13 commits built: 103 named design partners, four personal agents (Instinct, Manus, Meta, OpenAI) and 99 companies (1Password, Adyen, Delta Air Lines, ElevenLabs, GEICO, Gap Inc., Intuit, Notion, Salesforce, Twilio, United Airlines, Wells Fargo, Zoom, and the previously recorded Walmart, Bank of America, Target, Rocket, PayPal/Venmo, Stripe, Visa, Mastercard, Cloudflare, Okta, Shopify, Sierra among them), with payments, push notifications, signed approvals, attachments, and self-hosted agents on the roadmap alongside the Mediated Sign-In drop.
Repository created 2026-10-14, pushed 2026-11-14, 77 stars (as of 2026-11-12), 18 forks, 38 open issues, MDX (GitHub API, as of 2026-11-15).
**The deployment record moved with 1.0: Sierra's 2026-11-13 release post claims Shopify enabled Poppy for every merchant (each storefront auto-publishes a Poppy file, and Shopify co-authored the commerce extension linking Poppy to UCP), Meta's Muse now looks for Poppy first on every site it visits, and Mercury, Synchrony, and Turkish Airlines are named live.**
The scan record brackets the wave: a third-party check of 49 domains belonging to the 44 then-named partners found one file, DIRECTV's, valid but a placeholder with no sign-in and an empty `web` object (2026-10-27, Personal Agent Bench), an earlier scan of 24,577 API-provider domains found five valid files none from launch partners (2026-10-19, API Evangelist), a site scanner counted 27 live files none from a design partner (2026-10-14, per the poppy.md press inventory), and a Shopify storefront fetched 2026-11-15 outside the announcement (Allbirds) serves the auto-published file declaring protocol 0.4 with UCP checkout scopes, confirming the mechanism and showing the wave still speaks the 0.4 document.
Sierra's promised reference implementation has not appeared as a server; 1.0 shipped with an implementation kit and validator at personalagentprotocol.org/kit/company instead.
Meta named the protocol on its 2026-10-21 earnings call, with its CFO expecting uneven adoption (per the poppy.md coverage inventory).
The Hacker News footprint is thin for the partner count: four stories totaling 16 points, the 9-point launch (2026-10-06), a 4-point follow-up (2026-10-22), a 2-point explainer (2026-10-07), and a 1-point map post (2026-10-26).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=personal-agent-protocol/personal-agent-protocol&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=personal-agent-protocol/personal-agent-protocol&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=personal-agent-protocol/personal-agent-protocol&type=date&legend=top-left" />
</picture>

Implementations outside the partner list exist: a vendor-hosted signed-out-only integration (Salespeak for Panaya), a personal site running draft 0.2 read-only (movahedi.ca), and demo stores on the spec site.

## Strengths

- **Specification discipline no same-age protocol in this category matches**: frozen published drafts at per-version URLs, a dated changelog tagging every breaking change, and design moving issue by issue in public (the 0.4 changelog cites issues 66, 67, and 75 by number).
- Built almost entirely on standards engineers already run: the 0.3 restructuring makes the spec read as standard OAuth plus a signed session header, so a team can reuse its OAuth issuer, DPoP stack, and MCP servers.
- The 0.3 scope redesign is the draft's best idea: companies define their own scopes and carry machine-readable consequence hints (`changes`: reversible or irreversible, `personal_data`), so an agent can decide before sign-in which scopes need the user's approval.
- Secrets hygiene is written into the spec, not left to guidance: access tokens, session JWTs, private keys, and authorization codes must stay out of model context, following the IETF agent-identity draft.
- The coalition spans both sides of the door, consumer agent builders and the businesses those agents knock on, which neither UCP, Visa's TAP, nor Decagon's PACT assembled in one list.

## Cautions

- **The five-week draft train broke compatibility at every step, and early implementers were left behind**: three of the four non-partner implementations in the October scan still served 0.2 files defining scopes 0.3 had removed, and the storefront wave still serves the 0.4 document, not 1.0 (the Allbirds file fetched 2026-11-15). The 1.0 freeze plus minor-versioning (1.x adds behavior only for agents that declare that version) is the fix, so the churn story is now about the archives, not the next release.
- Approval is the part the protocol cannot police, and its own Operations extension says so: `approved_by` works on trust because the company cannot see the agent's interface, so an agent that misreports its user's consent stays inside the protocol. The 0.4-era operations version 3 added agent-approved operations on standing user instructions, widening the surface the trust assumption covers.
- Governance is steward-run: no foundation, no independent conformance suite, no neutral body, with feedback landing in the Sierra and Meta controlled repository, and Sierra also selling the customer-service implementation path to its own market.
- Mediated Sign-In, the credential pass-through the draft itself compares to OAuth's password grant, now carries its 1.0-set retirement date (March 17, 2027) but stays live until then; privacy reviewers flag it, with allowlists and stable per-company identifiers, as the design's sharpest edges.
- **The deployment record is vendor-announced**: Shopify-wide publishing, Muse Poppy-first, and the named live partners all come from Sierra's own release post; the independent scans that checked partner domains before the wave found placeholders and refusals, and no independent measurement of the wave exists yet.
- Partner overlap dilutes the coalition: Stripe, Shopify, Visa, Mastercard, Walmart, and Meta also sit in UCP, ACP, or TAP lanes, Walmart's own 2026-10-21 agent program (Agent Profiles, an MCP gateway, agent terms) does not mention Poppy, and payments are still a roadmap topic with Anthropic and Amazon outside the partner list.

## Pricing

Pricing does not apply: the specification, its site, and the repository are Apache-2.0 and free, with no certification or hosted component announced.

## Compared to

- [MCP](../mcp/index.md): the tool-connection layer Poppy deliberately rides on; Poppy adds what MCP leaves out for this use, the agent's identity, a pseudonymous user, account sign-in, and one session across channels.
- [A2A](../a2a/index.md): agent-to-agent interop between platforms; Poppy is the consumer-agent-to-company lane, and its per-company pseudonymous user ID answers a question A2A never asks.
- [PIC Standard](../pic-standard/index.md): the other permission contract in this category; PIC gates one tool call pre-execution on provenance evidence, Poppy grants standing account access over OAuth scopes, and one deployment could reasonably carry both.
- Visa's Trusted Agent Protocol and Google's UCP cover adjacent lanes, signed agent identity from the card networks and shopping checkout, with overlapping partners, and beri.net's four-standard comparison is the grounded read on how they stack.

## Bottom line

**Recommended now for any company whose customers' agents arrive unannounced: 1.0 is frozen, the implementation kit walks setup with a validator, and Shopify merchants already publish the file by default, so the remaining work is the permission-tier design, which ports to UCP or TAP whichever wins.**
Not as an MCP or A2A substitute in engineering stacks, and not yet for irreversible flows, since payments remain a roadmap topic.
My disagreeable claim: the front door now has a landlord, but beri.net's test still separates the announcement from the fact: the agent that checks Poppy first today is Meta's own Muse, and the bar, a non-Meta agent completing authorized transactions at companies that are not Sierra customers by January 2027, stays unmet on today's evidence, with a demand-side agent outside the two stewards yet to appear.

## Changes

- 2026-11-07 - Created from the coordinator's 2026-11-03 admission handoff, with the published-draft record (0.1 through 0.4) replacing the unshipped-v0.1 fact the handoff carried, the one-of-44-partners deployment scan as the adoption gap, and beri.net's pre-spec comparison as the standing critical source.
- 2026-11-12 - Draft 0.4 published and frozen 2026-11-10 as the 1.0 release candidate (Direct Sign-In preferred, the someone-else-started-sign-in risk accepted with mitigations), with a draft 1.0 in progress and the stated policy that changes before 1.0 are fixes, not features, and can still break compatibility; the reference implementation the 2026-10-09 post promised for the following month still has not appeared; the design-partner roster holds at 43 with the repository pushed 2026-11-11 (15 forks, 25 open issues); the Status section moved with the release-candidate promotion.
- 2026-11-14 - The design-partner roster tripled past the recorded 43 names: commits on 2026-11-13 folded the former technology-providers tier into the companies list and expanded the path-to-1.0 roster to 103 named partners (four personal agents, Manus joining Instinct, Meta, and OpenAI, and 99 companies adding 1Password, Adyen, Delta Air Lines, ElevenLabs, GEICO, Gap Inc., Intuit, Notion, Salesforce, Twilio, United Airlines, Wells Fargo, and Zoom among many others) while the page's status line still reads November 11; the draft 1.0 changelog now carries six breaking changes (conversation protocol descriptions, Pushed Authorization Requests, PS384 for client assertions and delegations, consent pages listing every scope granted before, the same DPoP key at refresh, and UCP scope requests naming every scope); the repository pushed 2026-11-13 (15 forks, 34 open issues); the intro claim, the Status section, and the path-to-1.0 reference moved with the roster and the draft record.
- 2026-11-15 - Out-of-rotation re-verification on the 1.0 signal: 1.0 was published and frozen on 2026-11-14 (0.4 plus implementer fixes, the six breaking majors shipped as recorded plus three breaking minors, the fixes-not-features policy retired, and 1.x versioned so features stop breaking 1.0 implementations), and 1.0 set the Mediated Sign-In retirement date the drafts had deferred, March 17, 2027; Sierra's 2026-11-13 release post claims Shopify enabled Poppy for every merchant, Muse looks for Poppy first, and Mercury, Synchrony, and Turkish Airlines are live, confirmed on the supply side this run by an independent Shopify storefront's fetched discovery file (protocol 0.4); the path-to-1.0 status line now reads "Version 1.0 is published"; the Status section, intro claim, churn and Mediated-Sign-In cautions, and Bottom line moved with the freeze and the deployment record; repository facts refreshed (pushed 2026-11-14, 18 forks, 38 open issues), the HN footprint re-counted at four stories, and the release post, the storefront file, and the re-fetched sources moved into References.

## See also

- [Model Context Protocol (MCP)](../mcp/index.md) - the tool layer Poppy lists as one of its API lanes
- [Agent Network Protocol (ANP)](../anp/index.md) - the open-web discovery bet; Poppy's per-company pseudonymous IDs are the platform-mediated opposite
- [PIC Standard](../pic-standard/index.md) - the pre-execution gating contract at the tool boundary Poppy's standing scopes sit above
- [Protocols Feature Matrix](../protocols-feature-matrix/index.md) - the category comparison this note joins as the fourteenth column

## References

- https://sierra.ai/blog/introducing-personal-agent-protocol - the 2026-10-06 announcement: the OAuth session design, launch partners, the promised v0.1, workshops, and reference implementation (fetched 2026-11-07)
- https://sierra.ai/blog/poppy - the 2026-10-09 draft post: the Poppy name, the five building blocks, and the 35 additional design partners including OpenAI (fetched 2026-11-07, re-fetched 2026-11-15)
- https://sierra.ai/blog/releasing-poppy - the 2026-11-13 release post: v1.0 available, Shopify enabled for every merchant with auto-published Poppy files, Muse Poppy-first, Mercury, Synchrony, and Turkish Airlines live, and the implementation kit with validator (fetched 2026-11-15)
- https://personalagentprotocol.org/docs/changelog - the version train: 0.1 published 2026-10-09, 0.2 on 2026-10-24, 0.3 frozen 2026-11-04, 0.4 published and frozen 2026-11-10 as the 1.0 release candidate, 1.0 published and frozen 2026-11-14 with its breaking-change tags and the Mediated Sign-In retirement date of March 17, 2027 (re-fetched 2026-11-15)
- https://personalagentprotocol.org/docs/path-to-1 - the status line updated 2026-11-14 now reading "Version 1.0 is published", the 103 named design partners (four personal agents, 99 companies), and the roadmap including the Mediated Sign-In drop (re-fetched 2026-11-15)
- https://personalagentprotocol.org/docs/introduction - the principles (existing standards, controls not policy, progressive adoption) and the Apache-2.0 license (fetched 2026-11-07, re-fetched 2026-11-15)
- https://api.github.com/repos/personal-agent-protocol/personal-agent-protocol - repository facts: 77 stars (as of 2026-11-12), 18 forks, 38 open issues, created 2026-10-14, pushed 2026-11-14, Apache-2.0, MDX (GitHub API, as of 2026-11-15)
- https://www.beri.net/article/meta-sierra-personal-agent-protocol-oauth-guest-read-write-access-vs-ucp-acp-trusted-agent-protocol-retail-banks - the standing critical source, dated pre-spec (2026-10-07): the four-standard comparison with UCP, ACP, and TAP, the partner-hedging record, the permission-tier advice, and the adoption test
- https://personalagentbench.com/personal-agent-protocol/ - the independent partner scan (one file among 44 partners on 2026-10-27), the scope-history read (poppy:read and poppy:write removed in 0.3), and the approval-trust gap (fetched 2026-11-07, re-fetched 2026-11-15; its scan predates the Shopify wave)
- https://apievangelist.com/2026/10/19/the-first-poppy-files-and-the-one-a-vendor-wrote/ - five valid poppy.json files across 24,577 API providers, none from launch partners, and the vendor-hosted file the 0.2 redirect rule closed (fetched 2026-11-07, re-fetched 2026-11-15)
- https://hn.algolia.com/api/v1/search?query=%22Personal%20Agent%20Protocol%22&tags=story - the footprint scan: a 9-point launch thread (2026-10-06), a 4-point follow-up (2026-10-22), a 2-point explainer (2026-10-07), and a 1-point map post (2026-10-26) (re-fetched 2026-11-15)
- https://poppy.md/press.html - the independent coverage inventory: Meta's Q3-earnings naming, the Meta-versus-Sierra partner-list difference, the community scan links, and the November 13-to-14 1.0 coverage round including Wix's default-availability claim and Clerk's Poppy browser sessions general availability (re-fetched 2026-11-15)
- https://allbirds.com/.well-known/poppy.json - an independent Shopify storefront's served discovery file, protocol_version 0.4 with UCP checkout scopes, confirming the auto-publish mechanism this run (fetched 2026-11-15)
