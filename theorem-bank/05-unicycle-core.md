# Unicycle Core theorem bank

Recovered from the canonical V2 registry. **Records:** 20. Registry authority/status are preserved and do not imply independent re-verification.

## CLAIM-0280 — Unicyclic Tree-Absorption Reduction
**Status:** `UNCONDITIONAL_ALGORITHMIC` · **Authority:** `PROPOSED`

For a finite fiber-CSP whose connected incidence graph has exactly one cycle, absorb all attached trees by exact CC12 messages. The original CSP is coherent iff the resulting binary CSP on the unique cycle has a solution.

**Fingerprint:** `a9495fc14dfedd6ba04ae992b31ce9bf18c1ce9d8753fd23fb327d872dbdab47`

## CLAIM-0281 — Variable-Feedback Conditioning Theorem
**Status:** `UNCONDITIONAL_ALGORITHMIC` · **Authority:** `PROPOSED`

If S is a set of variable nodes whose deletion leaves an incidence forest, the CSP is coherent iff some assignment to S leaves a satisfiable restricted forest CSP.

**Fingerprint:** `5e5512625a4e18917028412aa8d0daa06eda42d7205d8ec154fabdbd41d05cd4`

## CLAIM-0282 — Twisted-Cycle K4-Free Realization
**Status:** `UNCONDITIONAL_CONSTRUCTION` · **Authority:** `PROPOSED`

For n≥7 and bits σ_i, there is a finite K4-free stable-partition realization whose cycle coherence relations are b_{i+1}=b_i⊕σ_i and whose realized triangle types are exactly the intended local triples.

**Fingerprint:** `5678366653fcd6940a5928ca1481b77950753a0c27ac3ed5d2f0b5fcde774d6f`

## CLAIM-0283 — Unicyclic Fixed-Point Criterion
**Status:** `UNCONDITIONAL_CHARACTERIZATION` · **Authority:** `PROPOSED`

After UC01 reduction to cycle relations R_i, coherence is equivalent to the relational composition R_0∘…∘R_{m-1} containing a fixed point.

**Fingerprint:** `f7714c87d602ce8d3d5fd76153cd2e7808fd68af62580246781a1499a7aee50b`

## CLAIM-0284 — Polynomial-Time Unicyclic Coherence
**Status:** `UNCONDITIONAL_ALGORITHMIC` · **Authority:** `PROPOSED`

Finite fiber-CSPs with at most one incidence cycle per connected component are decidable and reconstructible in polynomial time in the explicit instance size.

**Fingerprint:** `079f82b62d771b3fb89226250e0fb9005bc7a3b6112a1b19c340f4875e320724`

## CLAIM-0285 — Feedback-Set Coherence Algorithm
**Status:** `UNCONDITIONAL_ALGORITHMIC` · **Authority:** `PROPOSED`

With variable feedback set S, coherence is decidable in O((∏_{s∈S}|F_s|)·poly(N)); finite fiber coherence is FPT in variable-feedback number plus maximum fiber size.

**Fingerprint:** `706b86a853a647b505403cb8f9128687e5be00aa9fe970e255642794f89f8e6f`

## CLAIM-0286 — Feedback-Assignment Refutation Certificate
**Status:** `UNCONDITIONAL_CERTIFICATE` · **Authority:** `PROPOSED`

An incoherent finite CSP with feedback set S has a refutation consisting, for every assignment to S, of one exact forest empty-message certificate; at most ∏|F_s| such certificates are required.

**Fingerprint:** `5f933c4716780563efe79ef4b4520229a774dc31b7fc1ec3471be266ba0cb582`

## CLAIM-0287 — Permutation-Cycle Monodromy Theorem
**Status:** `UNCONDITIONAL_CHARACTERIZATION` · **Authority:** `PROPOSED`

If the projected cycle relations are bijections π_i, coherent sections are in bijection with fixed points of the monodromy permutation Π=π_{m-1}∘…∘π_0. Their number is |Fix(Π)|.

**Fingerprint:** `888e82f3d0ecb245c55f495e1a422074612365e8f174e7c35f5e3ac1d9bca66f`

## CLAIM-0288 — No Third Obstruction at Cycle Rank One
**Status:** `UNCONDITIONAL_CLASSIFICATION` · **Authority:** `PROPOSED`

Every finite incoherent unicyclic fiber-CSP has either support-pruning failure during tree absorption or a fixed-point-free cycle composition. No third obstruction occurs at incidence cycle rank one.

**Fingerprint:** `62ee2298eb813109e5e2c49a8ee17ffaa7d051a4e679e368cfbb21454827b990`

## CLAIM-0289 — Twisted-Cycle XOR Criterion
**Status:** `UNCONDITIONAL_CHARACTERIZATION` · **Authority:** `PROPOSED`

The UC03 twisted cycle has exactly two coherent sections when ⊕_i σ_i=0 and none when the xor is 1.

**Fingerprint:** `94907ba6ee37cecbb1f440ebd6a4eecfc5458f2c62f4a0d76d637af82916cb26`

## CLAIM-0290 — Arbitrarily Large Minimal Pure-Cycle Frustration
**Status:** `UNCONDITIONAL_CONSTRUCTION` · **Authority:** `PROPOSED`

For every n≥7 there is a finite K4-free n-constraint instance that is incoherent, every proper subsystem coherent, every value survives support pruning, and incidence cycle rank is one.

**Fingerprint:** `0bf379f5299c4b4fe781e84e67619746212718e90b97525680afa7fae955da56`

## CLAIM-0291 — Arc Consistency Is Insufficient in K4-Free Fiber Systems
**Status:** `UNCONDITIONAL_NEGATIVE_THEOREM` · **Authority:** `PROPOSED`

Support consistency on every variable-constraint incidence does not decide finite K4-free fiber coherence, even with binary domains and one incidence cycle.

**Fingerprint:** `a682389e34ee46514e1f706e418dc92cd02c1afea1cdd4ac7a174a5b210ff2fd`

## CLAIM-0292 — Support and Monodromy Frustration Are Orthogonal
**Status:** `UNCONDITIONAL_COMPOSITE` · **Authority:** `PROPOSED`

K4-free fiber coherence has independently necessary support-intersection and support-consistent monodromy obstruction families; neither cycle detection alone nor support pruning alone classifies minimal incoherence.

**Fingerprint:** `919a9e6191ca85d02f9dee1edcc464eedc87c38087faaa2149b10500b1d3b4a9`

## CLAIM-0293 — Finite Minimal-Core Cycle-Rank Trichotomy
**Status:** `UNCONDITIONAL_CLASSIFICATION_BOUNDARY` · **Authority:** `PROPOSED`

Every inclusion-minimal finite incoherent instance lies in exactly one branch: forest support-pruning, unicyclic support/fixed-point obstruction, or incidence cycle rank at least two. Any genuinely new mixed obstruction first appears in the multicyclic branch.

**Fingerprint:** `434c6145c1e183d8db14c9eafd28eae3c03c5aa6662de1975c1940fcc480e039`

## CLAIM-0294 — Refined Finite-Fiber #595 Close Trichotomy
**Status:** `UNCONDITIONAL_REDUCTION` · **Authority:** `PROPOSED`

A hypothetical #595 witness with a finite-fiber stable partition yields either a finite acyclic core, a finite unicyclic core, a finite multicyclic minimal core, or an exact coherent uncountably chromatic Berge-C3-free compression.

**Fingerprint:** `293923039710f91be8c831ad0b9d5fe065c754e7c627e5e7be6cf7ee61b77161`

## CLAIM-0295 — Page-Free Refined Close Trichotomy
**Status:** `UNCONDITIONAL_REDUCTION` · **Authority:** `PROPOSED`

The HG21 page-free unary-homogeneous induced witness satisfies the same four-way finite-fiber split as UC15.

**Fingerprint:** `50577f11178c86b12ad9332ce65211dde496cf3f340eb5784ea0a2bb080f7f92`

## CLAIM-0296 — Bounded-Feedback Exact Certification
**Status:** `UNCONDITIONAL_ALGORITHMIC` · **Authority:** `PROPOSED`

If every minimal incoherence core in a class has variable feedback ≤r and fibers ≤d, incoherence has a certificate of at most d^r acyclic empty-message proofs and is decidable in O(d^r poly(N)).

**Fingerprint:** `0176976a1cb35bbf3757266c48c6f0aba456c3fbb06e25365ea1b25b6e19f14b`

## CLAIM-0297 — Bounded Feedback Does Not Give a Helly Bound
**Status:** `UNCONDITIONAL_NEGATIVE_THEOREM` · **Authority:** `PROPOSED`

Bounded incidence feedback number does not imply any bounded local coherence test; failure already occurs at feedback number zero.

**Fingerprint:** `40ee51200ac8c6a23b8c29acf8671dd72ab034b55a7da75ca4a53d32e09d9bf9`

## CLAIM-0298 — Multicycle Interaction Quotient Target
**Status:** `UNPROVED_CHECKABLE_TARGET` · **Authority:** `PROPOSED`

Enumerate minimal K4-free multicyclic cores, tree-absorb them, record minimum feedback sets and cycle-space relations, and determine whether genuinely mixed multi-cycle obstructions exist.

**Fingerprint:** `31f9acd862d19771586065802969fa1c29bcc81c580ef8f80c812528b073c6a6`

## CLAIM-0299 — Permutation-Cycle Realization Generalization Target
**Status:** `UNPROVED_CHECKABLE_TARGET` · **Authority:** `PROPOSED`

Determine which finite permutation-labeled cycle CSPs have K4-free stable-partition graph realizations with no extra realized triangle types; generalize the binary xor family and characterize graph restrictions on monodromy.

**Fingerprint:** `96ad1aaa83278ff7baf5046daf8fe55d0fab85e63fb99e74824d0d25279d897a`
