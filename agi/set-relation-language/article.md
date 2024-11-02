---
title: Set Relation Language
created: 2015-09-06
taxonomy:
  tag: [Artificial General Intelligence]
  status: in progress
---

## Notation

- A = {1, 2, 3}
- {x | x = 1 or x = 2 or x = 3}
- {x | P(x)} (where P is a predicate)

## Tests

Results in a boolean value.

- x memberOf A
- x containedIn A
- x includedIn A
- x elementOf A, x in A, x eo A
- A contains x
- A includes x, A has x
- A subsetOf B, A <= B
- A properSubsetOf B, A < B
- B supersetOf A, B >= A
- B properSupersetOf A, B > A

## Queries

- cardinality(A), card(A), |A| -> int (set is seen as a collection of elements)
- subsetCardinality(A), sscard(A) -> int (set is seen as a collection of elements AND sets)

## Operations/Transformations

Results in a Set.

- A union B, union(A, B), A + B, A | B, A u B
- A intersection B, intersection(A, B), A & B, A i B
- A difference B, difference(A, B), A - B, A \ B, A d B
- A symmetricDifference B, symmetricDifference(A, B) A xor B, A ^ B, A sd B
- A cartesianProduct B, cartesianProduct(A, B), A cartesian B, A x B, A * B, A cp B
- power A, power(A), p A, A**, A^, A^n

## Tests on relations

Results in a boolean value.

Consider f a function that maps items from set A to set B.

- surjective(f), sur(f)
- injective(f), inj(f)
- bijective(f), bij(f)

## Uncategorized

- Partial function
- Total function
- Reflexive
- Symmetric
- Antisymmetric
- Transitive
- Surjective
- Injective
- Bijective
- Composition
	- Cartesian product
- Membership
- Identity
- Domain
- Range
- Union - Field
- Inverse
- Image
- Preimage

## Ideas

- x Relation y
	- Tom isA human
	- Tom knows programming
	- Tom knows agi? (how do we determine the NOT operation based on relations alone? if there's no relation, then it implies the NOT operator)

# References
- https://en.wikibooks.org/wiki/Set_Theory/Relations
- https://en.wikibooks.org/wiki/Set_Theory/Sets
- https://en.wikipedia.org/wiki/Set_theory
- https://en.wikipedia.org/wiki/Set-builder_notation
