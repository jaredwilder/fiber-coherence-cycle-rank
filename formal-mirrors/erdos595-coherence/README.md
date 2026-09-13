# Fiber coherence, cycle rank and finite kernel structure

This directory is a **research-program mirror** for a large relational/coherence theory that grew out of the Erdős #595 work. It should be read as its own mathematical program, not as part of this repository's 79-declaration Lean corpus.

## Program scale

Together with `../erdos595-fiber-coherence/` and the corresponding public archive extraction, the program contains **216 records across nine mathematical layers**. The files here preserve the major theorem banks:

- `ERDOS-595-SELF-GROWTH-16.jsonl`
- `RELATIONAL-THEOREM-CARDS.jsonl`
- `COHERENCE-CSP-STATEMENTS.jsonl`
- `UNICYCLE-CORE-STATEMENTS.jsonl`
- `THETA-COLLISION-STATEMENTS.jsonl`
- `RANK-THREE-KERNEL-STATEMENTS.jsonl`
- `PERMUTATION-GLUING-STATEMENTS.jsonl`
- `HIGH-GEAR-THEOREM-CARDS.jsonl`

The separate `../erdos595-fiber-coherence/` directory contains 23 focused fiber-coherence records.

## Mathematical content

The program moves from local relational growth and consistency constraints toward finite structural classification:

- relational self-growth identities;
- coherence as a finite constraint-satisfaction problem;
- unicyclic and cactus structure;
- theta-collision restrictions;
- finite kernel reduction by suppressing degree-two paths;
- rank-three kernel classification;
- permutation/gluing structure;
- recursive bridges toward higher cycle rank.

The rank-three extraction is particularly concrete: after suppressing degree-two paths, every loopless 2-connected cyclomatic-rank-three kernel falls into exactly four types (`Q4`, `T221`, `D22`, `K4`). The same layer records finite K4-free realizations of binary CSPs, fixed-rank tractability versus unbounded-rank NP-completeness, and rank four as the first unclassified fixed-rank regime in the program.

## Naming warning

This material must **not** be confused with `ck-gold-and-r3-envelope`. The `r_3` in that repository is the Roth/three-term-arithmetic-progression extremal function. Here, “rank three” means graph cycle rank / kernel structure.

## Repository status

This program has outgrown a broad theorem-bank mirror and warrants a dedicated subject repository. Until that home exists, these files are the public research record and should be cited by their exact statements/statuses rather than by any umbrella authority label from `erdos-theorems`.
