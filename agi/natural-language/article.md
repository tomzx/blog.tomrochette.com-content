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

# Overview

# User oriented

* Vocabulary
	* Shortest/Longest word/sentences (characters/syllables)
* Categories
	* Level of speech
	* Type of words
* Distribution
	* Word length
	* Sentence length
	* Syllable count
	* Number of punctuation used per sentence
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

Words vs Sentences

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

# See also

# Sources

* http://textalyser.net/index.php?lang=en
* http://www.online-utility.org/text/analyzer.jsp
* http://www.editcentral.com/gwt1/EditCentral.html