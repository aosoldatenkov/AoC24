import itertools as it
import re
import math

with open("test") as f_test, open("input") as f_inp:
    test = f_test.read()
    inpt = f_inp.read()

def results(t1, i1, t2, i2):
    print("Part I:\n  test:", t1, "\n  input:", i1, "\nPart II:\n  test:", t2, "\n  input:", i2)

def solve1(inp):
    count = 0
    freq = dict()
    inp = inp.splitlines()
    for j, l in enumerate(inp):
        for i, a in enumerate(l):
            if a == '.':
                continue
            elif a in freq:
                freq[a].append((i, j))
            else:
                freq[a] = [(i, j)]
#    print(freq)
    antinodes = set()
    L = max(len(inp), len(inp[0]))
    for f in freq:
        for (a, b), (c, d) in it.combinations(freq[f], 2):
            dx, dy = a - c, b - d
            for i in range(-L, L + 1):
                antinodes.add((c + i * dx, d + i * dy))
#    print(antinodes)
    return len([(x, y) for (x, y) in antinodes if 0 <= x < len(inp[0]) and 0 <= y < len(inp)])

def solve2(inp):
    return 0

print(solve1(inpt))

#results(solve1(test), solve1(inpt), solve2(test), solve2(inpt))
