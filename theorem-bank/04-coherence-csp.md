# Coherence CSP theorem bank

Recovered from the canonical V2 registry. **Records:** 24. Registry authority/status are preserved and do not imply independent re-verification.

## CLAIM-0449 — Fiber-Coherence CSP Equivalence
**Status:** `UNCONDITIONAL_DEFINITIONAL` · **Authority:** `PROPOSED`

For a stable partition and K⊆R_P(G), let each type t have domain F_t and each type-hyperedge h have relation C_h of actual fiber-edge triples forming graph triangles. A triangle-coherent section of K is exactly a satisfying assignment of this CSP.

**Fingerprint:** `5f75c20acb4a7ba78d787c995541082e6cf86c410569720b58ff9101cbc49a0c`

## CLAIM-0450 — Coherence Factorization over Incidence Components
**Status:** `UNCONDITIONAL_ELEMENTARY` · **Authority:** `PROPOSED`

A fiber-coherence CSP has a global section iff every connected component of its variable-constraint incidence graph has a section.

**Fingerprint:** `10a529cd951f45c871b312f7ce20849d4156eeab0409d51e23c5db78f4531f83`

## CLAIM-0451 — Star Support-Intersection Theorem
**Status:** `UNCONDITIONAL_CHARACTERIZATION` · **Authority:** `PROPOSED`

If all constraints share one type t and are otherwise disjoint, with S_i the supported values of t in constraint i, then a coherent section exists iff ⋂_i S_i is nonempty.

**Fingerprint:** `261965a7eaa449e257dd8b65c45af77cfa1382f626861fa73f75b11d02bf3278`

## CLAIM-0452 — K4-Free Star-Support Universality
**Status:** `UNCONDITIONAL_CONSTRUCTION` · **Authority:** `PROPOSED`

Every set system {S_i:i∈I} of nonempty subsets of X is realizable as the support system of a K4-free star-shaped fiber-coherence instance whose shared fiber is indexed by X.

**Fingerprint:** `7cf3dc96348d10894b653f87ad8eeeccf9704e9c76572094cafd10eeb23ac466`

## CLAIM-0453 — Berge-Acyclic Coherence Frustration
**Status:** `UNCONDITIONAL_COUNTEREXAMPLE` · **Authority:** `PROPOSED`

There is a finite K4-free system with two type-hyperedges sharing one type, so its incidence graph is a tree, but the full system has no coherent section.

**Fingerprint:** `c5c4669cbaa683a0a4c5d37af349e8b9cef1d0c502b186e443a9efbd8bc9232b`

## CLAIM-0454 — Arbitrarily Large Minimal Acyclic Frustration
**Status:** `UNCONDITIONAL_CONSTRUCTION` · **Authority:** `PROPOSED`

For every n≥2 there is a finite K4-free star-shaped system with exactly n constraints that is unsatisfiable while every proper constraint subsystem is satisfiable.

**Fingerprint:** `7e989f1f763666302564cff026b4d12385af10b0ee73c367fa374279a6f7a29f`

## CLAIM-0455 — No Bounded Local Coherence Test
**Status:** `UNCONDITIONAL_NEGATIVE_THEOREM` · **Authority:** `PROPOSED`

For every finite m, a finite K4-free Berge-acyclic fiber system can have every subsystem of at most m constraints coherent while the full system is incoherent.

**Fingerprint:** `dc716243866f754098224507538d22aa89a3beb493218df22fb9dc01a20f5af5`

## CLAIM-0456 — Countable Compactness Failure with Infinite Fibers
**Status:** `UNCONDITIONAL_CONSTRUCTION` · **Authority:** `PROPOSED`

There is a countable K4-free star-shaped fiber system for which every finite subsystem has a coherent section but the whole system does not.

**Fingerprint:** `7e5cfc87aff6ca69334976865840c669d9748d7a9fa561e630923bf6b3d945a6`

## CLAIM-0457 — Finite-Fiber Coherence Compactness
**Status:** `UNCONDITIONAL_WITH_STANDARD_COMPACTNESS` · **Authority:** `PROPOSED`

If every domain F_t is finite and every finite constraint subsystem is coherent, the entire possibly infinite fiber-coherence CSP is coherent.

**Fingerprint:** `e2277737b78553a6120458e29914913260c90f4f06483a39304cafe035696205`

## CLAIM-0458 — Exact Fiber-Compactness Boundary
**Status:** `UNCONDITIONAL_COMPOSITE` · **Authority:** `PROPOSED`

Finite fibers satisfy compactness; countably infinite fibers do not, even for K4-free star-shaped Berge-acyclic systems.

**Fingerprint:** `db0e1fd1fc7072f9e3029215b12da835e76240b70897cc2ff742f94dd62cd849`

## CLAIM-0459 — Regular-Cardinal Frustration Spectrum
**Status:** `UNCONDITIONAL_CONSTRUCTION` · **Authority:** `PROPOSED`

For every infinite regular cardinal λ there is a K4-free star-shaped system of λ constraints whose every <λ subsystem is coherent while the full system is not.

**Fingerprint:** `a820aa2203fb99ec65413b16c9609419ed81419cd8c0a94a49fa4b70fdebc12d`

## CLAIM-0460 — Incidence-Tree Message Theorem
**Status:** `UNCONDITIONAL_ALGORITHMIC` · **Authority:** `PROPOSED`

For finite fiber-CSPs with incidence graph a tree, the standard inward support messages are exact: the CSP is coherent iff the root's incoming supported-value intersection is nonempty.

**Fingerprint:** `6d56f3a360d116c6a1ddd949ef33123cdd98b3b5b4e3792eade337b6a36f0c3f`

## CLAIM-0461 — Star Theorem as Message-Passing Specialization
**Status:** `UNCONDITIONAL_COROLLARY` · **Authority:** `PROPOSED`

On a star-shaped type hypergraph, CC12 reduces exactly to the support-intersection criterion CC03.

**Fingerprint:** `c1974a0d4845dcac4f536185a9d7d0cb2e6811b9af2c2f6bae9a2e14751108e6`

## CLAIM-0462 — Polynomial-Time Acyclic Coherence
**Status:** `UNCONDITIONAL_ALGORITHMIC` · **Authority:** `PROPOSED`

A finite fiber-coherence CSP with acyclic incidence graph is decidable, and a section reconstructible, in time polynomial in the explicitly listed domain and relation sizes.

**Fingerprint:** `b86746ed5e5462b9c91d25e5e6049a4adfb005b1d73e636d4d3007c1fff68543`

## CLAIM-0463 — Minimal Frustration Core Certificate
**Status:** `UNCONDITIONAL_ELEMENTARY` · **Authority:** `PROPOSED`

Every finite incoherent fiber system has an inclusion-minimal incoherent constraint subsystem K such that K-h is satisfiable for every h∈E(K).

**Fingerprint:** `1a767493ac9c3b556b49dd16c2763ca5f22a9ff145e292251234879f1124199d`

## CLAIM-0464 — Cycle-or-Pruning Obstruction Dichotomy
**Status:** `UNCONDITIONAL_ALGORITHMIC` · **Authority:** `PROPOSED`

A finite incoherent system either has a cycle in its incidence graph, or is a forest whose exact message computation produces an empty root intersection, yielding an acyclic frustration certificate.

**Fingerprint:** `6587fe83a7fc380942ee272132d70f259059d1e0f007463c642a6efb306ba430`

## CLAIM-0465 — Finite-Fiber Exact-Compression Dichotomy
**Status:** `UNCONDITIONAL_WITH_STANDARD_COMPACTNESS` · **Authority:** `PROPOSED`

For a stable partition with finite nonempty edge fibers, either some finite realized-type subsystem has no coherent section, or the full realized-type hypergraph has one and tc(G)=χ(R_P(G)); in a K4-free graph the latter also forces Berge-C3-freeness.

**Fingerprint:** `5a70143f438bf4496b5e53f98443cc91985d6993175ec1dbf4d4bbc897483307`

## CLAIM-0466 — Unique-Fiber Exactness
**Status:** `UNCONDITIONAL_ELEMENTARY` · **Authority:** `PROPOSED`

If every nonempty part-pair fiber has exactly one graph edge, the full realized-type hypergraph has a unique coherent section and tc(G)=χ(R_P(G)); after isolated type deletion it is naturally the triangle hypergraph of the triangle core.

**Fingerprint:** `3dad8c42dd1eb4ba8364abbe770e888c096844694b2dc06590cc186dda6134a6`

## CLAIM-0467 — Finite-Obstruction or Compressed #595 Witness
**Status:** `UNCONDITIONAL_REDUCTION` · **Authority:** `PROPOSED`

For a hypothetical #595 witness and any stable partition with finite edge fibers, either a finite type subsystem is coherence-frustrated, or R_P(G) is an uncountably chromatic Berge-C3-free coherently sectioned 3-uniform hypergraph with tc(G)=χ(R_P(G)).

**Fingerprint:** `fadd2dbc00429c3e016cfffeaa411f7a4adfe66ee566b4127e0c2448ee5c915c`

## CLAIM-0468 — Page-Free Finite-Fiber Close Dichotomy
**Status:** `UNCONDITIONAL_REDUCTION` · **Authority:** `PROPOSED`

The HG21 page-free unary-homogeneous induced witness obeys the same finite-frustration-or-exact-compression dichotomy as CC19 for every stable partition with finite fibers.

**Fingerprint:** `a1ed825d091b02b59318814fc816a12a3d88a1fffb7f15e768a6437ac5fd63a9`

## CLAIM-0469 — Finite Frustration-Number Spectrum
**Status:** `UNCONDITIONAL_CONSTRUCTION` · **Authority:** `PROPOSED`

Among finite K4-free star-shaped systems, every frustration number 2,3,4,...,∞ occurs.

**Fingerprint:** `ff7312fd3b0bb93373137960432c56051b3222484fda1e049fcb47bd2403a0d0`

## CLAIM-0470 — Acyclicity Gives Algorithms, Not Automatic Coherence
**Status:** `UNCONDITIONAL_COMPOSITE` · **Authority:** `PROPOSED`

Berge acyclicity does not imply coherence, even in finite K4-free systems; it does provide an exact polynomial-time message criterion.

**Fingerprint:** `caa74adcb832a876820ae712d8cea6251eb4e72dcc36d4caf63953a4e55a1fdb`

## CLAIM-0471 — Two Orthogonal K4-Free Frustration Modes
**Status:** `UNCONDITIONAL_CLASSIFICATION_BOUNDARY` · **Authority:** `PROPOSED`

The proved local mechanisms are support frustration on Berge-acyclic stars and cycle-coherence frustration from forbidden coherent Berge-C3s. Any complete classification must track both.

**Fingerprint:** `ff152370d81623c58723a91c4029fe11f5a814e0ed2b9d9d10a53741b8554c9d`

## CLAIM-0472 — Minimal Fiber-Coherence Classification Target
**Status:** `UNPROVED_CHECKABLE_TARGET` · **Authority:** `PROPOSED`

Enumerate finite K4-free fiber-CSPs by incidence cycles, domain sizes, relations, message-pruning cores, coherent/incoherent Berge cycles, and frustration number; classify minimal obstructions and test whether all arise from support, cycle, or a genuinely mixed third family.

**Fingerprint:** `a22adff1634aa8fa73a2be98830ab4748669d3d108331c0b94850f6c0968f753`
