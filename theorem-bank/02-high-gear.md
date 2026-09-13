# High Gear theorem bank

Recovered from the canonical V2 registry. **Records:** 23. Registry authority/status are preserved and do not imply independent re-verification.

## CLAIM-0300 — Vertex-Partition Compression Inequality
**Source ID:** `HG01` · **Status:** `UNCONDITIONAL_ELEMENTARY` · **Authority:** `PROPOSED`

Let G be a graph, let P be a partition of V(G), and let μ be a cardinal for which |P|≤2^μ. Then tc(G)≤μ+sup_P tc(G[P]).

**Fingerprint:** `01a0328786c46fea94f6171ed9548b71818cc7030136d0fbc62b03c9ef336e83`

## CLAIM-0301 — Edge-Partition Self-Similarity
**Source ID:** `HG02` · **Status:** `UNCONDITIONAL_ELEMENTARY` · **Authority:** `PROPOSED`

Let κ be infinite and tc(G)>κ. If E(G)=⋃_{i∈I}F_i with |I|≤κ, then tc((V(G),F_i))>κ for at least one i.

**Fingerprint:** `2346b23e315aff06869c7e9c58d9acd8440d9a9eba7565678deb65a202e0cd2a`

## CLAIM-0302 — Successor-Length Adaptive Edge-Null Surgery
**Source ID:** `HG03` · **Status:** `UNCONDITIONAL_TRANSFINITE` · **Authority:** `PROPOSED`

Let κ be infinite, tc(G)>κ, and choose F_α adaptively for α<κ^+ with tc((V(G),F_α))≤κ. For G_α=G-⋃_{β<α}F_β, tc(G_α)>κ for every α<κ^+.

**Fingerprint:** `1630dbe85516a52bd4d56f5011f25bfd90cd86fba66a000c2d9f9b325d25f055`

## CLAIM-0303 — The 2^κ-Complete Induced-Null Vertex Ideal
**Source ID:** `HG04` · **Status:** `UNCONDITIONAL_ELEMENTARY` · **Authority:** `PROPOSED`

For infinite κ define J_κ(G)={A⊆V(G):tc(G[A])≤κ}. Then J_κ(G) is downward closed and closed under unions of at most 2^κ members.

**Fingerprint:** `141dd692f6dc59606005f923a4999085106091ad95fe8825366b0c4a6dbae3d5`

## CLAIM-0304 — Induced-Null Vertex Deletion Persistence
**Source ID:** `HG05` · **Status:** `UNCONDITIONAL_ELEMENTARY` · **Authority:** `PROPOSED`

If tc(G)>κ and A∈J_κ(G), then tc(G-A)>κ.

**Fingerprint:** `407d6c1e6032df7bf4d8fc10614acaabb7dd196d374bf3e216ea3b735785cc9f`

## CLAIM-0305 — 2^κ-Cell Vertex Indivisibility
**Source ID:** `HG06` · **Status:** `UNCONDITIONAL_ELEMENTARY` · **Authority:** `PROPOSED`

Every partition of V(G) into at most 2^κ cells has a cell P satisfying tc(G[P])>κ whenever tc(G)>κ.

**Fingerprint:** `31a18103cd4f9a2ddc78bc22e98f28ecc2ccfd0c3bf9da30746c2bd3f9d8c9eb`

## CLAIM-0306 — Finite/Small Edge-Profile Canonization
**Source ID:** `HG07` · **Status:** `UNCONDITIONAL_ELEMENTARY` · **Authority:** `PROPOSED`

If tc(G)>κ and a family of edge maps has combined profile space of cardinality at most κ, some common profile class F⊆E(G) satisfies tc((V(G),F))>κ.

**Fingerprint:** `19173e5f919a27bb09051286f832b416c72e9bebf2de705d08d7b3dd89bb366b`

## CLAIM-0307 — Simultaneous Unary Canonization
**Source ID:** `HG08` · **Status:** `UNCONDITIONAL_ELEMENTARY` · **Authority:** `PROPOSED`

For every family of at most κ vertex maps, each with range size at most κ, there is U⊆V(G) with tc(G[U])>κ on which every map is constant.

**Fingerprint:** `731941bcec300e19cfe35383c4037f658d2fb515195ad927686de97b417d9041`

## CLAIM-0308 — Successor-of-2^κ Adaptive Vertex-Null Surgery
**Source ID:** `HG09` · **Status:** `UNCONDITIONAL_TRANSFINITE` · **Authority:** `PROPOSED`

Let θ=(2^κ)^+ and tc(G)>κ. Adaptively delete induced κ-null vertex sets A_α for α<θ. Every proper-stage residual remains κ-positive.

**Fingerprint:** `04c6b8bad95d2ed504e24707c0c0e31d36a04dfc09ca54864d5761e6550dcec7`

## CLAIM-0309 — Dual Surgery Horizons
**Source ID:** `HG10` · **Status:** `UNCONDITIONAL_COROLLARY` · **Authority:** `PROPOSED`

Adaptive deletion of κ-null edge sets is guaranteed through stages below κ^+, while induced κ-null vertex deletion is guaranteed through stages below (2^κ)^+.

**Fingerprint:** `d381721b88cd7234c2214dc37e363aba2e7cd41cf2fe7b2a2126cee9b1de7e9b`

## CLAIM-0310 — Unary-Profile Sterility Boundary
**Source ID:** `HG11` · **Status:** `UNCONDITIONAL_NEGATIVE_THEOREM` · **Authority:** `PROPOSED`

No family of at most κ unary κ-valued invariants can decompose a κ-positive graph into induced κ-null profile classes.

**Fingerprint:** `15f4f90d1baf22a8051e3f4fec30287b3ac38d4b522b9bb4a15e743e1db0bebc`

## CLAIM-0311 — Canonized High-Chromatic Link Extraction
**Source ID:** `HG12` · **Status:** `UNCONDITIONAL_ELEMENTARY` · **Authority:** `PROPOSED`

If G is K4-free with tc(G)>κ, there are v and a triangle-free induced L⊆N_G(v) with χ(L)>κ such that v and every vertex of L share one common unary profile for any prescribed ≤κ family of κ-valued vertex maps.

**Fingerprint:** `f3889f19b970f917a49d63ef2c077e550acb17989134c756ab7c9500df308de4`

## CLAIM-0312 — Edge-Profile Homogeneous Link Extraction
**Source ID:** `HG13` · **Status:** `UNCONDITIONAL_ELEMENTARY` · **Authority:** `PROPOSED`

Under HG07 in a K4-free graph, a common edge-profile class yields a spanning κ-positive subgraph containing a triangle-free forward link of chromatic number >κ.

**Fingerprint:** `39cde76fcf7c6b95a2f7bcc3f8a6712e7aca500844c08c00dc0f1c6d2e3adeae`

## CLAIM-0313 — Closed-Neighborhood Escape Beyond 2^κ
**Source ID:** `HG14` · **Status:** `UNCONDITIONAL_ELEMENTARY` · **Authority:** `PROPOSED`

If G is K4-free with tc(G)>κ and |S|≤2^κ, then tc(G-N_G[S])>κ.

**Fingerprint:** `a454888613d18b3a11e934268fcc093d869b250d6f33a785ad9bc3ab6c3197e8`

## CLAIM-0314 — Massive Vertex-Disjoint High-Link Cone Packing
**Source ID:** `HG15` · **Status:** `UNCONDITIONAL_TRANSFINITE` · **Authority:** `PROPOSED`

Let θ=(2^κ)^+. Every K4-free κ-positive graph contains θ pairwise vertex-disjoint induced cones K1∨L_α where each L_α is triangle-free and χ(L_α)>κ.

**Fingerprint:** `9ac6c323339e504a3a6fecb058288be3b18e520108ec529aaa3ffc08e5ce6c33`

## CLAIM-0315 — Massive Pairwise-Anticomplete Critical-Cone Packing
**Source ID:** `HG16` · **Status:** `UNCONDITIONAL_WITH_STANDARD_COMPACTNESS` · **Authority:** `PROPOSED`

For θ=(2^κ)^+ and any f:θ→ω, a K4-free κ-positive graph contains pairwise anticomplete induced cones K1∨Q_α with each Q_α finite, triangle-free, vertex-critical, and χ(Q_α)>f(α).

**Fingerprint:** `f810b6898840cd6fdeef0c02360f608391133d20dce1b804216564e33d121116`

## CLAIM-0316 — Conditional Massive Prescribed Tree-Cone Packing
**Source ID:** `HG17` · **Status:** `CONDITIONAL_ON_ERDOS_738_SEQUENCE` · **Authority:** `PROPOSED`

Conditional on a prescribed sequence of #738 finite-tree statements, every K4-free κ-positive graph contains θ pairwise anticomplete induced cones K1∨T_α.

**Fingerprint:** `5c324275a06836173e1a66506e02b5274c977229e4b722fd388b86f8b2e3b2e4`

## CLAIM-0317 — Complete Stable-Certificate Page Eviction
**Source ID:** `HG18` · **Status:** `UNCONDITIONAL_ELEMENTARY` · **Authority:** `PROPOSED`

For ≤κ maximal spanning triangle-free subgraphs, choose their common omitted edge xy and stable certificate pages W_i. Deleting {x,y} and all W_i leaves a κ-positive residual.

**Fingerprint:** `53362fd89b8031fc1478aa90e3e14cd9b8bb14a03ec4eb7fd2234f7f2f9c4dcb`

## CLAIM-0318 — Successor-of-2^κ Common-Book Eviction Process
**Source ID:** `HG19` · **Status:** `UNCONDITIONAL_TRANSFINITE` · **Authority:** `PROPOSED`

Iterating HG18 below θ=(2^κ)^+ preserves κ-positivity at every proper stage.

**Fingerprint:** `c0edd9ed19b53faff513fda896125e9fa4593f15897437a8af6eff0014bd6c70`

## CLAIM-0319 — Canonized Pairwise-Anticomplete Critical-Cone Packing
**Source ID:** `HG20` · **Status:** `UNCONDITIONAL_WITH_STANDARD_COMPACTNESS` · **Authority:** `PROPOSED`

Under HG08 in a K4-free graph, one common unary profile contains (2^κ)^+ pairwise anticomplete induced critical cones meeting arbitrary prescribed finite chromatic thresholds.

**Fingerprint:** `65ba8384e92f4d24c1ac5b3d4d7c77c8b33da225445ed0210d6d477b48fc30e8`

## CLAIM-0320 — Canonized Page-Free Subwitness
**Source ID:** `HG21` · **Status:** `UNCONDITIONAL_ELEMENTARY` · **Authority:** `PROPOSED`

Fix ≤κ maximal spanning triangle-free layers and ≤κ unary κ-valued maps. There is an induced κ-positive subgraph avoiding the common omitted-edge endpoints and all certificate pages while all unary maps are constant on it.

**Fingerprint:** `5d9b6ceda4012b072c908a64d4f24370016218b69822dc05c60331c30a948aec`

## CLAIM-0321 — Fully Canonized Page-Free Cone Civilization
**Source ID:** `HG22` · **Status:** `UNCONDITIONAL_WITH_STANDARD_COMPACTNESS` · **Authority:** `PROPOSED`

The HG21 page-free common-profile subwitness contains (2^κ)^+ pairwise anticomplete induced critical cones, all vertices sharing the same unary profile.

**Fingerprint:** `fbbd9291a4090d674aa8b370f2ab50e0d8ae76134d2622d697b469c45d3a9104`

## CLAIM-0322 — Conditional Universal Finite-Tree Cone Civilization
**Source ID:** `HG23` · **Status:** `CONDITIONAL_ON_FULL_ERDOS_738` · **Authority:** `PROPOSED`

Assume Erdős #738 holds for every finite tree. Every K4-free κ-positive graph contains a pairwise anticomplete family of θ induced cones in which every finite tree occurs as the cone base θ times.

**Fingerprint:** `60eeed25728be52340e2c829e91cb8f0685d7c2ddb8107e4b79748291f0ac5d5`
