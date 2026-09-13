# Fiber-Coherence Self-Growth Round 4
## Realized triangle types, coherent sections, endpoint schemes, and civilization migration

**Date:** 2026-08-04  
**Inherited theorem cards:** 65  
**Generated theorem/target cards:** 23  
**Historical novelty:** **UNRUN**  
**Lean status:** **UNRUN**  
**Flagship status:** Erdős #595 and Erdős #738 remain open.

---

## Executive result

The fourth recursive pass replaced the lossy ordinary quotient by an exact
three-level coherence hierarchy:

```text
ordinary quotient graph
        ↓
realized triangle-type hypergraph
        ↓
actual edge fibers and coherent triangle triples
```

The central proved sandwich is

\[
cs_{\mathcal P}(G)\le tc(G)\le\chi(\mathcal R_{\mathcal P}(G)).
\]

The upper bound colors all edges by their realized part-pair type. The lower
bound uses one coherent representative edge per type. K4-freeness forbids a
coherently sectioned Berge triangle, creating the first exact local
**coherence-frustration constraint**.

The run also converted graph-realizability into endpoint equivalence data and
extracted a large anticomplete civilization of finite high-cover graphs—then
proved that the entire civilization is countably decomposable and deletable.
Thus the #595 obstruction migrates yet again: it is not in quotient complexity,
not in isolated finite high-cover blocks, but in cross-fiber coherence.

```text
Seed cards:                65
Generated cards:           23
Frozen-seed control:       5
Recursive-only gain:       18
Productive generations:    5
```

---


# Generation 1

## FC01 — Triangle-Core Invariance

**Status:** `UNCONDITIONAL_ELEMENTARY`  
**Dependencies:** `NONE`  
**Structural leverage:** `95/100`  
**Claim hash:** `df79d15c42fccde8473726aef9a7c2f01564293c17bd0c3401d34d0004c62b5b`  
**Lean mission:** `triangleCover_triangleCore_invariant`  
**Novelty query:** `"triangle core" triangle-cover number invariant`

### Statement

Let \(\Delta(G)\) be the spanning subgraph consisting of the edges of
\(G\) that lie in at least one triangle. If \(G\) contains a triangle,
then
\[
tc(G)=tc(\Delta(G)).
\]
In general, with \(tc\) of an edgeless graph taken as zero,
\[
tc(G)=\max\{1,tc(\Delta(G))\}
\]
whenever \(E(G)\ne\varnothing\).

### Proof / route

Restriction gives \(tc(\Delta(G))\le tc(G)\). Conversely, color
\(\Delta(G)\) with \(tc(\Delta(G))\) colors and assign every edge
outside \(\Delta(G)\) an arbitrary existing color. Such an edge lies
in no triangle, so it cannot create a monochromatic triangle. If the
triangle core is empty but \(G\) has an edge, one triangle-free layer
is necessary and sufficient.

### Exact falsifier

A graph whose non-triangle edges change its triangle-cover number beyond the stated empty-core convention.

---

## FC02 — Triangle-Hypergraph and K4/Berge-C3 Dictionary

**Status:** `UNCONDITIONAL_ELEMENTARY`  
**Dependencies:** `NONE`  
**Structural leverage:** `100/100`  
**Claim hash:** `d40419fb2aba2c311ecc39001bee661d2f3d1d06abfcc8780f8db1a2a1968281`  
**Lean mission:** `triangleHypergraph_K4_bergeC3_dictionary`  
**Novelty query:** `"triangle hypergraph" Berge C3 K4-free`

### Statement

Let \(\mathcal T(G)\) be the 3-uniform hypergraph with vertex set
\(E(G)\) and one hyperedge for each graph triangle. Then:
1. \(tc(G)=\chi(\mathcal T(G))\), where hypergraph coloring forbids a
   monochromatic hyperedge;
2. \(\mathcal T(G)\) is linear;
3. \(G\) is \(K_4\)-free if and only if \(\mathcal T(G)\) contains no
   Berge cycle of length three.

### Proof / route

The first assertion is the definition of triangle-cover coloring.
Distinct graph triangles share at most one graph edge, proving
linearity. A \(K_4\) has three triangular faces whose pairwise
intersections are three distinct edges, yielding a Berge triangle.
Conversely, three graph triangles with pairwise distinct shared edges
necessarily use four graph vertices and collectively contain all six
edges among them, hence form a \(K_4\).

### Exact falsifier

A failure of the coloring identity, linearity, or either direction of the explicit K4/Berge-triangle construction.

---

## FC03 — Stable-Partition Realized-Type Hypergraph

**Status:** `UNCONDITIONAL_DEFINITIONAL`  
**Dependencies:** `NONE`  
**Structural leverage:** `100/100`  
**Claim hash:** `92e01ac2e03cccd70d07f279fbd3e9b0c724dffe69d38b90276ebe11230051b0`  
**Lean mission:** `realizedTypeHypergraph_of_stablePartition`  
**Novelty query:** `"realized triangle type hypergraph" stable partition`

### Statement

Let \(\mathcal P\) be a partition of \(V(G)\) into stable sets. Define
\(\mathcal R_{\mathcal P}(G)\) as follows. Its vertices are the
unordered pairs \(AB\) of distinct parts for which \(G\) has an edge
between \(A\) and \(B\). A triple
\(\{AB,BC,CA\}\) is a hyperedge exactly when some
\(a\in A,b\in B,c\in C\) form a graph triangle. Then every graph
triangle maps to one hyperedge of \(\mathcal R_{\mathcal P}(G)\).

### Proof / route

Stability of the parts forces the three vertices of every graph
triangle into three distinct parts. Its three graph edges therefore
have the three displayed part-pair types, and the triangle itself
witnesses that the type triple is realized.

### Exact falsifier

A graph triangle in a stable partition using fewer than three parts or mapping to a nonrealized type triple.

---

## FC04 — Endpoint-Scheme Characterization of Graph-Realizable Triangle Hypergraphs

**Status:** `UNCONDITIONAL_CHARACTERIZATION`  
**Dependencies:** `NONE`  
**Structural leverage:** `100/100`  
**Claim hash:** `9df6a482767136f31519324c254be3f2dca5341bde7bdebf239c7dec5e746c29`  
**Lean mission:** `triangleHypergraph_endpointScheme_iff`  
**Novelty query:** `"endpoint scheme" graph-realizable 3-uniform hypergraph`

### Statement

A 3-uniform hypergraph \(H\) is isomorphic to \(\mathcal T(G)\) for
some simple graph \(G\) if and only if there is an equivalence relation
\(\sim\) on \(V(H)\times\{0,1\}\) such that:
1. \((e,0)\not\sim(e,1)\) for every \(e\in V(H)\);
2. distinct \(e,f\) do not determine the same unordered pair of
   equivalence classes;
3. for every \(\{e,f,g\}\in E(H)\), the three unordered endpoint pairs
   determined by \(e,f,g\) are exactly the edges of a triangle;
4. every triple of hypergraph vertices whose endpoint pairs form a
   triangle is a hyperedge of \(H\).

### Proof / route

If \(H=\mathcal T(G)\), give each graph edge its two endpoints and let
equivalence mean equality of graph endpoints. Simplicity gives (1)-(2),
and the definition of \(\mathcal T(G)\) gives (3)-(4). Conversely,
take the equivalence classes as graph vertices and each
\(e\in V(H)\) as the graph edge joining its two endpoint classes.
Conditions (1)-(2) make the graph simple, while (3)-(4) say exactly
that its graph triangles are the hyperedges of \(H\).

### Exact falsifier

A realizable hypergraph without such a scheme, or a scheme whose constructed simple graph has a different triangle hypergraph.

---

## FC05 — Finite High-Cover Extraction

**Status:** `UNCONDITIONAL_WITH_STANDARD_COMPACTNESS`  
**Dependencies:** `FC02`  
**Structural leverage:** `100/100`  
**Claim hash:** `8105e0d805506eaa852e4cc28d789a8a35baeb985b2a37eabc92449a9a71567b`  
**Lean mission:** `finite_subgraph_highTriangleCover_compactness`  
**Novelty query:** `"finite subgraph" high triangle-cover compactness`

### Statement

Let \(n<\omega\). If \(tc(G)>n\), then \(G\) contains a finite
subgraph \(F\) with \(tc(F)>n\). If \(G\) is \(K_4\)-free, \(F\)
may be chosen \(K_4\)-free.

### Proof / route

By FC02, \(tc(G)>n\) means that the hypergraph \(\mathcal T(G)\) is
not \(n\)-colorable. The compactness theorem for finite hypergraph
colorings gives a finite non-\(n\)-colorable subhypergraph. Take the
finite graph formed by its finitely many graph edges. Its triangle
hypergraph contains the chosen subhypergraph, so its triangle-cover
number is greater than \(n\). Subgraphs preserve \(K_4\)-freeness.

### Exact falsifier

A non-n-colorable triangle hypergraph all of whose finite subhypergraphs are n-colorable.

---


# Generation 2

## FC06 — Realized-Type Pullback Upper Bound

**Status:** `UNCONDITIONAL_ELEMENTARY`  
**Dependencies:** `FC03`  
**Structural leverage:** `100/100`  
**Claim hash:** `9ac6a398a1b845acbf38eb497ca8ffe55570d81f6c2f66d0a67dcc8137b68541`  
**Lean mission:** `triangleCover_le_realizedTypeHypergraphChromatic`  
**Novelty query:** `"realized type hypergraph" pullback coloring triangle cover`

### Statement

For every stable partition \(\mathcal P\) of \(V(G)\),
\[
tc(G)\le \chi(\mathcal R_{\mathcal P}(G)).
\]

### Proof / route

Color every graph edge by the color of its part-pair type in a proper
weak coloring of \(\mathcal R_{\mathcal P}(G)\). A graph triangle maps
by FC03 to a realized type hyperedge, whose three types are not
monochromatic. Hence the graph triangle is not monochromatic.

### Exact falsifier

A type-hypergraph coloring whose pulled-back graph-edge coloring creates a monochromatic graph triangle.

---

## FC07 — Triangle-Coherent Section Lower Bound

**Status:** `UNCONDITIONAL_ELEMENTARY`  
**Dependencies:** `FC03`  
**Structural leverage:** `100/100`  
**Claim hash:** `fbfb6bab951d4bbd18513d948fa4a468702d94813c8de078af055b14acc7ab4b`  
**Lean mission:** `coherentSection_chromatic_le_triangleCover`  
**Novelty query:** `"triangle-coherent section" chromatic lower bound`

### Statement

Let \(K\) be a subhypergraph of \(\mathcal R_{\mathcal P}(G)\). A
triangle-coherent section of \(K\) chooses one actual graph edge
\(s(t)\) from every part-pair type \(t\in V(K)\) so that for every
hyperedge \(\{t_1,t_2,t_3\}\in E(K)\), the selected graph edges
\(s(t_1),s(t_2),s(t_3)\) form a graph triangle. If such a section
exists, then
\[
\chi(K)\le tc(G).
\]

### Proof / route

Restrict any no-monochromatic-triangle edge coloring of \(G\) to the
selected edges and transfer the selected-edge color to its type.
Coherence ensures that every hyperedge of \(K\) is represented by an
actual graph triangle, so the induced type coloring has no
monochromatic hyperedge.

### Exact falsifier

A coherent section whose hypergraph requires more colors than the containing graph.

---

## FC08 — Coherence Sandwich

**Status:** `UNCONDITIONAL_ELEMENTARY`  
**Dependencies:** `FC06, FC07`  
**Structural leverage:** `100/100`  
**Claim hash:** `c00718f9e293b3c59956dc39a2b7e8b8793279b3492fb990bde3bdcfea5c47ce`  
**Lean mission:** `coherenceSandwich_triangleCover`  
**Novelty query:** `"coherence sandwich" triangle-cover type hypergraph`

### Statement

For a stable partition \(\mathcal P\), define
\[
cs_{\mathcal P}(G)=\sup\{\chi(K):K\subseteq
\mathcal R_{\mathcal P}(G)\text{ admits a triangle-coherent section}\}.
\]
Then
\[
cs_{\mathcal P}(G)\le tc(G)\le
\chi(\mathcal R_{\mathcal P}(G)).
\]
If the full realized-type hypergraph admits a coherent section, both
inequalities are equalities.

### Proof / route

The lower bound is FC07 applied to every coherently sectioned
subhypergraph and then taking the supremum. The upper bound is FC06.
A coherent section of the full type hypergraph makes its chromatic
number one of the terms in the lower supremum.

### Exact falsifier

A graph/partition violating either side, or a full coherent section without equality.

---

## FC09 — Positive Realized-Type Obstruction

**Status:** `UNCONDITIONAL_COROLLARY`  
**Dependencies:** `FC06`  
**Structural leverage:** `100/100`  
**Claim hash:** `81e7ac236bf7e8f7edb10f04cd88298cf0eaf15a80a85018eff81abe34a9da1c`  
**Lean mission:** `highTriangleCover_forces_positive_realizedTypes`  
**Novelty query:** `"high triangle cover" realized type hypergraph chromatic`

### Statement

If \(tc(G)>\kappa\), then for every stable partition
\(\mathcal P\) of \(V(G)\),
\[
\chi(\mathcal R_{\mathcal P}(G))>\kappa.
\]

### Proof / route

This is the contrapositive of FC06.

### Exact falsifier

A stable partition of a high-cover graph whose realized-type hypergraph is κ-colorable.

---

## FC10 — Matching Correction to Quotient Sterility

**Status:** `UNCONDITIONAL_ELEMENTARY`  
**Dependencies:** `RG02, FC03`  
**Structural leverage:** `96/100`  
**Claim hash:** `c4fd3a86cc74b4ac3a20bb62c04f72f34a1a59ed1d8f21653f2e17b8e79cf47a`  
**Lean mission:** `matching_realizedTypeHypergraph_empty`  
**Novelty query:** `"matching quotient" realized triangle types empty`

### Statement

In the incidence-matching realization of an arbitrary quotient graph
from RG02, the ordinary quotient may be arbitrary, but the realized-type
hypergraph has no hyperedges. Thus its chromatic number is at most one.

### Proof / route

The realizing ambient graph is a matching and has no graph triangles.
By definition FC03, no quotient part-triple is realized as a triangle.

### Exact falsifier

A realized type hyperedge in a matching.

---

## FC11 — K4-Free Coherence-Frustration Theorem

**Status:** `UNCONDITIONAL_ELEMENTARY`  
**Dependencies:** `FC03`  
**Structural leverage:** `100/100`  
**Claim hash:** `40932ae2d0df3ff8e51e5e5b59d941149dd165dd1fffdc15ab97fb43dff9d166`  
**Lean mission:** `K4free_realizedType_bergeC3_frustrated`  
**Novelty query:** `"coherence frustration" Berge triangle K4-free fibers`

### Statement

Let \(G\) be \(K_4\)-free and \(\mathcal P\) a stable partition. No
Berge cycle of length three in \(\mathcal R_{\mathcal P}(G)\) admits a
triangle-coherent section. Equivalently, if three realized part-triangles
pairwise share three distinct part-pair types, then any choice of actual
triangle witnesses must use different actual graph edges in at least
one shared type.

### Proof / route

A Berge triangle in the realized-type hypergraph consists of three
quotient triangles arranged as three faces on four quotient parts.
If a coherent section existed, the selected edge for each shared
part-pair would be reused in both incident selected triangles. The three
selected graph triangles would then use one consistent graph vertex in
each of the four parts and collectively contain all six edges of a
\(K_4\), contradiction.

### Exact falsifier

A K4-free graph with a coherently sectioned Berge triangle of realized types.

---

## FC12 — Exact Endpoint-Scheme Reformulation of Erdős #595

**Status:** `UNCONDITIONAL_EQUIVALENCE`  
**Dependencies:** `FC02, FC04`  
**Structural leverage:** `100/100`  
**Claim hash:** `2abdb7e16a3c8e2ba8d95cd590f181c36d39269bae34b0113d0ec5af8f417131`  
**Lean mission:** `erdos595_endpointScheme_hypergraph_equiv`  
**Novelty query:** `"Erdos 595" endpoint scheme Berge C3-free hypergraph`

### Statement

Erdős #595 is equivalent to the existence of a 3-uniform hypergraph
\(H\) such that:
1. \(\chi(H)>\aleph_0\);
2. \(H\) admits an endpoint scheme from FC04;
3. \(H\) contains no Berge cycle of length three.

### Proof / route

Given a #595 witness \(G\), take \(H=\mathcal T(G)\) and apply FC02
and FC04. Conversely, an endpoint scheme constructs a simple graph
\(G\) with \(H=\mathcal T(G)\). The absence of Berge triangles makes
\(G\) \(K_4\)-free by FC02, and \(\chi(H)>\aleph_0\) gives
\(tc(G)>\aleph_0\).

### Exact falsifier

A failure of either direction after explicitly constructing the endpoint graph or triangle hypergraph.

---


# Generation 3

## FC13 — Massive Anticomplete Finite High-Cover Packing

**Status:** `UNCONDITIONAL_WITH_STANDARD_COMPACTNESS`  
**Dependencies:** `HG14, FC05`  
**Structural leverage:** `100/100`  
**Claim hash:** `59bb51f1f627cbabed960a058d42dc31b0d15a80f91735907f22ee305a0f3235`  
**Lean mission:** `massive_anticomplete_finiteHighCoverPacking`  
**Novelty query:** `"pairwise anticomplete" finite high triangle-cover packing`

### Statement

Let \(\kappa\) be infinite, \(\theta=(2^\kappa)^+\), and let \(G\)
be \(K_4\)-free with \(tc(G)>\kappa\). For every function
\(f:\theta\to\omega\), \(G\) contains pairwise anticomplete finite
induced subgraphs \(F_\alpha\) for \(\alpha<\theta\) such that
\[
tc(F_\alpha)>f(\alpha).
\]

### Proof / route

Recurse on \(\alpha<\theta\). The previously chosen finite graphs use
at most \(2^\kappa\) vertices. Apply HG14 to obtain a positive induced
residual outside their closed neighborhood, hence anticomplete to all
earlier blocks. Apply FC05 in that residual with \(n=f(\alpha)\).

### Exact falsifier

A first stage below θ where closed-neighborhood escape or finite compactness extraction fails.

---

## FC14 — Finite-Civilization Sterility

**Status:** `UNCONDITIONAL_ELEMENTARY`  
**Dependencies:** `T4`  
**Structural leverage:** `96/100`  
**Claim hash:** `b5f21d685b1667e0b0d505ffa0b05bcbde17dad3a3370420351d346abe415dcd`  
**Lean mission:** `finiteAnticompleteCivilization_triangleCover_countable`  
**Novelty query:** `"disjoint finite graphs" unbounded triangle-cover countable`

### Statement

Let \(\{F_i:i\in I\}\) be pairwise anticomplete finite graphs. Then
\[
tc\!\left(\bigsqcup_{i\in I}F_i\right)=\sup_{i\in I}tc(F_i)\le\aleph_0.
\]
In particular, even arbitrarily many finite blocks with unbounded
finite triangle-cover number remain countably triangle-decomposable.

### Proof / route

The equality is the component supremum formula T4. Every finite graph
has finite triangle-cover number, so the supremum is at most
\(\aleph_0\).

### Exact falsifier

A disjoint union of finite components whose triangle-cover number exceeds the supremum of the finite component values.

---

## FC15 — Null High-Cover Civilization Migration

**Status:** `UNCONDITIONAL_WITH_STANDARD_COMPACTNESS`  
**Dependencies:** `FC13, FC14, HG05`  
**Structural leverage:** `100/100`  
**Claim hash:** `998d94c9a41ce2d25fd3ac3336ee0f045bd83d9f1200d78d65b4faefeeff9f58`  
**Lean mission:** `finiteHighCoverCivilization_null_and_deletable`  
**Novelty query:** `"finite Folkman civilization" null deletion witness`

### Statement

Under FC13 with \(\kappa=\aleph_0\), let
\(U=\bigcup_{\alpha<\mathfrak c^+}V(F_\alpha)\). Then
\(tc(G[U])\le\aleph_0\), while the finite component triangle-cover
numbers are unbounded. Moreover,
\[
tc(G-U)>\aleph_0.
\]

### Proof / route

FC14 makes \(G[U]\) countably triangle-decomposable. The induced-null
vertex deletion theorem HG05 therefore preserves the #595 obstruction
in \(G-U\).

### Exact falsifier

A #595 witness in which the extracted anticomplete finite civilization is positive, or its deletion destroys positivity.

---

## FC16 — Coherent Skeleton Close Dichotomy

**Status:** `UNCONDITIONAL_DICHOTOMY`  
**Dependencies:** `FC08, FC09`  
**Structural leverage:** `100/100`  
**Claim hash:** `1f52300292211845c6881510d5aee1d86d03dc4e71c522a5e3ce9c34a46dc489`  
**Lean mission:** `coherentSkeleton_or_diffuseCoherence_dichotomy`  
**Novelty query:** `"diffuse coherence" triangle type hypergraph section`

### Statement

Let \(G\) satisfy \(tc(G)>\kappa\), and let \(\mathcal P\) be a stable
partition. Exactly one of the following search outcomes occurs:
1. some coherently sectioned subhypergraph
   \(K\subseteq\mathcal R_{\mathcal P}(G)\) has \(\chi(K)>\kappa\);
2. every coherently sectioned subhypergraph has chromatic number at most
   \(\kappa\), while the full realized-type hypergraph has chromatic
   number greater than \(\kappa\).
The second outcome says that all positive type complexity is diffuse
across mutually incompatible fiber choices.

### Proof / route

FC09 gives positivity of the full realized-type hypergraph. Either the
defining supremum in FC08 exceeds \(\kappa\), yielding (1), or it does
not, yielding (2).

### Exact falsifier

A stable partition of a positive graph satisfying neither exhaustive alternative.

---

## FC17 — Least-Cardinality Witness Coherence Dispersion

**Status:** `CONDITIONAL_ON_EXISTENCE_OF_LEAST_WITNESS`  
**Dependencies:** `FC07`  
**Structural leverage:** `88/100`  
**Claim hash:** `d049dfa23e49b385498c72f80c790eceb3e249a669850e8e1492248d7a70f5dd`  
**Lean mission:** `leastWitness_coherentSkeletons_small_areNull`  
**Novelty query:** `"least cardinal witness" coherent skeleton dispersion`

### Statement

Let \(G\) be a \(K_4\)-free graph of least vertex cardinality among
graphs with \(tc(G)>\kappa\). Let \(\mathcal P\) be a stable
partition, and let \(K\subseteq\mathcal R_{\mathcal P}(G)\) admit a
triangle-coherent section using fewer than \(|V(G)|\) types. Then
\[
\chi(K)\le\kappa.
\]

### Proof / route

If \(\chi(K)>\kappa\), the selected representative edges form a
\(K_4\)-free subgraph \(F\subseteq G\). FC07 gives
\(tc(F)\ge\chi(K)>\kappa\). The graph \(F\) uses at most twice as many
vertices as selected edge types, hence fewer than \(|V(G)|\) vertices
for an infinite least cardinal, contradicting minimality.

### Exact falsifier

A least-cardinality witness with a smaller positive coherently selected skeleton.

---

## FC18 — Endpoint-Scheme SAT Certificate Target

**Status:** `UNPROVED_CHECKABLE_TARGET`  
**Dependencies:** `FC02, FC04`  
**Structural leverage:** `100/100`  
**Claim hash:** `7d1b9c768ad8fde18876a4d6c7e176ff0aad3add68341789f7200a3b88eb2122`  
**Lean mission:** `endpointScheme_SAT_classification`  
**Novelty query:** `"endpoint scheme" SAT graph triangle hypergraph realizability`

### Statement

Encode FC04 by Boolean endpoint-slot identifications, no-loop and
no-parallel-edge constraints, required triangle constraints, forbidden
extra-triangle constraints, and optionally the Berge-C3 prohibition
from FC02. Enumerate the smallest nonrealizable linear 3-uniform
hypergraphs, minimal endpoint-scheme obstructions, and the smallest
realizable Berge-C3-free hypergraphs of each finite chromatic number.

### Proof / route

FC04 gives an exact finite certificate language; FC02 supplies the
\(K_4\)-free constraint. SAT/ILP can therefore return either an endpoint
scheme or a checked unsatisfiability certificate for bounded inputs.

### Exact falsifier

A finite hypergraph whose realizability is not faithfully represented by the endpoint constraints.

---


# Generation 4

## FC19 — Page-Free Positive Type Hypergraph

**Status:** `UNCONDITIONAL_ELEMENTARY`  
**Dependencies:** `HG21, FC09`  
**Structural leverage:** `98/100`  
**Claim hash:** `22fced10c48de1a8f9bc6a033dfc18eacb92c4aac0098b896c4181701046f3f8`  
**Lean mission:** `pageFreeResidual_realizedTypes_positive`  
**Novelty query:** `"page-free" realized type hypergraph positive`

### Statement

In the page-free, unary-homogeneous induced subwitness supplied by HG21,
every stable vertex partition has a realized-type hypergraph of
chromatic number greater than \(\kappa\).

### Proof / route

HG21 supplies an induced graph \(H\) with \(tc(H)>\kappa\). Apply FC09
inside \(H\).

### Exact falsifier

A stable partition of the page-free positive residual with κ-colorable realized types.

---

## FC20 — Page-Free Coherence Dichotomy

**Status:** `UNCONDITIONAL_DICHOTOMY`  
**Dependencies:** `HG21, FC16`  
**Structural leverage:** `100/100`  
**Claim hash:** `757a1c6a1e094fe5e9cec85ff2e2df8ac5717c6523a9273fb0c127b629e7c2a6`  
**Lean mission:** `pageFreeResidual_coherenceDichotomy`  
**Novelty query:** `"page-free diffuse coherence" triangle fibers`

### Statement

Every page-free unary-homogeneous positive residual from HG21 has, for
each stable partition, either a positive triangle-coherent skeleton or
diffuse positive realized-type complexity with no positive coherent
section.

### Proof / route

Apply FC16 inside the residual from HG21.

### Exact falsifier

A page-free residual/partition for which the coherence dichotomy fails.

---

## FC21 — Finite Endpoint-Scheme Civilization

**Status:** `UNCONDITIONAL_WITH_STANDARD_COMPACTNESS`  
**Dependencies:** `FC02, FC04, FC13, FC15`  
**Structural leverage:** `100/100`  
**Claim hash:** `57680bc8f2019fbf440160d81e1db20745dcba6146f04dccf4a284fd0163ebcc`  
**Lean mission:** `finite_endpointScheme_civilization_null`  
**Novelty query:** `"finite endpoint schemes" anticomplete civilization Erdős 595`

### Statement

In every #595 witness there is a family of \(\mathfrak c^+\) pairwise
anticomplete finite endpoint-scheme hypergraphs
\(H_\alpha=\mathcal T(F_\alpha)\) such that each \(H_\alpha\) is
linear, Berge-C3-free, and the values \(\chi(H_\alpha)\) are unbounded
in \(\omega\). The induced union of the corresponding graph blocks is
nevertheless countably triangle-decomposable and deletable while a
#595 witness survives.

### Proof / route

Use FC13 with unbounded finite thresholds. Apply FC02 and FC04 to each
finite block, then FC15 to the whole anticomplete union.

### Exact falsifier

A failure of endpoint realizability/K4 translation for a finite block, or a positive anticomplete union.

---

## FC22 — Coherence-Only Information Deficit

**Status:** `UNCONDITIONAL_NEGATIVE_THEOREM`  
**Dependencies:** `RG12, FC21`  
**Structural leverage:** `100/100`  
**Claim hash:** `519e02704ecd37a4e5861a3eb1815a5a031c27d499b1bfd74a7c500fceb93b3e`  
**Lean mission:** `coarseQuotient_and_finiteCivilization_sterile`  
**Novelty query:** `"coherence information deficit" triangle-cover quotient fibers`

### Statement

Neither of the following coarse data can certify high triangle-cover
number by itself:
1. the ordinary quotient graph of a stable partition;
2. an anticomplete family of finite endpoint-realizable, Berge-C3-free
   triangle hypergraphs with unbounded finite chromatic number.
The remaining information must include cross-fiber or cross-block
coherence.

### Proof / route

RG12 realizes every ordinary quotient over a matching of triangle-cover
number one. FC21 gives the second structure inside a countably
triangle-decomposable induced union. Thus both coarse objects may be
arbitrarily complicated while the ambient represented graph remains
countably decomposable.

### Exact falsifier

A theorem deriving uncountable triangle-cover solely from either listed coarse datum.

---


# Generation 5

## FC23 — Fiber-Coherence Classification Target

**Status:** `UNPROVED_CHECKABLE_TARGET`  
**Dependencies:** `FC08, FC10, FC11, FC20, FC22`  
**Structural leverage:** `100/100`  
**Claim hash:** `23ee5a0948bfb2d07e69875ca5547c9e35eecc029e1c60bf5a694843eda31181`  
**Lean mission:** `fiberCoherence_finiteClassification`  
**Novelty query:** `"fiber coherence" realized triangle types coherent sections`

### Statement

For a stable partition \(\mathcal P\), retain:
1. the realized-type hypergraph \(\mathcal R_{\mathcal P}(G)\);
2. the actual edge fiber over every type;
3. for every realized type hyperedge, the set of coherent triples of
   actual fiber edges forming graph triangles;
4. the forbidden coherent Berge-C3 constraints imposed by FC11.
Classify finite such systems by their edge-level triangle-cover number,
coherent-section number, realizability, and minimal frustration
patterns. Use the classification to attack the diffuse side of FC20.

### Proof / route

FC08 proves that coherent sections give lower bounds while the full
realized-type hypergraph gives an upper bound. FC10 and FC22 prove that
quotient/type data without fiber coherence are insufficient. FC11
supplies the exact local \(K_4\)-free frustration constraint. The
listed structure is therefore the first representation in this loop
retaining every currently known load-bearing datum.

### Exact falsifier

A smaller exact representation that determines all actual triangle constraints, or a fibered system escaping the proposed certificate language.

---


# Recursive dependency spine

```text
FC03 realized types
 ├─ FC06 pullback upper bound
 │   ├─ FC08 coherence sandwich
 │   │   ├─ FC16 coherent-skeleton/diffuse dichotomy
 │   │   │   └─ FC20 page-free coherence dichotomy
 │   │   └─ FC23 fiber-coherence classification
 │   └─ FC09 positive type obstruction
 │       └─ FC19 page-free positive type hypergraph
 ├─ FC07 coherent-section lower bound
 │   ├─ FC08
 │   └─ FC17 least-witness coherence dispersion
 ├─ FC10 matching correction
 └─ FC11 Berge-triangle frustration
     └─ FC23

FC02 triangle-hypergraph dictionary + FC04 endpoint schemes
 ├─ FC12 exact #595 reformulation
 ├─ FC18 endpoint-SAT target
 └─ FC21 finite endpoint-scheme civilization

FC05 finite compactness + HG14 escape
 └─ FC13 anticomplete finite high-cover packing
     ├─ FC15 null civilization migration
     │   └─ FC21
     └─ FC14 civilization sterility
```

# Exact new close wall

The ordinary quotient is too coarse. The realized-type hypergraph is a valid
upper compression, but it can still overstate the true cover number because
one color may split an edge fiber internally. A coherent section gives a valid
lower compression, but K4-freeness frustrates Berge-triangle sections.

The live problem is now exact:

> Can a high-chromatic realized-type hypergraph in a K4-free graph have all of
> its high-chromatic complexity diffuse across mutually incompatible edge-fiber
> choices, or must it contain a positive coherent skeleton after a suitable
> refinement?

FC23 turns that question into a finite certificate and classification program.
