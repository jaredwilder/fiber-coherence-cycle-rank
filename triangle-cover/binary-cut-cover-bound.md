# Binary-coordinate cover bound for triangle-free edge covers

**Author:** Jared Wilder  
**Program:** Erdős #595 / triangle-cover number  
**Status:** elementary general theorem  
**Historical novelty:** not claimed

Let `tc(G)` denote the least cardinality of a family of triangle-free spanning subgraphs whose edge sets cover `E(G)`.

## Theorem

Let `κ` be a cardinal. If

\[
|V(G)|\le 2^\kappa,
\]

then

\[
\boxed{tc(G)\le\kappa.}
\]

No hypothesis on `G` is needed.

## Proof

Choose an injection

\[
\phi:V(G)\longrightarrow\{0,1\}^{\kappa}.
\]

For each coordinate `alpha<κ`, define a spanning subgraph `H_alpha` of `G` by keeping exactly those edges `uv` for which

\[
\phi(u)(\alpha)\ne\phi(v)(\alpha).
\]

Each `H_alpha` is bipartite: its two parts are the vertices carrying bit 0 and bit 1 in coordinate `alpha`. Therefore every `H_alpha` is triangle-free.

Now take any edge `uv` of `G`. Since `phi` is injective, `phi(u)` and `phi(v)` are distinct binary strings, so they differ in at least one coordinate `alpha`. Hence `uv` belongs to `H_alpha`.

Thus

\[
E(G)=\bigcup_{\alpha<\kappa}E(H_\alpha),
\]

with every `H_alpha` triangle-free. Therefore `tc(G)<=κ`.

## Finite form

For a finite graph on `n` vertices this gives

\[
\boxed{tc(G)\le \lceil\log_2 n\rceil.}
\]

The proof is the same: assign distinct binary labels of length `ceil(log2 n)` to the vertices and use coordinate cuts.

## Interpretation

This is a **power-blindness barrier** for triangle-cover arguments: below the cardinal scale `2^κ`, the bound `tc(G)<=κ` follows from pure information/separation and says nothing about the internal structure of `G`.

Consequently, any route that hopes to force a larger triangle-cover number must cross the corresponding vertex-cardinality threshold or exploit an invariant stronger than the raw cover number.

## Provenance

Recovered from the non-mathematically named archive layer of the Erdős #595 / fiber-coherence program. The original archive stated the theorem as a barrier; this file supplies the complete one-paragraph proof and places it in the canonical subject home.
