import itertools as it
import re
import math
from functools import cache

with open("test") as f_test, open("input") as f_inp:
    test = f_test.read()
    inpt = f_inp.read()

def results(t1, i1, t2, i2):
    print("Part I:\n  test:", t1, "\n  input:", i1, "\nPart II:\n  test:", t2, "\n  input:", i2)

def mp(n, m):
    return (n ^ m) % 16777216

def solve1(inp):
    nums = [int(a) for a in inp.splitlines()]
    for i in range(2000):
        nums = [mp(n, n * 64) for n in nums]
        nums = [mp(n, n // 32) for n in nums]
        nums = [mp(n, n * 2048) for n in nums]
    return sum(nums)

def count(seqs, changes, ref):
    counts = {r: 0 for r in ref}
    for j, s in enumerate(changes):
        print(j, 'of', len(changes))
        c = {r: -1 for r in ref}
        for i in range(len(s) - 3):
            subseq = tuple(s[i: i+4])
            if subseq in ref and c[subseq] < 0:
                c[subseq] = seqs[j][i + 4]
        for r in ref:
            counts[r] += max(c[r], 0)
    m = max(counts[r] for r in ref)
    print([r for r in ref if counts[r] == m])
    return m

def solve2(inp):
    nums = [int(a) for a in inp.splitlines()]
    seqs = [[nums[i] % 10] for i in range(len(nums))]
    for i in range(2000):
        nums = [mp(n, n * 64) for n in nums]
        nums = [mp(n, n // 32) for n in nums]
        nums = [mp(n, n * 2048) for n in nums]
        for i, x in enumerate(nums):
            seqs[i].append(x % 10)
    changes = [[] for _ in range(len(nums))]
    print("1")
    for i, s in enumerate(seqs):
        for a, b in it.pairwise(s):
            changes[i].append(b - a)
    best = 0
    print('2')
    ref = set()
    for j, c in enumerate(changes):
        for i in range(0, len(c) - 3):
            ref.add(tuple(c[i:i+4]))
    print(len(ref))
    #for i, r in enumerate(ref):
    #    print(i)
    #    n = count(seqs, changes, r)
    #    if n > best:
    #        best = n
    return count(seqs, changes, ref)

print(solve2(inpt))

#results(solve1(test), solve1(inpt), solve2(test), solve2(inpt))
