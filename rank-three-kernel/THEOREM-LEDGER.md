# Rank-Three Kernel theorem/target ledger

This ledger preserves the exact source authority classes. `UNCONDITIONAL_*` means the source packet supplies a mathematical proof/derivation. Novelty and Lean status were both `UNRUN` throughout.

| ID | Status | Title | Claim / role |
|---|---|---|---|
| R3K01 | `UNCONDITIONAL_CLASSIFICATION` | Four-Kernel Classification for 2-Connected Cycle Rank Three | Suppression of degree-two paths leaves exactly Q4, T221, D22, or K4. |
| R3K02 | `UNCONDITIONAL_CHARACTERIZATION` | Exact Branch-Kernel Relation Reduction | A tree-absorbed block is coherent iff its branch-kernel binary CSP is solvable. |
| R3K03 | `UNCONDITIONAL_CONSTRUCTION` | K4-Free Arbitrary Binary-Relation Strip | Every finite binary relation is exactly realizable as a K4-free fiber strip. |
| R3K04 | `UNCONDITIONAL_CONSTRUCTION` | Complete-Graph Coloring Core | The q-color `K_(q+1)` inequality CSP is inclusion-minimal incoherent, cycle rank `q(q-1)/2`. |
| R3K05 | `UNCONDITIONAL_CONSTRUCTION` | Universal K4-Free Realization of Finite Binary CSPs | Every finite binary CSP has a polynomial-size exact K4-free fiber realization. |
| R3K06 | `UNCONDITIONAL_COMPLEXITY` | NP-Completeness of Finite K4-Free Fiber Coherence | NP-complete; hardness already with branch domains of size 3. |
| R3K07 | `UNCONDITIONAL_CHARACTERIZATION` | Q4 Kernel Intersection Criterion | Coherence iff the four path relations have nonempty common intersection. |
| R3K08 | `UNCONDITIONAL_CHARACTERIZATION` | Doubled-Square Kernel Reduction | D22 reduces to two parallel intersections plus a cycle fixed-point test. |
| R3K09 | `UNCONDITIONAL_CHARACTERIZATION` | Doubled-Triangle Kernel Join Criterion | T221 reduces to two parallel intersections plus a three-relation join. |
| R3K10 | `UNCONDITIONAL_CHARACTERIZATION` | K4 Kernel Exact CSP Criterion | K4 coherence is exactly satisfaction of its six binary edge relations. |
| R3K11 | `UNCONDITIONAL_CLASSIFICATION` | Complete Cycle-Rank-Three Structural Classification | The four kernel relation mechanisms exhaust rank three. |
| R3K12 | `UNCONDITIONAL_ALGORITHMIC` | Polynomial-Time Fixed-Rank-Three Coherence | Rank ≤3 is decidable in polynomial time in explicit relation-table size. |
| R3K13 | `UNCONDITIONAL_CONSTRUCTION` | Intrinsic K4 Pigeonhole Core on Three Colors | Four 3-valued variables with pairwise inequality form a minimal incoherent core. |
| R3K14 | `UNCONDITIONAL_ELEMENTARY` | Domain Three Is Minimal for the K4 Pigeonhole Core | Domain 2 cannot have the same one-edge-repair property; domain 3 suffices. |
| R3K15 | `UNCONDITIONAL_CONSTRUCTION` | K4-Free Realization of the Intrinsic K4 Core | The intrinsic K4 CSP has an exact K4-free graph realization preserving block deletion. |
| R3K16 | `UNCONDITIONAL_ENUMERATION` | Exact First- and Second-Order Deletion Profile | One deletion gives 6 solutions; adjacent pair 12; disjoint pair 18. |
| R3K17 | `UNCONDITIONAL_CHARACTERIZATION` | Pair-Deletion Profile Reconstructs Constraint Geometry | The 12/18 profile reconstructs `L(K4)`. |
| R3K18 | `UNCONDITIONAL_ENUMERATION` | Exact Violation Ledger of the Three-Color K4 Core | `N0=0, N1=36, N2=18, N3=24, N6=3`. |
| R3K19 | `UNCONDITIONAL_ENUMERATION` | General Complete-Graph Core Deletion Formulas | `q!`, `2q!`, `3q!` deletion counts and exact `N1,N2` formulas. |
| R3K20 | `UNCONDITIONAL_NEGATIVE_AND_POSITIVE` | Second-Order Repair Is the First Noncollapsed Geometric Invariant | First-order repair data collapse; second-order data recover incidence geometry in the K4 core. |
| R3K21 | `UNCONDITIONAL_COMPLEXITY` | Fixed-Cycle-Rank Tractability versus Unbounded NP-Completeness | `O(d^r poly(N))` for fixed rank/domain bound versus NP-complete unbounded rank. |
| R3K22 | `UNCONDITIONAL_REDUCTION` | Refined Finite-Fiber #595 Close Split through Rank Three | A #595 finite-fiber compression either has an exactly classifiable rank≤3 core, a rank≥4 core, or compactness/coherence branch. |
| R3K23 | `UNPROVED_CHECKABLE_TARGET` | Rank-Four Branch-Kernel Census Target | Enumerate/classify rank-four branch kernels and their repair geometry. |
| R3K24 | `UNPROVED_CHECKABLE_TARGET` | Higher-Order Repair Reconstruction Target | Determine the deletion order needed to reconstruct fixed rank-four kernels. |

## Exact source receipts

- Packet: `RANK-THREE-KERNEL-THEOREM-PACKET.md`, 29,492 bytes, SHA-256 `c3e9f3d3d527c5c06c9f8ec880f813ad1129fd0ff8c0009a0c7ac3d4707155b0`.
- Card ledger: `RANK-THREE-KERNEL-THEOREM-CARDS.jsonl`, 28,862 bytes, SHA-256 `c1e98dda8425dd1effe08c333502c364d1b2f5d78a7fcb1a725cc6e7acc21e87`.

The public extraction above does not silently upgrade the two targets, the novelty status, or the Lean status.