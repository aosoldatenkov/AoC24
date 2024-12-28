import itertools as it
import re
import math
from functools import cache

with open("test") as f_test, open("input") as f_inp:
    test = f_test.read()
    inpt = f_inp.read()

def results(t1, i1, t2, i2):
    print("Part I:\n  test:", t1, "\n  input:", i1, "\nPart II:\n  test:", t2, "\n  input:", i2)

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

wmap = [[a for a in l] for l in inpt.splitlines()]

def race(inp, xs, ys, xe, ye):
    pos = {(xs, ys): 0}
    new = {(xs, ys)}
    while len(new) > 0:
        px, py = new.pop()
        for dx, dy in dirs:
            x, y = px + dx, py + dy
            if wmap[y][x] != '#' and ((x, y) not in pos or pos[(x, y)] > pos[(px, py)] + 1):
                pos[(x, y)] = pos[(px, py)] + 1
                new.add((x, y))
    return pos

@cache
def race2(xs, ys, xe, ye):
    pos = {(xs, ys): 0}
    new = {(xs, ys)}
    while len(new) > 0:
        px, py = new.pop()
        for dx, dy in dirs:
            x, y = px + dx, py + dy
            if wmap[y][x] != '#' and ((x, y) not in pos or pos[(x, y)] > pos[(px, py)] + 1):
                pos[(x, y)] = pos[(px, py)] + 1
                new.add((x, y))
    return pos[(xe, ye)]

def solve1(inp):
    inp = [[a for a in l] for l in inp.splitlines()]
    ys = min(i for i in range(len(inp)) if 'S' in inp[i])
    xs = inp[ys].index('S')
    ye = min(i for i in range(len(inp)) if 'E' in inp[i])
    xe = inp[ye].index('E')
    h = len(inp)
    w = len(inp[0])
    base = race(inp, xs, ys, xe, ye)
    count = 0
    print(w, h)
    for j in range(1, h - 1):
        for i in range(1, w - 1):
            print(i, j, end='\r')
            if inp[j][i] != '#' or all(inp[j + dy][i + dx] == '#' for dx, dy in dirs):
                continue
            for a, b in dirs:
                if 0 < i + a < w - 1 and 0 < j + b < h - 1 and inp[j + b][i + a] != '#':
                    r1 = min(base[(i + dx, j + dy)] for dx, dy in dirs if (i + dx, j + dy) in base) + 1
                    second = race(inp, i + a, j + b, xe, ye)
                    r2 = second[(xe, ye)]
                    dif = base[(xe, ye)] - r1 - r2 - 1
                    if dif >= 20:
                        #print(dif)
                        count += 1
    print('')
    return count

def solve2(inp):
    wmap = [[a for a in l] for l in inp.splitlines()]
    inp = [[a for a in l] for l in inp.splitlines()]
    
    ys = min(i for i in range(len(inp)) if 'S' in inp[i])
    xs = inp[ys].index('S')
    ye = min(i for i in range(len(inp)) if 'E' in inp[i])
    xe = inp[ye].index('E')
    h = len(inp)
    w = len(inp[0])
    base = race2(xs, ys, xe, ye)
    count = 0
    print(w, h)
    for j in range(1, h - 1):
        for i in range(1, w - 1):
            print(i, j, end='\r')
            if inp[j][i] == '#':# or all(inp[j + dy][i + dx] == '#' for dx, dy in dirs):
                continue
            for a, b in it.product(range(1, w - 1), range(1, h - 1)):
                if abs(i - a) + abs(j - b) <= 20 and inp[b][a] != '#':
                    r1 = race2(xs, ys, i, j) #min(base[(i + dx, j + dy)] for dx, dy in dirs if (i + dx, j + dy) in base)
                    r2 = race2(a, b, xe, ye)
                    dif = base - r1 - r2 - (abs(i - a) + abs(j - b))
                    if dif >= 100:
#                        print(i, j, a, b)
                        count += 1
    print('')
    return count

print(solve2(inpt))

#results(solve1(test), solve1(inpt), solve2(test), solve2(inpt))
