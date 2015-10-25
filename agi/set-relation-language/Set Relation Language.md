---
title: Set Relation Language
created: 2015-09-06
taxonomy:
  category: [artificial general intelligence]
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

- cardinality(A), card(A), |A| -> int

## Operations/Transformations

Results in a Set.

- A union B, A + B, A | B, A u B
- A intersection B, A & B, A i B
- A difference B, A - B, A \ B, A d B
- A symmetricDifference B, A xor B, A ^ B, A sd B
- A cartesianProduct B, A cartesian B, A x B, A * B, A cp B
- power A, p A, A**, A^, A^n

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
	- Tom knows agi? (how do we determine the NOT operation based on relations alone?)

# Sources
- https://en.wikibooks.org/wiki/Set_Theory/Relations
- https://en.wikibooks.org/wiki/Set_Theory/Sets
- https://en.wikipedia.org/wiki/Set_theory
- https://en.wikipedia.org/wiki/Set-builder_notation
