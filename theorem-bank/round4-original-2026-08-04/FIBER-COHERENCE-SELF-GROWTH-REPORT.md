# Fiber-Coherence Self-Growth Round 4 — Build, Run, and Proof Report

**Date:** 2026-08-04  
**Inherited cards:** 65  
**Generated cards:** 23  
**Frozen-seed control:** 5  
**Recursive-only gain:** 18  
**Productive generations:** 5  
**Final verification:** `PASS`

## What the recursion discovered

Round 3 proved that the ordinary quotient graph is too lossy: every graph is
the quotient of a matching. Round 4 replaced it with two exact objects.

1. The **realized-type hypergraph** records which triples of part-pair fibers
   actually support a graph triangle.
2. A **triangle-coherent section** chooses one representative graph edge from
   each type so that selected representatives realize every chosen type
   triangle simultaneously.

These yield the coherence sandwich

\[
cs_{\mathcal P}(G)\le tc(G)\le
\chi(\mathcal R_{\mathcal P}(G)).
\]

The upper bound is a valid compression; the lower bound measures how much of
that compressed complexity can be realized by one globally consistent edge
choice.

## K4-free frustration

In a K4-free graph, no Berge triangle of realized types admits a coherent
section. Three coherently glued quotient triangles would produce one actual
K4. This is the first exact local constraint on fiber coherence.

## Exact realizability language

The run introduced an endpoint-scheme characterization of graph triangle
hypergraphs. Each hypergraph vertex receives two endpoint slots; an equivalence
relation identifies slots into graph vertices. Simple-graph, required-triangle,
and forbidden-extra-triangle constraints are exact. Together with the
K4/Berge-C3 dictionary, this gives the exact reformulation:

> Erdős #595 asks for an uncountably chromatic 3-uniform hypergraph admitting
> an endpoint scheme and containing no Berge cycle of length three.

## New migration theorem

Every hypothetical #595 witness contains \(\mathfrak c^+\) pairwise
anticomplete finite induced K4-free graphs whose finite triangle-cover numbers
are unbounded. Nevertheless, the entire induced union has triangle-cover
number at most \(leph_0\), and deleting it leaves another #595 witness.

Thus even a vast civilization of finite Folkman-type blocks is locally rich
but globally sterile. The missing obstruction is cross-block and cross-fiber
coherence.

## Causal ablation

The fixed-premise control could generate only 5
claims. Recursive treatment generated 23;
18 disappear when generated claims are forbidden from
becoming later premises.

## Finite mathematical verification

```text
Graphs exhausted:                         1099
Stable partitions checked:               12347
Realized type hypergraphs:               12347
Representative assignments:             29419
Full coherent sections:                  21043
Candidate Berge cycles:                  60
Triangle-core checks:                    1099
Endpoint/K4 dictionary checks:           1099
Matching quotient checks:                1099
Exact assertions:                        66166
```

## Hostile gates

- semantic duplicate refusal: PASS
- dependency ordering: PASS
- authority self-promotion blocked: PASS
- false flagship closure blocked: PASS
- tamper detection: PASS
- causal ablation: PASS
- retracting FC03 invalidated 12 claims including the root
- clean deterministic replay: PASS

## New exact wall

The live branch is now:

```text
positive realized-type hypergraph
        ↓
positive coherent skeleton found?
   yes  → smaller/structured K4-free witness route
   no   → diffuse coherence across incompatible edge-fiber choices
```

The next executable campaign is FC23: enumerate finite fiber-coherence systems,
including actual edge fibers, coherent triangle triples, and forbidden coherent
Berge-C3 patterns.

## Claim boundary

No historical novelty or Lean acceptance is claimed. Neither Erdős #595 nor
Erdős #738 is marked closed. The package proves the displayed direct theorem
routes, the finite kernels, the recursive dependency gain, and the exact new
classification wall.
