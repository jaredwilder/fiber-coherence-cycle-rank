# Fiber Coherence and Cycle Rank

**Jared Wilder**

Graph/CSP structure for fiber coherence, with exact K4-free realizations, finite cycle-rank classification, and computational verification.

## Universal K4-free realization

For finite sets `A,B` and an arbitrary relation

```text
R ⊆ A × B,
```

the rank-three construction builds a finite **K4-free stable-partition graph gadget** with boundary fibers indexed by `A` and `B` such that

> a boundary pair `(a,b)` extends to a coherent section exactly when `(a,b) ∈ R`.

The gadget uses six stable parts and private four-triangle chains for allowed pairs.

Composing one relation strip per binary constraint yields:

> **Every finite binary CSP has a polynomial-size exact K4-free fiber-coherence realization.**

Global coherent sections correspond exactly to satisfying assignments of the original CSP. A direct reduction from graph 3-coloring gives NP-completeness for finite K4-free fiber coherence at unbounded cycle rank, with branch-domain size three already sufficient for NP-hardness.

See [`rank-three-kernel/README.md`](rank-three-kernel/README.md) for the construction and proof details.

## Rank-three topology

After suppressing degree-two vertices, every loopless 2-connected cyclomatic-rank-three kernel falls into four branch types:

- `Q4` — four parallel edges
- `T221` — triangle multiplicities `2,2,1`
- `D22` — a four-cycle with opposite doubled edges
- `K4`

For tree-absorbed fiber-coherence blocks, suppressed paths become exact endpoint relations, so these four topologies induce four corresponding relation mechanisms.

## Complexity

For fixed cyclomatic rank `r` and maximum fiber-domain size `d`, feedback conditioning gives

```text
O(d^r poly(N)).
```

At unbounded rank, the K4-free realization theorem above supplies the formulation-specific NP-completeness result.

## Verification

The finite replay passes **66,166 assertions over 1,099 graphs** together with dependency and correction checks.

Run:

```sh
python verification/verify_source_packet.py
python verification/replay_packet.py --receipt verification/local-replay.json
```

The replay uses a temporary copy so the recovered historical packet remains byte-stable.

## Repository map

- `theorem-bank/` — nine-layer fiber-coherence theorem bank
- `rank-three-kernel/` — focused rank-three extraction and status ledger
- `formal-mirrors/` — related Erdős #595 formal/theorem mirrors
- `verification/` — source-integrity and finite replay tooling

The rank-three topology classification is classical infrastructure; the exact relation semantics and K4-free CSP realization are the distinctive mathematical layer developed here.