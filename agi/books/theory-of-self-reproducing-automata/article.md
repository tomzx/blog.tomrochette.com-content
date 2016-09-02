---
title: John von Neumann, Arthur W. Burks - Theory of self-reproducing automata (1966)
created: 2016-08-06
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore
* Higher class type implies it can describe a subset of the lower class type? For example, a program description (higher level) describing potential programs (lower level)
* For mutations to be probabilistically non-lethal, this means that most of the DNA code is likely to be a mutation chain that has expanded, while the basic mechanisms of self-reproduction are most likely minimal and left untouched

# Overview
* The idea that communication between different systems is done through the translation of their respective language into the target's language (for example, from the sender's central nervous system language to the sender's language (English) to the receiver's language (English) and finally into the receiver's language central nervous system language)
	* Is the sender's CNS language different from his english language?
* The idea that digital computers are used to perform computations of exceedingly great logical depth (while it would be the opposite for natural automata) seems to imply that we should look for ANN architectures that are more parallel and less deep
* When faced with a very difficult problem, it is difficult to even define what the difficulties are

# Notes
* (p14) A problem of any considerable complexity is composed of many subproblems, and flow diagrams and subroutines can be prepared for these in advance
* (p15) Thus the nervous system appears to be using a radically different system of notation from the ones we are familiar with in ordinary arithmetics and mathematics...
... whatever language the central nervous system is using, it is characterized by less logical and arithmetical depth than what we are normally used to.
Thus logics and mathematics in the central nervous system, when viewed as languages, must be structurally essentially different from those languages to which our common experience refers.
... when we talk mathematics, we may be discussing a secondary language, built on the primary language truly used by the central nervous system
* (p19) Two basic questions of automata theory:
	* How can reliable systems be constructed from unreliable components?
	* What kind of logical organization is sufficient for an automaton to be able to reproduce itself?
* (p20) Three fundamental factors limiting the engineer's ability to build really powerful computers:
	* The size of the available components
	* The reliability of these components
	* A lack of a theory of the logical organization of complicated systems of computing elements
* (p22) Natural automata are more parallel in operation, digital computers more serial
* (p22) Von Neumann calculated the thermodynamical minimum of energy that must be dissipated by a computing element and concluded that in theory computing elements could be of the order of $10^10$ times more efficient in the use of energy than neurons
* (p23) Von Neumann thought that below a certain level, complexity is degenerative, and self-reproduction is impossible. He suggested that, generally speaking, in the case of simple automata a symbolic description of the behavior of an automaton is simpler than the automaton itself, but that in the case of exceedingly complex automata the automaton is simpler than a symbolic description of its behavior
* (p24) Pulses circulating in neuron cycles, the change of neural thresholds with use, the organization of the nervous system, and the coding of the genes together constitute such a (memory) hierarchy (similar to a digital computer memory hierarchy)
* (p25) Von Neumann thought that automata mathematics should be closer to the continuous (mathematics) and should draw heavily on analysis. He thought that the specific problems of automata theory require this, and he felt that there is a general advantage in an analytical as opposed to a combinatorial approach in mathematics
* (p26) Von Neumann wanted a probabilistic logic which would handle component malfunction as an essential and integral part of automata operation
* (p28) Von Neumann found an analog of thermodynamic degeneration in the theory of self-reproducing automata: below a certain minimum level, complexity and degree of organization are degenerative, but above that level they are not degenerative and may even increase.
* (p28) The efficiency of a computer depends on the proper balance of its different parts with respect to speed and size
* (p28) Von Neumann thought that the mathematics of automata theory should start with mathematical logic and move toward analysis, probability theory, and thermodynamics
* (p32) Of all automata of high complexity, computing machines are the ones which we have the best chance of understanding. In the case of computing machines the complications can be very high, and yet they pertain to an object which is primarily mathematical and which we understand better than we understand most natural objects
* (p38) The reason for using a fast computing machine is not that you want to produce a lot of information. After all, the mere fact that you want some information means that you somehow imagine that you can absorb it, and, therefore, wherever there may be bottlenecks in the automatic arrangement which produces and processes this information, there is a worse bottleneck at the human intellect into which the information ultimately seeps
* (p39) All these automata really consist of two important parts: the general switching part (an active part which affects the logical operations the automaton is supposed to perform), and the memory (which stores information, chiefly intermediate results which are needed for a while and are then discarded and replaced by others)
* (p41) There is one very important thing we do not know: whether nature has ever been subject to this handicap (the use of memory to store temporary computation), or whether natural organisms involve some much better memory device
* (p41) In any fast machine the memory you need is characterized by two data:
	* the capacity
	* the access time
* (p44) McCulloch and Pitts wanted to axiomatize an idealized neuron, which is much simpler than the real one. They believed that the extremely amputated, simplified, idealized object which they axiomatized possessed the essential traits of the neuron, and that all else are incidental complications, which in a first analysis are better forgotten
* (p44) A formal neuron is symbolically designated by a circle, which symbolizes the body of the neuron, and a line branching out from the circle, which symbolizes the axon of the neuron. A neuron has two states: it's excited or not
* (p45) No matter how you formulate your conditions, you can always put a neural network in the box which will realize these conditions, which means that the generality of neural systems is exactly the same as the generality of logics
* (p47) Using the figures we have, which are not very good, but which are probably all right for an orientation, we conclude that apparently a network of about 2 billion relays does nothing but determine how to organize a visual picture
* (p47) There is a good deal in formal logics to indicate that the description of the functions of an automaton is simpler than the automaton itself, as long as the automaton is not very complicated, but that when you get to high complications, the actual object is simpler than the literary description
* (p48) Why has the digital notation never been used in nature, as far as we know, and why has this pulse notation been used instead? (in reference to neuron pulse)
	* Suggested answer: the frequency modulation scheme is more reliable than the digital scheme
* (p49) The memory requirements of the human nervous system are probably very large. Estimates have been made and they are of the order of 10^16 binary digits
* (p49) The main difficulty with th memory organ is that it appears to be nowhere in particular
* (p49) A lesser degree of complexity in an automaton can be compensated for by an appropriate increase of complexity of the instructions
	* Additional complexity is brought in by giving more elaborate instructions (separation of class types thus the avoidance of gödel incompleteness?)
* (p57) If you look at automata which have been built by men or which exist in nature you will very frequently notice that their structure is controlled only partly by rigorous requirements and is controlled to a much larger extent by the manner in which they might fail and by the (more or less effective) precautionary measures which have been taken against their failure. And to say that they are precautions against failure is to overstate the case, to use an optimistic terminology which is completely alien to the subject. Rather than precautions against failure, they are arrangements by which it is attempted to achieve a state where at least a majority of all failures will not be lethal. All we can try to do is arrange an automaton so that in the vast majority of failures it can continue to operate
* (p65) The human nervous system is roughly a million times more complicated than these large computing machines (ENIAC and IBM SSEC)
* (p65) The time in which a human nerve can respond is about 1/2 millisecond. However thattime is not a fair measure of the speed of the neuron, because what matters is not the time in which the neuron responds, but the time in which it recovers, the time from one response to the next potential response. That time is, at best, 5 milliseconds
* (p65) Thus the nervous system has a million times as many components as these machines have, but each components of the machine is about 5 thousand times faster than a neuron
* (p66) The thermodynamical minimum of energy per elementary act of information
	* $3 \times 10^{-14} \mathrm{ergs}$ for the the thermodynamical minimum
	* $3 \times 10^{-3} \mathrm{ergs}$ for a neuron cell
	* $6 \times 10^2 \mathrm{ergs}$ for a vacuum tube
* (p67) The disparity of $10^{11}$ between the thermodynamical minimum and the neuron might be due to something like a desire for reliability of operation
* (p68) There's no reason to believe that the memory of the central nervous system is in the switching organs (the neurons)
* (p69) The human organism is essentially a mixed system (digital and analog)
* (p69) It appears that digital mechanisms are necessary for complicated functions. Pure analog mechanisms are usually not suited for very complicated situations. The only way to handle a complicated situation with analog mechanisms is to break it up into parts and deal with the parts separately and alternately, and this is a digital trick
* (p70) The natural materials have some sort of mechanical stability and are well balanced with respect to mechanical properties, electrical properties, and reliability requirements
* (p72) In discussing a computing machine it is meaningless to ask how fast or how slow it is, unless you specify what type of problems will be given to it

## Re-evaluation of the problems of complicated automata - Problems of hierarchy and evolution
* (p75) The medium which is fed to the automaton and which is produced by the automaton is completely different from the automaton. In fact, the automaton doesn't produce any medium at all; it merely modifies a medium which is completely different from it
* (p75) Draw up a list of unambiguously defined elementary parts. Imagine that there is a pratically unlimited supply of these parts floating around in a large container. One can then imagine an automaton functioninig in the following manner: It also is floating around in this medium; it essential activity is to pick up parts and put them together, or, if aggregates of parts are found, to them them apart
* (p77) I will introduce as elementary units neurons, a "muscle," entities which make and cut fixed contacts, and entities which supply energy
* (p77) What principles are involved in organizing these elementary parts into functioning organisms, what are the traits of such organisms, and what are the essential quantitative characteristics of such organisms?
* (p78) An object is of the highest degree of complexity if it can do very difficult and involved things
* (p78) Living organisms are very complicated aggregations of elementary parts, and by any reasonable theory of probability or thermodynamics highly improbably. That they should occur in the world at all is a miracle of the first magnitude; the only thing which removes, or mitigates, this miracle is that they reproduce themselves
* (p79) These organisms have the ability to produce something more complicated than themselves
* (p79) An automaton A, which can make an automaton B, must contain a complete description of B and also rules on how to behave while effecting the synthesis
* (p79) Complication, or productive potentiality in organization, is degenerative, that an organization which synthesizes something is necessarily more complicated, of a higher order, than the organization it synthesizes
* (p79) Complication is degenerative below a certain minimum level
* (p80) There is a minimum number of parts below which complication is degenerative, in the sense that if one automaton makes another the second is less complex than the first, but above which it is possible for an automaton to construct other automata of equal or higher complexity
* (p80) Von Neumann estimated this threshold to be in the millions of simple parts required to be over the minimum threshold
* (p81) Eight kinds of parts:
	1. A stimulus organ (p or q)
	2. A coincidence organ (p and q)
	3. An inhibitory organ (p and not-q)
	4. A stimuli producer
	5. A rigid member (can connect to other rigid members as well as to parts which are not rigid members)
	6. A fusing organ (when stimulated, welds or solders two parts together)
	7. A cutting organ (when stimulated, unsolders a connection)
	8. A muscle (used to produce motion)
* (p82) The construction automaton contains in its memory a description of the automaton to be constructed. Operating under the direction of this description, it picks up the parts it needs and assembles them into the desired automaton. To do this, it must contain a device which catches and identifies the parts that come in contact with it
* (p84) There is reason to suspect that our predilection for linear codes, which have a simple, almost temporal sequence, is chiefly a literary habit, corresponding to our not particularly high level of combinatorial cleverness, and that a very efficient language would probably depart from linearity
* (p85) The juxtaposition of two copies of the same thing is in no sense of higher order than the thing itself
* (p85) The general constructive automaton A has a certain creative ability, the ability to go from a description of an object to the object
* (p86) The general copying automaton B has the creative ability to go from an object to two copies of it
* (p86) Neither A nor B are self-reproductive
* (p86) The control automaton C is far from having any kind of creative or reproductive ability. All it can do is stimulate two other organs so that they act in certain ways, tie certain things together, and cut these things loose from the original system
* (p86) Yet the combination of the three automata A, B and C is auto-reproductive. Thus you may break a self-reproductive system into parts whose functioning is necessary for the whole system to be self-reproductive, but which are not themselves self-reproductive
* (p86) Let X be A + B + C + D, where D is any automaton. Then $(A+B+C) + \phi(A+B+C+D)$ produces $(A+B+C+D) + \phi(A+B+C+D)$. In other words, our constructing automaton is now of such a nature that in its normal operation it produces another object D as well as making a copy of itself
* (p86) The system (A + B + C + D) can undergo processes similar to the process of mutation
* (p86) If any element is changed at random in one of the automata A, B, or C, the system will usually not completely reproduce itself
* (p86) If there is a change in the description $\phi(A+B+C+D)$, the system will produce, not itself, but a modification of itself. Whether the next generation can produce anything or not depends on where the change is. If the change is in A, B, or C, the next generation will be sterile. If the change occurs in D, the system with the mutation is exactly like the original system, except that D has been replaced by D'. This system can reproduce itself, but its by-product will be D' rather than D. This is the normal pattern of an inheritable mutation

## The Theory of Automata: Construction, Reproduction, Homogeneity
* (p92) Logical universality: When is a class of automata logically universal, i.e., able to perform all those logical operations that are at all performable with finite (but arbitrarily extensive) means?
* (p92) Constructability: Can an automaton be constructed, i.e., assembled and built from appropriately defined "raw materials," by another automaton?
* (p92) Construction-universality: Can any automaton be construction-universal, i.e., be able to construct every other automaton?
* (p92) Self-reproduction: Can any automaton construct other automata that are exactly like it? Can it be made, in addition, to perform further tasks, e.g., also construct certain other, prescribed automata?
* (p92) Evolution: Can the construction of automata by automata progress from simpler types to increasingly complicated types? Assuming some suitable definition of "efficiency," can this evolution go from less efficient to more efficient automata
* (p93) Von Neumann considered five models of self-reproduction:
	* The kinematic model: Deals with the geometric-kinematic problems of movement, contact, positioning, fusing, and cutting, but ignores problems of force and energy.
		* Logical (switch) and memory (delay) elements: store and process information
		* Girders: provide structural rigidity
		* Sensing elements: sense objects in the environment
		* Kinematic (muscle-like) elements: move objects around
		* Joining (welding) and cutting elements: connect and disconnect elements
	* The cellular model: Self-reproduction takes place in an indefinitely large space which is divided into cells, each cell containing the same finite automaton. Each cell of the infinite structure of the cellular model contains a 29-state automaton
	* The excitation-threshold-fatigue model: The neuron has a designated threshold and a designated refractory period. The refractory period is divided into two parts, an absolute refractory period and a relative refractory period. If a neuron is not fatigued, it becomes excited whenever the number of active inputs equals or exceeds its threshold. The neuron cannot be excited during the relative refractory period; it can be excited during the relative refractory period, but only if the number of active inputs equals or exceeds a threshold which is higher than the normal threshold
	* The continuous model: The cellular model of self-reproduction is developed first, it is then reduced to the excitation-threshold-fatigue model, and finally, this model is described by non-linear partial differential equations
	* The probabilistic model: Automata in which the transitions between states are probabilistic rather than deterministic
* (p106) Von Neumann chose an infinite 2-dimensional array of square cells. Each cell is occupied by the same 29-state finite automaton, and each such automaton is connected to its four immediate neighbords in exactly the same way
* (p107) The 29 states each cell is capable of assuming falls into three categories:
	* unexcitable (1)
	* excitable (20)
		* 4 confluent states $C_{\epsilon\epsilon'}$, where $\epsilon$ and $\epsilon'$ range over 0 and 1, 0 symbolize quiescence, 1 symbolizes excitation
		* 8 ordinary transmission states $T_{0\alpha\epsilon}$, where $\alpha = 0, 1, 2, 3$ and $\epsilon = 0, 1$ as before
		* 8 special transmission states $T_{1\alpha\epsilon}$
	* sensitized (8)
* (p110) Ordinary stimuli are to be used for logical operations, taking the species of the neurons that are involved as fixed; that is, ordinary stimuli are to be used for the control and utilization of already satifactorily organized sub-assemblies
* (p110) Special stimuli are to be used for growth operations, involving the introduction of excitability, together with a new determination of the neuronic species, into previously unexcitable, or otherwise different areas

# See also

# Sources
* Neumann, John von, and Arthur W. Burks. "Theory of self-reproducing automata." (1966).