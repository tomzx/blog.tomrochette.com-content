---

title: "Code Factories: Or How I Learned to Stop Worrying and Build the Belt"
created: 2026-05-03
type: post
status: finished
tags: [software-engineering, factorio, metaphors, ai, software-factory, fully-ai-generated, llm=glm-5.1, llm=glm-5.3]
readability: 3
audience_notes: >
  Assumes the reader is a software engineer familiar with CI/CD, build pipelines, and
  running services in production; no Factorio experience is required, as each game
  mechanic is explained before it is compared.
agent_sessions:
  - ses_211cfc402ffeWDoF7RVgiLScCy
  - ses_20f8526bbffeRhAuYRUB1acWRC
  - ses_20f2a36d4ffeE84CIt4WLZhNO2
  - ses_0c555d9bfffeUL6dpThyPWb5n0
---

I land on an alien planet with nothing but a pickaxe and a furnace.

That's [Factorio](https://factorio.com/).
It's also my first day as a software developer.

In Factorio, I crash-land and must build a rocket to escape.
I start by hand-mining iron ore, smelting it in a stone furnace, and crafting simple items.
Within hours, I've built conveyor belts that carry ore automatically, assemblers that craft without me, and trains that shuttle materials across the map.
The factory grows.
I go from doing everything myself to watching machines do everything for me.

**Software development is following the same trajectory.**
The question is whether I'm still hand-mining iron ore.

## The Belt: The CI/CD Pipeline

In Factorio, the conveyor belt is the first automation I build.
Instead of walking back and forth carrying ore, I lay down a belt and let it move resources while I do something else.

**The CI/CD pipeline is the belt.**
Every time I push code, tests run, builds compile, deployments ship.
I don't walk the ore to the furnace anymore.
The belt carries it.

Teams without CI/CD are the players who never unlock belts.
They're still carrying ore by hand, one commit at a time, manually deploying to servers, manually running tests.
It works when the team is small.
It doesn't scale.

## Assemblers: The Build System

After belts come assembling machines.
I feed them ingredients and they output a product.
I don't craft gears by hand anymore (the assembler does it, faster and without mistakes).

**Compilers, bundlers, transpilers: these are the assemblers.**
I feed them source code and they output runnable software.
I used to manage dependencies by hand, include scripts individually, and pray the versions matched.
Now the assembler handles it.

The parallel goes deeper.
In Factorio, I quickly learn that one assembler isn't enough.
I need a chain: iron ore becomes iron plates, iron plates become gears, gears become transport belts.
Each step is its own assembler, fed by belts from the previous one.

The build pipeline works the same way.
Source code becomes transpiled code, transpiled code becomes bundled assets, bundled assets become container images, container images become deployed services.
Each stage is an assembler in a chain.
If one assembler is slow, the whole chain backs up.
If one assembler breaks, nothing after it gets built.

## Inserters: The Integration Points

Inserters are the quiet heroes of Factorio.
They take items from belts and put them into assemblers, furnaces, and chests.
They're the glue between every machine.

**Integration points in software are the inserters.**
APIs, webhooks, message queues, event streams: they move data between services.
Nobody talks about them at conferences.
But when an inserter stops working in Factorio, the assembler starves.
When an integration point breaks in production, the service starves.

Most production outages aren't caused by a broken assembler.
They're caused by a broken inserter, a misconfigured webhook, a timed-out API call, a corrupted message in a queue.
The machines were fine.
The connection between them failed.

## The Main Bus: The Monorepo

As my Factorio factory grows, I face a critical design decision: how to organize my belts.
Most experienced players converge on the same solution, the main bus.

A main bus is a wide highway of parallel belts carrying every resource I need, running in a straight line across my factory.
I branch off production lines from the bus, pull what I need, and return byproducts.
It's not the most space-efficient design.
It's not the fastest.
But it's the most understandable, and in a game where my own factory can become incomprehensible, understandability is survival.

**A monorepo is the main bus.**
All the code, all the services, all the shared libraries in one place, organized in a predictable structure.
Teams branch off to build their services, pull shared dependencies from the bus, and contribute back.
Like Factorio, the monorepo isn't optimal in every dimension.
But when a new developer joins and needs to understand how everything connects, they follow the bus.
No archaeology required.

Teams that reject the main bus in Factorio end up with spaghetti, belts crisscrossing everywhere, impossible to trace, impossible to modify without breaking something.
Teams that reject the monorepo end up the same way: dozens of microservices with undocumented dependencies, where nobody knows which service calls which, and changing one API breaks three things nobody knew existed.

## Logistics Bots: The AI Agents

At some point in Factorio, I unlock logistic robots.
Flying drones that carry items anywhere in my network.
They don't need belts.
They don't follow paths.
I request an item, and a bot brings it.

AI coding agents are the logistics bots.
I ask for a function, and the agent writes it.
I ask for tests, and the agent generates them.
I ask for a bug investigation, and the agent traces the stack.
They don't need me to lay down a belt first.
They go directly to the source and bring back what I need.

**But here's what Factorio teaches about bots: they don't replace belts.**
Players who try to run everything on bots discover that bots have a capacity limit.
When the network gets busy, bots queue up, delivery times spike, and the factory starves.
The best factories use bots for the weird, one-off requests and keep belts for the high-throughput, predictable flows.

The best engineering teams do the same.
AI agents handle the ad-hoc tasks, the one-off scripts, the bug investigations, the documentation updates.
But the core pipeline (the build system, the CI/CD, the deployment process) runs on belts.
Predictable.
Reliable.
Fast.

## The Ratios: The System Architecture

In Factorio, every recipe has precise ratios.
To produce one science pack per second, I need exactly 1.25 assemblers making gears and 0.8 assemblers making copper cable.
The math is deterministic.
If I get the ratios wrong, I get bottlenecks.
One belt backs up while another starves.
Resources pile up where they're not needed and run dry where they are.

**System architecture has the same dynamics, just less precise.**
Every service has throughput limits.
Every database has connection pool limits.
Every queue has a maximum depth.
If the authentication service can handle 100 requests per second but the API gateway is sending 200, there's a bottleneck.
The requests pile up.
Timeouts cascade.
Users see errors.

Factorio players solve ratio problems with calculators and spreadsheets.
They plan their factory before they build it.
Software engineers solve the same problems with load testing and capacity planning, or they should.
Too many teams build first and measure later, then wonder why production is slow.

## Biters: The Production Incidents

The alien natives in Factorio are called biters.
They attack the factory in increasing waves, drawn by the pollution the machines produce.
The more I build, the more they attack.
I can ignore them for a while, but eventually they'll overwhelm my defenses.

**Production incidents are the biters.**
They come in waves, drawn by the complexity of the system.
The more services I deploy, the more dependencies I add, the more incidents I attract.
I can ignore them for a while, patch the symptom, restart the service, move on.
But eventually they'll overwhelm me.

In Factorio, the solution isn't to stop building.
It's to build defenses: walls, turrets, artillery.
In software, the solution isn't to stop deploying.
It's to build defenses: monitoring, alerting, automatic rollback, chaos engineering.

The best Factorio players don't just react to biter attacks.
They proactively clear nests before they evolve.
The best engineering teams don't just react to incidents.
They proactively eliminate failure modes before they cause outages.

## Throughput vs Latency: The Eternal Trade-off

Factorio players eventually discover that throughput and latency are different things.
A belt with 100 items per minute has high throughput but items take time to travel from one end to the other.
A bot delivery is low throughput (one item at a time) but low latency (it goes straight there).

**Microservices vs monoliths is the same trade-off.**
A monolith has high throughput; everything runs in the same process, no network calls.
But change latency is high; I deploy the whole thing even if I changed one function.
Microservices have low change latency; I deploy one service independently.
But throughput suffers from network overhead, serialization, and distributed coordination.

Factorio doesn't judge me for choosing bots over belts or belts over bots.
It just shows me the consequences.
Software architecture should work the same way.
I choose my trade-offs, but I stay realistic about what I'm trading.

## The Rocket: Shipping

The goal of Factorio is to launch a rocket.
Everything I build (every belt, every assembler, every defense) exists to launch that rocket.
The goal is easy to forget.
Players spend hundreds of hours optimizing a single belt intersection, perfecting a circuit network, or making their factory look pretty.
Meanwhile, the rocket sits unbuilt.

Software teams do the same thing.
They refactor code that works fine.
They migrate to the latest framework.
They rebuild systems that don't need rebuilding.
Meanwhile, the product sits unshipped.
The users sit unserved.
The business sits unimproved.

Factorio teaches a simple lesson: the factory exists to launch the rocket, not the other way around.
**The code exists to ship the product.**
Every optimization that doesn't serve the product is a belt to nowhere.

## The Map: The Unknown Unknowns

When I start Factorio, the map is covered in fog.
I don't know where the iron is, where the oil is, or where the biters are nesting.
I explore by walking into the fog, revealing terrain piece by piece.
Sometimes I find a massive ore patch right next to my base.
Sometimes I walk into a biter nest and die.

Software development is exploring a fog of war.
I don't know what the users want until I ship.
I don't know what the legacy system does until I try to change it.
I don't know what the dependency actually does until it breaks in production.

The Factorio solution to the fog of war is radar.
I build radar stations that slowly reveal the map around them.
Not all at once, but gradually, giving me visibility without requiring me to walk everywhere.

**Observability is the radar.**
Logging, metrics, tracing, dashboards: they don't eliminate the unknown, but they reveal it gradually.
I can't see everything.
But I can see enough to make good decisions.

## Pollution: Technical Debt

Every machine in Factorio produces pollution.
Pollution spreads across the map and triggers biter attacks.
More machines, more pollution, more attacks.
Pollution is the cost of growth.

**Technical debt is pollution.**
Every shortcut, every hack, every "we'll fix it later" generates debt.
Debt spreads through the codebase, making changes harder, triggering bugs, slowing development.
More code, more debt, more incidents.

I can't eliminate pollution in Factorio without eliminating production.
I can't eliminate technical debt without eliminating software.
The key is management: build efficiently, clean up regularly, and invest in infrastructure that reduces the debt per feature shipped.
Electric furnaces produce less pollution than steel furnaces.
Good abstractions produce less technical debt than bad ones.

## The Late Game: Software Factories

In the late game of Factorio, something interesting happens.
I stop building things myself entirely.
Instead, I design blueprints, templates for entire sections of factory.
I place a blueprint and construction bots build the whole thing automatically.
I'm no longer an assembler.
I'm an architect.

**Software factories are the late game of software development.**
I don't write code.
I write specifications.
I don't review code.
I design verification systems.
I don't debug.
I design healing systems.

Like Factorio's late game, the software factory requires an enormous upfront investment.
I need to have built the belts, the assemblers, the bots, the logistics network before I can stamp down blueprints.
Software factories require CI/CD, testing infrastructure, monitoring, and AI agents before they can operate autonomously.

Players who try to skip to blueprints in Factorio without building the infrastructure first find that their construction bots can't reach the build site, don't have materials, or build the wrong thing.
Teams that try to skip to software factories without the infrastructure find that their AI agents produce broken code, can't deploy, and create more problems than they solve.

## The Spidertron: Autonomous Agents

The Spidertron is Factorio's ultimate vehicle.
A walking base that I can remote-control, equip with rockets, and send into dangerous territory.
It's the end result of everything I've built: it uses the tech I researched, the weapons I crafted, the logistics network I established.

**Autonomous AI coding agents are the Spidertron of software development.**
They roam the codebase, make changes, run tests, deploy code, all while I watch from the map.
But like the Spidertron, they're only as good as the infrastructure behind them.
A Spidertron without researched weapons is a walking target.
An AI agent without a testing infrastructure is a liability.

## The Lesson

Factorio is a game about building something that builds itself.
I start by doing everything manually.
I end by watching machines do everything for me.
The satisfaction isn't in the automation itself: it's in designing a system that works, that's elegant, that grows.

Software development is the same game.
I start by writing code manually.
I end by designing systems that write, test, and deploy code without me.
**The satisfaction isn't in the code: it's in the factory.**

If I'm still hand-crafting every iron gear, it's time to build my first assembler.
If I'm still carrying ore by hand, it's time to lay down a belt.
If I'm still reviewing every line of code myself, it's time to build a verification system.

The factory must grow.

## See also

- [Code Factories: The StarCraft Perspective](../code-factories-starcraft/index.md) - the same concept explored through StarCraft metaphors
- [Code Factories: The World of Warcraft Perspective](../code-factories-wow/index.md) - the same concept explored through World of Warcraft metaphors
- [Code Factories: The Stock Market Perspective](../code-factories-stock-market/index.md) - the same concept explored through stock market metaphors
- [Code Factories: The RollerCoaster Tycoon Perspective](../code-factories-rollercoaster-tycoon/index.md) - the same concept explored through RollerCoaster Tycoon metaphors

