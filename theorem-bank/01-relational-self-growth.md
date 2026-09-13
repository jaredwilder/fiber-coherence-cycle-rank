# Relational Self Growth theorem bank

Recovered from the canonical V2 registry. **Records:** 26. Registry authority/status are preserved and do not imply independent re-verification.

## CLAIM-0254 — Quotient-Lift Compression Theorem
**Source ID:** `RG01` · **Status:** `UNCONDITIONAL_ELEMENTARY` · **Authority:** `PROPOSED` · **Verification:** `INHERITED_FROM_V1_AUDIT`

Let \(\mathcal P\) be a partition of \(V(G)\), and let \(Q_{\mathcal P}\) be the quotient graph whose vertices are the parts and whose edges are the pairs of parts joined by at least one edge of \(G\). Let \(bc(Q_{\mathcal P})\) be the least cardinality of a cover of \(E(Q_{\mathcal P})\) by bipartite subgraphs. Then \(tc(G)\le bc(Q_{\mathcal P})+\sup_{P\in\mathcal P}tc(G[P])\).

**Fingerprint:** `b028a010fc071d345303c9135533d85081fa7d1bc4e82f63af457e6c4f49d0ff`

## CLAIM-0255 — Universal Quotient Realization by a Matching
**Source ID:** `RG02` · **Status:** `UNCONDITIONAL_CONSTRUCTION` · **Authority:** `PROPOSED` · **Verification:** `INHERITED_FROM_V1_AUDIT`

Every simple graph \(Q\) is the quotient graph of a matching under a partition into stable sets.

**Fingerprint:** `0eb9f6d5c40b4b8a79f8009c9a86a6261d17992d06c02d349d639000d69b685d`

## CLAIM-0256 — Adjacency Pair-Homogeneity Impossibility
**Source ID:** `RG03` · **Status:** `UNCONDITIONAL_NEGATIVE_THEOREM` · **Authority:** `PROPOSED` · **Verification:** `INHERITED_FROM_V1_AUDIT`

Let \(\kappa\) be infinite and let \(G\) be \(K_4\)-free with \(tc(G)>\kappa\). For the binary pair map \(a(\{x,y\})=\mathbf 1_{xy\in E(G)}\), there is no \(U\subseteq V(G)\) such that \(tc(G[U])>\kappa\) and \(a\) is constant on \([U]^2\).

**Fingerprint:** `0656c01c05ddd8cb2691ec1522e530382cbeda95680a6d72953652199a4c144e`

## CLAIM-0257 — Large Domination Obstruction
**Source ID:** `RG04` · **Status:** `UNCONDITIONAL_ELEMENTARY` · **Authority:** `PROPOSED` · **Verification:** `INHERITED_FROM_V1_AUDIT`

Let \(\kappa\) be infinite. If \(G\) is \(K_4\)-free and \(tc(G)>\kappa\), then \(\gamma(G)>2^\kappa\), where \(\gamma(G)\) is the domination number.

**Fingerprint:** `d34a9363fe511f8ce09c3ef37bfa118093cd11f4c88b2fd39a006203a30dfb6e`

## CLAIM-0258 — Closed-Neighborhood Escape Component
**Source ID:** `RG05` · **Status:** `UNCONDITIONAL_ELEMENTARY` · **Authority:** `PROPOSED` · **Verification:** `INHERITED_FROM_V1_AUDIT`

Let \(\kappa\) be infinite, let \(G\) be \(K_4\)-free with \(tc(G)>\kappa\), and let \(|S|\le2^\kappa\). Then some connected component \(C\) of \(G-N[S]\) satisfies \(tc(C)>\kappa\).

**Fingerprint:** `e40496e62df8ab9cf5a50158b7eadf7ea6fce0d55e195a008f61f2747266a66a`

## CLAIM-0259 — Cardinal Invariants of the Induced-Null Ideal
**Source ID:** `RG06` · **Status:** `UNCONDITIONAL_ELEMENTARY` · **Authority:** `PROPOSED` · **Verification:** `INHERITED_FROM_V1_AUDIT`

Let \(\kappa\) be infinite, \(tc(G)>\kappa\), and \(\mathcal J_\kappa(G)=\{A\subseteq V(G):tc(G[A])\le\kappa\}\). Then \(\operatorname{add}(\mathcal J_\kappa),\operatorname{cov}(\mathcal J_\kappa),\operatorname{non}(\mathcal J_\kappa)\ge (2^\kappa)^+\).

**Fingerprint:** `126e631b450d44eaccd9fd90d43cad394a527a6ce96fe8b6b922d0a193a15969`

## CLAIM-0260 — No Maximal Null Set and No Minimal Positive Set
**Source ID:** `RG07` · **Status:** `UNCONDITIONAL_ELEMENTARY` · **Authority:** `PROPOSED` · **Verification:** `INHERITED_FROM_V1_AUDIT`

If \(tc(G)>\kappa\), then \(\mathcal J_\kappa(G)\) has no inclusion-maximal member, and the family \(\mathcal J_\kappa(G)^+\) has no inclusion-minimal member.

**Fingerprint:** `313a1d868fc4091adb6876338d19f203f49902369c3d485adea8287409e2e200`

## CLAIM-0261 — Mixed Unary–Edge Profile Canonization
**Source ID:** `RG08` · **Status:** `UNCONDITIONAL_ELEMENTARY` · **Authority:** `PROPOSED` · **Verification:** `INHERITED_FROM_V1_AUDIT`

Let \(G\) be \(K_4\)-free with \(tc(G)>\kappa\). Fix at most \(\kappa\) unary vertex maps with ranges of size at most \(\kappa\), and edge maps whose combined profile space on \(E(G)\) has cardinality at most \(\kappa\). Then there is a spanning subgraph \(F\) on a vertex set \(U\) such that \(tc(F)>\kappa\); all vertices of \(U\) have one common unary profile; all edges of \(F\) have one common edge profile; and \(F\) contains a triangle-free forward link of chromatic number greater than \(\kappa\).

**Fingerprint:** `bf184c737123840a86bb4722432eeb5771573d1af6feb563242b7a81c77f6b8f`

## CLAIM-0262 — Page-Free Mixed Profile Canonization
**Source ID:** `RG09` · **Status:** `UNCONDITIONAL_ELEMENTARY` · **Authority:** `PROPOSED` · **Verification:** `INHERITED_FROM_V1_AUDIT`

Under the hypotheses of HG21, additionally fix edge maps whose combined edge-profile space has size at most \(\kappa\). Then the page-free, unary-homogeneous induced witness supplied by HG21 contains a positive common edge-profile subgraph and hence a high-chromatic triangle-free forward link, all avoiding the original stable certificate pages.

**Fingerprint:** `6b528f8f62303817cee7f7063e89ff5cac21a38231a2e1049cc3cc10670fb029`

## CLAIM-0263 — Optimal Stable-Partition Quotient Exactness
**Source ID:** `RG10` · **Status:** `UNCONDITIONAL_ELEMENTARY` · **Authority:** `PROPOSED` · **Verification:** `INHERITED_FROM_V1_AUDIT`

Let \(\mathcal P\) be the stable color classes of a proper coloring of \(G\). Then \(\chi(G)\le\chi(Q_{\mathcal P})\). If the coloring uses exactly \(\chi(G)\) colors, then \(\chi(Q_{\mathcal P})=\chi(G)\).

**Fingerprint:** `33504c9db99dbf75262d639e4f89347fef3d1ede55449dae4f51b8eb017d49ac`

## CLAIM-0264 — Null-Cell Quotient Obstruction
**Source ID:** `RG11` · **Status:** `UNCONDITIONAL_ELEMENTARY` · **Authority:** `PROPOSED` · **Verification:** `INHERITED_FROM_V1_AUDIT`

Let \(\kappa\) be infinite and \(tc(G)>\kappa\). If every part \(P\in\mathcal P\) satisfies \(tc(G[P])\le\kappa\), then \(bc(Q_{\mathcal P})>\kappa\) and \(\chi(Q_{\mathcal P})>2^\kappa\).

**Fingerprint:** `3e237edce511505820b424e0d01aed6b3ddf6098381f4592dc306a246ecfae1b`

## CLAIM-0265 — Quotient-Only Sterility Theorem
**Source ID:** `RG12` · **Status:** `UNCONDITIONAL_NEGATIVE_THEOREM` · **Authority:** `PROPOSED` · **Verification:** `INHERITED_FROM_V1_AUDIT`

Quotient isomorphism type alone cannot give any nontrivial universal lower bound on the triangle-cover number of a partitioned graph: every quotient graph \(Q\), including graphs of arbitrarily large chromatic number, has a realization whose ambient graph has triangle-cover number at most one.

**Fingerprint:** `46727672b6dd4afdde02b1504e6137364f31fe6306b5c32b7907afd012abca9d`

## CLAIM-0266 — Exact Unary–Pair Arity Boundary
**Source ID:** `RG13` · **Status:** `UNCONDITIONAL_NEGATIVE_THEOREM` · **Authority:** `PROPOSED` · **Verification:** `INHERITED_FROM_V1_AUDIT`

In a \(K_4\)-free graph with \(tc(G)>\kappa\), every family of at most \(\kappa\) unary \(\kappa\)-valued vertex maps is simultaneously constant on an induced positive subgraph, but complete homogeneity already fails for the single binary adjacency relation.

**Fingerprint:** `0b32cbe966b81c1f129e362685bb7d834bc123dc985c00c2bf4865cabe79cf1b`

## CLAIM-0267 — Huge Stable Set Theorem
**Source ID:** `RG14` · **Status:** `UNCONDITIONAL_TRANSFINITE` · **Authority:** `PROPOSED` · **Verification:** `INHERITED_FROM_V1_AUDIT`

Let \(\theta=(2^\kappa)^+\). Every \(K_4\)-free graph \(G\) with \(tc(G)>\kappa\) contains a stable set of cardinality \(\theta\).

**Fingerprint:** `2f109893dded5e7cf4978ddb62c16ec473397df0e91f8d1b22bd4411b0a2a07e`

## CLAIM-0268 — Large Maximal Stable Sets
**Source ID:** `RG15` · **Status:** `UNCONDITIONAL_COROLLARY` · **Authority:** `PROPOSED` · **Verification:** `INHERITED_FROM_V1_AUDIT`

Every maximal stable set in a \(K_4\)-free graph with \(tc(G)>\kappa\) has cardinality at least \((2^\kappa)^+\).

**Fingerprint:** `6493d0a4bff540dc537a7e86745510006954bb180179f2b28d4a2942f34b6583`

## CLAIM-0269 — Stable Reserve after Every Null Deletion
**Source ID:** `RG16` · **Status:** `UNCONDITIONAL_ELEMENTARY` · **Authority:** `PROPOSED` · **Verification:** `INHERITED_FROM_V1_AUDIT`

If \(A\in\mathcal J_\kappa(G)\) and \(G\) is \(K_4\)-free with \(tc(G)>\kappa\), then \(G-A\) contains a stable set of cardinality \((2^\kappa)^+\).

**Fingerprint:** `f38e6e06e72eb4b98a3e94d6757820781d7ae97c2036775f9a4ff9e9eb9e2dda`

## CLAIM-0270 — No Small Null Cover and No Small Positive Set
**Source ID:** `RG17` · **Status:** `UNCONDITIONAL_COROLLARY` · **Authority:** `PROPOSED` · **Verification:** `INHERITED_FROM_V1_AUDIT`

At least \((2^\kappa)^+\) induced \(\kappa\)-null sets are required to cover \(V(G)\), and every induced positive vertex set has cardinality at least \((2^\kappa)^+\).

**Fingerprint:** `178a9e2634b7bb3d9ea2abd2768c31bd87cd8a0ab59892351c1b7b5651ce39e6`

## CLAIM-0271 — Null-Deletion Hereditary Quotient Obstruction
**Source ID:** `RG18` · **Status:** `UNCONDITIONAL_ELEMENTARY` · **Authority:** `PROPOSED` · **Verification:** `INHERITED_FROM_V1_AUDIT`

Let \(A\in\mathcal J_\kappa(G)\), where \(tc(G)>\kappa\). Every partition of \(V(G)\setminus A\) into induced \(\kappa\)-null cells has quotient chromatic number greater than \(2^\kappa\).

**Fingerprint:** `fcc04bb07cdde27fc4bf49d9ac08cf89f0238ec6ce1dc913796da29afa68828f`

## CLAIM-0272 — Finite High-Chromatic Quotient Skeletons Are Null
**Source ID:** `RG19` · **Status:** `UNCONDITIONAL_WITH_STANDARD_COMPACTNESS` · **Authority:** `PROPOSED` · **Verification:** `INHERITED_FROM_V1_AUDIT`

Under the hypotheses of RG11, for every finite \(n\) there is a finite subfamily \(\mathcal F_n\subseteq\mathcal P\) such that \(\chi(Q_{\mathcal P}[\mathcal F_n])>n\), while \(\bigcup\mathcal F_n\in\mathcal J_\kappa(G)\).

**Fingerprint:** `bf54d9dd921c4a8e3dc7f66e7c568ec27a760f29b26c9c6446b310be4f4dc1c8`

## CLAIM-0273 — Relational Migration Theorem
**Source ID:** `RG20` · **Status:** `UNCONDITIONAL_NEGATIVE_THEOREM` · **Authority:** `PROPOSED` · **Verification:** `INHERITED_FROM_V1_AUDIT`

In every null-cell partition of a positive graph, arbitrarily high-chromatic finite quotient patterns may be supported on induced-null vertex unions. Consequently neither quotient chromatic number nor any finite quotient subgraph, considered without its edge-fiber realization, can carry the triangle-cover obstruction.

**Fingerprint:** `95f9e34c235a32094b53054896870bbb7ec9031b12e55d3019a147695a353bc1`

## CLAIM-0274 — Disjoint Huge-Stable-Grid Extraction
**Source ID:** `RG21` · **Status:** `UNCONDITIONAL_TRANSFINITE` · **Authority:** `PROPOSED` · **Verification:** `INHERITED_FROM_V1_AUDIT`

Let \(\theta=(2^\kappa)^+\). Every \(K_4\)-free graph \(G\) with \(tc(G)>\kappa\) contains a family \(\langle S_\alpha:\alpha<\theta\rangle\) of pairwise disjoint stable sets, each of cardinality \(\theta\).

**Fingerprint:** `20e0612fa901d8e8d5aba37d37d7bb5d03be25f819f5acafa91d6003ccd25c5b`

## CLAIM-0275 — Unary-Homogeneous Stable Grid
**Source ID:** `RG22` · **Status:** `UNCONDITIONAL_TRANSFINITE` · **Authority:** `PROPOSED` · **Verification:** `INHERITED_FROM_V1_AUDIT`

Under the unary-label hypotheses of HG08, one common unary profile contains \((2^\kappa)^+\) pairwise disjoint stable sets, each of cardinality \((2^\kappa)^+\).

**Fingerprint:** `c044ddc4e611e5f6d26165254c8398f1776ea33e1174184ccbf5eb3a0ca96958`

## CLAIM-0276 — Exact Replacement for Failed Pair Homogenization
**Source ID:** `RG23` · **Status:** `UNCONDITIONAL_COMPOSITE` · **Authority:** `PROPOSED` · **Verification:** `INHERITED_FROM_V1_AUDIT`

Complete pair homogenization is impossible by RG13, but the following replacement is always available: simultaneous unary homogeneity on an induced positive vertex set, followed by edge-profile homogeneity on a positive spanning subgraph and high-chromatic link extraction.

**Fingerprint:** `d56e205020a8ac154e547405a6c4d8f3adfce1158c9907ae6cc9dc5ab4f20a96`

## CLAIM-0277 — Page-Free Relational Residual
**Source ID:** `RG24` · **Status:** `UNCONDITIONAL_ELEMENTARY` · **Authority:** `PROPOSED` · **Verification:** `INHERITED_FROM_V1_AUDIT`

Under the hypotheses of HG21, let \(U\) be its page-free, unary-homogeneous induced positive set. Every partition of \(U\) into induced \(\kappa\)-null cells has quotient chromatic number greater than \(2^\kappa\), yet the quotient graph alone cannot certify positivity.

**Fingerprint:** `f8f361baf81f5f983d4a9049233a4dfb32606b742531e6696d81352a5c314075`

## CLAIM-0278 — Page-Free Homogeneous Stable Grid
**Source ID:** `RG25` · **Status:** `UNCONDITIONAL_TRANSFINITE` · **Authority:** `PROPOSED` · **Verification:** `INHERITED_FROM_V1_AUDIT`

Under the hypotheses of HG21, its page-free unary-homogeneous induced subwitness contains \((2^\kappa)^+\) pairwise disjoint stable sets, each of cardinality \((2^\kappa)^+\), all avoiding the original certificate pages and sharing the same unary profile.

**Fingerprint:** `431bcd3cf054becad587c9dff296c85cdf4c99cb807d3b6e650005e181920643`

## CLAIM-0279 — Fiber-Coherence Classification Target
**Source ID:** `RG26` · **Status:** `UNPROVED_CHECKABLE_TARGET` · **Authority:** `PROPOSED` · **Verification:** `INHERITED_FROM_V1_AUDIT`

For a null-cell partition \(\mathcal P\), retain the quotient graph together with every bipartite edge fiber \(G[P,Q]\) and the ternary incidence rule specifying which triples of fiber edges share endpoints to form graph triangles. Classify the finite \(K_4\)-free fibered quotients that are realizable, determine which have triangle-cover number above a prescribed bound, and identify the minimal coherence patterns not reproducible by the matching construction of RG02.

**Fingerprint:** `45d248a94ef362e4847e3fb544508ba1f0df64e5b7488c27370baf74ca78f1e2`
