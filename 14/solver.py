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
    n = list(map(int, re.findall(r'-?\d+', inp)))
    px, py, vx, vy = n[0::4], n[1::4], n[2::4], n[3::4]
    h = 103
    w = 101
    pos = [((px[i] + 100 * vx[i]) % w, (py[i] + 100 * vy[i]) % h) for i in range(len(px))]
    n1 = sum(1 for p in pos if p[0] < w // 2 and p[1] < h // 2)
    n2 = sum(1 for p in pos if p[0] > w // 2 and p[1] < h // 2)
    n3 = sum(1 for p in pos if p[0] < w // 2 and p[1] > h // 2)
    n4 = sum(1 for p in pos if p[0] > w // 2 and p[1] > h // 2)
    return n1 * n2 * n3 * n4

def solve2(inp):
    n = list(map(int, re.findall(r'-?\d+', inp)))
    px, py, vx, vy = n[0::4], n[1::4], n[2::4], n[3::4]
    h = 103
    w = 101
    maxx = []
    for t in range(101 * 103):
        pos = [((px[i] + t * vx[i]) % w, (py[i] + t * vy[i]) % h) for i in range(len(px))]
        max_l = 1
        for x, y in it.product(range(w), range(h)):
            ll = [u for u in range(10) if (x + u, y) not in pos]
            ll.append(10)
            if min(ll) > max_l:
                max_l = min(ll)
                break
        if max_l > 2:
            print('t=', t, 'l=', max_l)
        maxx.append(max_l)
    return 0

print(solve2(inpt))

#results(solve1(test), solve1(inpt), solve2(test), solve2(inpt))
