# Permutation Gluing theorem bank

Recovered from the canonical V2 registry. **Records:** 22. Registry authority/status are preserved and do not imply independent re-verification.

## CLAIM-0425 — Constraint-Deletion Excitation Identity
**Status:** `UNCONDITIONAL_ELEMENTARY` · **Authority:** `PROPOSED`

For finite CSP C={C_1,...,C_m} on finite assignment space Ω, let ν(a) be violated constraints and N_j=#{a:ν(a)=j}. Then Σ_i |Sol(C-{C_i})|=mN_0+N_1.

**Fingerprint:** `eb4ead5acd1a5d77f0514990a453c6850e6962135c9f9d9b68f560e3e62de0cc`

## CLAIM-0426 — Higher Deletion Hierarchy
**Status:** `UNCONDITIONAL_ELEMENTARY` · **Authority:** `PROPOSED`

For 0≤r≤m, summing the solution counts after deleting r constraints equals Σ_{a:ν(a)≤r} C(m-ν(a),r-ν(a)).

**Fingerprint:** `9c74155019cabe73dc82e9c984729c5476cadf916f21d3856277f36008dfe265`

## CLAIM-0427 — Exact Constraint-Extension Repair Operator
**Status:** `UNCONDITIONAL_ELEMENTARY` · **Authority:** `PROPOSED`

For a new constraint H, ρ(H|C)=min{ν_C(a):a satisfies H} is exactly the minimum number of old constraints that must be deleted to make C∪{H} satisfiable.

**Fingerprint:** `4f6e88c5a90898d53e9c4a4af575f33453fa028f3cc83d6b8c564791d1cab027`

## CLAIM-0428 — Finite-Domain Permutation-Cycle Realization
**Status:** `UNCONDITIONAL_CONSTRUCTION` · **Authority:** `PROPOSED`

For d≥2, n≥7, and π_0,...,π_{n-1}∈S_d, there is a finite K4-free stable-partition graph realization whose consecutive/distance-two fibers implement those permutations and whose coherent sections are in bijection with fixed points of the monodromy Π=π_{n-1}∘...∘π_0.

**Fingerprint:** `5ff4920266f69c4ec0ee765047d648c5fd8c5c697bc86c6f11bb7908ce9aa422`

## CLAIM-0429 — Boundary-Projection Gluing Theorem
**Status:** `UNCONDITIONAL_ELEMENTARY` · **Authority:** `PROPOSED`

If finite CSPs share exactly one boundary variable x and otherwise have disjoint internal variables, their union is satisfiable iff their boundary-support sets have nonempty intersection; global solution count is the sum over common boundary values of the product of local multiplicities.

**Fingerprint:** `044031bdd7f15c4d3a4756fbb0f1392f0b8245564c4688027e6979c095b6ee97`

## CLAIM-0430 — Permutation-Cycle Bouquet Theorem
**Status:** `UNCONDITIONAL_CHARACTERIZATION` · **Authority:** `PROPOSED`

Permutation-cycle gadgets sharing exactly one fiber variable are jointly coherent iff the fixed-point sets of their monodromies have nonempty intersection.

**Fingerprint:** `0a63e4b79645efa991cb6aea56a3193c77bd07b01d2710f1ba0bdaa741d3057f`

## CLAIM-0431 — First Pure Mixed Multicycle Obstruction
**Status:** `UNCONDITIONAL_CONSTRUCTION` · **Authority:** `PROPOSED`

There is a finite K4-free cycle-rank-two fiber system in which each cycle subsystem is coherent, all relations are bijections and all values support-consistent, but the union is incoherent.

**Fingerprint:** `1189ab1a49505a01f2277a58cad2b2d2a7342bca0faf40a5cb224cef45488ee1`

## CLAIM-0432 — Arbitrarily Large Minimal Monodromy Bouquets
**Status:** `UNCONDITIONAL_CONSTRUCTION` · **Authority:** `PROPOSED`

For every r≥2 there is a K4-free bouquet of r permutation cycles whose every proper subbouquet is coherent but full bouquet incoherent, with bijective relations and local support consistency everywhere.

**Fingerprint:** `1df958bc5360dbb0a1b4c7c312540abe83c38058cb93c0a7a613d151545217ed`

## CLAIM-0433 — No Helly Bound for Pure Monodromy Coherence
**Status:** `UNCONDITIONAL_NEGATIVE_THEOREM` · **Authority:** `PROPOSED`

No finite Helly number exists for finite K4-free fiber systems even within support-consistent bouquets of permutation cycles.

**Fingerprint:** `0749a200944e1121c06996c221ba9cbf501c8231270d4a5682d9cd539544b462`

## CLAIM-0434 — Minimal-Incoherence Near-Solution Ledger
**Status:** `UNCONDITIONAL_COROLLARY` · **Authority:** `PROPOSED`

Every inclusion-minimal incoherent m-constraint CSP has a near-solution for each constraint violating that constraint alone, and N_1=Σ_i|Sol(C-{C_i})|≥m.

**Fingerprint:** `27c8d3d3151c985642e621e4f15db7403d488d7c7ae0819bc0778ee6b9c8b45e`

## CLAIM-0435 — Cycle-Extension Repair Formula
**Status:** `UNCONDITIONAL_ELEMENTARY` · **Authority:** `PROPOSED`

For a coherent permutation-cycle bouquet with fixed sets S_i, adding a new cycle with fixed set T requires deleting exactly min_{a∈T} #{i:a∉S_i} old cycle blocks to restore coherence.

**Fingerprint:** `6498633a561048206d483cba6073ae4bd6f0157a37223c1407bc0b821670d86d`

## CLAIM-0436 — Bouquet Deletion-Spectrum Identity
**Status:** `UNCONDITIONAL_ELEMENTARY` · **Authority:** `PROPOSED`

For fixed sets S_1,...,S_m⊆D, the sum over all r-deletions of the remaining intersection sizes equals Σ_{a∈D} C(m-ν(a),r-ν(a)), where ν(a)=#{i:a∉S_i}.

**Fingerprint:** `ce72a4fbfd2330646736cbe28c375be42513e9552b15c6292bfa646e93df1731`

## CLAIM-0437 — Exact Collision Penalty for Cycle Bouquets
**Status:** `UNCONDITIONAL_CHARACTERIZATION` · **Authority:** `PROPOSED`

Bouquet incoherence is exactly empty intersection of monodromy fixed sets; the block-deletion repair number is min_a #{i:a∉Fix(Π_i)}.

**Fingerprint:** `5f32688e64d84882b689b12c09b10649bee003db6c657d08caeccf79f3cc64bd`

## CLAIM-0438 — Cactus Block-Message Theorem
**Status:** `UNCONDITIONAL_ALGORITHMIC` · **Authority:** `PROPOSED`

A finite fiber-CSP with cactus incidence graph is decided exactly by block-cut-tree message passing: tree blocks use CC12 and cycle blocks use UC01/relational composition. Coherence is equivalent to the root retaining a value.

**Fingerprint:** `56fe0403e24c753630cf2fd3732c76eb1c37d8970a2ce08c4e314e208774aacf`

## CLAIM-0439 — Cactus Obstruction Classification
**Status:** `UNCONDITIONAL_CLASSIFICATION` · **Authority:** `PROPOSED`

Every finite incoherent cactus-incidence fiber CSP has an exact block-message certificate; there is no further obstruction mechanism inside the cactus class.

**Fingerprint:** `7ba930edd1ec4eeb007707e4c6f80cdc9ccd9507dcea6c3068279fc6bcdbd322`

## CLAIM-0440 — Pure Monodromy Cactus Universality
**Status:** `UNCONDITIONAL_CONSTRUCTION` · **Authority:** `PROPOSED`

Every finite family of subsets S_i⊆D whose complements do not have size one can be represented as the boundary-support family of a K4-free cactus of permutation-cycle blocks.

**Fingerprint:** `d90f4acc6f10e14e9a6a6011de9952fbc479150a143d481699ef597aee1d34f8`

## CLAIM-0441 — No Unclassified Core in the Cactus Regime
**Status:** `UNCONDITIONAL_CLASSIFICATION_BOUNDARY` · **Authority:** `PROPOSED`

Any inclusion-minimal finite incoherent fiber CSP not classified by forest, unicyclic or cactus message theorems contains a 2-connected incidence block of cycle rank at least two.

**Fingerprint:** `f0442fe516052e4ad36ad270a07437d065f9256a203d990689352806f15bb1e3`

## CLAIM-0442 — Refined Finite-Fiber #595 Close Split
**Status:** `UNCONDITIONAL_REDUCTION` · **Authority:** `PROPOSED`

A finite-fiber stable compression of a hypothetical #595 witness yields either a finite cactus core with explicit message failure, a finite minimal core containing a 2-connected cycle-rank≥2 block, or a full coherent exact uncountably chromatic Berge-C3-free hypergraph compression.

**Fingerprint:** `a29b87e2947d42653f30c66f8754e3cc5c9b764e0d88ffc1a33c2f2c0e7b2b50`

## CLAIM-0443 — Deletion-Debt Certificate for Minimal Cores
**Status:** `UNCONDITIONAL_COROLLARY` · **Authority:** `PROPOSED`

For every inclusion-minimal incoherent m-constraint core, the vector (|Sol(C-C_i)|)_i is a positive-integer deletion spectrum whose sum equals the number of assignments violating exactly one constraint; it is an isomorphism invariant.

**Fingerprint:** `794527d90a026323a0d7be05d50f4480340fcb8131d51e878689a94cbcf959fb`

## CLAIM-0444 — Biconnected Multicycle Collision Census Target
**Status:** `UNPROVED_CHECKABLE_TARGET` · **Authority:** `PROPOSED`

Enumerate minimal K4-free cores with one 2-connected cycle-rank≥2 incidence block; record deletion spectrum, feedback certificates, cycle monodromies and overlap patterns, and classify the first intrinsically biconnected obstructions.

**Fingerprint:** `a5740572e0db52366302b62c6e8556671e6a95966e761196a88436c7bfa5103e`

## CLAIM-0445 — Core-Extension Slack
**Status:** `UNCONDITIONAL_ELEMENTARY` · **Authority:** `PROPOSED`

For coherent C plus new constraint H, extension slack σ=ρ(H|C) is exactly the old-block deletion distance needed to restore coherence; σ=0 preserves coherence, σ=1 requires exactly one deletion.

**Fingerprint:** `1cde4ddb44a3973236c3743c40bbc5cc3f358456636549577984df6753bf95a5`

## CLAIM-0446 — Collision-or-Slack Program for 2-Connected Cores
**Status:** `UNPROVED_CHECKABLE_TARGET` · **Authority:** `PROPOSED`

Build minimal biconnected multicycle cores by constraint extension and test whether every first intrinsic obstruction is either an overlap collision of coherent cycle projections or incurs positive extension slack before final closure.

**Fingerprint:** `5d5121706a349ce97376fea007122d421b5350fd7c9082f4cf2687db50dfff3f`
