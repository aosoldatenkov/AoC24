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
    blocks = [b.splitlines() for b in inp.split('\n\n')]
    keys = []
    locks = []
    for i, b in enumerate(blocks):
        if b[0][0] == '#':
            locks.append(i)
        else:
            keys.append(i)
    count = 0
    for i, j in it.product(locks, keys):
        l = blocks[i]
        k = blocks[j]
        h = min(len(l), len(k))
        w = min(len(l[0]), len(k[0]))
        fit = True
        for x, y in it.product(range(w), range(h)):
            if l[y][x] == k[y][x] == '#':
                fit = False
                break
        if fit:
            count += 1
    return count
    
def solve2(inp):
    return 0

print(solve1(inpt))

