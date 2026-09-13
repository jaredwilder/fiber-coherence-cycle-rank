# Runbook

From this directory:

```bash
bash prove_system.sh
```

This rebuilds the theorem cards, regenerates the Lean/novelty queues, runs the
finite coherence verifier and hostile gates twice, and byte-compares the final
verification receipt.

Recommended local order:

1. novelty-check FC04, FC06-FC08, FC11, FC12, FC13-FC15;
2. Lean-formalize FC01-FC04, then FC06-FC08 and FC11-FC12;
3. implement FC18 endpoint-scheme SAT encoding;
4. implement FC23 fiber-coherence enumeration;
5. use coherent-section lower bounds as a new close rail for #595;
6. feed finite coherent skeletons back into the #738 link/tree machinery.
