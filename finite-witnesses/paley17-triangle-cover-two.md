# Paley(17) — exact triangle-free edge-cover number 2

**Author:** Jared Wilder  
**Program:** Erdős #595 / triangle-cover / fiber-coherence finite witnesses  
**Status:** exact finite theorem with explicit certificate

Let `G` be the Paley graph on `Z/17Z`, with connection set

\[
S=\{1,2,4,8,9,13,15,16\},
\]

the nonzero quadratic residues modulo 17.

Direct enumeration gives:

- `17` vertices;
- `68` edges;
- `68` triangles;
- **0 copies of `K_4`** among all `C(17,4)=2380` four-sets.

Define `tc(G)` to be the minimum number of triangle-free spanning subgraphs whose edge sets cover `E(G)`.

Then

\[
\boxed{tc(G)=2.}
\]

## Lower bound

`G` contains triangles, so its full edge set is not triangle-free. Hence

\[
tc(G)\ge2.
\]

## Explicit two-class certificate

The following 36 edges form a triangle-free subgraph:

```text
(0,2) (0,9) (0,13) (0,16) (1,3) (1,10) (1,14) (2,3) (2,10) (2,15)
(3,4) (3,5) (3,11) (4,6) (4,8) (4,12) (4,13) (5,6) (5,9) (5,14)
(6,7) (6,10) (6,15) (7,8) (7,9) (7,11) (7,16) (9,10) (10,11) (10,12)
(11,13) (12,14) (12,16) (13,14) (14,15) (15,16)
```

The complementary 32 Paley edges also form a triangle-free subgraph:

```text
(0,1) (0,4) (0,8) (0,15) (1,2) (1,5) (1,9) (1,16) (2,4) (2,6) (2,11)
(3,7) (3,12) (3,16) (4,5) (5,7) (5,13) (6,8) (6,14) (7,15) (8,9) (8,10)
(8,12) (8,16) (9,11) (9,13) (10,14) (11,12) (11,15) (12,13) (13,15) (14,16)
```

These two lists are disjoint and their union is exactly the 68-edge Paley graph. Each class has zero triangles. Therefore `tc(G)<=2`, and together with the lower bound:

\[
\boxed{tc(G)=2}.
\]

## Why this belongs here

This computation was recovered from an archive whose filename did not advertise mathematics. In the original broad dump it appeared beside the larger Erdős #595 coherence program, including cycle-rank kernels and triangle-cover bounds.

The finite witness does not settle Erdős #595. Its value is that it gives a completely checkable nontrivial calibration object for the triangle-cover invariant used by that program.

## Reproduction

The companion verifier reconstructs the graph from the residue connection set and checks:

1. exact edge/triangle/K4 counts;
2. the 36+32 edge lists partition `E(G)`;
3. both classes are triangle-free.

No heuristic search is needed to verify the published certificate.
