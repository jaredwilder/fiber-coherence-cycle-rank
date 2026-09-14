# Fiber coherence, cycle rank, and K4-free CSP realization

**Author:** Jared Wilder  
**Status:** structural graph/CSP research program; not a claim that the parent Erdős problem is closed.

This repository is the canonical public home for the estate's fiber-coherence program: relational self-growth, coherence CSPs, unicyclic and cactus kernels, permutation gluing, theta collisions, finite cycle-rank classification, and the rank-three kernel layer.

## Strongest distinctive theorem layer

The final source court separates the program's **classical topology infrastructure** from its most distinctive source theorem.

For finite sets `A,B` and an arbitrary relation

`R ⊆ A × B`,

the rank-three packet constructs a finite **K4-free stable-partition graph gadget** with boundary fibers indexed by `A` and `B` such that

> a boundary pair `(a,b)` extends to a coherent section **if and only if** `(a,b) ∈ R`.

The construction uses six stable parts and private four-triangle chains for allowed pairs. Composing one fresh relation strip per binary constraint yields:

> **Every finite binary CSP has a polynomial-size exact K4-free fiber-coherence realization.**

The realization is exact at the boundary: global coherent sections correspond precisely to satisfying assignments of the original CSP. A direct reduction from graph 3-COLORING then gives the packet's consequence that finite K4-free fiber coherence is NP-complete when cycle rank is unbounded, with branch-domain size three already sufficient for NP-hardness.

Historical novelty is **not** certified. The source court treats the relation-strip / universal-realization pair as an `N2` candidate requiring specialist graph-gadget/CSP/homomorphism prior-art review.

See [`rank-three-kernel/README.md`](rank-three-kernel/README.md) for the full construction, authority boundary, complexity consequence, and exact repair profiles.

## Rank-three topology infrastructure

After suppressing degree-two vertices, every loopless 2-connected cyclomatic-rank-three kernel falls into exactly four branch types:

- `Q4` — four parallel edges;
- `T221` — triangle multiplicities `2,2,1`;
- `D22` — a four-cycle with opposite doubled edges;
- `K4`.

For tree-absorbed fiber-coherence blocks, suppressed paths become exact endpoint relations, so these four topologies induce four corresponding relation mechanisms.

The topology classification itself lies in classical reduced-graph / cyclomatic-number territory and is retained as useful infrastructure rather than claimed as novel mathematics. The source-specific content begins with the exact relation semantics and K4-free realization theorems above.

## Complexity boundary

For fixed cyclomatic rank `r` and maximum fiber-domain size `d`, feedback conditioning gives

`O(d^r poly(N))`

time. The generic fixed-feedback-set mechanism is standard CSP methodology and receives no novelty credit in the source court.

At unbounded rank, the exact K4-free realization theorem supplies the formulation-specific NP-completeness result.

For the finite-fiber Erdős #595 reduction, cycle rank four is the first fixed-rank minimal incoherence regime not exhaustively classified by this packet. That is a reduction boundary, not a solution of #595.

## Source layout

Exact historical source bytes are migrated under:

- `theorem-bank/` — the nine-layer fiber-coherence theorem bank;
- `rank-three-kernel/` — focused rank-three extraction and 24-card status ledger;
- `formal-mirrors/` — related Erdős #595 formal/theorem mirrors when present.

The provenance archives remain public, but this repository is the preferred subject-focused reading surface.

## Scope discipline

Proved structural statements, finite classifications, computational evidence, negative results, and open targets remain distinct. `UNCONDITIONAL_*` in the source means an ordinary mathematical proof/derivation was supplied; it does **not** mean Lean-kernel certification. Historical novelty is not inferred from internal status labels.

## Recovered original source packet — 2026-09-13

The round-four source contains 23 generated cards, including two explicitly unproved targets. Its recorded Lean and novelty statuses remain unchanged. The original verifier references three external seed files at `/mnt/data` paths; recovered seed dependencies and a portable replay are supplied separately.

- [Original record table](theorem-bank/round4-original-2026-08-04/FIBER-COHERENCE-THEOREM-CARDS.jsonl)
- [Source packet](theorem-bank/round4-original-2026-08-04/)
- [Source hashes and observed status counts](verification/source-packet.json)

Run `python verification/verify_source_packet.py` to verify recovered source bytes, original JSON manifests when present, and record counts.

### Finite replay

Run `python verification/replay_packet.py --receipt verification/local-replay.json`. The runner uses a temporary copy and preserves the original packet and historical receipts. See the [2026-09-13 replay receipt](verification/replay-2026-09-13.json).

The replay passed **66,166 finite assertions over 1,099 graphs** and the source dependency/correction checks. Three recovered seed tables are included with hashes under `verification/seed-dependencies/`. Only the three original `/mnt/data` seed-path literals are adapted in the temporary copy; mathematical checking logic and original source bytes are preserved. These are finite and source-integrity checks, not Lean verification or closure of the parent problems.
