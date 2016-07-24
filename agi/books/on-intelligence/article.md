---
title: Jeff Hawkins - On Intelligence (2004)
created: 2016-06-30
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore
* Is there any research/proof that cortical regions learn and store sequences of pattern? How does that work at the neuron level?
* It is claimed that neuron? cells remain active for a relative long duration of a sequence, what is considered "active"? Is it the firing of the neuron on its axon?

# Overview

## One hundred-step rule exercise
Hawkins suggests that the brain is able to recognize a cat in a picture in less than half a second. He names this the one hundred-step rule, meaning processing an image to determine the presence or absence of a cat can go through neural network of 100 neurons deep (each neuron takes about 5ms to fire and reset, thus a chain of 100 neurons can be fired in 500ms).

Here we do a little bit of thinking about the network itself. If it was a single input neuron connected to all of the neurons in the brain, then in a single step, all neurons would have been reached. However this design is highly unlikely as it would require every single neuron to be connected to that input neuron.

Then we think of the brain as a tree structure. With 100 levels, it is very likely for the brain to be fully covered. However a tree structure implies that there would be no consolidation of information. Neurons would be fired, but at no point would a neuron say "yeap, that's a cat alright". It would be more like "I saw a paw", "I saw some ears", "I saw a tail", but nothing aggregating all of these indices.

TBC

## AGI model
* System that integrates and differentiate inputs
* The differences are what trigger/attract attention

## Some critique
* The books mentions "experiments show that", yet no sources are given

# Notes
## Preface
* The biggest mistake is the belief that intelligence is defined by intelligent behavior
* It is the ability to make predictions about the future that is the crux of intelligence
* A good theory should be easy to comprehend, not obscured in jargon or convoluted argument

## 1 Artificial Intelligence
* Computers and brains are built on completely different principles
	* One is programmed, one is self-learning
	* One has to be perfect to work at all, one is naturally flexible and tolerant of failures
	* One has a central processor, one has no centralized control
* The AI approach was born with the digital computer
* A key figure in the early AI movement was the English mathematician Alan Turing
* A thesis of this book is that understanding cannot be measured by external behavior, it is instead an internal metric of how the brain remembers things and uses its memories to make predictions
* When you don't know how to proceed, often the best strategy is to make no changes until your options become clear

# 2 Neural Networks
* Linguists talked of intelligence in terms such as "syntax" and "semantics". To them, the brain and intelligence was all about language
* Vision scientists referred to 2D, 2.5D and 3D sketches. To them, the brain and intelligence was all about visual pattern recognition
* Computer scientists talked of schemas and frames, new terms they made up to represent knowledge
* Anatomists and neurophysiologists wrote extensively about the structure of the brain and how neurons behave, but they mostly avoided any attempt at large-scale theory
* A neural network is unlike a computer in that it has no CPU and doesn't store information in a centralized memory. The network's knowledge and memories are distributed throughout its connectivity - just like real brains (the connectivities/weight values is the distributed memory, which, unless "stored"/"persisted", means that the brain would be void of any memory)
* Hawkins 3 essential things to understanding the brain:
	* The inclusion of time in brain function: Real brains process rapidly changing streams of information. There is nothing static about the flow of information into and out of the brain.
	* The importance of feedback: Feedback dominates most connections throughout the neocortex.
	* Any theory or model of the brain should account for the physical architecture of the brain: Any neural network that didn't acknowledge ... the repeating hierarchical structure of the neocortex ... was certainly not going to work like a brain.
* The most fundamental problem with most neural networks is a trait they share with AI programs. Both are fatally burdened by their focus on behavior. Whether they are calling these behaviors "answers," "patterns," or "outputs," both AI and neural networks assume intelligence lies in the behavior that a program or a neural network produces after processing a given input. The most important attribute of a computer program or a neural network is whether it gives the correct or desired output. As inspired by Alan Turing, intelligence equals behavior
* Intelligence is not just a matter of acting or behaving intelligently. Behavior is a manifestation of intelligence, but not the central characteristic or primary definition of being intelligent
* You can be intelligent just lying in the dark, thinking and understanding
* Auto-associative memories are built out of simple "neurons" that connected to each other and fired when they reached a certain threshold. They are interconnected differently than regular neural networks, using lots of feedback. Instead of only passing information forward, as in a back propagation network, auto-associative memories fed the output of each neuron back into the input. This feedback loop led to some interesting features. When a pattern of activity was imposed on the artificial neurons, they formed a memory of this pattern
* The most important property is that you don't have to have the entire pattern you want to retrieve in order to retrieve it
* An auto-associative memory can be designed to store sequences of patterns, or temporal patterns
* Hawkins proposes the brain uses circuits similar to auto-associative memory
* We don't have machine that think, we have machines that do
* Intelligence is something that is happening in your head. Behavior is an optional ingredient
* According to functionalism, being intelligent or having a mind is purely a property of organization and has nothing to do with what you're organized out of
* By this principle, an artificial system that used the same functional architecture as an intelligent, living brain should be likewise intelligent - and not just contrivedly so, but actually, truly intelligent
* Some philosophers of mind have taken a shine to the metaphor of the "cognitive wheel," that is, an AI solution to some problem that although entirely different from how the brain does it is just as good
* To succeed (have intelligent machines), we will need to crib heavily from nature's engine of intelligence, the neocortex. We have to extract intelligence from within the brain

## 3 The Human Brain
* Being human and being intelligent are separate matters. An intelligent machine need not have sexual urges, hunger, a pulse, muscles, emotions, or a humanlike body
* The neocortex is about 2 millimeters thick and has six layers
* Stretched flat, the human neocortical sheet is roughly the size of a large dinner napkin
* Human are smarter because our cortex, relative to body size, covers a larger area, not because our layers are thicker or contain some special class of "smart" cells
* Some anatomists have estimated that the typical human neocortex contains around thirty billion neurons (30,000,000,000), but no one would be surprised if the figure was significantly higer or lower
* Each of these regions (of the cortex) is semi-independent and seems to be specialized for certain aspects of perception or thought. Physically they are arranged in an irregular patchwork quilt, which varies only a little from person to person. Rarely are the functions cleanly delineated. Functionally they are arranged in a branching hierarchy
* The lowest of the functional regions, the primary sensory areas, are where sensory information first arrives in the cortex
* V1 (the primary visual area) is concerned with low-level visual features such as tiny edge-segments, small-scale components of motion, binocular disparity (for stereo-vision), and basic color and constrast information
* Eventually, sensory information passes into "association areas," which is the name sometimes used for the regions of the cortex that receive inputs from more than one sense
* It is thanks to association regions that your are able to be aware that the sight of a fly crawling up your arm and the tickling sensation you feel there share the same cause
* Pyramidal neurons comprises 8 out of every 10 neuron cells of the neocortex
* Mountcastle suggests that since (all the brain) regions all look the same, perhaps they are actually performing the same basic operation. He proposed that the cortex uses the same computational tool to accomplish everything it does
* Mountcastle argues that the reason one region of cortex looks slightly different from another is because of what it is connected to, and not because its basic function is different. He concludes that there is a common function, a common algorithm, that is performed by all cortical regions
* The human brain has an incredible capacity to learn and adapt to thousands of environments that didn't exist until very recently. This argues for an extremely flexible system, not one with a thousand solutions for a thousand problems
* Apparently no area of cortex is content to represent nothing. The visual cortex, not receiving information from the eyes like it is "supposed" to, casts around for other input patterns to sift through - in this case, from other cortical regions
* Visual information from the outside world is sent to your brain via a million fibers in your optic nerve. After a brief transit through the thalamus, they arrive at the primary visual cortex
* Sounds are carried via the thirty thousand fibers of your auditory nerve. They pass through some older parts of your brain and then arrive at your primary auditory cortex
* Your spinal cord carries information about touch and internal sensations to your brain via another million fibers. They are received by your primary somatosensory cortex
* In vision, the sense organ is your retina. An image enters your pupil, gets inverted by your lens, hits your retina, and creates a spatial pattern. This pattern gets relayed to your brain
* About three times every second, your eyes make a sudden movement called a saccade. They fixate on one point, and then suddenly jump to another point. Every time your eyes move, the image on your retina changes. This means that the patterns carried into your brain are also changing completely with each saccade
* Sounds are converted into action potentials through a coiled-up organ in each ear called the cochlea. High-frequency tones cause vibrations in the cochlea's stiff base. Low-frequency tones cause vibrations in the cochlea's floppier and wider outer portion. Mid-frequency tones vibrate intermediate segments. Each site on the cochlea is studded with neurons that fire as they are shaken
* Vision is more like three senses - motion, color and luminance (black-and-white constrast)
* Touch has pressure, temperature, pain, and vibration
* We also have an entire system of sensors that tell us about our joint angles and bodily position. It is called the proprioceptive system
* We also have the vestibular system in the inner ear, which gives us our sense of balance
* Your cortex doesn't really know or sense the world directly. The only thing the cortex knows is the pattern streaming in on the input axons

## 4 Memory
* A neuron collects inputs from its synapses, and combines these inputs together to decide when to output a spike to other neurons. A typical neuron can do this and reset itself in about five milliseconds, or around two hundred times per second
* The one hundred-step rule: In half a second, the information entering your brain can only traverse a chain one hundred neurons long. That is, the brain "computes" solutions to problems like this in one hundred steps or fewer, regardless of how many total neurons might be involved (comparison computer instructions with neurons "instructions", which is a faulty comparison)
* How can a brain perform difficult tasks in one hundred steps that the largest parallel computer imaginable can't solve in a million or a billion steps? The answer is the brain doesn't "compute" the answers to problems; it retrieves the answers from memory
* The entire cortex is a memory system. It isn't a computer at all
* There are four attributes of neocortical memory that are fundamentally different from computer memory:
	* The neocortex stores sequences of patterns
	* The neocortex recalls patterns auto-associatively
	* The neocortex stores patterns in an invariant form
	* The neocortex stores patterns in a hierarchy
* You can only recall memory the same way you learned it (in the same sequence)
* Texture can only be perceived through pattern sequences across the pressure-and vibration-sensing neurons in your skin (differences?)
* An auto-associative memory system is one that can recall complete patterns when given only partial or distorted inputs
* How can we perceive something as being the same or constant when the input patterns representing it are novel and changing?
* We use the term invariant representation to refer to the brain's internal representation (the same neuron cells are triggered while in presence of the same high level concept (e.g. a face))
* Memories are stored in a form that captures the essence of relationships, not the details of the moment
* When you see, feel, or hear something, the cortex takes the detailed, highly specific input and converts it to an invariant form. It is the invariant form that is stored in memory, and it is the invariant form of each new input pattern that it gets compared to
* The way you understand the world is by finding invariant structure in the constantly changing stream of input

## 5 A New Framework of Intelligence
* To notice that something is different, some neurons in my brain that weren't active before would have to become active. [...] When I look around the room, my brain is using memories to form predictions about what it expects to experience before I experience it. [...] But when some visual pattern comes in that I had not memorized in that context, a prediction is violated. And my attention is drawn to the error
* Prediction is not just one of the things your brain does. It is the primary function of the neocortex, and the foundation of intelligence
* The important point is that higher intelligence is not a diffent kind of process from perceptual intelligence
* Intelligence is measured by the capacity to remember and predict patterns in the world, including language, mathematics, physical properties of objects, and social situations
* Behavior came first, then intelligence
* Here then is the core of my argument on how to understand the neocortex, and why memory and prediction are the keys to unlocking the mystery of intelligence. We start with the reptilian brain with no cortex. Evolution discovers that if it tacks on a memory system (the neocortex) to the sensory path of the primitive brain, the animal gains an ability to predict the future. [...] By comparing the actual sensory input with recalled memory, the animal not only understands where it is but can see into the future.
* Intelligence and understanding started as a memory system that fed predictions into the sensory stream
* To know something means that you can make predictions about it
* The cortex has evolved in two directions. First it got larger and more sophisticated in the types of memories it could store. Second, it started interacting with the motor system of the old brain
* Prediction, not behavior, is the proof of intelligence

## 6 How the Cortex Works
* Using the "top-down" approach, you start with the image of what the solved puzzle should look like, and use this to decide which pieces to ignore and which pieces to search for
* The other approach is "bottom-up", where you focus on the individual pieces themselves. You study them for unusual features and look for close matches with other puzzle pieces
* If you don't have a picture of the puzzle's solution, the bottom-up method is sometimes the only way to proceed
* To make predictions, your cortex needs a way to memorize and store knowledge about sequences of events
* To make predictions of novel events, the cortex must form invariant representations

### Invariant Representations
* Each V1 neuron has a so-called receptive field that is highly specific to a minute part of your total field of vision
* Each V1 cell is also tuned for specific kinds of input patterns. For instance, a particular cell might fire vigorously when it sees a line or an edge slanted at thirty degrees within its receptive field
* In the course of spanning four cortical stages from retina to IT, cells have changed from being rapidly changing, spatially specific, tiny-feature recognition cells, to being constantly firing, spatially nonspecific, object recognition cells
* There are many, if not more feedback connections in visual cortex as there are feedforward connections
* With hearing and touch you can't recognize an object with a momentary input. Therefore the neural activity corresponding to the mental perception of objects, such as spoken words, must last longer in time than the individual input patterns

### Integrating the Senses
* Information flows up and down sensory hierarchies to form predictions and create a unified sensory experience
* We interpret downward-flowing patterns as predictions. In the motor cortex we interpret them as motor commands

## A New View of V1
* If all cortical regions perform the same function, why should IT be special?
* Experiments clearly show that nonadjacent patches of V1 are not directly connected; the left side of V1 can't know directly what the right side is seeing
* Subregions or clusters of V1 are physically disconnected but do the same thing
* Experiments show that all higher regions of cortex receive converging inputs from two or more sensory regions below themselves
* The job of any cortical region is to find out how its inputs are related, to memorize the sequence of correlations between them, and to use this memory to predict how the inputs will behave in the future
* Invariant representations are formed in every cortical region

## A Model of the World
* One of the most important concepts in this book is that the cortex's hierarchical structure stores a model of the hierarchical structure of the real world. The real world's nested structure is mirrored by the nested structure of your cortex
* You can only experience a subset of the world at any moment in time
* A sequence is a set of patterns that generally accompany each other but not always in a fixed order. What is important is that patterns of a sequence follow one another in time even if not in a fixed order
* The fact that certain input patterns repeat time and again is what lets a cortical region know that those experiences are caused by a real object in the world
* "Whenever I see any of these events, I will refer to them by a common name. It is this group name, not the individual patterns, that I will pass on to higher regions of the cortex" - Cortical region

# See also

# Sources
* https://www.amazon.com/Intelligence-Jeff-Hawkins/dp/0805078533