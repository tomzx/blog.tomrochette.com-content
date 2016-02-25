---
title: PHP Brain
created: 2016-02-24
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

* Splay tree memory access

# Overview

The goal of this article is to detail my process of developing an initial implementation of a "brain" in PHP. As a  initial version, I want to lay down the tools that will help me build such thing so that it may be decomposed into libraries of reusable components.

# Components

* Stopwatch/Time monitoring
* Memory monitoring
* Tokenizer
* Token cleanup
* Database
* Cache layers

# Construction

The first step in order to be able to do anything is to be able to store information. In our case, we will use wikipedia articles as a source of information.

## Naïve in-memory implementation

A naïve first implementation will simply store the article tokens in a huge array we'll call a `stream`. When we add tokens, we also build up a dictionary or word lookup table, which allows us to return the index of a given word in the `stream`. Doing so allows us to quickly retrieve (dictionary lookup should be O(1)) whether we've already seen a word previously or not at the cost of memory.

This simple construct allows us to store and retrieve strings relatively rapidly. However, as its knowledge base increases in size, it becomes more and more memory hungry (increases linearly with how much data we insert) and slower to test if a particular query string has been seen (a simplistic layered token filtering algorithm will perform badly on frequent/common words).

With this simple "study" of document insertion and retrieval, we can observe two properties we'd like to respect:

* Given a specific amount of memory space for storage and temporary computation, the process should stay within these boundaries at the price of losing existing information.
* Querying for a string should be done in constant time. Given a deadline, the result should either be a result or a failure to find the answer. Common knowledge should be more readily accessible than less frequently used knowledge. In the latter case, it is acceptable to spend more time retrieving said information (similar to how splay tree would optimize their tree).

In order to have a common knowledge base during the rest of our tests, we will build on a small subset of articles from wikipedia. The list can be found [here](assets/txt/articles.txt). It consists of about 200 articles with varying amount of content.

Using an implementation of the previously mentioned strategy yields the following results:

| Min (s) | Mean (s) | Max (s) | StdDev (s) |
|---------|----------|---------|------------|
| 0.001000 | 0.208460 | 0.737043 | 0.173586 |

Thus, on average it takes ~210ms to process a query of length varying from 0 to 100 words with a standard deviation of ~175ms.

## Upgrading to a database

### The relational database approach

The next obvious step is to move from an in-memory data store to a database such as MySQL. Doing so allows us to make use of more efficient means of data storage and retrieval.

In order to store our articles, we have a couple of ways to structure the information:
* Create a `documents` table where we have a field that contains the whole article in a single row
* Create a `words` table where we have a field that contains all the words of the article in a sequence over multiple rows

![Documents table](assets/images/documents.png)

In the `documents` table approach, we cannot "quickly" retrieve if a word is contained within the knowledge base. It is necessary to go through each article and search for the given word.

![Words table](assets/images/words.png)

In the `words` table approach however we can quickly retrieve if a word is contained within the knowledge base but we cannot tell from which article it came.

| Min (s) | Mean (s) | Max (s) | StdDev (s) |
|---------|----------|---------|------------|
| 0.005000 | 0.187026 | 0.240013 | 0.031417 |

![Documents-Words tables](assets/images/documents-words.png)

Thus the next approach is to make an hybrid of both: a table such that we have a column that identifies the article containing the word.

Here, we can reconstruct the whole sentence by querying for a given `document_id` and ordering by id. If you are familiar with [database normalization](https://en.wikipedia.org/wiki/Database_normalization), you will probably notice very soon that the word column will most likely contains hundreds, if not thousands and more, copies of the same word. Thus, it'll most likely be appropriate to move this dictionary of unique words to its own table.

![Documents-Documents_Words-Words tables](assets/images/documents-documents_words-words.png)

Given enough time, one will probably end up with a data structure like the following:

![Corpus to word tables](assets/images/corpus-to-word.png)

This database contains relations going from corpus down to word. We could even go a little bit further and deconstruct words into characters.

The biggest issue with such a design is that querying for sentences become very complicated. You basically need to do as many `JOIN` as you have words in your lookup query. Each query must then also make sure that words are sequential within the given sentence (that is, the `id` field is increasing). One thing that can be done is to add an `order` column to the `sentence_word` table such that the words "this is a sentence" look as such:

| word | order |
|------|-------|
| this | 0 |
| is | 1 |
| a | 2 |
| sentence | 3 |

This allows us to tell the query that `W2.order =  W1.order + 1` (that the order of the word 2 `W2` must be one more than the order of word 1 `W1`). However all of this is very cumbersome to work with (although it could definitely be hidden from developers/users once a query generator is built to create such requests).

### The key-value database approach

If you recall our initial in-memory approach, we used a simple dictionary approach to store and retrieve information. In other words, we used a key-value storage approach, for which key-value databases such as Redis have been built.

To reproduce the same behavior has we had in memory, we'll create the following keys:

* stream: A list of all the words we've seen in order
* stream.$word: A list per word we can use to lookup all the index at which the word can be found in the `stream` list

If we reuse the same ideas of the naïve in-memory implementation, but apply it to a key-value datastore such as Redis, we get the following results:

| Min (s) | Mean (s) | Max (s) | StdDev (s) |
|---------|----------|---------|------------|
| 0.507029 | 5.694373 | 13.236758 | 3.798500 |

As you can probably tell, these results are terrible. This is mainly caused by the fact that we need to check if every word is available in the datastore (n queries) and then we need to fetch the list of each word in order to search for the word sequence. Furthermore, like we initially discovered in the naïve implementation analysis, common words will produce a lot of indexes. In this particular case, it makes the search worse as we'll be receiving thousands of indexes (for instance the word "of" will return approximately 59k results).

In this particular case, it seems obvious that getting rid of very frequent words could help us deal with this issue. If, for example we will skip any word that has more than 1000 indexes (we'll refer to this as the cutoff parameter). When we will be asked to search a sequence A * C (where * is a frequent word), we will simply ignore checking the frequent word and match any word instead. This is more permissive than previous testing methods and will return incorrect results. With this change, we get the following results:

| Min (s) | Mean (s) | Max (s) | StdDev (s) |
|---------|----------|---------|------------|
| 0.000000 | 0.074198 | 0.344020 | 0.084238 |

If we play with the cutoff parameter and decrease it to 100 (from 1000), performance improve quite considerably (at the cost of generating more wildcard words).

| Min (s) | Mean (s) | Max (s) | StdDev (s) |
|---------|----------|---------|------------|
| 0.000000 | 0.006155 | 0.052003 | 0.008185 |

# Serial vs parallel

So far we've been exploring various ways to store information in a sequential fashion, document by document. This obviously simplifies reflecting about the whole system because we do not have to consider concurrent interations. But this also means that we are limited to doing things in a sequential manner which is more likely going to be a bottleneck further down the road.

# See also

# Sources
