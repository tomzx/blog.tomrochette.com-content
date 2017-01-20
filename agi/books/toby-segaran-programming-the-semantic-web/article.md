---
title: Toby Segaran - Programming the Semantic Web - 2009
created: 2017-01-01
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview

# Notes
## 1. Why Semantics?
* Semantics: symbols can refer to things or concepts, and sequences of symbols convey meaning
* Ways to model data
	* Tabular Data
		* Easy to understand and formulate
		* Fields which contain more than a single piece of information are harder to use/parse
		* The models are rigid, limited and usually not changeable by the users
	* Relational Data
		* Fast and powerful tools for storing large sets of data where the data model is well understood and the usage patterns are fairly predictable
		* Pivot tables are essentially tables that indicate equality between two other tables entries
		* Schema migration is often a huge headache
	* Semantic Relationships
		* Extremely flexible, adaptible to new changes describing the data
		* Gets rid of normalization, degrades performance, columns type cannot be set/constrained

## 2. Expressing Meaning
* The triple is the fundamental building block of semantic representations
* It is composed of a subject, a predicate, and an object
* A subject corresponds to an entity - a "thing" for which we have a conceptual class
* Predicates are a property of the entity to which they are attached
* Objects are either entities or literal values such as strings or numbers
* Multiple triples can be tied together by using the same subjects and objects in different triples

## 3. Using Semantic Data
-

## 4. Just Enough RDF
### The RDF Data Model
* RDF is a language for expressing data models using statements expressed as triples
* Each statement is composed of a subject, a predicate, and an object

### Resources
* A resource is simply anything that can be identified with a Universal Resource Identifier (URI)

### Blank Nodes
* Blank nodes are graph nodes that represent a subject (or object) for which we would like to make assertions, but have no way to address with a proper URI

### Literal Values
* Can have an optional language (e.g., English, French) and type (e.g., integer, boolean, string, float)

### RDF Serialization Formats
* Four serialization formats:
	* N-Triples
	* N3
	* RDF/XML
	* RDF in attributes (RDFa)

* N3 uses the letter "a" as a predicate representing the RDF "type" relationship
	* tom a foaf:Person

### SPARQL
* SPARQL provides four forms of queries:
	* SELECT
	* CONSTRUCT
	* ASK
	* DESCRIBE

# See also

# References
* Segaran, Toby, Colin Evans, and Jamie Taylor. Programming the semantic web. " O'Reilly Media, Inc.", 2009.
