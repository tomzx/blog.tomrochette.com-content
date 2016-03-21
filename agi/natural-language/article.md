---
title: Natural language
created: 2015-12-06
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

We use natural language on a daily basis, either to communicate with others or to communite with ourself in the future by leaving us notes. Similarly to fitness trackers, it can be possible to track the "health" of our language and how it evolves over time. Learning about our own language learning history can be as interesting as history itself.

## Learned in this study

## Things to explore

* Generate simplified version of complex texts (use X most common words instead of the least frequently used words)
	* What are the tools available to do such a thing? Synonyms/Antonyms/Definitions?
* Natural language as a problem is nothing other than the question of transferring knowledge between encodings
* Compression through function composition
	* One can create a new sequence of values simply by applying a function over the generative function.

# Overview

# Structure of a "generic" natural language

- Characters
	- Words
		- Sentences
			- Paragraphs
				- Sections
					- Documents
						- Corpus 

At the root of every natural language is a set of graphemes (also known as glyphs, signs or characters). Once you are past the graphemes, everything is about relations:

- words are constructed by assembling a sequence of characters
- sentences are constructed by assembling a sequence of words
- and so on.

We rarely think of characters themselves when the language uses the latin alphabet. However languages making use of the chinese characters (chinese, japanese, korean and vietnamese[^3]), the characters are associated to some idea (may it be an action/verb or an object). Thus, we will generate reflect on words and their relations with one another. But thinking this way is wrong. We do not think about the words themselves, but their overall field of activation (all the images and experiences we've had about the word/concept).

A machine can however be taught to associate a symbol with anything (as symbols are simply placeholders).

# Problem reduction

In order for computers to process spoken language, it needs to be able to process audio and convert it into text. Once that is done, it is then a problem of understanding natural language in a textual form. However, in recent natural language processor, it is not rare for the process to be intertwined. This allows the algorithm to suggest which words were heard based on grammar rules as well as other rules the algorithm might have learned (for instance through statistical analysis).

# Processing and retrieval

How does one store as much information while using as little space as possible? What about being able to receive a stream of information and being able to tell, bit by bit, whether this sequence has already been observed in the past? The former sounds like compression while the latter sounds like string search.

# User oriented

* Vocabulary
	* Shortest/Longest word/sentences (characters/syllables)
* Categories
	* Level of speech
	* Type of words
* Distribution
	* Word length
	* Word frequency (most frequent count to least frequent)
	* Sentence length (words, characters)
	* Syllable count
	* Number of punctuation used per sentence
	* Word frequency spectrogram (0 if word is not known, 1 if it is)
* Usage frequency
* Evolution of vocabulary (history of word usage)
	* First/Last time a word was used
* Distribution/Density of vocabulary over a period of time (how many different words have been used for a given period of time)
* Markov chains (sequence of words with their probability of occurring)
* Complexity factor (lexical density)
* Readability (Gunning-Fog index) (Flesch-Kincaid grade level) (Coleman-Liau index) (SMOG index) (Automated readability index)
* Number of characters/words/sentences tracked
* Source of the word (document, conversation)
* Number of languages learned/used
* Percentage of words used (against the number of active words in a language)
* Vocabulary based on the time of the day
* bigram, trigram, four-gram

## Words vs Sentences

# Between 2 or more users

* Common vocabulary
* Shared vocabulary
* Unique vocabulary

# Context specific

## IRC/Chat oriented

* Most active channels
* Most active users
* Most active user per channel
* Activity distribution throughout the day (per channel)
* Vocabulary analysis
 * Per channel
 * Per user
 * Words distribution (top 100)
* Most common initiator of conversation
* Conversation killer
* Who interacts/talk with who the most
* Who asks questions?
* Who exclaims a lot?
* Language detection
* Link database (collect all url linked in chat)
* User time of arrival/departure (per channel)
* Distribution of sentence length

# Algorithms for computing readability

wordCount is the number of words in the text.
sentenceCount is the number of sentences in the text.
syllableCount is the number of syllables in the text.
letterNumberCount is the number of letters and numbers in the text.
complexCount is the number of words of three or more syllables in the text.

## Flesch reading ease score
double fres = 206.835 - (1.015 * wordCount) / sentenceCount - (84.6 * syllableCount) / wordCount;

##  Automated readability index
double ari = (4.71 * letterNumberCount) / wordCount + (0.5 * wordCount) / sentenceCount -21.43;

##  Flesch-Kincaid grade level
double fkgl = (0.39 * wordCount) / sentenceCount + (11.8 * syllableCount) / wordCount - 15.59;

##  Coleman-Liau index
double cl = (5.89 * letterNumberCount) / wordCount - (30.0 * sentenceCount) / wordCount - 15.8;

##  Gunning fog index
double fog = 0.4 * ( (double)wordCount / sentenceCount + (100.0 * complexCount) / wordCount );

## SMOG index
double smog = Math.sqrt( complexCount * 30.0 / sentenceCount ) + 3.0;

# English language

The Second Edition of the Oxford English Dictionary contains entries for 171,476 words in current use as well as 47,156 obsolete words[^1].

The average active vocabulary of an adult English speaker is of around 20,000 words, with a passive vocabulary of around 40,000[^2].

It is said that a vocabulary of just 3000 words provides coverage for around 95% of common texts[^2].

# See also

# Sources

[^1]: http://www.oxforddictionaries.com/words/how-many-words-are-there-in-the-english-language
[^2]: http://www.lingholic.com/how-many-words-do-i-need-to-know-the-955-rule-in-language-learning-part-2/
[^3]: https://en.wikipedia.org/wiki/Chinese_characters

## Graphemes
* https://en.wikipedia.org/wiki/Writing_system
* https://en.wikipedia.org/wiki/Grapheme
* https://en.wikipedia.org/wiki/Character_(symbol)
* https://en.wikipedia.org/wiki/Latin_script

## Text analysis
* http://textalyser.net/index.php?lang=en
* http://www.online-utility.org/text/analyzer.jsp
* http://www.editcentral.com/gwt1/EditCentral.html
* Free word frequency list http://www.wordfrequency.info/sample.asp
* http://voyant-tools.org/