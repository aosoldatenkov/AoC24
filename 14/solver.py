import itertools as it
import re
from collections import Counter

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
    pos = [(px[i], py[i]) for i in range(len(px))]
    for t in range(101 * 103):
        counts = Counter((p[0] // 5, p[1] // 5) for p in pos)
        m = counts.most_common(1)[0]
        if m[1] > 20:
            return t
        pos = [((pos[i][0] + vx[i]) % w, (pos[i][1] + vy[i]) % h) for i in range(len(px))]
    return 0

results(solve1(test), solve1(inpt), solve2(test), solve2(inpt))
