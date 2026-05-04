---
title: "Code Factories: The RollerCoaster Tycoon Perspective"
created: 2026-05-04
type: post
status: finished
tags: [software-engineering, rollercoaster-tycoon, metaphors, ai, software-factory, fully-ai-generated, llm=glm-5.1]
readability: 3
---

You start with an empty plot of land, a small bank loan, and an objective to attract 600 guests by the end of year two.

That's RollerCoaster Tycoon.
It's also your first day as a startup founder.

In RollerCoaster Tycoon, you build a theme park from nothing.
You lay down paths, construct rides, hire staff, set prices, manage finances, and try to keep thousands of guests happy simultaneously.
You watch little pixelated people queue for attractions, complain about litter, get sick on rides, and leave when they've had enough.

Building a software product is the same game with different sprites.
The question is whether your park guests are leaving happy or leaving forever.

## Ride Design: Feature Development

In RollerCoaster Tycoon, every ride is a design problem.

A roller coaster starts as blank track on a canvas.
You choose the lift hill height, the drop angle, the number of inversions, the banking on turns.
Each decision affects three metrics: excitement, intensity, and nausea.

Excitement is what attracts guests.
Intensity is the thrill level — some guests love it, some won't ride.
Nausea is the cost — too much and guests vomit on your paths.

Feature development has the same three metrics.

Excitement is user value — the feature that solves a real problem, delivers a delightful experience, or unlocks new capability.
Intensity is complexity — the learning curve, the configuration surface, the cognitive load on users.
Nausea is maintenance burden — the edge cases, the performance overhead, the support tickets.

A roller coaster with high excitement and moderate intensity is the ideal ride.
Guests line up for it, enjoy it, and ride again.
A feature with high value and manageable complexity is the ideal feature.
Users adopt it, benefit from it, and recommend it.

A roller coaster with maximum intensity and maximum nausea empties the queue.
Guests try it once, throw up, and never return.
A feature with maximum complexity and maximum maintenance burden empties the user base.
Users try it once, get confused, and never return.

The RollerCoaster Tycoon lesson: optimize for excitement, manage intensity, minimize nausea.
In software: optimize for value, manage complexity, minimize burden.

## Park Layout: Information Architecture

In RollerCoaster Tycoon, path layout determines everything.

Guests follow paths.
They can only reach rides that are connected to the path network.
If a ride is hidden behind another ride with no path leading to it, it might as well not exist.
If the path network is a tangled mess, guests get lost, frustrated, and leave.

Your information architecture is your path layout.

Users follow navigation.
They can only find features that are connected to the navigation flow.
If a feature is buried three menus deep with no link to it, it might as well not exist.
If the navigation is a tangled mess, users get lost, frustrated, and leave.

RollerCoaster Tycoon teaches a specific layout pattern: the hub-and-spoke.

A central plaza connects to several themed areas.
Each themed area contains related rides.
Signs guide guests from the hub to the areas they want.
The layout is intuitive, discoverable, and scalable — add a new spoke when you add a new area.

Good information architecture is hub-and-spoke.

A homepage or dashboard connects to major feature areas.
Each area contains related functionality.
Breadcrumbs and search guide users to what they need.
The layout is intuitive, discoverable, and scalable — add a new section when you add a new feature area.

Parks with random path layouts have low guest counts and low ratings.
Products with random navigation have low engagement and low retention.

## Guest Happiness: User Satisfaction

Every guest in RollerCoaster Tycoon has a happiness meter.

It starts high when they enter the park.
Every good ride increases it.
Every long queue decreases it.
Every piece of litter they see decreases it.
Every overpriced item decreases it.
When happiness drops below a threshold, the guest leaves and the park rating drops.

User satisfaction works the same way.

Every smooth interaction increases it.
Every loading spinner decreases it.
Every confusing error message decreases it.
Every unexpected price increase decreases it.
When satisfaction drops below a threshold, the user churns and the review rating drops.

RollerCoaster Tycoon teaches that guest happiness is a composite of many small factors, not one big one.

No single ride makes guests happy.
It's the combination of good rides, short queues, clean paths, reasonable prices, attractive scenery, and available amenities.
Fix one problem while ignoring the others and happiness barely moves.

User satisfaction is equally composite.
No single feature makes users happy.
It's the combination of useful features, fast performance, clear error messages, fair pricing, good design, and responsive support.
Fix one problem while ignoring the others and satisfaction barely moves.

The park with the highest rating isn't the one with the best roller coaster.
It's the one where everything works well together.
The product with the highest satisfaction isn't the one with the best feature.
It's the one where everything works well together.

## Queue Management: Performance Optimization

In RollerCoaster Tycoon, queues are the visual indicator of a problem.

A long queue means guests are waiting.
Waiting guests are unhappy guests.
Unhappy guests leave bad reviews and reduce the park rating.

The solutions are straightforward: increase ride capacity, add more rides, or optimize throughput.
Run three trains instead of two.
Synchronize the dispatch timing.
Build a second coaster nearby to distribute the load.

Performance bottlenecks are queues.

A slow API response means requests are waiting.
Waiting requests are unhappy users.
Unhappy users abandon carts, close tabs, and leave bad reviews.

The solutions are equally straightforward: increase capacity, add more instances, or optimize throughput.
Scale horizontally with more servers.
Cache frequently requested data.
Build a read replica to distribute the load.

RollerCoaster Tycoon also teaches a subtler lesson about queues: the perception of waiting matters as much as the actual wait.

Rides with themed queue lines — tunnels with decorations, TV screens playing videos, interactive elements — have higher guest satisfaction than rides with bare concrete queues, even when the wait time is identical.

The software equivalent is perceived performance.

A page that loads a skeleton UI immediately and fills in content progressively feels faster than a page that shows nothing for two seconds and then renders everything at once.
The actual load time is the same.
The perceived load time is dramatically different.

Theme your queue lines.
Show progress indicators, skeleton screens, and optimistic updates.
The wait is the same.
The experience is better.

## Staff Management: Team Operations

Your park needs staff.

Handymen sweep litter and empty trash cans.
Mechanics inspect and repair broken rides.
Security guards catch vandals and keep the peace.
Entertainers make guests happy in queue lines.

Each staff member has a patrol zone.
Set the zone too large and they can't cover it all — litter accumulates in the corners.
Set the zone too small and they cluster in one area while the rest of the park deteriorates.
Hire too few and the park falls apart.
Hire too many and the payroll drains your budget.

Engineering teams have the same dynamics.

SREs are mechanics — they inspect, repair, and prevent production failures.
Support engineers are handymen — they clean up tickets, triage issues, and keep the user experience tidy.
Security engineers are security guards — they find vulnerabilities, respond to incidents, and keep the codebase safe.
Developer advocates are entertainers — they engage the community, write documentation, and make the developer experience enjoyable.

The patrol zone problem is the on-call rotation problem.

Give an on-call engineer too many services and they can't respond to incidents fast enough — errors accumulate.
Give them too few and they sit idle while other on-call engineers are overwhelmed.
Too few engineers on rotation and the team burns out.
Too many and context is spread thin.

RollerCoaster Tycoon also teaches that staff training matters.

A trained mechanic repairs rides faster.
A trained handyman cleans more efficiently.
In software, the equivalent is runbooks, incident playbooks, and onboarding documentation.
A trained on-call engineer resolves incidents faster because they've seen the failure modes before and know the recovery steps.

Invest in your staff or watch your park deteriorate.

## Ride Breakdowns: Production Incidents

Every ride in RollerCoaster Tycoon has a reliability rating.

New rides are highly reliable.
As they age, reliability drops.
The more a ride runs, the more likely it breaks down.
A broken ride closes.
Guests in the queue leave unhappy.
The mechanic has to walk across the park, inspect the ride, and repair it.

During the downtime, the queue grows, the guests complain, and the park rating drops.

Production incidents are ride breakdowns.

New services are highly reliable.
As they age, complexity accumulates.
The more a service runs, the more likely an edge case triggers a failure.
A failed service goes down.
Users in the middle of a workflow are interrupted.
The on-call engineer has to investigate, diagnose, and fix the issue.

During the downtime, error rates spike, users complain, and the product reputation drops.

RollerCoaster Tycoon's solution to breakdowns is preventive maintenance.

Mechanics can be assigned to inspect rides before they break.
Regular inspections increase reliability and reduce the frequency of breakdowns.
The cost is the mechanic's time — time spent inspecting is time not spent repairing.
But the net effect is positive: fewer breakdowns, shorter downtimes, happier guests.

The software equivalent is proactive reliability engineering.

Chaos engineering, load testing, dependency auditing, and synthetic monitoring are preventive inspections.
The cost is engineering time — time spent testing reliability is time not spent building features.
But the net effect is positive: fewer incidents, shorter outages, happier users.

Parks that skip inspections have spectacular breakdowns at the worst moments.
Services that skip reliability testing have spectacular outages during peak traffic.

## Research: Technical Exploration

RollerCoaster Tycoon has a research system.

You allocate funding to research and over time, new rides, scenery, and improvements become available.
More funding accelerates research.
Less funding slows it.
No funding means you're stuck with what you have.

The tension is real: every dollar spent on research is a dollar not spent on building rides right now.
But without research, you can't build the rides that attract guests later.

Technology exploration is research.

Every hour spent evaluating a new framework, prototyping a new architecture, or experimenting with a new tool is an hour not spent shipping features right now.
But without exploration, you can't build the features that attract users later.

RollerCoaster Tycoon teaches that research should be funded consistently, not in bursts.

A player who sets research to maximum at the start and then cuts it to zero runs out of new content mid-game.
A player who funds research at a moderate, steady rate unlocks new rides throughout the game.

The software equivalent: invest in exploration consistently, not just when the team is between projects.

A team that dedicates 10% of every sprint to technical exploration — trying new tools, reading papers, prototyping ideas — continuously discovers improvements.
A team that only explores during quarterly hackathons discovers nothing for three months at a time.

Consistent research wins.
Burst research wastes the intervals between bursts.

## Scenario Objectives: Sprint Goals and OKRs

Every RollerCoaster Tycoon scenario has an objective.

"Have 600 guests in your park by the end of year two."
"Achieve a park rating of 700 by October, year three."
"Build ten roller coasters with an excitement rating above 6.00."
"Repay your loan and achieve a monthly profit of $1,000."

The objectives are specific, measurable, and time-bound.
They force you to prioritize — you can't do everything, so you do what matters for the objective.

Sprint goals and OKRs are scenario objectives.

"Ship the new checkout flow by end of sprint."
"Reduce p95 latency below 200ms by end of quarter."
"Increase test coverage to 80% by end of year."
"Reduce onboarding time for new engineers by 50%."

RollerCoaster Tycoon teaches something critical about objectives: the scenario ends.

When you achieve the objective, the scenario is complete.
You can keep playing — most players do — but the pressure is off.
The objective gave the gameplay structure.
Without it, you'd build aimlessly and the park would suffer.

Sprint goals give development structure.
Without them, teams build aimlessly and the product suffers.

But RollerCoaster Tycoon also teaches that the wrong objective leads to the wrong park.

An objective that demands 1,000 guests by year one forces you to build cheap, low-quality rides to attract crowds fast.
The park fills up but the rating is terrible.
An objective that demands a park rating of 900 forces you to build slowly and carefully.
The rating is excellent but the guest count is low.

Software objectives have the same distortion effect.

An objective that measures lines of code produces lots of code.
An objective that measures features shipped produces lots of features.
Neither guarantees quality, user satisfaction, or business value.
The metric you optimize is the park you get.

Choose your scenario objective carefully.
It will shape everything you build.

## Loan Management: Technical Debt

Many RollerCoaster Tycoon scenarios start you in debt.

You've borrowed money to buy the land and build the first rides.
The loan accrues interest every month.
The longer you carry it, the more it costs.

You can invest in rides to generate revenue and pay it off slowly.
Or you can cut spending, build cheap rides, and pay it off quickly.
The first strategy grows the park but increases the total interest paid.
The second strategy limits growth but reduces the financial burden.

Technical debt is a loan.

You borrowed time by taking shortcuts — skipping tests, ignoring architecture, hardcoding values.
The debt accrues interest every sprint.
The longer you carry it, the more it costs in debugging, refactoring, and developer frustration.

You can invest in features to grow the product and pay down debt slowly.
Or you can pause features, refactor aggressively, and pay it down quickly.

RollerCoaster Tycoon teaches that the optimal strategy depends on the interest rate.

A low-interest loan is fine to carry — the revenue from new rides exceeds the interest cost.
A high-interest loan is an emergency — it consumes revenue faster than the park can generate it.

Low-interest technical debt — a slightly messy module that rarely changes — is fine to carry.
The velocity gained by shipping features exceeds the cost of the debt.
High-interest technical debt — a critical module that breaks every sprint — is an emergency.
It consumes velocity faster than the team can generate it.

Know your interest rate.
Manage accordingly.

## Park Value: Technical Assets

RollerCoaster Tycoon tracks your park value — the combined worth of all your rides, scenery, and infrastructure.

It's not the same as cash in the bank.
You can have high park value and no cash if you spent everything on construction.
You can have high cash and low park value if you haven't built anything.

Park value represents what you've built, not what you have.
It compounds — every ride you build increases the value, and the more valuable the park, the more guests it attracts, which generates more revenue for building more rides.

Technical assets are park value.

Your component library, your CI/CD pipeline, your monitoring infrastructure, your documentation, your test suite — these are rides you've built.
They represent what you've constructed, not what you have in the backlog.

A team with high technical assets and an empty backlog is in good shape — they can build anything quickly.
A team with low technical assets and a full backlog is in trouble — everything they try to build requires starting from scratch.

Park value compounds the same way.
A park with ten rides attracts more guests than one with two, generating more revenue to build more rides.
A codebase with ten reusable components ships faster than one with two, generating more time to build more components.

The RollerCoaster Tycoon lesson: invest in park value, not just cash flow.
Build rides that attract guests.
Build infrastructure that attracts velocity.

## Scenery and Theming: Design and UX

In RollerCoaster Tycoon, scenery affects guest happiness.

Trees, fountains, gardens, statues, themed decorations — guests notice them.
A ride surrounded by matching scenery gets an excitement bonus.
A path lined with trees and benches keeps guests happy while they walk.
A park with no scenery is functional but joyless.

Design and UX are scenery.

A functional interface without thoughtful design is a park without trees.
Users can complete their tasks but they don't enjoy them.
There's no delight, no personality, no sense that someone cared about the experience.

RollerCoaster Tycoon teaches that scenery is most effective when it's themed.

A pirate-themed roller coaster surrounded by pirate scenery — ships, treasure chests, palm trees — gets a higher excitement bonus than the same ride surrounded by random, unrelated decorations.
Consistency matters more than quantity.

Design systems are theming.

A consistent design system — typography, colors, spacing, components — creates a cohesive experience.
Users don't have to relearn the interface on every page.
The product feels intentional, polished, professional.

A product with random design choices — different button styles, inconsistent spacing, clashing colors — is a park with random scenery.
Each element might look fine on its own.
Together, they're incoherent.

Theme your park.
Theme your product.

## Marketing: Developer Relations and Product Marketing

RollerCoaster Tycoon lets you run marketing campaigns.

Advertising for the park increases guest count.
You can target local, national, or international audiences at increasing cost.
More marketing brings more guests, but if the park isn't ready for them, they arrive to long queues, dirty paths, and broken rides.
They leave unhappy and the marketing was wasted.

Product marketing and developer relations work the same way.

A successful marketing campaign brings users.
But if the product isn't ready — if the onboarding is rough, the documentation is thin, the performance is slow — users arrive to a bad experience.
They leave unhappy and the marketing was wasted.

RollerCoaster Tycoon teaches the sequence: build the park first, then market it.

Players who spend their initial budget on marketing instead of rides attract guests to an empty park.
The guests find nothing to do and leave.
The money is gone and the park rating is worse than if they'd never marketed at all.

Startups learn this the hard way.
Marketing before product-market fit brings users to a product that doesn't serve them.
The users leave, the analytics look terrible, and the brand is damaged.

Build the ride first.
Then put up the billboard.

## Terrain Constraints: Legacy Systems

Some RollerCoaster Tycoon scenarios give you a blank, flat parcel of land.
These are the easy scenarios.
You build what you want, where you want, with no constraints.

Most scenarios aren't like that.

You get a mountainous plot with a river running through it.
Or a partially built park with existing paths and rides you can't remove.
Or an underground cavern with limited space.
The terrain constrains every decision.
You can't build a flat coaster on a mountain.
You can't extend a path across a river without a bridge.
You have to work with what you've got.

Legacy codebases are constrained terrain.

The ideal software project starts from nothing — blank repository, no dependencies, no constraints.
Most projects aren't like that.

You inherit a codebase with a decade of decisions baked in.
A database schema that can't be changed without migrating millions of rows.
An API contract that external clients depend on.
A build system that nobody fully understands.
The legacy constrains every decision.

RollerCoaster Tycoon teaches that constrained terrain isn't a disadvantage — it's a design prompt.

The best coasters in the game are built on mountains, using the elevation changes to create drops and turns that flat terrain can't support.
The constraint forces creativity.
The result is better than what flat terrain would have produced.

The best software architectures emerge from constrained codebases.
The legacy forces you to think carefully about abstractions, boundaries, and migration paths.
The result is often more robust than a greenfield design that never faced real constraints.

Don't wish for flat terrain.
Build better coasters on the mountain.

## Ride Synchronization: Service Coordination

In RollerCoaster Tycoon, you can build ride sequences.

A log flume that ends near a roller coaster entrance.
A transport ride that shuttles guests from the back of the park to the front.
A path that naturally guides guests through a series of attractions in order.

When rides are well-connected, guests flow through the park naturally, experiencing each attraction in sequence.
When rides are disconnected, guests wander, backtrack, and miss attractions they would have enjoyed.

Microservice coordination is ride synchronization.

A well-orchestrated service mesh lets data flow through the system naturally, each service processing requests in sequence.
A poorly connected architecture forces data to backtrack, retry, and miss services that should have been involved.

RollerCoaster Tycoon also teaches that you can't force guests through a sequence.

You can build a path that leads from Ride A to Ride B, but if the guest is tired, hungry, or has already ridden Ride A, they'll skip Ride B and look for food instead.
The sequence must be optional, not mandatory.

Service orchestration must be the same.
Each service should work independently.
Coordination is an optimization, not a requirement.
If Service A is down, Service B should still function, even if degraded.

Guests who are forced through a sequence they don't want rebel.
Services that are forced into tight coupling fail together.

Build the path.
Let the guest choose.

## The Late Game: Software Factories

In RollerCoaster Tycoon's late game, something shifts.

Your park is established.
Rides are built, staff is hired, research is funded, guests are flowing.
You stop placing individual track pieces and start thinking about the park as a system.

You notice that the path near the pirate coaster always gets congested, so you widen it.
You notice that guests cluster near the food court at noon, so you add another food stall.
You notice that the park rating dips every time it rains, so you build more indoor attractions.

You're no longer building rides.
You're optimizing a system.

Software factories are the late game of development.

Your CI/CD pipeline is established.
Your monitoring is running.
Your team is staffed, your architecture is sound, your users are flowing.
You stop writing individual functions and start thinking about the development process as a system.

You notice that deploys always cause a spike in errors, so you add automated smoke tests.
You notice that code review is the bottleneck, so you add AI-assisted review tooling.
You notice that onboarding takes too long, so you build interactive tutorials.

You're no longer writing code.
You're optimizing a system that writes code.

In RollerCoaster Tycoon, the late game players build mega-parks — sprawling empires with dozens of rides, thousands of guests, and perfect ratings.
They didn't get there by building one perfect ride.
They got there by building a system where every ride supports every other ride.

In software, the late game teams build software factories — sprawling systems where AI agents write code, tests run automatically, deployments ship continuously, and incidents heal themselves.
They didn't get there by writing one perfect feature.
They got there by building a system where every tool supports every other tool.

The park guest who walks into a mega-park sees rides.
The developer who walks into a software factory sees features.
Neither sees the decades of system optimization that made it all possible.

## The Lesson

RollerCoaster Tycoon is a game about building something that delights people.

You start with empty land and an objective.
You end with a park that thousands of guests enjoy.
The satisfaction isn't in any single ride — it's in the system that makes every ride better.

Software development is the same game.

You start with an empty repository and a requirement.
You end with a product that thousands of users rely on.
The satisfaction isn't in any single feature — it's in the system that makes every feature better.

In RollerCoaster Tycoon, the parks that endure aren't the ones with the tallest coaster or the most rides.
They're the ones where everything works together — the paths flow, the queues are short, the staff is attentive, the scenery is beautiful, and every guest leaves happy.

In software, the products that endure aren't the ones with the most features or the latest technology.
They're the ones where everything works together — the architecture is clean, the performance is fast, the support is responsive, the design is consistent, and every user leaves satisfied.

If you're still building rides one track piece at a time, it's time to think about the park.
If you're still writing features one line at a time, it's time to think about the factory.

The park is open.

## See also

- [Code Factories: The Factorio Perspective](/code-factories-factorio) — the same concept explored through Factorio metaphors
- [Code Factories: The StarCraft Perspective](/code-factories-starcraft) — the same concept explored through StarCraft metaphors
- [Code Factories: The World of Warcraft Perspective](/code-factories-wow) — the same concept explored through World of Warcraft metaphors
- [Code Factories: The Stock Market Perspective](/code-factories-stock-market) — the same concept explored through stock market metaphors
