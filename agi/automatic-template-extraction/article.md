---
title: Automatic template extraction
created: 2016-07-14
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore
* To extract patterns, group them by starting character, then test how many have the same following character
* Grammar induction
* Compression
	* Compression can be a tool for automatic template extraction, however we would most likely want to priority semantics of the extracted template over better compression
* Diff/match/patch
* Fragment extraction, then wildcard pattern generation
* Lexer-like that will replace a whole sequence if it is already in the grammar instead of doing character by character replacement like sequitur

# Overview
* Extract textual templates from any language (basically tries to find repetitions/patterns)
* Min/max length (characters)
* Discovery of syntax
* Hierarchical/meta extraction

# Example
<...> is a placeholder (can be replaced/is variable)

<pre><code class="language-php line-numbers">
public function getClassification()
{
	return $this->classification;
}

public function setClassification($classification)
{
	$this->classification = $classification;

	return $this;
}
</code></pre>

<pre><code class="language-php line-numbers">
public function get<x>()
{
	return $this-><y>;
}


public function set<x>(<y>)
{
	$this-><z> = <y>;

	return $this;
}
</code></pre>

<pre><code class="language-php line-numbers">
class SomeClass extends Model {
	protected $table = 'some_table';

	protected $fillable = ['field_1', 'field_2'];
}
</code></pre>

<pre><code class="language-php line-numbers">
class <x> extends Model {
	protected $table = '<y>';

	protected $fillable = [<z>];
}
</code></pre>

## If extraction
<pre><code class="language-php line-numbers">
if ($someCondition) {
	// Do something
}
</code></pre>

<pre><code class="language-php line-numbers">
if (<x>)
	<y>
</code></pre>

# Prototype ideas/pseudo-code
* Create a dictionary of all seen characters
* Create a dictionary of characters -> index
* Define some sort of relative threshold for which to ignore patterns
* You have a single string, you want to extract patterns out of it
* You have two strings, you want to extract patterns out of them

# Questions
* How to extract simple constructs such as if/elseif/else/while/do/for/foreach?
* How to compress aaaabbbb into an expanding aCb -> aaCbb -> aaaCbbb -> aaaabbbb vs AB -> aaaaB -> aaaabbbb
	* aaaabbbb -> aaaCbbb -> aaDbb -> aEb -> F
		* C := ab
		* D := aCb
		* E := aDb
		* F := aEb

		* C := aCb
-> This is a context-free grammar
* Do we want to prioritize short rules such as S -> Sa such that they can be repeated many times, or rules that contains a lot of symbols such as S -> aSa
	* Probably want to minimize the number of rules/productions
	* Probably want to minimize the rule length
* From [^1]
	* p1: no pair of adjacent symbols appears more than once in the grammar;
	* p2: every rule is used more than once.
* How can we prefer `public function <>(<>) {<>}` over `} public function <>(<>) {`?
	* If we refer to an explicit grammar, we can give more weight to the first one because it is likely a construct/production in the grammar, while the second one is the concatenation of two productions

# See also

# References
* http://www.sequitur.info/
* [Identifying Hierarchical Structure in Sequences: A linear-time algorithm](http://www.jair.org/media/374/live-374-1630-jair.pdf)
* https://en.wikipedia.org/wiki/Three-address_code
* https://en.wikipedia.org/wiki/Optimizing_compiler
* https://en.wikipedia.org/wiki/Intermediate_representation
* https://en.wikipedia.org/wiki/Abstract_syntax_tree
