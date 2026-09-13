# Fiber coherence, cycle rank, and the rank-three kernel

**Author:** Jared Wilder  
**Status:** structural graph/CSP research program; not a claim that the parent Erdős problem is closed.

This repository is the canonical public home for the estate's fiber-coherence program: relational self-growth, coherence CSPs, unicyclic and cactus kernels, permutation gluing, theta collisions, finite cycle-rank classification, and the rank-three kernel layer.

## Strongest structural layer

After suppressing degree-two vertices, loopless 2-connected cyclomatic-rank-three kernels fall into exactly four branch types: `Q4`, `T221`, `D22`, and `K4`. The program also records the associated CSP realizations, deletion/assignment ledgers, fixed-rank algorithmic consequences, and the next structural wall at rank four.

## Source layout

Exact historical source bytes are migrated under:

- `theorem-bank/` — the nine-layer fiber-coherence theorem bank;
- `rank-three-kernel/` — focused rank-three extraction;
- `formal-mirrors/` — related Erdős 595 formal/theorem mirrors when present.

The provenance archives remain public, but this repository is the preferred subject-focused reading surface.

## Scope discipline

Proved structural statements, finite classifications, computational evidence, negative results, and open targets remain distinct. Historical novelty is not inferred from internal status labels.

## Recovered original source packet — 2026-09-13

The round-four source contains 23 generated cards, including two explicitly unproved targets. Its recorded Lean and novelty statuses remain unchanged. The original verifier references three external seed files at /mnt/data paths; recovered seed dependencies and a portable replay are supplied separately.

- [Original record table](theorem-bank/round4-original-2026-08-04/FIBER-COHERENCE-THEOREM-CARDS.jsonl)
- [Source packet](theorem-bank/round4-original-2026-08-04/)
- [Source hashes and observed status counts](verification/source-packet.json)

Run `python verification/verify_source_packet.py` to verify all recovered source bytes, original JSON manifests when present, and record counts.

### Finite replay

Run `python verification/replay_packet.py --receipt verification/local-replay.json`. The runner uses a temporary copy and preserves the original packet and historical receipts. See the [2026-09-13 replay receipt](verification/replay-2026-09-13.json).

The replay passed 66,166 finite assertions over 1,099 graphs and the source dependency/correction checks. Three recovered seed tables are included with hashes under `verification/seed-dependencies/`. Only the three original `/mnt/data` seed-path literals are adapted in the temporary copy; mathematical checking logic and original source bytes are preserved. These are finite and source-integrity checks, not Lean verification or closure of the parent problems.
