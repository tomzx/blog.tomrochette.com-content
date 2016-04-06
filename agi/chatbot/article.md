---
title: Chatbot
created: 2015-08-26
taxonomy:
  status: in progress
  tag: [ai, chatbot]
---

## Learned in this study

* A machine can generate sentences that are grammatically and syntactically correct, but devoided of any semantical sense

## Things to explore

* How can a machine learn simply from text (no other input sensors)
* Attempt to reproduce the internal chatter we all have in our mind

# Objectives

* Starts and maintains multiple conversation threads
* Knows many facts about the world
* Does not attempt to deceive its interlocutor (make it think it is something that it is not)

# Corpus construction

* Set of letters -> allow to discover anagrams

# Sequence of language learning

* Store all sentences heard and repeat them word for word
	* Nothing new is ever said
* Build a markov chain of all heard sentences and generate sentences
	* Nothing new is ever said as markov chains are simply the encoding of the probability a "path sentence" being heard
* Teach it valid grammar and vocabulary for a language
	* Can generate a lot of grammatically valid sentences but devoided of any meaning
* Infer/build a grammar/vocabulary based on experience
	* Limited to what has been seen (which is fine)
	* Can be taught or can learn incorrect grammar/vocabulary
* Build a network of "concepts" = words
	* Used alone, would simply generate a random arrangement of words
	* Builds upon other strategies to generate sentences as this is more related to generating concept-related sentences

## The constructive nature of language

```mermaid
graph TD;
	0[Nothing]
	0 --> 1[Vocabulary]
	1 --> 2[Sentences/Grammar]
	2 --> 3[Context sensitivity]
```

# Problems

* Simply repeating what they've heard
* Creating grammatically valid sentences devoided of any meaning
* What is said has no relation to what is being discussed (no context)

# *Things* it needs to be able to do

* Construct grammatically valid sentences
* Reply with context relevant content

# Construction of sentences

* Learn about as many words as possible (learn in the sense of knowing how they are formed, not their significance)
* Learn about the valid relations that the word can been seen in (before or after certain words)
* Attempt to generalize a valid grammar

Construction of sentences at this level means that the chatbot has no intent. Sentences may make grammatical/syntactical sense, but semantically they don't mean anything.

By constructing a relation graph between words, the chatbot may *begin* to be able to make semantical sense. For instance, if it has seen **red car** often, it may be able to infer that **red** can be replaced by any other color. To do so, it will have to be able to know that red, blue, green, yellow, orange, etc. are **colors**, and that *colors* maybe changed for one another in some *contexts*. This construct is known as **is-a[^is-a]**. The question then becomes, how can I tell what is the type of relation between two words? Is it a **is-a/type-of** (hyponym-hypernym), **has-a** (holonym-meronym), **part-of** (meronym-holonym) or **member-of** (meronym-holonym).

Is it possible, simply by looking at enough examples and without supervision to determine classes of words?

* Noun
* Pronoun
* Adjective
* Verb
* Adverb
* Preposition
* Conjunction
* Interjection
* Article

# Context

Reward feed: If the bot says something to someone and that person replies with the name of the agent and +1/-1 to indicate whether what the bot said is relevant or not, the bot can build knowledge of what to say/not say based on "context" (vaguely undefined here)

* How can context be built and used?
	* Store what others are saying and use the words they've used to create an overlay over the word network the bot already possess

# Internal dialog loop

Each and everyone of us has an internal voice we talk to ourselves with. In this same fashio, the internal dialog loop of a chatbot keeps thinking to itself what to discuss next as well as listening to whomever is currently talking.

```mermaid
graph TD;
    0[Start]
    0 --> 1[Main loop]
    1 --> 2[Sense = listen]
    2 --> 3[Think = process]
    3 --> 4[Act = communicate]
    4 --> 5[End loop]
    5 --> 1
    5 --> 6[Done]
```

## IBM Watson Dialog Service

Request
* A client id
* A conversation id
* An input string

Response
* A client id
* A conversation id
* An input string
* An html formatted response

The replies that are generated contains "actionables". It appears that dialogs are oriented around specific domains and thus it will generate responses that may have data specifically formatted for the purpose of the application.

**Source**
* https://new-console.ng.bluemix.net/catalog/services/dialog/

## Microsoft Bot Framework

Microsoft Bot Framework works in the same fashion as IBM Watson Dialog Service: the develop defines the actionables, in other words, what will make the bot progress in state, and the user requests are simply processed in order to attempt to extract information about the action the user wants to take.

**Source**
* https://dev.botframework.com/
* http://docs.botframework.com/sdkreference/csharp/forms.html

# Use an existing dictionary

* https://github.com/first20hours/google-10000-english
* http://norvig.com/ngrams/count_1w.txt
* https://books.google.com/ngrams/info
* http://storage.googleapis.com/books/ngrams/books/datasetsv2.html

# Topics of interest

* https://en.wikipedia.org/wiki/Is-a

# Sources

## Grammar

* https://en.wikipedia.org/wiki/English_grammar
* https://en.wikipedia.org/wiki/Grammar_checker
* http://englishgrammar101.com/
* https://en.wikipedia.org/wiki/Formal_grammar
* https://en.wikipedia.org/wiki/Chomsky_hierarchy


## Part of speech

* https://en.wikipedia.org/wiki/Part_of_speech
* https://en.wikipedia.org/wiki/Part-of-speech_tagging
* https://en.wikipedia.org/wiki/Moby_Project
* http://wordlist.aspell.net/
* http://wordlist.aspell.net/pos-readme
* https://wordnet.princeton.edu/
* http://ucrel.lancs.ac.uk/claws/

## Language

* https://en.wikipedia.org/wiki/Formal_language

[^is-a]: https://en.wikipedia.org/wiki/Is-a
