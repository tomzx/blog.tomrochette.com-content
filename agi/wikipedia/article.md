---
title: Wikipedia
created: 2016-01-29
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

Wikipedia is the most popular and known encyclopedia of topics known to man. As such, it attempts to be complete and rigorous, which makes it a prime target as a source of knowledge.

Each article being uniquely identified by a URL, which allows us to *hopefully* uniquely identify knowledge topics using a common vocabulary.

## Learned in this study

## Things to explore

* Build a network graph to explore wikipedia
	* How should the graph be built?
	* Use tree/graph traversal algorithms to find the shortest path between two topics

# Overview

The goal of this article is to find means for people to track their knowledge through wikipedia as the source of common knowledge. As more and more people use a system in which this *knowledge* of knowledge is shared, it should be possible to develop tools such as "related pages" (a pool of page users that have visited a certain page also visited), "stereotypical users" (a *user* that is interested in AGI will look into these articles) and more based on users profiles.

# What should we track?

In order to determine what one should track, one has to ask himself what is the end purpose.

In our case, we want to be able to establish user profiles, that is, to characterize a visitor by the page he's visited.

Furthermore, one of the purpose of establishing a profile is to be able to tell its user what has already been explored.

Here's a non-exhaustive list of attributes we might be interested to track in order to establish such profile:

* view history
	* article name
	* date
	* time
* some way to track the article was read (since viewing the page does not necessarily translate to having read it)
* edited articles

# Relations within the content

Wikipedia contains a huge amount of internal links (links between articles) as well as external links. Internal links can be extremely valuable to us since they can allow us to build a network of topics.

There are various types of internal links, which we'll describe below:

## Content

Within the content of an article, there will often be terms which are themselves defined as an article.

A definition is generally based on other definitions which are themselves based on other definitions and so on.

As such, we can determine that internal links in the content of articles are reciprocal relations between the two articles. Another way to determine the relation between two articles is to verify if both link to one another.

## See also

The *See also* section of articles contains a list of vetted related articles that may interest the reader of the current article. As such, it may have no relation with the current article other than being of similar domain.

## Categories

As the definition of *[categories](https://en.wikipedia.org/wiki/Help:Category)* of Wikipedia states very well:

> **Categories** are intended to group together pages on similar subjects.

The category itself though can be seen as a container of all the articles. In other words, it can serve as an abstraction of all the articles under its umbrella.

# Additional relations

## Redirects

Some concepts are know under various name, but in order to reduce the amount of confusion between them, it is possible to create redirections which will bring to the generally accepted term of a concept. Thus, this allows us to determine that if we've read the article a redirection points to, we probably can safely assume that the point of redirection is also something we *now* know.

# Wikipedia exploration application

With all this information in hand, it is now time to design an application that will allow us to navigate through Wikipedia while allowing us to

# See also

# References

## Wikipedia API endpoints
* https://www.mediawiki.org/wiki/API:Categories
* https://www.mediawiki.org/wiki/API:Links
* https://www.mediawiki.org/wiki/API:Linkshere
* https://www.mediawiki.org/wiki/API:Redirects

## Wikipedia visualization tools
* http://sepans.com/sp/works/wikistalker/
* http://en.eyeplorer.com/show/
* http://www.idea.org/WikiNodes.htm

## Wikipedia toolkits
* https://github.com/Wikidata/Wikidata-Toolkit

## Mindmap
* https://github.com/kennethkufluk/js-mindmap
