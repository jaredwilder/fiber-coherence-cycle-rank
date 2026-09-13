# Theorem map — fiber coherence / triangle cover / cycle-rank program

This file is the reader-facing index for theorem identities that were previously easy to lose inside the larger Erdős #595 / #738 theorem banks.

**Important:** Erdős #595 remains open. This map separates general proved-in-packet theorems, exact finite classifications, constructions, reductions, and still-unproved frontier targets. It is not a claim that the parent Erdős problem is solved.

## Authority labels used here

- `PROVED_IN_PACKET` — the source packet contains a mathematical proof route; not automatically Lean/kernel authority.
- `UNCONDITIONAL_CLASSIFICATION` / `CHARACTERIZATION` / `CONSTRUCTION` — theorem-card status backed by an explicit proof or exact finite verifier as cited in the source bank.
- `UNCONDITIONAL_REDUCTION` — exact reduction assuming only the stated upstream theorems.
- `UNPROVED_CHECKABLE_TARGET` — research target, not a theorem.

Where a theorem card lists `lean_status=UNRUN`, do **not** read the Lean mission name as a completed formalization.

---

# I. Cover-cardinality theorems

## T05 — triangle-transversal centeredness equivalence

**Status:** `PROVED_IN_PACKET`.

Let `Tr(G)` be the family of edge sets meeting every triangle of `G`. For every cardinal `kappa`,

> `tc(G) > kappa` iff every subfamily of `Tr(G)` of cardinality at most `kappa` has nonempty intersection.

This packages triangle-cover cardinality as an intersection/centeredness property of the transversal family.

## T06 — centeredness trichotomy

**Status:** `PROVED_IN_PACKET`.

For a graph containing at least one triangle:

1. `tc(G)=n<omega` exactly when `n` is the least size of a triangle-transversal family with empty intersection;
2. `tc(G)=aleph_0` exactly when `Tr(G)` has the finite-intersection property but some countable subfamily has empty intersection;
3. `tc(G)>aleph_0` exactly when `Tr(G)` is countably centered.

**Lean mission in source:** `triangleCover_centeredness_trichotomy` — mission name only unless separately certified.

## T07 — exact bipartite-cover cardinal theorem

**Status:** `PROVED_IN_PACKET`.

Let `bc(G)` be the least cardinal `kappa` such that `E(G)` is covered by `kappa` bipartite subgraphs. Then

\[
\boxed{bc(G)=\min\{\kappa:\chi(G)\le2^\kappa\}.}
\]

### Proof idea

If `chi(G)<=2^kappa`, code colors by binary `kappa`-sequences and use one bipartite cut/layer per coordinate. Conversely, concatenate the two sides of each of `kappa` covering bipartite subgraphs into a binary word; adjacent vertices differ in at least one coordinate, yielding a proper `2^kappa`-valued coloring.

**Lean mission in source:** `bipartiteCoverNumber_eq_cardinalLog_chromatic`.

## T08 — finite logarithmic bipartite cover

**Status:** `PROVED_IN_PACKET`.

For every finite graph with at least one edge,

\[
\boxed{bc(G)=\lceil\log_2\chi(G)\rceil.}
\]

This is the finite specialization of T07.

## T09 — triangle cover bounded by bipartite cover

The source theorem refinery continues from T07/T08 with the comparison between triangle-free cover number and bipartite cover number. See the theorem-bank source for the exact scope/proof route; this map intentionally does not silently paraphrase the stronger statement beyond the recovered text.

---

# II. Unicyclic coherence theory

The unicycle theorem cards classify the first nontrivial cycle-rank layer of finite fiber-coherence CSPs.

## UC04 — unicyclic fixed-point criterion

**Status:** unconditional theorem-card characterization.

After support-pruning attached trees, a unicyclic fiber CSP is coherent exactly when the relational composition around its unique cycle has a fixed point.

This converts global coherence into one finite monodromy/fixed-point test.

## No-third-obstruction theorem at cycle rank one

**Status:** `UNCONDITIONAL_CLASSIFICATION`.

At incidence cycle rank one, incoherence has exactly two mechanisms:

1. **support-pruning failure:** an attached-tree reduction empties a variable domain or projected cycle relation;
2. **cycle fixed-point failure:** all local supports survive, but the composed cycle relation has no fixed point.

There is no third obstruction species at this rank.

## UC10 — twisted-cycle XOR criterion

**Status:** `UNCONDITIONAL_CHARACTERIZATION`.

For the binary twisted-cycle construction with twist bits `sigma_i`, the system has exactly two coherent sections when

\[
\sigma_0\oplus\cdots\oplus\sigma_{n-1}=0,
\]

and no coherent section when the xor is `1`.

The proof is monodromy: composition around the cycle is either identity or bit-flip.

## UC11 — minimal pure-cycle frustration at arbitrary length

**Status:** unconditional theorem-card construction/classification.

For every `n>=7`, there is a finite `K_4`-free fiber-coherence system with exactly `n` constraints which is incoherent, every proper constraint subsystem is coherent, every fiber value survives support pruning, and the incidence graph has exactly one cycle.

Thus arbitrarily long inclusion-minimal **pure cyclic** obstructions exist.

## UC03 — twisted-cycle `K_4`-free graph realization

**Status:** `UNCONDITIONAL_CONSTRUCTION`.

For every `n>=7` and every binary twist vector `(sigma_0,...,sigma_{n-1})`, the source gives an explicit finite `K_4`-free graph with two-vertex stable fibers `P_i` whose realized triangle constraints encode exactly the twisted-cycle relations.

This is the graph-realization bridge that turns the CSP obstruction into a concrete `K_4`-free graph object.

### Exact finite verification receipt

The recovered finite-verification receipt reports:

- `179210` assertions;
- `54225` binary relation cycles exhausted;
- `56104` permutation cycles exhausted and section-counted;
- `1920` twist vectors / twisted graphs checked;
- `960` odd-twist minimal cores;
- `19262` support-pruning failures;
- `14` pure-cycle fixed-point failures;
- overall `passed=true`.

The checked claims named in that receipt include UC04, UC08, UC03, UC10, UC11, and UC12.

---

# III. Cactus and cycle-rank-two close

The next source layer classifies tree-of-cycle/cactus behavior and then the first genuinely multicycle 2-connected incidence blocks.

## Cactus obstruction layer

The theorem bank contains exact cactus-core criteria reducing coherence to the constituent cycle constraints after tree absorption. This is the bridge between the unicycle theory and higher 2-connected blocks.

## TH19 — finite-fiber #595 rank-two close theorem

**Status:** `UNCONDITIONAL_REDUCTION`.

In the finite-obstruction branch of a stable finite-fiber compression of a hypothetical #595 witness, every inclusion-minimal 2-connected incidence block of cycle rank two is classified by the rank-two/theta theory.

Therefore every still-unclassified minimal 2-connected block has cycle rank at least three.

This is a **frontier reduction**, not a parent close.

## TH20 — page-free rank-two close

**Status:** `UNCONDITIONAL_REDUCTION`.

The same rank-two closure survives inside the page-free unary-homogeneous witness produced by the #738-side reduction: every finite minimal obstruction is either cactus, theta-classified, or has a 2-connected block of cycle rank at least three; otherwise the coherent-compression branch holds.

---

# IV. Rank-three kernel classification

The dedicated `rank-three-kernel/` subtree contains the next structural extraction. After suppressing degree-two vertices in a loopless 2-connected cyclomatic-rank-three kernel, the program classifies the finite kernel shapes into four types and develops the corresponding CSP realization/complexity layer.

This is a general structural object independent of whether the ultimate #595 bridge closes.

See the dedicated subtree for the exact four-type statement, receipts, and the explicit rank-four frontier.

---

# V. Exact frontier

## TH21 — cycle-rank-three ear-interaction census

**Status:** `UNPROVED_CHECKABLE_TARGET` — **NOT A THEOREM**.

The source proposes the first unclassified incidence block as a theta block plus one added ear and asks for a complete census of path/ear relations, pair/triple intersections, deletion spectra, and whether incoherence is already visible in a proper rank-two subblock.

TH19 makes cycle rank three the first genuinely open finite 2-connected block rank in this reduction architecture.

Do not promote TH21 merely because it has a Lean mission name or high structural-leverage score.

---

# VI. Where the source lives

The canonical repository already preserves the underlying theorem banks, finite witnesses, formal mirrors, verification artifacts, rank-three kernel package, triangle-cover records, and cross-program #738 material.

High-value original source identities include:

- `ERDOS-595-ENCIRCLEMENT-THEOREM-REFINERY-2026-08-04.md`;
- `UNIFIED-CLAIM-BANK.jsonl`;
- `UNICYCLE-CORE-THEOREM-CARDS.jsonl`;
- `THETA-COLLISION-THEOREM-CARDS.jsonl`;
- the finite-verification receipts;
- the rank-three-kernel package.

This map exists so a reader does not need to infer the mathematical program from hundreds of cards.

## Publication / novelty rule

Historical priority varies theorem by theorem. Several of the cover-number statements have explicit medium/high prior-art risk in the source bank. **Publication here records the mathematics and its estate authority; it does not settle novelty.**
