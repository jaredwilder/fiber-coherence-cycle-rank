#!/usr/bin/env python3
"""Verify the Paley(17) triangle-cover-two certificate."""
from itertools import combinations

N = 17
S = {1, 2, 4, 8, 9, 13, 15, 16}


def edge(u, v):
    return u != v and ((v - u) % N in S)


E = {tuple(sorted((u, v))) for u in range(N) for v in range(u + 1, N) if edge(u, v)}
assert len(E) == 68

triangles = [t for t in combinations(range(N), 3)
             if all(tuple(sorted(e)) in E for e in combinations(t, 2))]
k4s = [q for q in combinations(range(N), 4)
       if all(tuple(sorted(e)) in E for e in combinations(q, 2))]
assert len(triangles) == 68
assert len(k4s) == 0

A = {
(0,2),(0,9),(0,13),(0,16),(1,3),(1,10),(1,14),(2,3),(2,10),(2,15),
(3,4),(3,5),(3,11),(4,6),(4,8),(4,12),(4,13),(5,6),(5,9),(5,14),
(6,7),(6,10),(6,15),(7,8),(7,9),(7,11),(7,16),(9,10),(10,11),(10,12),
(11,13),(12,14),(12,16),(13,14),(14,15),(15,16)
}
B = {
(0,1),(0,4),(0,8),(0,15),(1,2),(1,5),(1,9),(1,16),(2,4),(2,6),(2,11),
(3,7),(3,12),(3,16),(4,5),(5,7),(5,13),(6,8),(6,14),(7,15),(8,9),(8,10),
(8,12),(8,16),(9,11),(9,13),(10,14),(11,12),(11,15),(12,13),(13,15),(14,16)
}

assert len(A) == 36
assert len(B) == 32
assert not (A & B)
assert A | B == E


def triangle_count(F):
    return sum(1 for t in combinations(range(N), 3)
               if all(tuple(sorted(e)) in F for e in combinations(t, 2)))


assert triangle_count(A) == 0
assert triangle_count(B) == 0
assert triangle_count(E) == 68

print('PASS')
print('edges=68 triangles=68 K4=0')
print('triangle-free partition sizes=36+32')
print('triangle-cover number=2')
