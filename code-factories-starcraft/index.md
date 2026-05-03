---
title: "Code Factories: The StarCraft Perspective"
created: 2026-05-03
type: post
status: finished
tags: [software-engineering, starcraft, metaphors, ai, software-factory, fully-ai-generated, llm=glm-5.1]
readability: 3
---

You start with four workers, a command center, and fog of war in every direction.

That's StarCraft.
It's also your first day at a startup.

In StarCraft, you command one of three races — Terran, Protoss, or Zerg — each with radically different economies, armies, and strategies.
You gather minerals and vespene gas, build structures, research upgrades, and produce units.
You scout the opponent, react to their strategy, and try to win through superior economy, tactics, or both.
The clock never stops.
The other player never waits.

Building a software organization is the same game with different units.
The question is which race you're playing and whether you know it.

## APM: Developer Productivity

In StarCraft, APM — actions per minute — is the raw measure of how fast a player can issue commands.
Pros sustain 300+ APM over games that last 20 to 40 minutes.
Beginners hover around 30.

But high APM doesn't win games.
Efficient APM does.
A pro spends most of those actions on macro — building workers, expanding, producing units — and only the necessary actions on micro — controlling individual units in combat.
A beginner wastes APM clicking the same unit six times or panicking during a fight.

Lines of code per day is the APM of software development.
It measures activity, not impact.
A developer who writes 500 lines in a day isn't necessarily more productive than one who writes 50.
The 50-line developer might have deleted 200 lines, simplified an abstraction, or prevented a week of debugging.

The StarCraft lesson: optimize for effective actions, not total actions.
In code, optimize for value shipped, not code written.

## Worker Production: Hiring

In StarCraft, the single most important thing a new player can learn is to never stop making workers.
Workers gather resources.
Resources fund everything else — units, buildings, upgrades.
A player who stops producing workers at the five-minute mark will be economically crushed by one who didn't, regardless of army composition or tactical skill.

Hiring is your worker production.
Every engineer you add increases your resource gathering rate — the rate at which your team can design, build, and ship software.
A team that stops hiring after its founding engineers will be outpaced by a team that kept recruiting, even if the founding team was brilliant.

But StarCraft also teaches that worker production has a ceiling.
You can only send so many workers to a mineral patch before they queue up and waste time.
In software, the ceiling is communication overhead.
Add too many engineers to a project and they spend more time coordinating than building.
Brooks said it decades ago: adding people to a late project makes it later.
StarCraft players learn it every game: there's an optimal number of workers per base, and exceeding it wastes resources.

## Expanding: New Teams and Services

In StarCraft, one base isn't enough.
The mineral patches deplete.
Gas geysers run dry.
To keep growing, you must expand — build a new command center, nexus, or hatchery at a new resource location.

Each expansion is a bet.
It costs resources to build.
It takes time to become profitable.
And it's vulnerable — spread across the map, harder to defend, exposed to attack.

Starting a new team or service is expanding.
You invest resources — hiring, onboarding, infrastructure — in exchange for future throughput.
The first team's codebase, like a mineral patch, eventually becomes congested.
Too many engineers working on the same service creates merge conflicts, deployment bottlenecks, and architectural compromises.
A new team with its own service spreads the load.

But like StarCraft expansions, new teams are vulnerable.
They don't yet know the codebase, the domain, or the culture.
They'll make mistakes the first team already learned from.
They'll build things that duplicate or conflict with existing systems.
And they require protection — mentoring, clear interfaces, architectural guidance — or they'll be overrun by the complexity the first team already tamed.

StarCraft players know: expand when your main base is saturated, not when you're under attack.
Software leaders should know: create new teams when the current team is at capacity, not when the project is already late.

## The Supply Cap: Organizational Scaling

In StarCraft, you can't just build an infinite army.
Every unit costs supply.
Terran supply depots, Protoss pylons, Zerg overlords — each race has its own mechanism for increasing the supply cap.
If you hit the cap, production halts.
Your factories, barracks, and starports sit idle until you build more supply.

Organizational scaling has supply caps too.
They just aren't as explicit.

The first cap is communication.
A team of 5 people has 10 communication channels.
A team of 15 has 105.
At some point, people spend more time talking than building, and adding another engineer actually decreases output.

The second cap is architecture.
A monolith can support a certain number of contributors before merge conflicts, test suite times, and deployment coordination become unbearable.
You need to split the monolith — build a pylon, if you will — to increase the cap.

The third cap is process.
A small team doesn't need sprint planning, architecture review boards, or release managers.
A large team does.
Each process is a supply depot — it costs resources to build but increases the number of people who can work together productively.

Teams that ignore the supply cap wonder why their army is small despite having plenty of factories.
The factories are there.
The supply isn't.

## Build Orders: Project Plans

Every StarCraft game begins with a build order — a planned sequence of actions for the first few minutes.
Build a supply depot at 10 supply.
A barracks at 12.
A refinery at 13.
Expand at the natural at 20.

Build orders aren't rigid scripts.
They're opening principles — a sequence that has been proven to lead to a strong mid-game position.
Players deviate when they scout something unexpected, but they always have a plan to return to.

Project plans are build orders.
You don't start building features randomly.
You have a sequence: set up the repository, configure CI/CD, build the core domain model, add the API layer, implement authentication, deploy to staging.
The order matters because each step depends on the previous one.

But just like in StarCraft, the build order only covers the opening.
After the first few minutes, the game becomes dynamic.
You react to what you see.
You adapt to the opponent's strategy.
The build order gave you a strong position — it didn't win the game.

Agile methodology is the StarCraft mid-game.
You've executed your build order — the project is set up, the architecture is sound.
Now you play reactively, adjusting to user feedback, market changes, and technical surprises.
The build order got you here.
Reaction wins the game.

## Scouting: User Research

In StarCraft, if you don't scout, you die.
Period.
A player who builds the wrong units because they didn't know the opponent was going air gets crushed.
A player who expands into a choke point the opponent already controls loses the expansion.
Information is more valuable than any unit.

User research is scouting.
If you don't talk to users, watch them use your product, read their support tickets, and analyze their behavior, you're building blind.
You might be building the perfect counter to a strategy the opponent isn't using.
You might be expanding into territory nobody wants.

StarCraft players send a worker to scout at supply 13.
They sacrifice a unit to gain information.
Good software teams do the same — they sacrifice development time to talk to users, run usability tests, and analyze metrics.
The cost of scouting is always less than the cost of building the wrong thing.

## Tech Trees: Technology Choices

Every StarCraft race has a technology tree.
You can't build battlecruisers without a starport, a fusion core, and an armory.
You can't research stimpack without a tech lab on your barracks.
Each technology unlocks new capabilities but requires investment in the prerequisite technologies.

Technology stacks are tech trees.
You can't deploy containers without a container runtime.
You can't run Kubernetes without understanding networking, DNS, and certificate management.
You can't implement real-time features without WebSockets, which requires understanding persistent connections, which requires understanding your load balancer's timeout settings.

The StarCraft lesson about tech trees is simple: don't tech too fast and don't tech too wide.

Teching too fast means skipping army production to rush advanced technology.
In StarCraft, this loses to an early attack.
In software, this means spending months building infrastructure while shipping nothing.
The business can't wait for your perfect Kubernetes setup.
Ship something with simpler tech and upgrade later.

Teching too wide means researching every upgrade simultaneously.
In StarCraft, this spreads resources thin and leaves you weak everywhere.
In software, this means adopting every new framework, database, and tooling option.
Your team can't be experts in everything.
Pick a path through the tech tree and commit to it.

## Unit Composition: Team Composition

In StarCraft, army composition matters more than army size.
A player with 50 marines loses to a player with 10 banelings and 20 zerglings.
A player with 20 stalkers loses to a player with 10 immortals.
Each unit has strengths and weaknesses, and the right combination is stronger than any individual unit.

Team composition works the same way.
Ten frontend developers can't build a backend service.
Ten senior engineers can't ship quickly without junior engineers handling the simpler tasks.
Ten generalists can't match a team with specialized expertise in security, performance, and DevOps.

The ideal StarCraft army mixes unit types that cover each other's weaknesses.
Marines deal high damage but are fragile — medivacs keep them alive.
Zealots are strong in close combat but slow — sentries create force fields to trap enemies.

The ideal software team mixes skills the same way.
Backend engineers build the services.
Frontend engineers build the interfaces.
DevOps engineers build the infrastructure.
Security engineers build the defenses.
No single role can win the game alone.

## Multitasking: Context Switching

StarCraft demands multitasking.
While your army fights at the front, your economy must keep producing at home.
While you scout the enemy, your upgrades must keep researching.
Drop one ball and the whole performance suffers.

Software development demands the same.
While you write code, production issues arise.
While you debug a problem, meetings are scheduled.
While you plan the next sprint, the current sprint falls behind.

StarCraft players learn to use control groups — binding units and buildings to hotkeys so they can jump between tasks instantly.
Press 1, manage the army.
Press 2, build workers.
Press 3, research upgrades.
The hotkeys don't reduce the number of tasks, but they reduce the cost of switching between them.

In software, your control groups are your tools and workflows.
A good IDE setup lets you switch between files instantly.
A good terminal setup lets you switch between environments instantly.
A good project management tool lets you switch between tasks instantly.

But StarCraft also teaches that there's a hard limit to multitasking.
Even pros can't manage five simultaneous drops, a base race, and an upgrade timing all at once.
They prioritize.
They let minor fights play out automatically while they manage the critical ones.

Software developers need to learn the same lesson.
You can't context-switch between five tasks and do any of them well.
Prioritize the critical path.
Let minor tasks wait.
Not everything is a drop in your mineral line.

## Creep Spread: Codebase Quality

Zerg players will recognize this one.
Creep is the organic substance that Zerg structures generate, spreading across the ground like a living carpet.
Zerg units move faster on creep.
Zerg structures can only be built on creep.
Creep tumors extend the network, and a well-spread creep carpet gives the Zerg player vision, mobility, and territorial control.

Codebase quality is creep spread.
Good test coverage, clear documentation, consistent naming conventions, and well-defined interfaces — these are your creep tumors.
Each one extends the area where future development moves faster.
New engineers onboard more quickly on a well-documented codebase.
Refactoring is safer with comprehensive tests.
Features ship faster when the interfaces are clean.

Terran and Protoss players hate creep.
It gives the Zerg vision and speed in territory that should be neutral.
Technical debt is the reverse — it gives bugs and confusion territory that should be clean.
Every hardcoded value, every undocumented assumption, every god class is an area where development moves slower and bugs move faster.

The Zerg lesson: invest in creep spread early and often.
A Zerg player who tumors aggressively in the first five minutes controls the map in the tenth.
A team that invests in code quality early ships faster in the long run.
Not because quality is its own reward, but because quality compounds.

## Ladder Anxiety: Imposter Syndrome

Every StarCraft player knows ladder anxiety.
That feeling before clicking the "Find Match" button — the fear of losing, of being exposed as a fraud, of dropping a league and having everyone see.

The anxiety is universal.
Grandmasters feel it.
Day9 famously talked about how terrified he was to play his placement matches, and he was one of the best players in the world.

Imposter syndrome in software is ladder anxiety.
The fear of submitting a pull request because your code might be wrong.
The fear of speaking up in an architecture meeting because your idea might be bad.
The fear of applying for a senior role because you might not be good enough.

StarCraft players overcome ladder anxiety the same way every time: by playing.
Not by studying build orders.
Not by watching replays.
By clicking the button and playing the game.
Losses stop hurting after the hundredth one.
Wins start feeling earned.

Software developers overcome imposter syndrome the same way.
Submit the pull request.
Speak up in the meeting.
Apply for the role.
The fear doesn't go away.
You just learn that it's not predictive of outcome.

## Cheese: Shortcuts and Hacks

Every StarCraft player has been cheesed.
A cannon rush in your mineral line.
A proxy barracks outside your base.
A six-pool of zerglings that arrives before you have any defense.

Cheese strategies are high-risk, high-reward.
They win quickly against unprepared opponents and lose decisively against prepared ones.
Nobody wins a tournament with cheese alone.
But everyone encounters it, and everyone has to learn to defend against it.

Technical shortcuts are cheese.
Copy-pasting code from Stack Overflow without understanding it.
Deploying directly to production without tests.
Hardcoding a configuration value because you're in a hurry.

Like StarCraft cheese, technical shortcuts work in the short term.
The code runs.
The feature ships.
The deadline is met.
But the opponent — in this case, future you or your teammate — is unprepared for the consequences.
The hardcoded value becomes a production incident.
The untested code breaks in an edge case.
The copy-pasted solution has a security vulnerability.

StarCraft players learn to scout for cheese early and defend against it.
Software developers need to do the same.
Code review catches shortcuts before they merge.
Linting and static analysis catch them before they deploy.
The defense doesn't have to be elaborate — just present.

## The Late Game: Software Factories

In the late game of StarCraft, something shifts.
Individual battles matter less than economy and production.
The player with more bases, more production facilities, and better upgrades wins through attrition.
They replace losses faster.
They tech-switch faster.
They recover from setbacks faster.

Software factories are the late game of software development.
Individual code contributions matter less than the systems that produce them.
The team with better CI/CD, better testing infrastructure, better monitoring, and better AI tooling ships faster.
They recover from incidents faster.
They adapt to changing requirements faster.
They replace departing engineers faster.

In StarCraft, the late game rewards the player who invested in economy during the early and mid game.
The player who cut workers to build a bigger army might win a battle, but they lose the war.
In software, the late game rewards the team that invested in infrastructure when it would have been faster to just ship features.
The team that skipped tests to hit a deadline might ship faster this quarter, but they slow down every quarter after.

## Playing the Race: Choosing Your Stack

In StarCraft, race selection defines everything.
Terran is positional and mechanical — siege tanks, bunkers, planetary fortresses.
Protoss is elegant and powerful — expensive units, warp-in mechanics, force fields.
Zerg is swarm-like and reactive — expendable units, rapid reinforcement, creep spread.

Each race rewards a different mindset.
A player who tries to play Terran like Zerg — aggressive, expendable, swarm-like — loses.
A player who tries to play Protoss like Terran — defensive, positional, slow — loses.
You have to play your race's strengths.

Technology stacks are races.
A Python/Django stack rewards rapid development and convention-over-configuration — Protoss-like elegance.
A Java/Spring stack rewards enterprise robustness and type safety — Terran-like positional strength.
A Go microservices stack rewards simplicity, concurrency, and operational efficiency — Zerg-like speed and resilience.

Teams that try to fight their stack's nature lose.
Using Python for high-performance computing.
Using Java for rapid prototyping.
Using Go for enterprise business logic.
Each can work, but each is fighting the race's design.

Play your race.
Or in StarCraft terms: pick Random, learn all three, and choose the one that fits the game you're playing.

## The GG: Knowing When to Refactor

In StarCraft, there's a moment every player must learn to recognize: the game is lost.
Your economy is destroyed.
Your army is gone.
Your opponent has three bases to your one.
Fighting on is admirable but wasteful.

Good players type "gg" — good game — and leave.
Not because they're quitters.
Because the time spent losing a doomed game is better spent starting a new one where they can apply what they learned.

The software equivalent is knowing when to rewrite.
Not every codebase can be saved.
Sometimes the technical debt is so deep, the architecture so convoluted, the assumptions so wrong, that incremental improvement is slower than starting fresh.

But here's where the StarCraft analogy gets tricky.
In StarCraft, a new game starts clean.
In software, a rewrite inherits the constraints of the existing system — the users, the data, the integrations.
The "gg" in software isn't abandoning the project.
It's recognizing that the current implementation has reached the point of diminishing returns and a new approach will serve everyone better.

StarCraft players learn to recognize the threshold through experience.
They don't quit at the first setback.
They quit when recovery becomes impossible.
Software teams need the same judgment.
Don't rewrite at the first sign of technical debt.
Rewrite when the debt makes every change slower than a fresh start would be.

## The Lesson

StarCraft is a game of simultaneous decisions under time pressure.
You manage economy, technology, army composition, map control, and reconnaissance all at once, while an opponent does the same and tries to disrupt you.
The best players aren't the ones with the fastest hands — they're the ones who make better decisions about where to invest their attention.

Software development is the same game.
You manage features, infrastructure, team composition, code quality, and user feedback all at once, while the market changes and competitors advance.
The best teams aren't the ones who write the most code — they're the ones who make better decisions about where to invest their resources.

In StarCraft, every game is different.
The map changes, the opponent changes, the meta shifts.
But the fundamentals remain: workers gather resources, buildings unlock technology, scouting reveals information, and good decisions win games.

In software, every project is different.
The domain changes, the team changes, the technology shifts.
But the fundamentals remain: engineers build features, infrastructure enables scale, user research reveals needs, and good decisions ship products.

If you're still playing single-player, it's time to scout the map.
If you're still on one base, it's time to expand.
If you're still manually producing every unit, it's time to set a rally point.

GL HF.

## See also

- [Code Factories: The Factorio Perspective](/code-factories-factorio) — the same concept explored through Factorio metaphors
