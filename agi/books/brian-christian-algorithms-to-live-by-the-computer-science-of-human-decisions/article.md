---
title: Brian Christian - Algorithms to Live By: The Computer Science of Human Decisions - 2016
created: 2017-07-27
taxonomy:
  category: [Artificial General Intelligence]
  status: finished
---

## Context

## Learned in this study

## Things to explore
* Optimal stopping
* Given that exploration can lead to better results than our current best option, it seems rational to try and determine the likelihood of finding better alternative and to use that to guide further exploration (vs exploitation)
* Is Google search results LRU-based?

# Overview

# Notes
## Introduction
* How can one know that something is the best unless you have a baseline to judge it against?
* The more information you gather, the better you'll know the right opportunity when you see it - but the more likely you are to have already passed by it
* It requires some sort of balance between looking and leaping
* You should spend 37% of your time exploring options, the rest of the time is about finding the best options
* The algorithms that researchers have developed to solve the hardest classes of problems have moved computers away from an extreme reliance on exhaustive calculation. Instead, tackling real-world tasks requires being comfortable with chance, trading off time with accuracy, and using approximations

## 1 Optimal Stopping
* When have you met enough people to know who your best match is?
* What if acquiring the data costs you that very match?
* The optimal solution takes the form of what we'll call the Look-Then-Leap Rule: You set a predetermined amount of time for "looking" - that is, exploring your options, gathering data - in which you categorically don't choose anyone, no matter how impressive. After that point, you enter the "leap" phase, prepared to instantly commit to anyone who outshines the best applicant you saw in the look phase
* In the face of slim pickings, lower your standards. With more fish in the sea, raise them
* The overall rate at which people found the best possible applicant was pretty good: about 31%, not far from the optimal 37%
* For people there's always a time cost (which makes them stop earlier than when optimal)
* Neil Bearden: "After searching for a while, we humans just tend to get bored. It's not irrational to get bored, but it's hard to model that rigorously."

## 2 Explore/Exploit
* Exploration is gathering information, exploitation is using the information you have to get a known good result
* In computer science, the tension between exploration and exploitation takes its most concrete form in a scenario called the "multi-armed bandit problem"
* The explore/exploit tradeoff isn't just a way to improve decisions about where to eat or what to listen to. It also provides fundamental insights into how our goals should change as we age, and why the most rational course of action isn't always trying to choose the best

### Regret and Optimism
* Regret is the result of comparing what we actually did with what would have been best in hindsight
* Assuming you're not omniscient, your total amount of regret will probably never stop increasing, even if you pick the best possible strategy - because even the best strategy isn't perfect every time
* Regret will increase at a slower rate if you pick the best strategy than if you pick others; what's more, with a good strategy regret's rate will go down over time, as you learn more about the problem and are able to make better choices
* The minimum possible regret - again assuming non-omniscience - is regret that increases at a logarithmic rate with every pull of the handle
* In a multi-armed bandit problem, an Upper Confidence Bound algorithm says, quite simply, to pick the option for which the top of the confidence interval is highest
* An Upper Confidence Bound algorithm doesn't care which arm has performed the best so far; instead, it chooses the arm that could reasonably perform best in the future
* Upper Confidence Bound algorithms implement a principle that has been dubbed "optimism in the face of uncertainty"
	* By focusing on the best that an option could be, given the evidence obtained so far, these algorithms give a boost to possibilities we know less about

### Explore...
* Our intuitions about rationality are too often informed by exploitation rather than exploration
* Over a lifetime, you're going to make a lot of decisions. It's actually rational to emphasize exploration - the new rather than the best, the exciting rather than the safe, the random rather than the considered - for many of those choices, particularly earlier in life

### ... And Exploit
* The elderly have few social relationships by choice
	* The result of lifelong selection processes by which people strategically and adaptively cultivate their social networks to maximize social and emotional gains and minimize social and emotional risks
* These differences in social preference are not about age as such - they're about where people perceive themselves to be on the interval relevant to their decision
* What an explorer trades off for knowledge is pleasure

## 3 Sorting
### Blood Sort: Pecking Orders and Dominance Hierarchies
* Displacement happens when an animal uses its knowledge of the hierarchy to determine that a particular confrontation simply isn't worth it
* Dominance hierarchies are ultimately information hierarchies

## 4 Caching
* What to do when cache is full?

### Eviction and Clairvoyance
* The goal of cache management is to minimize the number of times you can't find what you're looking for in the cache and must go to the slower main memory to find it; these are known as "page faults" or "cache misses"
* The optimal cache eviction policy - essentially by definition - is, when the cache is full, to evict whichever item we'll need again the longest from now
* Bélády compared Random Eviction, FIFO, and variants of LRU in a number of scenarios and found that LRU consistently performed the closest to clairvoyance
* The LRU principle is effective because of something computer scientists call "temporal locality": if a program has called for a particular piece of information once, it's likely to do so again in the near future
* The nearest thing to clairvoyance is to assume that history repeats itself - backwards

### Filing and Piling
* If you always put an item back (you just used) at the very front of the list, then the total amount of time you spend searching will never be more than twice as long as if you'd known the future

### The Forgetting Curve
* A natural way to think about forgetting is that our minds simply run out of space
* The key idea behind Anderson's new account of human memory is that the problem might be not one of storage, but of organization
* According to his theory, the mind has essentially infinite capacity for memories, but we have only a finite amount of time in which to search for them
* The key to a good human memory becomes the same as the key to a good computer cache: predicting which items are most likely to be wanted in the future
* Reality has a statistical structure that mimics the Ebbinghaus (Forgetting) curve
* Many people hold the bias that human memory is anything but optimal. They point to the many frustrating failures of memory. However, these criticisms fail to appreciate the task before human memory, which is to try and manage a huge stockpile of memories. In any system responsible for managing a vast data base there must be failures of retrieval. It is just too expensive to maintain access to an unbounded number of items

## 5 Scheduling
### Handling Deadlines
* In the case of single-machine scheduling, however, if we are going to do all the tasks assigned, then all schedules will take equally long to complete; the order is irrelevant
* First lesson in single-machine scheduling: make your goals explicit
* If you are concerned with minimizing maximum lateness, then the best strategy is to start with the task due soonest and work your way toward the task due last. This strategy is known as Earliest Due Date
* Moore's Algorithm says that we start out just like with Earliest Due Date - by scheduling out our produce in order of spoilage date, earliest first, one item at a time. However, as soon as it looks like we won't get to eating the next item in time, we pause, look back over the meals we've already planned, and throw out the biggest item (that is, the one that would take the most days to consume)
* Moore's algorithm minimizes the number of items you'll need to throw away

### Getting Things Done
* Minimizing the sum of completion times leads to a very simple optimal algorithm called Shortest Processing Time: always do the quickest (shortest) task you can
* Only prioritize a task that takes twice as long if it's twice as important

### Picking Our Problems
* Putting off work on a major project by attending instead to various trivial matters can likewise be seen as "the hastening of subgoal completion" - which is another way of saying that procrastinators are acting (optimally!) to reduce as quickly as possible the number of outstanding tasks on their minds
* Staying focused not just on getting things done but on getting weighty things done sounds like a surefire cure for procrastination. But as it turns out, even that is not enough

### Priority Inversion and Precedence Constraints
* Sometimes that which matters most cannot be done until that which matters least is finished, so there's no choice but to treat that unimportant thing as being every bit as important as whatever it's blocking

### Drop Everything: Preemption and Uncertainty
* The weighted version of Shortest Processing Time is a pretty good candidate for best general-purpose scheduling strategy in the face of uncertainty
	* Each time a new piece of work comes in, divide its importance by the amount of time it will take to complete. If that figure is higher than for the task you're currently doing, switch to the new one; otherwise stick with the current task

### Preemption Isn't Free: The Context Switch
* A friend of ours who writes software says that the normal workweek isn't well suited to his workflow, since for him sixteen-hour days are more than twice as productive as eight-hour days
* Brian, for his part, thinks of writing as a kind of blacksmithing, where it takes a while just to heat up the metal before it's malleable. He finds it somewhat useless to block out anything less than ninety minutes for writing, as nothing much happens in the first half hour except loading a giant block of "Now, where was I?" into his head
* The more you take on, the more overhead there is. At its nightmarish extreme, this turns into a phenomenon called thrashing

### Thrashing
* If a task requires keeping track of so many things that they won't all fit into memory, then you might well end up spending more time swapping information in and out of memory than doing the actual work
* Computer scientists now use the term "trashing" to refer to pretty much any situation where the system grinds to a halt because it's entirely preoccupied with metawork
* The easiest thing to do is simply to get more memory: enough RAM, for instance, to fit the working sets of all the running programs into memory at once and reduce the time taken by a context switch
* Another way to avert trashing before it starts is to learn that art of saying no
* In cases where there's clearly no way to work any harder you can work ... dumber
	* Instead of answering the most important emails first - which requires an assessment of the whole picture that may take longer than the work itself - maybe you should sidestep that quadratic-time quicksand by just answering the emails in random order, or in whatever order they happen to appear on-screen

### Interrupt Coalescing
* The moral is that you should try to stay on a single task as long as possible without decreasing your responsiveness below the minimum acceptable limit
* Decide how responsive you need to be - and then, if you want to get things done, be no more responsive than that
* If you find yourself doing a lot of context switching because you're tackling a heterogeneous collection of short tasks, you can also employ another idea from computer science: "interrupt coalescing"
	* Wait until some fixed interval and check everything, instead of context-switching to handle separate, uncoordinated interrupts from their various subcomponents

## 6 Bayes's Rule
### The Copernican Principle
* Unless we know better we can expect to have shown up precisely halfway into the duration of any given phenomenon. And if we assume that we're arriving precisely halfway into something's duration, the best guess we can make for how long it will last into the future becomes obvious: exactly as long as it's lasted already (known as the Copernican Principle)
	* This is basically because we assume either a standard or gaussian distribution, and being at the 50% (mass) point is the likeliest of all

### ... and Their Prediction Rules
* For any power-law distribution, Bayes's Rule indicates that the appropriate prediction strategy is a Multiplicative Rule
	* Multiply the quantity observed so far by some constant factor. For an uninformative prior, that constant factor happens to be 2, hence the Copernican prediction; in other power-law cases, the multiplier will depend on the exact distribution you're working with
* When we apply Bayes's Rule with a normal distribution as a prior, on the other hand, we obtain a very different kind of guidance. Instead of a multiplicative rule, we get an Average Rule
	* Use the distribution's "natural" average - its single specific scale - as your guide
* Between those two extremes, there's actually a third category of things in life: those that are neither more nor less likely to end just because they've gone on for a while
* The Erlang distribution gives us a third kind of prediction rule, the Additive Rule
	* Always predict that things will go on just a constant amount longer

### Small Data and the Mind
* Small data is big data in disguise
* The reason we can often make good predictions from a small number of observations - or just a single one - is that our priors are so rich

## 7 Overfitting
### How to Combat Overfitting: Penalizing Complexity
* If you can't explain it simply, you don't understand it well enough
* Introduce an additional term to your calculations that penalizes more complex solutions. If we introduce a complexity penalty, then more complex models need to do not merely a better job but a significantly better job of explaining the data to justify their greater complexity
	* Computer scientists refer to this principle - using constraints that penalize models for their complexity - as Regularization
* Living organisms get a certain push toward simplicity almost automatically, thanks to the constraints of time, memory, energy, and attention. The burden of metabolism, for instance, acts as a brake on the complexity of organisms, introducing a caloric penalty for overly elaborate machinery
* Neuroscientists have suggested that brains try to minimize the number of neurons that are firing at any given moment
* Language forms yet another natural Lasso: complexity is punished by the labor of speaking at greater length and the taxing of our listener's attention span

### The Upside of Heuristics
* The study of heuristics shows that less information, computation, and time can in fact improve accuracy

### The Weight of History
* Giving yourself time to decide about something does not necessarily mean that you'll make a better decision. But it does guarantee that you'll end up considering more factors, more hypotheticals, more pros and cons, and thus risk overfitting

### When to Think Less
* If you have all the facts, they're free of error and uncertainty, and you can directly assess whatever is important to you, then don't stop early. Think long and hard: the complexity and effort are appropriate

## 8 Relaxation
### Defining Difficulty
* An algorithm should be considered "efficient" if it runs in what's called "polynomial time" - that is, $O(n^n)$, $O(n^3)$, or in fact n to the power of any number at all
* A problem, in turn, is considered "tractable" if we know how to solve it using an efficient algorithm
* A problem we don't know how to solve in polynomial time, on the other hand, is considered "intractable"

### Just Relax
* One of the simplex forms of relaxation in computer science is known as Constraint Relaxation
	* In this technique, researchers remove some of the problem's constraints and set about solving the problem they wish they had
	* Then, after they've made a certain amount of headway, they try to add the constraint back in
* If you can't solve the problem in front of you, solve an easier version of it - and then see if that solution offers you a starting point, or a beacon, in the full-blown problem

### Uncountably Many Shades of Gray: Continuous Relaxation
* Turn a discrete problem into a continuous one (where instead of using integers you use reals)

### Just a Speeding Ticket: Lagrangian Relaxation
* The idea behind Lagrangian Relaxation is simple
	* An optimization problem has two parts
		* The rules
		* The scorekeeping
	* In Lagragian Relaxation, we take some of the problem's constraints and bake them into the scoring system instead

### Learning to Relax
* Relaxation offer us a number of advantages
	* They offer a bound on the quality of the true solution (as the unconstrained solution set will contain the constrained solution as an (possibly) unoptimal solution)
	* Relaxations are designed so that they can indeed be reconciled with reality - and this gives us bounds on the solution from the other direction

## 9 Randomness
### When to Leave It to Chance
* There is a deep message in the fact that on certain problems, randomized approaches can outperform even the best deterministic ones
* Merely knowing that randomness can be helpful isn't good enough. You need to know when to rely on chance, in what way, and to what extent
* When we want to know something about a complex quantity, we can estimate its value by sampling from it

### In Praise of Sampling
* The polynomial identity test shows that sometimes our effort is better spent checking random values - sampling from the two expressions we want to know about - than trying to untangle their inner workings
* Given a pair of nondescript gadgets and asked whether they are two different devices or two copies of the same one, most of us would start pushing random buttons rather than crack open the cases to examine the wiring
* Rawls offered a way of approaching this set of questions that he called the "veil of ignorance."
	* Imagine, he said, that you were about to be born, but didn't know as whom: male or female, rich or poor, urban or rural, sick or healthy. And before learning your status, you had to choose what kind of society you'd live in. What would you want?
* When it comes to handling a qualitatively unmanageable problem, something so thorny and complicated that can be digested whole, sampling offers one of the simplest, and also the best, ways of cutting through the difficulties

### The Three-Part Tradeoff
* Time and space are at the root of the most familiar tradeoffs in computer science
* There is a third dimension: error probability

### Out of the Local Maximum
* Instead of turning to full-bore randomness when you're stuck, use a little bit of randomness every time you make a decision
* This is called the Metropolis Algorithm

### Creativity
* William James viewed randomness as the heart of creativity. And he believed it was magnified in the most creative people
* When it comes to stimulating creativity, a common technique is introducing a random element, such as a word that people have to form associations with
* Even if you're in the habit of sometimes acting on bad ideas, you should always act on good ones
* Your likelihood of following a bad idea should be inversely proportional to how bad an idea it is
* You should front-load randomness, rapidly cooling out of a totally random state, using ever less and less randomness as time goes on, lingering longest as you approach freezing

## 10 Networking
### Acknowledgment
* How exactly should we handle a person - or a computer - that's unreliable?
* The first question is how long a period of nonresponsiveness we should take to constitute a breakdown
* Once we do recognize a breakdown, what should we do about it?

### Exponential Backoff: The Algorithm of Forgiveness
* Retry at an exponential rate (1, 2, 4, 8, 16, ...) instead of simply giving up

### Flow Control and Congestion Avoidance
* Additive Increase, Multiplicative Decrease: Increase by one for each successful round and decrease by half the current rate in case of an unsuccessful round
* It may be that human communications themselves mirror the very protocols that transmit them: every text message or email reply encourages yet another, while every unreturned message stanches the flow
* Every public servant should be demoted to the immediately lower rank, because they were advanced until they became incompetent
	* José Ortega y Gasset
* One can imagine a corporation in which, annually, every employee is always either promoted a single step up the or chart or sent part of the way back down

### Backchannels: Flow Control in Linguistics
* Both the person who has the turn and his partner are simultaneously engaged in both speaking and listening. This is because of the existence of the back channel, over which the person who has the turn receives short messages such as "yes", and "uh-huh" without relinquishing the turn
* What happens when something listening to a personal story gets distracted: the story falls apart
	* A poor listener destroys the tale
* It is worthwhile to acknowledge someone while they are speaking

### Bufferbloat: It's the Latency, Stupid
* A buffer is essentially a queue whose function is to smooth out bursts

### Better Never than Late
* Take your most basic problem as a single person … someone likes you, you don’t like them back. At one point, that used to be kind of an awkward situation. You had to have a conversation, it was weird. Now what do you do? Someone likes you, you don’t like them back? You just pretend to be busy … forever.
* The problem isn't that we're always connected; we're not. The problem is that we're always buffered
* We used to reject; now we defer

## 11 Game Theory
### Reaching Equilibrium
* The mathematician John Nash proved in 1951 that every two-player game has at least one equilibrium

### Dominant Strategies, for Better or Worse
* The price of anarchy measures the gap between cooperation (a centrally designed or coordinated solution) and competition (where each participant is independently trying to maximize the outcome for themselves)

### Mechanism Design by Evolution
* Because feelings are involuntary, they enable contracts that need no outside enforcement
* Love is like organized crime. It changes the structure of the marriage game so that the equilibrium becomes the outcome that works best for everybody
* Being able to fall involuntarily in love makes you, in turn, a more attractive partner to have. Your capacity for heartbreak, for sleeping with the emotional fishes, is the very quality that makes you such a trusty accomplice

### Information Cascades: The Tragic Rationality of Bubbles
* Part of the reason why it's a good idea to pay attention to the behavior of others is that in doing so, you get to add their information about the world to your own
* On the other hand, learning from others doesn't always seem particularly rational
* Sealed-bid first-price auction: Each participant write down their bid in secret, and the one whose bid is the highest wins the item for whatever price they wrote down
* Dutch auction: Gradually lower an item's price until someone is willing to buy it
* English auction: Bidders alternate raising the price until all but one of them drop out
* Something very important happens once somebody decides to follow blindly his predecessors independently of his own information signal, and that is that his action becomes uninformative to all later decision makers. Now the public pool of information is no longer growing. That welfare benefit of having public information... has ceased
* Investors are said to fall into two broad camps:
	* Fundamental: trade on what they perceive as the underlying value of a company
	* Technical: trade on the fluctuations of the market
* Be wary of cases where public information seems to exceed private information, where you know more about what people are doing than why they're doing it, where you're more concerned with your judgements fitting the consensus than fitting the facts
* When you're mostly looking to others to set a course, they may well be looking right back at you to do the same
* Remember that actions are not beliefs; cascades get caused in part when we misinterpret what others think based on what they do
* We should remember from the prisoner's dilemma that sometimes a game can have irredeemably lousy rules

### To Thine Own Self Compute
* Vickrey auction: A sealed bid auction process. Every participant simply writes down a single number in secret, and the highest bidder wins. The winner ends up paying the bid of the second-place bidder
* Roger Myerson proved that any game that requires strategically masking the truth can be transformed into a game that requires nothing but simple honesty

## Conclusion
### Computational Kindness
* Three simple pieces of wisdom:
	* There are cases where computer scientists and mathematicians have identified good algorithmic approaches that can simply be transferred over to human problems
	* Knowing that you are using an optimal algorithm should be a relief even if you don't get the results you were looking for
	* We can draw a clear line between problem that admit straightforward solutions and problems that don't
* If we have control over which situations we confront, we should choose the ones that are tractable
* In the case of interviews, it seems that people preferred receiving a constrained problem, even if the constraints were plucked out of thin air, than a wide-open one
* Computation is bad: the underlying directive of any good algorithm is to minimize the labor of thought
* You can try to reduce, rather than maximize, the number of options that you give other people
* In the hard cases, the best algorithms are all about doing what makes the most sense in the least amount of time, which by no means involves giving careful consideration to every factor and pursuing every computation to the end

# See also

# References
* https://en.wikipedia.org/wiki/Optimal_stopping
