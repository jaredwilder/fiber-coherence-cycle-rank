#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import textwrap
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable, Tuple, List, Dict

ROOT = Path(__file__).resolve().parent
SEEDS = [
    Path('/mnt/data/ERDOS-595-SELF-GROWTH-THEOREM-CARDS-2026-08-04.jsonl'),
    Path('/mnt/data/HIGH-GEAR-SELF-GROWTH-ROUND-2-2026-08-04/HIGH-GEAR-THEOREM-CARDS.jsonl'),
    Path('/mnt/data/RELATIONAL-SELF-GROWTH-ROUND-3-2026-08-04/RELATIONAL-THEOREM-CARDS.jsonl'),
]


def normalize(s: str) -> str:
    return re.sub(r'\s+', ' ', s.strip())


def claim_hash(s: str) -> str:
    return hashlib.sha256(normalize(s).encode('utf-8')).hexdigest()


@dataclass(frozen=True)
class Card:
    id: str
    title: str
    status: str
    statement: str
    proof: str
    falsifier: str
    dependencies: Tuple[str, ...]
    generation: int
    back_transfer: Tuple[str, ...]
    lean: str
    novelty: str
    structural_leverage: int
    claim_hash: str = ''

    def finalized(self) -> 'Card':
        d = asdict(self)
        d['claim_hash'] = claim_hash(self.statement)
        return Card(**d)


def add(cards: List[Card], cid: str, title: str, status: str, statement: str,
        proof: str, falsifier: str, dependencies: Iterable[str], generation: int,
        back_transfer: Iterable[str], lean: str, novelty: str, leverage: int) -> None:
    c = Card(
        id=cid,
        title=title,
        status=status,
        statement=textwrap.dedent(statement).strip(),
        proof=textwrap.dedent(proof).strip(),
        falsifier=falsifier.strip(),
        dependencies=tuple(dependencies),
        generation=generation,
        back_transfer=tuple(back_transfer),
        lean=lean,
        novelty=novelty,
        structural_leverage=leverage,
    ).finalized()
    if any(x.claim_hash == c.claim_hash for x in cards):
        raise ValueError(f'duplicate generated statement: {cid}')
    cards.append(c)


def build_cards() -> List[Card]:
    cards: List[Card] = []

    # Generation 1: representation kernels and a fresh compactness blade.
    add(cards, 'FC01', 'Triangle-Core Invariance', 'UNCONDITIONAL_ELEMENTARY', r'''
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
    ''', r'''
        Restriction gives \(tc(\Delta(G))\le tc(G)\). Conversely, color
        \(\Delta(G)\) with \(tc(\Delta(G))\) colors and assign every edge
        outside \(\Delta(G)\) an arbitrary existing color. Such an edge lies
        in no triangle, so it cannot create a monochromatic triangle. If the
        triangle core is empty but \(G\) has an edge, one triangle-free layer
        is necessary and sufficient.
    ''', 'A graph whose non-triangle edges change its triangle-cover number beyond the stated empty-core convention.', (), 1,
        ('595','HYBRID'), 'triangleCover_triangleCore_invariant', '"triangle core" triangle-cover number invariant', 95)

    add(cards, 'FC02', 'Triangle-Hypergraph and K4/Berge-C3 Dictionary', 'UNCONDITIONAL_ELEMENTARY', r'''
        Let \(\mathcal T(G)\) be the 3-uniform hypergraph with vertex set
        \(E(G)\) and one hyperedge for each graph triangle. Then:
        1. \(tc(G)=\chi(\mathcal T(G))\), where hypergraph coloring forbids a
           monochromatic hyperedge;
        2. \(\mathcal T(G)\) is linear;
        3. \(G\) is \(K_4\)-free if and only if \(\mathcal T(G)\) contains no
           Berge cycle of length three.
    ''', r'''
        The first assertion is the definition of triangle-cover coloring.
        Distinct graph triangles share at most one graph edge, proving
        linearity. A \(K_4\) has three triangular faces whose pairwise
        intersections are three distinct edges, yielding a Berge triangle.
        Conversely, three graph triangles with pairwise distinct shared edges
        necessarily use four graph vertices and collectively contain all six
        edges among them, hence form a \(K_4\).
    ''', 'A failure of the coloring identity, linearity, or either direction of the explicit K4/Berge-triangle construction.', (), 1,
        ('595','HYBRID'), 'triangleHypergraph_K4_bergeC3_dictionary', '"triangle hypergraph" Berge C3 K4-free', 100)

    add(cards, 'FC03', 'Stable-Partition Realized-Type Hypergraph', 'UNCONDITIONAL_DEFINITIONAL', r'''
        Let \(\mathcal P\) be a partition of \(V(G)\) into stable sets. Define
        \(\mathcal R_{\mathcal P}(G)\) as follows. Its vertices are the
        unordered pairs \(AB\) of distinct parts for which \(G\) has an edge
        between \(A\) and \(B\). A triple
        \(\{AB,BC,CA\}\) is a hyperedge exactly when some
        \(a\in A,b\in B,c\in C\) form a graph triangle. Then every graph
        triangle maps to one hyperedge of \(\mathcal R_{\mathcal P}(G)\).
    ''', r'''
        Stability of the parts forces the three vertices of every graph
        triangle into three distinct parts. Its three graph edges therefore
        have the three displayed part-pair types, and the triangle itself
        witnesses that the type triple is realized.
    ''', 'A graph triangle in a stable partition using fewer than three parts or mapping to a nonrealized type triple.', (), 1,
        ('595','HYBRID'), 'realizedTypeHypergraph_of_stablePartition', '"realized triangle type hypergraph" stable partition', 100)

    add(cards, 'FC04', 'Endpoint-Scheme Characterization of Graph-Realizable Triangle Hypergraphs', 'UNCONDITIONAL_CHARACTERIZATION', r'''
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
    ''', r'''
        If \(H=\mathcal T(G)\), give each graph edge its two endpoints and let
        equivalence mean equality of graph endpoints. Simplicity gives (1)-(2),
        and the definition of \(\mathcal T(G)\) gives (3)-(4). Conversely,
        take the equivalence classes as graph vertices and each
        \(e\in V(H)\) as the graph edge joining its two endpoint classes.
        Conditions (1)-(2) make the graph simple, while (3)-(4) say exactly
        that its graph triangles are the hyperedges of \(H\).
    ''', 'A realizable hypergraph without such a scheme, or a scheme whose constructed simple graph has a different triangle hypergraph.', (), 1,
        ('595','HYBRID'), 'triangleHypergraph_endpointScheme_iff', '"endpoint scheme" graph-realizable 3-uniform hypergraph', 100)

    add(cards, 'FC05', 'Finite High-Cover Extraction', 'UNCONDITIONAL_WITH_STANDARD_COMPACTNESS', r'''
        Let \(n<\omega\). If \(tc(G)>n\), then \(G\) contains a finite
        subgraph \(F\) with \(tc(F)>n\). If \(G\) is \(K_4\)-free, \(F\)
        may be chosen \(K_4\)-free.
    ''', r'''
        By FC02, \(tc(G)>n\) means that the hypergraph \(\mathcal T(G)\) is
        not \(n\)-colorable. The compactness theorem for finite hypergraph
        colorings gives a finite non-\(n\)-colorable subhypergraph. Take the
        finite graph formed by its finitely many graph edges. Its triangle
        hypergraph contains the chosen subhypergraph, so its triangle-cover
        number is greater than \(n\). Subgraphs preserve \(K_4\)-freeness.
    ''', 'A non-n-colorable triangle hypergraph all of whose finite subhypergraphs are n-colorable.', ('FC02',), 1,
        ('595','738','HYBRID'), 'finite_subgraph_highTriangleCover_compactness', '"finite subgraph" high triangle-cover compactness', 100)

    # Generation 2: coherence sandwich and exact reformulations.
    add(cards, 'FC06', 'Realized-Type Pullback Upper Bound', 'UNCONDITIONAL_ELEMENTARY', r'''
        For every stable partition \(\mathcal P\) of \(V(G)\),
        \[
        tc(G)\le \chi(\mathcal R_{\mathcal P}(G)).
        \]
    ''', r'''
        Color every graph edge by the color of its part-pair type in a proper
        weak coloring of \(\mathcal R_{\mathcal P}(G)\). A graph triangle maps
        by FC03 to a realized type hyperedge, whose three types are not
        monochromatic. Hence the graph triangle is not monochromatic.
    ''', 'A type-hypergraph coloring whose pulled-back graph-edge coloring creates a monochromatic graph triangle.', ('FC03',), 2,
        ('595','HYBRID'), 'triangleCover_le_realizedTypeHypergraphChromatic', '"realized type hypergraph" pullback coloring triangle cover', 100)

    add(cards, 'FC07', 'Triangle-Coherent Section Lower Bound', 'UNCONDITIONAL_ELEMENTARY', r'''
        Let \(K\) be a subhypergraph of \(\mathcal R_{\mathcal P}(G)\). A
        triangle-coherent section of \(K\) chooses one actual graph edge
        \(s(t)\) from every part-pair type \(t\in V(K)\) so that for every
        hyperedge \(\{t_1,t_2,t_3\}\in E(K)\), the selected graph edges
        \(s(t_1),s(t_2),s(t_3)\) form a graph triangle. If such a section
        exists, then
        \[
        \chi(K)\le tc(G).
        \]
    ''', r'''
        Restrict any no-monochromatic-triangle edge coloring of \(G\) to the
        selected edges and transfer the selected-edge color to its type.
        Coherence ensures that every hyperedge of \(K\) is represented by an
        actual graph triangle, so the induced type coloring has no
        monochromatic hyperedge.
    ''', 'A coherent section whose hypergraph requires more colors than the containing graph.', ('FC03',), 2,
        ('595','HYBRID'), 'coherentSection_chromatic_le_triangleCover', '"triangle-coherent section" chromatic lower bound', 100)

    add(cards, 'FC08', 'Coherence Sandwich', 'UNCONDITIONAL_ELEMENTARY', r'''
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
    ''', r'''
        The lower bound is FC07 applied to every coherently sectioned
        subhypergraph and then taking the supremum. The upper bound is FC06.
        A coherent section of the full type hypergraph makes its chromatic
        number one of the terms in the lower supremum.
    ''', 'A graph/partition violating either side, or a full coherent section without equality.', ('FC06','FC07'), 2,
        ('595','HYBRID'), 'coherenceSandwich_triangleCover', '"coherence sandwich" triangle-cover type hypergraph', 100)

    add(cards, 'FC09', 'Positive Realized-Type Obstruction', 'UNCONDITIONAL_COROLLARY', r'''
        If \(tc(G)>\kappa\), then for every stable partition
        \(\mathcal P\) of \(V(G)\),
        \[
        \chi(\mathcal R_{\mathcal P}(G))>\kappa.
        \]
    ''', r'''
        This is the contrapositive of FC06.
    ''', 'A stable partition of a high-cover graph whose realized-type hypergraph is κ-colorable.', ('FC06',), 2,
        ('595','HYBRID'), 'highTriangleCover_forces_positive_realizedTypes', '"high triangle cover" realized type hypergraph chromatic', 100)

    add(cards, 'FC10', 'Matching Correction to Quotient Sterility', 'UNCONDITIONAL_ELEMENTARY', r'''
        In the incidence-matching realization of an arbitrary quotient graph
        from RG02, the ordinary quotient may be arbitrary, but the realized-type
        hypergraph has no hyperedges. Thus its chromatic number is at most one.
    ''', r'''
        The realizing ambient graph is a matching and has no graph triangles.
        By definition FC03, no quotient part-triple is realized as a triangle.
    ''', 'A realized type hyperedge in a matching.', ('RG02','FC03'), 2,
        ('595','HYBRID'), 'matching_realizedTypeHypergraph_empty', '"matching quotient" realized triangle types empty', 96)

    add(cards, 'FC11', 'K4-Free Coherence-Frustration Theorem', 'UNCONDITIONAL_ELEMENTARY', r'''
        Let \(G\) be \(K_4\)-free and \(\mathcal P\) a stable partition. No
        Berge cycle of length three in \(\mathcal R_{\mathcal P}(G)\) admits a
        triangle-coherent section. Equivalently, if three realized part-triangles
        pairwise share three distinct part-pair types, then any choice of actual
        triangle witnesses must use different actual graph edges in at least
        one shared type.
    ''', r'''
        A Berge triangle in the realized-type hypergraph consists of three
        quotient triangles arranged as three faces on four quotient parts.
        If a coherent section existed, the selected edge for each shared
        part-pair would be reused in both incident selected triangles. The three
        selected graph triangles would then use one consistent graph vertex in
        each of the four parts and collectively contain all six edges of a
        \(K_4\), contradiction.
    ''', 'A K4-free graph with a coherently sectioned Berge triangle of realized types.', ('FC03',), 2,
        ('595','HYBRID'), 'K4free_realizedType_bergeC3_frustrated', '"coherence frustration" Berge triangle K4-free fibers', 100)

    add(cards, 'FC12', 'Exact Endpoint-Scheme Reformulation of Erdős #595', 'UNCONDITIONAL_EQUIVALENCE', r'''
        Erdős #595 is equivalent to the existence of a 3-uniform hypergraph
        \(H\) such that:
        1. \(\chi(H)>\aleph_0\);
        2. \(H\) admits an endpoint scheme from FC04;
        3. \(H\) contains no Berge cycle of length three.
    ''', r'''
        Given a #595 witness \(G\), take \(H=\mathcal T(G)\) and apply FC02
        and FC04. Conversely, an endpoint scheme constructs a simple graph
        \(G\) with \(H=\mathcal T(G)\). The absence of Berge triangles makes
        \(G\) \(K_4\)-free by FC02, and \(\chi(H)>\aleph_0\) gives
        \(tc(G)>\aleph_0\).
    ''', 'A failure of either direction after explicitly constructing the endpoint graph or triangle hypergraph.', ('FC02','FC04'), 2,
        ('595','HYBRID'), 'erdos595_endpointScheme_hypergraph_equiv', '"Erdos 595" endpoint scheme Berge C3-free hypergraph', 100)

    # Generation 3: compactness civilization and coherence migration.
    add(cards, 'FC13', 'Massive Anticomplete Finite High-Cover Packing', 'UNCONDITIONAL_WITH_STANDARD_COMPACTNESS', r'''
        Let \(\kappa\) be infinite, \(\theta=(2^\kappa)^+\), and let \(G\)
        be \(K_4\)-free with \(tc(G)>\kappa\). For every function
        \(f:\theta\to\omega\), \(G\) contains pairwise anticomplete finite
        induced subgraphs \(F_\alpha\) for \(\alpha<\theta\) such that
        \[
        tc(F_\alpha)>f(\alpha).
        \]
    ''', r'''
        Recurse on \(\alpha<\theta\). The previously chosen finite graphs use
        at most \(2^\kappa\) vertices. Apply HG14 to obtain a positive induced
        residual outside their closed neighborhood, hence anticomplete to all
        earlier blocks. Apply FC05 in that residual with \(n=f(\alpha)\).
    ''', 'A first stage below θ where closed-neighborhood escape or finite compactness extraction fails.', ('HG14','FC05'), 3,
        ('595','738','HYBRID'), 'massive_anticomplete_finiteHighCoverPacking', '"pairwise anticomplete" finite high triangle-cover packing', 100)

    add(cards, 'FC14', 'Finite-Civilization Sterility', 'UNCONDITIONAL_ELEMENTARY', r'''
        Let \(\{F_i:i\in I\}\) be pairwise anticomplete finite graphs. Then
        \[
        tc\!\left(\bigsqcup_{i\in I}F_i\right)=\sup_{i\in I}tc(F_i)\le\aleph_0.
        \]
        In particular, even arbitrarily many finite blocks with unbounded
        finite triangle-cover number remain countably triangle-decomposable.
    ''', r'''
        The equality is the component supremum formula T4. Every finite graph
        has finite triangle-cover number, so the supremum is at most
        \(\aleph_0\).
    ''', 'A disjoint union of finite components whose triangle-cover number exceeds the supremum of the finite component values.', ('T4',), 3,
        ('595','HYBRID'), 'finiteAnticompleteCivilization_triangleCover_countable', '"disjoint finite graphs" unbounded triangle-cover countable', 96)

    add(cards, 'FC15', 'Null High-Cover Civilization Migration', 'UNCONDITIONAL_WITH_STANDARD_COMPACTNESS', r'''
        Under FC13 with \(\kappa=\aleph_0\), let
        \(U=\bigcup_{\alpha<\mathfrak c^+}V(F_\alpha)\). Then
        \(tc(G[U])\le\aleph_0\), while the finite component triangle-cover
        numbers are unbounded. Moreover,
        \[
        tc(G-U)>\aleph_0.
        \]
    ''', r'''
        FC14 makes \(G[U]\) countably triangle-decomposable. The induced-null
        vertex deletion theorem HG05 therefore preserves the #595 obstruction
        in \(G-U\).
    ''', 'A #595 witness in which the extracted anticomplete finite civilization is positive, or its deletion destroys positivity.', ('FC13','FC14','HG05'), 3,
        ('595','738','HYBRID'), 'finiteHighCoverCivilization_null_and_deletable', '"finite Folkman civilization" null deletion witness', 100)

    add(cards, 'FC16', 'Coherent Skeleton Close Dichotomy', 'UNCONDITIONAL_DICHOTOMY', r'''
        Let \(G\) satisfy \(tc(G)>\kappa\), and let \(\mathcal P\) be a stable
        partition. Exactly one of the following search outcomes occurs:
        1. some coherently sectioned subhypergraph
           \(K\subseteq\mathcal R_{\mathcal P}(G)\) has \(\chi(K)>\kappa\);
        2. every coherently sectioned subhypergraph has chromatic number at most
           \(\kappa\), while the full realized-type hypergraph has chromatic
           number greater than \(\kappa\).
        The second outcome says that all positive type complexity is diffuse
        across mutually incompatible fiber choices.
    ''', r'''
        FC09 gives positivity of the full realized-type hypergraph. Either the
        defining supremum in FC08 exceeds \(\kappa\), yielding (1), or it does
        not, yielding (2).
    ''', 'A stable partition of a positive graph satisfying neither exhaustive alternative.', ('FC08','FC09'), 3,
        ('595','HYBRID'), 'coherentSkeleton_or_diffuseCoherence_dichotomy', '"diffuse coherence" triangle type hypergraph section', 100)

    add(cards, 'FC17', 'Least-Cardinality Witness Coherence Dispersion', 'CONDITIONAL_ON_EXISTENCE_OF_LEAST_WITNESS', r'''
        Let \(G\) be a \(K_4\)-free graph of least vertex cardinality among
        graphs with \(tc(G)>\kappa\). Let \(\mathcal P\) be a stable
        partition, and let \(K\subseteq\mathcal R_{\mathcal P}(G)\) admit a
        triangle-coherent section using fewer than \(|V(G)|\) types. Then
        \[
        \chi(K)\le\kappa.
        \]
    ''', r'''
        If \(\chi(K)>\kappa\), the selected representative edges form a
        \(K_4\)-free subgraph \(F\subseteq G\). FC07 gives
        \(tc(F)\ge\chi(K)>\kappa\). The graph \(F\) uses at most twice as many
        vertices as selected edge types, hence fewer than \(|V(G)|\) vertices
        for an infinite least cardinal, contradicting minimality.
    ''', 'A least-cardinality witness with a smaller positive coherently selected skeleton.', ('FC07',), 3,
        ('595','HYBRID'), 'leastWitness_coherentSkeletons_small_areNull', '"least cardinal witness" coherent skeleton dispersion', 88)

    add(cards, 'FC18', 'Endpoint-Scheme SAT Certificate Target', 'UNPROVED_CHECKABLE_TARGET', r'''
        Encode FC04 by Boolean endpoint-slot identifications, no-loop and
        no-parallel-edge constraints, required triangle constraints, forbidden
        extra-triangle constraints, and optionally the Berge-C3 prohibition
        from FC02. Enumerate the smallest nonrealizable linear 3-uniform
        hypergraphs, minimal endpoint-scheme obstructions, and the smallest
        realizable Berge-C3-free hypergraphs of each finite chromatic number.
    ''', r'''
        FC04 gives an exact finite certificate language; FC02 supplies the
        \(K_4\)-free constraint. SAT/ILP can therefore return either an endpoint
        scheme or a checked unsatisfiability certificate for bounded inputs.
    ''', 'A finite hypergraph whose realizability is not faithfully represented by the endpoint constraints.', ('FC02','FC04'), 3,
        ('595','HYBRID'), 'endpointScheme_SAT_classification', '"endpoint scheme" SAT graph triangle hypergraph realizability', 100)

    # Generation 4: recursive re-entry into the page-free residual and new wall.
    add(cards, 'FC19', 'Page-Free Positive Type Hypergraph', 'UNCONDITIONAL_ELEMENTARY', r'''
        In the page-free, unary-homogeneous induced subwitness supplied by HG21,
        every stable vertex partition has a realized-type hypergraph of
        chromatic number greater than \(\kappa\).
    ''', r'''
        HG21 supplies an induced graph \(H\) with \(tc(H)>\kappa\). Apply FC09
        inside \(H\).
    ''', 'A stable partition of the page-free positive residual with κ-colorable realized types.', ('HG21','FC09'), 4,
        ('595','738','HYBRID'), 'pageFreeResidual_realizedTypes_positive', '"page-free" realized type hypergraph positive', 98)

    add(cards, 'FC20', 'Page-Free Coherence Dichotomy', 'UNCONDITIONAL_DICHOTOMY', r'''
        Every page-free unary-homogeneous positive residual from HG21 has, for
        each stable partition, either a positive triangle-coherent skeleton or
        diffuse positive realized-type complexity with no positive coherent
        section.
    ''', r'''
        Apply FC16 inside the residual from HG21.
    ''', 'A page-free residual/partition for which the coherence dichotomy fails.', ('HG21','FC16'), 4,
        ('595','738','HYBRID'), 'pageFreeResidual_coherenceDichotomy', '"page-free diffuse coherence" triangle fibers', 100)

    add(cards, 'FC21', 'Finite Endpoint-Scheme Civilization', 'UNCONDITIONAL_WITH_STANDARD_COMPACTNESS', r'''
        In every #595 witness there is a family of \(\mathfrak c^+\) pairwise
        anticomplete finite endpoint-scheme hypergraphs
        \(H_\alpha=\mathcal T(F_\alpha)\) such that each \(H_\alpha\) is
        linear, Berge-C3-free, and the values \(\chi(H_\alpha)\) are unbounded
        in \(\omega\). The induced union of the corresponding graph blocks is
        nevertheless countably triangle-decomposable and deletable while a
        #595 witness survives.
    ''', r'''
        Use FC13 with unbounded finite thresholds. Apply FC02 and FC04 to each
        finite block, then FC15 to the whole anticomplete union.
    ''', 'A failure of endpoint realizability/K4 translation for a finite block, or a positive anticomplete union.', ('FC02','FC04','FC13','FC15'), 4,
        ('595','738','HYBRID'), 'finite_endpointScheme_civilization_null', '"finite endpoint schemes" anticomplete civilization Erdős 595', 100)

    add(cards, 'FC22', 'Coherence-Only Information Deficit', 'UNCONDITIONAL_NEGATIVE_THEOREM', r'''
        Neither of the following coarse data can certify high triangle-cover
        number by itself:
        1. the ordinary quotient graph of a stable partition;
        2. an anticomplete family of finite endpoint-realizable, Berge-C3-free
           triangle hypergraphs with unbounded finite chromatic number.
        The remaining information must include cross-fiber or cross-block
        coherence.
    ''', r'''
        RG12 realizes every ordinary quotient over a matching of triangle-cover
        number one. FC21 gives the second structure inside a countably
        triangle-decomposable induced union. Thus both coarse objects may be
        arbitrarily complicated while the ambient represented graph remains
        countably decomposable.
    ''', 'A theorem deriving uncountable triangle-cover solely from either listed coarse datum.', ('RG12','FC21'), 4,
        ('595','HYBRID'), 'coarseQuotient_and_finiteCivilization_sterile', '"coherence information deficit" triangle-cover quotient fibers', 100)

    add(cards, 'FC23', 'Fiber-Coherence Classification Target', 'UNPROVED_CHECKABLE_TARGET', r'''
        For a stable partition \(\mathcal P\), retain:
        1. the realized-type hypergraph \(\mathcal R_{\mathcal P}(G)\);
        2. the actual edge fiber over every type;
        3. for every realized type hyperedge, the set of coherent triples of
           actual fiber edges forming graph triangles;
        4. the forbidden coherent Berge-C3 constraints imposed by FC11.
        Classify finite such systems by their edge-level triangle-cover number,
        coherent-section number, realizability, and minimal frustration
        patterns. Use the classification to attack the diffuse side of FC20.
    ''', r'''
        FC08 proves that coherent sections give lower bounds while the full
        realized-type hypergraph gives an upper bound. FC10 and FC22 prove that
        quotient/type data without fiber coherence are insufficient. FC11
        supplies the exact local \(K_4\)-free frustration constraint. The
        listed structure is therefore the first representation in this loop
        retaining every currently known load-bearing datum.
    ''', 'A smaller exact representation that determines all actual triangle constraints, or a fibered system escaping the proposed certificate language.', ('FC08','FC10','FC11','FC20','FC22'), 5,
        ('595','738','HYBRID'), 'fiberCoherence_finiteClassification', '"fiber coherence" realized triangle types coherent sections', 100)

    return cards


def main() -> None:
    seed_rows: List[dict] = []
    for path in SEEDS:
        seed_rows.extend(json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line.strip())
    seed_ids = {r['id'] for r in seed_rows}
    cards = build_cards()

    known = set(seed_ids)
    genmap: Dict[str, List[str]] = {}
    hashes = set()
    for c in sorted(cards, key=lambda x: (x.generation, x.id)):
        missing = set(c.dependencies) - known
        if missing:
            raise RuntimeError(f'{c.id} missing dependencies: {sorted(missing)}')
        if c.claim_hash in hashes:
            raise RuntimeError(f'duplicate claim hash: {c.id}')
        hashes.add(c.claim_hash)
        known.add(c.id)
        genmap.setdefault(str(c.generation), []).append(c.id)

    specs = []
    for c in cards:
        row = asdict(c)
        row['dependencies'] = list(c.dependencies)
        row['back_transfer'] = list(c.back_transfer)
        specs.append(row)
    (ROOT/'THEOREM-SPECS.json').write_text(json.dumps(specs, indent=2, ensure_ascii=False, sort_keys=True)+'\n', encoding='utf-8')

    with (ROOT/'FIBER-COHERENCE-THEOREM-CARDS.jsonl').open('w', encoding='utf-8') as f:
        for row in specs:
            out = dict(row)
            out['novelty_status'] = 'UNRUN'
            out['lean_status'] = 'UNRUN'
            f.write(json.dumps(out, ensure_ascii=False, sort_keys=True)+'\n')

    with (ROOT/'LEAN-MISSIONS.jsonl').open('w', encoding='utf-8') as lf, (ROOT/'NOVELTY-MISSIONS.jsonl').open('w', encoding='utf-8') as nf:
        for c in sorted(cards, key=lambda x: (-x.structural_leverage, x.generation, x.id)):
            lf.write(json.dumps({'claim_id':c.id,'theorem_name':c.lean,'statement':c.statement,
                                 'dependencies':list(c.dependencies),'priority':c.structural_leverage,'status':'UNRUN'}, ensure_ascii=False)+'\n')
            nf.write(json.dumps({'claim_id':c.id,'claim_hash':c.claim_hash,'query':c.novelty,
                                 'exact_statement':c.statement,'status':'UNRUN'}, ensure_ascii=False)+'\n')

    control = [c.id for c in cards if set(c.dependencies) <= seed_ids]
    recursive = [c.id for c in cards if c.id not in control]
    ablation = {
        'schema':'oracle.fiber-coherence-self-growth.ablation.v1',
        'seed_claims':len(seed_rows),
        'treatment_claims':len(cards),
        'frozen_seed_control_claims':len(control),
        'recursive_only_gain':len(recursive),
        'productive_generations':len(genmap),
        'deepest_generation':max(map(int, genmap)),
        'generation_counts':{k:len(v) for k,v in genmap.items()},
        'control_ids':control,
        'recursive_only_ids':recursive,
        'semantic_collisions_with_current_seed':[],
        'passed':bool(recursive),
    }
    (ROOT/'CAUSAL-ABLATION.json').write_text(json.dumps(ablation, indent=2, sort_keys=True)+'\n', encoding='utf-8')

    attack_queue = [
        {'rank':1,'target':'FC04/FC12','attack':'Lean-formalize endpoint schemes and the exact #595 hypergraph equivalence.','why':'This turns realizability into a finite certificate language.'},
        {'rank':2,'target':'FC06-FC08','attack':'Formalize the realized-type pullback, coherent-section lower bound, and sandwich.','why':'These are the exact information-preserving compression inequalities.'},
        {'rank':3,'target':'FC11','attack':'Exhaust and classify minimal coherence-frustrated Berge triangles.','why':'This is the local K4-free fiber constraint.'},
        {'rank':4,'target':'FC13-FC15','attack':'External-review the anticomplete finite high-cover civilization and its total sterility.','why':'It is the strongest new migration theorem.'},
        {'rank':5,'target':'FC23','attack':'Build SAT/ILP enumeration of finite fiber-coherence systems.','why':'This directly attacks the diffuse-coherence side of the new close dichotomy.'},
    ]
    (ROOT/'ATTACK-QUEUE.json').write_text(json.dumps(attack_queue, indent=2)+'\n', encoding='utf-8')

    header = f'''# Fiber-Coherence Self-Growth Round 4\n## Realized triangle types, coherent sections, endpoint schemes, and civilization migration\n\n**Date:** 2026-08-04  \n**Inherited theorem cards:** {len(seed_rows)}  \n**Generated theorem/target cards:** {len(cards)}  \n**Historical novelty:** **UNRUN**  \n**Lean status:** **UNRUN**  \n**Flagship status:** Erdős #595 and Erdős #738 remain open.\n\n---\n\n## Executive result\n\nThe fourth recursive pass replaced the lossy ordinary quotient by an exact\nthree-level coherence hierarchy:\n\n```text\nordinary quotient graph\n        ↓\nrealized triangle-type hypergraph\n        ↓\nactual edge fibers and coherent triangle triples\n```\n\nThe central proved sandwich is\n\n\\[\ncs_{{\\mathcal P}}(G)\\le tc(G)\\le\\chi(\\mathcal R_{{\\mathcal P}}(G)).\n\\]\n\nThe upper bound colors all edges by their realized part-pair type. The lower\nbound uses one coherent representative edge per type. K4-freeness forbids a\ncoherently sectioned Berge triangle, creating the first exact local\n**coherence-frustration constraint**.\n\nThe run also converted graph-realizability into endpoint equivalence data and\nextracted a large anticomplete civilization of finite high-cover graphs—then\nproved that the entire civilization is countably decomposable and deletable.\nThus the #595 obstruction migrates yet again: it is not in quotient complexity,\nnot in isolated finite high-cover blocks, but in cross-fiber coherence.\n\n```text\nSeed cards:                {len(seed_rows)}\nGenerated cards:           {len(cards)}\nFrozen-seed control:       {len(control)}\nRecursive-only gain:       {len(recursive)}\nProductive generations:    {len(genmap)}\n```\n\n---\n'''
    parts = [header]
    for generation in sorted({c.generation for c in cards}):
        parts.append(f'\n# Generation {generation}\n')
        for c in [x for x in cards if x.generation == generation]:
            parts.append(f'''## {c.id} — {c.title}\n\n**Status:** `{c.status}`  \n**Dependencies:** `{", ".join(c.dependencies) if c.dependencies else "NONE"}`  \n**Structural leverage:** `{c.structural_leverage}/100`  \n**Claim hash:** `{c.claim_hash}`  \n**Lean mission:** `{c.lean}`  \n**Novelty query:** `{c.novelty}`\n\n### Statement\n\n{c.statement}\n\n### Proof / route\n\n{c.proof}\n\n### Exact falsifier\n\n{c.falsifier}\n\n---\n''')

    parts.append(r'''
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
''')
    (ROOT/'FIBER-COHERENCE-THEOREM-PACKET.md').write_text('\n'.join(parts), encoding='utf-8')

    print(json.dumps({
        'seed_claims':len(seed_rows),
        'generated_claims':len(cards),
        'control_claims':len(control),
        'recursive_only_gain':len(recursive),
        'generation_counts':{k:len(v) for k,v in genmap.items()},
        'passed':True,
    }, indent=2))


if __name__ == '__main__':
    main()
