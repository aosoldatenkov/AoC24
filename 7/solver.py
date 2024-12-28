import itertools as it
import re
import math

with open("test") as f_test, open("input") as f_inp:
    test = f_test.read()
    inpt = f_inp.read()

def results(t1, i1, t2, i2):
    print("Part I:\n  test:", t1, "\n  input:", i1, "\nPart II:\n  test:", t2, "\n  input:", i2)

def solve1(inp):
    inp = inp.splitlines()
    count = 0
    for l in inp:
        left, right = l.split(':')
        res = int(left)
        vals = [int(a) for a in right.split()]
        for ops in it.product([0, 1], repeat=len(vals)):
            if ops[0] == 1:
                continue
            r = 0
            for i in range(len(vals)):
                r = (r + vals[i]) if ops[i] == 0 else (r * vals[i])
            if r == res:
                count += res
                break
    return count

def compute(vals):
    if len(vals) == 1:
        yield int(vals[0])
        return
    for v in compute(vals[:-1]):
        w = int(vals[-1])
        yield v + w
        yield v * w
        yield v * (10 ** len(vals[-1])) + w

def solve2(inp):
    inp = inp.splitlines()
    count = 0
    for l in inp:
        left, right = l.split(':')
        res = int(left)
        vals = [a for a in right.split()]
        for v in compute(vals):
            if v == res:
                count += res
                break
    return count

results(solve1(test), solve1(inpt), solve2(test), solve2(inpt))
