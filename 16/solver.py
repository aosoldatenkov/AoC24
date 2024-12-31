import itertools as it
import re
import math
from functools import cache

with open("test") as f_test, open("input") as f_inp:
    test = f_test.read()
    inpt = f_inp.read()

def results(t1, i1, t2, i2):
    print("Part I:\n  test:", t1, "\n  input:", i1, "\nPart II:\n  test:", t2, "\n  input:", i2)

def locate(m, s):
    pos = []
    for y, l in enumerate(m):
        for x, n in enumerate(l):
            if n == s:
                pos.append((x, y))
    return pos

def solve1(inp):
    m = inp.splitlines()
    xs, ys = locate(m, 'S')[0]
    xe, ye = locate(m, 'E')[0]
    positions = {(xs, ys, -1, 0): 0}
    coords = {(xs, ys)}
    step = True
    cost = 2 ** 20
    finish = []
    active = {(xs, ys, -1, 0): 0}
    while step:
        step = False
        update = set()
        update = {}
        for p in active:
            value = active[p]
            if value >= cost:
                continue
            if p[0] == xe and p[1] == ye:
                if cost > value:
                    cost = value
                continue
            pp = (p[0] + p[2], p[1] + p[3], p[2], p[3])
            cc = (p[0] + p[2], p[1] + p[3])
            if m[pp[1]][pp[0]] != '#' and (pp not in update or update[pp] > value + 1):
                update[pp] = value + 1
            dirs = [(-1, 0), (1, 0)] if p[2] == 0 else [(0, -1), (0, 1)]
            for d in dirs:
                pp = (p[0], p[1], d[0], d[1])
                if pp not in update or update[pp] > value + 1000:
                    update[pp] = value + 1000
        active = {}
        for p in update:
            if p not in positions or positions[p] > update[p]:
                positions[p] = update[p]
                active[p] = update[p]
                step = True
    return cost
    
def solve2(inp):
    m = inp.splitlines()
    xs, ys = locate(m, 'S')[0]
    xe, ye = locate(m, 'E')[0]
    positions = {(xs, ys, 1, 0): (0, set())}
    coords = {(xs, ys)}
    step = True
    cost = 2 ** 20
    finish = []
    active = {(xs, ys, 1, 0): (0, set())}
    while step:
        step = False
        update = {}
        for p in active:
            value = active[p][0]
            if value > cost:
                continue
            if p[0] == xe and p[1] == ye:
                if cost > value:
                    cost = value
                continue
            pp = (p[0] + p[2], p[1] + p[3], p[2], p[3])
            if m[pp[1]][pp[0]] != '#':
                if pp not in update:
                    update[pp] = (value + 1, {p})
                elif update[pp][0] > value + 1:
                    update[pp] = (value + 1, {p})
                elif update[pp][0] == value + 1:
                    update[pp][1].add(p)
            dirs = [(-1, 0), (1, 0)] if p[2] == 0 else [(0, -1), (0, 1)]
            for d in dirs:
                pp = (p[0], p[1], d[0], d[1])
                if pp not in update:
                    update[pp] = (value + 1000, {p})
                elif update[pp][0] > value + 1000:
                    update[pp] = (value + 1000, {p})
                elif update[pp][0] == value + 1000:
                    update[pp][1].add(p)
        active = {}
        for p in update:
            if p not in positions or positions[p][0] > update[p][0]:
                positions[p] = update[p]
                active[p] = update[p]
                step = True
            elif positions[p][0] == update[p][0]:
                positions[p][1].update(update[p][1])
                active[p] = positions[p]
                step = True
    current = {p for p in positions if p[0] == xe and p[1] == ye and positions[p][0] == cost}
    coords = set()
    while len(current) > 0:
        p = current.pop()
        coords.add((p[0], p[1]))
        for pp in positions[p][1]:
            current.add(pp)
    return len(coords)

results(solve1(test), solve1(inpt), solve2(test), solve2(inpt))
