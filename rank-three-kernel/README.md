# Rank-Three Kernel / K4-Free Fiber-Coherence Theorem Bank

**Author:** Jared Wilder  
**Source date:** 2026-08-04  
**Public release:** 2026-09-11

This is a scope-preserving public extraction of the pure mathematics in the Rank-Three Kernel self-growth campaign.

## Authority boundary

- The source packet contains **24 theorem/target cards**: **22 unconditional results/reductions** and **2 explicitly unproved checkable targets**.
- Historical novelty was **UNRUN** in the source packet. This release makes **no historical-novelty claim**.
- Lean formalization was **UNRUN** in the source packet. `UNCONDITIONAL_*` below means the campaign supplied an ordinary mathematical argument; it does **not** mean Lean-kernel certification.
- Erdős #500, #595 and #738 remain open. Nothing here claims to close them.
- Source packet SHA-256: `c3e9f3d3d527c5c06c9f8ec880f813ad1129fd0ff8c0009a0c7ac3d4707155b0`.
- Source theorem-card JSONL SHA-256: `c1e98dda8425dd1effe08c333502c364d1b2f5d78a7fcb1a725cc6e7acc21e87`.

## Flagship classification

Let `B` be a finite simple 2-connected graph with cyclomatic number

`|E(B)| - |V(B)| + 1 = 3`.

Suppress every maximal path whose internal vertices have degree two. The resulting loopless 2-connected multigraph is isomorphic to exactly one of four kernels:

1. `Q4`: two vertices joined by four parallel edges;
2. `T221`: a triangle with edge multiplicities `2,2,1`;
3. `D22`: a four-cycle with two opposite edges doubled;
4. the simple graph `K4`.

The proof is the degree-excess identity

`sum_v (deg(v)-2) = 2|E|-2|V| = 4`,

which bounds the suppressed kernel by four vertices; the 2-, 3-, and 4-vertex cases then force exactly the four types above.

For tree-absorbed fiber-coherence blocks, every suppressed path can be replaced by its exact endpoint relation. Consequently the four kernels give exactly four relation mechanisms:

- `Q4` → four-way relation intersection;
- `T221` → two parallel intersections followed by a ternary join;
- `D22` → two parallel intersections followed by cycle monodromy / fixed point;
- `K4` → a four-variable, six-relation binary CSP.

There is no fifth branch-kernel mechanism at cycle rank three.

## Universal K4-free CSP realization

For finite sets `A,B` and any binary relation `R ⊆ A×B`, the packet gives a finite K4-free stable-partition graph gadget whose boundary choices extend to a coherent section exactly for pairs in `R`. The construction uses six stable parts and a four-triangle path gadget for each allowed pair.

Gluing one such private strip per binary constraint gives:

> **Every finite binary CSP has a polynomial-size realization as the exact boundary projection of a finite K4-free fiber-coherence system.**

A direct reduction from graph 3-COLORING then yields the packet's complexity statement:

> Finite K4-free fiber coherence is NP-complete when cycle rank is unbounded; NP-hardness already holds with branch domains of size three.

For fixed cyclomatic rank `r` and maximum fiber domain `d`, feedback conditioning gives `O(d^r poly(N))` time. Thus the same framework records a fixed-rank tractability / unbounded-rank NP-completeness boundary.

## The intrinsic K4 pigeonhole core

Take four variables, domain `{0,1,2}`, and inequality on all six pairs. This CSP is inclusion-minimal incoherent: four variables cannot receive pairwise-distinct values from three colors, while deleting any one inequality permits the missing pair to share a color.

The exact repair profile is:

- delete one constraint → `6` solutions;
- delete two adjacent K4 edges → `12` solutions;
- delete two disjoint K4 edges → `18` solutions.

Hence the second-order deletion profile reconstructs the line graph `L(K4)` and distinguishes adjacent from disjoint constraints. The assignment violation ledger is

`N0=0, N1=36, N2=18, N3=24, N6=3`,

with all other `Nj=0`.

For the general `q`-color `K_(q+1)` core:

- one-edge deletion has `q!` solutions;
- two adjacent-edge deletions have `2q!` solutions;
- two disjoint-edge deletions have `3q!` solutions;
- `N1 = C(q+1,2) q!`;
- `N2 = 3 C(q+1,4) q!`.

## Erdős #595 reduction boundary

For a stable finite-fiber compression of a hypothetical Erdős #595 witness, the packet records the following reduction: either

1. a finite minimal incoherence core has cycle rank at most three and is handled by the forest/unicyclic/theta-cactus/rank-three mechanisms;
2. a finite minimal core has cycle rank at least four; or
3. every finite subsystem coheres and compactness gives a full coherent section, producing the corresponding hypergraph compression.

This is a **reduction**, not a solution of Erdős #595.

## Exact next wall

The two cards intentionally left open are:

- **R3K23 — Rank-Four Branch-Kernel Census Target** (`UNPROVED_CHECKABLE_TARGET`)
- **R3K24 — Higher-Order Repair Reconstruction Target** (`UNPROVED_CHECKABLE_TARGET`)

Cycle rank four is therefore the first fixed-rank branch-kernel regime not classified by this packet.

See `THEOREM-LEDGER.md` for the complete 24-card status ledger.