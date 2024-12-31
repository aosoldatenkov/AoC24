import itertools as it
import time
from functools import cache

try: 
    with open("test") as f_test: test = f_test.read()
except: test = None
try:
    with open("input") as f_inp: inpt = f_inp.read()
except: inpt = None

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

@cache
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
        vals = tuple(a for a in right.split())
        for v in compute(vals):
            if v == res:
                count += res
                break
    return count

def run():
    if test:
        t1 = time.time()
        r1 = solve1(test)
        t2 = time.time()
        r2 = solve2(test)
        t3 = time.time()
        assert r1 == 3749, r2 == 11387
        print("Test I:", r1, f'{t2 - t1:10.3f}s', "\nTest II:", r2, f'{t3 - t2:10.3f}s')
    if inpt:
        t1 = time.time()
        r1 = solve1(inpt)
        t2 = time.time()
        r2 = solve2(inpt)
        t3 = time.time()
        assert r1 == 5512534574980, r2 == 328790210468594
        print("Part I:", r1, f'{t2 - t1:10.3f}s', "\nPart II:", r2, f'{t3 - t2:10.3f}s')

run()

