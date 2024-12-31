import itertools as it
import re
import math
from functools import cache

with open("test") as f_test, open("input") as f_inp:
    test = f_test.read()
    inpt = f_inp.read()

def results(t1, i1, t2, i2):
    print("Part I:\n  test:", t1, "\n  input:", i1, "\nPart II:\n  test:", t2, "\n  input:", i2)

def solve1(inp):
    strs = [s.split('-') for s in inp.splitlines()]
    con = [(a, b) for a, b in strs]
    names = set()
    for c in con:
        names.add(c[0])
        names.add(c[1])
    triples = set()
    for t in names:
        if t[0] != 't':
            continue
        for p in con:
            if ((t, p[0]) in con or (p[0], t) in con) and ((t, p[1]) in con or (p[1], t) in con):
                if any(tr in triples for tr in it.permutations([t, p[0], p[1]], 3)):
                    continue
                triples.add((t, p[0], p[1]))
    return len(triples)

def solve2(inp):
    strs = [s.split('-') for s in inp.splitlines()]
    con = [(a, b) for a, b in strs]
    names = set()
    for c in con:
        names.add(c[0])
        names.add(c[1])
    clusters = [[a, b] for a, b in strs]
    connections = dict()
    for n in names:
        connections[n] = set()
        for c in con:
            if c[0] == n:
                connections[n].add(c[1])
            if c[1] == n:
                connections[n].add(c[0])
    inc = True
    while inc:
        inc = False
        for j in range(len(clusters)):
            group = connections[clusters[j][0]]
            for n in clusters[j]:
                group = group & connections[n]
            if group != set():
                clusters[j].append(group.pop())
                inc = True

    m = max(len(c) for c in clusters)
    for c in clusters:
        if len(c) == m:
            cc = sorted(c)
            return ','.join(x for x in cc)

results(solve1(test), solve1(inpt), solve2(test), solve2(inpt))
