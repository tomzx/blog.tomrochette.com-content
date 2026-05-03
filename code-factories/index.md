---
title: "Code Factories: Or How I Learned to Stop Worrying and Build the Belt"
created: 2026-05-03
type: post
status: finished
tags: [software-engineering, factorio, metaphors, ai, software-factory, fully-ai-generated, llm=glm-5.1]
readability: 3
---

You land on an alien planet with nothing but a pickaxe and a furnace.

That's Factorio.
It's also your first day as a software developer.

In Factorio, you crash-land and must build a rocket to escape.
You start by hand-mining iron ore, smelting it in a stone furnace, and crafting simple items.
Within hours, you've built conveyor belts that carry ore automatically, assemblers that craft without you, and trains that shuttle materials across the map.
The factory grows.
You go from doing everything yourself to watching machines do everything for you.

Software development is following the same trajectory.
The question is whether you're still hand-mining iron ore.

## The Belt: Your CI/CD Pipeline

In Factorio, the conveyor belt is the first automation you build.
Instead of walking back and forth carrying ore, you lay down a belt and let it move resources while you do something else.

Your CI/CD pipeline is the belt.
Every time you push code, tests run, builds compile, deployments ship.
You don't walk the ore to the furnace anymore.
The belt carries it.

Teams without CI/CD are the players who never unlock belts.
They're still carrying ore by hand, one commit at a time, manually deploying to servers, manually running tests.
It works when you're small.
It doesn't scale.

## Assemblers: Your Build System

After belts come assembling machines.
You feed them ingredients and they output a product.
You don't craft gears by hand anymore — the assembler does it, faster and without mistakes.

Compilers, bundlers, transpilers — these are your assemblers.
You feed them source code and they output runnable software.
You used to manage dependencies by hand, include scripts individually, and pray the versions matched.
Now the assembler handles it.

The parallel goes deeper.
In Factorio, you quickly learn that one assembler isn't enough.
You need a chain: iron ore becomes iron plates, iron plates become gears, gears become transport belts.
Each step is its own assembler, fed by belts from the previous one.

Your build pipeline works the same way.
Source code becomes transpiled code, transpiled code becomes bundled assets, bundled assets become container images, container images become deployed services.
Each stage is an assembler in a chain.
If one assembler is slow, the whole chain backs up.
If one assembler breaks, nothing after it gets built.

## Inserters: Your Integration Points

Inserters are the quiet heroes of Factorio.
They take items from belts and put them into assemblers, furnaces, and chests.
They're the glue between every machine.

Integration points in software are your inserters.
APIs, webhooks, message queues, event streams — they move data between services.
Nobody talks about them at conferences.
But when an inserter stops working in Factorio, the assembler starves.
When an integration point breaks in production, the service starves.

Most production outages aren't caused by a broken assembler.
They're caused by a broken inserter — a misconfigured webhook, a timed-out API call, a corrupted message in a queue.
The machines were fine.
The connection between them failed.

## The Main Bus: Your Monorepo

As your Factorio factory grows, you face a critical design decision: how to organize your belts.
Most experienced players converge on the same solution — the main bus.

A main bus is a wide highway of parallel belts carrying every resource you need, running in a straight line across your factory.
You branch off production lines from the bus, pull what you need, and return byproducts.
It's not the most space-efficient design.
It's not the fastest.
But it's the most understandable, and in a game where your own factory can become incomprehensible, understandability is survival.

A monorepo is your main bus.
All your code, all your services, all your shared libraries in one place, organized in a predictable structure.
Teams branch off to build their services, pull shared dependencies from the bus, and contribute back.
Like Factorio, the monorepo isn't optimal in every dimension.
But when a new developer joins and needs to understand how everything connects, they follow the bus.
No archaeology required.

Teams that reject the main bus in Factorio end up with spaghetti — belts crisscrossing everywhere, impossible to trace, impossible to modify without breaking something.
Teams that reject the monorepo end up the same way: dozens of microservices with undocumented dependencies, where nobody knows which service calls which, and changing one API breaks three things nobody knew existed.

## Logistics Bots: Your AI Agents

At some point in Factorio, you unlock logistic robots.
Flying drones that carry items anywhere in your network.
They don't need belts.
They don't follow paths.
You request an item, and a bot brings it.

AI coding agents are your logistics bots.
Need a function written? The agent writes it.
Need tests generated? The agent generates them.
Need a bug investigated? The agent traces the stack.
They don't need you to lay down a belt first.
They go directly to the source and bring back what you need.

But here's what Factorio teaches about bots: they don't replace belts.
Players who try to run everything on bots discover that bots have a capacity limit.
When the network gets busy, bots queue up, delivery times spike, and your factory starves.
The best factories use bots for the weird, one-off requests and keep belts for the high-throughput, predictable flows.

The best engineering teams do the same.
AI agents handle the ad-hoc tasks — the one-off scripts, the bug investigations, the documentation updates.
But the core pipeline — the build system, the CI/CD, the deployment process — runs on belts.
Predictable. Reliable. Fast.

## The Ratios: Your System Architecture

In Factorio, every recipe has precise ratios.
To produce one science pack per second, you need exactly 1.25 assemblers making gears and 0.8 assemblers making copper cable.
The math is deterministic.
If you get the ratios wrong, you get bottlenecks.
One belt backs up while another starves.
Resources pile up where they're not needed and run dry where they are.

System architecture has the same dynamics, just less precise.
Every service has throughput limits.
Every database has connection pool limits.
Every queue has a maximum depth.
If your authentication service can handle 100 requests per second but your API gateway is sending 200, you have a bottleneck.
The requests pile up.
Timeouts cascade.
Users see errors.

Factorio players solve ratio problems with calculators and spreadsheets.
They plan their factory before they build it.
Software engineers solve the same problems with load testing and capacity planning — or they should.
Too many teams build first and measure later, then wonder why production is slow.

## Biters: Your Production Incidents

The alien natives in Factorio are called biters.
They attack your factory in increasing waves, drawn by the pollution your machines produce.
The more you build, the more they attack.
You can ignore them for a while, but eventually they'll overwhelm your defenses.

Production incidents are your biters.
They come in waves, drawn by the complexity of your system.
The more services you deploy, the more dependencies you add, the more incidents you attract.
You can ignore them for a while — patch the symptom, restart the service, move on.
But eventually they'll overwhelm you.

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

Microservices vs monoliths is the same trade-off.
A monolith has high throughput — everything runs in the same process, no network calls.
But change latency is high — you deploy the whole thing even if you changed one function.
Microservices have low change latency — deploy one service independently.
But throughput suffers from network overhead, serialization, and distributed coordination.

Factorio doesn't judge you for choosing bots over belts or belts over bots.
It just shows you the consequences.
Software architecture should work the same way.
Choose your trade-offs, but be honest about what you're trading.

## The Rocket: Shipping

The goal of Factorio is to launch a rocket.
Everything you build — every belt, every assembler, every defense — exists to launch that rocket.
It's easy to forget this.
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
The code exists to ship the product.
Every optimization that doesn't serve the product is a belt to nowhere.

## The Map: Your Unknown Unknowns

When you start Factorio, the map is covered in fog.
You don't know where the iron is, where the oil is, or where the biters are nesting.
You explore by walking into the fog, revealing terrain piece by piece.
Sometimes you find a massive ore patch right next to your base.
Sometimes you walk into a biter nest and die.

Software development is exploring a fog of war.
You don't know what the users want until you ship.
You don't know what the legacy system does until you try to change it.
You don't know what the dependency actually does until it breaks in production.

The Factorio solution to the fog of war is radar.
You build radar stations that slowly reveal the map around them.
Not all at once, but gradually, giving you visibility without requiring you to walk everywhere.

Observability is your radar.
Logging, metrics, tracing, dashboards — they don't eliminate the unknown, but they reveal it gradually.
You can't see everything.
But you can see enough to make good decisions.

## Pollution: Technical Debt

Every machine in Factorio produces pollution.
Pollution spreads across the map and triggers biter attacks.
More machines, more pollution, more attacks.
Pollution is the cost of growth.

Technical debt is pollution.
Every shortcut, every hack, every "we'll fix it later" generates debt.
Debt spreads through the codebase, making changes harder, triggering bugs, slowing development.
More code, more debt, more incidents.

You can't eliminate pollution in Factorio without eliminating production.
You can't eliminate technical debt without eliminating software.
The key is management: build efficiently, clean up regularly, and invest in infrastructure that reduces the debt per feature shipped.
Electric furnaces produce less pollution than steel furnaces.
Good abstractions produce less technical debt than bad ones.

## The Late Game: Software Factories

In the late game of Factorio, something interesting happens.
You stop building things yourself entirely.
Instead, you design blueprints — templates for entire sections of factory.
You place a blueprint and construction bots build the whole thing automatically.
You're no longer an assembler.
You're an architect.

Software factories are the late game of software development.
You don't write code.
You write specifications.
You don't review code.
You design verification systems.
You don't debug.
You design healing systems.

Like Factorio's late game, this requires an enormous upfront investment.
You need to have built the belts, the assemblers, the bots, the logistics network before you can stamp down blueprints.
Software factories require CI/CD, testing infrastructure, monitoring, and AI agents before they can operate autonomously.

Players who try to skip to blueprints in Factorio without building the infrastructure first find that their construction bots can't reach the build site, don't have materials, or build the wrong thing.
Teams that try to skip to software factories without the infrastructure find that their AI agents produce broken code, can't deploy, and create more problems than they solve.

## The Spidertron: Autonomous Agents

The Spidertron is Factorio's ultimate vehicle.
A walking base that you can remote-control, equip with rockets, and send into dangerous territory.
It's the culmination of everything you've built — it uses the tech you researched, the weapons you crafted, the logistics network you established.

Autonomous AI coding agents are the Spidertron of software development.
They roam your codebase, make changes, run tests, deploy code — all while you watch from the map.
But like the Spidertron, they're only as good as the infrastructure behind them.
A Spidertron without researched weapons is a walking target.
An AI agent without a testing infrastructure is a liability.

## The Lesson

Factorio is a game about building something that builds itself.
You start by doing everything manually.
You end by watching machines do everything for you.
The satisfaction isn't in the automation itself — it's in designing a system that works, that's elegant, that grows.

Software development is the same game.
We start by writing code manually.
We end by designing systems that write, test, and deploy code without us.
The satisfaction isn't in the code — it's in the factory.

If you're still hand-crafting every iron gear, it's time to build your first assembler.
If you're still carrying ore by hand, it's time to lay down a belt.
If you're still reviewing every line of code yourself, it's time to build a verification system.

The factory must grow.

## See also

- [Code Factories: The StarCraft Perspective](/code-factories-starcraft) — the same concept explored through StarCraft metaphors
